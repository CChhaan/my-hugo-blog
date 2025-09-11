---
# 文章标题
title: 3.2 props
# 文章内容摘要
# description:
# 文章内容关键字
keywords: Vue Props 声明 (defineProps), Props 传递规范，Props 单向数据流，Props 校验配置，Props 响应式处理
summary: 本节详细介绍了 Vue 3 中组件间传递数据的核心机制 Props，包括声明方式、传递方式、命名规范、单向数据流、校验配置和响应式处理等。通过本节的学习，读者将掌握如何在 Vue 3 中高效地使用 Props 进行组件间通信。
# 发表日期
date: 2025-04-09
# 分类
categories:
  - vue3文档阅读
# 标签
tags:
  - vue3
  - 前端框架
  - 组件化开发
  - 前端开发
---

## Props 核心作用与声明方式

Props 是父组件向子组件传递数据的**唯一标准接口**，子组件需显式声明接收的 props，Vue 才能才能区分 props 与透传 attribute。根据组件是否使用 `<script setup>`，声明方式略有不同。

### `<script setup>` 中声明 props（推荐）

使用 `defineProps()` 宏声明 props（无需导入），支持数组式、对象式和 TypeScript 类型标注三种形式。

#### 数组式声明（简单场景）

仅指定 prop 名称，不限制类型：

```js
// 子组件 Child.vue
<script setup>
// 声明接收的 props（仅指定名称）
const props = defineProps(['title', 'content'])

// 在脚本中访问 props
console.log(props.title)
</script>

<template>
  <!-- 模板中直接访问 props -->
  <h2>{{ title }}</h2>
  <p>{{ content }}</p>
</template>
```

#### 对象式声明（推荐，支持类型与校验）

指定 prop 名称、类型、默认值等，兼具文档和校验功能：

```js
<script setup>
const props = defineProps({
  // 基础类型：字符串（未传递时为 undefined）
  title: String,
  // 数字类型 + 必填校验
  count: {
    type: Number,
    required: true // 父组件必须传递
  },
  // 布尔类型 + 默认值
  isVisible: {
    type: Boolean,
    default: false // 未传递时默认为 false
  },
  // 对象类型 + 默认值（需用函数返回，避免引用共享）
  user: {
    type: Object,
    default: () => ({ name: 'Guest', age: 0 })
  }
})
</script>
```

#### TypeScript 类型标注（类型安全场景）

结合 TypeScript 时，可通过类型标注声明 props，支持默认值语法：

```ts
<script setup lang="ts">
// 基础类型
const props = defineProps<{
  title?: string // 可选
  count: number  // 必选
  isVisible: boolean
}>()

// 带默认值的类型标注（3.3+ 支持）
const props = defineProps<{
  title?: string
  count: number
}>()
  .withDefaults({
    title: '默认标题',
    count: 0
  })
</script>
```

### 非 `<script setup>` 中声明 props

通过 `props` 选项声明，作为组件选项的一部分：

```js
export default {
  // 数组式
  props: ["title", "content"],

  // 或对象式
  props: {
    title: String,
    count: {
      type: Number,
      required: true,
    },
  },

  setup(props) {
    // setup 函数中通过参数访问 props
    console.log(props.title);
  },
};
```

## Props 传递方式与命名规范

### 基础传递方式

父组件通过“自定义 attribute”向子组件传递 props，静态值直接书写，动态值用 `v-bind`（`:`）绑定。

#### 示例：

```xml
<!-- 父组件 Parent.vue -->
<template>
  <!-- 1. 传递静态值（字符串） -->
  <Child title="静态标题" />

  <!-- 2. 传递动态值（响应式数据） -->
  <Child
    :count="currentCount"
    :is-visible="showChild"
    :user="currentUser"
  />

  <!-- 3. 传递对象的所有属性（v-bind 无参数） -->
  <Child v-bind="article" /> <!-- 等价于 :title="article.title" :content="article.content" -->
</template>

<script setup>
import Child from './Child.vue'
import { ref, reactive } from 'vue'

// 动态数据
const currentCount = ref(10)
const showChild = ref(true)
const currentUser = reactive({ name: 'Alice', age: 20 })
const article = { title: '文章标题', content: '文章内容' }
</script>
```

### 命名规范

- **子组件声明**：使用 `camelCase`（驼峰命名），符合 JavaScript 标识符规则（如 `isVisible`）；
- **父组件传递**：使用 `kebab-case`（短横线命名），符合 HTML attribute 规范（如 `is-visible`）；
- **Vue 自动映射**：模板中会自动将 `kebab-case` 转换为 `camelCase`，无需手动处理。

#### 示例：

```js
// 子组件：camelCase 声明
const props = defineProps({ isVisible: Boolean });
```

```xml
<!-- 父组件：kebab-case 传递 -->
<Child is-visible="true" />
```

## Props 单向数据流与修改限制

Vue 中 props 遵循**单向绑定原则**：父组件更新 → props 变化 → 子组件更新，子组件**不能直接修改 props**（否则会触发警告）。

### 禁止直接修改的原因

- 确保数据流可预测：避免子组件意外修改父组件状态，导致数据流向混乱；
- 维护性：父组件是 props 的唯一数据源，便于追踪数据变更源头。

#### 错误示例（禁止）：

```js
<script setup>
const props = defineProps({ count: Number })

// ❌ 错误：直接修改 props
const increment = () => {
  props.count++ // Vue 会在控制台抛出警告
}
</script>
```

### 合法修改 props 的场景与解决方案

若需基于 props 做修改，需通过以下两种方式：

#### 将 props 作为局部数据的初始值

场景：props 仅用于初始化，后续修改子组件局部状态。

```js
<script setup>
import { ref } from 'vue'
const props = defineProps({ initialCount: Number })

// 1. 基于 props 初始化局部数据
const localCount = ref(props.initialCount)

// 2. 修改局部数据（不影响父组件）
const increment = () => {
  localCount.value++
}
</script>
```

#### 基于 props 定义计算属性或处理后的值

场景：需对 props 进行转换或计算后使用。

```js
<script setup>
import { computed } from 'vue'
const props = defineProps({ rawMessage: String })

// 基于 props 计算处理后的值
const formattedMessage = computed(() => {
  return props.rawMessage?.toUpperCase() || 'DEFAULT'
})
</script>
```

#### 对象/数组的特殊情况

对象或数组按引用传递，子组件**可修改内部属性**（Vue 不阻止，因性能代价过高），但不推荐：

```js
<script setup>
const props = defineProps({ user: Object })

// ⚠️ 不推荐：修改对象内部属性（影响父组件）
const changeName = () => {
  props.user.name = 'New Name' // 无警告，但破坏单向数据流
}
</script>
```

**最佳实践**：子组件通过 `emit` 通知父组件修改，而非直接操作：

```js
// 子组件：抛出事件
const emit = defineEmits(['update-user'])
const changeName = () => {
  emit('update-user', { ...props.user, name: 'New Name' })
}

// 父组件：监听事件并更新
<Child :user="currentUser" @update-user="currentUser = $event" />
```

## Props 校验与高级配置

通过对象式声明可配置 props 校验规则，在开发环境下，若传递的 props 不符合规则，Vue 会抛出控制台警告。

### 完整校验选项

```js
const props = defineProps({
  // 基础类型校验
  id: {
    type: Number, // 类型：Number
    required: true, // 必传
  },

  // 多类型校验
  value: {
    type: [String, Number], // 允许 String 或 Number
    default: 0, // 默认值
  },

  // 自定义校验函数（复杂逻辑）
  age: {
    type: Number,
    // 校验函数：返回 true 表示通过，false 表示失败
    validator: (value) => {
      return value >= 0 && value <= 120;
    },
    message: "年龄必须在 0-120 之间", // 自定义错误信息（3.4+ 支持）
  },

  // 可为 null 的必传类型
  config: {
    type: [Object, null], // 允许 Object 或 null
    required: true,
  },
});
```

### `type` 支持的类型

- 原生构造函数：`String`、`Number`、`Boolean`、`Array`、`Object`、`Date`、`Function`、`Symbol`、`Error`；
- 自定义类/构造函数：通过 `instanceof` 校验（如 `class User {}`，`type: User`）。

### 布尔类型 props 的特殊转换

布尔类型 props 遵循 HTML attribute 行为：

- 父组件传递 `<Child is-active />` → 子组件接收 `true`；
- 未传递 → 接收 `false`（可通过 `default: undefined` 改为 `undefined`）；
- 传递 `:is-active="false"` → 接收 `false`。

#### 多类型中的布尔转换：

当同时允许 `Boolean` 和 `String` 时，`Boolean` 需排在前面才能触发转换：

```js
// 正确：Boolean 在前，支持 <Child flag /> 解析为 true
flag: {
  type: [Boolean, String];
}

// 错误：String 在前，<Child flag /> 解析为 "flag" 字符串
flag: {
  type: [String, Boolean];
}
```

## Props 响应式与解构注意事项

### 响应式访问

props 是响应式的，直接访问 `props.xxx` 可追踪变化，但**解构会丢失响应性**：

```js
// ❌ 错误：解构后 count 不再响应式
const { count } = defineProps({ count: Number });

// ✅ 正确：保持响应式访问
const props = defineProps({ count: Number });
console.log(props.count); // 响应式
```

### 3.5+ 版本的解构优化

3.5+ 中，同一 `<script setup>` 内解构 props 会被编译器自动转换为 `props.xxx`，保持响应性：

```js
// 3.5+ 支持：解构后仍响应式（编译后为 props.count）
const { count } = defineProps({ count: Number });
```

### 传递解构 props 到外部函数

若需将解构的 props 传递到外部函数并保持响应性，需包装为 getter：

```js
// 子组件
const { count } = defineProps({ count: Number });

// 包装为 getter（保持响应性）
const getCount = () => count;

// 传递给外部函数
externalFunction(getCount);

// 外部函数中通过调用 getter 追踪变化
function externalFunction(getter) {
  watch(getter, (newVal) => {
    console.log("count 变化：", newVal);
  });
}
```

## 核心总结

| 主题       | 关键要点                                                      | 最佳实践                                              |
| ---------- | ------------------------------------------------------------- | ----------------------------------------------------- |
| 声明方式   | `<script setup>` 用 `defineProps()`，非 setup 用 `props` 选项 | 优先对象式声明，指定类型和校验                        |
| 传递规范   | 静态值直接传，动态值用 `v-bind`，对象全量传递用 `v-bind`      | 子组件用 `camelCase` 声明，父组件用 `kebab-case` 传递 |
| 单向数据流 | 子组件不可直接修改 props，对象/数组内部修改需谨慎             | 需修改时，通过局部数据或 `emit` 通知父组件            |
| 校验配置   | 支持类型、必填、默认值、自定义校验函数                        | 开发环境开启校验，提高组件健壮性                      |
| 响应式处理 | 避免解构丢失响应性，3.5+ 支持安全解构                         | 传递解构 props 到外部函数时用 getter 包装             |

Props 是组件通信的基础，遵循单向数据流和显式声明原则，能有效保证应用数据流向清晰、易于维护。
