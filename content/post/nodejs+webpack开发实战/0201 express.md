---
# 文章标题
title: 2.1 express
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: express 框架, express 路由, express 中间件, 请求对象 request, 响应对象 response, Node.js Web 开发, express 静态资源, cookie-parser, body-parser, express 错误处理, express 模板引擎, ejs 模板, express 路由参数, express 响应方法, express 重定向, express 下载文件, express 配置, express 基本使用
# 发表日期
date: 2025-11-20
summary: 本文主要介绍了 express 框架的基本使用、路由、请求对象和响应对象等内容。
# 分类
categories:
  - Nodejs+webpack开发实战
# 标签
tags:
  - nodejs
  - 后端开发
---

## 基本使用

express 框架的核心特性：

- 通过设置中间件处理 HTTP 请求
- 通过路由执行不同的 HTTP 请求操作
- 通过模板渲染 HTML 页面

初始化：安装 express，并将其保存到 `package.json` 依赖列表中

使用 express 开发步骤：初始化项目 → 安装依赖 → 创建应用实例 → 编写路由文件并导入中间件 → 编写模板文件 → 开启监听 → 运行项目并测试

使用 express 框架优点如下：

- **支持路由**，Node.js 原生 http 模块需要自行实现
- **支持直接输出 JSON**，原生模块需要手动 JSON.stringify

## 路由

路由用于根据路由路径与 HTTP 请求方法处理请求。

在 express 中，每个路由可以包含一个或多个处理函数。

路由结构：

```js
app.METHOD(PATH, HANDLER);
```

app：应用实例；method：HTTP 请求方法（小写）；PATH：路由路径；HANDLER：路由匹配时执行的函数

### 路由方法

路由方法由 HTTP 方法派生，express 支持所有 HTTP 方法

使用 `app.all()` 可处理所有请求方法

### 路由路径

路由路径 + 请求方法共同定义可请求的地址。

路由路径可为字符串、字符串模式或正则表达式。GET 查询字符串 **不属于** 路由路径。

字符串模式可以认为是正则表达式的子集，支持部分正则表达式语法：

- `?`：至多一个
- `+`：至少一个
- `()`：分组

### 路由参数

路由参数用于捕获 URL 各位置的值，放入 `req.params`

路由参数名由大小写字母、数字、下划线组成，字符串模式中的 `-` 和 `.` 按字面含义解析

可使用正则表达式限制参数类型，不满足则无法匹配该路由

### 路由函数

路由方法和路由路径匹配之后就会执行对应的路由函数

```js
function(request,response,next)
```

request：请求对象；response：响应对象；next：匹配的下一个路由函数（可选参数）

最简单的路由函数对请求处理后直接结束响应

同一个路由可定义多个路由函数，每个路由函数做一项工作。必须调用 `next()` 才能继续执行后续路由函数

可用函数数组定义多个路由函数

`app.route()` 用于统一管理相同路径但不同请求方法的路由

Router 对象可用于模块化路由，便于维护、统一前缀、模块化解耦

## 请求对象

每个路由函数都会接收一个 request 对象，用于访问本次请求的信息。

常用属性：

method：请求方法

path：不含 GET 参数的路径

url：除域名外的含 GET 参数的完整 URL

query：GET 参数对象

params：路由参数对象

headers：请求报头

cookies：请求 cookie，需要 cookie-parser 中间件

ip：客户端 IP

body：POST 请求体数据，需要 body-parser 中间件

### 获取请求体

express 默认不处理请求体，可手动监听 data 的 end 事件或使用 body-parser 中间件

## 响应对象

用于向客户端发送响应，并结束请求处理。若不调用任何响应方法，请求将挂起直到超时。

常用操作：

1. 设置响应状态码：

```js
resp.status(statusCode);
```

statusCode：响应状态码

2. 设置响应报头

```js
resp.set(field[,value])
resp.set({
    [field]:value
})
```

field：响应报头字段名称；value：响应报头字段值

3. 通过 content-disposition 响应报头提示客户端下载文件

```js
resp.download(path[,filename][,options][,callback])
```

path：需要提供给客户端下载的服务端文件路径；filename：客户端下载文件时的别名；options：下载选项；callback：回调函数

4. 结束响应

```js
resp.end([chunk][,encoding][,callback])
```

chunk：响应数据；encoding：响应体编码；callback：回调函数

5. 重定向到指定的 URL Path 或者完整的 URL 链接，默认情况下响应状态码为 302

```js
resp.redirect([status,]path)
```

status：响应状态码，301 或 302；path：重定向路径

6. 渲染 HTML 模板页面，渲染模板页面需要使用模板引擎

```js
resp.render(view[,locals][,callback])
```

view：视图名称；locals：传递到视图的变量对象，视图可以访问到这些变量并进行渲染

callback：回调函数，如果提供，该方法将返回可能的错误和 HTML 字符串，但不是自动发生 HTML 到客户端

7. 设置 cookie

```js
resp.cookie(name,value[,options])
```

name：cookie 名称；value：cookie 值；

options 选项：

- domain：域名。默认为当前域名
- expires GMT：到期时间，如果未设置或者设置为 0，则浏览器关闭后 Cookie 失效
- httpOnly：将 cookie 标记为只有 HTTP 服务器能访问，客户端 JS 无法访问
- maxAge：以毫秒为单位的过期时间，通常比 expires 选项使用方便
- path：cookie 路径
- secure：标记为仅在 HTTPS 协议下才发送
- signed：是否对 cookie 签名

8. 发送 HTTP 响应

```js
resp.send([body]);
```

body 类型决定 content-type：

- string → text/html
- buffer → application/octet-stream
- object/array → application/json

## 中间件

中间件是能访问请求、响应和 next 的函数。

中间件可以执行以下任务：

- 执行逻辑代码
- 更改请求/响应对象
- 结束请求-响应周期
- 调用下一个中间件

若当前中间件未调用 next() 且未结束响应，请求将挂起。

中间件类型：

- **全局中间件**：对所有请求生效
- **路由中间件**：仅对特定路径生效

### cookie 中间件

编写 cookie 的思路如下：

- 读取请求报头的 cookie 字段
- 使用 `;` 分隔 cookie
- 针对单个 cookie，使用 `=` 分隔名称和值
- 将获取到的 cookie 名字和值挂载到 req.cookies 对象上

express 默认不解析请求报头中的 cookie

cookie-parser 中间件的作用：解析 header 中的 cookie 并挂载到 `req.cookies`

### 响应时长中间件

使用 response 的 `finish` 事件监听响应结束

需要 `once` 绑定事件，不能使用 `on`，否则会导致内存泄漏

### 静态资源中间件

为了提供图片、css 和 js 之类的静态文件的访问，可以使用内置的 express.static 中间件：

```js
express.static(root, [options]);
```

root：服务器文件夹路径；options：选项

## 错误处理

express 默认提供错误处理程序。

**同步错误**：自动交由框架处理

**异步错误**：需 `next(error)`，任意非空参数都会触发错误流程，建议传递 Error 对象

### 自定义错误处理函数

```js
function errorHandler(err,req,resp,next)
```

err：错误对象；req：请求对象；resp：响应对象；next：下一个错误处理器

错误处理器需放在所有中间件和路由的后面

可拆分为多个错误处理中间件（如日志记录、响应处理），需调用 `next()` 才会进入下一个错误处理器

## 模板渲染

模板引擎可在运行时替换变量并生成 HTML。

要渲染模板文件，需要安装对应的模板引擎，还需要更改 app 设置

```js
app.set("views", "./templates");
app.set("view engine", "ejs");
```

ejs 是接近普通 html 语言的模板，靠标记实现模板动态化。

### ejs 语法

- 转义输出，如果 title 字符串含有 HTML 代码，则最终显示时会被转义为实体字符

```ejs
<%= title %>
```

- 不转义输出（有 XSS 风险）

```ejs
<%- title %>
```

- 执行 JS

```ejs
<% 代码 %>
```

- 导入其他模板

```ejs
<% include 模板路径 %>
```

- 逻辑判断

```ejs
<% if(condition) { %>
    // HTML代码
<% } %>
```

- 循环

```ejs
<% list.forEach((item)=>{ %>
    <%= item %>
<% }) %>
```
