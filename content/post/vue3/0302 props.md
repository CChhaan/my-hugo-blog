---
# 文章标题
title: 3.2 Props
# 文章内容摘要
# description:
# 文章内容关键字
keywords: Vue props, Vue defineProps, Vue props 声明, Vue props 校验, Vue 响应式 props, Vue 单向数据流, Vue props 默认值, Vue props 类型检查, Vue TypeScript props, Vue Boolean props, Vue props 对象绑定, Vue props 解构, Vue props 验证函数
# 发表日期
date: 2025-04-12
summary: 本文主要介绍 Vue3 中组件的 Props，包括 Props 声明、响应式 Props 解构、传递 prop 的细节、单向数据流、Prop 校验等内容。
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

## Props 声明

组件需要**显式声明 props**，Vue 才能区分外部传入的是 props 还是透传 attribute。

声明方式：

- `<script setup>` 中使用 **`defineProps()` 宏**。
- 非 `<script setup>` 中使用 **`props` 选项**。

传递给 `defineProps()` 的参数与 `props` 选项的值相同，本质上使用的都是 **props 选项**。

声明形式：

- **字符串数组**。
- **对象形式**：
  - key：prop 名称。
  - value：预期类型的构造函数。
  - 优点：
    - 一定程度上充当文档。
    - 类型错误时会在浏览器控制台抛出警告。

TypeScript：在 `<script setup>` 中可使用 **类型标注**声明 props。

## 响应式 Props 解构

Vue 响应系统基于属性访问跟踪状态。

在 `<script setup>` 中，解构的变量会自动加上 `props.` 前缀。

可使用 **JavaScript 默认值语法**声明 props 默认值。

Vue VSCode 插件可为解构 props 提供内联提示。

### 将解构的 props 传递到函数中

解构的 prop 传入函数时，传递的是**值**而非响应式数据源。

Vue 会捕捉并警告此情况。

推荐：将其包装在 **getter** 中，以保持响应性。

外部函数可调用 getter（或使用 **`toValue`**）来追踪 prop 变更。

## 传递 prop 的细节

### Prop 名字格式

长 prop 名：推荐使用 **camelCase**（合法的 JS 标识符，可直接在模板表达式中使用）。

实际传递时：通常写为 **kebab-case**，与 HTML attribute 对齐。

组件名推荐使用 **PascalCase**，提升可读性。

### 使用对象绑定多个 prop

使用**无参数的 `v-bind`** 可将对象所有属性作为 props 传入。

## 单向数据流

所有 props 遵循 **单向绑定**：

- 父组件更新 → 子组件接收新值。
- 子组件**不能修改** prop，否则 Vue 会警告。

导致你想要更改一个 prop 的常见需求场景：

1. **作为初始值**：子组件需定义新的本地数据属性，并以 prop 初始化。

2. **对传入值做转换**：基于该 prop 定义计算属性。

### 对象 / 数组类型的 props

子组件**可以修改对象或数组内部的值**（按引用传递）。

缺陷：可能导致子组件隐式影响父组件状态。

最佳实践：应通过**事件抛出**通知父组件修改。

## Prop 校验

声明方式：向 `defineProps()` 传入带校验的对象：

```js
defineProps({
  // 基础类型检查
  // (给出 `null` 和 `undefined` 值则会跳过任何类型检查)
  propA: Number,
  // 多种可能的类型
  propB: [String, Number],
  // 必传，且为 String 类型
  propC: {
    type: String,
    required: true,
  },
  // 必传但可为 null 的字符串
  propD: {
    type: [String, null],
    required: true,
  },
  // Number 类型的默认值
  propE: {
    type: Number,
    default: 100,
  },
  // 对象类型的默认值
  propF: {
    type: Object,
    // 对象或数组的默认值
    // 必须从一个工厂函数返回。
    // 该函数接收组件所接收到的原始 prop 作为参数。
    default(rawProps) {
      return { message: "hello" };
    },
  },
  // 自定义类型校验函数
  // 在 3.4+ 中完整的 props 作为第二个参数传入
  propG: {
    validator(value, props) {
      // The value must match one of these strings
      return ["success", "warning", "danger"].includes(value);
    },
  },
  // 函数类型的默认值
  propH: {
    type: Function,
    // 不像对象或数组的默认，这不是一个
    // 工厂函数。这会是一个用来作为默认值的函数
    default() {
      return "Default function";
    },
  },
});
```

`defineProps()` 参数中**不能访问 `<script setup>` 内定义的其他变量**。

补充细节：

- 所有 prop 默认都是**可选**，除非 `required: true`。
- 未传递的可选 prop：默认值为 **`undefined`**（`Boolean` 除外）。
- `Boolean` 类型未传递时：默认转换为 **`false`**。
- 有 `default` 值时：当 prop 值为 `undefined` 时会被替换为 `default` 值。

当 prop 的校验失败后，Vue 会在开发模式下抛出控制台警告。

如果使用了基于类型的 prop 声明 ，Vue 会尽最大努力在运行时按照 prop 的类型标注进行编译。

### 运行时类型检查

`type` 可为以下原生构造函数：

- `String`、`Number`、`Boolean`、`Array`、`Object`、`Date`、`Function`、`Symbol`、`Error`

`type` 也可为自定义类或构造函数，通过 **`instanceof`** 检查。

### 可为 null 的类型

必传但可为 null：使用包含 `null` 的数组语法。

若仅声明为 `type: null`，则允许任何类型。

## Boolean 类型转换

**声明为 Boolean 类型的 props** 有特别的转换规则，更贴近原生 boolean attributes 行为。

当允许多种类型时，Boolean 的转换规则依然适用。

当同时允许 **String** 和 **Boolean** 时：

- 仅当 **Boolean 出现在 String 之前**时，Boolean 转换规则才会生效。
