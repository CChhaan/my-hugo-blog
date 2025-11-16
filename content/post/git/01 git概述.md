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

**Git**：一种 **分布式版本控制系统**，用于记录文件变化、追踪项目历史。

### 版本控制的意义

- 能查看任意时间点的文件内容。
- 能比较不同版本间的差异。
- 能在误操作后恢复旧版本。
- 方便多人协作，避免文件混乱。

### Git 的优势

**免费开源**

**速度快、文件体积小**

- 传统版本控制系统：记录各版本间的差异。
- Git：记录的是 **文件内容的快照**，因此切换版本极快。

**分布式系统**

- 每个人的本地仓库都包含完整历史记录。
- 即使没有服务器或网络，也能正常进行版本控制。
- 网络恢复后可再同步，不受外部影响。

**与集中式系统的对比（如 SVN）**

| 对比点   | Git（分布式）    | SVN（集中式）          |
| -------- | ---------------- | ---------------------- |
| 工作方式 | 每人拥有完整仓库 | 所有操作依赖中央服务器 |
| 离线操作 | ✅ 可离线提交     | ❌ 必须联网             |
| 速度     | 快，读取本地数据 | 慢，需网络交互         |
| 结构     | 多中心           | 单一中心               |

## 命令行（终端 / 命令提示符）

### 常用命令对照表

| Windows | macOS/Linux | 说明         |
| ------- | ----------- | ------------ |
| cd      | cd          | 切换目录     |
| cd      | pwd         | 显示当前位置 |
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

### 命令行常用符号

| 符号 | 含义                           |
| ---- | ------------------------------ |
| `~`  | 当前用户的 home 目录           |
| `..` | 上一级目录                     |
| `*`  | 通配符，匹配任意字符           |
| `>`  | 将输出写入文件（重定向）       |
| `/`  | 目录分隔符（Windows 可用 `\`） |

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

## vim 编辑器基础

**模式切换**：

- **Normal 模式**：命令模式，无法直接输入文本。
- **Insert 模式**：文本输入模式。

**进入 Insert 模式**：

- `i` → 插入
- `a` → 追加
- `o` → 新建一行并输入

**切换模式**：

- Insert → Normal：`Esc` 或 `Ctrl + [`

**常用命令**：

| 命令  | 作用                     |
| ----- | ------------------------ |
| `:w`  | 保存文件                 |
| `:q`  | 退出文件（未保存会提示） |
| `:wq` | 保存并退出               |

## Git 基本设置

### 设置用户名与邮箱

```bash
git config --global user.name "Allay"
git config --global user.email "allay@qq.com"
```

检查配置：

```bash
git config --list
```

这些配置保存在 `~/.gitconfig` 文件中，也可手动修改。

### 针对单个项目设置不同作者

针对特定的项目设置不同的作者，可以用--local 参数

```bash
git config --local user.name "Andy"
git config --local user.email "andy@qq.com"
```

**global 设置**：全局生效。

**local 设置**：仅当前项目生效。

### 设置缩写

```bash
git config --global alias.co checkout
git config --global alias.l "log --oneline --graph"
```

示例：

- `git co` = `git checkout`
- `git l` = `git log --oneline --graph`

别名配置同样保存在 `~/.gitconfig` 文件中。
