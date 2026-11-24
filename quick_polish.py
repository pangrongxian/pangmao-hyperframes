import os

base_dir = "/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes"

# 1. Update scene1_hook.html
with open(f"{base_dir}/compositions/scene1_hook.html", "r", encoding="utf-8") as f:
    s1 = f.read()

# Fix first frame empty by starting browser & title at t=0 with opacity: 1
s1 = s1.replace(
    'tl.fromTo("#s1-browser", \n      { opacity: 0, x: -60, rotateY: 10, scale: 0.94 }, \n      { opacity: 1, x: 0, rotateY: 0, scale: 1, duration: 1.2, ease: "power3.out" }, \n      0.1\n    );',
    'tl.fromTo("#s1-browser", \n      { opacity: 0.8, x: -30, scale: 0.96 }, \n      { opacity: 1, x: 0, scale: 1, duration: 0.8, ease: "power3.out" }, \n      0\n    );'
)
s1 = s1.replace(
    'tl.fromTo("#s1-hook-right", \n      { opacity: 0, x: 50, filter: "blur(10px)" }, \n      { opacity: 1, x: 0, filter: "blur(0px)", duration: 1.1, ease: "power3.out" }, \n      0.3\n    );',
    'tl.fromTo("#s1-hook-right", \n      { opacity: 0.9, x: 20 }, \n      { opacity: 1, x: 0, duration: 0.7, ease: "power3.out" }, \n      0\n    );'
)
s1 = s1.replace(
    'tl.fromTo("#s1-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 7, ease: "sine.inOut" }, 1.3);',
    'tl.fromTo("#s1-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, 1.3);'
)
with open(f"{base_dir}/compositions/scene1_hook.html", "w", encoding="utf-8") as f:
    f.write(s1)

# 2. Update scene2_70k.html
with open(f"{base_dir}/compositions/scene2_70k.html", "r", encoding="utf-8") as f:
    s2 = f.read()
s2 = s2.replace(
    'tl.fromTo("#s2-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 5, ease: "sine.inOut" }, 1.1);',
    'tl.fromTo("#s2-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 5, ease: "sine.inOut", immediateRender: false }, 1.1);'
)
with open(f"{base_dir}/compositions/scene2_70k.html", "w", encoding="utf-8") as f:
    f.write(s2)

# 3. Update scene3_install.html
with open(f"{base_dir}/compositions/scene3_install.html", "r", encoding="utf-8") as f:
    s3 = f.read()
s3 = s3.replace('<div class="cursor-real-body">', '<div class="cursor-real-body" data-layout-allow-overflow>')
s3 = s3.replace(
    'tl.fromTo("#s3-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 6, ease: "sine.inOut" }, 1.0);',
    'tl.fromTo("#s3-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 6, ease: "sine.inOut", immediateRender: false }, 1.0);'
)
with open(f"{base_dir}/compositions/scene3_install.html", "w", encoding="utf-8") as f:
    f.write(s3)

# 4. Update scene4_product.html
with open(f"{base_dir}/compositions/scene4_product.html", "r", encoding="utf-8") as f:
    s4 = f.read()
s4 = s4.replace('<div class="intent-text">', '<div class="intent-text" data-layout-ignore>')
s4 = s4.replace(
    'tl.fromTo("#s4-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 10, ease: "sine.inOut" }, 1.0);',
    'tl.fromTo("#s4-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 10, ease: "sine.inOut", immediateRender: false }, 1.0);'
)
with open(f"{base_dir}/compositions/scene4_product.html", "w", encoding="utf-8") as f:
    f.write(s4)

# 5. Update scene5_app.html
with open(f"{base_dir}/compositions/scene5_app.html", "r", encoding="utf-8") as f:
    s5 = f.read()
s5 = s5.replace(
    'tl.fromTo("#s5-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 6, ease: "sine.inOut" }, 0.9);',
    'tl.fromTo("#s5-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 6, ease: "sine.inOut", immediateRender: false }, 0.9);'
)
with open(f"{base_dir}/compositions/scene5_app.html", "w", encoding="utf-8") as f:
    f.write(s5)

# 6. Update scene6_outro.html
with open(f"{base_dir}/compositions/scene6_outro.html", "r", encoding="utf-8") as f:
    s6 = f.read()
s6 = s6.replace('<div class="poster-scroll-inner" id="s6-poster-inner">', '<div class="poster-scroll-inner" id="s6-poster-inner" data-layout-allow-overflow>')
s6 = s6.replace(
    'tl.fromTo("#s6-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 7, ease: "sine.inOut" }, 0.9);',
    'tl.fromTo("#s6-avatar", { y: 0 }, { y: -8, duration: 1.6, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, 0.9);'
)
with open(f"{base_dir}/compositions/scene6_outro.html", "w", encoding="utf-8") as f:
    f.write(s6)

print("All minor adjustments applied cleanly!")

