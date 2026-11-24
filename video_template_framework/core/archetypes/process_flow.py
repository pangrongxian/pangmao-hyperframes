"""
Archetype 3: Dual-Lane Process Flow Comparison with Syntax-Highlighted IDE Box
"""

from ..components import render_header, render_presenter_hud, render_subtitle_hud

def generate_process_flow_html(scene_id, config, duration=12.5):
    chapter_num = config.get("chapter_num", "03")
    chapter_title = config.get("chapter_title", "一键安装")
    brand_name = config.get("brand_name", "胖猫")

    subtitles = config.get("subtitles", [
        {"start": 0.0, "text": "以前我们要写一堆配置、查半天文档，还容易报错。"},
        {"start": 4.5, "text": "现在只需要在 <span class='sub-hl'>Cursor</span> 里输入一条命令，技能自动装载！"}
    ])

    sub_timeline_js = []
    for s in subtitles:
        sub_timeline_js.append(f"""
    tl.call(() => {{
      const sub = document.getElementById("s3-sub");
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

    /* Pipeline Comparison */
    .pipeline-stage {{
      position: absolute;
      top: 130px;
      left: 180px;
      width: 1560px;
      height: 330px;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      z-index: 20;
    }}
    .pipeline-lane {{
      display: flex;
      align-items: center;
      gap: 36px;
      position: relative;
      transition: opacity 0.5s ease;
    }}
    .lane-label {{
      width: 140px;
      font-size: 22px;
      font-weight: 800;
      color: #1E2024;
      text-align: right;
    }}
    .lane-dimmed {{ opacity: 0.28; }}
    .lane-nodes {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
    }}
    .lane-line {{
      position: absolute;
      top: 42px;
      left: 60px;
      right: 60px;
      height: 2px;
      background: #CBD5E1;
      z-index: 1;
    }}
    .p-node {{
      position: relative;
      z-index: 2;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
    }}
    .p-card {{
      width: 84px;
      height: 84px;
      background: #FFFFFF;
      border-radius: 24px;
      border: 1px solid rgba(220, 214, 204, 0.8);
      box-shadow: 0 12px 28px -4px rgba(45, 35, 20, 0.08), inset 0 1px 0 #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 32px;
    }}
    .p-node.active .p-card {{
      border: 2px solid #C58B35;
      box-shadow: 0 16px 36px rgba(197, 139, 53, 0.25), inset 0 1px 0 #FFFFFF;
      transform: scale(1.08);
    }}
    .p-title {{
      font-size: 16px;
      font-weight: 700;
      color: #334155;
    }}

    /* IDE Terminal Box */
    .ide-box {{
      position: absolute;
      top: 490px;
      left: 360px;
      width: 1200px;
      height: 330px;
      background: #18181B;
      border-radius: 20px;
      box-shadow: 0 24px 50px rgba(0, 0, 0, 0.35);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      z-index: 20;
    }}
    .ide-header {{
      height: 42px;
      background: #27272A;
      display: flex;
      align-items: center;
      padding: 0 18px;
      gap: 10px;
    }}
    .ide-dot {{
      width: 12px;
      height: 12px;
      border-radius: 50%;
    }}
    .dot-r {{ background: #EF4444; }}
    .dot-y {{ background: #F59E0B; }}
    .dot-g {{ background: #10B981; }}
    .ide-body {{
      flex: 1;
      padding: 24px 32px;
      font-family: 'SF Mono', Menlo, monospace;
      font-size: 19px;
      line-height: 1.7;
      color: #E4E4E7;
    }}
    .code-hl-cmd {{ color: #60A5FA; font-weight: 700; }}
    .code-hl-pkg {{ color: #FBBF24; font-weight: 700; }}
    .code-hl-ok {{ color: #34D399; font-weight: 700; }}

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

    <div class="pipeline-stage">
      <!-- Slow Lane -->
      <div class="pipeline-lane" id="lane-slow">
        <div class="lane-label" style="color: #64748B;">传统流程</div>
        <div class="lane-nodes">
          <div class="lane-line"></div>
          <div class="p-node"><div class="p-card">📖</div><div class="p-title">查阅文档</div></div>
          <div class="p-node"><div class="p-card">⚙️</div><div class="p-title">环境配置</div></div>
          <div class="p-node"><div class="p-card">🐞</div><div class="p-title">排查错误</div></div>
          <div class="p-node"><div class="p-card">📦</div><div class="p-title">部署发布</div></div>
        </div>
      </div>

      <!-- Fast Lane -->
      <div class="pipeline-lane" id="lane-fast">
        <div class="lane-label" style="color: #C58B35;">极速模式</div>
        <div class="lane-nodes">
          <div class="lane-line" style="background: #FDE68A;"></div>
          <div class="p-node active"><div class="p-card" style="border-color: #C58B35;">💡</div><div class="p-title">需求描述</div></div>
          <div class="p-node active"><div class="p-card" style="border-color: #C58B35;">⚡️</div><div class="p-title">Skill 自动装载</div></div>
          <div class="p-node active"><div class="p-card" style="border-color: #10B981;">🚀</div><div class="p-title">成品即刻就绪</div></div>
        </div>
      </div>
    </div>

    <!-- IDE Box -->
    <div class="ide-box" id="s3-ide">
      <div class="ide-header">
        <div class="ide-dot dot-r"></div>
        <div class="ide-dot dot-y"></div>
        <div class="ide-dot dot-g"></div>
        <span style="color: #A1A1AA; font-size: 13px; font-weight: 600; margin-left: 10px;">Cursor Terminal · zsh</span>
      </div>
      <div class="ide-body">
        <div>$ <span class="code-hl-cmd">npx</span> skills-cli add <span class="code-hl-pkg">@vercel/find-skills</span></div>
        <div style="color: #71717A; margin-top: 6px;">[1/3] Resolving skill package metadata...</div>
        <div style="color: #71717A;">[2/3] Linking MCP rules and context instructions...</div>
        <div style="margin-top: 8px;"><span class="code-hl-ok">✔ SUCCESS</span> Skill activated in workspace! Ready for vibe coding.</div>
      </div>
    </div>

    {render_presenter_hud("../assets/avatar.jpg", "s3-avatar")}
    {render_subtitle_hud("", "s3-sub")}
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});

    tl.fromTo("#lane-slow", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.3);
    tl.to("#lane-slow", {{ opacity: 0.28, duration: 0.5 }}, 4.2);

    tl.fromTo("#lane-fast", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 4.5);
    tl.fromTo("#s3-ide", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "power2.out" }}, 5.0);

    // Subtitles
    {"".join(sub_timeline_js)}

    // Avatar breathing
    tl.fromTo("#s3-avatar", {{ y: 0 }}, {{ y: -6, duration: 1.6, yoyo: true, repeat: 7, ease: "sine.inOut" }}, 0.2);

    // Exit fadeout
    tl.to("#root", {{ opacity: 0, duration: 0.25 }}, {duration - 0.25});

    window.__timelines = window.__timelines || {{}};
    window.__timelines["{scene_id}"] = tl;
  </script>
</template>
"""

