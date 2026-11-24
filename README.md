# 🎬 胖猫 HyperFrames 视频生成引擎 (Pangmao HyperFrames Video Engine)

> 基于 **HyperFrames + GSAP 3 + Edge-TTS + FFmpeg** 的高质感自媒体与科技教程短视频工程。  
> 告别千篇一律的固定死板模板，以“暖纸极简（亚里风格）”为基底，根据不同文案脚本定制专属的炫酷视觉动效与精准音画同步。

---

## 🌟 核心特性与设计哲学

- 🎨 **Warm Editorial 亚里设计风格**：
  - 54px 建筑透光网格底纹 + 暖调米白纸质底色 (`#FCFAF5`)
  - 黏土态 (Claymorphism) 微拟物卡片，双层柔和弥散阴影
  - 36px 底部磨砂玻璃胶囊字幕，字号层级清晰，关键词品牌金黄高亮
- ⚡ **文案定制化，拒绝模板套路**：
  - 每条文案独立拆解叙事节拍（Hook、Dual Core、Decision Flow、Console Mockup 等）
  - 包含 12+ 种可复用的高级视觉隐喻动效（3D 账单下坠碎裂、双反应堆粒子聚变、动态决策分叉树、拟态手机投币交互、景深准星推焦、全息防御盾等）
- 🔊 **专业级音频处理流**：
  - 微软自然语音云端生成（如经典的 `zh-CN-YunxiaNeural`，精准语速微调）
  - 毫秒级字句时间戳提取与音画锚定
  - 自动闪避 BGM（Ducking）、立体声音效（SFX Hits）毫秒对齐与多级压限提升 (`-18.6 dB LUFS`)
- 🛑 **品牌永恒定格 (Grand Outro Hold)**：
  - 视频尾帧绝不黑屏，永久定格于个人 IP / 品牌展示页，增强记忆点与完播转化率

---

## 📁 目录结构

```text
pangmao-hyperframes/
├── compositions/             # HTML5 + GSAP 场景动效组件
│   ├── deal_s1_hook.html     # Scene 1: 痛点与破局 (3D 账单下坠)
│   ├── deal_s2_flagship.html # Scene 2: 双旗舰核聚变 (双粒子旋转汇聚)
│   ├── deal_s3_selfcheck.html# Scene 3: 账号自检分流 (决策分叉树)
│   ├── deal_s4_step1.html    # Scene 4: 步骤一 清除旧冲突 (macOS 碎纸)
│   ├── deal_s5_step2.html    # Scene 5: 步骤二 敲门砖引子 (拟态 iPhone 投币)
│   ├── deal_s6_step3.html    # Scene 6: 步骤三 刷新刷出五折 (准星景深锁定)
│   ├── deal_s7_pitfalls.html # Scene 7: 避坑指南 (赛博时钟 & 全息护盾)
│   └── deal_s8_outro.html    # Scene 8: 品牌尾页定格 (胖猫 AI 永久悬浮)
├── assets/                   # 音频、音效、BGM 与高清截图资产
│   ├── bgm/                  # 背景音乐库
│   ├── sfx/                  # 动态音效库 (whoosh, pop, ding, coin 等)
│   ├── deal_master_audio.mp3 # Gemini 实测指南母带完整音轨
│   ├── deal_timestamps.json  # 场景与字幕时间戳映射表
│   └── gsap.min.js           # 本地离线高性能动效引擎
├── docs/                     # 制作手册与开发规范
│   └── VIDEO_CREATION_PLAYBOOK.md # 核心制作指导与动效设计资产库
├── video_template_framework/ # 模块化代码生成引擎
│   ├── core/                 # 核心组件库与原型模板
│   ├── cli.py                # 快速脚手架命令行
│   └── design_tokens.json    # 统一视觉设计 Token
├── out/                      # 渲染快照与产物目录
│   └── deal_snapshots/       # 场景高分辨率验证快照
├── hyperframes.json          # HyperFrames 项目编排清单
└── index.html                # 复合多场景挂载与时间轴驱动入口
```

---

## 🚀 快速上手

### 1. 环境准备

确保已安装：
- **Node.js** (v18+)
- **Python** (3.10+) 及 `edge-tts`
- **FFmpeg** (带 libx264 与 aac 编码支持)
- **HyperFrames CLI**

```bash
pip install edge-tts
```

### 2. 本地预览开发

在项目根目录下启动本地开发服务器或直接使用 HyperFrames：

```bash
# 启动本地实时动效预览
hyperframes preview

# 或使用任意本地 HTTP 静态服务器直接查看 index.html
python3 -m http.server 8080
```

### 3. 一键渲染 1080P 全高清视频

```bash
hyperframes render --out out/gemini_pro_deal_v1.mp4 --fps 30 --width 1920 --height 1080
```

---

## 📚 视频制作 SOP 与动效指南

查阅完整的 **[VIDEO_CREATION_PLAYBOOK.md](docs/VIDEO_CREATION_PLAYBOOK.md)**：
1. **文案拆解黄金法则**：如何根据一篇文章提炼 Hook、反转、实操与排坑
2. **12 大酷炫动效资产库**：源码级 GSAP 实现参数与视觉规范
3. **音频工程标准**：配音增益、背景音乐智能避让与音效毫秒对齐法则
4. **渲染前质检清单**：避免穿帮、掉帧、截断与黑屏的 10 项严苛审查

---

## 👤 作者与致谢

- **作者**：胖猫 AI (Pangmao AI)
- **宗旨**：带你探索 AI 时代超级个体之路
- **开源协议**：[MIT License](LICENSE)

