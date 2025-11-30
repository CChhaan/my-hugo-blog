---
# 文章标题
title: 1.2 nodejs编程基础
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: npm, npm 包管理器, nodejs 包管理, npm 镜像源, npm init, npm install, npm uninstall, npm update, npm publish, npm unpublish, yarn 包管理器, package.json, 语义化版本号, dependencies, devDependencies, CommonJS 模块, module.exports, exports, require, nodejs 模块系统, events 模块, fs 模块, stream 接口, http 模块
# 发表日期
date: 2025-11-18
summary: 本文主要介绍 npm 包管理器的使用方式，并对 yarn 的基本命令进行了补充。文章详细说明了 package.json 的字段与语义化版本号规则，介绍了 Node.js 的 CommonJS 模块机制，并讲解了 Node.js 常用模块。
# 分类
categories:
  - Nodejs+webpack开发实战
# 标签
tags:
  - nodejs
  - 前端开发
---

## npm 包管理器介绍

**包管理器**：管理 Node.js 软件包的工具。

**NPM**：Node.js 默认包管理工具，用于解决依赖管理与软件包发布等问题。

常见的使用场景：

- 从 npm 服务器下载第三方包。
- 将自己编写的软件包发布到 npm 服务器。

### 更换 npm 镜像源

国内访问官方 npm 仓库较慢，可切换至淘宝镜像加速安装。

命令：

```bash
# 设镜像源为淘宝。
npm config set registry http://registry.npm.taobao.org
# 还原官方镜像源
npm config delete registry
```

使用淘宝镜像时无法执行 `publish` 与 `unpublish`，发布包需切回官方源。

### 初始化项目

在项目目录执行 `npm init`。按照提示生成 `package.json`，其中包含模块名称、版本、依赖等信息。

### 使用 npm 命令安装模块

命令格式：

```bash
npm install <模块名称>
```

安装类型：

- 本地安装（默认）：

  - 安装至当前目录的 `node_modules`。
  - 通过`require('模块名')` 可导入。

- 全局安装（-g）：

  - 第三方模块将被安装到/usr/local/lib/node_modules 目录或者安装 node.js 的目录。
  - 可直接在命令行使用。
  - 不可用 require 引用。

依赖类型：

**开发依赖**：`--save-dev` → 写入 `devDependencies`

**生产依赖**：`--save` → 写入 `dependencies`，开发环境和生产环境都需要使用

### 其他 npm 命令

卸载模块：`npm uninstall 模块名 [-g]`

查看已安装模块：`npm list [-g]`

更新模块：`npm update 模块名 [-g]`

搜索模块：`npm search 模块名`

发布模块：`npm publish`

撤销发布：`npm unpublish 模块名@版本号`

读取配置：`npm config get 名称`

设置配置：`npm config set 名称`

删除配置：`npm config delete 名称`

执行 package.json 中 scripts 定义的命令：`npm run 命令`

### yarn 包管理器

yarn：Facebook 发布的 NPM 替代工具，解决下载速度慢、全量下载、依赖混乱等问题。

安装命令：

```bash
npm install -g yarn
```

常用命令：

卸载模块：`yarn [global] remove 模块名`

更新模块：`yarn [global] upgrade 模块名`

安装模块：`yarn [global] add 模块名`

配置读写：`yarn config get/set/delete 配置名称`

执行 package.json 中 scripts 定义的命令：`yarn run 命令`

## package.json 文件介绍

package.json：Node.js 软件包的源数据描述文件，由 npm 或 yarn 创建。

### 字段说明

name：软件包名称。

version：软件包版本。

description：软件包简介。

main：软件包入口文件

scripts：项目命令

repository：仓库地址

bugs：问题反馈页面

keywords：软件包关键字

author：软件包作者

contributors：软件包贡献者

dependencies：生产依赖

devDependencies：开发依赖

license：开源协议

### 版本号说明（语义化版本）

版本号格式为 x.y.z 分别代表主版本号，次版本号和补丁版本号。

变更规则：

- 修复 bug → 更新 **z**
- 新增功能（向下兼容）→ 更新 **y**
- 不兼容变更 → 更新 **x**

### 常见版本号限定符

- `^0.1.0`：0.1.0 ~ 1.0.0（不含）
- `~0.1.0`：0.1.0 ~ 0.2.0（不含）
- `0.1.0`：固定版本
- `>=0.1.0`：大于等于 0.1.0
- `*`：任意版本

## nodejs 模块系统

Node.js 使用 **CommonJS 模块规范**。

每个 js 文件是独立模块，拥有自己的作用域。

### module 和 exports

每个模块内部的变量 module 代表当前模块对象。

module.exports 是对外的接口。加载模块实际上是读取该模块的 module.exports 属性。

module.exports 也是一个对象，所有需要导出的变量，函数，类都需要挂载到该对象上才能实现导出。

`exports`：`module.exports` 的引用别名，使用 `exports.xxx` 导出属性。

**不要修改 exports 的指向**。若模块只导出一个对象/函数，需使用 `module.exports = ...`。

### require

require 用于加载模块文件。

require 读取并执行一个 js 模块，然后返回该模块的 exports 对象，如果模块未找到，则会抛出错误。

加载模块时，模块扩展名为.js。

参数规则：

- `"/"` 开头：绝对路径
- `"./"` 开头：相对路径
- 无前缀：核心模块 或 node_modules 中的模块
- 如果没有找到指定的模块文件 node js 会尝试自动添加.js，.json，.node（编译后的二进制模块）后再去搜索。
- 如果传入的参数解析之后是一个目录，Nodejs 会读取该目录下的 package.json 文件的 main 字段来加载真正的入口文件，如果该目录下没有 package.json 文件，则尝试加载 index.js 或者 index.node。

## nodejs 常用模块

### events 模块

事件驱动 & 非阻塞 I/O 的核心模块，大多数 Node 模块继承自 events

基于事件的编程是发布订阅模式的典型实现。

使用步骤：

- 创建事件监听器实例
- 注册事件。

nodejs 中可以对同一个事件进行多次监听，也可以多次触发同一事件。

可以使用 once 来进行一次性监听。

### fs 模块

用来操作系统文件的模块。

> 以下：path：文件路径，content：文件内容；options：选项；callback：回调函数

读取文件：

```js
fs.readFile(path[,options],callback)
```

写入文件：

```js
fs.writeFile(path,content[,options],callback)
```

追加内容：

```js
fs.appendFile(path,content[,options],callback)
```

删除文件：

```js
fs.unlink(path, callback);
```

创建文件夹：

```js
fs.mkdir(path[,options],callback)
```

读取文件夹内容：

```js
fs.readdir(path,content[,options],callback)
```

删除文件夹：

```js
fs.rmdir(path, callback);
```

### stream 接口

Node.js 的抽象流接口，很多对象都实现了这个接口

属于 **EventEmitter** 实例，常用的事件有：

- data：当有数据可读时触发
- end：当没有更多数据可读时触发
- error：在读取或写入时发生错误时触发
- finish：在所有数据写入系统底层时触发

nodejs 中 stream 有四种类型：

- readable：可读
- writable：可写
- duplex：可读可写
- transform：数据转换

读取流都可以通过监听 data 和 end 事件来接收数据，不需要关系读取流的类型

优点：**低内存占用**，分块处理数据

通过调用写入流的 write()方法来写入数据，调用写入流的 end()来完成写入。当数据写入完毕时会触发 finish 事件

管道提供了一个读取流到写入流的机制，通常用管道从一个流中获取数据并将数据传递到另外一个流中。多个管道可以串行处理，数据会依次流经每个管道

```js
readStream.pipe(writeStream);
```

数据转换流：本质还是利用管道进行处理，将读取流通过 pipe()操作传入转换流，以达到数据转换的目的

### http 模块

作用：创建 HTTP 服务器处理请求、创建 HTTP 客户端发出请求

http 客户端可以向指定的 URL 发出请求，返回一个可读流。

实际开发中一般使用 Web 框架而非直接使用原生 http 模块
