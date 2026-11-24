#!/usr/bin/env python3
"""
Pangmao Video Studio - Warm Tech Video Framework Engine
Generates and manages HyperFrames video projects based on the '亚里' warm paper editorial style.
"""

import os
import sys
import json
import argparse
import subprocess

FRAMEWORK_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(FRAMEWORK_DIR)

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_common_css(tokens):
    c = tokens["colors"]
    t = tokens["typography"]
    s = tokens["shadows"]
    l = tokens["layout"]
    
    return f"""
@font-face {{
  font-family: "PingFang SC";
  src: local("PingFang SC");
  font-display: swap;
}}
* {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}
.scene-root {{
  position: absolute;
  inset: 0;
  width: {l['width']}px;
  height: {l['height']}px;
  overflow: hidden;
  font-family: {t['fontFamily']};
  color: {c['textPrimary']};
  -webkit-font-smoothing: antialiased;
}}

/* Top Navigation Header */
.header-nav {{
  position: absolute;
  top: {l['headerTop']};
  left: {l['headerLeft']};
  display: flex;
  align-items: baseline;
  gap: 12px;
  z-index: 50;
}}
.nav-num {{
  font-size: {t['chapterNumberSize']};
  font-weight: 800;
  color: {c['accentGold']};
  letter-spacing: 0.02em;
}}
.nav-title {{
  font-size: {t['chapterTitleSize']};
  font-weight: 800;
  color: {c['textPrimary']};
  letter-spacing: 0.04em;
}}

/* Brand Canopy Arch */
.header-brand {{
  position: absolute;
  top: 42px;
  right: {l['headerRight']};
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 50;
}}
.brand-arch {{
  width: 32px;
  height: 6px;
  border-top: 3.5px solid {c['accentGold']};
  border-radius: 50%;
  margin-bottom: 2px;
}}
.brand-title {{
  font-size: {t['brandTitleSize']};
  font-weight: 900;
  color: {c['textPrimary']};
  letter-spacing: 0.16em;
}}

/* Presenter Avatar HUD */
.avatar-hud {{
  position: absolute;
  bottom: {l['avatarBottom']};
  left: {l['avatarLeft']};
  width: 114px;
  height: 114px;
  border-radius: 50%;
  background: #FAF7F0;
  border: 4px solid #FFFFFF;
  box-shadow: {s['avatarHud']};
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 60;
}}
.avatar-hud img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
}}

/* Subtitle HUD */
.subtitle-hud {{
  position: absolute;
  bottom: {l['subtitleBottom']};
  left: {l['subtitlePaddingX']};
  right: {l['subtitlePaddingX']};
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 60;
  pointer-events: none;
}}
.subtitle-text {{
  font-size: {t['subtitleSize']};
  font-weight: 800;
  color: {c['textPrimary']};
  letter-spacing: 0.04em;
  text-align: center;
  line-height: 1.35;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.9);
}}
.sub-hl {{
  color: {c['accentGold']};
  font-weight: 900;
}}

/* Hand Pointer Cursor */
.hand-pointer {{
  position: absolute;
  width: 54px;
  height: 54px;
  pointer-events: none;
  z-index: 100;
  filter: drop-shadow({s['pointerShadow']});
  opacity: 0;
}}
"""

def generate_index_html(config, tokens):
    c = tokens["colors"]
    g = tokens["grid"]
    l = tokens["layout"]
    scenes = config["scenes"]
    audio = config.get("audio", "assets/audio.mp3")
    total_duration = config.get("totalDuration", 92)
    
    scene_divs = []
    for idx, s in enumerate(scenes):
        div = f"""      <!-- Scene {idx+1}: {s['chapter']} ({s['start']}s - {s['start']+s['duration']}s) -->
      <div
        id="{s['id']}"
        data-composition-id="{s['id']}"
        data-composition-src="compositions/{s['file']}"
        data-start="{s['start']}"
        data-duration="{s['duration']}"
        data-track-index="{idx}"
        data-track-kind="graphics"
        data-width="{l['width']}"
        data-height="{l['height']}"
      ></div>"""
        scene_divs.append(div)
        
    scenes_html = "\n\n".join(scene_divs)
    
    return f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={l['width']}, height={l['height']}" />
    <title>{config.get('title', 'Pangmao Video Studio')}</title>
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face {{
        font-family: "PingFang SC";
        src: local("PingFang SC");
        font-display: swap;
      }}
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}
      html, body {{
        margin: 0;
        width: {l['width']}px;
        height: {l['height']}px;
        overflow: hidden;
        background: {c['background']};
        font-family: {tokens['typography']['fontFamily']};
        color: {c['textPrimary']};
        -webkit-font-smoothing: antialiased;
      }}
      #root {{
        position: relative;
        width: {l['width']}px;
        height: {l['height']}px;
        overflow: hidden;
        background: {c['background']};
      }}
      .paper-bg {{
        position: absolute;
        inset: 0;
        background: {c['backgroundRadial']};
        pointer-events: none;
        z-index: 0;
      }}
      .ambient-grid {{
        position: absolute;
        inset: 0;
        background-image: 
          linear-gradient({c['gridLine']} {g['lineWidth']}, transparent {g['lineWidth']}),
          linear-gradient(90deg, {c['gridLine']} {g['lineWidth']}, transparent {g['lineWidth']});
        background-size: {g['size']};
        pointer-events: none;
        z-index: 1;
      }}
    </style>
  </head>
  <body>
    <div
      id="root"
      data-composition-id="main"
      data-start="0"
      data-duration="{total_duration}"
      data-width="{l['width']}"
      data-height="{l['height']}"
      data-fps="{l['fps']}"
      data-hold
    >
      <div class="paper-bg"></div>
      <div class="ambient-grid"></div>

      <audio
        id="voiceover"
        src="{audio}"
        data-start="0"
        data-duration="{total_duration}"
        data-volume="1"
      ></audio>

{scenes_html}
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""

def main():
    parser = argparse.ArgumentParser(description="Pangmao Video Studio Builder")
    parser.add_argument("--config", default=os.path.join(FRAMEWORK_DIR, "episode_config.v4.json"), help="Path to episode config")
    parser.add_argument("--build-index", action="store_true", help="Compile index.html")
    parser.add_argument("--snapshot", action="store_true", help="Take verification snapshots")
    parser.add_argument("--render", action="store_true", help="Render final MP4")
    parser.add_argument("--out", default="out/pangmao_skills_v4.mp4", help="Output MP4 file path")
    
    args = parser.parse_args()
    
    tokens = load_json(os.path.join(FRAMEWORK_DIR, "design_tokens.json"))
    if not os.path.exists(args.config):
        print(f"Config file not found: {args.config}")
        sys.exit(1)
        
    config = load_json(args.config)
    print(f"Loaded config: {config.get('title')}")
    
    # 1. Build index.html
    index_content = generate_index_html(config, tokens)
    index_path = os.path.join(PROJECT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"✓ Compiled {index_path}")
    
    env = os.environ.copy()
    bin_dir = "/Users/rongxianpang/Desktop/video-project/bin"
    venv_bin = "/Users/rongxianpang/Desktop/video-project/.venv/bin"
    env["PATH"] = f"{bin_dir}:{venv_bin}:" + env.get("PATH", "")
    env["HYPERFRAMES_BROWSER_PATH"] = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    # 2. Snapshot if requested
    if args.snapshot:
        print("Taking verification snapshots...")
        cmd = ["npx", "--yes", "hyperframes@0.9.7", "snapshot", "--at", "11.0,18.0,28.0,52.0,64.0,78.0", "-o", "out/snapshots_v4"]
        subprocess.run(cmd, cwd=PROJECT_DIR, env=env, check=True)
        print("✓ Snapshots saved to out/snapshots_v4")
        
    # 3. Render if requested
    if args.render:
        print(f"Rendering final MP4 to {args.out}...")
        cmd = ["npx", "--yes", "hyperframes@0.9.7", "render", ".", "-o", args.out, "-f", "30"]
        subprocess.run(cmd, cwd=PROJECT_DIR, env=env, check=True)
        print(f"✓ Render complete: {args.out}")

if __name__ == "__main__":
    main()
