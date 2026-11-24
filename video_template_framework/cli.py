#!/usr/bin/env python3
"""
Pangmao Video Studio - Universal Video Template Framework CLI
通用视频制作神器命令行工具
"""

import os
import sys
import json
import shutil
import argparse
import subprocess

FRAMEWORK_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, FRAMEWORK_DIR)

from core.compiler import ProjectCompiler
from core.audio_engine import AudioMasteringEngine
from core.tokens import load_tokens

def get_env():
    env = os.environ.copy()
    bin_dir = "/Users/rongxianpang/Desktop/video-project/bin"
    venv_bin = "/Users/rongxianpang/Desktop/video-project/.venv/bin"
    env["PATH"] = f"{bin_dir}:{venv_bin}:" + env.get("PATH", "")
    env["HYPERFRAMES_BROWSER_PATH"] = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    return env

def cmd_init(args):
    target = os.path.abspath(args.target_dir)
    print(f"Scaffolding new video project at: {target}")
    os.makedirs(target, exist_ok=True)
    os.makedirs(os.path.join(target, "compositions"), exist_ok=True)
    os.makedirs(os.path.join(target, "assets"), exist_ok=True)
    os.makedirs(os.path.join(target, "out"), exist_ok=True)

    # Copy assets
    framework_assets = os.path.join(FRAMEWORK_DIR, "assets")
    if os.path.exists(framework_assets):
        shutil.copytree(framework_assets, os.path.join(target, "assets"), dirs_exist_ok=True)
        print("✓ Copied default assets (GSAP, SFX library, BGM)")

    # Copy tokens
    shutil.copyfile(
        os.path.join(FRAMEWORK_DIR, "design_tokens.json"),
        os.path.join(target, "design_tokens.json")
    )
    print("✓ Copied design_tokens.json")

    # Copy template config
    tpl_config = os.path.join(FRAMEWORK_DIR, "templates", "episode_config.template.json")
    if not os.path.exists(tpl_config):
        tpl_config = os.path.join(FRAMEWORK_DIR, "episode_config.template.json")
    shutil.copyfile(tpl_config, os.path.join(target, "episode_config.json"))
    print("✓ Created episode_config.json")

    print("\n🎉 Project initialized successfully!")
    print(f"Next steps:")
    print(f"  cd {target}")
    print(f"  python3 {os.path.abspath(__file__)} build")
    print(f"  python3 {os.path.abspath(__file__)} render")

def cmd_build(args):
    project_dir = os.path.abspath(args.project_dir)
    config_path = os.path.abspath(args.config) if args.config else os.path.join(project_dir, "episode_config.json")
    if not os.path.exists(config_path):
        # Fallback to episode_config.v4.json or pangmao_v5 if in root
        fallback = os.path.join(project_dir, "episode_config.pangmao_v5.json")
        if os.path.exists(fallback):
            config_path = fallback
        else:
            print(f"Error: Config file not found at {config_path}")
            sys.exit(1)

    print(f"Compiling project from config: {config_path}")
    compiler = ProjectCompiler(project_dir)
    compiler.compile(config_path)

def cmd_audio(args):
    project_dir = os.path.abspath(args.project_dir)
    config_path = os.path.abspath(args.config) if args.config else os.path.join(project_dir, "episode_config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    voiceover = config.get("voiceover", "assets/v4_original_voice.mp3")
    bgm = config.get("bgm", "assets/bgm/dreamer.mp3")
    output_audio = config.get("audio", "assets/audio_master_v5_loud.mp3")
    total_duration = config.get("totalDuration", 92.0)
    sfx_events = config.get("sfx_events", [])

    print(f"Mastering audio: voiceover={voiceover}, bgm={bgm}, total_duration={total_duration}s")
    engine = AudioMasteringEngine()
    engine.master(
        os.path.join(project_dir, voiceover),
        os.path.join(project_dir, bgm),
        sfx_events,
        os.path.join(project_dir, output_audio),
        total_duration
    )

def cmd_snapshot(args):
    project_dir = os.path.abspath(args.project_dir)
    env = get_env()
    out_dir = os.path.join(project_dir, args.out)
    os.makedirs(out_dir, exist_ok=True)
    cmd = [
        "npx", "--yes", "hyperframes@0.9.7", "snapshot",
        "--at", args.at,
        "-o", args.out
    ]
    print(f"Executing: {' '.join(cmd)}")
    subprocess.run(cmd, cwd=project_dir, env=env, check=True)
    print(f"✓ Snapshots saved to {out_dir}")

def cmd_render(args):
    project_dir = os.path.abspath(args.project_dir)
    env = get_env()
    out_path = os.path.join(project_dir, args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    cmd = [
        "npx", "--yes", "hyperframes@0.9.7", "render", ".",
        "-o", args.out,
        "-f", str(args.fps)
    ]
    print(f"Rendering MP4 video to {out_path}...")
    subprocess.run(cmd, cwd=project_dir, env=env, check=True)
    print(f"✓ Video successfully rendered: {out_path}")

def cmd_inspect(args):
    file_path = os.path.abspath(args.file)
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    env = get_env()
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size,bit_rate:stream=codec_name,width,height,r_frame_rate",
        "-of", "json", file_path
    ]
    res = subprocess.run(probe_cmd, capture_output=True, text=True, env=env, check=True)
    info = json.loads(res.stdout)
    print(json.dumps(info, indent=2))

    vol_cmd = [
        "ffmpeg", "-i", file_path,
        "-af", "volumedetect",
        "-f", "null", "/dev/null"
    ]
    vol_res = subprocess.run(vol_cmd, capture_output=True, text=True, env=env)
    for line in vol_res.stderr.splitlines():
        if "mean_volume:" in line or "max_volume:" in line:
            print(f"Audio Loudness: {line.strip()}")

def main():
    parser = argparse.ArgumentParser(description="Pangmao Video Studio - Universal Video Template Framework CLI")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # init
    p_init = subparsers.add_parser("init", help="Scaffold a new video project")
    p_init.add_argument("target_dir", help="Target project folder path")

    # build / generate
    p_build = subparsers.add_parser("build", aliases=["generate"], help="Compile episode config into index.html and scene compositions")
    p_build.add_argument("--project-dir", default=".", help="Project root directory")
    p_build.add_argument("--config", default=None, help="Path to episode_config.json")

    # master-audio
    p_audio = subparsers.add_parser("master-audio", aliases=["audio"], help="Run automated audio mastering (Voiceover + BGM + SFX)")
    p_audio.add_argument("--project-dir", default=".", help="Project root directory")
    p_audio.add_argument("--config", default=None, help="Path to episode_config.json")

    # snapshot
    p_snap = subparsers.add_parser("snapshot", help="Capture timestamp snapshots for verification")
    p_snap.add_argument("--project-dir", default=".", help="Project root directory")
    p_snap.add_argument("--at", default="11.0,18.0,28.0,52.0,64.0,78.0", help="Comma-separated timestamps")
    p_snap.add_argument("--out", default="out/snapshots", help="Output directory")

    # render
    p_render = subparsers.add_parser("render", help="Render final MP4 video")
    p_render.add_argument("--project-dir", default=".", help="Project root directory")
    p_render.add_argument("--out", default="out/output.mp4", help="Output MP4 filename")
    p_render.add_argument("--fps", type=int, default=30, help="Frames per second")

    # inspect
    p_inspect = subparsers.add_parser("inspect", help="Inspect video and audio properties of an MP4 file")
    p_inspect.add_argument("file", help="Path to MP4 file")

    args = parser.parse_args()

    if args.subcommand == "init":
        cmd_init(args)
    elif args.subcommand in ("build", "generate"):
        cmd_build(args)
    elif args.subcommand in ("master-audio", "audio"):
        cmd_audio(args)
    elif args.subcommand == "snapshot":
        cmd_snapshot(args)
    elif args.subcommand == "render":
        cmd_render(args)
    elif args.subcommand == "inspect":
        cmd_inspect(args)

if __name__ == "__main__":
    main()
