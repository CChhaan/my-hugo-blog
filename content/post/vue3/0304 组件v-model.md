---
# 文章标题
title: 3.4 组件 v-model
# 文章内容摘要
# description:
# 文章内容关键字
keywords: Vue v-model, Vue defineModel, Vue 双向绑定, Vue 组件通信, Vue 3.4 v-model 新语法, Vue modelValue, Vue update:modelValue, Vue v-model 参数, Vue 多个 v-model, Vue v-model 修饰符, Vue defineModel get set, Vue defineModel 默认值, Vue 组件数据同步
# 发表日期
date: 2025-04-12
summary: 本文主要介绍了 Vue 3.4 中组件 v-model 的使用方法，包括基本用法、分类、注意事项等。
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

## 基本用法

**`v-model`** 可以在组件上使用以实现**双向绑定**。

从 **Vue 3.4** 开始，推荐的实现方式是使用 **`defineModel()` 宏**。

**`defineModel()` 返回的值是一个 `ref`**：

- `.value` 与父组件的 `v-model` 值同步；
- 子组件变更 `.value` 时，父组件绑定的值也会更新。

可以用 `v-model` 把这个 `ref` 绑定到原生 input 元素，实现包装。

```vue
<script setup>
const model = defineModel();

function update() {
  model.value++;
}
</script>

<template>
  <div>Parent bound v-model is: {{ model }}</div>
  <button @click="update">Increment</button>
</template>
```

### 底层机制

`defineModel` 是一个**便利宏**，编译器会将其展开为：

- 一个名为 **`modelValue` 的 prop**，与本地 ref 的值同步；
- 一个名为 **`update:modelValue` 的事件**，在本地 ref 的值变更时触发。

Vue 3.4 之前的实现方式

```vue
<script setup>
const props = defineProps(["modelValue"]);
const emit = defineEmits(["update:modelValue"]);
</script>

<template>
  <input
    :value="props.modelValue"
    @input="emit('update:modelValue', $event.target.value)"
  />
</template>
```

父组件中的 `v-model="foo"` 将被编译为：

```vue
<Child :modelValue="foo" @update:modelValue="($event) => (foo = $event)" />
```

### 注意事项

- `defineModel` 声明了一个 prop。
- 可以通过传递选项给 `defineModel` 来声明底层 prop 的选项。
- **如果设置了 `default` 值且父组件没有提供该值，会导致父子组件不同步。**

## `v-model` 的参数

组件上的 `v-model` 可以接受参数。

在子组件中，通过将字符串作为 **第一个参数传递给 `defineModel()`** 来支持相应的参数。

如果需要额外的 prop 选项，应在 model 名称之后传递。

## 多个 `v-model` 绑定

利用参数和事件名，可以在单个组件实例上创建**多个 `v-model` 双向绑定**。

每个 `v-model` 会同步不同的 prop，且无需额外选项。

## 处理 `v-model` 修饰符

### 获取修饰符

- 通过解构 `defineModel()` 的返回值，可以在子组件中访问 `v-model` 的修饰符

```vue
<script setup>
const [model, modifiers] = defineModel();
</script>

<template>
  <input type="text" v-model="model" />
</template>
```

### 基于修饰符调节

- 可以给 `defineModel()` 传入 **`get`** 和 **`set`** 选项：
  - `get` 在读取值时接收当前值，并返回处理后的新值。
  - `set` 在设置值时接收当前值，并返回处理后的新值。
