---
# 文章标题
title: 2.5 更新 state 中的数组
# 文章内容摘要
# description: 本文详细介绍了 Git 这一分布式版本控制系统的优点，对比了 Windows 与 macOS/Linux 系统下的常用命令，讲解了 vim 操作模式及常用命令，还阐述了 Git 的基本配置、特定项目配置和命令缩写设置等内容。
# 文章内容关键字
keywords: React 数组更新, React state 不可变, React 更新数组方法, React 不可变数据, 更新数组内部对象, React 使用 map 更新数组, React 使用 filter 删除元素, React 使用 slice 插入元素, React 展开语法更新数组, React 避免 mutation, React 浅拷贝数组, React 深拷贝对象, React reverse sort 安全用法, 更新嵌套 state, Immer 更新 state, Immer draft Proxy, React state 最佳实践, 数组不可变更新示例, React 维护 state 纯函数, React 性能优化引用比较, React immutable array update, JavaScript 不可变更新技巧
# 发表日期
date: 2025-10-12
summary: 本文介绍了 React 中更新 state 中的数组的方法，包括在没有 mutation 的前提下更新数组、更新数组内部的对象、使用 Immer 编写简洁的更新逻辑等。
# 分类
categories:
  - React文档阅读
# 标签
tags:
  - react
  - 前端框架
  - 前端开发
  - 组件化开发
---

## 在没有 mutation 的前提下更新数组

数组是对象，需要将 React state 中的数组视为只读的。

每次更新数组时，都需要传入一个**新数组**。

使用不会修改原数组的方法生成新数组，如 `filter()`、`map()`。

`slice` 与 `splice` 的区别：

- **`slice`**：拷贝数组或数组的一部分。
- **`splice`**：**直接修改**原始数组（插入或删除元素）。

### 向数组中添加元素

创建一个**新数组**，包含原数组所有元素，以及新增元素。使用 `...` 数组展开语法。

展开语法也可将新元素放在 `...artists` 前，实现类似 `push()` 或 `unshift()` 的效果。

```js
setArtists([{ id: nextId++, name: name }, ...artists]);
```

### 从数组中删除元素

通过 **过滤出不需要删除的元素** 来生成新数组。使用 `filter()`。

```js
setArtists(artists.filter((a) => a.id !== artist.id));
```

### 转换数组

使用 `map()` 创建一个**新数组**。`map` 的回调根据元素值或索引返回新元素或原元素。

### 替换数组中的元素

不能使用 `arr[0] = 'bird'`，因为会直接修改数组。

使用 `map()` 根据索引来决定替换或保留元素。

### 向数组中插入元素

使用展开运算符 `...` + `slice()`。

插入步骤：取出插入点前的部分（`slice()`）；加入新元素；展开剩余部分。

### 其他改变数组的情况

`reverse()` 和 `sort()` 会直接修改原数组。

处理方式：**先拷贝**数组，再修改这个拷贝。

注意：

- 数组拷贝是**浅拷贝**，**不能直接修改拷贝中包含的对象**，否则仍会修改 state 中的对象。
- 解决方式：像更新嵌套对象一样，对需要修改的元素进行拷贝。

## 更新数组内部的对象

数组中的对象是数组“指向”的其他位置的值。**更新嵌套 state 时需要逐层创建拷贝，直到顶层。**

使用 `map` 替换旧对象为新对象。

**只应该直接修改“刚刚创建的对象”。**

## 使用 Immer 编写简洁的更新逻辑

适用情况：当没有 mutation 的前提下更新嵌套数组变得重复时。

通常不需要更新极深层级的 state，可考虑调整数据结构使其扁平化。不想调整结构时可使用 **Immer**。

## Immer 的特性

- 能够使用会产生 mutation 的语法，如 `artwork.seen = nextSeen`。
- 修改的是 **draft（Proxy）对象**，而非真实 state。
- `push()`、`pop()` 等修改数组的方法可以直接使用。
- Immer 会根据对 draft 的修改 **从头构建新的 state**，而不会修改现有 state。
