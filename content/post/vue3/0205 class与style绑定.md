---
# 文章标题
title: 2.5 class与style绑定
# 文章内容摘要
# description:
# 文章内容关键字
keywords: Vue v-bind, Vue 动态绑定, Vue class 绑定, Vue style 绑定, Vue 动态样式, Vue 动态 class, Vue 计算属性样式, Vue 响应式样式绑定, Vue class 数组绑定, Vue 自动前缀
# 发表日期
date: 2025-04-10
summary: 本文主要介绍了 Vue 3 中如何使用 `v-bind` 指令绑定 HTML 元素的 `class` 和 `style` 属性。
# 分类
categories:
  - vue3文档阅读
# 标签
tags:
  - vue
  - vue3
  - 前端框架
  - 前端开发
---

**`v-bind`**: 用于将 HTML 元素的属性（包括 `class` 和 `style`）与动态数据绑定。

**特殊增强**: Vue 为 `class` 和 `style` 的 `v-bind` 提供了特殊功能，除了字符串，表达式的值也可以是**对象**或**数组**。

## 绑定 HTML class

### 绑定对象

使用 `:class`（`v-bind:class` 的缩写）可以绑定一个对象，根据对象的键值对动态地控制 class。

```vue
<div :class="{ active: isActive }"></div>
```

上面的语法表示 `isActive` 为 `true` 时，`active` 类会被添加；如果为 `false`，则移除该类。

可以在对象中定义多个类，按需控制多个类的添加或移除。

`:class` 指令可以与常规的 `class` attribute 共存。

绑定的对象不一定需要是内联的，可以直接绑定一个数据对象或**计算属性**。

### 绑定数组

`:class` 可以绑定一个数组来渲染多个 CSS class。

可以在数组中使用三元表达式来实现有条件地渲染某个 class。为了避免冗长，可以在数组中嵌套对象来处理有多个依赖条件的 class。

### 在组件上使用

当在组件上使用 `class` attribute 时，这些 class 会被添加到根元素上，并与该元素已有的 class **合并**。

如果组件有多个根元素，可以通过组件的 `$attrs` 属性指定接收 `class` 的元素

## 绑定内联样式

### 绑定对象

`:style` 支持绑定 JavaScript 对象值，对应 HTML 元素的 `style` 属性。

推荐使用 **camelCase** 来命名样式属性，但 `:style` 也支持 **kebab-case** 形式的属性名。

绑定一个样式对象通常是好主意，可以使模板更简洁。

如果样式对象需要更复杂的逻辑，可以使用返回样式对象的**计算属性**。

`:style` 指令可以和常规的 `style` attribute 共存。

### 绑定数组

`:style` 可以绑定一个包含多个样式对象的数组。这些对象会被**合并**后渲染到同一元素上。

## 自动前缀

如果你在 `:style` 中使用需要浏览器特殊前缀的 CSS 属性，Vue 会自动为这些属性添加相应的前缀。

Vue 会在运行时检测浏览器支持的属性，并为不支持的属性自动加上浏览器前缀。

### 样式多值

你可以为某个样式属性提供多个值，Vue 会渲染出当前浏览器支持的值。

```vue
<div :style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }"></div>
```
