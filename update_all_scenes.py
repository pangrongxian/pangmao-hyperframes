import os

base = "/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes/compositions"

# ----------------- Scene 1 -----------------
scene1 = """<template>
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

    /* 3D Browser Mockup */
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

    /* Right Side Typography & Highlights */
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

    /* 4 Core Skill Feature Badges */
    .features-grid {
      position: absolute;
      bottom: 210px;
      left: 140px;
      right: 140px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 22px;
    }
    .feature-card {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 16px;
      padding: 22px 24px;
      display: flex;
      align-items: center;
      gap: 18px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    .feat-icon-box {
      width: 52px;
      height: 52px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      flex-shrink: 0;
    }
    .icon-sql { background: linear-gradient(135deg, rgba(14, 165, 233, 0.2), rgba(2, 132, 199, 0.4)); border: 1px solid rgba(56, 189, 248, 0.4); }
    .icon-ppt { background: linear-gradient(135deg, rgba(245, 158, 11, 0.2), rgba(217, 119, 6, 0.4)); border: 1px solid rgba(245, 158, 11, 0.4); }
    .icon-doc { background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(147, 51, 234, 0.4)); border: 1px solid rgba(168, 85, 247, 0.4); }
    .icon-art { background: linear-gradient(135deg, rgba(236, 72, 153, 0.2), rgba(219, 39, 119, 0.4)); border: 1px solid rgba(236, 72, 153, 0.4); }
    
    .feat-info h4 {
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 4px;
    }
    .feat-info p {
      font-size: 13px;
      color: #94a3b8;
      font-weight: 500;
    }

    /* Floating PangMao Cat Avatar HUD */
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
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .avatar-tag {
      font-size: 11px;
      color: #38bdf8;
      font-weight: 600;
      padding: 1px 6px;
      background: rgba(56, 189, 248, 0.15);
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
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
    }

    /* Subtitle Bar */
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
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-hl {
      color: #38bdf8;
    }
  </style>

  <div id="root" data-composition-id="scene1" data-width="1920" data-height="1080">
    <!-- 3D Browser Showcase with User's Latest Screenshot -->
    <div class="browser-card" id="s1-browser">
      <div class="browser-header">
        <div class="mac-dots">
          <div class="mac-dot dot-r"></div>
          <div class="mac-dot dot-y"></div>
          <div class="mac-dot dot-g"></div>
        </div>
        <div class="url-bar">
          https://<span class="url-hl">skills.sh</span>/
        </div>
      </div>
      <div class="browser-content">
        <img src="assets/skills_sh_latest.png" alt="skills.sh 最新界面" />
      </div>
    </div>

    <!-- Right Side Typography -->
    <div class="hook-right" id="s1-hook-right">
      <div class="tag-hook" data-layout-ignore>⚡️ 颠覆式 AI 技能生态</div>
      <h1 class="hook-title">
        一不小心加了个 <span class="text-glow">.sh</span><br />
        推开新世界大门
      </h1>
      <p class="hook-desc">
        这不是普通网站，这是全球最大的 AI Agent Skills 技能库，赋予 AI 真实的工程执行力。
      </p>
    </div>

    <!-- 4 Core Skill Feature Badges -->
    <div class="features-grid" id="s1-features">
      <div class="feature-card feat-1">
        <div class="feat-icon-box icon-sql">🗄️</div>
        <div class="feat-info">
          <h4>直连数据库 SQL</h4>
          <p>秒级读写万级生产数据</p>
        </div>
      </div>
      <div class="feature-card feat-2">
        <div class="feat-icon-box icon-ppt">📊</div>
        <div class="feat-info">
          <h4>一键生成 PPT</h4>
          <p>结构化思维导图出稿</p>
        </div>
      </div>
      <div class="feature-card feat-3">
        <div class="feat-icon-box icon-doc">📝</div>
        <div class="feat-info">
          <h4>长文深度写作</h4>
          <p>多源研报聚合分析</p>
        </div>
      </div>
      <div class="feature-card feat-4">
        <div class="feat-icon-box icon-art">🎨</div>
        <div class="feat-info">
          <h4>全景爆款海报</h4>
          <p>自适应排版色彩烘托</p>
        </div>
      </div>
    </div>

    <!-- Floating Avatar HUD -->
    <div class="avatar-hud" id="s1-avatar" data-layout-ignore>
      <div class="avatar-img-wrap">
        <img src="assets/avatar.jpg" alt="胖猫AI" />
      </div>
      <div class="avatar-meta">
        <div class="avatar-title">胖猫AI <span class="avatar-tag">主理人</span></div>
        <div class="avatar-status"><span class="status-pulse"></span>正在实测讲解</div>
      </div>
    </div>

    <!-- Subtitle Bar -->
    <div class="subtitles-pill" id="s1-sub">
      <span class="sub-text" id="s1-sub-text">当你一不小心在 skills 后面加了个 <span class="sub-hl">sh</span>...</span>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({ paused: true });

    // Entry 0s (0 - 9.3s Part 1)
    tl.fromTo("#s1-browser", 
      { opacity: 0, x: -60, rotateY: 10, scale: 0.94 }, 
      { opacity: 1, x: 0, rotateY: 0, scale: 1, duration: 1.2, ease: "power3.out" }, 
      0.1
    );

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

    // Subtitle update at 4.2s
    tl.call(() => {
      const el = document.getElementById("s1-sub-text");
      if (el) el.innerHTML = "你就进入了这个全球最大的 <span class='sub-hl'>AI Agent Skills</span> 技能库！";
    }, null, 4.2);

    // 9.3s - 13.9s Part 2: 4 Feature Cards Stagger in
    tl.to("#s1-browser", { y: -70, scale: 0.88, duration: 0.9, ease: "power2.inOut" }, 9.2);
    tl.to("#s1-hook-right", { opacity: 0.2, y: -40, duration: 0.7, ease: "power2.out" }, 9.2);

    tl.call(() => {
      const el = document.getElementById("s1-sub-text");
      if (el) el.innerHTML = "有帮你<span class='sub-hl'>连数据库的</span>、<span class='sub-hl'>做 PPT 的</span>、写长文的、做海报的。";
    }, null, 9.31);

    tl.fromTo("#s1-features .feature-card", 
      { opacity: 0, y: 60, scale: 0.85, filter: "blur(8px)" }, 
      { opacity: 1, y: 0, scale: 1, filter: "blur(0px)", duration: 0.75, stagger: 0.18, ease: "expo.out" }, 
      9.5
    );

    tl.fromTo("#s1-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 7, ease: "sine.inOut" }, 1.3);

    // Outro transition at 13.4s
    tl.to("#root", { opacity: 0, scale: 0.97, filter: "blur(6px)", duration: 0.5, ease: "power2.inOut" }, 13.4);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene1"] = tl;
  </script>
</template>
"""

# ----------------- Scene 2 (151万+ Skills) -----------------
scene2 = """<template>
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

    /* Big Golden "全免费！无限扩展" Sticker */
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

    /* Vibe Coding Cards */
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
      font-size: 19px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 4px;
    }
    .vibe-info p {
      font-size: 13px;
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
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-hl {
      color: #38bdf8;
    }
    .sub-gold {
      color: #fbbf24;
    }
  </style>

  <div id="root" data-composition-id="scene2" data-width="1920" data-height="1080">
    <div class="hero-center" id="s2-hero">
      <div class="badge-capsule" data-layout-ignore>
        <span>🌐 2026 全新实时收录数据</span>
      </div>
      <div class="stat-number" id="s2-counter">1,517,216+</div>
      <div class="stat-label">全球海量即时装配的智能体技能</div>
    </div>

    <!-- Golden Highlight Sticker -->
    <div class="golden-banner" id="s2-golden">
      <span class="golden-text">全免费！无限扩展</span>
      <span class="golden-sub" data-layout-ignore>无需注册绑定 · 一键装载</span>
    </div>

    <!-- Vibe Coding Concept Cards -->
    <div class="vibe-showcase" id="s2-vibe">
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

    tl.fromTo("#s2-golden", 
      { opacity: 0, scale: 0.7, rotate: -4 }, 
      { opacity: 1, scale: 1, rotate: 0, duration: 0.7, ease: "elastic.out(1, 0.6)" }, 
      1.8
    );

    tl.call(() => {
      const el = document.getElementById("s2-sub-text");
      if (el) el.innerHTML = "哪怕你是<span class='sub-hl'>零基础文科生</span>，也能通过 <span class='sub-gold'>Vibe Coding</span> 轻松手搓出全功能网站！";
    }, null, 3.2);

    tl.fromTo("#s2-vibe .vibe-card", 
      { opacity: 0, y: 40, scale: 0.9 }, 
      { opacity: 1, y: 0, scale: 1, duration: 0.6, stagger: 0.15, ease: "power3.out" }, 
      3.8
    );

    tl.fromTo("#s2-avatar", 
      { opacity: 0, scale: 0.8 }, 
      { opacity: 1, scale: 1, duration: 0.6, ease: "power2.out" }, 
      0.3
    );

    tl.fromTo("#s2-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 5, ease: "sine.inOut" }, 1.1);

    tl.to("#root", { opacity: 0, scale: 1.05, filter: "blur(6px)", duration: 0.5, ease: "power2.inOut" }, 10.1);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene2"] = tl;
  </script>
</template>
"""

# ----------------- Scene 3 (Install in Cursor) -----------------
scene3 = """<template>
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

    .install-container {
      position: absolute;
      top: 130px;
      left: 100px;
      right: 100px;
      height: 640px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 36px;
    }

    .step-card {
      flex: 1;
      height: 580px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 20px;
      backdrop-filter: blur(20px);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), 0 0 30px rgba(56, 189, 248, 0.15);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .card-top {
      height: 48px;
      background: #111827;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
    }
    .card-tag {
      font-size: 14px;
      font-weight: 800;
      color: #38bdf8;
    }
    .card-body {
      padding: 32px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      flex: 1;
    }
    .skill-badge {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      align-self: flex-start;
      padding: 8px 18px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.4);
      border-radius: 10px;
      font-size: 15px;
      font-weight: 800;
      color: #38bdf8;
    }
    .skill-name {
      font-size: 38px;
      font-weight: 900;
      color: #ffffff;
      line-height: 1.2;
    }
    .skill-desc {
      font-size: 16px;
      color: #94a3b8;
      line-height: 1.6;
    }
    .code-snippet {
      background: #090d16;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 18px 22px;
      font-family: monospace;
      font-size: 15px;
      color: #a5f3fc;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .copy-btn {
      padding: 10px 24px;
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      border: none;
      border-radius: 8px;
      font-size: 15px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
    }
    .copied-badge {
      display: none;
      padding: 4px 12px;
      background: #10b981;
      color: #ffffff;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 800;
    }

    .flow-arrow {
      width: 70px;
      height: 70px;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.8);
      border: 2px solid rgba(56, 189, 248, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      color: #38bdf8;
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.3);
      flex-shrink: 0;
    }

    .cursor-card {
      border-color: rgba(168, 85, 247, 0.4);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), 0 0 30px rgba(168, 85, 247, 0.15);
    }
    .cursor-input-box {
      margin-top: 10px;
      background: #090d16;
      border: 1px solid rgba(168, 85, 247, 0.4);
      border-radius: 12px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .cursor-prompt {
      font-family: monospace;
      font-size: 15px;
      color: #e2e8f0;
    }
    .status-installed {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 18px;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.5);
      border-radius: 8px;
      font-size: 15px;
      font-weight: 800;
      color: #34d399;
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
      color: #10b981;
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
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-hl {
      color: #38bdf8;
    }
    .sub-green {
      color: #34d399;
    }
  </style>

  <div id="root" data-composition-id="scene3" data-width="1920" data-height="1080">
    <div class="install-container">
      <div class="step-card" id="s3-card-left">
        <div class="card-top">
          <div class="card-tag">STEP 01 · SKILLS.SH 复制技能</div>
          <div style="color: #38bdf8; font-size: 12px; font-weight: bold;">● ONLINE</div>
        </div>
        <div class="card-body">
          <div class="skill-badge">💡 顶尖策划必备</div>
          <div class="skill-name">头脑风暴 Skill</div>
          <div class="skill-desc">
            内置硅谷资深架构师与产品经理思考链，一键补全产品设计盲区与功能边界。
          </div>
          <div class="code-snippet">
            <span>$ npx skills add brainstorm-skill</span>
            <button class="copy-btn" id="s3-copy-btn">
              <span>📋 复制命令</span>
            </button>
            <span class="copied-badge" id="s3-copied-badge">✓ 已复制到剪贴板</span>
          </div>
        </div>
      </div>

      <div class="flow-arrow" id="s3-arrow">➔</div>

      <div class="step-card cursor-card" id="s3-card-right">
        <div class="card-top">
          <div class="card-tag" style="color: #c084fc;">STEP 02 · CURSOR 对话框</div>
          <div style="color: #a855f7; font-size: 12px; font-weight: bold;">● AI READY</div>
        </div>
        <div class="card-body">
          <div class="skill-badge" style="background: rgba(168, 85, 247, 0.15); border-color: rgba(168, 85, 247, 0.4); color: #c084fc;">
            ⚡️ 即装即用
          </div>
          <div class="skill-name" style="font-size: 32px;">直接丢进对话框</div>
          <div class="cursor-input-box">
            <div style="font-size: 12px; color: #94a3b8;" data-layout-ignore>Cursor Chat / Composer:</div>
            <div class="cursor-prompt" id="s3-prompt-text">$ npx skills add brainstorm-skill</div>
          </div>
          <div class="status-installed" id="s3-installed-pill" style="opacity: 0;">
            <span>✓</span> 技能已成功装载到当前项目 (1.2s)
          </div>
        </div>
      </div>
    </div>

    <div class="avatar-hud" id="s3-avatar" data-layout-ignore>
      <div class="avatar-img-wrap">
        <img src="assets/avatar.jpg" alt="胖猫AI" />
      </div>
      <div class="avatar-meta">
        <div class="avatar-title">胖猫AI</div>
        <div class="avatar-status">⚡️ 极度丝滑体验</div>
      </div>
    </div>

    <div class="subtitles-pill" id="s3-sub">
      <span class="sub-text" id="s3-sub-text">操作极度丝滑：在 skills.sh 上选中「头脑风暴」skill，点击复制...</span>
    </div>
  </div>

  <script>
    const tl = gsap.timeline({ paused: true });

    tl.fromTo("#s3-card-left", 
      { opacity: 0, x: -60, scale: 0.95 }, 
      { opacity: 1, x: 0, scale: 1, duration: 0.9, ease: "power3.out" }, 
      0.1
    );

    tl.fromTo("#s3-arrow", 
      { opacity: 0, scale: 0 }, 
      { opacity: 1, scale: 1, duration: 0.6, ease: "back.out(2)" }, 
      0.6
    );

    tl.fromTo("#s3-card-right", 
      { opacity: 0, x: 60, scale: 0.95 }, 
      { opacity: 1, x: 0, scale: 1, duration: 0.9, ease: "power3.out" }, 
      0.4
    );

    tl.to("#s3-copy-btn", { scale: 0.9, duration: 0.15, yoyo: true, repeat: 1 }, 2.8);
    tl.call(() => {
      const btn = document.getElementById("s3-copy-btn");
      const badge = document.getElementById("s3-copied-badge");
      if (btn) btn.style.display = "none";
      if (badge) badge.style.display = "inline-block";
    }, null, 3.0);

    tl.call(() => {
      const el = document.getElementById("s3-sub-text");
      if (el) el.innerHTML = "随即打开 Cursor，把代码直接丢进对话框，<span class='sub-green'>下一秒技能就装好了！</span>";
    }, null, 5.2);

    tl.fromTo("#s3-installed-pill", 
      { opacity: 0, y: 20, scale: 0.8 }, 
      { opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.6)" }, 
      5.8
    );

    tl.fromTo("#s3-avatar", 
      { opacity: 0, y: 20 }, 
      { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 
      0.3
    );

    tl.fromTo("#s3-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 6, ease: "sine.inOut" }, 1.0);

    tl.to("#root", { opacity: 0, scale: 0.96, filter: "blur(6px)", duration: 0.5, ease: "power2.inOut" }, 11.3);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene3"] = tl;
  </script>
</template>
"""

# ----------------- Scene 4 (Using Native Cursor IDE Retina Screenshot!) -----------------
scene4 = """<template>
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

    /* Floating Intent Card */
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

    /* Floating PM Badge */
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
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-hl {
      color: #38bdf8;
    }
    .sub-purple {
      color: #c084fc;
    }
  </style>

  <div id="root" data-composition-id="scene4" data-width="1920" data-height="1080">
    <!-- Native 2x Retina Cursor IDE Showcase -->
    <div class="cursor-ide-container" id="s4-ide">
      <img src="assets/cursor_kidslingo_retina.png" class="cursor-ide-img" alt="Cursor IDE KidsLingo" />
    </div>

    <!-- Floating Intent Dialogue -->
    <div class="intent-floating-card" id="s4-intent">
      <div class="intent-tag">PROMPT 指令输入：</div>
      <div class="intent-text">
        “我想做一个适合家长带孩子<span>学英语的网站</span>，先帮我<span>头脑风暴</span>，再写代码。”
      </div>
    </div>

    <!-- Floating PM Transformation Badge -->
    <div class="pm-floating-card" id="s4-pm">
      <div class="pm-tag">⚡️ AGENT SKILLS 思考链激活</div>
      <div class="pm-title">👔 Cursor 变身顶尖产品经理</div>
      <div class="pm-desc">
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

    tl.fromTo("#s4-intent", 
      { opacity: 0, x: -40, scale: 0.9 }, 
      { opacity: 1, x: 0, scale: 1, duration: 0.8, ease: "back.out(1.5)" }, 
      0.4
    );

    // 7.8s: PM Transform & Subtitle update
    tl.call(() => {
      const el = document.getElementById("s4-sub-text");
      if (el) el.innerHTML = "Cursor 瞬间变身<span class='sub-purple'>顶尖产品经理</span>，不仅梳理需求，还自动输出完整 PRD！";
    }, null, 7.8);

    tl.fromTo("#s4-pm", 
      { opacity: 0, y: 30, scale: 0.85 }, 
      { opacity: 1, y: 0, scale: 1, duration: 0.8, ease: "back.out(1.6)" }, 
      8.0
    );

    // 14.5s: Auto Coding
    tl.call(() => {
      const el = document.getElementById("s4-sub-text");
      if (el) el.innerHTML = "确认后，Cursor <span class='sub-hl'>直接开始自动写全栈代码</span>。";
    }, null, 14.5);

    tl.to("#s4-intent", { opacity: 0.15, duration: 0.6 }, 14.8);
    tl.to("#s4-pm", { opacity: 0.15, duration: 0.6 }, 14.8);
    tl.to("#s4-ide", { scale: 1.05, duration: 3.5, ease: "power1.inOut" }, 15.0);

    tl.fromTo("#s4-avatar", 
      { opacity: 0, y: 20 }, 
      { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 
      0.3
    );

    tl.fromTo("#s4-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 10, ease: "sine.inOut" }, 1.0);

    tl.to("#root", { opacity: 0, scale: 0.97, filter: "blur(6px)", duration: 0.5, ease: "power2.inOut" }, 18.2);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene4"] = tl;
  </script>
</template>
"""

# ----------------- Scene 5 (Exclusive KidsLingo AI Web App Retina!) -----------------
scene5 = """<template>
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

    /* Floating Time Stamp Pill */
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
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-green {
      color: #34d399;
    }
    .sub-hl {
      color: #38bdf8;
    }
  </style>

  <div id="root" data-composition-id="scene5" data-width="1920" data-height="1080">
    <!-- Exclusive 2x Retina Web App Mockup -->
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

    tl.fromTo("#s5-time-badge", 
      { opacity: 0, scale: 0.7 }, 
      { opacity: 1, scale: 1, duration: 0.8, ease: "back.out(1.8)" }, 
      0.5
    );

    // Subtitle update at 4.2s (show 4 features)
    tl.call(() => {
      const el = document.getElementById("s5-sub-text");
      if (el) el.innerHTML = "分级阅读库、<span class='sub-green'>AI实时发音纠错</span>、生词本、家长监控，功能一应俱全！";
    }, null, 4.2);

    tl.fromTo("#s5-avatar", 
      { opacity: 0, y: 20 }, 
      { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 
      0.3
    );

    tl.fromTo("#s5-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 6, ease: "sine.inOut" }, 0.9);

    tl.to("#root", { opacity: 0, scale: 0.97, filter: "blur(6px)", duration: 0.5, ease: "power2.inOut" }, 10.3);

    window.__timelines = window.__timelines || {};
    window.__timelines["scene5"] = tl;
  </script>
</template>
"""

# ----------------- Scene 6 -----------------
scene6 = """<template>
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

    .skills-deck-wrap {
      position: absolute;
      top: 140px;
      left: 0;
      right: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 32px;
    }
    .deck-header {
      font-size: 52px;
      font-weight: 900;
      letter-spacing: -0.02em;
      text-align: center;
    }
    .deck-header span.glow-blue {
      color: #38bdf8;
      text-shadow: 0 0 25px rgba(56, 189, 248, 0.6);
    }
    .deck-header span.glow-orange {
      color: #fb923c;
      text-shadow: 0 0 25px rgba(251, 146, 60, 0.6);
    }
    .deck-sub {
      font-size: 18px;
      font-weight: 700;
      color: #94a3b8;
      letter-spacing: 0.1em;
    }

    .cards-row {
      display: flex;
      align-items: center;
      gap: 20px;
      margin-top: 10px;
    }
    .skill-card-item {
      width: 280px;
      height: 160px;
      border-radius: 16px;
      background: rgba(15, 23, 42, 0.9);
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      backdrop-filter: blur(20px);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
    }
    .card-border-blue {
      border: 2px solid #38bdf8;
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.35);
    }
    .card-border-purple {
      border: 2px solid #a855f7;
      box-shadow: 0 0 25px rgba(168, 85, 247, 0.35);
    }
    .card-border-orange {
      border: 2px solid #f97316;
      box-shadow: 0 0 25px rgba(249, 115, 22, 0.35);
    }
    .card-border-dark {
      border: 1px solid rgba(255, 255, 255, 0.15);
      background: rgba(10, 15, 26, 0.7);
    }
    .card-item-tag {
      font-size: 13px;
      font-weight: 700;
      color: #94a3b8;
    }
    .card-item-title {
      font-size: 20px;
      font-weight: 900;
      color: #ffffff;
      font-family: monospace;
    }
    .card-item-desc {
      font-size: 14px;
      color: #cbd5e1;
      font-weight: 600;
    }

    .reply-badge {
      display: inline-flex;
      align-items: center;
      gap: 16px;
      padding: 14px 36px;
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.25), rgba(37, 99, 235, 0.2));
      border: 2px solid #38bdf8;
      border-radius: 9999px;
      font-size: 22px;
      font-weight: 900;
      color: #ffffff;
      box-shadow: 0 10px 35px rgba(56, 189, 248, 0.4);
    }
    .reply-code {
      background: #38bdf8;
      color: #041226;
      padding: 4px 16px;
      border-radius: 9999px;
      font-weight: 900;
      font-size: 20px;
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
      font-size: 24px;
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
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.04em;
    }
    .sub-hl {
      color: #38bdf8;
    }
  </style>

  <div id="root" data-composition-id="scene6" data-width="1920" data-height="1080">
    <div class="skills-deck-wrap" id="s6-deck">
      <div class="deck-header">
        挂上最顶流的 <span class="glow-blue">神仙</span> <span class="glow-orange">Skill</span>
      </div>
      <div class="deck-sub" data-layout-ignore>精选高赞智能体扩展包 · 涵盖 150+ 真实生产场景</div>

      <div class="cards-row" id="s6-cards-row">
        <div class="skill-card-item card-border-blue">
          <div class="card-item-tag">Skill 01</div>
          <div class="card-item-title">video-shotcraft</div>
          <div class="card-item-desc">150 个镜头智能构图</div>
        </div>

        <div class="skill-card-item card-border-purple">
          <div class="card-item-tag">Skill 02</div>
          <div class="card-item-title">video-talkcraft</div>
          <div class="card-item-desc">口播动效卡片流</div>
        </div>

        <div class="skill-card-item card-border-orange">
          <div class="card-item-tag">Skill 03</div>
          <div class="card-item-title">mv-director</div>
          <div class="card-item-desc">音乐 MV 导演智能体</div>
        </div>

        <div class="skill-card-item card-border-dark">
          <div class="card-item-tag">Skill Pack</div>
          <div class="card-item-title">mg-styles-15</div>
          <div class="card-item-desc">+ 更多顶级神仙技能</div>
        </div>
      </div>

      <div class="reply-badge" id="s6-reply-badge">
        <span>在评论区回复</span>
        <span class="reply-code">666</span>
        <span>免费送你精选十大多模态 Skills 清单</span>
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

    tl.fromTo("#s6-deck .deck-header", 
      { opacity: 0, y: 30, filter: "blur(10px)" }, 
      { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.8, ease: "power3.out" }, 
      0.1
    );

    tl.fromTo("#s6-cards-row .skill-card-item", 
      { opacity: 0, y: 50, scale: 0.9 }, 
      { opacity: 1, y: 0, scale: 1, duration: 0.7, stagger: 0.15, ease: "back.out(1.4)" }, 
      0.4
    );

    // 6.5s: Subtitle Line 2 & Reply 666 Badge
    tl.call(() => {
      const el = document.getElementById("s6-sub-text");
      if (el) el.innerHTML = "十个最好用的神仙 Skills 已经整理好了，评论区回复 <span class='sub-hl'>「666」</span> 免费领！";
    }, null, 6.5);

    tl.fromTo("#s6-reply-badge", 
      { opacity: 0, scale: 0.8 }, 
      { opacity: 1, scale: 1, duration: 0.7, ease: "elastic.out(1, 0.6)" }, 
      6.8
    );

    // 13.5s: Outro Brand Screen
    tl.call(() => {
      const el = document.getElementById("s6-sub-text");
      if (el) el.innerHTML = "我是 <span class='sub-hl'>胖猫 AI</span>，带你探索 AI 超级个体之路，咱们下期见！";
      const deck = document.getElementById("s6-deck");
      const outro = document.getElementById("s6-grand-outro");
      const avHud = document.getElementById("s6-avatar");
      if (deck) deck.style.display = "none";
      if (avHud) avHud.style.display = "none";
      if (outro) outro.style.display = "flex";
    }, null, 13.5);

    tl.fromTo("#s6-grand-outro", 
      { opacity: 0, scale: 0.9 }, 
      { opacity: 1, scale: 1, duration: 0.8, ease: "power3.out" }, 
      13.6
    );

    tl.fromTo("#s6-outro-ring", 
      { scale: 0.6, rotate: -20 }, 
      { scale: 1, rotate: 0, duration: 1.0, ease: "back.out(1.8)" }, 
      13.8
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
"""

with open(os.path.join(base, "scene1_hook.html"), "w", encoding="utf-8") as f:
    f.write(scene1)
with open(os.path.join(base, "scene2_70k.html"), "w", encoding="utf-8") as f:
    f.write(scene2)
with open(os.path.join(base, "scene3_install.html"), "w", encoding="utf-8") as f:
    f.write(scene3)
with open(os.path.join(base, "scene4_product.html"), "w", encoding="utf-8") as f:
    f.write(scene4)
with open(os.path.join(base, "scene5_app.html"), "w", encoding="utf-8") as f:
    f.write(scene5)
with open(os.path.join(base, "scene6_outro.html"), "w", encoding="utf-8") as f:
    f.write(scene6)

print("Successfully written all 6 updated scene compositions!")

