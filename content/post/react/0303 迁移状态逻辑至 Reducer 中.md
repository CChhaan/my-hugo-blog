---
# 文章标题
title: 3.3 迁移状态逻辑至 Reducer 中
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: React useReducer, reducer 状态管理, useState 对比 useReducer, React 状态逻辑整合, reducer 纯函数, React action 派发, 状态更新逻辑, reducer 可测试性, reducer 可读性, React 状态管理模式, reducer 最佳实践, Immer 不可变数据, action type 设计, React 复杂状态管理, useReducer 使用场景
# 发表日期
date: 2025-10-15
summary: 本文介绍了如何使用 reducer 整合状态逻辑，包括将设置状态的逻辑修改成 dispatch 的 action，编写 reducer 函数，以及在组件中使用 reducer。同时对比了 `useState` 和 `useReducer` 的优缺点，并给出了编写一个好的 reducer 的建议。
# 分类
categories:
  - React文档阅读
# 标签
tags:
  - react
  - 前端框架
  - 前端开发
  - 组件化开发
---

## 使用 reducer 整合状态逻辑

Reducer 是处理状态的另一种方式。你可以通过三个步骤将 `useState` 迁移到 `useReducer`：

1. 将设置状态的逻辑**修改**成 dispatch 的 action

   使用 reducer 管理状态与直接设置状态不同。它不是通过设置状态告诉 React “要做什么”，而是通过事件处理程序 dispatch 一个 “action” 来指明 **用户刚刚做了什么**。状态更新逻辑保存在其他地方。

   传递给 `dispatch` 的对象叫做 “action”，它是普通 JavaScript 对象。action 的结构由你决定，但通常应至少包含表明 **发生了什么事情** 的信息。

   按照惯例通常会添加字符串类型的 `type` 字段，并通过其它字段传递额外信息。`type` 是特定于组件的。

2. **编写** 一个 reducer 函数；

   reducer 是放置状态逻辑的地方。它接受两个参数：当前 state、action 对象。

   reducer 返回更新后的 state，React 会将状态设置为它返回的值。

   由于 reducer 依赖 state 参数，可以 **在组件外部声明它**，减少缩进、提升可读性。

   在 reducer 中使用 `switch` 语句是一种惯例，建议：

   - 每个 `case` 块使用 `{}` 包裹，避免变量互相冲突。
   - 每个 `case` 通常应以 `return` 结尾。忘记 `return` 会 “进入” 下一个 `case`，产生错误。

3. 在组件中 **使用** reducer。

`useReducer` 与 `useState` 相似，需要传递初始状态，并返回：一个有状态的值和一个 dispatch 函数（用于派发 action）

`useReducer` 接受两个参数：reducer 函数和初始 state

如果需要，可以将 reducer 移到单独文件。事件处理程序通过派发 `action` 指定 **发生了什么**，而 reducer 通过响应 `actions` 决定 **状态如何更新**。

## 对比 `useState` 和 `useReducer`

- **代码体积：**使用 `useState` 时，一开始只需编写少量代码，使用 `useReducer` 时需要提前编写 reducer 和 actions，当多个事件处理程序以相似方式修改 state 时，`useReducer` 可以减少代码量。

- **可读性：** 当状态逻辑简单时，`useState` 可读性尚可。当逻辑变复杂时，组件会变得臃肿难读。`useReducer` 能将状态更新逻辑与事件处理程序分离。
- **可调试性：**使用 `useState` 时，很难判断问题来源。`useReducer` 中可以通过 reducer 打印日志观察每次状态更新及 action 来源。如果所有 action 没问题，则问题出在 reducer 的逻辑中。但相比 `useState`，需要单步执行更多代码。
- **可测试性：**reducer 是不依赖组件的 **纯函数**，可独立测试。对于复杂状态更新逻辑，可以针对特定初始状态与 action 断言 reducer 输出。

如果频繁在修改状态时出现问题，或组件需要更多逻辑，建议使用 reducer。不必整个项目都使用 reducer，可以自由搭配。

## 编写一个好的 reducer

- **reducer 必须是纯粹的。**

  与状态更新函数相似，`reducer` **在渲染时运行**。

  reducer 必须纯净：相同输入 → 相同输出。不应包含：异步请求、定时器、副作用（影响组件外部），应以不可变方式更新对象和数组。

  Reducer 不应修改 state。Immer 提供 `draft` 对象，用于安全修改 state，并在底层创建副本。

- 每个 action 描述单一用户交互，即使这个交互会引发数据的多个变化。
