---
# 文章标题
title: 5.2 TransitionGroup
# 文章内容摘要
# description:
# 文章内容关键字
keywords: Vue TransitionGroup, Vue 列表动画, Vue 列表过渡, Vue 渐进延迟动画, Vue moveClass, Vue CSS 列表动画, Vue v-for 动画, Vue 列表元素过渡
# 发表日期
date: 2025-04-17
summary: 本文主要介绍了 Vue3 中 `<TransitionGroup>` 组件的使用，包括其和 `<Transition>` 的区别、自定义过渡组 class 以及渐进延迟列表动画的实现方法。
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

## `<TransitionGroup>` 组件

`<TransitionGroup>` 是一个内置组件，用于对 `v-for` 列表中的元素或组件的 **插入、移除和顺序改变** 添加动画效果。

## 和 `<Transition>` 的区别

支持与 `<Transition>` 基本相同的 **props、CSS 过渡 class 和 JavaScript 钩子监听器**。

**区别**：

1. 默认情况下不会渲染容器元素，可通过 `tag` prop 指定容器元素。
2. **过渡模式不可用**，因为不是在互斥元素之间切换。
3. 列表中的每个元素都 **必须** 有独一无二的 `key` attribute。
4. **CSS 过渡 class 作用在列表内元素上，而不是容器元素上**。

当在 DOM 内模板中使用时，组件名需要写为 **`<transition-group>`**。

### 自定义过渡组 class

通过 `moveClass` prop 可以为 **移动元素** 指定自定义过渡 class。类似于 自定义过渡 class。

## 渐进延迟列表动画

实现方法：

1. 将每个元素的 **索引** 渲染为该元素的 **data attribute**。
2. 在 JavaScript 钩子中，基于元素的 data attribute，给该元素的 **进场动画添加延迟**。
