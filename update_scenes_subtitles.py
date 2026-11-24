import re

css_capsule_style = """
    /* Presenter HUD & Elevated Large Subtitle Capsule */
    .avatar-hud {
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
    }
    .avatar-hud img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .subtitle-hud {
      position: absolute;
      bottom: 64px;
      left: 200px;
      right: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 60;
      pointer-events: none;
    }
    .subtitle-capsule {
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
    }
    .subtitle-text {
      font-size: 36px;
      font-weight: 850;
      color: #1A1C20;
      letter-spacing: 0.03em;
      text-align: center;
      line-height: 1.35;
    }
    .sub-hl {
      color: #C58B35;
      font-weight: 900;
      background: rgba(254, 243, 199, 0.55);
      padding: 1px 8px;
      border-radius: 6px;
    }
"""

def update_file(filepath, sub_id):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace old avatar-hud / subtitle-hud CSS
    # Find from "/* Presenter HUD" or ".avatar-hud {" to end of style
    pattern_css = re.compile(r'(\.avatar-hud\s*\{[\s\S]*?)(</style>)')
    if pattern_css.search(content):
        content = pattern_css.sub(css_capsule_style + "\n  \\2", content)
    else:
        print(f"Warning: CSS pattern not matched in {filepath}")

    # Replace subtitle-hud HTML to include subtitle-capsule
    old_sub_html = re.compile(r'<div class="subtitle-hud">\s*<div class="subtitle-text" id="([^"]+)">([\s\S]*?)</div>\s*</div>')
    new_sub_html = r'<div class="subtitle-hud">\n      <div class="subtitle-capsule">\n        <div class="subtitle-text" id="\1">\2</div>\n      </div>\n    </div>'
    content = old_sub_html.sub(new_sub_html, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

for scene_file, sid in [
    ("compositions/scene2_70k.html", "s2-sub"),
    ("compositions/scene3_install.html", "s3-sub"),
    ("compositions/scene4_product.html", "s4-sub"),
    ("compositions/scene5_app.html", "s5-sub")
]:
    update_file(scene_file, sid)
