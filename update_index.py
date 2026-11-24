import os

base_dir = "/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes"

# 1. Update index.html
index_html = '''<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>胖猫AI - 1分钟学会Agent Skills手搓网站</title>
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
        background: #06080f;
        font-family: "PingFang SC", -apple-system, sans-serif;
        color: #f8fafc;
        -webkit-font-smoothing: antialiased;
      }
      #root {
        position: relative;
        width: 1920px;
        height: 1080px;
        overflow: hidden;
        background: #06080f;
      }

      /* Global Ambient Tech Lighting */
      .ambient-glow-1 {
        position: absolute;
        width: 800px;
        height: 800px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(14, 165, 233, 0.22) 0%, transparent 70%);
        top: -150px;
        right: -100px;
        pointer-events: none;
        z-index: 1;
      }
      .ambient-glow-2 {
        position: absolute;
        width: 700px;
        height: 700px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.18) 0%, transparent 70%);
        bottom: -150px;
        left: -100px;
        pointer-events: none;
        z-index: 1;
      }
      .ambient-grid {
        position: absolute;
        inset: 0;
        background-image: 
          linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
          linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
        background-size: 48px 48px;
        opacity: 0.6;
        mask-image: radial-gradient(circle at 50% 50%, black 40%, transparent 95%);
        -webkit-mask-image: radial-gradient(circle at 50% 50%, black 40%, transparent 95%);
        pointer-events: none;
        z-index: 1;
      }

      /* Top Header Brand Watermark */
      .header-brand {
        position: absolute;
        top: 36px;
        left: 48px;
        display: flex;
        align-items: center;
        gap: 14px;
        z-index: 50;
      }
      .brand-badge {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 8px 18px;
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 9999px;
        backdrop-filter: blur(16px);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
      }
      .brand-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #38bdf8;
        box-shadow: 0 0 10px #38bdf8;
      }
      .brand-name {
        font-size: 17px;
        font-weight: 800;
        letter-spacing: 0.05em;
        background: linear-gradient(135deg, #ffffff 40%, #93c5fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
      }
      .brand-sub {
        font-size: 13px;
        font-weight: 600;
        color: #94a3b8;
        letter-spacing: 0.05em;
      }

      /* Series Tag */
      .series-tag {
        position: absolute;
        top: 36px;
        right: 48px;
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 18px;
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 9999px;
        backdrop-filter: blur(12px);
        font-size: 14px;
        font-weight: 700;
        color: #94a3b8;
        z-index: 50;
      }
      .series-pill {
        background: linear-gradient(135deg, #38bdf8, #2563eb);
        color: #ffffff;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 13px;
        font-weight: 800;
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
    >
      <!-- Global Ambient Lighting -->
      <div class="ambient-glow-1"></div>
      <div class="ambient-glow-2"></div>
      <div class="ambient-grid"></div>

      <!-- Top Header Watermarks -->
      <div class="header-brand" data-layout-ignore>
        <div class="brand-badge">
          <div class="brand-dot"></div>
          <span class="brand-name">胖猫AI</span>
          <span class="brand-sub">| 超级个体实验室</span>
        </div>
      </div>
      <div class="series-tag" data-layout-ignore>
        <span class="series-pill">实操篇</span>
        <span>Agent Skills 从入门到精通 2026全新版</span>
      </div>

      <!-- Narration Audio Track (zh-CN-YunxiaNeural "星仔" voice) -->
      <audio
        id="voiceover"
        src="assets/audio.mp3"
        data-start="0"
        data-duration="91.7"
        data-volume="1"
      ></audio>

      <!-- Scene 1: 0 - 14.0s Hook & Dynamic Multi-Cut Feature Skills -->
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

      <!-- Scene 2: 14.0 - 24.5s 1,517,216+ Skills Counter & Vibe Coding -->
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

      <!-- Scene 3: 24.5 - 37.0s Brainstorming Skill Copy & Cursor Install Cut -->
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

      <!-- Scene 4: 37.0 - 57.8s Product Manager PRD & Next.js Auto Coding -->
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

      <!-- Scene 5: 57.8 - 71.4s Exclusive KidsLingo AI Web App Showcase -->
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

      <!-- Scene 6: 71.4 - 92.0s TOP 10 Skills Poster Auto-Scroll & Grand Outro -->
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

