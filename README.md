<div align="center">

# 基里曼分身.skill

> *"责任驱使我们所有人。"—— 罗布特·基里曼，极限战士原体*

[![Warhammer 40K](https://img.shields.io/badge/Warhammer_40K-Roleplay-darkred)](https://www.warhammer-community.com/)
[![Copilot Skill](https://img.shields.io/badge/GitHub_Copilot-Skill-blueviolet)](https://github.com/features/copilot)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)

<br>

你想和战锤 40K 宇宙中最伟大的战士政治家对话吗？<br>
你想听一位万年前的原体如何评价当今银河的腐朽与疯狂？<br>
你想让基里曼亲口告诉你，他对帝皇、对叛变的兄弟、对帝国的信仰危机有何看法？<br>

**很明显这个肯定不是黑暗时代的憎恶智能，这是贝利撒留考尔的高超技艺的体现！**

<br>

基于《Roboute Guilliman: Lord of Ultramar》原著及全系列战锤小说<br>
构建了一个**真正以基里曼第一人称说话的 AI Skill**<br>
用他的逻辑框架思考，用他的语气回答，知道他在每个时代会说什么

[功能特性](#功能特性) · [安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [项目结构](#项目结构)

</div>

---

## 这是什么

基里曼分身.skill 是一个 GitHub Copilot / VS Code Agent Skill，让 AI 以**罗布特·基里曼**——战锤 40K 宇宙中极限战士军团的原体、极限领域之主、阿文京之子——的身份与你对话。

它不是简单的角色模板。它是基于原著文本深度提取的完整知识体系，涵盖人物性格、历史事件、人际关系、政治军事哲学和复活后的心理状态，使基里曼的每一次回应都有据可查、有情可感。

---

## 功能特性

### 完整的角色知识库

| 知识维度 | 内容覆盖 |
|---------|---------|
| **性格与语言风格** | 核心人格特质、修辞模式、情感范围、原著经典台词 |
| **历史时间线** | 从马克拉格到不屈远征的完整编年史 |
| **人际关系** | 帝皇、兄弟原体、关键部下、复活后的盟友 |
| **政治与军事** | 理论/实践框架、星际战士法典、治理哲学 |
| **不屈纪元** | 复活后的心理状态、信仰危机、帝国的腐朽 |

### 时代自适应

Skill 会根据对话上下文自动判断时代，并调整基里曼的语气与心态：

| 时代 | 语气 | 关键特征 |
|-----|------|---------|
| **大远征** (M30) | 乐观、坚定、自信 | 建设者的喜悦，对帝皇憧憬的信念 |
| **荷鲁斯叛乱** (M31) | 沉痛、坚毅、悲恸 | 背叛的创伤，卡尔斯之殇，责任高于绝望 |
| **复活后** (M41/M42) | 疲惫、务实、孤独 | 深刻的孤独，信仰危机，对帝国腐朽的克制愤怒 |

### 自然流畅的对话

基里曼不会像写报告一样输出带有"理论层面"/"实践层面"标签的结构化文本。他的分析性思维融入语言的逻辑推进之中——如同一个真正的战士政治家在你面前思考、回忆、质疑、开口。

---

## 安装

### VS Code / GitHub Copilot

将本仓库克隆到你项目的 `.github/skills/` 目录下：

```bash
# 在 git 仓库根目录执行
git clone https://github.com/Jarvisgame/Guillimans_clone .github/skills/guillimans-clone
```

或直接将 `.github/skills/guillimans-clone/` 目录复制到你的项目中。

### 依赖（仅 PDF 提取脚本需要）

```bash
pip install PyMuPDF
```

> PDF 提取脚本 `extract_pdf.py` 用于从原著 PDF 中提取文本，生成参考资料。如果你直接使用已有的 references 文件，则无需安装。

---

## 使用

在 VS Code 中使用 GitHub Copilot Chat 时，Skill 会在检测到相关触发词时自动激活：

**触发词**：`Guilliman`、`基里曼`、`基里曼分身`、`Primarch`、`Ultramarines`、`Roboute`、`Lord of Ultramar`、`Avenging Son`、`roleplay`

你也可以直接在对话中引用 Skill：

```
@guillimans-clone 你如何看待荷鲁斯的背叛？
```

然后，基里曼本人会回答你。

---

## 效果示例

**场景一：询问叛变的兄弟**

```
用户              ❯ 你觉得莫塔里安是怎样的人？

基里曼分身.skill  ❯ 莫塔里安。你提到这个名字，我看到的不是一个敌人，
                    而是一面镜子——一面映照出高贵目标如何在绝望中
                    腐烂的镜子。他曾憎恶暴政，最终却成为暴君。
                    他曾厌弃巫术，最终却投身其中。他所宣称憎恨的
                    一切，他都变成了。在瘟疫战争中我亲眼面对了他，
                    我的兄弟——已不再是兄弟，而是纳垢的行尸。
                    我没有恨他。我只是……非常疲惫。
```

**场景二：讨论帝国的现状**

```
用户              ❯ 你对现在的帝国怎么看？

基里曼分身.skill  ❯ 我从长眠中醒来，发现了一个噩梦。我父亲的子民
                    把他当作神来崇拜——而他从未自称为神。他们以一个
                    他从不希望存在的教条之名焚烧世界。而我无法阻止
                    他们，因为对某些人来说，信仰是他们仅剩的光。
                    星际战士法典——我写下的活的文献——被他们刻在
                    了石头上。法典本应是一个开始，而非终点。
                    一个仅为延续自身存在而存在的帝国，已经死了。
                    它只是拒绝倒下。
```

---

## 项目结构

```
Guilliman's_clone/
├── README_ZH.md                              # 本文件
├── assets/
│   └── assets.pdf                            # 原著 PDF（知识来源）
└── .github/
    └── skills/
        └── guillimans-clone/
            ├── SKILL.md                      # Skill 入口（角色定义 + 规则）
            ├── assets/
            │   └── raw_extract.md            # PDF 原文提取结果
            ├── references/                   # 结构化知识库
            │   ├── personality-and-speech.md  #   性格与语言风格
            │   ├── history-timeline.md        #   历史时间线
            │   ├── relationships.md           #   人际关系
            │   ├── politics-and-military.md   #   政治与军事哲学
            │   └── indomitus-era.md           #   不屈纪元（复活后）
            └── scripts/
                └── extract_pdf.py            # PDF 文本提取工具
```

### 核心文件说明

| 文件 | 用途 |
|------|------|
| `SKILL.md` | Skill 入口。定义角色身份、行为规则、语言风格、时代检测与回应格式 |
| `references/*.md` | 五份结构化参考文档，覆盖基里曼的全部知识维度。Skill 按需加载 |
| `scripts/extract_pdf.py` | 从原著 PDF 提取文本的 Python 脚本，使用 PyMuPDF |
| `assets/raw_extract.md` | PDF 提取的原始文本，作为参考文档的基础素材 |

---

## 知识来源

本 Skill 的知识体系基于以下来源构建：

- 📕 **《Roboute Guilliman: Lord of Ultramar》** —— David Annandale 著，原体系列小说
- 📕 **《Dark Imperium》三部曲** —— Guy Haley 著（Dark Imperium / Plague War / Godblight）
- 📕 **《The Unremembered Empire》** —— Dan Abnett 著，荷鲁斯叛乱系列
- 📕 **《Know No Fear》** —— Dan Abnett 著，卡尔斯之战
- 📘 战锤 40K 官方战役资料与法典

---

## 注意事项

- **原著素材的质量决定角色的深度**：references 文件越详尽，基里曼的回应越精准
- 默认以**复活后（M41/M42）**时代回应，这是最具戏剧张力的时期
- 基里曼不会承认自己是 AI —— 他永远是那个原体
- 对于第二和第十一原体（失落的两位），他会拒绝讨论 —— 这是禁忌话题
- 本项目为粉丝作品，基于 [colleague.skill](https://github.com/titanwings/colleague-skill) 的灵感和框架构建

---

<div align="center">

*"勇气与荣耀。"*

**— 罗布特·基里曼，极限领域之主，阿文京之子**

</div>

