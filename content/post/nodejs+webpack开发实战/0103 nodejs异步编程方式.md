---
# 文章标题
title: 1.3 nodejs 异步编程方式
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: nodejs 异步编程, 回调函数, 回调地狱, callback(error, data), Promise 基本概念, Promise 状态, then 链式调用, catch 捕获错误, Promise.resolve, Promise.reject, Promise.all, Promise.race, async 函数, await 用法, async/await 语法糖, 异步错误处理
# 发表日期
date: 2025-11-18
summary: 本文主要介绍了 nodejs 异步编程的方式，包括回调函数、Promise 和 async/await。
# 分类
categories:
  - Nodejs+webpack开发实战
# 标签
tags:
  - nodejs
  - 前端开发
---

## 回调函数

**nodejs 异步编程通过回调函数实现，但使用回调并不一定表示异步。**

回调函数在任务完成后被调用，nodejs 大量 API 都支持回调。

回调函数风格：错误需要通过回调参数传递，不能使用标准的抛错与捕获。

nodejs 回调函数签名：

```ts
func(param..., callback(Error,data))
```

**param**：调用 API 的参数，可有多个。

**callback(Error, data)**：

- 第一个参数永远是错误对象，成功时 error 为 `null`
- 第二个参数是成功结果

## Promise

### 基本知识

Promise 对象用于表示一个异步操作的最终完成或失败及其结果值。

promise 有以下几种状态：pending（初始状态）、fulfilled（操作成功）、rejected（操作失败）

状态只能从 pending → fulfilled / rejected，且只能发生一次。

Promise 构造函数的签名如下：

```ts
function Promise(function(resolve,reject):Promise{})
```

Promise 构造函数接收一个执行函数，该函数接受 resolve 和 reject 两个回调函数，当执行函数运行成功调用 `resolve`，失败调用 `reject`。

一旦 promise 发生状态变化，就会触发 then 方法

```ts
Promise.prototype.then = function(onFulfilled[, onRejcted]):Promise
```

**onFulfilled**：成功时回调；**onRejected**：失败时回调，参数可选

then 方法**返回一个新的 Promise**（支持链式调用）

由于 then 的第二个参数 onRejcted 的参数是可选的，因此 promise 的原型上提供了 catch 方法用于捕获异步错误，返回新的 Promise 对象：

```ts
Promise.prototype.catch = function(onRejected):Promise
```

链式调用特性：then/catch 的返回值会传给下一个 then/catch。链式调用中一旦某个 Promise 出错，链会中断并进入 catch。

### 其他操作

```ts
Promise.resolve(value);
```

根据 value 决定返回的 Promise 状态：

- value 是 Promise → 返回该 Promise
- value 是基本类型/空/普通对象 → 状态 fulfilled，值为 value

```ts
Promise.reject(reason);
```

返回一个状态为 rejected 的 Promise，reason 通常为 error 对象

```ts
Promise.all(promises);
```

所有 promise 成功，返回成功；任意一个失败，返回失败

```ts
Promise.race(promises);
```

第一个完成（成功或失败）决定最终状态

## async/await

async/await 是 **Promise 的语法糖**。使异步代码写起来更像同步，但 **不会阻塞线程**。

### async

async 必须加在函数前（普通函数、箭头函数、类方法均可）。被 async 修饰的函数 **最终一定返回 Promise**。

返回值规则：

- 返回基本值/空/普通对象 → Promise fulfilled，值为返回值

- 函数抛错 → Promise rejected，reason 为错误对象

- 返回 Promise → 结果由该 Promise 决定

直接调用 async 函数得到的是 Promise，需用 then 才能取结果。

### await

await **只能在 async 函数内部**使用。await 可以放在任何返回 promise 的函数前。

Promise 成功，返回成功值；Promise 失败，抛出错误（可用 try/catch 捕获）

callback 风格的异步函数可包装为 Promise，若回调返回多个值，需要手动封装为数组
