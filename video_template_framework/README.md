# 胖猫视频工坊 · 通用视频制作神器项目框架
> **Universal Video Creation Framework (Warm-Tech Editorial Architecture)**  
> 基于“亚里”温暖纸质编排设计系统与 HyperFrames 引擎沉淀的标准化、模块化、数据驱动通用视频生产框架。

---

## 🌟 框架核心特性

1. **零代码 / 声明式视频编排（Declarative JSON-Driven）**
   - 通过配置 `episode_config.json` 即可定义全片镜头、起止时间戳、字幕、音效与交互动画。
   - 一键自动生成 `index.html` 与全套场景组件 `compositions/*.html`。

2. **6 大开箱即用经过实战验证的场景原型（Proven Scene Archetypes）**
   - **`grid_cards`（功能矩阵）**：4 列 / N 列拟态卡片网格，支持鼠标光标平滑寻址点击、单卡聚焦放大高亮（`scale: 1.08`）、未选中卡片降亮（`opacity: 0.32`）。
   - **`leaderboard`（天梯榜单）**：动态 Elo 评测柱状动画、金银铜排行勋章、百万级翻滚计数器。
   - **`process_flow`（双轨流程对比）**：传统模式 vs 极速模式双管道对比，内置深色 IDE 语法高亮终端打字机效果。
   - **`workspace_prd`（企划工作台）**：里程碑节点轴 + 产品经理需求气泡对话 + PRD 条目动态打钩（✓）+ 自动编码 0%~100% 进度条。
   - **`app_satellites`（成品卫星卡）**：居中视口浏览器模拟器 + 四角环绕功能卡片，单卡依次选中有机交互与声波律动。
   - **`poster_outro`（海报长图收尾）**：手机画框平滑长图自动滚动 + 互动福利 CTA 脉冲卡片 + 品牌全屏大结局。**保证最后一帧定格不黑屏**！

3. **工业级自动化混音母带引擎（Audio Mastering Engine）**
   - **攻克 FFmpeg `amix` 音量衰减陷阱**：避免多路混音时音量被平均除以 N 的问题。
   - **专业响度标定**：原声人声动态增益压缩（`volume=2.2,alimiter=0.95`），BGM 纯音乐氛围低音垫乐（`volume=0.06`，-26 dB），全片平均响度稳定在 **-18.9 dB** 广播级标准。
   - **23 节点微秒级音效自动对齐**：内置精选音效库（`pop_click`、`whoosh`、`ding`、`check`、`tap`）。

4. **高辨识度“亚里”温暖纸质设计系统（Warm Paper Design System）**
   - **底色**：温暖径向渐变 `#FCFAF5` → `#F5F1E6` 搭配 54px 建筑网格。
   - **卡片**：纯白 Claymorphism 黏土拟态，多重柔和弥散阴影与 28px 圆角。
   - **字幕**：36px 加粗浮空胶囊，毛玻璃模糊 `backdrop-filter: blur(14px)`，居中悬浮极佳易读性。
   - **出镜 HUD**：双环微动呼吸头像，带正弦波轻柔浮沉。

---

## 📁 目录结构

```text
video_template_framework/
├── README.md                          # 框架开发与使用手册
├── cli.py                             # 框架统一 CLI 工具 (init/build/audio/render)
├── design_tokens.json                 # 全局设计规范 (色彩、网格、字号、阴影、混音参数)
├── episode_config.template.json       # 新视频标准配置模板
├── episode_config.pangmao_v5.json     # 完整官方实战生产样例配置
├── core/
│   ├── __init__.py
│   ├── tokens.py                      # 设计 Token 管理与基础 CSS 注入
│   ├── components.py                  # 基础 UI 组件 (导航标、品牌弧形、头像HUD、字幕胶囊、光标)
│   ├── audio_engine.py                # 自动化双阶段音频母带混合引擎
│   ├── compiler.py                    # JSON -> HTML 页面全自动编译器
│   └── archetypes/                    # 6 大场景组件生成器
│       ├── grid_cards.py              # 原型 1: 功能卡片矩阵
│       ├── leaderboard.py             # 原型 2: 天梯榜单与大数字
│       ├── process_flow.py            # 原型 3: 双轨流程与终端
│       ├── workspace_prd.py           # 原型 4: PRD 企划工作台
│       ├── app_satellites.py          # 原型 5: 真实成品与卫星功能卡
│       └── poster_outro.py            # 原型 6: 滚动长图与品牌定格
└── assets/
    ├── gsap.min.js                    # GSAP 3.12.5 核心动画库
    ├── avatar.jpg                     # 默认出镜讲解员头像
    ├── top10_poster.jpg               # 原型长图样例
    ├── bgm/                           # 授权免版税 BGM 乐库
    └── sfx/                           # 精品交互音效库 (.wav)
```

---

## 🚀 极速上手：三步出片

### 1. 初始化新视频工程
在任意目标文件夹初始化一个新的视频项目：
```bash
python3 video_template_framework/cli.py init my_new_video
cd my_new_video
```
CLI 会自动复制所需的设计规范、音效包、字体、模板配置文件并建立规范目录。

### 2. 编辑配置并编译页面
根据你的剧本需求，修改 `episode_config.json` 中的各场景文字、类型与字幕：
```bash
# 编译生成 index.html 和 compositions/*.html
python3 /path/to/cli.py build
```

### 3. 母带混音与最终渲染
```bash
# 一键母带混音 (自动对齐人声、乐垫与音效)
python3 /path/to/cli.py master-audio

# 抽检关键帧快照 (0.1秒出图用于快速校验设计)
python3 /path/to/cli.py snapshot --out out/snapshots

# 渲染 1080P @ 30fps MP4 最终成品
python3 /path/to/cli.py render --out out/final_video.mp4

# 校验视频格式与响度规格
python3 /path/to/cli.py inspect out/final_video.mp4
```

---

## 🎛️ CLI 命令行工具手册

| 命令 | 别名 | 说明 | 示例 |
| :--- | :--- | :--- | :--- |
| `init` | - | 脚手架初始化新项目目录 | `python3 cli.py init my_project` |
| `build` | `generate` | 将 JSON 配置文件编译为 HTML 工程 | `python3 cli.py build --config config.json` |
| `master-audio`| `audio` | 执行专业双阶段混音（增益+压限+下潜） | `python3 cli.py master-audio` |
| `snapshot` | - | 快速截取各分段关键帧图片验证排版 | `python3 cli.py snapshot --at 11,28,52` |
| `render` | - | 调用 HyperFrames 渲染出 MP4 视频 | `python3 cli.py render --out out/v1.mp4` |
| `inspect` | - | 查看视频编码流信息与声音平均响度 | `python3 cli.py inspect out/v1.mp4` |

---

## 🎨 场景原型配置指南

### 原型 1: `grid_cards` (功能卡片矩阵)
```json
{
  "id": "scene1",
  "type": "grid_cards",
  "chapter_num": "01",
  "chapter_title": "发现神器",
  "start": 0.0,
  "duration": 14.0,
  "cards": [
    { "id": "c1", "title": "连数据库", "desc": "秒级打通业务数据底座", "tag": "实时直连", "color": "#0284C7" },
    { "id": "c2", "title": "做 PPT", "desc": "商务演说级美学输出", "tag": "一键排版", "color": "#F59E0B" }
  ]
}
```

### 原型 2: `leaderboard` (天梯榜单与大数字)
```json
{
  "id": "scene2",
  "type": "leaderboard",
  "chapter_num": "02",
  "chapter_title": "浩瀚生态",
  "counter_target": "1,514,280",
  "start": 14.0,
  "duration": 10.5
}
```

### 原型 3: `process_flow` (双轨流程对比)
```json
{
  "id": "scene3",
  "type": "process_flow",
  "chapter_num": "03",
  "chapter_title": "一键安装",
  "start": 24.5,
  "duration": 12.5
}
```

### 原型 4: `workspace_prd` (PRD 企划工作台)
```json
{
  "id": "scene4",
  "type": "workspace_prd",
  "chapter_num": "04",
  "chapter_title": "需求企划",
  "start": 37.0,
  "duration": 20.8
}
```

### 原型 5: `app_satellites` (成品与卫星功能卡)
```json
{
  "id": "scene5",
  "type": "app_satellites",
  "chapter_num": "05",
  "chapter_title": "极速交付",
  "app_url": "https://myapp.ai · 实时运行中",
  "start": 57.8,
  "duration": 13.6
}
```

### 原型 6: `poster_outro` (海报滚动与终局定格)
```json
{
  "id": "scene6",
  "type": "poster_outro",
  "chapter_num": "06",
  "chapter_title": "超级个体",
  "poster_src": "../assets/top10_poster.jpg",
  "cta_code": "666",
  "cta_reward": "免费领取全套资源包",
  "outro_title": "胖猫 AI",
  "outro_desc": "带你探索 AI 时代超级个体之路",
  "start": 71.4,
  "duration": 20.6
}
```

---

## 🔊 音频设计黄金法则

1. **避免默认 `amix` 踩坑**：永远不要使用 `amix=inputs=N` 默认参数，它会强制把每一个音频输入音量除以 $N$。框架已封装好 `normalize=0` 与离线 SFX 单轨渲染。
2. **人声母带标准**：
   - 原始解说人声：加 `volume=2.2,alimiter=limit=0.95`。
   - 目标平均响度（mean_volume）：保持在 `-18.0 dB` 至 `-19.5 dB`。
3. **BGM 垫乐标准**：
   - 纯音乐伴奏音量：控制在 `volume=0.06`（约 `-26 dB`），确保衬托氛围但绝不抢人声。
   - 结尾淡出：在全片结束前 2.5 秒触发柔和指数级 fade-out。
4. **音效（SFX）设计**：
   - 卡片切换、点击：`pop_click.wav`（时长 0.1s，音量 0.5）。
   - 镜头推进与大卡进入：`whoosh.wav`（音量 0.3）。
   - 关键概念与高潮提示：`ding.wav`（音量 0.35）。
   - 勾选与任务完成：`check.wav`（音量 0.35）。

