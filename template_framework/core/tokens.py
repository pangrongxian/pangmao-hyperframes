"""
Design Token Manager and Common Styles Generator for Warm-Tech Editorial Theme
"""

import os
import json

DEFAULT_TOKENS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "design_tokens.json")

def load_tokens(path=None):
    if path is None:
        path = DEFAULT_TOKENS_PATH
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_common_css(tokens=None):
    if tokens is None:
        tokens = load_tokens()
        
    c = tokens["colors"]
    t = tokens["typography"]
    s = tokens["shadows"]
    l = tokens["layout"]
    g = tokens["grid"]

    return f"""
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
    html, body {{
      margin: 0;
      width: {l['width']}px;
      height: {l['height']}px;
      overflow: hidden;
      background: {c['background']};
      font-family: {t['fontFamily']};
      color: {c['textPrimary']};
      -webkit-font-smoothing: antialiased;
    }}
    #root {{
      position: absolute;
      inset: 0;
      width: {l['width']}px;
      height: {l['height']}px;
      overflow: hidden;
      font-family: {t['fontFamily']};
      color: {c['textPrimary']};
    }}

    /* Paper Texture Radial & Grid Background */
    .paper-bg {{
      position: absolute;
      inset: 0;
      background: {c['backgroundRadial']};
      pointer-events: none;
      z-index: 0;
    }}
    .ambient-grid {{
      position: absolute;
      inset: 0;
      background-image: 
        linear-gradient({c['gridLine']} {g['lineWidth']}, transparent {g['lineWidth']}),
        linear-gradient(90deg, {c['gridLine']} {g['lineWidth']}, transparent {g['lineWidth']});
      background-size: {g['size']};
      pointer-events: none;
      z-index: 1;
    }}

    /* Navigation Header */
    .header-nav {{
      position: absolute;
      top: {l['headerTop']};
      left: {l['headerLeft']};
      display: flex;
      align-items: baseline;
      gap: 12px;
      z-index: 50;
    }}
    .nav-num {{
      font-size: {t['chapterNumberSize']};
      font-weight: 800;
      color: {c['accentGold']};
      letter-spacing: 0.02em;
    }}
    .nav-title {{
      font-size: {t['chapterTitleSize']};
      font-weight: 800;
      color: {c['textPrimary']};
      letter-spacing: 0.04em;
    }}

    /* Brand Canopy Arch */
    .header-brand {{
      position: absolute;
      top: 42px;
      right: {l['headerRight']};
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 50;
    }}
    .brand-arch {{
      width: 32px;
      height: 6px;
      border-top: 3.5px solid {c['accentGold']};
      border-radius: 50%;
      margin-bottom: 2px;
    }}
    .brand-title {{
      font-size: {t['brandTitleSize']};
      font-weight: 900;
      color: {c['textPrimary']};
      letter-spacing: 0.16em;
    }}

    /* Presenter HUD */
    .avatar-hud {{
      position: absolute;
      bottom: {l['avatarBottom']};
      left: {l['avatarLeft']};
      width: {l['avatarSize']};
      height: {l['avatarSize']};
      border-radius: 50%;
      background: #FAF7F0;
      border: 4px solid #FFFFFF;
      box-shadow: {s['avatarHud']};
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

    /* Elevated Subtitle Capsule */
    .subtitle-hud {{
      position: absolute;
      bottom: {l['subtitleBottom']};
      left: {l['subtitlePaddingX']};
      right: {l['subtitlePaddingX']};
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 60;
      pointer-events: none;
    }}
    .subtitle-capsule {{
      background: {c['capsuleBackground']};
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1.5px solid {c['capsuleBorder']};
      border-radius: 9999px;
      padding: 12px 42px;
      box-shadow: {s['capsule']};
      display: inline-flex;
      align-items: center;
      justify-content: center;
      max-width: 1440px;
    }}
    .subtitle-text {{
      font-size: {t['subtitleSize']};
      font-weight: 850;
      color: {c['textPrimary']};
      letter-spacing: 0.03em;
      text-align: center;
      line-height: 1.35;
    }}
    .sub-hl {{
      color: {c['accentGold']};
      font-weight: 900;
      background: rgba(254, 243, 199, 0.55);
      padding: 1px 8px;
      border-radius: 6px;
    }}

    /* Cursor Hand Pointer */
    .hand-pointer {{
      position: absolute;
      width: 54px;
      height: 54px;
      pointer-events: none;
      z-index: 100;
      filter: drop-shadow({s['pointerShadow']});
      opacity: 0;
    }}
"""
