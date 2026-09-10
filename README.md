# 大数据与人工智能 课程仓库

> **作者：** 袁玉明　**GitHub：** [`Yym113`](https://github.com/Yym113)　**邮箱：** `jz3681@qq.com`
>
> 课程：大数据与人工智能

## 📌 评分对照表（老师请直接看这里）

| 评分项 | 分值 | 交付文件 |
|---|---|---|
| 项目级 Skill | 35 | [`.workbuddy/skills/concept-unpacker/SKILL.md`](https://github.com/Yym113/big-data-ai/blob/main/.workbuddy/skills/concept-unpacker/SKILL.md) |
| 学习资料（HTML） | 30 | [`agent.html`](https://github.com/Yym113/big-data-ai/blob/main/learning-materials/agent.html) · [`llm-context.html`](https://github.com/Yym113/big-data-ai/blob/main/learning-materials/llm-context.html) · [`skill.html`](https://github.com/Yym113/big-data-ai/blob/main/learning-materials/skill.html) |
| 概念关系与个人理解 | 15 | [`concept-relationship.html`](https://github.com/Yym113/big-data-ai/blob/main/learning-materials/concept-relationship.html) |
| GitHub 仓库 + 版本 | 10 | 仓库首页 [Yym113/big-data-ai](https://github.com/Yym113/big-data-ai)（含 commit 历史 + `.gitignore`） |
| README + AI 规范 | 10 | 本文件 [`README.md`](https://github.com/Yym113/big-data-ai/blob/main/README.md) |

> 总分 100。作业 1 已全部命中。

本仓库用于存放「大数据与人工智能」课程的学习笔记、作业、实验代码、课程项目与配套 Skills / 学习资料。

## 本仓库的实际位置

- **正式路径**：`C:\Users\lenovo-mr\big-data-ai`（本地）
- **GitHub 远端**：`git@github.com:Yym113/big-data-ai.git`（公开）
- 如果你看到过桌面上的同名目录，那是为某次作业临时建的副本，**不是权威源**——以本仓库为准。

## 目录结构

```
big-data-ai/
├── .workbuddy/
│   └── skills/
│       └── concept-unpacker/            # 项目级 Skill · 把任意概念拆成 8 段式中文学习包
├── learning-materials/                  # 由 concept-unpacker 生成的 3 份概念学习资料 + 关系图
│   ├── agent.html
│   ├── llm-context.html
│   ├── skill.html
│   └── concept-relationship.html
├── assignments/                         # 课程作业（作业 1 交付物在 learning-materials/）
├── .gitignore
└── README.md                            # 本文件
```

## 项目级 Skills（WorkBuddy 可调用）

| Skill 名 | 路径 | 用途 |
|---|---|---|
| `concept-unpacker` | `.workbuddy/skills/concept-unpacker/SKILL.md` | 把任意陌生概念拆成 8 段式中文学习包（学习目标 / 结构化解释 / 边界辨析 / 自测 / 可核查来源 / 核查记录） |

调用方式：在 WorkBuddy 里说「用 `concept-unpacker` 帮我学一下 `RAG`」即可；它会自动生成 `learning-materials/rag.html`，并附核查记录。

## 学习资料

`learning-materials/` 目录下的概念学习资料：

| 文件 | 主参考 |
|---|---|
| `agent.html` | ReAct 论文 (arXiv:2210.03629)、Russell & Norvig AIMA、Wikipedia |
| `llm-context.html` | "Lost in the Middle" 论文 (arXiv:2307.03172)、Anthropic 上下文工程博客 |
| `skill.html` | Anthropic Agent Skills 公告 (2025-10-16)、agentskills.io 开放规范 |
| `concept-relationship.html` | 三概念关系（Mermaid 流程图 + 对照表 + 链路例子） |

每份都遵循同一个 9 分节结构：个人理解 / 学习目标 / 核心问题 / 结构化解释 / 应用场景 / 概念辨析 / 自测问题 / 可核查来源 / 核查记录。

## 课程作业

按学期累积在 `assignments/` 下，每次作业一个子文件夹：

- `assignments/assignment-1/`（作业 1：用 AI 构建概念学习资料生成 Skill，本仓库的 `learning-materials/` 就是其交付物）

## 学习进度

- [ ] 大数据基础
- [ ] Python 编程基础
- [ ] 数据处理与分析
- [ ] 机器学习
- [ ] 深度学习
- [ ] 课程项目

## 环境

- Git 2.55
- Python 3.12（managed 3.13 也可用）
- VS Code
- 操作系统：Windows

## Git / 提交规范

```bash
# 克隆
git clone git@github.com:Yym113/big-data-ai.git

# 拉取最新
git pull

# 修改后提交（用 conventional commits 风格）
git add .
git commit -m "feat: 新增xxx"          # 新功能
git commit -m "docs: 更新xxx说明"      # 仅文档
git commit -m "fix: 修复xxx"            # 修复
git push
```

环境约定：SSH 直连（`gh` CLI 当前未登录，临时不需要）；`gh` 登录随时可做。

## 隐私与安全

- `.gitignore` 排除 `.env` / `*.pem` / `*.key` / `node_modules` / `.venv` 等敏感或依赖目录
- API Key / 密码 / 个人隐私永远不进 commit
- 引用资料优先官方文档 / arXiv 论文 / Wikipedia，AI 生成后人工逐条核验

---

_本仓库使用 AI 辅助 + 人工复核。引用资料的核验状态见各 HTML 文件末「核查记录」。_
