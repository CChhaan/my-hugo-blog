---
# 文章标题
title: 5.4 Teleport
# 文章内容摘要
# description:
# 文章内容关键字
keywords: Vue Teleport, Vue 组件传送, Vue DOM 外渲染, Vue 模态框, Vue Teleport to prop, Vue Teleport 动态禁用, Vue Teleport defer, Vue 组件逻辑保持
# 发表日期
date: 2025-04-18
summary: 本文主要介绍了 Vue 3 中的 Teleport 组件，它可以将组件内部的一部分模板“传送”到该组件 DOM 结构外层的位置。使用场景包括全屏模态框等。Teleport 组件的使用方法、分类、与组件的搭配使用、禁用 Teleport、多个 Teleport 共享目标以及延迟解析的 Teleport 等内容都进行了详细说明。
# 分类
categories:
  - vue3文档阅读
# 标签
tags:
  - vue
  - vue3
  - 前端框架
  - 前端开发
  - 组件化开发
---

## `<Teleport>` 组件

`<Teleport>` 是一个内置组件，它可以将组件内部的一部分模板 **“传送”到该组件 DOM 结构外层的位置**。

使用场景：模板的一部分逻辑上属于该组件，但在 DOM 中需要渲染到其他位置，甚至 Vue 应用外部。

常见例子：全屏模态框。

- 触发按钮和模态框属于同一个组件，逻辑紧密相关。
- 若不使用 `<Teleport>`，模态框会深嵌在 DOM 结构中，导致 CSS 布局困难。

**解决方案**：使用 `<Teleport>` 将模板片段传送到 DOM 中的其他位置，避免 DOM 结构的限制。

**`to` prop**：

- 用于指定传送的目标。
- 值类型：
  - CSS 选择器字符串
  - DOM 元素对象
- 含义：将以下模板片段 **传送到 `to` 指定的标签下**。

**结合使用**：

- `<Teleport>` 可以与 `Transition`搭配，创建带动画的模态框。

**挂载要求**：

- `<Teleport>` 挂载时，目标 `to` 必须已存在于 DOM 中。
- 理想情况下，目标元素应位于 Vue 应用 DOM 树外部。
- 若目标元素由 Vue 渲染，则必须在 `<Teleport>` 挂载前挂载该元素。

## 搭配组件使用

`<Teleport>` 只改变 **渲染的 DOM 结构**，不会影响组件的逻辑关系。

**逻辑保持**：

- 如果 `<Teleport>` 包含组件，该组件仍与使用 `<Teleport>` 的组件保持 **父子关系**。
- props 传递和事件触发依然照常工作。

**开发工具表现**：

- 父组件的注入正常生效。
- 子组件在 Vue Devtools 中依然嵌套在父组件下，而不是出现在实际渲染的位置。

## 禁用 Teleport

通过动态传入 `disabled` prop，可以按需禁用 `<Teleport>`。

## 多个 Teleport 共享目标

在多个实例共存的场景下（如 `<Modal>` 可复用组件）：

- 多个 `<Teleport>` 可将内容挂载到同一个目标元素。
- **顺序规则**：后挂载的内容会排在目标元素下更后的位置，但都属于该目标元素。

## 延迟解析的 Teleport

**版本要求**：Vue 3.5+

使用 `defer` prop 可以 **推迟目标解析**，直到应用的其他部分挂载完成。

适用场景：目标容器由 Vue 渲染，且位于组件树之后部分。

**注意事项**：

- 目标元素必须与 `<Teleport>` 在 **同一个挂载/更新周期** 内渲染。
- 若目标元素延迟过久（如 1 秒后才挂载），Teleport 仍会报错。
- 延迟原理与 `mounted` 生命周期钩子类似。
