---
# 文章标题
title: 11. git flow
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: Git Flow, Git 分支模型, master 分支, develop 分支, feature 分支, hotfix 分支, release 分支, 分支职责, Git 分支管理, Git 版本控制, 稳定版本, 功能开发, 紧急修复, 上线测试, 分支合并策略
# 发表日期
date: 2025-07-11
summary: 本文主要介绍了 Git Flow 分支模型，包括 master 分支、develop 分支、feature 分支、hotfix 分支和 release 分支的职责和层级关系，以及分支合并策略。
# 分类
categories:
  - Git从入门到精通
# 标签
tags:
  - Git
  - 版本控制系统
---

根据 **Git Flow** 的建议，分支主要分为以下几类：

- **master 分支**
- **develop 分支**
- **hotfix 分支**
- **release 分支**
- **feature 分支**

其中：

- **master** 和 **develop** 被称为 **长期分支**，因为它们会一直存在于整个 Git Flow 生命周期中。
- 其他分支（如 hotfix、release、feature）属于 **临时分支**，会在任务完成后被删除。

## 各分支职责

master 分支

- 用于存放 **稳定、可随时上线的项目版本**。
- **来源**：只能从其他分支合并，开发者不会直接在 master 上 commit。
- **特征**：每个稳定版本的 commit 通常会打上 **版本号标签（tag）**。

develop 分支

- 是 **所有开发分支的基础分支**。
- 新增功能时，所有的 **feature 分支** 都从 develop 分支划出。
- 当 feature 分支的功能完成后，会被 **合并回 develop 分支**。

hotfix 分支

- 当 **线上产品出现紧急问题** 时，从 **master 分支** 划出一个 hotfix 分支进行修复。
- 修复完成后：
  - **合并回 master 分支**（发布修复版本）。
  - **同时合并一份到 develop 分支**。

合并到 develop 的原因

> 如果不这样做，当 develop 分支未来合并回 master 时，之前修复过的问题会再次出现。

不从 develop 分支划出的原因

> 因为 develop 分支的功能可能尚未完成，若从中直接切出修复分支再合并回 master，反而可能造成更大的问题。

release 分支

- 当 **develop 分支** 的代码足够成熟时，将其合并到 **release 分支**，进行上线前的 **最终测试**。
- 测试完成后：
  - **合并到 master 分支**（正式上线版本）。
  - **同时合并回 develop 分支**。

合并回 develop 的原因

> 在 release 阶段可能会发现并修正问题，需同步回 develop，避免未来版本再次出现同样的错误。

feature 分支

- 用于 **新增功能的开发**。
- 所有 feature 分支都从 **develop 分支** 划出。
- 功能开发完成后，**合并回 develop 分支**。

## 层级关系

```
master ← release ← develop ← feature
     ↑          ↑
     └── hotfix ┘
```
