import re

scenes_dir = "compositions"

# 1. Update scene1_hook.html
with open(f"{scenes_dir}/scene1_hook.html", "r", encoding="utf-8") as f:
    s1 = f.read()
# Update subtitle hud padding
s1 = re.sub(r'\.subtitle-hud\s*\{[^}]+\}', '''.subtitle-hud {
      position: absolute;
      bottom: 46px;
      left: 200px;
      right: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 60;
      pointer-events: none;
    }''', s1)
s1 = re.sub(r'\.subtitle-text\s*\{[^}]+\}', '''.subtitle-text {
      font-size: 30px;
      font-weight: 800;
      color: #1A1C20;
      letter-spacing: 0.04em;
      text-align: center;
      line-height: 1.35;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.9);
    }''', s1)
# Add root fadeout at end
if 'tl.to("#root"' not in s1:
    s1 = s1.replace('window.__timelines["scene1"] = tl;', 'tl.to("#root", { opacity: 0, duration: 0.25 }, 13.75);\n    window.__timelines["scene1"] = tl;')
with open(f"{scenes_dir}/scene1_hook.html", "w", encoding="utf-8") as f:
    f.write(s1)

# 2. Update scene2_70k.html
with open(f"{scenes_dir}/scene2_70k.html", "r", encoding="utf-8") as f:
    s2 = f.read()
s2 = re.sub(r'\.subtitle-hud\s*\{[^}]+\}', '''.subtitle-hud {
      position: absolute;
      bottom: 46px;
      left: 200px;
      right: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 60;
      pointer-events: none;
    }''', s2)
s2 = re.sub(r'\.subtitle-text\s*\{[^}]+\}', '''.subtitle-text {
      font-size: 30px;
      font-weight: 800;
      color: #1A1C20;
      letter-spacing: 0.04em;
      text-align: center;
      line-height: 1.35;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.9);
    }''', s2)
# Fix elo bars animation
s2 = s2.replace(
    'tl.fromTo(".elo-bar-fill", \n      { width: "0%" }, \n      { width: (i, target) => target.style.width, duration: 1.2, ease: "power2.out", stagger: 0.15 }, \n      0.8\n    );',
    '''tl.fromTo(".fill-green", { width: "0%" }, { width: "96%", duration: 1.2, ease: "power2.out" }, 0.6);
    tl.fromTo(".fill-teal", { width: "0%" }, { width: "93%", duration: 1.2, ease: "power2.out" }, 0.8);
    tl.fromTo(".fill-orange", { width: "0%" }, { width: "86%", duration: 1.2, ease: "power2.out" }, 1.0);
    tl.fromTo(".fill-dark", { width: "0%" }, { width: "81%", duration: 1.2, ease: "power2.out" }, 1.2);'''
)
if 'tl.to("#root"' not in s2:
    s2 = s2.replace('window.__timelines["scene2"] = tl;', 'tl.to("#root", { opacity: 0, duration: 0.25 }, 10.25);\n    window.__timelines["scene2"] = tl;')
with open(f"{scenes_dir}/scene2_70k.html", "w", encoding="utf-8") as f:
    f.write(s2)

# 3. Update scene3_install.html
with open(f"{scenes_dir}/scene3_install.html", "r", encoding="utf-8") as f:
    s3 = f.read()
s3 = re.sub(r'\.subtitle-hud\s*\{[^}]+\}', '''.subtitle-hud {
      position: absolute;
      bottom: 46px;
      left: 200px;
      right: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 60;
      pointer-events: none;
    }''', s3)
s3 = re.sub(r'\.subtitle-text\s*\{[^}]+\}', '''.subtitle-text {
      font-size: 30px;
      font-weight: 800;
      color: #1A1C20;
      letter-spacing: 0.04em;
      text-align: center;
      line-height: 1.35;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.9);
    }''', s3)
# Fix cursor card display: none initially
s3 = s3.replace('display: flex;\n      flex-direction: column;\n      overflow: hidden;\n      z-index: 30;\n      opacity: 0;', 'display: none;\n      flex-direction: column;\n      overflow: hidden;\n      z-index: 30;\n      opacity: 0;')
s3 = s3.replace(
    'tl.to("#s3-cursor-card", { opacity: 1, y: 0, duration: 0.8, ease: "back.out(1.2)" }, 3.5);',
    '''tl.call(() => {
      const c = document.getElementById("s3-cursor-card");
      if (c) c.style.display = "flex";
    }, null, 3.4);
    tl.fromTo("#s3-cursor-card", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.8, ease: "back.out(1.2)" }, 3.5);'''
)
if 'tl.to("#root"' not in s3:
    s3 = s3.replace('window.__timelines["scene3"] = tl;', 'tl.to("#root", { opacity: 0, duration: 0.25 }, 12.25);\n    window.__timelines["scene3"] = tl;')
with open(f"{scenes_dir}/scene3_install.html", "w", encoding="utf-8") as f:
    f.write(s3)

# 4. Update scene4_product.html
with open(f"{scenes_dir}/scene4_product.html", "r", encoding="utf-8") as f:
    s4 = f.read()
s4 = re.sub(r'\.subtitle-hud\s*\{[^}]+\}', '''.subtitle-hud {
      position: absolute;
      bottom: 46px;
      left: 200px;
      right: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 60;
      pointer-events: none;
    }''', s4)
s4 = re.sub(r'\.subtitle-text\s*\{[^}]+\}', '''.subtitle-text {
      font-size: 30px;
      font-weight: 800;
      color: #1A1C20;
      letter-spacing: 0.04em;
      text-align: center;
      line-height: 1.35;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.9);
    }''', s4)
if 'tl.to("#root"' not in s4:
    s4 = s4.replace('window.__timelines["scene4"] = tl;', 'tl.to("#root", { opacity: 0, duration: 0.25 }, 20.55);\n    window.__timelines["scene4"] = tl;')
with open(f"{scenes_dir}/scene4_product.html", "w", encoding="utf-8") as f:
    f.write(s4)

# 5. Update scene5_app.html
with open(f"{scenes_dir}/scene5_app.html", "r", encoding="utf-8") as f:
    s5 = f.read()
s5 = re.sub(r'\.subtitle-hud\s*\{[^}]+\}', '''.subtitle-hud {
      position: absolute;
      bottom: 46px;
      left: 200px;
      right: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 60;
      pointer-events: none;
    }''', s5)
s5 = re.sub(r'\.subtitle-text\s*\{[^}]+\}', '''.subtitle-text {
      font-size: 30px;
      font-weight: 800;
      color: #1A1C20;
      letter-spacing: 0.04em;
      text-align: center;
      line-height: 1.35;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.9);
    }''', s5)
if 'tl.to("#root"' not in s5:
    s5 = s5.replace('window.__timelines["scene5"] = tl;', 'tl.to("#root", { opacity: 0, duration: 0.25 }, 13.35);\n    window.__timelines["scene5"] = tl;')
with open(f"{scenes_dir}/scene5_app.html", "w", encoding="utf-8") as f:
    f.write(s5)

# 6. Update scene6_outro.html
with open(f"{scenes_dir}/scene6_outro.html", "r", encoding="utf-8") as f:
    s6 = f.read()
s6 = re.sub(r'\.subtitle-hud\s*\{[^}]+\}', '''.subtitle-hud {
      position: absolute;
      bottom: 46px;
      left: 200px;
      right: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 60;
      pointer-events: none;
    }''', s6)
s6 = re.sub(r'\.subtitle-text\s*\{[^}]+\}', '''.subtitle-text {
      font-size: 30px;
      font-weight: 800;
      color: #1A1C20;
      letter-spacing: 0.04em;
      text-align: center;
      line-height: 1.35;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.9);
    }''', s6)
with open(f"{scenes_dir}/scene6_outro.html", "w", encoding="utf-8") as f:
    f.write(s6)

print("All scenes polished and protected!")
