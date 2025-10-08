---
# 文章标题
title: 5.1 Transition
# 文章内容摘要
# description:
# 文章内容关键字
keywords: Vue 过渡, Vue 动画, Vue Transition, Vue TransitionGroup, Vue CSS 动画, Vue JavaScript 钩子, Vue 动态过渡, Vue 组件过渡, Vue 过渡模式, Vue 可复用过渡组件
# 发表日期
date: 2025-04-17
summary: 本文主要介绍了 Vue 3 中内置的过渡与动画组件，包括 `<Transition>`以及基于 CSS 的过渡效果和 JavaScript 钩子。
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

## Vue 内置过渡与动画

Vue 提供了两个内置组件，用于基于状态变化的过渡和动画：

- **`<Transition>`**：在一个元素或组件进入和离开 DOM 时应用动画。
- **`<TransitionGroup>`**：在 `v-for` 列表中的元素或组件被插入、移动、或移除时应用动画。

其他动画方式：

- 切换 CSS class
- 用状态绑定样式来驱动动画

## `<Transition>` 组件

**内置组件**：无需注册，任意组件中均可使用。

作用：将进入和离开动画应用到通过默认插槽传递的元素或组件上。

**触发条件**：

- 由 `v-if` 触发的切换
- 由 `v-show` 触发的切换
- `<component>` 动态组件切换
- 改变特殊的 `key` 属性

限制：

- 仅支持单个元素或组件作为插槽内容。
- 如果内容是组件，该组件必须仅有一个根元素。

当 `<Transition>` 内元素被插入或移除时：

1. Vue 自动检测目标元素是否应用了 CSS 过渡或动画，添加/移除相应的 CSS class。
2. 如果提供了 JavaScript 钩子，在适当时机被调用。
3. 如果无 CSS 动画或 JS 钩子，DOM 插入/删除操作将在浏览器的下一个动画帧执行。

## 基于 CSS 的过渡效果

### CSS 过渡 class

一共 **6 个 class**：

1. **`v-enter-from`**：进入起始状态。插入前添加，插入后下一帧移除。
2. **`v-enter-active`**：进入生效状态。插入前添加，过渡完成后移除。可定义进入动画的持续时间、延迟和速度曲线。
3. **`v-enter-to`**：进入结束状态。插入后下一帧添加，同时移除 `v-enter-from`，过渡完成后移除。
4. **`v-leave-from`**：离开起始状态。离开触发时立即添加，一帧后移除。
5. **`v-leave-active`**：离开生效状态。离开触发时立即添加，过渡完成后移除。可定义离开动画的持续时间、延迟和速度曲线。
6. **`v-leave-to`**：离开结束状态。离开触发后下一帧添加，同时移除 `v-leave-from`，过渡完成后移除。

> `v-enter-active` 和 `v-leave-active` 可以为进入和离开动画指定不同速度曲线。

### 为过渡效果命名

使用 `name` prop 声明过渡效果名。

命名过渡的 class 前缀使用该名字而不是 `v`。

### CSS 过渡与动画

**CSS transition**：通过 `transition` 属性一次性定义过渡属性、持续时间和速度曲线。

**CSS animation**：与 transition 类似，但 `*-enter-from` 在 `animationend` 事件触发时才移除。

大多数 CSS 动画可在 `*-enter-active` 和 `*-leave-active` 中声明。

### 自定义过渡 class

通过 props 指定：

- `enter-from-class`
- `enter-active-class`
- `enter-to-class`
- `leave-from-class`
- `leave-active-class`
- `leave-to-class`

这些 class 会覆盖默认 class 名。

### 同时使用 transition 和 animation

Vue 依赖 `transitionend` 或 `animationend` 事件判断结束。

若同时使用两者，需显式传入 `type` prop，值为 `animation` 或 `transition`。

### 深层级过渡与显式过渡时长

可用深层级 CSS 选择器触发深层元素过渡。

可设置过渡延迟，形成渐进动画序列。

**默认问题**：Vue 仅监听根元素的第一个结束事件，嵌套过渡可能不符合预期。

**解决方案**：使用 `duration` prop 显式指定时长（可区分进入与离开）。

### 性能考量

**高效属性**：`transform`、`opacity`（不会触发布局，支持 GPU 加速）。

**昂贵属性**：`height`、`margin`（触发布局，需谨慎使用）。

## JavaScript 钩子

通过事件监听传入：

```vue
<Transition
  @before-enter="onBeforeEnter"
  @enter="onEnter"
  @after-enter="onAfterEnter"
  @enter-cancelled="onEnterCancelled"
  @before-leave="onBeforeLeave"
  @leave="onLeave"
  @after-leave="onAfterLeave"
  @leave-cancelled="onLeaveCancelled"
>
  <!-- ... -->
</Transition>
```

```js
// 在元素被插入到 DOM 之前被调用
// 用这个来设置元素的 "enter-from" 状态
function onBeforeEnter(el) {}

// 在元素被插入到 DOM 之后的下一帧被调用
// 用这个来开始进入动画
function onEnter(el, done) {
  // 调用回调函数 done 表示过渡结束
  // 如果与 CSS 结合使用，则这个回调是可选参数
  done();
}

function onAfterEnter(el) {} // 进入过渡完成时调用。

function onEnterCancelled(el) {} // 进入过渡在完成之前被取消时调用

// 在 leave 钩子之前调用
// 大多数时候，你应该只会用到 leave 钩子
function onBeforeLeave(el) {}

// 在离开过渡开始时调用
// 用这个来开始离开动画
function onLeave(el, done) {
  // 调用回调函数 done 表示过渡结束
  // 如果与 CSS 结合使用，则这个回调是可选参数
  done();
}

function onAfterLeave(el) {} // 离开过渡完成且元素已从 DOM 中移除时调用

function onLeaveCancelled(el) {} //  仅在 v-show 过渡中可用
```

钩子可与 CSS 配合，也可单独使用。

使用纯 JavaScript 动画时：

- 添加 **`:css="false"`**，避免 CSS 自动探测。
- `done` 回调必须调用，否则钩子会同步结束，过渡立即完成。

## 可复用过渡效果

使用组件封装 `<Transition>`，通过插槽传递内容，即可复用。

## 出现时过渡

初次渲染时添加 `appear` prop 触发过渡。

## 元素间过渡

使用 `v-if` / `v-else` / `v-else-if` 切换多个组件时，确保同一时刻只有一个元素被渲染。

## 过渡模式

默认进入和离开同时执行，可能需要 `position: absolute`。

通过 `mode` prop 可实现先离开再进入。

## 组件间过渡

`<Transition>` 可作用于 动态组件切换。

## 动态过渡

`<Transition>` 的 props 可动态设置，例如 `name`。

可通过不同状态应用不同过渡效果。

最终可封装为可复用的过渡组件。

## 使用 Key Attribute 过渡

强制 DOM 重新渲染时使用 `key`。

无 `key` 时仅更新文本节点，不会触发过渡。

有 `key` 时 Vue 会创建新元素，从而在元素之间执行过渡。
