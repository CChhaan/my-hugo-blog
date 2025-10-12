---
# 文章标题
title: 3.5 透传 Attributes
# 文章内容摘要
# description:
# 文章内容关键字
keywords: Vue attributes 继承, Vue 透传 attribute, Vue inheritAttrs, Vue $attrs, Vue defineOptions inheritAttrs, Vue useAttrs, Vue v-on 事件继承, Vue class style 合并, Vue 多根组件 attribute 透传, Vue 组件属性继承, Vue 属性绑定, Vue attribute 透传控制
# 发表日期
date: 2025-04-12
summary: 本文主要介绍了 Vue 3 中透传 Attributes 的相关内容，包括 Attributes 继承、禁用 Attributes 继承、多根节点的 Attributes 继承以及在 JavaScript 中访问透传 Attributes 的方法。
# 分类
categories:
  - Vue3文档阅读
# 标签
tags:
  - vue
  - vue3
  - 前端框架
  - 前端开发
  - 组件化开发
---

## Attributes 继承

**透传 attribute**：传递给一个组件，却没有被该组件声明为 **props** 或 **emits** 的 attribute 或 `v-on` 事件监听器。

常见例子：`class`、`style`、`id`。

当一个组件以单个元素为根渲染时，透传的 attribute 会自动添加到根元素上。

### 对 `class` 和 `style` 的合并

如果子组件根元素已有 `class` 或 `style`，会与继承的值**合并**。

### `v-on` 监听器继承

同样规则适用于 `v-on` 事件监听器。

根元素自身的监听器与继承的监听器**都会被触发**。

### 深层组件继承

2. 透传的 attribute **不会包含**父组件已声明的 props 或 `emits` 的 `v-on` 侦听函数，这些被父组件**消费**。
3. 符合声明的透传 attribute，可以作为 **props** 传入子组件。

## 禁用 Attributes 继承

设置 `inheritAttrs: false` 可禁用自动继承。

在 `<script setup>` 中可使用 **`defineOptions`** 设置。

使用场景：当 attribute 需要应用到根节点以外的其他元素时。设置 `inheritAttrs: false` 后，可完全控制透传 attribute 的使用。

模板中可用 `$attrs` 访问透传 attribute。

`$attrs` 包含除已声明的 **props** 和 **emits** 外的所有 attribute：包括 `class`、`style`、`v-on` 监听器等。

#### 注意事项

- 透传 attributes 在 **JavaScript 中保留原始大小写**。
- `v-on` 事件监听器会暴露为函数，例如：`$attrs.onClick`。
- 使用没有参数的 `v-bind`，可将对象的所有属性作为 attribute 应用到目标元素上。

## 多根节点的 Attributes 继承

多根节点组件**没有自动 attribute 透传**。

如果 `$attrs` 没有显式绑定，会抛出运行时警告。

显式绑定 `$attrs` 时，则不会有警告。

## 在 JavaScript 中访问透传 Attributes

在 `<script setup>` 中可用 **`useAttrs()` API** 访问透传 attribute。

未使用 `<script setup>` 时，`attrs` 会作为 `setup()` 上下文对象的一个属性暴露。

### 注意事项

- `attrs` 对象总是反映**最新的透传 attribute**，但它**不是响应式**。
- 不能通过侦听器监听 `attrs` 的变化。
- 如果需要响应性：
  - 使用 **prop**；
  - 或使用 **`onUpdated()`** 在每次更新时结合最新的 `attrs` 执行副作用。
