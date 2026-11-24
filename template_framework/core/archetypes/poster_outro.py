"""
Archetype 6: Prototype Poster Auto-Scroll & Grand Outro Hold Page
(Guarantees final frame holds indefinitely without black screen fadeout)
"""

from ..components import render_header, render_presenter_hud, render_subtitle_hud

def generate_poster_outro_html(scene_id, config, duration=20.6):
    chapter_num = config.get("chapter_num", "06")
    chapter_title = config.get("chapter_title", "超级个体")
    brand_name = config.get("brand_name", "胖猫")
    poster_src = config.get("poster_src", "../assets/top10_poster.jpg")
    cta_code = config.get("cta_code", "666")
    cta_reward = config.get("cta_reward", "免费领取全套资源包")
    outro_title = config.get("outro_title", "胖猫 AI")
    outro_desc = config.get("outro_desc", "带你探索 AI 时代超级个体之路")
    outro_button = config.get("outro_button", "点赞 · 收藏 · 关注 ✦ 咱们下期见！")

    subtitles = config.get("subtitles", [
        {"start": 0.0, "text": "最实用的 <span class='sub-hl'>10 个高频 Skills</span> 也为你整理好了，评论区回复 <span class='sub-hl'>「666」</span> 免费领！"},
        {"start": 14.5, "text": "我是<span class='sub-hl'>胖猫 AI</span>，带你探索 AI 超级个体之路，咱们下期见！"}
    ])

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

    /* Stage 1: Poster Viewport & CTA Card */
    .s6-stage1 {{
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 60px;
      z-index: 20;
    }}

    /* Mobile Frame with Prototype Poster Auto-Scroll */
    .poster-phone {{
      width: 480px;
      height: 680px;
      background: #FFFFFF;
      border-radius: 36px;
      border: 4px solid #FFFFFF;
      box-shadow: 0 24px 60px -8px rgba(45, 35, 20, 0.14), 0 0 0 1px rgba(220, 214, 204, 0.8), inset 0 1px 0 #FFFFFF;
      overflow: hidden;
      position: relative;
    }}
    .poster-img-wrap {{
      width: 100%;
      position: absolute;
      top: 0;
      left: 0;
    }}
    .poster-img-wrap img {{
      width: 100%;
      height: auto;
      display: block;
    }}

    /* Right CTA Incentive Card */
    .cta-card {{
      width: 480px;
      background: #FFFFFF;
      border-radius: 28px;
      border: 1px solid rgba(220, 214, 204, 0.75);
      box-shadow: 0 20px 48px -8px rgba(45, 35, 20, 0.08), inset 0 1px 0 #FFFFFF;
      padding: 44px 40px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }}
    .cta-badge {{
      font-size: 14px;
      font-weight: 800;
      color: #C58B35;
      margin-bottom: 24px;
      letter-spacing: 0.1em;
    }}
    .cta-box {{
      width: 100%;
      background: #FFFDF9;
      border: 2px dashed #FDE68A;
      border-radius: 20px;
      padding: 24px 20px;
      margin-bottom: 24px;
    }}
    .cta-box-title {{
      font-size: 16px;
      color: #78716C;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .cta-box-code {{
      font-size: 48px;
      font-weight: 900;
      color: #C58B35;
      letter-spacing: 0.1em;
    }}
    .cta-box-desc {{
      font-size: 14px;
      color: #A8A29E;
      font-weight: 700;
    }}

    /* Stage 2: Grand Outro Hold Page */
    .grand-outro-screen {{
      position: absolute;
      inset: 0;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 30;
    }}
    .outro-avatar-ring {{
      width: 160px;
      height: 160px;
      border-radius: 50%;
      background: #FAF7F0;
      border: 5px solid #FFFFFF;
      box-shadow: 0 16px 40px rgba(50, 38, 25, 0.14), 0 0 0 4px #E5DBC7;
      overflow: hidden;
      margin-bottom: 28px;
    }}
    .outro-avatar-ring img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .outro-title {{
      font-size: 42px;
      font-weight: 900;
      color: #1E2024;
      letter-spacing: 0.04em;
      margin-bottom: 12px;
    }}
    .outro-desc {{
      font-size: 22px;
      font-weight: 700;
      color: #64748B;
      letter-spacing: 0.05em;
      margin-bottom: 32px;
    }}
    .outro-btn-capsule {{
      background: #FFFFFF;
      border: 1.5px solid rgba(220, 214, 204, 0.85);
      border-radius: 9999px;
      padding: 14px 44px;
      font-size: 18px;
      font-weight: 800;
      color: #C58B35;
      box-shadow: 0 10px 24px rgba(45, 35, 20, 0.06);
    }}

    /* Subtitle & Presenter HUD */
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

    <!-- Stage 1: Poster + CTA -->
    <div class="s6-stage1" id="s6-stage1">
      <div class="poster-phone">
        <div class="poster-img-wrap" id="s6-poster-img">
          <img src="{poster_src}" alt="Official Top 10 Poster" />
        </div>
      </div>

      <div class="cta-card" id="s6-cta-card">
        <div class="cta-badge">✦ 粉丝专属免费福利 ✦</div>
        <div class="cta-box">
          <div class="cta-box-title">评论区回复</div>
          <div class="cta-box-code">「 {cta_code} 」</div>
          <div class="cta-box-desc">{cta_reward}</div>
        </div>
        <div style="font-size: 15px; color: #78716C; line-height: 1.6; font-weight: 600;">
          包含 10 个高频 Skills 配置文件<br>以及零基础 Vibe Coding 实操视频教程
        </div>
      </div>
    </div>

    <!-- Stage 2: Grand Outro Hold Page -->
    <div class="grand-outro-screen" id="s6-grand-outro">
      <div class="outro-avatar-ring">
        <img src="../assets/avatar.jpg" alt="Outro Presenter" />
      </div>
      <div class="outro-title">{outro_title}</div>
      <div class="outro-desc">{outro_desc}</div>
      <div class="outro-btn-capsule">{outro_button}</div>
    </div>

    {render_presenter_hud("../assets/avatar.jpg", "s6-avatar")}
    {render_subtitle_hud("", "s6-sub")}
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});

    tl.fromTo("#s6-stage1", 
      {{ opacity: 0.9, y: 30, scale: 0.98 }}, 
      {{ opacity: 1, y: 0, scale: 1, duration: 0.8, ease: "power2.out" }}, 
      0
    );

    // Auto-scroll the prototype poster smoothly
    tl.fromTo("#s6-poster-img", 
      {{ y: 0 }}, 
      {{ y: -390, duration: 11.5, ease: "power1.inOut" }}, 
      1.0
    );

    // Pulse on reply CTA
    tl.to("#s6-cta-card", {{ scale: 1.03, duration: 1.2, yoyo: true, repeat: 5, ease: "sine.inOut" }}, 1.5);

    // Subtitle 1
    tl.call(() => {{
      const sub = document.getElementById("s6-sub");
      if (sub) sub.innerHTML = "{subtitles[0]['text']}";
    }}, null, 0.0);

    // Switch to Grand Outro at 14.5s
    tl.call(() => {{
      const sub = document.getElementById("s6-sub");
      if (sub) sub.innerHTML = "{subtitles[1]['text']}";

      const s1 = document.getElementById("s6-stage1");
      const outro = document.getElementById("s6-grand-outro");
      const avHud = document.getElementById("s6-avatar");
      if (s1) s1.style.display = "none";
      if (avHud) avHud.style.display = "none";
      if (outro) outro.style.display = "flex";
    }}, null, 14.5);

    tl.fromTo("#s6-grand-outro", 
      {{ opacity: 0, scale: 0.92 }}, 
      {{ opacity: 1, scale: 1, duration: 0.8, ease: "power2.out" }}, 
      14.6
    );

    // Avatar breathing
    tl.fromTo("#s6-avatar", {{ y: 0 }}, {{ y: -8, duration: 1.8, yoyo: true, repeat: 7, ease: "sine.inOut" }}, 0.2);

    window.__timelines = window.__timelines || {{}};
    // CONTRACT: Final frame holds on grand outro page without fadeout!
    window.__timelines["{scene_id}"] = tl;
  </script>
</template>
"""
