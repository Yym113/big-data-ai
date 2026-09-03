---
name: agent-skill-in-one-minute
description: |
  当用户想学习 Agent Skill、询问“Skill 是什么”、要求“一分钟学会 Agent Skill”、
  或需要生成/查看 Agent Skill 的一分钟速成学习页时触发。
  使用本 skill 目录下的 assets/agent-skill-in-one-minute.html 作为可视化学习材料。
agent_created: true
---

# Agent Skill · 一分钟速成

## 目标

帮助学习者在 1 分钟内理解 Agent Skill 的核心概念，并通过分层测试即时检验掌握程度。

## 核心结论（一句话版）

Skill 是**给 Agent 看的任务说明书**，它让通用 Agent 变成某个领域的“专家”。

## 必须讲清楚的三个点

1. **Skill 是一个目录**
   - 目录里必须包含 `SKILL.md`。
   - 可选 `scripts/`、`references/`、`assets/`。
   - 不要把它当成单文件或插件程序。

2. **`SKILL.md` 决定触发时机**
   - YAML frontmatter 里的 `name` 和 `description` 是触发器。
   - 当用户请求匹配 description 描述的场景时，Agent 才会加载该 skill。

3. **三级加载机制**
   - 元数据（name + description）：常驻上下文。
   - `SKILL.md` 正文：触发时加载。
   - `scripts/`、`references/`、`assets/`：按需加载。

## 输出方式

- 若用户需要可视化学习页：提供 `assets/agent-skill-in-one-minute.html`。
- 若用户只需要口头讲解：按“核心结论 → 三个点 → 目录结构”顺序讲解。
- 若用户需要测试：引导其打开 HTML 中的分层测试区域。

## 知识来源

- WorkBuddy Skill Creator 官方文档：https://www.workbuddy.cn/docs/workbuddy/Skills
- 详细摘要见本目录 `references/skill-creator-summary.md`。
