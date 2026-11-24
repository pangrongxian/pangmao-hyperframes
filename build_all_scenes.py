import os

base_dir = "/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes"

# ----------------- SCENE 1 -----------------
scene1 = '''<template>
  <style>
    @font-face {
      font-family: "PingFang SC";
      src: local("PingFang SC");
      font-display: swap;
    }
    #root {
      position: absolute;
      inset: 0;
      overflow: hidden;
      font-family: "PingFang SC", -apple-system, sans-serif;
      color: #f8fafc;
    }

    .browser-card {
      position: absolute;
      top: 130px;
      left: 140px;
      width: 1050px;
      height: 610px;
      background: #090d16;
      border-radius: 16px;
      border: 1px solid rgba(56, 189, 248, 0.25);
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.7), 0 0 35px rgba(56, 189, 248, 0.12);
      overflow: hidden;
      transform-origin: left center;
    }
    .browser-header {
      height: 44px;
      background: #111827;
      display: flex;
      align-items: center;
      padding: 0 18px;
      gap: 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .mac-dots {
      display: flex;
      gap: 8px;
    }
    .mac-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
    }
    .dot-r { background: #ef4444; }
    .dot-y { background: #f59e0b; }
    .dot-g { background: #10b981; }
    .url-bar {
      flex: 1;
      max-width: 540px;
      height: 28px;
      background: rgba(0, 0, 0, 0.4);
      border-radius: 6px;
      display: flex;
      align-items: center;
      padding: 0 14px;
      font-size: 13px;
      color: #94a3b8;
      font-family: monospace;
    }
    .url-hl {
      color: #38bdf8;
      font-weight: 700;
    }
    .browser-content {
      position: relative;
      width: 100%;
      height: calc(100% - 44px);
      overflow: hidden;
    }
    .browser-content img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
    }

    .hook-right {
      position: absolute;
      top: 150px;
      right: 120px;
      width: 520px;
      display: flex;
      flex-direction: column;
      gap: 22px;
    }
    .tag-hook {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      align-self: flex-start;
      padding: 6px 14px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.4);
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 700;
      color: #38bdf8;
      letter-spacing: 0.05em;
    }
    .hook-title {
      font-size: 46px;
      font-weight: 900;
      line-height: 1.25;
      letter-spacing: -0.02em;
    }
    .text-glow {
      color: #38bdf8;
      text-shadow: 0 0 20px rgba(56, 189, 248, 0.5);
    }
    .hook-desc {
      font-size: 20px;
      line-height: 1.6;
      color: #94a3b8;
      font-weight: 500;
    }

    .skills-dynamic-stage {
      position: absolute;
      inset: 0;
      opacity: 0;
      pointer-events: none;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .skill-cut-window {
      position: absolute;
      top: 120px;
      width: 1200px;
      height: 660px;
      background: #0b1120;
      border-radius: 20px;
      border: 1px solid rgba(56, 189, 248, 0.4);
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.8), 0 0 40px rgba(56, 189, 248, 0.2);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .skill-cut-header {
      height: 52px;
      background: #0f172a;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .skill-cut-title {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 16px;
      font-weight: 800;
    }
    .cut-badge {
      padding: 4px 14px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 800;
    }
    .badge-sql { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid #38bdf8; }
    .badge-ppt { background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid #fbbf24; }
    .badge-write { background: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid #c084fc; }
    .badge-canvas { background: rgba(236, 72, 153, 0.2); color: #f472b6; border: 1px solid #f472b6; }
    .cut-img-body {
      flex: 1;
      width: 100%;
      overflow: hidden;
      position: relative;
    }
    .cut-img-body img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
    }

    .sql-mock-content {
      padding: 40px 60px;
      display: flex;
      flex-direction: column;
      gap: 24px;
      background: #070d17;
      height: 100%;
    }
    .sql-code-box {
      background: #020617;
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 12px;
      padding: 24px;
      font-family: monospace;
      font-size: 18px;
      line-height: 1.8;
      color: #38bdf8;
    }
    .sql-table-mock {
      width: 100%;
      border-collapse: collapse;
      font-size: 15px;
      color: #cbd5e1;
    }
    .sql-table-mock th, .sql-table-mock td {
      padding: 12px 18px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      text-align: left;
    }
    .sql-table-mock th {
      background: rgba(15, 23, 42, 0.8);
      color: #38bdf8;
    }

    .avatar-hud {
      position: absolute;
      bottom: 80px;
      left: 56px;
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 20px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      z-index: 60;
    }
    .avatar-img-wrap {
      width: 54px;
      height: 54px;
      border-radius: 50%;
      overflow: hidden;
      border: 2px solid #38bdf8;
    }
    .avatar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .avatar-meta {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .avatar-title {
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
    }
    .avatar-tag {
      font-size: 11px;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.15);
      padding: 2px 6px;
      border-radius: 4px;
    }
    .avatar-status {
      font-size: 12px;
      color: #94a3b8;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .status-pulse {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
    }

    .subtitles-pill {
      position: absolute;
      bottom: 80px;
      left: 360px;
      right: 360px;
      padding: 12px 28px;
      background: rgba(10, 15, 26, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6);
      text-align: center;
      z-index: 60;
    }
    .sub-text {
      font-size: 28px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-hl { color: #38bdf8; }
    .sub-gold { color: #fbbf24; }
    .sub-purple { color: #c084fc; }
    .sub-pink { color: #f472b6; }
  </style>

  <div id="root" data-composition-id="scene1" data-width="1920" data-height="1080" data-hold>
    <div id="s1-part1">
      <div class="browser-card" id="s1-browser">
        <div class="browser-header">
          <div class="mac-dots">
            <div class="mac-dot dot-r"></div>
            <div class="mac-dot dot-y"></div>
            <div class="mac-dot dot-g"></div>
          </div>
          <div class="url-bar" data-layout-ignore>
            https://<span class="url-hl">skills.sh</span>/
          </div>
        </div>
        <div class="browser-content">
          <img src="assets/skills_sh_latest.png" alt="skills.sh 最新界面" />
        </div>
      </div>

      <div class="hook-right" id="s1-hook-right">
        <div class="tag-hook" data-layout-ignore>⚡️ 颠覆式 AI 技能生态</div>
        <h1 class="hook-title">
          一不小心加了个 <span class="text-glow">.sh</span><br />
          推开新世界大门
        </h1>
        <p class="hook-desc" data-layout-ignore>
          这不是普通网站，这是全球最大的 AI Agent Skills 技能库，赋予 AI 真实的工程执行力。
        </p>
      </div>
    </div>

    <!-- Part 2: Dynamic Multi-Cut Windows (8.5s - 14.0s) -->
    <div class="skills-dynamic-stage" id="cut-sql">
      <div class="skill-cut-window">
        <div class="skill-cut-header" data-layout-ignore>
          <div class="skill-cut-title">
            <span>🗄️ Database Query Agent</span>
            <span class="cut-badge badge-sql">连数据库 SQL · 秒级生产数据</span>
          </div>
          <div style="color: #38bdf8; font-size: 13px; font-weight: bold;">● LIVE CONNECTED</div>
        </div>
        <div class="sql-mock-content" data-layout-ignore>
          <div class="sql-code-box">
            <span style="color: #64748b;">-- AI Agent 自动挂载 SQL Skill</span><br />
            <span style="color: #f43f5e;">SELECT</span> id, user_name, total_skills, created_at <br />
            <span style="color: #f43f5e;">FROM</span> production_agents <br />
            <span style="color: #f43f5e;">WHERE</span> status = 'active' <span style="color: #f43f5e;">LIMIT</span> 5;
          </div>
          <table class="sql-table-mock">
            <thead>
              <tr><th>Agent ID</th><th>名称</th><th>挂载 Skills 数量</th><th>状态</th></tr>
            </thead>
            <tbody>
              <tr><td>AG-9801</td><td>Cursor Fullstack PM</td><td>12 核心技能</td><td><span style="color:#10b981;">● RUNNING</span></td></tr>
              <tr><td>AG-9802</td><td>KidsLingo Senior Engineer</td><td>8 前后端技能</td><td><span style="color:#10b981;">● COMPILED</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="skills-dynamic-stage" id="cut-ppt">
      <div class="skill-cut-window">
        <div class="skill-cut-header" data-layout-ignore>
          <div class="skill-cut-title">
            <span>📊 anthropic/skills/pptx</span>
            <span class="cut-badge badge-ppt">一键生成 PPT · 261.6K 安装</span>
          </div>
          <div style="color: #fbbf24; font-size: 13px; font-weight: bold;">★ 199.0K STARS</div>
        </div>
        <div class="cut-img-body">
          <img src="assets/skill_pptx.png" alt="pptx skill" />
        </div>
      </div>
    </div>

    <div class="skills-dynamic-stage" id="cut-writing">
      <div class="skill-cut-window">
        <div class="skill-cut-header" data-layout-ignore>
          <div class="skill-cut-title">
            <span>📝 obra/superpowers/writing-plans</span>
            <span class="cut-badge badge-write">长文深度写作 · 313.1K 安装</span>
          </div>
          <div style="color: #c084fc; font-size: 13px; font-weight: bold;">★ 324.1K STARS</div>
        </div>
        <div class="cut-img-body">
          <img src="assets/skill_writing_plans.png" alt="writing plans skill" />
        </div>
      </div>
    </div>

    <div class="skills-dynamic-stage" id="cut-canvas">
      <div class="skill-cut-window">
        <div class="skill-cut-header" data-layout-ignore>
          <div class="skill-cut-title">
            <span>🎨 anthropic/skills/canvas-design</span>
            <span class="cut-badge badge-canvas">全景爆款海报 · 138.2K 安装</span>
          </div>
          <div style="color: #f472b6; font-size: 13px; font-weight: bold;">★ 199.0K STARS</div>
        </div>
        <div class="cut-img-body">
          <img src="assets/skill_canvas_design.png" alt="canvas design skill" />
        </div>
      </div>
    </div>

    <div class="avatar-hud" id="s1-avatar" data-layout-ignore>
      <div class="avatar-img-wrap">
        <img src="assets/avatar.jpg" alt="胖猫AI" />
      </div>
      <div class="avatar-meta">
        <div class="avatar-title">胖猫AI <span class="avatar-tag">主理人</span></div>
        <div class="avatar-status"><span class="status-pulse"></span>正在实测讲解</div>
      </div>
    </div>

    <div class="subtitles-pill" id="s1-sub">
      <span class="sub-text" id="s1-sub-text">当你一不小心在 skills 后面加了个 <span class="sub-hl">sh</span>...</span>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({ paused: true });

    tl.fromTo("#s1-browser", 
      { opacity: 0, x: -60, rotateY: 10, scale: 0.94 }, 
      { opacity: 1, x: 0, rotateY: 0, scale: 1, duration: 1.2, ease: "power3.out" }, 
      0.1
    );

    // subtle float on browser
    tl.to("#s1-browser", { y: "-=8", duration: 2.0, yoyo: true, repeat: 3, ease: "sine.inOut" }, 1.3);

    tl.fromTo("#s1-hook-right", 
      { opacity: 0, x: 50, filter: "blur(10px)" }, 
      { opacity: 1, x: 0, filter: "blur(0px)", duration: 1.1, ease: "power3.out" }, 
      0.3
    );

    tl.fromTo("#s1-avatar", 
      { opacity: 0, y: 30, scale: 0.8 }, 
      { opacity: 1, y: 0, scale: 1, duration: 0.8, ease: "back.out(1.5)" }, 
      0.4
    );

    tl.fromTo("#s1-sub", 
      { opacity: 0, y: 20 }, 
      { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 
      0.2
    );

    tl.call(() => {
      const el = document.getElementById("s1-sub-text");
      if (el) el.innerHTML = "你就进入了这个全球最大的 <span class='sub-hl'>AI Agent Skills</span> 技能库！";
    }, null, 4.0);

    tl.to("#s1-part1", { opacity: 0, scale: 0.92, duration: 0.35, ease: "power2.in" }, 8.15);

    // Cut 1 (8.52s)
    tl.call(() => {
      const el = document.getElementById("s1-sub-text");
      if (el) el.innerHTML = "有帮你<span class='sub-hl'>连数据库的</span>...";
      document.getElementById("cut-sql").style.opacity = "1";
    }, null, 8.52);
    tl.fromTo("#cut-sql .skill-cut-window", 
      { opacity: 0, scale: 0.85, y: 40 }, 
      { opacity: 1, scale: 1, y: 0, duration: 0.35, ease: "back.out(1.5)" }, 
      8.52
    );

    // Cut 2 (9.80s)
    tl.call(() => {
      const el = document.getElementById("s1-sub-text");
      if (el) el.innerHTML = "有帮你连数据库的、<span class='sub-gold'>做 PPT 的</span>...";
      document.getElementById("cut-sql").style.opacity = "0";
      document.getElementById("cut-ppt").style.opacity = "1";
    }, null, 9.80);
    tl.fromTo("#cut-ppt .skill-cut-window", 
      { opacity: 0, scale: 0.88, x: 50 }, 
      { opacity: 1, scale: 1, x: 0, duration: 0.35, ease: "power3.out" }, 
      9.80
    );

    // Cut 3 (11.10s)
    tl.call(() => {
      const el = document.getElementById("s1-sub-text");
      if (el) el.innerHTML = "做 PPT 的、<span class='sub-purple'>写长文的</span>...";
      document.getElementById("cut-ppt").style.opacity = "0";
      document.getElementById("cut-writing").style.opacity = "1";
    }, null, 11.10);
    tl.fromTo("#cut-writing .skill-cut-window", 
      { opacity: 0, scale: 0.88, x: -50 }, 
      { opacity: 1, scale: 1, x: 0, duration: 0.35, ease: "power3.out" }, 
      11.10
    );

    // Cut 4 (12.40s)
    tl.call(() => {
      const el = document.getElementById("s1-sub-text");
      if (el) el.innerHTML = "写长文的、<span class='sub-pink'>做海报的</span>。功能一应俱全！";
      document.getElementById("cut-writing").style.opacity = "0";
      document.getElementById("cut-canvas").style.opacity = "1";
    }, null, 12.40);
    tl.fromTo("#cut-canvas .skill-cut-window", 
      { opacity: 0, scale: 0.88, y: 40 }, 
      { opacity: 1, scale: 1, y: 0, duration: 0.35, ease: "back.out(1.5)" }, 
      12.40
    );

    tl.fromTo("#s1-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 7, ease: "sine.inOut" }, 1.3);

    tl.to("#root", { opacity: 0, scale: 0.97, filter: "blur(6px)", duration: 0.4, ease: "power2.inOut" }, 13.6);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene1"] = tl;
  </script>
</template>
'''

# ----------------- SCENE 2 -----------------
scene2 = '''<template>
  <style>
    @font-face {
      font-family: "PingFang SC";
      src: local("PingFang SC");
      font-display: swap;
    }
    #root {
      position: absolute;
      inset: 0;
      overflow: hidden;
      font-family: "PingFang SC", -apple-system, sans-serif;
      color: #f8fafc;
    }

    .hero-center {
      position: absolute;
      top: 130px;
      left: 0;
      right: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 16px;
    }
    .badge-capsule {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 8px 24px;
      background: rgba(14, 165, 233, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.45);
      border-radius: 9999px;
      font-size: 15px;
      font-weight: 800;
      color: #38bdf8;
      letter-spacing: 0.08em;
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.25);
    }
    .stat-number {
      font-size: 110px;
      font-weight: 900;
      line-height: 1;
      letter-spacing: -0.04em;
      background: linear-gradient(135deg, #ffffff 30%, #38bdf8 80%, #2563eb 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 10px 30px rgba(56, 189, 248, 0.35));
    }
    .stat-label {
      font-size: 28px;
      font-weight: 800;
      color: #94a3b8;
    }

    .golden-banner {
      position: absolute;
      top: 410px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: 24px;
      padding: 16px 42px;
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.25), rgba(217, 119, 6, 0.15));
      border: 2px solid rgba(245, 158, 11, 0.85);
      border-radius: 20px;
      backdrop-filter: blur(20px);
      box-shadow: 0 16px 50px rgba(245, 158, 11, 0.35), 0 0 30px rgba(245, 158, 11, 0.2);
    }
    .golden-text {
      font-size: 46px;
      font-weight: 900;
      color: #fbbf24;
      text-shadow: 0 0 25px rgba(245, 158, 11, 0.6);
      letter-spacing: 0.02em;
    }
    .golden-sub {
      font-size: 20px;
      font-weight: 700;
      color: #fde68a;
    }

    .vibe-showcase {
      position: absolute;
      bottom: 210px;
      left: 200px;
      right: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 28px;
    }
    .vibe-card {
      flex: 1;
      max-width: 440px;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 16px;
      padding: 20px 26px;
      display: flex;
      align-items: center;
      gap: 16px;
      backdrop-filter: blur(16px);
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5);
    }
    .vibe-icon {
      font-size: 32px;
    }
    .vibe-info h5 {
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 4px;
    }
    .vibe-info p {
      font-size: 14px;
      color: #94a3b8;
    }

    .avatar-hud {
      position: absolute;
      bottom: 80px;
      left: 56px;
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 20px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      z-index: 60;
    }
    .avatar-img-wrap {
      width: 54px;
      height: 54px;
      border-radius: 50%;
      overflow: hidden;
      border: 2px solid #38bdf8;
    }
    .avatar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .avatar-meta {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .avatar-title {
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
    }
    .avatar-status {
      font-size: 12px;
      color: #38bdf8;
      font-weight: 600;
    }

    .subtitles-pill {
      position: absolute;
      bottom: 80px;
      left: 360px;
      right: 360px;
      padding: 12px 28px;
      background: rgba(10, 15, 26, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6);
      text-align: center;
      z-index: 60;
    }
    .sub-text {
      font-size: 28px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-hl { color: #38bdf8; }
    .sub-gold { color: #fbbf24; }
  </style>

  <div id="root" data-composition-id="scene2" data-width="1920" data-height="1080" data-hold>
    <div class="hero-center" id="s2-hero">
      <div class="badge-capsule" data-layout-ignore>
        <span>🌐 2026 官方实时收录数据</span>
      </div>
      <div class="stat-number" id="s2-counter">1,517,216+</div>
      <div class="stat-label">全球海量即时装配的智能体技能</div>
    </div>

    <div class="golden-banner" id="s2-golden">
      <span class="golden-text">全免费！无限扩展</span>
      <span class="golden-sub" data-layout-ignore>无需注册绑定 · 一键装载</span>
    </div>

    <div class="vibe-showcase" id="s2-vibe" data-layout-ignore>
      <div class="vibe-card card-1">
        <div class="vibe-icon">🎓</div>
        <div class="vibe-info">
          <h5>零基础文科生友好</h5>
          <p>无需懂复杂的底层代码架构</p>
        </div>
      </div>
      <div class="vibe-card card-2">
        <div class="vibe-icon">✨</div>
        <div class="vibe-info">
          <h5>Vibe Coding 魔法</h5>
          <p>自然语言意图驱动，AI 自动编译</p>
        </div>
      </div>
      <div class="vibe-card card-3">
        <div class="vibe-icon">🚀</div>
        <div class="vibe-info">
          <h5>手搓全功能网站</h5>
          <p>从头脑风暴到前后端部署 3 分钟</p>
        </div>
      </div>
    </div>

    <div class="avatar-hud" id="s2-avatar" data-layout-ignore>
      <div class="avatar-img-wrap">
        <img src="assets/avatar.jpg" alt="胖猫AI" />
      </div>
      <div class="avatar-meta">
        <div class="avatar-title">胖猫AI</div>
        <div class="avatar-status">⚡️ 151万+ Skills 实操</div>
      </div>
    </div>

    <div class="subtitles-pill" id="s2-sub">
      <span class="sub-text" id="s2-sub-text">面对如今浩如烟海的 <span class="sub-hl">151 万多个 skills</span>...</span>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({ paused: true });

    tl.fromTo("#s2-hero", 
      { opacity: 0, y: 50, scale: 0.9 }, 
      { opacity: 1, y: 0, scale: 1, duration: 1.0, ease: "back.out(1.4)" }, 
      0.1
    );

    // subtle floating
    tl.to("#s2-hero", { y: "-=10", duration: 2.2, yoyo: true, repeat: 3, ease: "sine.inOut" }, 1.2);

    tl.fromTo("#s2-golden", 
      { opacity: 0, scale: 0.7, rotate: -4 }, 
      { opacity: 1, scale: 1, rotate: 0, duration: 0.7, ease: "elastic.out(1, 0.6)" }, 
      1.8
    );

    tl.call(() => {
      const el = document.getElementById("s2-sub-text");
      if (el) el.innerHTML = "哪怕你是<span class='sub-hl'>零基础文科生</span>，也能通过 <span class='sub-gold'>Vibe Coding</span> 轻松手搓出全功能网站！";
    }, null, 4.0);

    tl.fromTo("#s2-vibe .vibe-card", 
      { opacity: 0, y: 40, scale: 0.9 }, 
      { opacity: 1, y: 0, scale: 1, duration: 0.6, stagger: 0.15, ease: "power3.out" }, 
      4.2
    );

    // gentle wave animation on vibe cards to prevent dead stretch
    tl.to("#s2-vibe .vibe-card", { y: "-=6", duration: 1.8, yoyo: true, repeat: 2, stagger: 0.2, ease: "sine.inOut" }, 5.5);

    tl.fromTo("#s2-avatar", 
      { opacity: 0, scale: 0.8 }, 
      { opacity: 1, scale: 1, duration: 0.6, ease: "power2.out" }, 
      0.3
    );

    tl.fromTo("#s2-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 5, ease: "sine.inOut" }, 1.1);

    tl.to("#root", { opacity: 0, scale: 1.05, filter: "blur(6px)", duration: 0.5, ease: "power2.inOut" }, 10.0);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene2"] = tl;
  </script>
</template>
'''

# ----------------- SCENE 3 -----------------
scene3 = '''<template>
  <style>
    @font-face {
      font-family: "PingFang SC";
      src: local("PingFang SC");
      font-display: swap;
    }
    #root {
      position: absolute;
      inset: 0;
      overflow: hidden;
      font-family: "PingFang SC", -apple-system, sans-serif;
      color: #f8fafc;
    }

    .brainstorm-stage {
      position: absolute;
      top: 110px;
      left: 140px;
      width: 1100px;
      height: 640px;
      background: #090d16;
      border-radius: 20px;
      border: 1px solid rgba(56, 189, 248, 0.35);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7), 0 0 35px rgba(56, 189, 248, 0.15);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .window-header {
      height: 48px;
      background: #111827;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
    }
    .window-title {
      font-size: 14px;
      font-weight: 800;
      color: #38bdf8;
    }
    .window-body {
      flex: 1;
      width: 100%;
      overflow: hidden;
    }
    .window-body img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
    }

    .action-side-card {
      position: absolute;
      top: 150px;
      right: 140px;
      width: 480px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .step-badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      align-self: flex-start;
      padding: 8px 18px;
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.5);
      border-radius: 9999px;
      font-size: 14px;
      font-weight: 800;
      color: #38bdf8;
    }
    .step-headline {
      font-size: 40px;
      font-weight: 900;
      color: #ffffff;
      line-height: 1.25;
    }
    .copy-pill-card {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 14px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .cmd-text {
      font-family: monospace;
      font-size: 14px;
      color: #a5f3fc;
      background: #020617;
      padding: 12px 16px;
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.08);
      word-break: break-all;
    }
    .copy-btn {
      padding: 12px 24px;
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
    }
    .copied-badge {
      display: none;
      padding: 8px 16px;
      background: #10b981;
      color: #ffffff;
      border-radius: 8px;
      font-size: 15px;
      font-weight: 800;
      text-align: center;
    }

    .cursor-real-stage {
      position: absolute;
      top: 100px;
      left: 120px;
      right: 120px;
      height: 670px;
      background: #0b1120;
      border-radius: 20px;
      border: 2px solid rgba(168, 85, 247, 0.5);
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.8), 0 0 40px rgba(168, 85, 247, 0.25);
      overflow: hidden;
      display: none;
      flex-direction: column;
    }
    .cursor-real-header {
      height: 48px;
      background: #111827;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .cursor-real-title {
      font-size: 15px;
      font-weight: 800;
      color: #c084fc;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .cursor-real-body {
      flex: 1;
      width: 100%;
      position: relative;
    }
    .cursor-real-body img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
    }
    .installed-floating-pill {
      position: absolute;
      bottom: 40px;
      right: 40px;
      padding: 14px 28px;
      background: rgba(16, 185, 129, 0.95);
      border: 2px solid #ffffff;
      border-radius: 9999px;
      font-size: 18px;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 12px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.6);
      z-index: 30;
    }

    .avatar-hud {
      position: absolute;
      bottom: 80px;
      left: 56px;
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 20px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      z-index: 60;
    }
    .avatar-img-wrap {
      width: 54px;
      height: 54px;
      border-radius: 50%;
      overflow: hidden;
      border: 2px solid #38bdf8;
    }
    .avatar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .avatar-meta {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .avatar-title {
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
    }
    .avatar-status {
      font-size: 12px;
      color: #c084fc;
      font-weight: 600;
    }

    .subtitles-pill {
      position: absolute;
      bottom: 80px;
      left: 360px;
      right: 360px;
      padding: 12px 28px;
      background: rgba(10, 15, 26, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6);
      text-align: center;
      z-index: 60;
    }
    .sub-text {
      font-size: 28px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-hl { color: #38bdf8; }
    .sub-green { color: #34d399; }
    .sub-purple { color: #c084fc; }
  </style>

  <div id="root" data-composition-id="scene3" data-width="1920" data-height="1080" data-hold>
    <div id="s3-stage1">
      <div class="brainstorm-stage" id="s3-brainstorm-win">
        <div class="window-header" data-layout-ignore>
          <div class="window-title">skills / obra / superpowers / brainstorming (439.5K 安装)</div>
          <div style="color: #38bdf8; font-size: 12px; font-weight: bold;">● SKILLS.SH LEADERBOARD</div>
        </div>
        <div class="window-body">
          <img src="assets/skill_brainstorming.png" alt="Brainstorming Skill" />
        </div>
      </div>

      <div class="action-side-card" id="s3-action-card">
        <div class="step-badge" data-layout-ignore>STEP 01 · 复制技能</div>
        <h2 class="step-headline">
          选中「头脑风暴」<br />
          一键秒复制
        </h2>
        <div class="copy-pill-card" data-layout-ignore>
          <div style="font-size: 13px; color: #94a3b8;">Terminal 安装命令：</div>
          <div class="cmd-text">$ npx skills add ... --skill brainstorming</div>
          <button class="copy-btn" id="s3-copy-btn">
            <span>📋 点击复制命令</span>
          </button>
          <div class="copied-badge" id="s3-copied-badge">✓ 已复制到剪贴板！</div>
        </div>
      </div>
    </div>

    <!-- Stage 2: Real Cursor Interface Cut -->
    <div class="cursor-real-stage" id="s3-cursor-stage">
      <div class="cursor-real-header" data-layout-ignore>
        <div class="cursor-real-title">
          <span>⚡️ Cursor Composer / Chat 实机环境</span>
          <span style="font-size: 12px; color: #a855f7; border: 1px solid #a855f7; padding: 2px 8px; border-radius: 9999px;">STEP 02</span>
        </div>
        <div style="color: #10b981; font-size: 13px; font-weight: bold;">● COMMAND EXECUTED</div>
      </div>
      <div class="cursor-real-body">
        <img src="assets/real_cursor_user.png" alt="Cursor Real Chat" />
        <div class="installed-floating-pill" id="s3-installed-badge" data-layout-ignore>
          <span>✓</span>
          <span>头脑风暴 Skill 载入完成 (1.2s)</span>
        </div>
      </div>
    </div>

    <div class="avatar-hud" id="s3-avatar" data-layout-ignore>
      <div class="avatar-img-wrap">
        <img src="assets/avatar.jpg" alt="胖猫AI" />
      </div>
      <div class="avatar-meta">
        <div class="avatar-title">胖猫AI</div>
        <div class="avatar-status">⚡️ 实测安装流程</div>
      </div>
    </div>

    <div class="subtitles-pill" id="s3-sub">
      <span class="sub-text" id="s3-sub-text">操作极度丝滑：在 skills.sh 上选中「头脑风暴」skill，点击复制...</span>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({ paused: true });

    tl.fromTo("#s3-brainstorm-win", 
      { opacity: 0, x: -60, scale: 0.95 }, 
      { opacity: 1, x: 0, scale: 1, duration: 0.9, ease: "power3.out" }, 
      0.1
    );

    // subtle floating on window
    tl.to("#s3-brainstorm-win", { y: "-=8", duration: 1.8, yoyo: true, repeat: 2, ease: "sine.inOut" }, 1.0);

    tl.fromTo("#s3-action-card", 
      { opacity: 0, x: 50 }, 
      { opacity: 1, x: 0, duration: 0.8, ease: "power3.out" }, 
      0.3
    );

    tl.to("#s3-copy-btn", { scale: 0.92, duration: 0.15, yoyo: true, repeat: 1 }, 2.8);
    tl.call(() => {
      const btn = document.getElementById("s3-copy-btn");
      const badge = document.getElementById("s3-copied-badge");
      if (btn) btn.style.display = "none";
      if (badge) badge.style.display = "block";
    }, null, 3.0);

    // Dynamic cut at 5.5s
    tl.call(() => {
      const el = document.getElementById("s3-sub-text");
      if (el) el.innerHTML = "随即打开 Cursor，把代码直接丢进对话框，<span class='sub-green'>下一秒技能就装好了！</span>";
      
      const s1 = document.getElementById("s3-stage1");
      const s2 = document.getElementById("s3-cursor-stage");
      if (s1) s1.style.display = "none";
      if (s2) s2.style.display = "flex";
    }, null, 5.5);

    tl.fromTo("#s3-cursor-stage", 
      { opacity: 0, scale: 0.9, y: 30 }, 
      { opacity: 1, scale: 1, y: 0, duration: 0.6, ease: "power3.out" }, 
      5.5
    );

    // slight zoom on cursor stage to keep visual active
    tl.to("#s3-cursor-stage", { scale: 1.03, duration: 5.0, ease: "power1.inOut" }, 6.2);

    tl.fromTo("#s3-installed-badge", 
      { opacity: 0, scale: 0.7, y: 20 }, 
      { opacity: 1, scale: 1, y: 0, duration: 0.6, ease: "back.out(1.8)" }, 
      6.5
    );

    tl.fromTo("#s3-avatar", 
      { opacity: 0, y: 20 }, 
      { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 
      0.3
    );

    tl.fromTo("#s3-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 6, ease: "sine.inOut" }, 1.0);

    tl.to("#root", { opacity: 0, scale: 0.96, filter: "blur(6px)", duration: 0.4, ease: "power2.inOut" }, 12.1);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene3"] = tl;
  </script>
</template>
'''

# ----------------- SCENE 4 -----------------
scene4 = '''<template>
  <style>
    @font-face {
      font-family: "PingFang SC";
      src: local("PingFang SC");
      font-display: swap;
    }
    #root {
      position: absolute;
      inset: 0;
      overflow: hidden;
      font-family: "PingFang SC", -apple-system, sans-serif;
      color: #f8fafc;
    }

    .cursor-ide-container {
      position: absolute;
      top: 120px;
      left: 100px;
      right: 100px;
      height: 660px;
      background: #0f141c;
      border-radius: 20px;
      border: 1px solid rgba(168, 85, 247, 0.4);
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8), 0 0 35px rgba(168, 85, 247, 0.2);
      overflow: hidden;
    }
    .cursor-ide-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
    }

    .intent-floating-card {
      position: absolute;
      top: 150px;
      left: 140px;
      width: 480px;
      background: rgba(15, 23, 42, 0.92);
      border: 1px solid rgba(56, 189, 248, 0.5);
      border-radius: 18px;
      padding: 22px 26px;
      backdrop-filter: blur(24px);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
      z-index: 20;
    }
    .intent-tag {
      font-size: 13px;
      font-weight: 800;
      color: #38bdf8;
      margin-bottom: 8px;
    }
    .intent-text {
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.5;
    }
    .intent-text span {
      color: #38bdf8;
    }

    .pm-floating-card {
      position: absolute;
      top: 310px;
      left: 140px;
      width: 480px;
      background: linear-gradient(135deg, rgba(168, 85, 247, 0.25), rgba(99, 102, 241, 0.2));
      border: 1px solid rgba(168, 85, 247, 0.7);
      border-radius: 18px;
      padding: 22px 26px;
      backdrop-filter: blur(24px);
      box-shadow: 0 20px 50px rgba(168, 85, 247, 0.3);
      z-index: 20;
    }
    .pm-tag {
      font-size: 13px;
      font-weight: 800;
      color: #c084fc;
      margin-bottom: 6px;
    }
    .pm-title {
      font-size: 24px;
      font-weight: 900;
      color: #ffffff;
      margin-bottom: 8px;
    }
    .pm-desc {
      font-size: 14px;
      color: #cbd5e1;
      line-height: 1.5;
    }

    .avatar-hud {
      position: absolute;
      bottom: 80px;
      left: 56px;
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 20px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      z-index: 60;
    }
    .avatar-img-wrap {
      width: 54px;
      height: 54px;
      border-radius: 50%;
      overflow: hidden;
      border: 2px solid #38bdf8;
    }
    .avatar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .avatar-meta {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .avatar-title {
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
    }
    .avatar-status {
      font-size: 12px;
      color: #c084fc;
      font-weight: 600;
    }

    .subtitles-pill {
      position: absolute;
      bottom: 80px;
      left: 360px;
      right: 360px;
      padding: 12px 28px;
      background: rgba(10, 15, 26, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6);
      text-align: center;
      z-index: 60;
    }
    .sub-text {
      font-size: 28px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-hl { color: #38bdf8; }
    .sub-purple { color: #c084fc; }
  </style>

  <div id="root" data-composition-id="scene4" data-width="1920" data-height="1080" data-hold>
    <div class="cursor-ide-container" id="s4-ide">
      <img src="assets/cursor_kidslingo_retina.png" class="cursor-ide-img" alt="Cursor IDE KidsLingo" />
    </div>

    <!-- Floating Intent Dialogue -->
    <div class="intent-floating-card" id="s4-intent">
      <div class="intent-tag" data-layout-ignore>PROMPT 指令输入：</div>
      <div class="intent-text">
        “我想做一个适合家长带孩子<span>学英语的网站</span>，先帮我<span>头脑风暴</span>，再写代码。”
      </div>
    </div>

    <!-- Floating PM Transformation Badge -->
    <div class="pm-floating-card" id="s4-pm">
      <div class="pm-tag" data-layout-ignore>⚡️ AGENT SKILLS 思考链激活</div>
      <div class="pm-title">👔 Cursor 变身顶尖产品经理</div>
      <div class="pm-desc" data-layout-ignore>
        梳理 4 大体系需求、自动输出完整 PRD 企划案，并立即自动编译 Next.js 全栈代码！
      </div>
    </div>

    <div class="avatar-hud" id="s4-avatar" data-layout-ignore>
      <div class="avatar-img-wrap">
        <img src="assets/avatar.jpg" alt="胖猫AI" />
      </div>
      <div class="avatar-meta">
        <div class="avatar-title">胖猫AI</div>
        <div class="avatar-status">⚡️ PRD 与全栈代码自动编译</div>
      </div>
    </div>

    <div class="subtitles-pill" id="s4-sub">
      <span class="sub-text" id="s4-sub-text">然后你对 Cursor 说：“我想做一个适合家长带孩子学英语的网站...”</span>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({ paused: true });

    tl.fromTo("#s4-ide", 
      { opacity: 0, scale: 0.94 }, 
      { opacity: 1, scale: 1, duration: 1.0, ease: "power3.out" }, 
      0.1
    );

    // Continuous camera pan across Cursor IDE to eliminate dead stretch
    tl.to("#s4-ide", { y: "-=12", duration: 7.0, ease: "sine.inOut" }, 1.0);

    tl.fromTo("#s4-intent", 
      { opacity: 0, x: -40, scale: 0.9 }, 
      { opacity: 1, x: 0, scale: 1, duration: 0.8, ease: "back.out(1.5)" }, 
      0.4
    );

    // 8.9s: PM Transform & Subtitle update
    tl.call(() => {
      const el = document.getElementById("s4-sub-text");
      if (el) el.innerHTML = "Cursor 瞬间变身<span class='sub-purple'>顶尖产品经理</span>，不仅梳理需求，还自动输出完整 PRD！";
    }, null, 8.9);

    tl.fromTo("#s4-pm", 
      { opacity: 0, y: 30, scale: 0.85 }, 
      { opacity: 1, y: 0, scale: 1, duration: 0.8, ease: "back.out(1.6)" }, 
      9.1
    );

    // 15.0s: Auto Coding
    tl.call(() => {
      const el = document.getElementById("s4-sub-text");
      if (el) el.innerHTML = "确认后，Cursor <span class='sub-hl'>直接开始自动写全栈代码</span>。";
    }, null, 15.0);

    tl.to("#s4-intent", { opacity: 0.15, duration: 0.6 }, 15.2);
    tl.to("#s4-pm", { opacity: 0.15, duration: 0.6 }, 15.2);
    tl.to("#s4-ide", { scale: 1.06, duration: 4.8, ease: "power1.inOut" }, 15.5);

    tl.fromTo("#s4-avatar", 
      { opacity: 0, y: 20 }, 
      { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 
      0.3
    );

    tl.fromTo("#s4-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 10, ease: "sine.inOut" }, 1.0);

    tl.to("#root", { opacity: 0, scale: 0.97, filter: "blur(6px)", duration: 0.5, ease: "power2.inOut" }, 20.3);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene4"] = tl;
  </script>
</template>
'''

# ----------------- SCENE 5 -----------------
scene5 = '''<template>
  <style>
    @font-face {
      font-family: "PingFang SC";
      src: local("PingFang SC");
      font-display: swap;
    }
    #root {
      position: absolute;
      inset: 0;
      overflow: hidden;
      font-family: "PingFang SC", -apple-system, sans-serif;
      color: #f8fafc;
    }

    .app-showcase {
      position: absolute;
      top: 110px;
      left: 100px;
      right: 100px;
      height: 670px;
      background: #090d16;
      border-radius: 20px;
      border: 2px solid rgba(16, 185, 129, 0.5);
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.7), 0 0 40px rgba(16, 185, 129, 0.25);
      overflow: hidden;
    }
    .app-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
    }

    .time-floating-pill {
      position: absolute;
      top: 130px;
      right: 130px;
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 14px 28px;
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.9), rgba(5, 150, 105, 0.9));
      border: 2px solid #ffffff;
      border-radius: 18px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      z-index: 20;
    }
    .time-num {
      font-size: 42px;
      font-weight: 900;
      color: #ffffff;
      line-height: 1;
    }
    .time-txt {
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
    }

    .feat-spotlight {
      position: absolute;
      padding: 12px 24px;
      background: rgba(15, 23, 42, 0.92);
      border: 1px solid rgba(16, 185, 129, 0.6);
      border-radius: 9999px;
      font-size: 18px;
      font-weight: 800;
      color: #34d399;
      box-shadow: 0 8px 25px rgba(0,0,0,0.6);
      backdrop-filter: blur(16px);
      z-index: 25;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .feat-1 { top: 220px; left: 140px; }
    .feat-2 { top: 380px; left: 140px; }
    .feat-3 { top: 220px; right: 140px; }
    .feat-4 { top: 380px; right: 140px; }

    .avatar-hud {
      position: absolute;
      bottom: 80px;
      left: 56px;
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 20px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      z-index: 60;
    }
    .avatar-img-wrap {
      width: 54px;
      height: 54px;
      border-radius: 50%;
      overflow: hidden;
      border: 2px solid #38bdf8;
    }
    .avatar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .avatar-meta {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .avatar-title {
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
    }
    .avatar-status {
      font-size: 12px;
      color: #34d399;
      font-weight: 600;
    }

    .subtitles-pill {
      position: absolute;
      bottom: 80px;
      left: 360px;
      right: 360px;
      padding: 12px 28px;
      background: rgba(10, 15, 26, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6);
      text-align: center;
      z-index: 60;
    }
    .sub-text {
      font-size: 28px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-green { color: #34d399; }
    .sub-hl { color: #38bdf8; }
  </style>

  <div id="root" data-composition-id="scene5" data-width="1920" data-height="1080" data-hold>
    <div class="app-showcase" id="s5-app">
      <img src="assets/kids_lingo_app_retina.png" class="app-img" alt="KidsLingo AI App" />
    </div>

    <!-- Floating Time Badge -->
    <div class="time-floating-pill" id="s5-time-badge" data-layout-ignore>
      <div class="time-num">3 min</div>
      <div class="time-txt">
        从零手搓上线<br />
        全功能独家交付
      </div>
    </div>

    <!-- 4 Feature Spotlights -->
    <div class="feat-spotlight feat-1" id="s5-f1" data-layout-ignore>📚 分级阅读文库 (AI 沉浸配音)</div>
    <div class="feat-spotlight feat-2" id="s5-f2" data-layout-ignore>🎙️ AI 实时发音纠错 (毫秒级评分)</div>
    <div class="feat-spotlight feat-3" id="s5-f3" data-layout-ignore>🌟 趣味生词本 (遗忘曲线复习)</div>
    <div class="feat-spotlight feat-4" id="s5-f4" data-layout-ignore>📊 家长伴学仪表盘 (多维学情)</div>

    <div class="avatar-hud" id="s5-avatar" data-layout-ignore>
      <div class="avatar-img-wrap">
        <img src="assets/avatar.jpg" alt="胖猫AI" />
      </div>
      <div class="avatar-meta">
        <div class="avatar-title">胖猫AI</div>
        <div class="avatar-status">⚡️ 原创作品实机展示</div>
      </div>
    </div>

    <div class="subtitles-pill" id="s5-sub">
      <span class="sub-text" id="s5-sub-text">只需要 <span class="sub-green">3 分钟</span>，你的网站就做好了！</span>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({ paused: true });

    tl.fromTo("#s5-app", 
      { opacity: 0, y: 50, scale: 0.96 }, 
      { opacity: 1, y: 0, scale: 1, duration: 1.0, ease: "power3.out" }, 
      0.1
    );

    // gentle app zoom to prevent dead stretch
    tl.to("#s5-app", { scale: 1.03, duration: 5.0, ease: "sine.inOut" }, 1.2);

    tl.fromTo("#s5-time-badge", 
      { opacity: 0, scale: 0.7 }, 
      { opacity: 1, scale: 1, duration: 0.8, ease: "back.out(1.8)" }, 
      0.5
    );

    // 4.5s: Subtitle update
    tl.call(() => {
      const el = document.getElementById("s5-sub-text");
      if (el) el.innerHTML = "分级阅读库、<span class='sub-green'>AI实时发音纠错</span>、生词本、家长监控，功能一应俱全！";
    }, null, 4.5);

    tl.fromTo("#s5-f1", { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: 0.5, ease: "back.out(1.5)" }, 4.6);
    tl.fromTo("#s5-f2", { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: 0.5, ease: "back.out(1.5)" }, 6.5);
    tl.fromTo("#s5-f3", { opacity: 0, x: 30 }, { opacity: 1, x: 0, duration: 0.5, ease: "back.out(1.5)" }, 8.5);
    tl.fromTo("#s5-f4", { opacity: 0, x: 30 }, { opacity: 1, x: 0, duration: 0.5, ease: "back.out(1.5)" }, 10.5);

    tl.fromTo("#s5-avatar", 
      { opacity: 0, y: 20 }, 
      { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 
      0.3
    );

    tl.fromTo("#s5-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 6, ease: "sine.inOut" }, 0.9);

    tl.to("#root", { opacity: 0, scale: 0.97, filter: "blur(6px)", duration: 0.5, ease: "power2.inOut" }, 13.1);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene5"] = tl;
  </script>
</template>
'''

# ----------------- SCENE 6 -----------------
scene6 = '''<template>
  <style>
    @font-face {
      font-family: "PingFang SC";
      src: local("PingFang SC");
      font-display: swap;
    }
    #root {
      position: absolute;
      inset: 0;
      overflow: hidden;
      font-family: "PingFang SC", -apple-system, sans-serif;
      color: #f8fafc;
    }

    .poster-stage {
      position: absolute;
      top: 100px;
      left: 120px;
      right: 120px;
      height: 680px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 40px;
    }

    .poster-phone-mockup {
      width: 480px;
      height: 660px;
      background: #090d16;
      border-radius: 28px;
      border: 2px solid rgba(56, 189, 248, 0.4);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(56, 189, 248, 0.2);
      overflow: hidden;
      position: relative;
    }
    .poster-scroll-inner {
      width: 100%;
      position: absolute;
      top: 0;
      left: 0;
    }
    .poster-scroll-inner img {
      width: 100%;
      height: auto;
      display: block;
    }

    .poster-narrative {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }
    .poster-badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      align-self: flex-start;
      padding: 8px 20px;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.5);
      border-radius: 9999px;
      font-size: 14px;
      font-weight: 800;
      color: #fbbf24;
    }
    .poster-title {
      font-size: 46px;
      font-weight: 900;
      line-height: 1.25;
      letter-spacing: -0.02em;
    }
    .poster-desc {
      font-size: 19px;
      color: #94a3b8;
      line-height: 1.6;
    }

    .reply-badge-card {
      display: flex;
      align-items: center;
      gap: 20px;
      padding: 20px 32px;
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.2), rgba(37, 99, 235, 0.2));
      border: 2px solid #38bdf8;
      border-radius: 20px;
      backdrop-filter: blur(20px);
      box-shadow: 0 16px 45px rgba(56, 189, 248, 0.35);
    }
    .reply-code-box {
      background: #38bdf8;
      color: #041226;
      font-size: 38px;
      font-weight: 900;
      padding: 6px 24px;
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(56, 189, 248, 0.6);
    }
    .reply-info h4 {
      font-size: 22px;
      font-weight: 900;
      color: #ffffff;
      margin-bottom: 4px;
    }
    .reply-info p {
      font-size: 14px;
      color: #93c5fd;
      font-weight: 600;
    }

    .grand-outro {
      position: absolute;
      inset: 0;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 24px;
      background: radial-gradient(circle at 50% 50%, rgba(14, 165, 233, 0.2) 0%, transparent 60%);
      z-index: 50;
    }
    .outro-avatar-ring {
      position: relative;
      width: 170px;
      height: 170px;
      border-radius: 50%;
      padding: 6px;
      background: linear-gradient(135deg, #38bdf8, #8b5cf6, #3b82f6);
      box-shadow: 0 0 50px rgba(56, 189, 248, 0.6);
    }
    .outro-brand-name {
      font-size: 64px;
      font-weight: 900;
      letter-spacing: 0.05em;
      background: linear-gradient(135deg, #ffffff 40%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 4px 20px rgba(56, 189, 248, 0.4));
    }
    .outro-slogan {
      font-size: 28px;
      font-weight: 700;
      color: #94a3b8;
      letter-spacing: 0.1em;
    }
    .follow-pill {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      padding: 12px 36px;
      background: #38bdf8;
      color: #051329;
      font-size: 20px;
      font-weight: 900;
      border-radius: 9999px;
      box-shadow: 0 8px 30px rgba(56, 189, 248, 0.5);
    }

    .avatar-hud {
      position: absolute;
      bottom: 80px;
      left: 56px;
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 20px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      z-index: 60;
    }
    .avatar-img-wrap {
      width: 54px;
      height: 54px;
      border-radius: 50%;
      overflow: hidden;
      border: 2px solid #38bdf8;
    }
    .avatar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .avatar-meta {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .avatar-title {
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
    }
    .avatar-status {
      font-size: 12px;
      color: #38bdf8;
      font-weight: 600;
    }

    .subtitles-pill {
      position: absolute;
      bottom: 80px;
      left: 360px;
      right: 360px;
      padding: 12px 28px;
      background: rgba(10, 15, 26, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 9999px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6);
      text-align: center;
      z-index: 60;
    }
    .sub-text {
      font-size: 28px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-hl { color: #38bdf8; }
  </style>

  <div id="root" data-composition-id="scene6" data-width="1920" data-height="1080" data-hold>
    <div class="poster-stage" id="s6-stage1">
      <div class="poster-phone-mockup" id="s6-poster-phone">
        <div class="poster-scroll-inner" id="s6-poster-inner">
          <img src="assets/top10_poster.jpg" alt="TOP 10 Skills Poster" />
        </div>
      </div>

      <div class="poster-narrative" id="s6-narrative">
        <div class="poster-badge" data-layout-ignore>🔥 Vercel AI 官方认证生态</div>
        <h2 class="poster-title">
          学会 Skills = 免费培训<br />
          <span style="color: #38bdf8;">数万个随时上岗的顶级员工</span>
        </h2>
        <p class="poster-desc" data-layout-ignore>
          无需高昂研发预算，10 个高频生产级技能现已整理成完整指南，即装即用。
        </p>
        <div class="reply-badge-card" id="s6-reply-card">
          <div class="reply-code-box">666</div>
          <div class="reply-info" data-layout-ignore>
            <h4>评论区回复「666」免费领取</h4>
            <p>即刻获取 10 大神仙 Skills 离线配置与代码示例</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Grand Outro Screen -->
    <div class="grand-outro" id="s6-grand-outro">
      <div class="outro-avatar-ring" id="s6-outro-ring">
        <div style="width:100%; height:100%; border-radius:50%; background:url(assets/avatar.jpg) center/cover no-repeat;"></div>
      </div>
      <div class="outro-brand-name">胖猫AI</div>
      <div class="outro-slogan">大 AI 时代即将到来 · 一起探索 AI 超级个体之路</div>
      <div class="follow-pill" data-layout-ignore>
        <span>＋ 关注胖猫AI</span>
      </div>
    </div>

    <div class="avatar-hud" id="s6-avatar" data-layout-ignore>
      <div class="avatar-img-wrap">
        <img src="assets/avatar.jpg" alt="胖猫AI" />
      </div>
      <div class="avatar-meta">
        <div class="avatar-title">胖猫AI</div>
        <div class="avatar-status">⚡️ 下期更精彩</div>
      </div>
    </div>

    <div class="subtitles-pill" id="s6-sub">
      <span class="sub-text" id="s6-sub-text">学会了 skills，等于给你的 AI 免费培训了数万个顶级员工！</span>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({ paused: true });

    tl.fromTo("#s6-poster-phone", 
      { opacity: 0, x: -60, scale: 0.95 }, 
      { opacity: 1, x: 0, scale: 1, duration: 1.0, ease: "power3.out" }, 
      0.1
    );

    tl.fromTo("#s6-narrative", 
      { opacity: 0, x: 50 }, 
      { opacity: 1, x: 0, duration: 0.9, ease: "power3.out" }, 
      0.3
    );

    // Auto-scroll poster continuously
    tl.to("#s6-poster-inner", { y: -520, duration: 13.0, ease: "power1.inOut" }, 0.8);

    tl.call(() => {
      const el = document.getElementById("s6-sub-text");
      if (el) el.innerHTML = "十个最好用的高频 Skills 已打包整理好，评论区回复 <span class='sub-hl'>「666」</span> 免费领！";
    }, null, 6.0);

    tl.fromTo("#s6-reply-card", 
      { opacity: 0, scale: 0.85 }, 
      { opacity: 1, scale: 1, duration: 0.7, ease: "elastic.out(1, 0.6)" }, 
      6.2
    );

    // gentle pulse on reply card
    tl.to("#s6-reply-card", { scale: 1.04, duration: 1.2, yoyo: true, repeat: 4, ease: "sine.inOut" }, 7.0);

    // Grand Outro Screen at 14.6s
    tl.call(() => {
      const el = document.getElementById("s6-sub-text");
      if (el) el.innerHTML = "我是 <span class='sub-hl'>胖猫 AI</span>，带你探索 AI 超级个体之路，咱们下期见！";
      
      const s1 = document.getElementById("s6-stage1");
      const outro = document.getElementById("s6-grand-outro");
      const avHud = document.getElementById("s6-avatar");
      if (s1) s1.style.display = "none";
      if (avHud) avHud.style.display = "none";
      if (outro) outro.style.display = "flex";
    }, null, 14.6);

    tl.fromTo("#s6-grand-outro", 
      { opacity: 0, scale: 0.9 }, 
      { opacity: 1, scale: 1, duration: 0.8, ease: "power3.out" }, 
      14.7
    );

    tl.fromTo("#s6-outro-ring", 
      { scale: 0.6, rotate: -20 }, 
      { scale: 1, rotate: 0, duration: 1.0, ease: "back.out(1.8)" }, 
      14.9
    );

    tl.fromTo("#s6-avatar", 
      { opacity: 0, y: 20 }, 
      { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 
      0.3
    );

    tl.fromTo("#s6-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 7, ease: "sine.inOut" }, 0.9);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene6"] = tl;
  </script>
</template>
'''

scenes = [("scene1_hook.html", scene1), ("scene2_70k.html", scene2), ("scene3_install.html", scene3), ("scene4_product.html", scene4), ("scene5_app.html", scene5), ("scene6_outro.html", scene6)]
for fname, content in scenes:
    with open(f"{base_dir}/compositions/{fname}", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote compositions/{fname}")

print("All scenes generated cleanly!")
