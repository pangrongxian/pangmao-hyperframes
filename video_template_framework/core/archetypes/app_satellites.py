"""
Archetype 5: Product Live Showcase with 4 Floating Interactive Satellite Cards
"""

from ..components import render_header, render_presenter_hud, render_subtitle_hud, render_pointer

def generate_app_satellites_html(scene_id, config, duration=13.6):
    chapter_num = config.get("chapter_num", "05")
    chapter_title = config.get("chapter_title", "极速交付")
    brand_name = config.get("brand_name", "胖猫")
    app_url = config.get("app_url", "https://kidslingo.ai · 实时运行中")

    subtitles = config.get("subtitles", [
        {"start": 0.0, "text": "只需要 <span class='sub-hl'>3 分钟</span>，你的网站就做好了！"},
        {"start": 4.0, "text": "分级阅读、发音纠错、生词本，功能一应俱全！"}
    ])

    sub_timeline_js = []
    for s in subtitles:
        sub_timeline_js.append(f"""
    tl.call(() => {{
      const sub = document.getElementById("s5-sub");
      if (sub) sub.innerHTML = "{s['text']}";
    }}, null, {s['start']});
        """)

    return f"""<template>
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
    #root {{
      position: absolute;
      inset: 0;
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      font-family: "PingFang SC", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      color: #1A1C20;
    }}

    .header-nav {{
      position: absolute;
      top: 48px;
      left: 64px;
      display: flex;
      align-items: baseline;
      gap: 12px;
      z-index: 50;
    }}
    .nav-num {{
      font-size: 26px;
      font-weight: 800;
      color: #C58B35;
      letter-spacing: 0.02em;
    }}
    .nav-title {{
      font-size: 24px;
      font-weight: 800;
      color: #1E2024;
      letter-spacing: 0.04em;
    }}

    .header-brand {{
      position: absolute;
      top: 42px;
      right: 68px;
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 50;
    }}
    .brand-arch {{
      width: 32px;
      height: 6px;
      border-top: 3.5px solid #C58B35;
      border-radius: 50%;
      margin-bottom: 2px;
    }}
    .brand-title {{
      font-size: 26px;
      font-weight: 900;
      color: #1E2024;
      letter-spacing: 0.16em;
    }}

    /* Central Browser Card */
    .app-browser {{
      position: absolute;
      top: 130px;
      left: 440px;
      width: 1040px;
      height: 640px;
      background: #FFFFFF;
      border-radius: 24px;
      border: 1px solid rgba(220, 214, 204, 0.75);
      box-shadow: 0 20px 48px -8px rgba(45, 35, 20, 0.1), 0 6px 16px rgba(45, 35, 20, 0.04), inset 0 1px 0 #FFFFFF;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      z-index: 20;
    }}
    .browser-header {{
      height: 48px;
      background: #FAF8F5;
      border-bottom: 1px solid rgba(224, 218, 208, 0.6);
      display: flex;
      align-items: center;
      padding: 0 20px;
      gap: 16px;
    }}
    .mac-dots {{
      display: flex;
      gap: 8px;
    }}
    .mac-dot {{
      width: 12px;
      height: 12px;
      border-radius: 50%;
    }}
    .dot-r {{ background: #FF5F56; }}
    .dot-y {{ background: #FFBD2E; }}
    .dot-g {{ background: #27C93F; }}

    .browser-url {{
      flex: 1;
      max-width: 440px;
      height: 28px;
      background: #FFFFFF;
      border: 1px solid rgba(215, 208, 196, 0.8);
      border-radius: 8px;
      display: flex;
      align-items: center;
      padding: 0 14px;
      font-size: 13px;
      color: #1E2024;
      font-weight: 700;
    }}
    .browser-body {{
      flex: 1;
      position: relative;
      background: #FFFFFF;
      overflow: hidden;
    }}
    .browser-body img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
    }}

    /* 4 Floating Feature Cards */
    .feat-card {{
      position: absolute;
      width: 320px;
      background: #FFFFFF;
      border-radius: 20px;
      border: 1.5px solid rgba(220, 214, 204, 0.75);
      box-shadow: 0 14px 32px -4px rgba(45, 35, 20, 0.08), 0 4px 10px rgba(45, 35, 20, 0.03), inset 0 1px 0 #FFFFFF;
      padding: 22px 24px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      z-index: 30;
      opacity: 0.32;
      transform: scale(0.94);
      filter: grayscale(18%);
      transition: opacity 0.38s cubic-bezier(0.2, 0.8, 0.2, 1),
                  transform 0.38s cubic-bezier(0.2, 0.8, 0.2, 1),
                  border-color 0.38s cubic-bezier(0.2, 0.8, 0.2, 1),
                  box-shadow 0.38s cubic-bezier(0.2, 0.8, 0.2, 1),
                  filter 0.38s cubic-bezier(0.2, 0.8, 0.2, 1);
    }}
    .feat-card.focused {{
      opacity: 1 !important;
      transform: scale(1.08) translateY(-6px) !important;
      filter: grayscale(0%) !important;
      border: 2px solid #C58B35 !important;
      box-shadow: 0 20px 44px rgba(197, 139, 53, 0.24), 0 6px 18px rgba(45, 35, 20, 0.08), inset 0 1px 0 #FFFFFF !important;
    }}
    .feat-header {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 18px;
      font-weight: 800;
      color: #1E2024;
    }}
    .feat-desc {{
      font-size: 14px;
      color: #64748B;
      font-weight: 600;
      line-height: 1.4;
    }}

    /* Card Positions */
    #f-card1 {{ top: 150px; left: 70px; }}
    #f-card2 {{ top: 150px; right: 70px; }}
    #f-card3 {{ bottom: 180px; left: 70px; }}
    #f-card4 {{ bottom: 180px; right: 70px; }}

    /* Subtitle & Presenter */
    .avatar-hud {{
      position: absolute;
      bottom: 52px;
      left: 64px;
      width: 110px;
      height: 110px;
      border-radius: 50%;
      background: #FAF7F0;
      border: 4px solid #FFFFFF;
      box-shadow: 0 10px 24px rgba(50, 38, 25, 0.12), 0 0 0 3px #E5DBC7;
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

    .subtitle-hud {{
      position: absolute;
      bottom: 64px;
      left: 200px;
      right: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 60;
      pointer-events: none;
    }}
    .subtitle-capsule {{
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1.5px solid rgba(220, 214, 204, 0.85);
      border-radius: 9999px;
      padding: 12px 42px;
      box-shadow: 0 12px 32px rgba(45, 35, 20, 0.09), inset 0 1px 0 #FFFFFF;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      max-width: 1440px;
    }}
    .subtitle-text {{
      font-size: 36px;
      font-weight: 850;
      color: #1A1C20;
      letter-spacing: 0.03em;
      text-align: center;
      line-height: 1.35;
    }}
    .sub-hl {{
      color: #C58B35;
      font-weight: 900;
      background: rgba(254, 243, 199, 0.55);
      padding: 1px 8px;
      border-radius: 6px;
    }}

    .hand-pointer {{
      position: absolute;
      width: 54px;
      height: 54px;
      pointer-events: none;
      z-index: 100;
      filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.22));
      opacity: 0;
    }}
  </style>

  <div id="root" data-composition-id="{scene_id}">
    {render_header(chapter_num, chapter_title, brand_name)}

    <!-- Central Browser -->
    <div class="app-browser" id="s5-browser">
      <div class="browser-header">
        <div class="mac-dots">
          <div class="mac-dot dot-r"></div>
          <div class="mac-dot dot-y"></div>
          <div class="mac-dot dot-g"></div>
        </div>
        <div class="browser-url">
          <span style="color: #64748B;">{app_url}</span>
        </div>
      </div>
      <div class="browser-body">
        <img src="../assets/kids_lingo_app_retina.png" alt="Kids Lingo App" />
      </div>
    </div>

    <!-- 4 Satellite Features -->
    <div class="feat-card" id="f-card1">
      <div class="feat-header"><span>📚</span> 分级阅读库</div>
      <div class="feat-desc">Level 1 - 6 原版阶梯绘本<br>智能词汇分级与情景音频</div>
    </div>

    <div class="feat-card" id="f-card2">
      <div class="feat-header"><span>🎙️</span> AI 实时发音纠错</div>
      <div class="feat-desc">真人音标精准比对，契合度 98.5%<br><span style="color: #C58B35; font-size: 12px;"> ▃▅▇▅▃ 音频实时波形</span></div>
    </div>

    <div class="feat-card" id="f-card3">
      <div class="feat-header"><span>📖</span> 趣味生词本</div>
      <div class="feat-desc">艾宾浩斯遗忘曲线复盘<br>趣味卡片拼读与发音强化</div>
    </div>

    <div class="feat-card" id="f-card4">
      <div class="feat-header"><span>📊</span> 家长伴学仪表盘</div>
      <div class="feat-desc">每日学习时长 · 掌握单词 24 个<br>周报自动生成与成长曲线</div>
    </div>

    {render_pointer("s5-pointer")}
    {render_presenter_hud("../assets/avatar.jpg", "s5-avatar")}
    {render_subtitle_hud("", "s5-sub")}
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});

    tl.fromTo("#s5-browser", 
      {{ opacity: 0, scale: 0.92, y: 30 }}, 
      {{ opacity: 1, scale: 1, y: 0, duration: 0.8, ease: "power2.out" }}, 
      0.3
    );

    tl.fromTo(".feat-card", 
      {{ opacity: 0, scale: 0.88 }}, 
      {{ opacity: 0.32, scale: 0.94, duration: 0.6, stagger: 0.1, ease: "back.out(1.2)" }}, 
      0.8
    );

    // Subtitles
    {"".join(sub_timeline_js)}

    // Pointer clicks & single card focus
    function focusFeature(cardId) {{
      document.querySelectorAll(".feat-card").forEach(el => {{
        if (el.id === cardId) {{
          el.classList.add("focused");
        }} else {{
          el.classList.remove("focused");
        }}
      }});
    }}

    // Feat 1: Top-Left
    tl.to("#s5-pointer", {{ opacity: 1, duration: 0.25 }}, 3.8);
    tl.fromTo("#s5-pointer", {{ left: 500, top: 400 }}, {{ left: 240, top: 220, duration: 0.45, ease: "power2.out" }}, 3.8);
    tl.call(() => focusFeature("f-card1"), null, 4.2);
    tl.to("#s5-pointer", {{ scale: 0.85, duration: 0.1, yoyo: true, repeat: 1 }}, 4.2);

    // Feat 2: Top-Right
    tl.to("#s5-pointer", {{ left: 1680, top: 220, duration: 0.55, ease: "power2.inOut" }}, 5.5);
    tl.call(() => focusFeature("f-card2"), null, 6.0);
    tl.to("#s5-pointer", {{ scale: 0.85, duration: 0.1, yoyo: true, repeat: 1 }}, 6.0);

    // Feat 3: Bottom-Left
    tl.to("#s5-pointer", {{ left: 240, top: 620, duration: 0.55, ease: "power2.inOut" }}, 7.4);
    tl.call(() => focusFeature("f-card3"), null, 7.9);
    tl.to("#s5-pointer", {{ scale: 0.85, duration: 0.1, yoyo: true, repeat: 1 }}, 7.9);

    // Feat 4: Bottom-Right
    tl.to("#s5-pointer", {{ left: 1680, top: 620, duration: 0.55, ease: "power2.inOut" }}, 9.2);
    tl.call(() => focusFeature("f-card4"), null, 9.7);
    tl.to("#s5-pointer", {{ scale: 0.85, duration: 0.1, yoyo: true, repeat: 1 }}, 9.7);

    tl.to("#s5-pointer", {{ opacity: 0, duration: 0.3 }}, 11.0);

    // Avatar soft breathing
    tl.fromTo("#s5-avatar", {{ y: 0 }}, {{ y: -6, duration: 1.6, yoyo: true, repeat: 8, ease: "sine.inOut" }}, 0.2);

    // Scene transition exit fadeout
    tl.to("#root", {{ opacity: 0, duration: 0.25 }}, {duration - 0.25});

    window.__timelines = window.__timelines || {{}};
    window.__timelines["{scene_id}"] = tl;
  </script>
</template>
"""

