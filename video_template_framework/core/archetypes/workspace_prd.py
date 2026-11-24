"""
Archetype 4: Workspace PRD with Milestones, Dialogue Bubbles, Checklist & Progress
"""

from ..components import render_header, render_presenter_hud, render_subtitle_hud

def generate_workspace_prd_html(scene_id, config, duration=20.8):
    chapter_num = config.get("chapter_num", "04")
    chapter_title = config.get("chapter_title", "需求企划")
    brand_name = config.get("brand_name", "胖猫")

    subtitles = config.get("subtitles", [
        {"start": 0.0, "text": "比如我想做一款<span class='sub-hl'>儿童英语分级绘本站</span>。"},
        {"start": 5.0, "text": "我们让 AI 扮演产品经理，逐条审查边界条件与技术可行性。"},
        {"start": 12.0, "text": "确认完毕后，直接交给自动化流水线并行编写全栈代码！"}
    ])

    sub_timeline_js = []
    for s in subtitles:
        sub_timeline_js.append(f"""
    tl.call(() => {{
      const sub = document.getElementById("s4-sub");
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

    /* Top Process Flow Pipeline */
    .flow-pipeline {{
      position: absolute;
      top: 125px;
      left: 280px;
      width: 1360px;
      height: 90px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
      z-index: 20;
    }}
    .pipeline-line-bg {{
      position: absolute;
      top: 45px;
      left: 60px;
      right: 60px;
      height: 2px;
      background: #E2D7C5;
      z-index: 1;
    }}
    .step-node {{
      position: relative;
      z-index: 2;
      display: flex;
      align-items: center;
      gap: 12px;
      background: #FFFFFF;
      padding: 10px 22px;
      border-radius: 9999px;
      border: 1px solid rgba(220, 214, 204, 0.8);
      box-shadow: 0 8px 20px rgba(45, 35, 20, 0.06);
      transition: all 0.3s ease;
    }}
    .step-node.active {{
      border: 2px solid #C58B35;
      background: #FFFBEB;
      transform: scale(1.05);
      box-shadow: 0 10px 24px rgba(197, 139, 53, 0.2);
    }}
    .step-icon {{ font-size: 20px; }}
    .step-text {{ font-size: 16px; font-weight: 800; color: #1E2024; }}

    /* Center Main Workspace Card */
    .workspace-card {{
      position: absolute;
      top: 240px;
      left: 200px;
      width: 1520px;
      height: 600px;
      background: #FFFFFF;
      border-radius: 28px;
      border: 1px solid rgba(220, 214, 204, 0.75);
      box-shadow: 0 20px 48px -8px rgba(45, 35, 20, 0.08), 0 6px 16px rgba(45, 35, 20, 0.03), inset 0 1px 0 #FFFFFF;
      display: flex;
      overflow: hidden;
      z-index: 20;
    }}

    /* Left Column: Chat Dialogue */
    .chat-col {{
      width: 58%;
      background: #FCFAF7;
      border-right: 1px solid rgba(224, 218, 208, 0.7);
      padding: 36px 40px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .bubble {{
      padding: 20px 26px;
      border-radius: 20px;
      font-size: 18px;
      line-height: 1.6;
      max-width: 90%;
      position: relative;
    }}
    .user-bubble {{
      align-self: flex-start;
      background: #FFFFFF;
      border: 1.5px solid rgba(215, 208, 196, 0.8);
      color: #1E2024;
      font-weight: 700;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.03);
    }}
    .ai-bubble {{
      align-self: flex-start;
      background: #FFFBEB;
      border: 1.5px solid #FDE68A;
      color: #92400E;
      font-weight: 600;
      box-shadow: 0 8px 20px rgba(245, 158, 11, 0.08);
    }}

    /* Right Column: PRD Checklist & Auto Coding */
    .prd-col {{
      width: 42%;
      background: #FFFFFF;
      padding: 36px 36px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .prd-header {{
      font-size: 20px;
      font-weight: 800;
      color: #1E2024;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .check-list {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .check-item {{
      display: flex;
      align-items: center;
      gap: 14px;
      font-size: 16px;
      font-weight: 700;
      color: #334155;
    }}
    .check-box {{
      width: 24px;
      height: 24px;
      border-radius: 6px;
      border: 2px solid #CBD5E1;
      display: flex;
      align-items: center;
      justify-content: center;
      color: transparent;
      transition: all 0.25s ease;
    }}
    .check-item.done .check-box {{
      background: #10B981;
      border-color: #10B981;
      color: #FFFFFF;
    }}
    .check-item.done {{
      color: #0F172A;
    }}

    /* Coding Progress Bar */
    .progress-box {{
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 16px;
      padding: 20px;
      margin-top: 20px;
    }}
    .progress-top {{
      display: flex;
      justify-content: space-between;
      font-size: 14px;
      font-weight: 800;
      color: #475569;
      margin-bottom: 10px;
    }}
    .progress-bar-bg {{
      height: 10px;
      background: #E2E8F0;
      border-radius: 999px;
      overflow: hidden;
    }}
    .progress-bar-fill {{
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #3B82F6, #10B981);
      border-radius: 999px;
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

    <!-- Flow Pipeline -->
    <div class="flow-pipeline" id="s4-pipeline">
      <div class="pipeline-line-bg"></div>
      <div class="step-node active"><span class="step-icon">💡</span><span class="step-text">01 灵感构想</span></div>
      <div class="step-node active" id="node-prd"><span class="step-icon">📝</span><span class="step-text">02 PRD 审查</span></div>
      <div class="step-node" id="node-code"><span class="step-icon">⚙️</span><span class="step-text">03 自动构建</span></div>
      <div class="step-node" id="node-deploy"><span class="step-icon">🚀</span><span class="step-text">04 极速交付</span></div>
    </div>

    <!-- Workspace Card -->
    <div class="workspace-card" id="s4-workspace">
      <!-- Left: Dialogue -->
      <div class="chat-col">
        <div class="bubble user-bubble" id="bubble-user">
          👤 想要一个全栈的「儿童英语分级绘本站」，支持 Level 1-6 绘本翻页、发音纠错和生词本。
        </div>
        <div class="bubble ai-bubble" id="bubble-ai" style="opacity: 0;">
          🤖 <strong>AI PM (Grill-me)</strong>：收到！已规划三大核心模块：<br>
          1. 绘本分级与词汇量权重算法<br>
          2. Web Speech 实时语音发音打分<br>
          3. Supabase 用户进度数据同步
        </div>
      </div>

      <!-- Right: PRD Checklist -->
      <div class="prd-col">
        <div>
          <div class="prd-header">
            <span>📋</span> PRD 规范与任务检查单
          </div>
          <div class="check-list">
            <div class="check-item" id="check-1"><div class="check-box">✓</div> 页面响应式与无障碍交互</div>
            <div class="check-item" id="check-2"><div class="check-box">✓</div> 智能语音打分容错机制</div>
            <div class="check-item" id="check-3"><div class="check-box">✓</div> Supabase 数据库表结构初始化</div>
            <div class="check-item" id="check-4"><div class="check-box">✓</div> 自动化单元测试用例通过</div>
          </div>
        </div>

        <div class="progress-box">
          <div class="progress-top">
            <span>AI Code Generation</span>
            <span id="prog-pct">0%</span>
          </div>
          <div class="progress-bar-bg">
            <div class="progress-bar-fill" id="prog-fill"></div>
          </div>
        </div>
      </div>
    </div>

    {render_presenter_hud("../assets/avatar.jpg", "s4-avatar")}
    {render_subtitle_hud("", "s4-sub")}
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});

    tl.fromTo("#s4-pipeline", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.3);
    tl.fromTo("#s4-workspace", {{ opacity: 0, y: 30, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.8, ease: "power2.out" }}, 0.6);

    // AI Bubble appears
    tl.to("#bubble-ai", {{ opacity: 1, y: 0, duration: 0.5 }}, 5.0);

    // Checklist ticks
    tl.call(() => document.getElementById("check-1").classList.add("done"), null, 8.0);
    tl.call(() => document.getElementById("check-2").classList.add("done"), null, 9.5);
    tl.call(() => document.getElementById("check-3").classList.add("done"), null, 11.0);
    tl.call(() => document.getElementById("check-4").classList.add("done"), null, 12.5);

    // Coding progress
    tl.to("#prog-fill", {{ width: "100%", duration: 6.0, ease: "power1.inOut" }}, 13.0);
    tl.call(() => {{
      const pct = document.getElementById("prog-pct");
      if (pct) pct.innerText = "100%";
      document.getElementById("node-code").classList.add("active");
    }}, null, 19.0);

    // Subtitles
    {"".join(sub_timeline_js)}

    // Avatar breathing
    tl.fromTo("#s4-avatar", {{ y: 0 }}, {{ y: -6, duration: 1.6, yoyo: true, repeat: 12, ease: "sine.inOut" }}, 0.2);

    // Exit fadeout
    tl.to("#root", {{ opacity: 0, duration: 0.25 }}, {duration - 0.25});

    window.__timelines = window.__timelines || {{}};
    window.__timelines["{scene_id}"] = tl;
  </script>
</template>
"""

