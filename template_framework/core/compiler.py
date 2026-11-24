"""
Project Compiler for HyperFrames Videos.
Transforms an episode_config.json into index.html and compositions/*.html
"""

import os
import json
from .tokens import load_tokens, generate_common_css
from .archetypes import get_archetype_generator

class ProjectCompiler:
    def __init__(self, project_dir, tokens_path=None):
        self.project_dir = os.path.abspath(project_dir)
        self.tokens = load_tokens(tokens_path)

    def compile(self, config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        l = self.tokens["layout"]
        c = self.tokens["colors"]
        g = self.tokens["grid"]

        total_duration = config.get("totalDuration", 92.0)
        audio_src = config.get("audio", "assets/audio_master_v5_loud.mp3")
        scenes = config.get("scenes", [])

        # 1. Compile index.html
        scene_divs = []
        for idx, s in enumerate(scenes):
            scene_file = s.get("file", s["id"] + ".html")
            scene_chapter = s.get("chapter", f"Scene {idx+1}")
            scene_div = f"""      <!-- Scene {idx+1}: {scene_chapter} ({s['start']}s - {s['start']+s['duration']}s) -->
      <div
        id="{s['id']}"
        data-composition-id="{s['id']}"
        data-composition-src="compositions/{scene_file}"
        data-start="{s['start']}"
        data-duration="{s['duration']}"
        data-track-index="{idx}"
        data-track-kind="graphics"
        data-width="{l['width']}"
        data-height="{l['height']}"
      ></div>"""
            scene_divs.append(scene_div)

        scenes_html = "\n\n".join(scene_divs)

        index_html = f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={l['width']}, height={l['height']}" />
    <title>{config.get('title', 'HyperFrames Video')}</title>
    <script src="assets/gsap.min.js"></script>
    <style>
      {generate_common_css(self.tokens)}
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
        src="{audio_src}"
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

        index_output_path = os.path.join(self.project_dir, "index.html")
        with open(index_output_path, "w", encoding="utf-8") as f:
            f.write(index_html)
        print(f"✓ Generated index.html -> {index_output_path}")

        # 2. Compile compositions/*.html
        comps_dir = os.path.join(self.project_dir, "compositions")
        os.makedirs(comps_dir, exist_ok=True)

        for s in scenes:
            scene_type = s.get("type", "grid_cards")
            gen = get_archetype_generator(scene_type)
            if not gen:
                print(f"Warning: No archetype generator for type '{scene_type}', skipping {s['id']}")
                continue

            scene_html = gen(s["id"], s, duration=s.get("duration", 10.0))
            scene_filename = s.get("file", f"{s['id']}.html")
            scene_path = os.path.join(comps_dir, scene_filename)
            with open(scene_path, "w", encoding="utf-8") as f:
                f.write(scene_html)
            print(f"✓ Generated composition -> {scene_path} (Type: {scene_type})")

        print("✓ Compilation complete!")
