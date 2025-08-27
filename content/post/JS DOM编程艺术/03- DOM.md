---
# 文章标题
title: 第三章 DOM
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: DOM, 文档对象模型，节点树，元素节点，getElementById, getElementsByClassName, setAttribute, DOM 属性操作
# 发表日期
date: 2025-08-16
summary: 本章详细介绍了 DOM 的核心概念、节点类型、CSS 与 DOM 的关联以及获取元素节点的 DOM 方法，为后续的 DOM 操作打下了基础。
# 分类
categories:
  - JS DOM编程艺术
# 标签
tags:
  - JavaScript
  - DOM 操作
  - 前端开发
---

## DOM 的核心概念

DOM（Document Object Model，文档对象模型）是一套用于抽象和概念化文档内容的接口，它将网页文档转换为可通过 JavaScript 操作的对象树结构。

### D：文档（Document）

- 当网页加载到浏览器时，浏览器会自动将 HTML/XML 文档解析为一个 **文档对象**，即 DOM 的基础。

### O：对象（Object）

- 对象是包含数据和方法的集合：
  - **属性**：对象关联的变量（如 `element.id`）；
  - **方法**：对象可调用的函数（如 `element.appendChild()`）。
- JS 中的对象类型：
  - **用户定义对象**：开发者创建的自定义对象；
  - **内建对象**：JS 自带的对象（如 `Array`、`Date`）；
  - **宿主对象**：浏览器环境提供的对象（如 `window`、`document`）。
- 关键宿主对象：
  - `window`：对应浏览器窗口，属于 BOM（浏览器对象模型）；
  - `document`：对应网页内容，是操作 DOM 的核心对象。

### M：模型（Model）

- DOM 将文档表示为一棵节点树（类似家谱树），用 “父子”“兄弟” 等关系描述元素间的层次结构：
  - 根元素是 `<html>`，所有其他元素都是其后代；
  - 节点树清晰展示了元素的嵌套关系，便于通过 JS 遍历和操作。

## 节点（Node）

DOM 文档由多种节点组成，核心类型包括：

### 元素节点（Element Node）

- 文档的基本构成单位，对应 HTML 标签（如 `<div>`、`<p>`）。
- 特点：可包含其他元素节点或文本节点，是节点树的 “骨架”。
- 根元素：`<html>` 是唯一不被其他元素包含的元素节点。

### 文本节点（Text Node）

- 包含文本内容（如文字、空格），**总是被元素节点包含**（如 `<p>Hello</p>` 中，“Hello” 是文本节点）。
- 注意：并非所有元素节点都包含文本节点（如空标签 `<img>`）。

### 属性节点（Attribute Node）

- 描述元素的附加信息（如 `class`、`id`、`src`），**仅存在于元素的起始标签中**。
- 特点：依赖元素节点存在，无法独立于元素存在（如 `<a href="url">` 中，`href` 是属性节点）。

## CSS 与 DOM 的关联

- CSS 通过节点树结构应用样式，子元素会继承父元素的样式（继承性）。
- 为精准定位元素，常用 `class` 和 `id` 属性：
  - **class 属性**：
    - 可在多个元素上重复使用，用于为一组元素定义相同样式（如 `.active { color: red; }`）。
    - 一个元素可包含多个类名（用空格分隔，如 `class="btn primary"`）。
  - **id 属性**：
    - 每个 `id` 在文档中唯一，用于标识单个元素（如 `id="logo"`）。
    - 可作为样式或 DOM 操作的 “挂钩”（如 `#logo { width: 100px; }`）。

## 获取元素节点的 DOM 方法

### `getElementById()`

- **作用**：根据元素的 `id` 属性值获取唯一元素节点。

- 语法：

  ```
  document.getElementById("idValue")
  ```

  - 参数：`id` 值（必须用引号包裹）；
  - 返回值：匹配的元素节点对象（若不存在则返回 `null`）。

- 示例：

  ```js
  const header = document.getElementById("main-header"); // 获取 id 为 "main-header" 的元素
  ```

### `getElementsByTagName()`

- **作用**：根据标签名获取所有匹配的元素节点，返回 **HTMLCollection（类数组对象）**。

- 语法：

  ```
  element.getElementsByTagName("tagName")
  ```

  - 参数：标签名（如 `"div"`、`"p"`），或通配符 `"*"`（匹配所有元素）；
  - 返回值：包含所有匹配元素的集合（即使只有一个元素，也返回集合）。

- 示例：

  ```js
  const paragraphs = document.getElementsByTagName("p"); // 获取所有 <p> 元素
  const allElements = document.getElementsByTagName("*"); // 获取所有元素
  ```

### `getElementsByClassName()`

- **作用**：根据 `class` 属性值获取所有匹配的元素节点，返回 **HTMLCollection**。

- 语法：

  ```
  element.getElementsByClassName("className")
  ```

  - 参数：类名（多个类名用空格分隔，如 `"btn active"`）；
  - 特点：忽略类名顺序，只要元素包含所有指定类名即匹配。

- 示例：

  ```js
  const activeItems = document.getElementsByClassName("active"); // 获取所有 class 含 "active" 的元素
  const specialBtns = document.getElementsByClassName("btn special"); // 匹配同时含 "btn" 和 "special" 的元素
  ```

## 获取和设置属性

### `getAttribute()`

- **作用**：获取元素节点的指定属性值。

- 语法：

  ```
  element.getAttribute("attributeName")
  ```

  - 参数：属性名（如 `"href"`、`"class"`）；
  - 注意：**只能通过元素节点调用**（不属于 `document` 对象）。

- 示例：

  ```js
  const link = document.getElementById("nav-link");
  const url = link.getAttribute("href"); // 获取 link 的 href 属性值
  ```

### `setAttribute()`

- **作用**：修改或添加元素节点的属性值。

- 语法：

  ```
  element.setAttribute("attributeName", "newValue")
  ```

  - 参数：属性名和新值；
  - 特点：修改后会实时反映在页面中，但 **不会改变原始 HTML 源代码**（DOM 动态刷新的特性）。

- 示例：

  ```js
  const img = document.getElementById("logo");
  img.setAttribute("src", "new-logo.png"); // 修改 img 的 src 属性
  img.setAttribute("alt", "New Logo"); // 添加或修改 alt 属性
  ```

## 补充说明

- DOM 操作是 “动态” 的：通过 JS 修改的内容会实时更新页面，但不会改变服务器返回的原始 HTML 代码（查看源代码时仍为初始状态）。
- 类数组对象（如 `HTMLCollection`）是动态的：当文档结构变化时，集合会自动更新（如删除一个元素后，集合长度会减少）。
- 现代 DOM API 扩展：除上述方法外，还有 `querySelector()` 和 `querySelectorAll()` 等更灵活的方法（支持 CSS 选择器），例如 `document.querySelector("#main .item")`。
