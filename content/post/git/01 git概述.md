---
# 文章标题
title: 1. git概述
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: Git 教程, Git 基础, Git 命令, Git 配置, Git 优点, Git 分布式版本控制, 终端命令, Linux 命令行, macOS 终端, Windows CMD, vim 编辑器, Git 用户设置, Git 别名 alias, Git global local, Git 快照, Git 入门
# 发表日期
date: 2025-07-01
summary: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 分类
categories:
  - Git从入门到精通
# 标签
tags:
  - Git
  - 版本控制系统
---

## git 概述

**Git**：一种 **分布式版本控制系统**。

### git 的优点

**免费开源**

**速度快、文件体积小**

- 其他版本控制系统：记录的是各版本之间的差异。
- Git：记录的是 **文本内容的快照**，可快速切换版本。

**分布式系统**

- 即使没有服务器或网络，也可以使用 Git 进行版本控制。
- 待服务器恢复或网络可用时再进行同步，不受影响。

## 终端机/命令提示符

### 常用命令

| Windows | macOS/Linux | 说明         |
| ------- | ----------- | ------------ |
| cd      | cd          | 切换目录     |
| cd      | pwd         | 获取当前位置 |
| dir     | ls          | 列出文件列表 |
| mkdir   | mkdir       | 创建目录     |
| 无      | touch       | 创建文件     |
| copy    | cp          | 复制文件     |
| move    | mv          | 移动文件     |
| del     | rm          | 删除文件     |
| cls     | clear       | 清屏         |

### 目录切换及显示

```bash
# 切换到 /tmp 目录（绝对路径）
cd /tmp

# 切换到 my_project 目录（相对路径）
cd my_project

# 切换到上一层目录
cd ..

# 切换到 home/project/namecards 目录
cd ~/project/namecards/

# 显示当前所在目录
pwd
```

### 文件列表

`ls`：列出当前目录下文件及目录。

`ls -al`：显示包含以`.`开头的文件，及完整权限、所有者、时间信息。

```bash
ls -al
```

### 创建文件、目录

```bash
# 创建文件
touch index.html

# 创建目录
mkdir demo
```

`touch`：

- 不存在 → 创建空白文件。
- 已存在 → 修改最后修改时间，不改动内容。

`mkdir`：创建目录。

### 文件操作

```bash
# 复制
cp index.html about.html

# 重命名 / 移动
mv index.html info.html

# 删除文件
rm index.html

# 删除目录下所有 .html 文件
rm *.html
```

## vim 操作介绍

**模式切换**：

- **Normal 模式**：命令模式，无法输入文本。
- **Insert 模式**：文本输入模式。

**进入 Insert 模式**：

- `i` → insert
- `a` → append
- `o` → 新建一行并输入

**切换模式**：

- Insert → Normal：`Esc` 或 `Ctrl + [`

**常用命令**：

- `:w` → 存储文件
- `:q` → 关闭文件（未存储会提示先保存）
- `:wq` → 存储并关闭文件

## 设置 Git

### 用户设置

```bash
git config --global user.name "Allay"
git config --global user.email "allay@qq.com"
```

检查配置：

```bash
git config --list
```

配置保存在 `~/.gitconfig` 文件中，可手动修改。

### 每个项目设置不同的作者

针对特定的项目设置不同的作者，可以用--local 参数

```bash
git config --local user.name "Andy"
git config --local user.email "andy@qq.com"
```

**local 设置**：仅对该项目生效。

其他项目仍使用 **global 设置**。

### 设置缩写

```bash
git config --global alias.co checkout
git config --global alias.l "log --oneline --graph"
```

示例：

- `git co` = `git checkout`
- `git l` = `git log --oneline --graph`

这些 alias 配置可在 `~/.gitconfig` 中修改。
