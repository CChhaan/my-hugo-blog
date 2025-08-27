---
# 文章标题
title: 第五章 开始使用git
# 文章内容摘要
# description:
# 文章内容关键字
keywords: Git, 仓库操作，提交记录，文件管控，.gitignore, reset, HEAD, SHA-1, Blob 对象，Tree 对象，commit 对象，版本控制
# 发表日期
date: 2025-06-23
summary: 本文主要介绍如何开始使用 Git，包括初始化 Repository、把文件交给 Git 管控、查看记录、删除文件或变更文件名以及修改 commit 记录等操作。
# 分类
categories:
  - Git从入门到精通
# 标签
tags:
  - Git
  - 版本控制工具
---

## 新增、初始 Repository

- **命令**：git init

- **作用**：在目录中创建一个.git 目录，该目录是 Git 进行版本控制的核心。若移除.git 目录，Git 将失去对该目录的控制权，可用于提供不含版控记录的内容给客户。

## 把文件交给 Git 管控

1. **查看目录状态**：git status

   - 显示文件状态：`Untracked`（未跟踪，新文件）、`Modified`（已修改未暂存）、`Staged`（已暂存待提交）。

2. **添加文件到暂存区**：

- 单个文件：git add <文件名>，将指定文件安置到暂存区。

- 特定类型文件：git add \*.html，把所有后缀为.html 的文件加到暂存区。

- 全部文件：

  - git add --all（或`git add -A`），添加项目中所有异动文件到暂存区；

  - git add .，添加当前目录及子目录中的异动文件到暂存区，对目录外文件无效。

1. **注意事项**：git add 后若再次改动文件，改动内容不会自动加入暂存区，暂存区仍为之前的版本，此时`git status`会显示文件同时处于`Modified`（工作区）和`Staged`（暂存区）状态。

2. **提交到存储库**：git commit -m 'init commit'，-m 后为提交说明，将暂存区内容永久保存到存储库。每次 commit 仅处理暂存区内容，未加入暂存区的文件不会被提交。

3. **空提交**：git commit --allow-empty -m ""，加上--allow-empty 参数，无文件变动时强制提交（常用于触发 CI/CD 流程或标记重要节点）。

## 工作区、暂存区与存储库

- **关系**：git add 将文件从工作目录移至暂存区，git commit 将暂存区内容移至存储库，完成 commit 才算整个流程结束。

- **简化提交**：git commit -a -m "update content"，-a 参数可缩短流程，跳过`git add`，直接将**已跟踪文件**的修改提交（新文件`Untracked`不生效，仍需手动`add`）。

## 查看记录

1. **基本查看**：git log，越新的信息越靠上，显示作者、提交时间、提交说明等。
2. **精简查看**：
   - `git log --oneline`：每行显示一条记录（哈希前缀 + 说明）。
   - `git log --graph --oneline`：图形化展示分支合并历史（直观看到分支流向）。
3. **按作者筛选**：git log --author="Sherly\\|Eddie"，\\|表示 “或者”，可查找多个人的提交记录。
4. **按提交信息筛选**：git log --grep="LOL"，从提交信息中搜索含关键字的内容。
5. **按内容筛选**：git log -S 'Ruby'，在所有提交文件中搜索符合特定条件的内容。
6. **按时间筛选**：git log --since="9am" --until="12am" --after="2017-01"，找出 2017 年 1 月之后每天早上 9 点到 12 点之间的提交。

## 删除文件或变更文件名

1. **删除文件**：

- 系统命令删除：使用 rm 或资源管理器删除后，git add 将改动加到暂存区再提交。

- git rm 命令：直接删除文件并加入暂存区，无需再 add。

- 仅移除管控：git rm --cached 文件名，--cached 参数使文件不被真的删除，仅从 Git 管控中移除。

2. **变更文件名**：

- 系统命令修改：mv 旧名 新名，Git 会视为删除旧文件和新增新文件，需 git add 将改动加到暂存区。

- git mv 命令：直接完成文件名变更并加入暂存区，减少操作步骤。

3. **Git 处理逻辑**：Git 通过**文件内容**（而非文件名）计算 SHA-1 哈希值，改名仅生成新的 Tree 对象（记录目录结构），Blob 对象（文件内容）不变，因此效率极高。

## 修改 commit 记录

1. **不建议方式**：删除.git 目录。

2. **推荐方式**：

- 使用 git rebase 命令改动历史记录。

- 用 git reset 命令删除提交，整理后重新提交。

- 改动最后一次提交：git commit --amend -m "xxx"，--amend 参数会重新计算并生成新的 commit 对象，仅适用于**未推送到远程**的提交（已推送的提交修改会导致协作冲突）。

3. **追加文件到最近一次提交**：

- 用 git reset 删除最后一次提交，加入新文件后重新提交。

- git commit --amend --no-edit，--no-edit 表示不编辑提交信息，将文件并入最近一次提交。

## 新增目录

- Git 根据文件内容计算生成对象，空目录无法提交，需在空目录中放一个文件（通常命名为`.gitkeep`，约定俗成的占位文件），使 Git 感应到目录存在。

## 忽略文件

1. **设置方法**：在项目目录中放置.gitignore 文件，设置忽略规则，文件不存在可手动新增。

2. **生效范围**：.gitignore 文件即使未提交或推送，也会生效，对规则设置后存入的文件有效，对已存在文件无效。

3. **常用规则写法**（面试高频）：

   - `# 注释`：单行注释。
   - `*.log`：忽略所有.log 文件。
   - `node_modules/`：忽略整个 node_modules 目录。
   - `/temp`：仅忽略根目录下的 temp 文件 / 目录（不忽略子目录中的 temp）。
   - `!README.md`：排除规则（不忽略 README.md，即使被前面的`*`匹配）。

4. **强制添加**：git add -f 文件名称，-f 参数可无视忽略规则添加文件。

5. **套用规则到已存在文件**：使用 git rm --cached。

6. **清除忽略文件**：git clean -fX，-f 为强制删除，-X 清除已被忽略的文件。

## 查看特定文件的 commit 记录

- git log 文件名，查看单一文件的提交记录；git log -p 文件名，查看该文件每次提交的改动内容。

## 查找代码作者

- git blame index.html，查看指定文件每一行代码的最后修改作者、时间及对应的 commit 识别代码。

- git blame -L 5,10 index.html，-L 参数指定显示第 5-10 行的信息。

## 恢复删除或修改的文件

- 恢复单个删除文件：git checkout index.html。

- 恢复所有删除文件：git checkout .，也可将改动文件恢复到上一次 commit 的状态。

- 原理：git checkout 后接文件名或路径时，会把暂存区或存储库中的文件复制到工作目录，覆盖当前内容（若文件在暂存区有修改，则用暂存区内容；否则用版本库最新内容）。

- 恢复到指定版本：git checkout HEAD~2 .，用距离现在两个版本以上的文件覆盖当前工作目录并更新暂存区。

## reset 相关操作

1. **拆掉最后一次 commit**：

- 相对做法：git reset e12d8ef^，^代表前一次，^^代表前两次，e12d8ef~5 代表前五次；因 HEAD 与 master 通常指向同一 commit，也可写成 git reset HEAD^或 git reset master^。

- 绝对做法：git reset 85e7e30，直接指明退回的 commit。

2. **参数区别**：

- --mixed（默认）：删除暂存区文件，不影响工作目录，拆出的文件留在工作目录但不在暂存区。

- --soft：工作目录与暂存区文件均不删除，拆出的文件直接放在暂存区，仅 HEAD 移动。

- --hard：工作目录和暂存区文件均被删除。

3. **本质**：git reset 并非删除或重新设置 commit，只是前往指定 commit。

4. **恢复 hard 模式 reset 的 commit**：可通过该 commit 的 SHA-1 值 reset 回去，--hard 参数可强迫放弃 reset 后的改动；若未记录 SHA-1 值，可用 git reflog 或 git log -g 查找记录。

## 提交文件的部分内容

- git add -p，-p 参数会询问是否将文件区域加到暂存区，选 y 加入整个文件，选 e 进入编辑器，删除不想加入的行，存档后即可将部分内容加到暂存区。

## HEAD

- 是指向某一分支的指标，通常指向当前所在分支，.git/HEAD 文件记录其内容。detached HEAD 状态指 HEAD 未指向任何分支。
- detached HEAD 状态：HEAD 直接指向某个 commit（而非分支），通常由`git checkout <commit哈希>`触发。
  - 注意：在此状态下提交的内容会成为 “游离 commit”，切换分支后可能丢失，需通过`git checkout -b 新分支`保留。

## SHA-1 值

- 是一种杂凑算法的结果，以 40 个十六进制数字呈现，输入相同则输出相同，输入不同则输出不同，Git 中所有对象编号均由此算法产生，SHA-1 重复概率极低。

- Blob 对象 SHA-1 组成：“blob” 字样 + 空白字节 + 输入内容长度 + null 结束符号 + 输入内容；tree 物件第一项为 “tree”，commit 为 “commit”，以此类推。

## .git 目录内容

**核心对象**

1. **Blob 对象**：存放文件内容，git add 时根据文件内容计算 SHA-1 值，以 SHA-1 值前两个字节为目录名，后 38 个字节为文件名，存于.git/objects 目录，内容经压缩。此设计可避免.git/object 目录因文件过多降低效率。

2. **Tree 对象**：存放目录及文件名，指向 Blob 对象或其他 Tree 对象，形成有向无环图（DAG）。

3. **commit 对象**：包含指向的 Tree 对象、提交时间、作者、提交信息，除第一个 commit 外，均指向前一次 commit。

4. **tag 对象**：指向特定 Commit（轻量 Tag 直接存 Commit 哈希，附注 Tag 为独立对象，含注释）。

5. **小结**：

- 文件内容转为 Blob 对象存储。

- 目录及文件名存于 Tree 对象，指向 Blob 或其他 Tree 对象。

- Commit 对象指向 Tree 对象，除首个外均指向前一次 Commit。

- Tag 对象指向 Commit 对象。

- 分支指向 Commit 对象，随提交移动。

- 推送后，.git/refs 下会多出 remote 目录，存放远端分支，指向 Commit 对象。

- HEAD 指向当前分支。

**存储特点**：

1. git add 时，即使文件仅改一字，因 SHA-1 值不同，也会生成全新 Blob 对象，而非记录差异，使 checkout 时无需拼凑历史记录，效率高。

2. **资源回收机制**：

- 作用：以高效方式压缩对象及制作下标，将.git/objects 目录下对象打包到.git/objects/pack 目录，打包时用类似差异备份方式缩小体积。

- 触发时机：.git/objects 目录对象或 packfile 对象过多时；执行 git push 命令推至远端服务器时；也可手动执行 git gc 触发。
