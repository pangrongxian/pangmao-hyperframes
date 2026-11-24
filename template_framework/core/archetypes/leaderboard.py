"""
Archetype 2: Leaderboard & Dynamic Ranking with Counter
"""

from ..components import render_header, render_presenter_hud, render_subtitle_hud

def generate_leaderboard_html(scene_id, config, duration=10.5):
    chapter_num = config.get("chapter_num", "02")
    chapter_title = config.get("chapter_title", "浩瀚生态")
    brand_name = config.get("brand_name", "胖猫")
    board_title = config.get("board_title", "Global Skills Elo Leaderboard")
    board_sub = config.get("board_sub", "基于开发者真实调用与评分构建的全球热门技能天梯榜")
    filter_tabs = config.get("filter_tabs", ["全部分类", "核心精选", "Vibe Coding", "自动化"])
    counter_target = config.get("counter_target", "1,514,280")
    
    rows = config.get("rows", [
        {"rank": "01", "name": "find-skills", "author": "Vercel-Labs", "elo": "1,420", "bar": "94%", "badge": "Gold", "hl": True},
        {"rank": "02", "name": "frontend-design", "author": "Anthropic", "elo": "1,385", "bar": "88%", "badge": "Silver", "hl": False},
        {"rank": "03", "name": "vercel-react-best-practices", "author": "Vercel", "elo": "1,340", "bar": "82%", "badge": "Bronze", "hl": False},
        {"rank": "04", "name": "agent-browser", "author": "Community", "elo": "1,290", "bar": "76%", "badge": "Normal", "hl": False}
    ])

    subtitles = config.get("subtitles", [
        {"start": 0.0, "text": "光是官方收录的技能，就已经超过了 <span class='sub-hl'>151 万次</span>安装！"},
        {"start": 5.0, "text": "它就像一个巨大的 <span class='sub-hl'>AI 外挂超市</span>，让普通人也能瞬间拥有顶级工程师的能力。"}
    ])

    rows_html = []
    for r in rows:
        badge_style = "background: #FEF3C7; color: #B45309;" if r['badge'] == "Gold" else "background: #F1F5F9; color: #475569;"
        hl_class = "highlighted" if r['hl'] else ""
        rows_html.append(f"""
        <div class="rank-row {hl_class}">
          <div class="col-rank">{r['rank']}</div>
          <div class="col-name">
            <span class="skill-name">{r['name']}</span>
            <span class="skill-author">{r['author']}</span>
          </div>
          <div class="col-bar-wrap">
            <div class="col-bar" style="width: {r['bar']};"></div>
          </div>
          <div class="col-elo">{r['elo']}</div>
          <div class="col-badge" style="{badge_style}">{r['badge']}</div>
        </div>
        """)

    tabs_html = []
    for idx, tab in enumerate(filter_tabs):
        active_class = "active" if idx == 0 else ""
        tabs_html.append(f'<div class="filter-tab {active_class}">{tab}</div>')

    sub_timeline_js = []
    for s in subtitles:
        sub_timeline_js.append(f"""
    tl.call(() => {{
      const sub = document.getElementById("s2-sub");
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

    /* Leaderboard Card Container */
    .arena-container {{
      position: absolute;
      top: 130px;
      left: 140px;
      width: 1140px;
      height: 700px;
      background: #FFFFFF;
      border-radius: 28px;
      border: 1px solid rgba(220, 214, 204, 0.75);
      box-shadow: 0 20px 48px -8px rgba(45, 35, 20, 0.08), 0 6px 16px rgba(45, 35, 20, 0.03), inset 0 1px 0 #FFFFFF;
      padding: 36px 44px;
      display: flex;
      flex-direction: column;
      z-index: 20;
    }}
    .arena-header-title {{
      display: flex;
      align-items: center;
      gap: 14px;
      font-size: 32px;
      font-weight: 800;
      color: #1E2024;
      letter-spacing: -0.01em;
      margin-bottom: 8px;
    }}
    .arena-badge {{
      font-size: 14px;
      font-weight: 700;
      color: #7C3AED;
      background: #F3E8FF;
      padding: 4px 12px;
      border-radius: 9999px;
    }}
    .arena-sub {{
      font-size: 15px;
      color: #64748B;
      font-weight: 500;
      margin-bottom: 24px;
    }}

    .filter-tabs {{
      display: flex;
      gap: 12px;
      margin-bottom: 24px;
    }}
    .filter-tab {{
      padding: 7px 18px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 700;
      background: #F1F5F9;
      color: #475569;
      border: 1px solid rgba(226, 232, 240, 0.8);
    }}
    .filter-tab.active {{
      background: #1E2024;
      color: #FFFFFF;
      border-color: #1E2024;
    }}

    .rank-table {{
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .rank-row {{
      display: flex;
      align-items: center;
      height: 66px;
      padding: 0 20px;
      background: #F8FAFC;
      border-radius: 16px;
      border: 1px solid rgba(226, 232, 240, 0.6);
      transition: all 0.3s ease;
    }}
    .rank-row.highlighted {{
      background: #FFFBEB;
      border: 2px solid #F59E0B;
      box-shadow: 0 8px 24px rgba(245, 158, 11, 0.15);
    }}
    .col-rank {{
      width: 44px;
      font-size: 20px;
      font-weight: 900;
      color: #C58B35;
    }}
    .col-name {{
      width: 320px;
      display: flex;
      flex-direction: column;
    }}
    .skill-name {{
      font-size: 18px;
      font-weight: 800;
      color: #1E2024;
    }}
    .skill-author {{
      font-size: 12px;
      color: #94A3B8;
      font-weight: 600;
    }}
    .col-bar-wrap {{
      flex: 1;
      height: 10px;
      background: #E2E8F0;
      border-radius: 999px;
      overflow: hidden;
      margin: 0 24px;
    }}
    .col-bar {{
      height: 100%;
      background: linear-gradient(90deg, #F59E0B, #E11D48);
      border-radius: 999px;
    }}
    .col-elo {{
      width: 90px;
      font-size: 17px;
      font-weight: 800;
      color: #1E2024;
      text-align: right;
    }}
    .col-badge {{
      margin-left: 20px;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 800;
    }}

    /* Right Highlight Counter Card */
    .stat-card {{
      position: absolute;
      top: 220px;
      right: 140px;
      width: 440px;
      background: #FFFFFF;
      border-radius: 28px;
      border: 1px solid rgba(220, 214, 204, 0.75);
      box-shadow: 0 20px 48px -8px rgba(45, 35, 20, 0.08), inset 0 1px 0 #FFFFFF;
      padding: 44px 36px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      z-index: 20;
    }}
    .stat-num {{
      font-size: 54px;
      font-weight: 900;
      color: #C58B35;
      letter-spacing: -0.02em;
      margin: 12px 0;
    }}
    .stat-lbl {{
      font-size: 17px;
      font-weight: 700;
      color: #64748B;
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
  </style>

  <div id="root" data-composition-id="{scene_id}">
    {render_header(chapter_num, chapter_title, brand_name)}

    <div class="arena-container" id="s2-arena">
      <div class="arena-header-title">
        {board_title}
        <span class="arena-badge">LIVE ELO</span>
      </div>
      <div class="arena-sub">{board_sub}</div>
      <div class="filter-tabs">
        {"".join(tabs_html)}
      </div>
      <div class="rank-table">
        {"".join(rows_html)}
      </div>
    </div>

    <div class="stat-card" id="s2-stat">
      <div class="stat-lbl">全网累计下载与装配量</div>
      <div class="stat-num">{counter_target}+</div>
      <div class="stat-lbl" style="color: #10B981; font-weight: 800;">✦ 全球开发者正在使用</div>
    </div>

    {render_presenter_hud("../assets/avatar.jpg", "s2-avatar")}
    {render_subtitle_hud("", "s2-sub")}
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});

    tl.fromTo("#s2-arena", 
      {{ opacity: 0, x: -40, scale: 0.96 }},
      {{ opacity: 1, x: 0, scale: 1, duration: 0.8, ease: "power2.out" }},
      0.3
    );

    tl.fromTo("#s2-stat",
      {{ opacity: 0, x: 40, scale: 0.94 }},
      {{ opacity: 1, x: 0, scale: 1, duration: 0.8, ease: "power2.out" }},
      0.5
    );

    // Dynamic bar growth
    tl.fromTo(".col-bar", 
      {{ width: "0%" }},
      {{ width: "100%", duration: 1.2, stagger: 0.1, ease: "power2.out" }},
      0.8
    );

    // Subtitles
    {"".join(sub_timeline_js)}

    // Avatar soft breathing
    tl.fromTo("#s2-avatar", {{ y: 0 }}, {{ y: -6, duration: 1.6, yoyo: true, repeat: 7, ease: "sine.inOut" }}, 0.2);

    // Exit fadeout
    tl.to("#root", {{ opacity: 0, duration: 0.25 }}, {duration - 0.25});

    window.__timelines = window.__timelines || {{}};
    window.__timelines["{scene_id}"] = tl;
  </script>
</template>
"""
