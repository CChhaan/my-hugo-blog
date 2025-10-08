---
# 文章标题
title: 9. git其他知识
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: Git stash, git filter-branch, 删除敏感信息, Git cherry-pick, git gc, Git prune, Git 资源回收机制, dangling 对象, unreachable 对象, detached HEAD, 断头状态, Git 暂存修改, Git 清理历史, Git 删除文件, git push -f, Git 恢复误删文件, Git 优化仓库, Git 清理命令
# 发表日期
date: 2025-07-09
summary: 本文主要介绍了 Git 的其他知识，包括如何暂存修改、删除敏感信息、将其他分支的 commit 捡过来合并、真正从 git 中移除文件、git 资源回收机制等内容。
# 分类
categories:
  - Git从入门到精通
# 标签
tags:
  - Git
  - 版本控制系统
---

## 手边的工作做到一半，临时要切换到别的任务

### 简单做法

1. **先保存当前所有修改**。
2. 切换到有问题的分支进行修复。
3. 修复完成后切换回原分支。
4. 执行 `reset` 命令，衔接上已完成的部分。
5. 继续之前的工作。

### 使用 stash

使用 `git stash` 将修改暂存。

- **注意**：`untracked` 状态的文件默认无法被 stash，需要使用 `-u` 参数。

使用 `git stash list` 查看当前状态栈。

- 最前面的 `stash@{0}` 表示最新的 stash。
- `WIP` 表示 “work in progress”（工作进行中）。

取回暂存内容

```bash
git stash pop stash@{0}
```

`pop` 会将指定的 stash 应用到当前分支上，并 **自动删除** 它。

若未指定，默认取出 `stash@{0}`（最后保存的那次）。

删除指定的 stash。

```bash
git stash drop stash@{0}
```

不删除地取回

```bash
git stash apply stash@{0}
```

将指定的 stash 套用到当前分支上，但 **不会被删除**。

可理解为：`pop = apply + drop`。

## 不小心把账号密码放进 git，想删掉

### 砍断重练法：

1. 删除 `.git` 目录。
2. 删除密码文件。
3. 重新 `commit`。

**优点**：简单直接。
**缺点**：所有历史记录都会消失，仅适合个人项目。

### 使用 `filter-branch`

可一次性从每个 commit 中移除文件。

```bash
git filter-branch --tree-filter "操作"
```

#### 说明

- `filter-branch` 会逐个处理 commit。
- `--tree-filter` 会在每个 commit 被 checkout 后执行指定操作，再重新 commit。
- 删除文件后，后续 commit 会重新计算，产生新的历史记录。

### 恢复到执行前状态

执行 `filter-branch` 时，git 会将原状态备份到.git/refs/original/refs/heads 目录中，可以通过该目录找出 `SHA-1`，再执行：

```bash
git reset refs/original/refs/heads/master --hard
```

即可回到执行前状态。

### 如果已经推出去了

执行：

```bash
git push -f
```

强制推送修改后的历史。

## 将其他分支的 commit 捡过来合并

使用 `cherry-pick`：

```bash
git cherry-pick SHA-1(1) SHA-1(2) ...
```

会将指定 commit 的内容复制过来，而非剪切粘贴。原分支的 commit 保留原位。

因为要接到当前分支上，会重新计算生成新的 commit。

若使用 `--no-commit` 参数，则捡过来的内容仅放入暂存区，不会立即生成 commit。

## 真正从 git 中移除文件

使用 `filter-branch` 可批量移除文件：

```bash
git filter-branch --tree-filter "rm -f 文件名"
```

#### 清理步骤

1. 删除备份引用：

```bash
rm .git/refs/original/refs/heads/master
```

2. 让 reflog 立即过期：

```bash
git reflog expire -all --expire=now
```

3. 检查不可达对象：

```bash
git fsck --unreachable
```

4. 启动资源回收：

```bash
git gc --prune=now
```

若内容已推送到远端，需执行：

```bash
git push -f
```

覆盖在线记录。

## git 资源回收机制

### 工作原理

- 每次将文件加入暂存区时，git 会生成 **blob 对象**。
- 每次 `commit` 时，生成对应的 **tree 对象** 与 **commit 对象**。
- 当对象数量达到一定量时，git 会自动触发 **资源回收机制**，清理不可达对象（`unreachable`），以缩小仓库体积并提高效率。

### 手动触发资源回收

1. 让 reflog 立即过期：

```bash
git reflog expire -all --expire=now
```

2. 启动回收：

```bash
git gc
```

git gc 指令会呼叫 git prune 指令来清除处于 unreachable 状态的对象，但 git prune 指令也要设置到期日。

```bash
git prune --expire=now
```

可以简写

```bash
git gc --prune=now
```

### 怎样产生边缘对象

- 在 commit 前犹豫不决

执行 `git add` 后会生成 blob 对象。

若再次修改文件并重新 `add`，旧的 blob 对象会变为 **unreachable**。

使用 `git commit --amend` 也会生成新的 unreachable 对象。

- 被删除的 tag 对象

使用 `git tag -d` 删除标签后，该 tag 对象无引用，立即变成 **unreachable**。

- 执行 rebase 时

rebase 会复制 commit 并重新计算，原 commit 成为 **unreachable**。

### dangling 与 unreachable

执行 `git fsck` 时可能看到 `dangling`：

- **unreachable 对象**：没有任何对象或指示标指向它，但可以指向其他对象。

- dangling 对象：无引用，也不指向其他对象，完全悬空。属于 unreachable 的子集。

**dangling 对象** 也会在 `gc` 时被清理。

## 断头状态（detached HEAD）

`HEAD`：指向当前分支的指示标。

**正常状态**：`HEAD → 分支 → commit`。

**断头状态**：`HEAD` 未指向任何分支。

可能出现的原因：

- 使用 `checkout` 直接跳到某个无分支指向的 commit。
- `rebase` 过程中会持续处于 detached 状态。
- 切换到远端分支时。

影响：

- 仍可操作或 commit。
- 若不记录 commit 的 `SHA-1`，离开分支后该 commit 难以再找到。
- 未被引用的 commit 会在回收机制中被清除。

### 保留当前 commit

创建分支指向当前 commit：

```bash
git branch 分支名
```

或指定 commit 创建分支：

```bash
git branch 分支名 SHA-1
```

或创建并切换到新分支：

```bash
git branch -b 分支名 SHA-1
```

### 切换远端分支的情况

- 使用 `--remote` 或 `-r` 可查看远端分支。
- 切换到远端分支时也会成为 detached 状态。
- 使用 `--track` 或 `-t` 参数可避免进入 detached 状态。

脱离 detached 状态：只需让 `HEAD` 指向任何本地分支即可。
