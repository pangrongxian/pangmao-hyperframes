import os

base_dir = "/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes"

# ----------------- COMMON STYLES & SVGS -----------------
common_css = """
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
.scene-root {
  position: absolute;
  inset: 0;
  width: 1920px;
  height: 1080px;
  overflow: hidden;
  font-family: "PingFang SC", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #1A1C20;
  -webkit-font-smoothing: antialiased;
}

/* Header Navigation (Exact Homage to Template Video) */
.header-nav {
  position: absolute;
  top: 48px;
  left: 64px;
  display: flex;
  align-items: baseline;
  gap: 12px;
  z-index: 50;
}
.nav-num {
  font-size: 26px;
  font-weight: 800;
  color: #C58B35;
  letter-spacing: 0.02em;
}
.nav-title {
  font-size: 24px;
  font-weight: 800;
  color: #1E2024;
  letter-spacing: 0.04em;
}

/* Top Right Brand Mark (Homage to 亚里) */
.header-brand {
  position: absolute;
  top: 42px;
  right: 68px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 50;
}
.brand-arch {
  width: 32px;
  height: 6px;
  border-top: 3.5px solid #C58B35;
  border-radius: 50%;
  margin-bottom: 2px;
}
.brand-title {
  font-size: 26px;
  font-weight: 900;
  color: #1E2024;
  letter-spacing: 0.16em;
}

/* Bottom Presenter Avatar (Circular Double Ring) */
.avatar-hud {
  position: absolute;
  bottom: 40px;
  left: 60px;
  width: 114px;
  height: 114px;
  border-radius: 50%;
  background: #FAF7F0;
  border: 4px solid #FFFFFF;
  box-shadow: 0 10px 26px rgba(50, 38, 25, 0.12), 0 0 0 3px #E5DBC7;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 60;
}
.avatar-hud img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Subtitle (Bottom Center Bold Sans-Serif) */
.subtitle-hud {
  position: absolute;
  bottom: 52px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 60;
  pointer-events: none;
}
.subtitle-text {
  font-size: 34px;
  font-weight: 800;
  color: #1A1C20;
  letter-spacing: 0.04em;
  text-align: center;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
}
.sub-hl {
  color: #C58B35;
  font-weight: 900;
}

/* Claymorphic 3D White Card */
.clay-card {
  background: #FFFFFF;
  border-radius: 24px;
  border: 1px solid rgba(224, 218, 206, 0.7);
  box-shadow: 0 16px 36px -6px rgba(45, 35, 20, 0.08), 0 4px 14px rgba(45, 35, 20, 0.04), inset 0 1px 0 #FFFFFF;
}

/* Animated Hand Pointer Cursor */
.hand-pointer {
  position: absolute;
  width: 48px;
  height: 48px;
  pointer-events: none;
  z-index: 100;
  filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.2));
  transform-origin: 10px 5px;
}
"""

print("Common CSS parsed successfully")
