---
# 文章标题
title: 3. commit相关
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: Git amend, Git rebase, Git reset, Git .gitignore, Git clean, Git blame, Git checkout, Git reflog, Git commit 修改, Git 恢复文件, Git 恢复删除文件, Git 追加文件, Git 空目录, Git keep 文件, Git reset hard soft mixed, Git 查看提交记录, Git 部分提交, Git add -p, Git 撤销 commit
# 发表日期
date: 2025-07-03
summary: 本文主要介绍了 Git 中 commit 相关的操作，包括修改 commit 记录、追加文件到最近一次 commit、新增目录、忽略文件、查看特定文件的 commit 记录、挽救删除的文件或目录、撤销最近一次 commit 等内容。
# 分类
categories:
  - Git从入门到精通
# 标签
tags:
  - Git
  - 版本控制系统
---

## 修改 commit 记录

### 修改方式

- 删除整个 `.git` 目录
- 使用 `git rebase` 删除并整理后重新 commit
- 使用 `git reset` 删除并整理后重新 commit
- 使用 `--amend` 改动最后一次的 commit

### 使用 --amend 参数修改最后一次 commit

在 commit 命令后加 `--amend` 即可

如果没有加 `-m`，会弹出 vim 编辑器编辑信息

虽然只是修改 commit 信息，但 git 会认为内容改变，重新生成新的 commit 对象（一次全新的 commit）

### 修改更早的 commit

使用 `git rebase`

**注意**：不要在已经 push 的 commit 上改动，否则会造成困扰

## 追加文件到最近一次 commit

采用下面两种方式：

- 使用 `git reset` 删除最近一次 commit，加入新文件后重新 commit
- 使用 `--amend`

### 操作流程

1. `git add` 把文件加到暂存区
2. `git commit --amend`
   - 可加 `--no-edit` 避免编辑信息

```bash
git commit --amend --no-edit
```

**注意**：尽量不要在已 push 的 commit 上执行

## 新增目录

Git 根据文件内容计算对象，空目录无法提交

解决方法：在空目录中放置一个文件（如 `.keep` 或 `.gitkeep`）

然后按正常流程 `add` 和 `commit`

## 忽略文件

### 使用 .gitignore

在项目目录新增 `.gitignore` 文件并设置规则

即使 `.gitignore` 未 commit/push 也有效，但建议提交共享

规则只对之后新增的文件有效，已存在的文件无效

若需让已存在的文件生效：

```bash
git rm --cached 文件名
```

### 忽略忽略

在 `git add` 时加 `-f` 参数可忽略 `.gitignore` 规则

```bash
git add -f 文件名称
```

### 清除忽略的文件

使用 `git clean -fX`

- `-f`：强制删除
- `-X`：删除被忽略的文件

## 查看特定文件的 commit 记录

查看单一文件的历史

```bash
git log index.html
```

查看改动内容

```bash
git log -p index.html
```

`+` 表示新增，`-` 表示删除

## 查看某行代码是谁写的

使用 `git blame`

显示每行代码的提交者和提交信息

可加 `-L` 参数指定范围

```bash
git blame -L 5,10 index.html
```

## 挽救删除的文件或目录

### 恢复操作

单一文件：

```bash
git checkout index.html
```

所有文件：

```bash
git checkout .
```

**说明**：可恢复修改或删除的文件，但若 `.git` 目录被删除，则无法恢复。

### 原理

`git checkout` 接分支名时切换分支

接文件名时，会从 `.git` 复制文件到工作目录

会用暂存区的文件覆盖工作目录文件

```bash
git checkout HEAD~2 welcome.html
```

用 2 次前的版本覆盖 `welcome.html`，更新暂存区状态

工作目录的 `welcome.html` 会被旧版本覆盖，且暂存区中该文件的状态会直接变为 “与 `HEAD~2` 版本一致”，**其他文件的暂存状态不受影响**

## 撤销最近一次 commit

### reset 操作

相对写法：

```bash
git reset e12d8ef^
```

符号"^"代表的是前一次。如果是 e12d8ef^^则是往前两次，以此类推。如果要倒退 5 次写成 e12d8ef~5

head 与 master 都是指向当前 commit，所以上面这行通常改写成

```bash
git reset Head^
git reset main^
```

这两个命令会得到一样的结果。

绝对写法：

```bash
git reset 85e7e30
```

### reset 模式

**mixed（默认）**：清除暂存区，不影响工作目录

**soft**：仅移动 Head，文件保留在暂存区

**hard**：清除工作目录和暂存区文件

## reset 后还能恢复吗？

reset 不会删除 commit

可通过 reset 回到原 commit 的 SHA-1

若未记录 SHA-1，可使用 `git reflog`

`git log -g` 也可查看 reflog

## 部分提交文件内容

使用 `git add -p` 进入交互模式

选项：

- `y`：提交整个区域
- `e`：编辑具体提交的区域
