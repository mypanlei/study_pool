---
title: "Agent to Agent（A2A）一文全了解"
source: "https://juejin.cn/post/7491231635868090394"
author:
  - "MervynZ"
published: 2025-04-09
created: 2026-06-18
source_type: article
description: "Agent to Agent（A2A）是 Google 推出的一种开放协议，旨在让不同框架和供应商的 AI Agents 能够互相通信和协作。"
tags:
  - source
  - agent
  - protocol
  - google
  - a2a
  - multi-agent
---
> A2A协议由Google于2025年4月9日开源发布，目前仍在不断调整中。

## 什么是代理对代理？

Agent to Agent（A2A）是 Google 最近推出的一种开放协议，旨在让不同框架和供应商的 AI Agent 能够互相通信和协作。AI Agents 是能够自主执行任务的系统，比如搜索信息或处理客服查询。A2A 让这些 Agent 能够发现全局、共享能力，并在安全的环境中良好工作，类似于 USB 或蓝牙让不同品牌的设备互联。

例如，一个熟练搜索的智能体可以与熟练总结的智能体合作，完成从信息收集到摘要生成的全过程。这种协作对用户透明，提升了任务效率。

---

## 代理到代理要解决什么问题？

在人工智能领域，AI Agent的快速发展带来了新的可能性。这些Agent能够自主执行任务、做出决策，并与环境交互，通常依赖大型语言模型（LLM）等技术。然而，随着Agent数量和种类的增加，一个显着的问题浮现：不同供应商或框架构建的AI Agent之间缺乏有效的通信和协作方式。这限制了它们在复杂、多步骤任务中的应用潜力。

为了解决这个问题，Google 于 2025 年 4 月 9 日推出了 Agent2Agent（A2A）协议，这一开放标准旨在让 AI Agent 实现跨框架和供应商的互操作性。A2A 的目标是建立一个通用的通信语言，让 Agent 能够发现多样性、展示能力、协调任务，并在安全的环境中协作。

使用A2A，代理能够在不共享记忆、思维或工具的情况下完成终端用户的任务。取而代之的是，智能体通过各自相互结合的方式交换上下文、状态、指令和数据。

- 简洁：复用现有标准
- 针对企业：支持身份认证、安全性、隐私保护、仓储追踪与监控
- 优先优先：支持（非常）长时间运行的任务和人类参与的流程
- 模态关联：支持文本、音频视频、表单、iframe等多种交互形式
- 黑盒执行：智能体消耗共享思考过程、计划或工具

---

## A2A的工作原理

A2A协议的核心是通过以下步骤实现Agents间的通信：

- **发现机制** ：允许Agent通过标准化的方式发现其他Agent的存在，构成网络中的DNS发现设备。每个Agent都有一个公开的Agent卡文件（位于 `/.well-known/agent.json` ），包含能力、技能和通信端点，每个Agent可以公布自己的技能，例如“搜索信息”、“汇总文本”或“处理图像”，其他Agent根据任务需求选择合作伙伴。
- **任务管理** ：任务是工作的核心单元，有唯一ID，状态包括提交、中、需要处理、完成、失败或取消。确保协作流程不止。
- **消息和内容** ：通过消息进行通信，消息包含文本、文件或格式化数据（部分），角色标记为“用户”或“代理”。
- **流式传输和自适应** ：支持长时间任务的流式更新（通过 Server-Sent Events）和自适应通知（通过 Webhook URL）。

### 参与者（演员）

A2A协议包含三个核心参与者：

- **用户（User）：** 使用智能体系统完成任务的终端用户（可以是人类，也可以是服务）。
- **客户端（Client）：** 代表用户向一个“黑盒”智能体发起任务请求的实体（可以是服务、代理或应用）。
- **远程** **智能** **体/服务器（Remote Agent / Server）：** 黑盒智能体，即A2A协议的服务端。

### 传输方式（Transport）

A2A协议使用 **HTTP** 作为客户端与远程智能体之间的传输协议。根据客户端与远程智能体的能力，它们还可以使用 **SSE** **（Server-Sent Events）** 来支持服务器向客户端主动实时更新的流式通信。

在客户端与远程智能体之间的数据交换格式，A2A协议还是采用 **JSON-RPC 2.0** 。

### 异步通信（Async）

A2A客户端与服务端可以使用标准的请求/响应模式，并通过轮询获取更新。但是，A2A也支持更高效的异步通信方式：

- 当客户端出现连接状态时，可以通过 **SSE** **（Server-Sent Events）** 接收实时流式更新；
- 当客户端处于断开状态时，也可以通过 **主动通知** 接收异步更新。

这使得A2A能够灵活配置各种任务持续时间和网络状态下的通信需求。

### 身份验证与授权（Authentication and Authorization）

A2A将Agents建模为企业级应用（由于A2A智能体是“黑盒”的，不共享工具和资源，因此适用），这使得Agents间互操作迅速具备企业级能力。

- **身份验证** **规范** ： A2A 遵循 OpenAPI 的身份验证规范进行认证。值得注意的是，A2A 协议中 **不会在协议中交换身份信息** 。代理应 **通过带外（out-of-band）方式** 获取认证信息（如 Token），并通过 **HTTP Header** 传递这些信息，而不是在 A2A Payload 中传输。
- **服务器身份要求声明** ： 尽管 A2A 不在协议内直接传输身份信息，但服务端会在 A2A Payload 中声明其认证要求。至少，服务端应在其 **Agent Card** 中公开其身份认证要求。
- **客户端认证流程** ： 客户端应选择服务端公布的一种认证协议完成身份认证，并获取认证材料。服务端应对每个请求进行身份验证，并使用标准 HTTP 状态码（如 `401 Unauthorized` 、 `403 Forbidden` ）以及认证协议特定的 Header 与响应体进行响应（例如通过 `WWW-Authenticate` Header 提示所需认证方案，或在某个 well-known 路径下提供 OIDC 发现文档）。更多细节可参考 Enterprise Ready 章节。
- **运行中追加认证** ： 若智能体在任务执行过程中需要客户端/用户提供额外的认证信息（例如访问某个工具所需权限），则应返回一个任务状态为 `Input-Required` 的响应，并在 Payload 中携带一个 Authentication 结构。此时客户端也应通过带外方式获取新的认证材料。

这套机制确保了 A2A 在不暴露身份信息的前提下，仍可安全、标准地支持企业级身份验证与权限管理。

### Agent Card

支持 A2A 协议的远程智能体必须以 **JSON 格式** 发布一份 **Agent Card（智能体卡片）** ，用于描述该智能体的能力（capabilities/skills）以及身份认证机制。

客户端会使用 Agent Card 中的信息来：

- 判断该智能体是否具备完成某项任务的能力；
- 获取所需的身份认证方式；
- 并基于 A2A 协议与该远程智能体建立通信。

### 发现机制（Discovery）

A2A 协议让 Agent 能够互相发现，是整个 A2A 协议中最基础也是最关键的环节。每个 Agent 公开一个 JSON 文件，称为 Agent Card，位于 `https://<base-url>/.well-known/agent.json` ，包含能力、技能和通信端点。客户端通过 HTTP 请求获取此文件，了解 Agent 功能并选择合适的合作伙伴。

- 一个 Agent 需要找到另一个它想要与之通信的 Agent。
- 发现机制不是 A2A 协议本身强制规定的，可以有多种实现方式，例如：
	- 通过用户手动操作（如扫描二维码、点击链接）。
		- 通过共享的发现服务（类似通讯录）。
		- 通过物理邻近（如使用蓝牙、Wi-Fi Direct 等底层技术，虽然 A2A 主要面向 Web）。
- 发现过程的目标是让两个 Agent 能够交换初始的连接信息（比如对方的公钥或一个临时的连接标识符）。

### 表示格式（Representation）

以下是 Agent Card 的推荐 JSON 表示结构（示意）：

```ts
代码解读复制代码// AgentCard 用于传达关键信息：
// - 基本信息（版本、名称、描述、用途）
// - 技能：智能体可以执行的一组能力
// - 智能体默认支持的模态/内容类型
// - 认证需求
interface AgentCard {
  // 智能体的可读名称。
  // 例如："菜谱助手"
  name: string;
  
  // 智能体的可读描述，用于帮助用户和其他智能体理解其功能。
  // 例如："一个帮助用户查找菜谱和烹饪的智能体。"
  description: string;

  // 智能体的服务地址 URL。
  url: string;

  // 智能体的服务提供方信息。
  provider?: {
    organization: string; // 提供方组织名称
    url: string;          // 提供方主页 URL
  };

  // 智能体的版本，格式由提供方自行定义。例如："1.0.0"
  version: string;

  // 智能体的文档地址（可选）。
  documentationUrl?: string;

  // 智能体支持的可选能力。
  capabilities: {
    streaming?: boolean; // 是否支持 SSE 流式更新
    pushNotifications?: boolean; // 是否支持推送通知
    stateTransitionHistory?: boolean; // 是否暴露任务状态变化的历史记录
  };

  // 智能体的身份认证需求。
  // 结构与 OpenAPI 的认证规范一致。
  authentication: {
    schemes: string[]; // 例如：Basic、Bearer 等认证方式
    credentials?: string; // 若为私有卡片，客户端应使用的凭证
  };

  // 智能体在所有技能中支持的默认交互模式。
  // 可在技能中进行覆盖。
  defaultInputModes: string[];  // 支持的输入 MIME 类型
  defaultOutputModes: string[]; // 支持的输出 MIME 类型

  // 技能是智能体可以执行的最小能力单元。
  skills: {
    id: string; // 技能的唯一标识符
    name: string; // 技能的可读名称

    // 技能的描述，用于客户端或人类理解技能功能。
    description: string;

    // 一组标签，用于描述该技能所属的能力类别
    // 例如："烹饪"、"客服支持"、"账单处理"
    tags: string[];

    // 技能可执行的示例场景。
    // 用于帮助客户端理解技能的使用方式。
    // 例如："我需要一个做面包的食谱"
    examples?: string[]; // 示例任务提示语

    // 技能支持的交互模式（如果不同于默认设置）
    inputModes?: string[];  // 支持的输入 MIME 类型
    outputModes?: string[]; // 支持的输出 MIME 类型
  }[];
}
```

### Agent-to-Agent 通信（智能体间通信）

客户端与远程智能体之间的通信是围绕 **任务完成** 而展开的，多个智能体可以协同合作，以满足最终用户的请求。 在 A2A 协议中， **Task（任务）对象** 是客户端与远程智能体协同完成任务的核心载体。

##### 任务执行模型

- **即时完成** ：某些任务由远程智能体接收后可以立即完成并返回结果。
- **长时间运行** ：对于耗时较长的任务，客户端可以通过轮询（polling）方式，周期性地向智能体请求任务最新状态。
- **推送更新** ：如果客户端与远程智能体保持连接，智能体也可以通过 **SSE** **（Server-Sent Events）** 向客户端实时推送任务状态更新。若客户端处于离线状态，也可以通过外部通知服务向其推送更新。

### 核心对象（Core Objects）

#### 任务（Task）

任务是一个有状态的实体，允许客户端和远程 Agent 达成特定结果并生成结果。客户端和远程 Agent 在任务中交换消息。远程 Agent 生成结果作为制品。

任务总是由客户端创建，状态总是由远程 Agent 确定。如果客户端需要，多个任务可以作为一个共同会话的一部分（通过可选的 sessionId 标识）。为此，客户端在创建任务时设置可选的 sessionId。

Agent 可以：

- 立即完成请求
- 将工作安排到后续时间
- 拒绝请求
- 协商不同的方式
- 向客户端请求更多信息
- 委托给其他 Agent 和系统 即使目标已经完成，客户端仍然可以请求更多信息或在同一任务的上下文中进行更改。（例如，客户端：“画一只兔子的画”，Agent：“<画>”，客户端：“把它弄成红色”）。

任务用于传输制品（结果）和消息（思想、指令、其他内容）。任务维护一个状态和可选的状态及消息历史记录。

```ts
代码解读复制代码// 任务
interface Task {
  id: string; // 任务的唯一标识符
  sessionId: string; // 客户端为持有任务的会话生成的 id
  status: TaskStatus; // 任务的当前状态
  history?: Message[];
  artifacts?: Artifact[]; // 由 Agent 创建的制品集合
  metadata?: Record<string, any>; // 扩展元数据
}

// 任务状态及附带的消息
interface TaskStatus {
  state: TaskState;
  message?: Message; // 客户端的额外状态更新
  timestamp?: string; // ISO 日期时间值
}

// 服务器在 sendSubscribe 或 subscribe 请求期间发送
interface TaskStatusUpdateEvent {
  id: string;
  status: TaskStatus;
  final: boolean; // 表示事件流的结束
  metadata?: Record<string, any>;
}

// 服务器在 sendSubscribe 或 subscribe 请求期间发送
interface TaskArtifactUpdateEvent {
  id: string;
  artifact: Artifact;
  metadata?: Record<string, any>;
}

// 客户端发送给 Agent 创建、继续 或者 重试任务
interface TaskSendParams {
  id: string;
  sessionId?: string; // 服务器为新任务创建新的 sessionId（如果未设置）
  message: Message;
  historyLength?: number; // 要检索的最近消息数量
  pushNotification?: PushNotificationConfig; // 断开连接时服务器发送通知的配置
  metadata?: Record<string, any>; // 扩展元数据
}

// 任务状态类型
type TaskState =
  | "submitted"
  | "working"
  | "input-required"
  | "completed"
  | "canceled"
  | "failed"
  | "unknown";
```

#### 制品（Artifact）

Agent 生成制品作为任务的最终结果。制品是不可变的，可以命名，并且可以包含多个部分。流响应可以将部分附加到现有的制品。

一个任务可以生成多个制品。例如，“创建网页”可能生成单独的 HTML 和图像制品。

```ts
代码解读复制代码interface Artifact {
  name?: string;
  description?: string;
  parts: Part[];
  metadata?: Record<string, any>;
  index: number;
  append?: boolean;
  lastChunk?: boolean;
}
```

#### 消息（Message）

消息包含任何不是制品的内容。它可以包括 Agent 的思维、用户上下文、指令、错误、状态或元数据等内容。

所有来自客户端的内容都是以消息的形式发送的。Agent 发送消息以传达状态或提供指令（而生成的结果作为制品发送）。

消息可以有多个部分，以表示不同的内容。例如，用户请求可能包括用户的文本描述，然后是多个文件，作为客户端的上下文。

```ts
代码解读复制代码interface Message {
  role: "user" | "agent";
  parts: Part[];
  metadata?: Record<string, any>;
}
```

#### Part

Part 是客户端和远程 Agent 交换的完全形成的内容，作为消息或制品的一部分。每个部分都有自己的内容类型和元数据。

```ts
代码解读复制代码interface TextPart {
  type: "text";
  text: string;
}

interface FilePart {
  type: "file";
  file: {
    name?: string;
    mimeType?: string;
    // oneof {
    bytes?: string; // base64 编码的内容
    uri?: string;
    //}
  };
}

interface DataPart {
  type: "data";
  data: Record<string, any>;
}

type Part = (TextPart | FilePart | DataPart) & {
  metadata: Record<string, any>;
};
```

#### 推送通知（Push Notifications）

A2A 支持一种安全的通知机制，Agent 可以通过 PushNotificationService 在连接会话外部通知客户端更新。在企业内外，Agent 验证通知服务的身份、与服务进行身份验证，并呈现一个标识符，将通知与正在执行的任务关联起来是至关重要的。

PushNotificationService 的目标服务器应视为一个独立的服务，并且不保证（甚至不期望）直接是客户端。此 PushNotificationService 负责验证和授权 Agent，并将已验证的通知 Agent 到适当的端点（可以是 pub/sub 队列、电子邮件收件箱或其他服务等）。

对于具有孤立的客户端-Agent 对的虚拟场景（例如，在受限的 VPC 中的本地服务网格等）或没有企业安全问题的孤立环境，客户端可以选择简单地打开端口并充当其自己的 PushNotificationService。任何企业实现很可能会有一个集中式服务，用于使用受信任的通知凭据验证远程 Agent，并可以处理在线/离线场景。（这应类似于移动推送通知服务）。

```ts
代码解读复制代码interface PushNotificationConfig {
  url: string;
  token?: string; // 此任务/会话的唯一标识符
  authentication?: {
    schemes: string[];
    credentials?: string;
  };
}

interface TaskPushNotificationConfig {
  id: string; // 任务 id
  pushNotificationConfig: PushNotificationConfig;
}
```

## 简单示例

### Agent Card

```json
代码解读复制代码{
  "name": "Google Maps Agent",
  "description": "Plan routes, remember places, and generate directions",
  "url": "https://maps-agent.google.com",
  "provider": {
    "organization": "Google",
    "url": "https://google.com"
  },
  "version": "1.0.0",
  "authentication": {
    "schemes": "OAuth2"
  },
  "defaultInputModes": ["text/plain"],
  "defaultOutputModes": ["text/plain", "application/html"],
  "capabilities": {
    "streaming": true,
    "pushNotifications": false
  },
  "skills": [
    {
      "id": "route-planner",
      "name": "Route planning",
      "description": "Helps plan routing between two locations",
      "tags": ["maps", "routing", "navigation"],
      "examples": [
        "plan my route from Sunnyvale to Mountain View",
        "what's the commute time from Sunnyvale to San Francisco at 9AM",
        "create turn by turn directions from Sunnyvale to Mountain View"
      ],
      // can return a video of the route
      "outputModes": ["application/html", "video/mp4"]
    },
    {
      "id": "custom-map",
      "name": "My Map",
      "description": "Manage a custom map with your own saved places",
      "tags": ["custom-map", "saved-places"],
      "examples": [
        "show me my favorite restaurants on the map",
        "create a visual of all places I've visited in the past year"
      ],
      "outputModes": ["application/html"]
    }
  ]
}
```

### 发送任务

允许客户端完成向远程代理发送内容，以启动新任务、恢复中断的任务或重新打开已的任务。任务中断可能是由于代理需要额外的用户输入或运行时错误引起的。

```json
代码解读复制代码//Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method":"tasks/send",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "message": {
      "role":"user",
      "data": [{
        "type":"text",
        "text": "tell me a joke"
      }]
    },
    "metadata": {}
  }
}
//Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "status": {
      "state": "completed",
    },
    "artifacts": [{
      "name":"joke",
      "parts": [{
          "type":"text",
          "text":"Why did the chicken cross the road? To get to the other side!"
        }]
      }],
    "metadata": {}
  }
}
```

### 获取任务

客户端可以使用此方法搜索任务生成的产品。Agent决定先前提交给它的任务的保留窗口。对于超出Agent保留窗口的任务或生命周期短且未持久化的任务，Agent可能会返回错误代码。

客户端还可以请求任务的最后 N 条历史记录，这将包括按顺序发送的所有消息，包括客户端和服务器的消息。默认情况下，为 0（没有历史记录）。

```json
代码解读复制代码//Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method":"tasks/get",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "historyLength": 10,
    "metadata": {}
  }
}
//Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "status": {
      "state": "completed"
    },
    "artifacts": [{
      "parts": [{
        "type":"text",
        "text":"Why did the chicken cross the road? To get to the other side!"
      }]
    }],
    "history":[
      {
        "role": "user",
        "parts": [
          {
            "type": "text",
            "text": "tell me a joke"
          }
        ]
      }
    ],
    "metadata": {}
  }
}
```

### 取消任务

客户端可以选择先前取消提交的任务。

```json
代码解读复制代码//Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method":"tasks/cancel",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "metadata": {}
  }
}
//Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": 1,
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "status": {
      "state": "canceled"
    },
    "metadata": {}
  }
}
```

### 设置任务主动通知

客户端可以配置一个分组通知URL，用于接收任务状态变更的更新。

```json
代码解读复制代码//Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method":"tasks/pushNotification/set",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "pushNotificationConfig": {
      "url": "https://example.com/callback",
      "authentication": {
        "schemes": ["jwt"]
      }
    }
  }
}
//Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "pushNotificationConfig": {
      "url": "https://example.com/callback",
      "authentication": {
        "schemes": ["jwt"]
      }
    }
  }
}
```

### 获取任务主动通知

客户端可以使用此方法搜索当前配置的任务通知配置。

```json
代码解读复制代码//Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method":"tasks/pushNotification/get",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64"
  }
}
//Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "pushNotificationConfig": {
      "url": "https://example.com/callback",
      "authentication": {
        "schemes": ["jwt"]
      }
    }
  }
}
```

### 多轮对话

如果任务需要额外的用户输入，它可能会暂停并等待在远程Agent上执行。当任务出现“需要输入”（需要输入）状态时，客户端需要提供额外的输入，以便任务能够继续在远程Agent上处理。

在“需要输入”状态中包含的消息必须包括指示客户端需要执行的操作的详细信息。例如，“填写表格”或“登录到 SaaS 服务 foo”。如果这包括格式化数据，指令应作为一个部分发送，格式化数据作为第二个部分发送。

```json
代码解读复制代码//Request - seq 1
{
  "jsonrpc": "2.0",
  "id": 1,
  "method":"tasks/send",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "message": {
      "role":"user",
      "parts": [{
        "type":"text",
        "text": "request a new phone for me"
      }]
    },
    "metadata": {}
  }
}
//Response - seq 2
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "status": {
      "state": "input-required",
      "message": {
        "parts": [{
          "type":"text",
          "text":"Select a phone type (iPhone/Android)"
        }]
      }
    },
    "metadata": {}
  }
}
//Request - seq 3
{
  "jsonrpc": "2.0",
  "id": 2,
  "method":"tasks/send",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "message": {
      "role":"user",
      "parts": [{
        "type":"text",
        "text": "Android"
      }]
    },
    "metadata": {}
  }
}
//Response - seq 4
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "id": 1,
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "status": {
      "state": "completed"
    },
    "artifacts": [{
      "name": "order-confirmation",
      "parts": [{
          "type":"text",
          "text":"I have ordered a new Android device for you. Your request number is R12443"
        }],
      "metadata": {}
    }],
    "metadata": {}
  }
}
```

### 流式支持

对于能够通过 HTTP 和 SSE 通信的客户端和远程代理，客户端可以在创建新任务时使用方法 `tasks/sendSubscribe` 发送 RPC 请求。远程代理可以通过任务状态更新事件（ `TaskStatusUpdateEvents` ）流式响应（用于传输状态变更或指令/请求）和任务产品更新事件（ `TaskArtifactUpdateEvents` 请注意， `TaskArtifactUpdateEvents` 可以将新部分附加到现有产品。客户端可以使用 `task/get` 在流式传输外部检索整个产品。代理在流结束时必须设置 `final: true` 属性，或者如果代理被中断并需要额外的用户输入时。

```json
代码解读复制代码//Request
{
  "method":"tasks/sendSubscribe",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "message": {
      "role":"user",
      "parts": [{
        "type":"text",
        "text": "write a long paper describing the attached pictures"
      },{
        "type":"file",
        "file": {
           "mimeType": "image/png",
           "data":"<base64-encoded-content>"
        }
      }]
    },
    "metadata": {}
  }
}

//Response
data: {
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": 1,
    "status": {
      "state": "working",
      "timestamp":"2025-04-02T16:59:25.331844"
    },
    "final": false
  }
}

data: {
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": 1,    
    "artifact": [
      "parts": [
        {"type":"text", "text": "<section 1...>"}
      ],
      "index": 0,
      "append": false,      
      "lastChunk": false
    ]
  }
}
data: {
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": 1,  
    "artifact": [
      "parts": [
        {"type":"text", "text": "<section 2...>"}
      ],
      "index": 0,
      "append": true,      
      "lastChunk": false
    ]
  }
}
data: {
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": 1,    
    "artifact": [
      "parts": [
        {"type":"text", "text": "<section 3...>"}
      ],
      "index": 0,
      "append": true,
      "lastChunk": true
    ]
  }
}

data: {
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": 1,
    "status": {
      "state": "completed",
      "timestamp":"2025-04-02T16:59:35.331844"
    },
    "final": true
  }
}
```

### 重新订阅任务

断开连接的客户端可以重新订阅支持流式传输的远程代理，通过SSE接收任务更新。

```json
代码解读复制代码//Request
{
  "method":"tasks/resubscribe",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "metadata": {}
  }
}
//Response
data: {
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "artifact":[
      "parts": [
        {"type":"text", "text": "<section 2...>"}
      ],
      "index": 0,
      "append": true,
      "lastChunk":false
    ]
  }
}
data: {
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "artifact":[
      "parts": [
        {"type":"text", "text": "<section 3...>"}
      ],
      "index": 0,
      "append": true,
      "lastChunk": true
    ]   
  }
}

data: {
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": 1,
    "status": {
      "state": "completed",
      "timestamp":"2025-04-02T16:59:35.331844"
    },
    "final": true
  }
}
```

### 文本非媒体

以下是客户端和代理之间包含非文本数据的交互示例。

```json
代码解读复制代码//Request - seq 1
{
  "jsonrpc": "2.0",
  "id": 9,
  "method":"tasks/send",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "message": {
      "role":"user",
      "parts": [{
        "type":"text",
        "text": "Analyze the attached report and generate high level overview"
      },{
        "type":"file",
        "file": {
           "mimeType": "application/pdf",
           "data":"<base64-encoded-content>"
        }
      }]
    },
    "metadata": {}
  }
}
//Response - seq 2
{
  "jsonrpc": "2.0",
  "id": 9,
  "result": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "status": {
      "state": "working",
      "message": {
        "role": "agent",
        "parts": [{
          "type":"text",
          "text":"analysis in progress, please wait"
        }],
        "metadata": {}
       }
     },
    "metadata": {}
  }
}
//Request - seq 3
{
  "jsonrpc": "2.0",
  "id": 10,
  "method":"tasks/get",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "metadata": {}
  }
}
//Response - seq 4
{
  "jsonrpc": "2.0",
  "id": 9,
  "result": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "status": {
      "state": "completed"
     },
    "artifacts": [{
      "parts": [{
        "type":"text",
        "text":"<generated analysis content>"
       }],
       "metadata": {}
     }],
    "metadata": {}
  }
}
```

### 形成输出

客户端和代理都可以请求对方提供格式输出。

```json
代码解读复制代码//Request
{
  "jsonrpc": "2.0",
  "id": 9,
  "method":"tasks/send",
  "params": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "message": {
      "role":"user",
      "parts": [{
        "type":"text",
        "text": "Show me a list of my open IT tickets",
        "metadata": {
          "mimeType": "application/json",
          "schema": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "ticketNumber": { "type": "string" },
                "description": { "type": "string" }
              }
            }
          }
        }
      }]
    },
    "metadata": {}
  }
}
//Response
{
  "jsonrpc": "2.0",
  "id": 9,
  "result": {
    "id": "de38c76d-d54c-436c-8b9f-4c2703648d64",
    "sessionId": "c295ea44-7543-4f78-b524-7a38915ad6e4",
    "status": {
      "state": "working",
      "message": {
        "role": "agent",
        "parts": [{
            "type":"text",
            "text":"[{"ticketNumber":"REQ12312","description":"request for VPN access"},{"ticketNumber":"REQ23422","description":"Add to DL - team-gcp-onboarding"}]"
        }],
        "metadata": {}
      }
    },
    "metadata": {}
  }
}
```

### 错误处理

以下是服务器在处理客户端请求时遇到错误时，响应客户端的 `ErrorMessage` 格式。

```ts
代码解读复制代码interface ErrorMessage {
  code: number;
  message: string;
  data?: any;
}
```

以下是服务器在错误场景中可以响应的标准 JSON-RPC 错误代码：

| 错误代码 | 消息 | 描述 |
| --- | --- | --- |
| \-32700 | JSON 解析错误 | 发送的 JSON 无效 |
| \-32600 | 无效请求 | 请求有效负载验证错误 |
| \-32601 | 方法未找到 | 不是有效的方法 |
| \-32602 | 参数无效 | 方法参数无效 |
| \-32603 | 内部错误 | 内部 JSON-RPC 错误 |
| \-32000 ~ -32099 | 服务器错误 | 保留用于实现特定的错误代码 |
| \-32001 | 任务未找到 | 提供的 id 缺少任务 |
| \-32002 | 任务无法取消 | 远程Agent无法取消任务 |
| \-32003 | 不支持全民通知 | 座席不支持主动通知 |
| \-32004 | 不支持的操作 | 操作不被支持 |
| \-32005 | 不兼容的内容类型 | 客户端和代理之间的内容类型不兼容 |