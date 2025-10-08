---
# 文章标题
title: 10. 使用github
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: Git 推送 GitHub, git push -u origin main, git remote add origin, GitHub 上游分支 upstream, git fetch, git pull, git clone, Pull Request 教程, fork 同步上游, 删除远端分支, git push -f 强制推送, GitHub Pages 部署, 免费个人网站, git format-patch, git am, Git 协作开发, Git 多人协作流程
# 发表日期
date: 2025-07-10
summary: 本文主要介绍了如何使用 GitHub 进行版本控制，包括如何将本地内容推送到 GitHub 上、如何从 GitHub 上拉取更新、如何强制推送以及如何从服务器获取项目等操作。
# 分类
categories:
  - Git从入门到精通
# 标签
tags:
  - Git
  - 版本控制系统
---

## 把内容推送到 GitHub 上

GitHub 是全球最大的 **git 服务器**。

**git 是工具**，**GitHub 是网站**，其本质是一个 git 服务器。

### 设置远端节点

```bash
git remote add origin xxx.git
```

`git remote`：进行与远端有关的操作。

`add`：加入一个远端节点。

`origin`：指向远端 GitHub 服务器的位置，是 **默认代名词**。

从服务器 `clone` 下来的项目默认远端名就是 **origin**，但该名称可以修改。

### 推送内容到远端

```bash
git push -u origin main
```

该命令完成以下操作：

1. 将 **main 分支内容推送到 origin**。
2. 若远端不存在 main 分支，则 **创建一个名为 main 的分支**。
3. 若存在，则 **移动远端 main 分支到最新进度**。
4. `-u` 参数：设置 **upstream**。

### upstream（上游分支）

upstream 翻译成中文意思是上游，其实就是另一个分支的名称

每个分支最多可设置一个上游（upstream）。

upstream 可追踪远端分支，也可指向本地分支。

若设置了 upstream，之后执行 `git push` 可 **自动推送到默认目标**。

若未设置，则需 **每次明确指定分支与目标**。

### 修改远端分支名称

```bash
git push -u origin main:main
```

与上方命令效果相同。

若希望远端分支名称不同，可修改为：

```bash
git push -u origin main:cat
```

此时会在远端创建名为 **cat** 的分支。

## 拉取更新（pull）

### fetch 指令

执行 fetch 指令

```bash
git fetch
```

执行后：

- Git 会拉取远端更新，并同步到本地的 **origin/** 分支。
- 远端分支命名如：`origin/HEAD`、`origin/main`。
- 因使用过 `-u` 参数，`origin/main` 即为本地 `main` 的 upstream。
- fetch 后若远端有新内容，会更新本地对应的 `origin` 分支。
- 接下来可执行 **merge** 合并更新。

### pull 指令

git pull = git fetch+git merge

```bash
git pull -rebase
```

`pull` 会拉取远端内容并更新本地进度。

使用 `-rebase` 参数时，fetch 后采用 **rebase** 方式合并。

在多人协作时，`rebase` 可避免多余的合并 commit。

## 推不上去的原因

当 **远端内容比本地新** 时，`push` 会失败。多出现在多人协作的情况。

解决方式：

1. **先拉再推**：更新本地内容后再推送。
2. **强制推送**：使用 `--force` 或 `-f` 参数强制覆盖。

## 从服务器获取项目

```bash
git clone xxx.git 目录名称
```

说明：

- 将整个项目复制到本地（包括历史记录、分支、标签等）。
- 若省略目录名，则使用项目原名。

### clone 与 pull 的区别

**clone**：第一次下载项目。

**pull/fetch**：更新已有项目。

> clone 通常只在首次使用，之后更新需使用 pull 或 fetch。

## 使用 Pull Request (PR)

步骤：

1. Fork 原作者项目到自己账号下。
2. 在自己账号中修改内容。
3. Push 到自己的仓库。
4. 发送 PR 通知原作者，请其审查并合并。

> PR（Pull Request）即 “请求原作者拉取你的更新”。

fork：原作者做的不够好，其他人觉得可以做的更好，或者想加入一些个人喜欢的功能而修改出另外的版本。

### 企业内部协作流程

- 企业项目可采用 PR 模式开发。
- 每位开发者 Fork 公司项目到个人账户。
- 功能完成后发送 PR。
- 管理者 Code Review 后合并。
- 保证正式分支（如 master、production）稳定可上线。

## 跟上 fork 源项目进度

方法一：砍掉重练

- 删除 fork 项目后重新 fork。
- 简单、直接、可确保为最新版本。

方法二：跟上游同步

1. **设置原作者项目为上游节点**。
   使用 `git remote -v` 查看详细信息。
2. **抓取上游最新内容**：
   使用 `fetch` 更新并手动合并。
3. **推回自己项目**：
   保持本地与 GitHub fork 项目同步更新。

## 删除远端分支

使用 `push` 指令并在分支名前加冒号。

等同于推送空内容更新，**变相删除远端分支**。

```bash
git push origin :cat
```

## 强制推送（git push -f）

这个指令可 **无视版本先后顺序**，直接覆盖远端。

使用场景：

**整理历史记录**：使用 `rebase` 后因历史被修改无法正常推送时。

**仅用于自己分支**：不影响他人，只强制更新个人分支。

```bash
git push -f origin 我的分支
```

若误覆盖，只要保有旧进度，可再执行 `git push -f` 恢复。

## 使用 GitHub 免费制作个人网站

当推送的分支名为 **gh-pages** 时，GitHub 可作为静态网站服务器。

限制：

- 仅支持静态页面。
- 不支持 `.htaccess` 或用户密码设置。
- 只能使用 git 上传。
- 所有 GitHub Pages 内容均为公开。

使用方法：

1. 在 GitHub 上创建新项目。
2. 在描述（Description）中填写 `username.github.io`。
3. 执行 `git add`、`git commit`、`git push`。
4. 推送后访问 `username.github.io` 即可查看页面。

自定义域名：

- 在项目根目录创建名为 `CNAME` 的文件，内容为目标网址。
- 管理网域时设置一组 CNAME 指向 `username.github.io`。

## 不使用 github

生成更新文件

```bash
git format-patch SHA-1(1)...SHA-1(N)
```

生成从 `SHA-1(1)`（不含）到 `SHA-1(N)` 的更新文件。

套用更新文件

```bash
git am 更新文件
```

可一次套用一个或多个更新文件。

Git 会依序将这些更新应用到当前项目中。
