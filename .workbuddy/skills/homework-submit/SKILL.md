---
name: homework-submit
description: 把本地作业文件提交并推送到 GitHub 仓库 Yym113/big-data-ai。当用户说「提交作业」「推一下」「交作业」「push 作业」「把 XX 交上去」时使用。自动完成：核对仓库状态 → 归位文件到 assignments/ → git add/commit/push → 回报结果。适用于大数据与人工智能课程的每次作业提交。
agent_created: true
---

# homework-submit（作业提交）

大数据与人工智能课程作业的**提交与推送**流程。

## 固定信息（不要问用户，直接用）

| 项 | 值 |
|---|---|
| 本地仓库 | `C:\Users\lenovo-mr\big-data-ai` |
| 远端仓库 | `git@github.com:Yym113/big-data-ai.git` |
| 分支 | `main` |
| 作业目录 | `assignments/` |
| 脚本目录 | `assignments/scripts/` |
| 作者 | Yym113 / jz3681@qq.com |
| Python | `C:\Users\lenovo-mr\AppData\Local\Programs\Python\Python312\python.exe`（3.12.10） |

## ⚠️ 首要规则：先检查，别乱建

**动手前必须先确认文件在哪。**

- 用户的练习代码**经常写错位置**：
  - ❌ `C:\Users\lenovo-mr\.workbuddy\scripts\`（WorkBuddy 工具目录，会被 gitignore 忽略）
  - ❌ `E:\wookbuddy\<session>\`（会话临时目录）
  - ✅ `C:\Users\lenovo-mr\big-data-ai\assignments\scripts\`（正确位置）
- **不要在 `E:\` 下另建同名项目**——用户的正式仓库只有一个：`C:\Users\lenovo-mr\big-data-ai`
- 找不到文件时，先搜：
  ```bash
  /usr/bin/find "C:/Users/lenovo-mr" -maxdepth 4 -name "*.py" -newer /tmp/ref 2>/dev/null
  ```

## 工作流（按顺序，不可跳步）

### 1. 检查仓库状态

```bash
cd "C:/Users/lenovo-mr/big-data-ai" && git status --short && git remote -v && git branch --show-current
```

确认：
- 远端是 `git@github.com:Yym113/big-data-ai.git`
- 分支是 `main`
- 有哪些改动待提交

### 2. 文件归位

如果用户的新文件不在 `assignments/scripts/`，先复制过去：

```bash
/usr/bin/mkdir -p "C:/Users/lenovo-mr/big-data-ai/assignments/scripts"
/usr/bin/cp "<源文件>" "C:/Users/lenovo-mr/big-data-ai/assignments/scripts/"
```

**🔴 复制用 `cp`，不要用 `mv`**——保留原文件，等用户确认后再清理。

### 3. 预处理 `.ipynb`（重要）

VS Code 打开笔记本时会自动改写 `execution_count`，造成无意义的 diff。

**提交前检查**：
```bash
git diff --stat
```

若只有 `execution_count` 变化（无实质内容改动），**直接提交即可**，不必纠结。

**若 `.ipynb` 从未运行过**（无 outputs），提醒用户先在 VS Code 里跑一遍再提交——**老师要看运行成功的证据**。

### 4. 提交

```bash
cd "C:/Users/lenovo-mr/big-data-ai"
git add -A
git commit -m "<有意义的提交信息>"
```

**提交信息规范**（中文，写清楚做了什么）：

| 场景 | 格式 | 示例 |
|---|---|---|
| 新增作业 | `feat(assignments): 新增 <日期> 课堂练习` | `feat(assignments): 新增 0917 课堂练习脚本` |
| 运行结果 | `feat(assignments): <文件名> 运行成功，记录输出` | `feat(assignments): 01.ipynb 运行成功，记录输出` |
| 笔记文档 | `docs(assignments): 新增 <主题> 笔记` | `docs(assignments): 新增 Python 基础笔记` |

### 5. 推送

```bash
cd "C:/Users/lenovo-mr/big-data-ai" && git push origin main
```

**必须用 `dangerouslyDisableSandbox: true`**——SSH 推送需要网络，沙盒会拦截。

超时给 **120000ms**（国内网络慢）。

### 6. 验证并回报（🔴 不可省略）

```bash
cd "C:/Users/lenovo-mr/big-data-ai"
git status -sb
git log --oneline -3
git ls-remote origin main
```

**必须向用户报告**：
- ✅ 推送成功/失败
- 提交哈希
- 本地与远端是否同步（`## main...origin/main` 无箭头 = 同步）
- GitHub 链接：`https://github.com/Yym113/big-data-ai`

**哪怕只有一句「推送成功了」也必须有**——用户看不懂技术细节，不给结论他会慌。

## 环境坑（这台机器上，必读）

### Bash 工具丢 PATH
```bash
# ❌ 报 command not found
ls / find / mkdir / rm / cp / head / grep / sed

# ✅ 用绝对路径
/usr/bin/ls  /usr/bin/find  /usr/bin/mkdir  /usr/bin/rm  /usr/bin/cp  /usr/bin/head
```

### PowerShell 工具无输出
此环境下 PowerShell 不返回 stdout → **改用 Bash + 绝对路径**。

### pip 装包必须加 `--user`
不加会被沙盒「批量删除保护」拦截（pip 替换旧文件被误判）：
```bash
"<python.exe>" -m pip install --user --no-cache-dir <包> -i https://mirrors.aliyun.com/pypi/simple/
```

### 反斜杠路径
多层 shell 里反斜杠会被吃掉 → **写 `.py` 脚本文件执行**，别用 `python -c`。

## 自检清单（完成前逐条核对）

- [ ] 远端确认是 `Yym113/big-data-ai`
- [ ] 文件在 `assignments/` 下，不在 `.workbuddy/` 里
- [ ] `.ipynb` 有运行输出（老师要看的证据）
- [ ] commit 信息写清做了什么
- [ ] push 成功（`git ls-remote` 返回新哈希）
- [ ] **已向用户明确报告结果**

## 不做的事

- ❌ 不在 `E:\` 或其他地方新建项目（只用 `C:\Users\lenovo-mr\big-data-ai`）
- ❌ 不删除用户文件（除非用户明确指定且已列出清单确认）
- ❌ 不用 `mv` 移动文件（用 `cp`，保留原件）
- ❌ 不执行 `git push -f` / `git reset --hard`（历史已推送，禁止改写）
- ❌ 不跳过 `git add -A` 的确认（提交前先 `git status --short` 看清单）
