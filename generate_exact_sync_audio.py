import asyncio
import os
import json
import subprocess
import edge_tts

sentences = [
    # 0
    "当你一不小心在 skills 后面加了个 sh，你就进入了这个全球最大的 AI Agent Skills 技能库！",
    # 1
    "有帮你连数据库的、做 PPT 的、写长文的、做海报的。",
    # 2
    "面对如今浩如烟海的 151 万多个 skills，哪怕你是零基础文科生，也能通过 Vibe Coding 轻松手搓出一个全功能网站！",
    # 3
    "操作极度丝滑：在 skills.sh 上选中「头脑风暴」skill，点击复制；随即打开 Cursor，把代码直接丢进对话框，下一秒这个技能就装好了！",
    # 4
    "然后你对 Cursor 说：“我想做一个适合家长带孩子学英语的网站，先帮我头脑风暴，再写代码。”",
    # 5
    "Cursor 瞬间变身顶尖产品经理，不仅和你梳理需求，还自动输出了一份完整的 PRD 企划案！确认后，Cursor 直接开始自动写代码。",
    # 6
    "只需要 3 分钟，你的网站就做好了！打开一看：分级阅读库、AI 实时发音纠错、趣味生词本，甚至还有独立的家长伴学仪表盘，功能一应俱全！",
    # 7
    "学会了 skills，就等于给你的 AI 免费培训了数万个随时上岗的顶级员工。最实用的 10 个高频 skills 已经给大家打包整理好了，评论区回复「666」免费领取。",
    # 8
    "我是胖猫 AI，带你探索 AI 超级个体之路，咱们下期见！"
]

temp_dir = "/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes/assets/audio_parts"
os.makedirs(temp_dir, exist_ok=True)
ffprobe = "/Users/rongxianpang/Desktop/video-project/bin/ffprobe"
ffmpeg = "/Users/rongxianpang/Desktop/video-project/bin/ffmpeg"

async def gen_all():
    part_files = []
    timings = []
    current_time = 0.2  # 0.2s pre-roll for smoothness
    
    for idx, text in enumerate(sentences):
        out_mp3 = os.path.join(temp_dir, f"part_{idx}.mp3")
        # Use zh-CN-YunxiaNeural (星仔的专属音色) with +8% rate for lively tempo
        comm = edge_tts.Communicate(text, "zh-CN-YunxiaNeural", rate="+8%")
        await comm.save(out_mp3)
        
        # probe duration
        res = subprocess.run([ffprobe, "-v", "quiet", "-show_entries", "format=duration", "-of", "json", out_mp3], capture_output=True, text=True)
        dur = float(json.loads(res.stdout)["format"]["duration"])
        
        start_t = round(current_time, 2)
        end_t = round(current_time + dur, 2)
        timings.append({
            "index": idx,
            "text": text,
            "file": f"part_{idx}.mp3",
            "start": start_t,
            "end": end_t,
            "duration": round(dur, 2)
        })
        part_files.append(out_mp3)
        # 0.35s pause between sentences
        current_time = end_t + 0.35
    
    total_dur = round(current_time, 2)
    print(f"Total calculated audio duration: {total_dur}s")
    
    # Create silence wav
    silence_wav = os.path.join(temp_dir, "silence.wav")
    subprocess.run([ffmpeg, "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", "0.35", "-q:a", "9", silence_wav], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Create pre-roll silence
    preroll_wav = os.path.join(temp_dir, "preroll.wav")
    subprocess.run([ffmpeg, "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", "0.2", "-q:a", "9", preroll_wav], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    list_txt = os.path.join(temp_dir, "concat_list.txt")
    with open(list_txt, "w") as f:
        f.write(f"file '{preroll_wav}'\n")
        for idx, p in enumerate(part_files):
            f.write(f"file '{p}'\n")
            if idx < len(part_files) - 1:
                f.write(f"file '{silence_wav}'\n")
    
    master_mp3 = "/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes/assets/audio.mp3"
    subprocess.run([ffmpeg, "-y", "-f", "concat", "-safe", "0", "-i", list_txt, "-c:a", "libmp3lame", "-b:a", "192k", master_mp3], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Probe final audio
    res = subprocess.run([ffprobe, "-v", "quiet", "-show_entries", "format=duration", "-of", "json", master_mp3], capture_output=True, text=True)
    real_dur = float(json.loads(res.stdout)["format"]["duration"])
    print(f"Final audio created: {master_mp3} | Real duration: {real_dur:.2f}s")
    
    # Save precise timestamps
    final_data = {
        "voice": "zh-CN-YunxiaNeural (星仔设计音色)",
        "duration": round(real_dur, 2),
        "sentences": timings
    }
    with open("/Users/rongxianpang/Desktop/video-project/pangmao-hyperframes/assets/timestamps.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
    
    for t in timings:
        s = t['start']
        e = t['end']
        txt = t['text']
        print(f"[{s:>5.2f}s - {e:>5.2f}s]: {txt}")

if __name__ == "__main__":
    asyncio.run(gen_all())

