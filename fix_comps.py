import os, re

base_dir = "/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes/compositions"
mapping = {
    "scene1_hook": "scene1",
    "scene2_70k": "scene2",
    "scene3_install": "scene3",
    "scene4_product": "scene4",
    "scene5_app": "scene5",
    "scene6_outro": "scene6",
}

for fname, comp_id in mapping.items():
    fpath = os.path.join(base_dir, f"{fname}.html")
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Replace .scene-wrap with #root
    c = c.replace(".scene-wrap {", "#root {")
    c = c.replace(f'class="scene-wrap" id="{comp_id}-wrap"', f'id="root"')
    c = c.replace(f'id="{comp_id}-wrap"', 'id="root"')
    c = c.replace(f'#{comp_id}-wrap', '#root')

    # 2. Fix fonts: replace custom monospace with standard sans-serif / monospace
    c = c.replace('ui-monospace, SFMono-Regular, Menlo, monospace', 'monospace')
    c = c.replace('ui-monospace, monospace', 'monospace')

    # 3. Fix avatar tween overlap in scene1
    if comp_id == "scene1":
        c = c.replace(
            'tl.to("#s1-avatar", { y: "-=8", duration: 1.6, yoyo: true, repeat: 6, ease: "sine.inOut" }, 1.0);',
            'tl.fromTo("#s1-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 6, ease: "sine.inOut" }, 1.3);'
        )
    if comp_id in ["scene2", "scene3", "scene4", "scene5", "scene6"]:
        c = re.sub(
            r'tl\.to\(["\']#s\d-avatar["\'],\s*\{\s*y:\s*["\']-=8["\']',
            r'tl.fromTo("#' + comp_id.replace("scene", "s") + r'-avatar", { y: 0 }, { y: -8',
            c
        )

    # 4. In scene6, replace second img with div background
    if comp_id == "scene6":
        c = c.replace(
            '<img src="assets/avatar.jpg" alt="胖猫AI" />',
            '<div style="width:100%; height:100%; border-radius:50%; background:url(assets/avatar.jpg) center/cover no-repeat;"></div>'
        )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)
    print("Fixed", fname)

