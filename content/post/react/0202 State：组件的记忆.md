---
# 文章标题
title: 2.2 State：组件的记忆
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: React useState, React 状态管理, React Hooks 基础, useState 初始值, state 更新触发渲染, 组件多次渲染机制, 局部变量与 state 区别, Hook 调用规则, 顶层调用 Hooks, React 组件 state 隔离, 私有 state, 多个 state 变量, 合并 state, React 渲染流程, state setter 函数, 自定义 Hook 原理, React 数据持久化, 重新渲染触发条件
# 发表日期
date: 2025-10-11
summary: 本文介绍了 React 中 State 的概念，包括 State 的定义、分类、剖析、赋予一个组件多个 state 变量以及 State 是隔离且私有的等内容。
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

## 当普通的变量无法满足时

**局部变量无法在多次渲染中持久保存。**React 会从头重新渲染组件，不会考虑之前对局部变量的更改。

**更改局部变量不会触发渲染。**React 并不会意识到数据变化，因此不会重新渲染组件。

解决需求，需要同时满足两点：

1. **保留** 渲染之间的数据。
2. **触发** React 使用新数据重新渲染组件。

`useState` 提供的功能

- **State 变量**：保存渲染间的数据。
- **State setter 函数**：更新变量并触发组件重新渲染。

## 剖析 `useState`

### Hook 的定义

`useState`（以及任何以 `use` 开头的函数）被称为 **Hook**。Hook 是特殊函数，只在 React **渲染时有效**，它们允许你“hook”到 React 的特性中。

**Hooks 只能在：**组件最顶层或 **自定义 Hook** 的最顶层调用。不能在条件语句、循环、嵌套函数中调用。将 Hook 视为组件顶层的“无条件声明”。

### `useState` 的行为

唯一参数：state 变量的 **初始值**。

每次渲染时，它返回一个数组：

1. **state 变量**（如 `index`）保存上次渲染的值。
2. **state setter 函数**（如 `setIndex`）更新 state 并触发重新渲染。

渲染过程（顺序）：

1. **组件进行第一次渲染。**
2. **你更新了 state。**
3. **组件进行第二次渲染。**
4. 以此类推。

## 赋予一个组件多个 state 变量

如果 state **不相关**，可以使用多个 state 变量；如果两个 state **经常一起改变**，应考虑将它们合并为一个。

### React 如何知道返回哪个 state

Hooks 依赖于 **稳定的调用顺序**。

React 为每个组件维护一个 **state 对数组**，并在每次渲染前将索引设为 0。

每次调用 `useState`，React 返回一个 state 对并增加内部索引指针

只要 Hooks 始终在顶层调用，调用顺序就不会变化。

## State 是隔离且私有的

**每个组件实例都有自己的 state。**即使渲染两次同一个组件，它们的 state 也完全隔离。

state 的作用域只影响组件在屏幕上的那一处实例。

**state 完全私有于声明它的组件，父组件无法更改它。**可以安全地添加或删除组件的 state，而不影响其他组件。
