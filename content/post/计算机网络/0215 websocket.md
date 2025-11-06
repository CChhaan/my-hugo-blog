---
# 文章标题
title: 2.15 WebSocket
# 文章内容摘要
# description:
# 文章内容关键字
keywords: HTTP 轮询, 长轮询, WebSocket 协议, WebSocket 握手, 全双工通信, HTTP 半双工, 实时通信, WebSocket 数据帧, payload 数据结构, Connection Upgrade, Upgrade WebSocket, Sec-WebSocket-Key, 服务器推送, 前端实时更新, 扫码登录, 消息队列长轮询, TCP 粘包问题, WebSocket 消息格式, 实时消息传输, HTTP 与 WebSocket 区别
# 发表日期
date: 2025-09-25
summary: 本节详细介绍了 WebSocket 的原理、使用场景、分类以及 WebSocket 的消息格式。
# 分类
categories:
  - 计算机网络
# 标签
tags:
  - 计算机基础
  - 计算机网络
  - WebSocket
---

## 使用 HTTP 不断轮询

**轮询（Polling）**：前端代码不断定时向服务器发送 HTTP 请求，服务器收到请求后返回消息。

这种方式是一种“伪服务器推送”，实际上是 **客户端主动请求**，服务器被动响应。

应用场景：常见于 **扫码登录** 等需要实时更新页面状态的场景。

问题：

- 打开 F12 调试工具时，会看到大量 HTTP 请求，请求虽小但**消耗带宽**，同时**增加服务器负担**。
- 用户体验问题：若用户扫码后正好错过下一次请求，需等待 **1~2 秒** 才触发跳转，造成**明显卡顿**。

## 长轮询

客户端发起 HTTP 请求，并设置较长超时时间（例如 **30 秒**）。服务器在这段时间内若收到数据（如扫码请求），立即返回响应，若超时，则客户端**立刻发起下一次请求**。

**减少请求次数**，**响应及时**，大多数情况下能在超时前获取到数据。

此机制也称为“长轮询机制”。常用于 **消息队列（如 RocketMQ）** 中消费者取数据的方式。

本质上仍是 **客户端主动取数据**，并非真正的服务器推送。

## WebSocket 是什么

**WebSocket** 是一种 **全双工通信协议**，双方可在同一时间内**主动向对方发送数据**。

HTTP/1.1 属于 **半双工**，只能客户端先请求、服务器再响应。WebSocket 基于 TCP，为了解决这一限制而设计。

### WebSocket 连接的建立

浏览器与服务器完成 **TCP 三次握手** 后，统一使用 **HTTP 协议** 进行第一次通信。

若为普通 HTTP 请求，则继续保持 HTTP 通信。

若要建立 WebSocket 连接，则在 HTTP 请求头中添加：

- `Connection: Upgrade`（请求升级协议）
- `Upgrade: WebSocket`（升级为 WebSocket）
- `Sec-WebSocket-Key`（随机生成的 base64 编码）

若服务器支持 WebSocket，则：

- 返回状态码 **101（Switching Protocols）**；
- 在响应头 `Sec-WebSocket-Accept` 中，放入基于客户端 `Sec-WebSocket-Key` 计算得到的字符串。

浏览器用相同算法转换 base64 字符串，若与服务器返回的一致，则握手成功。

至此，WebSocket 连接建立完成，双方可直接使用 WebSocket 数据格式进行通信。

### WebSocket 的消息格式

WebSocket 的数据单元称为 **帧（Frame）**。

**opcode 字段**：标识数据帧类型。

**payload 字段**：存放数据长度（单位：字节）。最开始的 **7 bit** 为标志位，根据取值判断是否继续读取 **16 bit** 或 **64 bit** 长度字段。

**payload data 字段**：存放实际要传输的数据，根据 payload 长度截取相应字节。

WebSocket 数据格式为：**数据头（含 payload 长度） + payload data**。

设计原因：**TCP 是全双工协议**，但直接传输数据会产生 **粘包问题**；为解决粘包，上层协议采用 **消息头 + 消息体** 格式；消息头中记录消息体长度，接收端可据此准确截取完整数据。
