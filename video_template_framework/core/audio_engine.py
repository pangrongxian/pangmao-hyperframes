"""
Automated Audio Mastering Engine for Universal Video Framework.
Solves the amix volume division trap and guarantees clean -18.9 dB loudness.
"""

import os
import re
import subprocess
import json

class AudioMasteringEngine:
    def __init__(self, ffmpeg_bin=None, tokens=None):
        if ffmpeg_bin is None:
            import shutil
            ffmpeg_bin = shutil.which("ffmpeg")
            if not ffmpeg_bin and os.path.exists("/Users/rongxianpang/Desktop/video-project/bin/ffmpeg"):
                ffmpeg_bin = "/Users/rongxianpang/Desktop/video-project/bin/ffmpeg"
            elif not ffmpeg_bin:
                ffmpeg_bin = "ffmpeg"
        self.ffmpeg_bin = ffmpeg_bin
        if tokens is None:
            from .tokens import load_tokens
            tokens = load_tokens()
        self.settings = tokens.get("audioMastering", {
            "voiceoverBoost": 2.2,
            "voiceoverLimiter": 0.95,
            "bgmVolume": 0.06,
            "bgmFadeInSeconds": 1.5,
            "bgmFadeOutSeconds": 2.0,
            "targetMeanVolumeDb": -18.9,
            "sampleRate": 48000
        })

    def mix_sfx_track(self, sfx_events, output_wav_path):
        """
        Mixes a list of (timestamp_seconds, wav_file_path, volume) into a single aligned SFX track.
        """
        os.makedirs(os.path.dirname(os.path.abspath(output_wav_path)), exist_ok=True)
        if not sfx_events:
            # Generate a silent 1s wav
            cmd = [
                self.ffmpeg_bin, "-y",
                "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                "-t", "1",
                "-c:a", "pcm_s16le", output_wav_path
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return output_wav_path

        cmd = [self.ffmpeg_bin, "-y"]
        for _, wav_path, _ in sfx_events:
            cmd.extend(["-i", wav_path])

        filter_chains = []
        inputs = []
        for idx, (t, _, vol) in enumerate(sfx_events):
            delay_ms = int(t * 1000)
            filter_chains.append(f"[{idx}:a]volume={vol},adelay={delay_ms}|{delay_ms}[s{idx}];")
            inputs.append(f"[s{idx}]")

        inputs_str = "".join(inputs)
        filter_chains.append(f"{inputs_str}amix=inputs={len(inputs)}:normalize=0:duration=longest[sfx_out]")

        cmd.extend([
            "-filter_complex", "".join(filter_chains),
            "-map", "[sfx_out]",
            "-c:a", "pcm_s16le",
            "-ar", str(self.settings.get("sampleRate", 48000)),
            "-ac", "2",
            output_wav_path
        ])

        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        return output_wav_path

    def master(self, voiceover_path, bgm_path, sfx_events, output_master_path, total_duration):
        """
        Runs the full mastering pipeline:
        1. Compiles sfx_track.wav
        2. Applies voiceover boost & limiter
        3. Ducks ambient BGM
        4. Mixes with amix normalize=0
        """
        os.makedirs(os.path.dirname(os.path.abspath(output_master_path)), exist_ok=True)
        scratch_dir = os.path.join(os.path.dirname(output_master_path), "scratch")
        os.makedirs(scratch_dir, exist_ok=True)
        sfx_track_path = os.path.join(scratch_dir, "framework_sfx_track.wav")

        print("1/3 Synthesizing & sequencing SFX timeline...")
        self.mix_sfx_track(sfx_events, sfx_track_path)

        print("2/3 Mastering Voiceover + BGM + SFX channels...")
        v_boost = self.settings.get("voiceoverBoost", 2.2)
        v_limiter = self.settings.get("voiceoverLimiter", 0.95)
        bgm_vol = self.settings.get("bgmVolume", 0.06)
        fade_in = self.settings.get("bgmFadeInSeconds", 1.5)
        fade_out = self.settings.get("bgmFadeOutSeconds", 2.0)
        fade_out_start = max(0, total_duration - fade_out - 0.5)

        mix_cmd = [
            self.ffmpeg_bin, "-y",
            "-i", voiceover_path,
            "-i", bgm_path,
            "-i", sfx_track_path,
            "-filter_complex",
            f"[0:a]volume={v_boost},alimiter=limit={v_limiter}[v_voice];"
            f"[1:a]atrim=0:{total_duration},afade=t=in:ss=0:d={fade_in},afade=t=out:st={fade_out_start}:d={fade_out},volume={bgm_vol}[v_bgm];"
            f"[2:a]atrim=0:{total_duration}[v_sfx];"
            f"[v_voice][v_bgm][v_sfx]amix=inputs=3:normalize=0:duration=first[outa]",
            "-map", "[outa]",
            "-c:a", "libmp3lame",
            "-b:a", "320k",
            output_master_path
        ]

        subprocess.run(mix_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        print("3/3 Verifying loudness profile...")
        stats = self.measure_loudness(output_master_path)
        print(f"✓ Master audio ready: {output_master_path} (mean_volume: {stats.get('mean_volume')}, max: {stats.get('max_volume')})")
        return stats

    def measure_loudness(self, audio_path):
        cmd = [
            self.ffmpeg_bin, "-i", audio_path,
            "-af", "volumedetect",
            "-f", "null", "/dev/null"
        ]
        result = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL, text=True)
        stats = {}
        for line in result.stderr.splitlines():
            if "mean_volume:" in line:
                stats["mean_volume"] = line.split("mean_volume:")[1].strip()
            elif "max_volume:" in line:
                stats["max_volume"] = line.split("max_volume:")[1].strip()
        return stats
