---
# 文章标题
title: 第九章 CSS DOM
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: 网页三层结构，DOM 样式操作，style 属性，className, CSS 与 JS 协作，前端分层思想
# 发表日期
date: 2025-08-19
summary: 本章详细介绍了网页的三层结构，以及如何通过 DOM 操作样式，包括 `style` 属性和 `className` 属性的使用。通过这些操作，开发者可以更灵活地控制网页的样式，实现更丰富的交互效果。
# 分类
categories:
  - JS DOM编程艺术
# 标签
tags:
  - JavaScript
  - DOM
  - CSS
  - 前端开发
---

## 网页的三层结构

网页的呈现和交互由**结构层、表示层、行为层**共同构成，三者各司其职又协同工作：

1. **结构层**：
   - 由 HTML/XHTML 标记语言实现，通过标签（如 `<p>`、`<div>`）描述内容的**语义和结构**（如标题、段落、列表），不包含样式或行为信息。
   - 示例：`<h1>标题</h1>` 仅定义 “这是一个一级标题”，不规定其颜色、大小。
2. **表示层**：
   - 由 CSS 负责，定义内容的**视觉呈现**（如颜色、字体、布局）。
   - 即使未显式编写 CSS，浏览器也会应用默认样式（如 `<h1>` 默认加粗、字号较大）。
3. **行为层**：
   - 由 JavaScript 和 DOM 控制，定义内容对**事件的响应方式**（如点击、鼠标悬停）。
   - 浏览器默认也有基础行为（如链接点击跳转、表单提交），JS 可扩展或修改这些行为。

## 通过 DOM 操作样式：`style` 属性

### `style` 属性的特性

- 每个元素节点的 `style` 属性是一个对象，包含该元素的**内嵌样式**（即通过 `style` 属性直接定义的样式，如 `<div style="color: red">`）。

- **命名规则**：CSS 属性名中的减号（如 `font-size`）在 `style` 对象中需转换为**驼峰命名法**（如 `style.fontSize`），避免与 JS 语法冲突。

- 局限性：

  - 仅能获取 / 修改**内嵌样式**，无法访问外部 CSS 文件或 `<style>` 标签中定义的样式。

  - 示例：

    ```html
    <div id="box" style="width: 100px; color: blue;"></div>
    <script>
      const box = document.getElementById("box");
      console.log(box.style.width); // 输出 "100px"（获取内嵌样式）
      console.log(box.style.fontSize); // 输出 ""（非内嵌样式无法获取）
    </script>
    ```

### 通过 `style` 属性设置样式

- `style` 对象的属性是**可读写的**，可通过赋值修改样式，值需为字符串（需加引号）。

- 示例：

  ```js
  const box = document.getElementById("box");
  box.style.color = "red"; // 修改文字颜色
  box.style.fontSize = "20px"; // 修改字号（驼峰命名）
  box.style.border = "1px solid black"; // 支持 CSS 速记属性
  ```

## `className` 属性操作样式

### 作用与用法

- `className` 属性用于获取或设置元素的 `class` 属性值，是操作样式类的便捷方式。
- **读取**：`element.className` 返回元素的 `class` 字符串（如 `box active`）。
- **设置**：通过赋值替换或追加类名，从而应用预定义的 CSS 样式。

### 示例

```html
<style>
  .highlight {
    color: red;
  }
  .bold {
    font-weight: bold;
  }
</style>
<p id="text" class="bold">文本</p>

<script>
  const text = document.getElementById("text");
  console.log(text.className); // 输出 "bold"

  // 替换类名
  text.className = "highlight"; // 现在 class 为 "highlight"，文本变红

  // 追加类名（保留原有类）
  text.className += " bold"; // 现在 class 为 "highlight bold"，文本既红又粗
</script>
```

## 何时用 DOM 设置样式？

选择 CSS 还是 DOM 脚本设置样式，需权衡以下因素：

1. **简单性**：
   - 静态样式（如默认布局）优先用 CSS，更简洁且易维护。
   - 动态样式（如点击后变色、滚动时改变位置）需用 DOM，因需响应事件。
2. **兼容性**：
   - 复杂 CSS 特性（如某些新属性）可能存在浏览器兼容问题，DOM 操作兼容性更一致。
3. **灵活性**：
   - DOM 可根据条件动态调整样式（如根据用户行为切换类名），CSS 难以实现这种逻辑判断。

## 抽象思维在样式操作中的体现

- 抽象：将具体功能通用化的过程。例如，将 “为某个按钮添加高亮” 的代码，改为 “为任意元素添加指定类名” 的函数，提升复用性：

  ```js
  // 具体实现：只为按钮添加高亮
  document.getElementById("btn").className += " highlight";

  // 抽象实现：为任意元素添加任意类
  function addClass(element, className) {
    element.className += " " + className;
  }
  addClass(document.getElementById("btn"), "highlight"); // 复用函数
  ```
