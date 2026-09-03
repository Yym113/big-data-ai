# Skill Creator 文档摘要

> 来源：WorkBuddy Skill Creator 官方 SKILL.md（本地路径：~/.workbuddy/plugins/cache/workbuddy-builtin/skill-skill-creator/0.1.0/SKILL.md）

## 什么是 Skill

Skill 是模块化的自包含包，通过提供专业知识、工作流和工具来扩展 Agent 的能力。它把通用 Agent 变成某个领域的“专家”。

## Skill 提供什么

1. 专业化工作流
2. 工具集成说明
3. 领域专业知识
4. 可复用资源（脚本、参考资料、资源文件）

## Skill 的目录结构

```
skill-name/
├── SKILL.md              # 必需。YAML frontmatter + Markdown 说明
├── scripts/              # 可选。可执行脚本
├── references/           # 可选。参考资料
└── assets/               # 可选。模板、图片等输出资源
```

## SKILL.md 的必需内容

- YAML frontmetadata 至少包含 `name` 和 `description`。
- `description` 决定 Agent 何时加载该 skill。
- 由 Agent 创建的技能必须包含 `agent_created: true`。

## 三级加载

1. **Metadata**：name + description，常驻上下文。
2. **SKILL.md body**：skill 触发时加载。
3. **Bundled resources**：Agent 按需读取。

## 两种作用范围

| 类型 | 路径 | 作用范围 |
|---|---|---|
| 用户级 skill | ~/.workbuddy/skills/skill-name/ | 跨所有项目可用 |
| 项目级 skill | .workbuddy/skills/skill-name/ | 随仓库共享给协作者 |
