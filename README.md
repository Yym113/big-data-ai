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

## 📌 作业 2：仓库级 Skill（老师请直接看这里）

老师要求「**要创建仓库级别的 skill 完成**」——本仓库的 skills 全部存放在 `.workbuddy/skills/` 下，**作为仓库的一部分提交到 Git**（非用户级目录，clone 即可用，可在 GitHub 上审查）。

| 仓库级 Skill | 路径（GitHub 可查看） | 用途 |
|---|---|---|
| `concept-unpacker` | [`.workbuddy/skills/concept-unpacker/SKILL.md`](https://github.com/Yym113/big-data-ai/blob/main/.workbuddy/skills/concept-unpacker/SKILL.md) | 把任意陌生概念拆成 9 段式中文学习包 |
| `homework-submit` | [`.workbuddy/skills/homework-submit/SKILL.md`](https://github.com/Yym113/big-data-ai/blob/main/.workbuddy/skills/homework-submit/SKILL.md) | 作业提交与推送流程自动化 |

**Skill 的运行成果**（可直接打开查看）：

- 15 份 Python 概念学习资料 + 目录页 → [`learning-materials/index.html`](https://github.com/Yym113/big-data-ai/blob/main/learning-materials/index.html)
- 13 次课学习地图 → [`learning-materials/python-learning-map.html`](https://github.com/Yym113/big-data-ai/blob/main/learning-materials/python-learning-map.html)

详细说明见下方「仓库级 Skills」一节。

本仓库用于存放「大数据与人工智能」课程的学习笔记、作业、实验代码、课程项目与配套 Skills / 学习资料。

## 本仓库的实际位置

- **正式路径**：`C:\Users\lenovo-mr\big-data-ai`（本地）
- **GitHub 远端**：`git@github.com:Yym113/big-data-ai.git`（公开）
- 如果你看到过桌面上的同名目录，那是为某次作业临时建的副本，**不是权威源**——以本仓库为准。

## 目录结构

```
big-data-ai/
├── .workbuddy/
│   ├── skills/                          # 仓库级 Skills（随仓库提交，clone 即可用）
│   │   ├── concept-unpacker/            # 把任意概念拆成 9 段式中文学习包
│   │   └── homework-submit/             # 作业提交与推送流程
│   └── memory/                          # 工作日志
├── learning-materials/
│   ├── index.html                       # 概念目录（15 份 Python 概念资料的总入口 + 跨概念联系）
│   ├── python-learning-map.html         # Python 基础学习地图（13 次课 · 零基础版）
│   ├── vars-and-types.html              # 01 变量与数据类型
│   ├── strings.html                     # 02 字符串
│   ├── lists.html                       # 03 列表
│   ├── dicts.html                       # 04 字典
│   ├── conditionals.html                # 05 条件判断
│   ├── loops.html                       # 06 循环
│   ├── functions.html                   # 07 函数
│   ├── comprehensions.html              # 08 推导式与内置函数
│   ├── file-io.html                     # 09 文件读写
│   ├── exceptions.html                  # 10 异常处理与调试
│   ├── regex.html                       # 11 正则表达式
│   ├── modules-and-packages.html        # 12 模块与包
│   ├── numpy.html                       # 13 numpy 数组
│   ├── pandas.html                      # 14 pandas 数据表
│   ├── matplotlib.html                  # 15 matplotlib 绘图
│   ├── agent.html                       # 作业 1 概念资料：Agent
│   ├── llm-context.html                 # 作业 1 概念资料：大模型的上下文
│   ├── skill.html                       # 作业 1 概念资料：Skill
│   └── concept-relationship.html        # 作业 1：三概念关系图
├── assignments/                         # 课程作业
│   ├── scripts/                         # 课堂练习脚本（如 01.ipynb）
│   └── README.md
├── .gitignore
└── README.md                            # 本文件
```

## 仓库级 Skills（随仓库提交，clone 即可用）

本仓库的 Skills 存放在 `.workbuddy/skills/` 下，**作为仓库的一部分提交到 Git**，任何人 clone 后都能直接使用。

| Skill 名 | 路径 | 用途 |
|---|---|---|
| `concept-unpacker` | [`.workbuddy/skills/concept-unpacker/SKILL.md`](https://github.com/Yym113/big-data-ai/blob/main/.workbuddy/skills/concept-unpacker/SKILL.md) | 把任意陌生**概念**拆成 9 段式中文学习包（个人理解 / 学习目标 / 核心问题 / 结构化解释 / 应用场景 / 概念辨析 / 自测问题 / 可核查来源 / 核查记录） |
| `homework-submit` | [`.workbuddy/skills/homework-submit/SKILL.md`](https://github.com/Yym113/big-data-ai/blob/main/.workbuddy/skills/homework-submit/SKILL.md) | 把本地**作业文件**自动提交并推送到本仓库：核对状态 → 文件归位 → git add/commit/push → 回报结果 |

**调用方式**（在 WorkBuddy 对话里说一句话即可）：

- 「用 `concept-unpacker` 帮我学一下 `RAG`」→ 自动生成 `learning-materials/rag.html`，并附核查记录
- 「提交作业」「交作业」「推一下」→ 自动走完提交推送流程，并回报结果

### 为什么是「仓库级」

| 特征 | 说明 |
|---|---|
| 存在位置 | 在仓库目录内（`.workbuddy/skills/`），不是用户级目录 `~/.workbuddy/skills/` |
| 版本管理 | 与代码一起 `git commit`，有完整提交历史，可回溯 |
| 可移植 | 别人 clone 仓库后，skill 随之而来，无需额外安装 |
| 可审查 | 打开 GitHub 即可阅读全文，格式为带 frontmatter 的 `SKILL.md` |

### Skill 的设计要点

**`concept-unpacker`**
- 9 段固定结构，每份资料都包含「可核查参考来源」与「核查记录」两节，明确区分 AI 生成与人工核对的部分
- 参考资料必须先用工具抓取真实页面，禁止凭记忆编造；抓不到的链接不得写入来源表
- **代码示例规范**：代码标识符一律用英文，中文只出现在字符串字面量、注释和正文里

**`homework-submit`**
- 内置本仓库的固定信息（路径、分支、作者），无需每次询问
- **强制回报结果**：即使只有一句「推送成功了」也必须给出，并附 commit 哈希与同步状态
- 安全约束：不用 `mv`（用 `cp` 保留原件）、不执行 `git push -f` / `git reset --hard`、不删除用户文件

## 学习资料

`learning-materials/` 目录下的概念学习资料：

### Python 概念系列（15 份 + 目录页）

从 [`index.html`](https://github.com/Yym113/big-data-ai/blob/main/learning-materials/index.html) 进入 —— 它是总入口，含依赖主线图与 6 组**跨概念联系**。

| 阶段 | 编号与文件 |
|---|---|
| 一 · 语言入门 | `01` vars-and-types · `02` strings · `03` lists · `04` dicts |
| 二 · 组织逻辑 | `05` conditionals · `06` loops · `07` functions · `08` comprehensions · `09` file-io · `10` exceptions |
| 三 · 文本与数据实战 | `11` regex · `12` modules-and-packages · `13` numpy · `14` pandas · `15` matplotlib |

配套 [`python-learning-map.html`](https://github.com/Yym113/big-data-ai/blob/main/learning-materials/python-learning-map.html)：13 次课 × 90 分钟的学习地图（课次与上述编号对应）。

每份遵循统一的 9 段结构：个人理解 / 学习目标 / 核心问题 / 结构化解释 / 应用场景 / 概念辨析 / 自测问题 / 可核查来源 / 核查记录。

### 作业 1 概念资料

| 文件 | 主参考 |
|---|---|
| `agent.html` | ReAct 论文 (arXiv:2210.03629)、Russell & Norvig AIMA、Wikipedia |
| `llm-context.html` | "Lost in the Middle" 论文 (arXiv:2307.03172)、Anthropic 上下文工程博客 |
| `skill.html` | Anthropic Agent Skills 公告 (2025-10-16)、agentskills.io 开放规范 |
| `concept-relationship.html` | 三概念关系（Mermaid 流程图 + 对照表 + 链路例子） |

## 课程作业

按学期累积在 `assignments/` 下，每次作业一个子文件夹：

- `assignments/assignment-1/`（作业 1：用 AI 构建概念学习资料生成 Skill，本仓库的 `learning-materials/` 就是其交付物）

## 学习进度

- [ ] 大数据基础
- [x] Python 编程基础（学习地图 + 15 份概念资料已就绪，待按 13 次课逐节学习）
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
