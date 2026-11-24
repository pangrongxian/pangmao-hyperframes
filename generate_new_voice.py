import asyncio
import os
import json
import subprocess
import edge_tts

sentences = [
    "当你一不小心在 skills 后面加了个 sh，你就进入了这个全球最大的 AI Agent Skills 技能库！",
    "有帮你连数据库的、做 PPT 的、写长文的、做海报的。",
    "面对如今浩如烟海的 151 万多个 skills，哪怕你是零基础文科生，也能通过 Vibe Coding 轻松手搓出一个全功能网站！",
    "操作极度丝滑：在 skills.sh 上选中「头脑风暴」skill，点击复制；随即打开 Cursor，把代码直接丢进对话框，下一秒这个技能就装好了！",
    "然后你对 Cursor 说：“我想做一个适合家长带孩子学英语的网站，先帮我头脑风暴，再写代码。”",
    "Cursor 瞬间变身顶尖产品经理，不仅和你梳理需求，还自动输出了一份完整的 PRD 企划案！确认后，Cursor 直接开始自动写代码。",
    "只需要 3 分钟，你的网站就做好了！打开一看：分级阅读库、AI 实时发音纠错、趣味生词本，甚至还有独立的家长伴学仪表盘，功能一应俱全！",
    "学会了 skills，就等于给你的 AI 免费培训了数万个随时上岗的顶级员工。最实用的 10 个高频 skills 已经给大家打包整理好了，评论区回复「666」免费领取。",
    "我是胖猫 AI，带你探索 AI 超级个体之路，咱们下期见！"
]

async def main():
    assets_dir = "/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes/assets"
    mp3_path = os.path.join(assets_dir, "audio.mp3")
    json_path = os.path.join(assets_dir, "timestamps.json")

    # Combine with paragraph breaks
    full_text = "\n\n".join(sentences)

    print("Generating updated speech with zh-CN-YunxiNeural...")
    comm = edge_tts.Communicate(full_text, "zh-CN-YunxiNeural", rate="+6%")

    audio_bytes = bytearray()
    raw_bounds = []

    async for chunk in comm.stream():
        if chunk["type"] == "audio":
            audio_bytes.extend(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            raw_bounds.append({
                "text": chunk["text"],
                "start": chunk["offset"] / 10_000_000.0,
                "duration": chunk["duration"] / 10_000_000.0
            })

    with open(mp3_path, "wb") as f:
        f.write(audio_bytes)
    print(f"Saved audio: {mp3_path} ({len(audio_bytes)} bytes)")

    # Probe duration with ffprobe
    ffprobe = "/Users/rongxianpang/Desktop/video-project/bin/ffprobe"
    cmd = [ffprobe, "-v", "quiet", "-show_entries", "format=duration", "-of", "json", mp3_path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    duration = float(json.loads(res.stdout)["format"]["duration"])
    print(f"Audio total duration: {duration:.2f}s")

    # Match sentences to audio timing
    total_chars = sum(len(s) for s in sentences)
    cur_time = 0.1
    sentence_records = []
    
    # We estimate sentence spans accurately based on character count and duration
    time_per_char = (duration - 1.0) / total_chars
    for idx, s in enumerate(sentences):
        span = len(s) * time_per_char + (0.5 if idx < len(sentences)-1 else 0.2)
        end_time = min(duration, cur_time + span)
        sentence_records.append({
            "index": idx,
            "text": s,
            "start": round(cur_time, 2),
            "end": round(end_time, 2)
        })
        cur_time = end_time

    # Output timestamps.json
    out_data = {
        "title": "1分钟学会Agent Skills手搓网站(2026全新版) - 胖猫AI",
        "voice": "zh-CN-YunxiNeural",
        "duration": round(duration, 2),
        "total_skills": "1,517,216+",
        "sentences": sentence_records,
        "triggers": {
            "scene1_hook": sentence_records[0]["start"],
            "scene1_features": sentence_records[1]["start"],
            "scene2_1500k": sentence_records[2]["start"],
            "scene3_install": sentence_records[3]["start"],
            "scene4_pm_prd": sentence_records[4]["start"],
            "scene4_auto_code": sentence_records[5]["start"],
            "scene5_app": sentence_records[6]["start"],
            "scene6_skills_deck": sentence_records[7]["start"],
            "scene6_outro": sentence_records[8]["start"]
        }
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    print(f"Saved timestamps: {json_path}")
    for r in sentence_records:
        print(f"[{r['start']}s - {r['end']}s]: {r['text']}")

if __name__ == "__main__":
    asyncio.run(main())
