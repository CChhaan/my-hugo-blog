---
# 文章标题
title: 2. 开始使用 Git
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: Git init, Git add, Git commit, Git log, Git rm, Git mv, Git 暂存区, Git 工作区, Git 存储库, Git 删除文件, Git 重命名文件, Git 提交记录, Git grep, Git since until, Git 命令教程, Git 文件追踪, Git allow-empty, Git 两段式提交
# 发表日期
date: 2025-07-02
summary: 本文主要介绍了 Git 的基本使用方法，包括如何初始化 Git 仓库、如何将文件添加到 Git 仓库、如何提交更改、如何查看提交记录以及如何在 Git 中删除或重命名文件等。通过这些基本操作，读者可以快速上手使用 Git 进行版本控制。
# 分类
categories:
  - Git从入门到精通
# 标签
tags:
  - Git
  - 版本控制系统
---

## 新增、初始 Repository

**`git init`**：在当前目录中创建一个 `.git` 目录，整个 Git 的核心都集中在此目录中。

如果不想让当前目录被 Git 管控，或只想提供不含版控记录的内容，只需移除 `.git` 目录，Git 就会失去对该目录的控制权。

## 把文件交给 git 管控

### 创建文件后交给 git

**`git status`**：查看当前目录状态。

- **untracked files**：文件尚未被加到 Git 版控系统中，只是新加入目录，尚未被追踪。

**`git add [文件名]`**：将文件交给 Git 管控。

- 状态从 _untracked files_ → **new files**。
- 表示该文件已经进入 **暂存区（index）**，稍后可与其他文件一起提交到存储库。

使用万用字元：

```bash
git add *.html
```

把所有后缀名是.html 的文件全部加到暂存区。

加入所有文件：

```bash
git add --all
```

### `--all` 与 `.` 的区别

**`git add .`**：将当前目录及其子目录中的修改加入暂存区，不包含该目录以外的内容。

**`git add --all`**：不论在哪一层目录执行，都会将整个项目的所有修改加入暂存区。

### 提交暂存区内容到存储库

**`git commit -m "xxx"`**：将暂存区的内容永久保存到存储库。

`-m "xxx"` 用于说明此次提交的内容。可以使用中英文，只要简单、清晰即可。说明的重点是 **让自己和别人都能快速理解本次改动**。

完成 `commit` 才算完成整个流程。

`git commit` **只会处理暂存区的内容**。尚未 `git add` 到暂存区的文件 **不会被提交**。

提交说明是必需的，否则提交不会完成。若未指定 `-m` 参数，Git 会打开默认编辑器（通常是 **vim**）以填写提交信息。

使用 `--allow-empty` 参数可以创建 **没有内容变更** 的提交：

```bash
git commit --allow-empty -m ""
```

## 工作区、暂存区与存储库

### 三个主要区域

- **工作目录 → 暂存区**：`git add`
- **暂存区 → 存储库**：`git commit`

**注意**：执行 `commit` 才算完成整个流程。

### 是否一定要二段式

使用 `-a` 参数可省略 `git add`

```bash
git commit -a -m "xxx"
```

`-a` 参数只对 **已存在于存储库的文件** 有效，对新加入的 **untracked files** 无效。

## 查看记录

### 查看记录方法

**`git log`**：查看历史记录，越新的信息越靠上。

可看到：

- **作者**
- **提交时间**
- **提交说明**

SHA-1 算法生成的长文本：作为 **commit 的唯一识别码**，可视为 **身份证号**。

参数：`--oneline`、`--graph`：输出更简洁，一次可看到更多 commit。

### 常见问题与查询方式

- 查询某个人的 commit：

```bash
git log --oneline --author="Amy"
```

- 查询多个人的 commit（`|` 表示或，需加 `\`）：

```bash
git log --oneline --author="Amy\|Eddie"
```

- 查询 commit 信息是否包含某关键字：

```bash
git log --oneline --grep="LoL"
```

- 在文件内容中搜索特定关键字：

```bash
git log -S "Ruby"
```

- 查询某一时间段内的 commit：

在查看历史记录时，可以搭配--since、--until 和--after 参数查询

```bash
git log --oneline --since="9am" --until="12am" --after="2017-01"
```

这样就可以找到“从 2017 年 1 月之后，每天早上 9 点到 12 点之间的 Commit”

## 在 git 中删除或变更文件名

在 git 中，无论是删除文件还是变更文件名，对 git 来说都是一种“改动”

### 删除文件

**直接删除**：使用 `rm` 或文件管理器删除，状态为 **deleted**，需加入暂存区确认。

**Git 删除**：先 `rm` 再 `git add`，也可直接使用 **`git rm`**（文件直接进入暂存区）。

**仅移除管控，不删除文件**

- **`git rm --cached`**：文件从 Git 管控移除，状态由 **tracked → untracked**，文件仍保留在工作目录中。

### 变更文件名

**直接改名**

- Git 识别为两个动作：删除旧文件 + 新增新文件（untracked）。
- 使用 `git add` 加入暂存区，状态显示为 **renamed**。

请 git 帮忙改名

```bash
git mv old.html new.html
```

### 文件名的重要性

- Git 通过 **文件内容** 计算 SHA-1 值，**文件名不重要**。
- 更改文件名不会生成新的 **Blob 对象**，但会生成新的 **Tree 对象**。
