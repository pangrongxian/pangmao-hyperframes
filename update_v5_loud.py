import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(r'data-duration="96\.5"', 'data-duration="92.0"', content)
content = re.sub(r'src="assets/audio_mixed_v5\.mp3"', 'src="assets/audio_master_v5_loud.mp3"', content)
content = re.sub(r'(id="scene6"[\s\S]*?data-duration=)"25\.1"', r'\1"20.6"', content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated index.html")

# 2. Update compositions/scene6_outro.html to ensure clean fadeout at 20.35s
with open("compositions/scene6_outro.html", "r", encoding="utf-8") as f:
    s6 = f.read()

if 'tl.to("#root"' not in s6:
    s6 = s6.replace('window.__timelines["scene6"] = tl;', 'tl.to("#root", { opacity: 0, duration: 0.25 }, 20.35);\n    window.__timelines["scene6"] = tl;')

with open("compositions/scene6_outro.html", "w", encoding="utf-8") as f:
    f.write(s6)
print("Updated scene6_outro.html")
