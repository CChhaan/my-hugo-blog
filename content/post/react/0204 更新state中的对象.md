---
# 文章标题
title: 2.4 更新 state 中的对象
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: React mutation, React state 不可变, 不可变数据 immutable, React 更新对象 state, 浅拷贝对象, 展开语法拷贝对象, 局部 mutation, React state 只读原则, Immer 更新 state, 深层嵌套 state 更新, Proxy draft 机制, React 为什么不能直接修改 state, 引用比较优化, React 性能优化, state 快照原理, React 调试一致性, 撤销恢复状态管理, state 历史记录, 避免直接修改对象, React 最佳实践
# 发表日期
date: 2025-10-12
summary: 本文介绍了如何在 React 中更新 state 中的对象，包括如何将 state 视为只读的、使用展开语法复制对象、使用 Immer 编写简洁的更新逻辑以及为什么在 React 中不推荐直接修改 state。
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

## 什么是 mutation

可以在 state 中存放任意类型的 JavaScript 值。

数字、字符串、布尔值是 **不可变（immutable）** 的，只能通过替换值来触发重新渲染。

对象的内容技术上可以改变，**当你改变对象内容时就产生了 mutation**。

尽管对象是可变的，但在 React 中应将它们视为不可变，**通过替换对象而不是修改对象来更新 state**。

## 将 state 视为只读的

原则：**把 state 中的所有 JavaScript 对象都视为只读的**，**需要创建一个新对象并传给 state 设置函数**，才能触发重新渲染。

修改已存在于 state 中的对象内容会产生 mutation → **问题来源**。

修改刚创建、未被引用的对象不会产生问题 → **“局部 mutation”**。

“局部 mutation” 可以安全地发生在渲染过程中。

## 使用展开语法复制对象

`...` 实现对象的 **浅拷贝**。浅拷贝意味着只复制一层结构，更新嵌套属性时需多次使用展开语法。

可以在对象定义中使用 `[` 和 `]` 来动态生成属性名。

对象之间不是“真正嵌套”，只是通过属性相互引用。

## 使用 Immer 编写简洁的更新逻辑

使用场景：当 state 嵌套层级过多但不想更改数据结构时。

Immer 的作用：允许使用类似“直接修改对象”的写法。实际不会产生 mutation，而是生成 **新的对象副本**。

原理：Immer 提供的 `draft` 是 Proxy 对象，会记录对它的修改，Immer 根据这些修改生成新对象。

```js
updatePerson((draft) => {
  draft.artwork.city = "Lagos";
});
```

## 为什么在 React 中不推荐直接修改 state

- **调试**：不直接修改 state，可以保证日志中的旧值不会被新的变化污染。

- **优化**：React 的优化策略依赖于引用比较：**如果 `prevObj === obj`，则对象内部没有改变**。不直接修改 state 更易捕捉变化。
- **新功能**：新的 React 功能依赖于 state 像“快照”一样工作。直接修改历史 state 会破坏这些功能。
- **需求变更**：一些功能（撤销/恢复、历史记录、状态重置）依赖于保留旧 state。若直接修改 state，会使这类功能难以实现。
- **更简单的实现**：React 不依赖 mutation，也不需要对对象做特殊处理（如代理或劫持属性）。因此可以存放任意大小的对象而不引入性能问题。
