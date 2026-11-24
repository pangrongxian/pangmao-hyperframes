import os

base_dir = "/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes"

# -------------------------------------------------------------
# 1. INDEX.HTML
# -------------------------------------------------------------
index_html = '''<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>胖猫AI - 1分钟学会Agent Skills手搓网站 (v4 模版风格精制版)</title>
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face {
        font-family: "PingFang SC";
        src: local("PingFang SC");
        font-display: swap;
      }
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      html, body {
        margin: 0;
        width: 1920px;
        height: 1080px;
        overflow: hidden;
        background: #F7F5EE;
        font-family: "PingFang SC", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: #1A1C20;
        -webkit-font-smoothing: antialiased;
      }
      #root {
        position: relative;
        width: 1920px;
        height: 1080px;
        overflow: hidden;
        background: #F7F5EE;
      }

      /* Subtle Paper Texture Radial Background */
      .paper-bg {
        position: absolute;
        inset: 0;
        background: radial-gradient(ellipse at 50% 40%, #FCFAF5 0%, #F5F1E6 100%);
        pointer-events: none;
        z-index: 0;
      }

      /* Architectural Subtle Grid (Exact Homage to Template) */
      .ambient-grid {
        position: absolute;
        inset: 0;
        background-image: 
          linear-gradient(rgba(185, 170, 150, 0.22) 1.5px, transparent 1.5px),
          linear-gradient(90deg, rgba(185, 170, 150, 0.22) 1.5px, transparent 1.5px);
        background-size: 54px 54px;
        pointer-events: none;
        z-index: 1;
      }
    </style>
  </head>
  <body>
    <div
      id="root"
      data-composition-id="main"
      data-start="0"
      data-duration="92"
      data-width="1920"
      data-height="1080"
      data-fps="30"
      data-hold
    >
      <div class="paper-bg"></div>
      <div class="ambient-grid"></div>

      <!-- Narration Audio Track -->
      <audio
        id="voiceover"
        src="assets/audio.mp3"
        data-start="0"
        data-duration="91.7"
        data-volume="1"
      ></audio>

      <!-- Scene 1: 0 - 14.0s Hook & 4-Category Squircle Skills Grid -->
      <div
        id="scene1"
        data-composition-id="scene1"
        data-composition-src="compositions/scene1_hook.html"
        data-start="0"
        data-duration="14.0"
        data-track-index="0"
        data-track-kind="graphics"
        data-width="1920"
        data-height="1080"
      ></div>

      <!-- Scene 2: 14.0 - 24.5s 151W+ Skills Arena Leaderboard Table -->
      <div
        id="scene2"
        data-composition-id="scene2"
        data-composition-src="compositions/scene2_70k.html"
        data-start="14.0"
        data-duration="10.5"
        data-track-index="1"
        data-track-kind="graphics"
        data-width="1920"
        data-height="1080"
      ></div>

      <!-- Scene 3: 24.5 - 37.0s Dual-Lane Process Flow Animation & Cursor Drop -->
      <div
        id="scene3"
        data-composition-id="scene3"
        data-composition-src="compositions/scene3_install.html"
        data-start="24.5"
        data-duration="12.5"
        data-track-index="2"
        data-track-kind="graphics"
        data-width="1920"
        data-height="1080"
      ></div>

      <!-- Scene 4: 37.0 - 57.8s Workflow Milestone & PRD Checklist & Auto Coding -->
      <div
        id="scene4"
        data-composition-id="scene4"
        data-composition-src="compositions/scene4_product.html"
        data-start="37.0"
        data-duration="20.8"
        data-track-index="3"
        data-track-kind="graphics"
        data-width="1920"
        data-height="1080"
      ></div>

      <!-- Scene 5: 57.8 - 71.4s 3-Minute Live App Showcase & Feature Waves -->
      <div
        id="scene5"
        data-composition-id="scene5"
        data-composition-src="compositions/scene5_app.html"
        data-start="57.8"
        data-duration="13.6"
        data-track-index="4"
        data-track-kind="graphics"
        data-width="1920"
        data-height="1080"
      ></div>

      <!-- Scene 6: 71.4 - 92.0s Top 10 High-Frequency Skills & Grand Outro -->
      <div
        id="scene6"
        data-composition-id="scene6"
        data-composition-src="compositions/scene6_outro.html"
        data-start="71.4"
        data-duration="20.6"
        data-track-index="5"
        data-track-kind="graphics"
        data-width="1920"
        data-height="1080"
      ></div>
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      window.__timelines["main"] = gsap.timeline({ paused: true });
    </script>
  </body>
</html>
'''

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
print("Updated index.html")
