"""
Archetype 1: Grid Cards Matrix with Selective Focus & Hand Pointer
"""

from ..components import render_header, render_presenter_hud, render_subtitle_hud, render_pointer

def generate_grid_cards_html(scene_id, config, duration=14.0):
    chapter_num = config.get("chapter_num", "01")
    chapter_title = config.get("chapter_title", "发现神器")
    brand_name = config.get("brand_name", "胖猫")
    browser_url = config.get("browser_url", "https://skills.sh")
    cards = config.get("cards", [
        {"id": "c1", "title": "连数据库", "desc": "Supabase / PG / MySQL<br>秒级打通业务数据底座", "tag": "实时直连", "color": "#0284C7", "icon": "M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"},
        {"id": "c2", "title": "做 PPT", "desc": "PptxGenJS 智能排版<br>商务演说级美学输出", "tag": "一键排版", "color": "#F59E0B", "icon": "M7 4V20M17 4V20M3 8H7M17 8H21M3 12H21M3 16H7M17 16H21M4 20H20C20.5523 20 21 19.5523 21 19V5C21 4.44772 20.5523 4 20 4H4C3.44772 4 3 4.44772 3 5V19C3 19.5523 3.44772 20 4 20Z"},
        {"id": "c3", "title": "写长文", "desc": "万字专业行业研报<br>深度拆解与知识逻辑", "tag": "万字研报", "color": "#10B981", "icon": "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"},
        {"id": "c4", "title": "做海报", "desc": "SVG & Canvas 矢量绘图<br>品牌级视觉宣发物料", "tag": "视觉工坊", "color": "#8B5CF6", "icon": "M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"}
    ])

    subtitles = config.get("subtitles", [
        {"start": 0.0, "text": "想要手搓<span class='sub-hl'>全栈应用</span>，但不知道从何开始？"},
        {"start": 4.5, "text": "别慌！打开这个目前全球最火的 <span class='sub-hl'>Skills 生态站</span>。"},
        {"start": 8.5, "text": "有帮你<span class='sub-hl'>连数据库</span>的、<span class='sub-hl'>做 PPT</span>的、<span class='sub-hl'>写长文</span>的，应有尽有！"}
    ])

    cards_html = []
    for c in cards:
        cards_html.append(f"""
        <div class="app-card" id="{c['id']}">
          <div class="app-icon-wrap" style="background: {c['color']};">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="{c['icon']}"/>
            </svg>
          </div>
          <div class="app-title">{c['title']}</div>
          <div class="app-desc">{c['desc']}</div>
          <div class="app-tag" style="background: {c['color']}18; color: {c['color']};">{c['tag']}</div>
        </div>
        """)

    cards_markup = "\n".join(cards_html)

    # Subtitle timeline calls
    sub_timeline_js = []
    for s in subtitles:
        sub_timeline_js.append(f"""
    tl.call(() => {{
      const sub = document.getElementById("s1-sub");
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

    /* Card Matrix Stage */
    .cards-stage {{
      position: absolute;
      top: 150px;
      left: 140px;
      width: 1640px;
      height: 640px;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 36px;
      z-index: 20;
    }}
    .app-card {{
      width: 340px;
      height: 440px;
      background: #FFFFFF;
      border-radius: 28px;
      border: 1px solid rgba(224, 218, 206, 0.75);
      box-shadow: 0 18px 40px -8px rgba(45, 35, 20, 0.08), 0 6px 16px rgba(45, 35, 20, 0.03), inset 0 1px 0 #FFFFFF;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 40px 24px;
      position: relative;
      transition: opacity 0.35s ease, transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), border-color 0.35s ease, box-shadow 0.35s ease;
    }}
    .app-card.focused {{
      transform: scale(1.08) translateY(-8px) !important;
      opacity: 1 !important;
      border: 2px solid #C58B35 !important;
      box-shadow: 0 24px 54px rgba(197, 139, 53, 0.22), 0 8px 24px rgba(45, 35, 20, 0.06), inset 0 1px 0 #FFFFFF !important;
    }}
    .app-icon-wrap {{
      width: 130px;
      height: 130px;
      border-radius: 36px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 28px;
      box-shadow: 0 14px 28px rgba(0, 0, 0, 0.08), inset 0 2px 4px rgba(255, 255, 255, 0.8);
      position: relative;
    }}
    .app-title {{
      font-size: 28px;
      font-weight: 800;
      color: #1E2024;
      margin-bottom: 12px;
      letter-spacing: 0.02em;
    }}
    .app-desc {{
      font-size: 16px;
      color: #64748B;
      font-weight: 600;
      text-align: center;
      line-height: 1.5;
    }}
    .app-tag {{
      margin-top: 24px;
      padding: 6px 16px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.05em;
    }}

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

    <div class="cards-stage" id="cards-stage">
      {cards_markup}
    </div>

    {render_pointer("s1-pointer")}
    {render_presenter_hud("../assets/avatar.jpg", "s1-avatar")}
    {render_subtitle_hud("", "s1-sub")}
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});

    // Enter cards
    tl.fromTo(".app-card", 
      {{ opacity: 0, y: 50, scale: 0.92 }},
      {{ opacity: 1, y: 0, scale: 1, duration: 0.7, stagger: 0.12, ease: "back.out(1.4)" }},
      0.4
    );

    // Subtitle transitions
    {"".join(sub_timeline_js)}

    // Pointer clicks & single card focus
    function focusCard(cardId) {{
      document.querySelectorAll(".app-card").forEach(el => {{
        if (el.id === cardId) {{
          el.classList.add("focused");
          el.style.opacity = "1";
        }} else {{
          el.classList.remove("focused");
          el.style.opacity = "0.32";
        }}
      }});
    }}

    // Card 1
    tl.to("#s1-pointer", {{ opacity: 1, duration: 0.3 }}, 8.8);
    tl.fromTo("#s1-pointer", {{ left: 500, top: 600 }}, {{ left: 380, top: 400, duration: 0.5, ease: "power2.out" }}, 8.8);
    tl.call(() => focusCard("c1"), null, 9.3);
    tl.to("#s1-pointer", {{ scale: 0.85, duration: 0.12, yoyo: true, repeat: 1 }}, 9.3);

    // Card 2
    tl.to("#s1-pointer", {{ left: 760, top: 400, duration: 0.5, ease: "power2.inOut" }}, 9.8);
    tl.call(() => focusCard("c2"), null, 10.3);
    tl.to("#s1-pointer", {{ scale: 0.85, duration: 0.12, yoyo: true, repeat: 1 }}, 10.3);

    // Card 3
    tl.to("#s1-pointer", {{ left: 1140, top: 400, duration: 0.5, ease: "power2.inOut" }}, 10.8);
    tl.call(() => focusCard("c3"), null, 11.3);
    tl.to("#s1-pointer", {{ scale: 0.85, duration: 0.12, yoyo: true, repeat: 1 }}, 11.3);

    // Card 4
    tl.to("#s1-pointer", {{ left: 1520, top: 400, duration: 0.5, ease: "power2.inOut" }}, 11.8);
    tl.call(() => focusCard("c4"), null, 12.3);
    tl.to("#s1-pointer", {{ scale: 0.85, duration: 0.12, yoyo: true, repeat: 1 }}, 12.3);

    tl.to("#s1-pointer", {{ opacity: 0, duration: 0.3 }}, 13.2);

    // Avatar soft breathing
    tl.fromTo("#s1-avatar", {{ y: 0 }}, {{ y: -6, duration: 1.6, yoyo: true, repeat: 8, ease: "sine.inOut" }}, 0.2);

    // Scene transition exit fadeout
    tl.to("#root", {{ opacity: 0, duration: 0.25 }}, {duration - 0.25});

    window.__timelines = window.__timelines || {{}};
    window.__timelines["{scene_id}"] = tl;
  </script>
</template>
"""

