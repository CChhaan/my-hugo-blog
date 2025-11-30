---
# 文章标题
title: 3.4 使用 Context 深层传递参数
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: React Context, React props drilling, 跨层级传递数据, context 使用场景, useContext, createContext, context provider, reducer 与 context 结合, React 状态管理, props 逐层传递问题, 状态提升问题, React 组件通信, 自定义 Hook, context 最佳实践, React 全局状态管理
# 发表日期
date: 2025-10-15
summary: 本文介绍了如何使用 Context 深层传递参数，包括创建 context、在需要数据的组件中使用 context、在提供数据的组件中提供 context 等步骤。同时，还介绍了如何结合使用 reducer 和 context，使组件更简洁。
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

## 传递 props 带来的问题

传递 props 是将数据通过 UI 树显式传递给需要它的组件的方式。

当需要在组件树 **深层传递参数**，或**复用相同参数** 于多个组件时，传递 props 会变得复杂。

最近的共同祖先组件可能离实际需要数据的组件很远。**状态提升过高** 会导致出现 **“逐层传递 props”** 的情况。

## Context：传递 props 的另一种方法

Context 允许父节点（甚至很远的父节点）向整棵子树提供数据。

使用 Context 的三个步骤：

1. **创建 context 并导出**

   使用 `createContext`仅需要 **默认值** 作为参数，默认值可为任意类型（如对象）。

2. **在需要数据的组件中使用 context**

   引入 `useContext` Hook 和所创建的 context，通过 `useContext(context)` 读取值。

   注意：`useContext` 只能在 React 组件的顶层调用（不能在循环或条件中）。

3. **在提供数据的组件中提供 context**

   使用 context 的 provider。**将需要访问这个 context 的组件树用 provider 包裹起来。**

## Context 会穿过中间层级的组件

Context 会穿越任意数量的中间组件（包括内置组件和自定义组件）。

**Context 让组件“适应周围环境”，根据所在的 context 进行不同渲染。**类似于 CSS 的属性继承。

**不同的 context 彼此独立，不会互相覆盖。**一个组件可以同时使用或提供多个不同的 context。

## 注意事项

如果只是要跨层级传 props，不一定需要使用 context。

使用 context 之前的替代方案：

1. **从 传递 props 开始**

   即使层级很多，也能保持数据流动非常清晰。这种方式更容易让维护者理解哪些组件使用哪些数据。

2. **抽象组件并通过 `children` 传递 JSX**

   如果许多中间组件只负责向下传递 props，这可能意味着应该抽象组件，减少不必要的中间层级。

只有在上述替代方案不适用时，再考虑使用 context。

## 结合使用 reducer 和 context

将 reducer 与 context 结合可避免显式传递当前状态和事件处理程序，使组件更简洁。

使用步骤：

1. **创建** context。

   在单独的文件中创建并导出 context，以便从其他文件导入。

2. 将 state 和 dispatch **放入** context。

   通过 context 提供 reducer 管理的状态和 dispatch。

3. 在组件树的任何地方 **使用** context。

   通过 context 读取 state 和 dispatch。

4. 将相关逻辑迁移到一个文件当中

   将 reducer 移动到该文件。声明新的 `Provider` 组件，用于统一管理：

Provider 的作用：

1.  管理 reducer 的状态。
2.  向组件树提供 context。
3.  接收 `children` 作为 prop，以便传递 JSX。

现在所有的 context 和 reducer 连接部分都在 `Context.js` 中。 **这保持了组件的干净和整洁，让我们专注于它们显示的内容，而不是它们从哪里获得数据。**

如果函数名以 `use` 开头，它就被认为是一个自定义 Hook。自定义 Hook 能使用其他 Hook。
