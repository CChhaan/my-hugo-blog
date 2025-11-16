---
# 文章标题
title: 1.3 将 Props 传递给组件
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: React props, React 组件通信, props 使用方法, React 传递数据, props 默认值, JSX children, JSX 展开语法, React 解构 props, props 不可变性, React 父子组件传值, React props 教程, React 数据流单向, React props 更新, 组件间传参, React 开发基础
# 发表日期
date: 2025-10-08
summary: 本文介绍了 React 组件使用 props 来互相通信。每个父组件都可以提供 props 给子组件，从而将信息传递给它。你可以通过 props 传递任何 JavaScript 值，包括对象、数组和函数。
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

**React 组件使用 _props_ 来互相通信。**每个父组件都可以提供 props 给子组件，从而将信息传递给它。你可以通过 props 传递任何 JavaScript 值，包括 **对象、数组和函数**。

## 熟悉的 props

Props 是你传递给 JSX 标签的信息。

对于内置标签，ReactDOM 所接受的 props 是 **预定义的**，并符合 HTML 标准

对于 **自定义组件**，你可以传递任意 props 以实现自定义。

## 向组件传递 props

步骤

1. **将 props 传递给子组件**
2. **在子组件中读取 props**

Props 使你可以独立思考父组件和子组件。

**Props 是组件的唯一参数。**React 组件函数接收一个 `props` 对象作为参数。

通常无需使用整个 `props` 对象，可通过 **解构** 获取单个 prop。

## 给 prop 指定一个默认值

如果未指定某个 prop，可以在参数解构时通过 `=` 为其赋予 **默认值**。

## 使用 JSX 展开语法传递 props

可以使用 **展开语法**（`{...props}`）来传递多个属性。

**请克制地使用展开语法。**如果在所有组件中都使用它，通常意味着组件设计需要重新拆分，将子组件作为 JSX 传递。

## 将 JSX 作为子组件传递

当你在 JSX 标签中嵌套内容时，父组件会在名为 **`children`** 的 prop 中接收到这些内容。

## Props 如何随时间变化

**组件可能会在不同时间收到不同的 props。**

Props 并不总是静态的，而是可以根据父组件的变化而更新。

**Props 是不可变的。**当组件需要改变 props 时，必须由父组件传入 **新的 props 对象**。

旧的 props 会被丢弃，最终由 JavaScript 引擎回收。

**不要尝试更改 props。**当需要响应用户输入时，应当使用 **state（状态）** 来实现。
