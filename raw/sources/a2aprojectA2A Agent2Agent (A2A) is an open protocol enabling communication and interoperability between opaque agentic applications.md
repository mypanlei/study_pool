---
title: "a2aproject/A2A: Agent2Agent (A2A) is an open protocol enabling communication and interoperability between opaque agentic applications."
source: "https://github.com/a2aproject/A2A"
author:
published:
created: 2026-06-18
description: "Agent2Agent (A2A) is an open protocol enabling communication and interoperability between opaque agentic applications. - a2aproject/A2A"
tags:
  - "clippings"
---
## Agent2Agent (A2A) Protocol

🌐 Language

[English](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=en) | [简体中文](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=zh-CN) | [繁體中文](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=zh-TW) | [日本語](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=ja) | [한국어](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=ko) | [हिन्दी](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=hi) | [ไทย](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=th) | [Français](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=fr) | [Deutsch](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=de) | [Español](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=es) | [Italiano](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=it) | [Русский](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=ru) | [Português](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=pt) | [Nederlands](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=nl) | [Polski](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=pl) | [العربية](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=ar) | [فارسی](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=fa) | [Türkçe](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=tr) | [Tiếng Việt](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=vi) | [Bahasa Indonesia](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=id) | [অসমীয়া](https://openaitx.github.io/view.html?user=a2aproject&project=A2A&lang=as)

## Agent2Agent (A2A) Protocol

**An open protocol enabling communication and interoperability between opaque agentic applications.**

The Agent2Agent (A2A) protocol addresses a critical challenge in the AI landscape: enabling gen AI agents, built on diverse frameworks by different companies running on separate servers, to communicate and collaborate effectively - as agents, not just as tools. A2A aims to provide a common language for agents, fostering a more interconnected, powerful, and innovative AI ecosystem.

With A2A, agents can:

- Discover each other's capabilities.
- Negotiate interaction modalities (text, forms, media).
- Securely collaborate on long-running tasks.
- Operate without exposing their internal state, memory, or tools.

## DeepLearning.AI Course

[![A2A DeepLearning.AI](https://camo.githubusercontent.com/17a0db316a9ce69566efaaedfd6c283333bcc47978c63d0c2e898f6302450aa4/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f3467596d305270375648632f6d617872657364656661756c742e6a7067)](https://goo.gle/dlai-a2a)

Join this short course on [A2A: The Agent2Agent Protocol](https://goo.gle/dlai-a2a), built in partnership with Google Cloud and IBM Research, and taught by [Holt Skinner](https://github.com/holtskinner), [Ivan Nardini](https://github.com/inardini), and [Sandi Besen](https://github.com/sandijean90).

**What you'll learn:**

- **Make agents A2A-compliant:** Expose agents built with frameworks like Google ADK, LangGraph, or BeeAI as A2A servers.
- **Connect agents:** Create A2A clients from scratch or using integrations to connect to A2A-compliant agents.
- **Orchestrate workflows:** Build sequential and hierarchical workflows of A2A-compliant agents.
- **Multi-agent systems:** Build a healthcare multi-agent system using different frameworks and see how A2A enables collaboration.
- **A2A and MCP:** Learn how A2A complements MCP by enabling agents to collaborate with each other.

## Why A2A?

As AI agents become more prevalent, their ability to interoperate is crucial for building complex, multi-functional applications. A2A aims to:

- **Break Down Silos:** Connect agents across different ecosystems.
- **Enable Complex Collaboration:** Allow specialized agents to work together on tasks that a single agent cannot handle alone.
- **Promote Open Standards:** Foster a community-driven approach to agent communication, encouraging innovation and broad adoption.
- **Preserve Opacity:** Allow agents to collaborate without needing to share internal memory, proprietary logic, or specific tool implementations, enhancing security and protecting intellectual property.

### Key Features

- **Standardized Communication:** JSON-RPC 2.0 over HTTP(S).
- **Agent Discovery:** Via "Agent Cards" detailing capabilities and connection info.
- **Flexible Interaction:** Supports synchronous request/response, streaming (SSE), and asynchronous push notifications.
- **Rich Data Exchange:** Handles text, files, and structured JSON data.
- **Enterprise-Ready:** Designed with security, authentication, and observability in mind.

## Getting Started

- 📚 **Explore the Documentation:** Visit the [Agent2Agent Protocol Documentation Site](https://a2a-protocol.org/) for a complete overview, the full protocol specification, tutorials, and guides.
- 📝 **View the Specification:** [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/)
- Use the SDKs:
	- [🐍 A2A Python SDK](https://github.com/a2aproject/a2a-python) `pip install a2a-sdk`
		- [🐿️ A2A Go SDK](https://github.com/a2aproject/a2a-go) `go get github.com/a2aproject/a2a-go`
		- [🧑💻 A2A JS SDK](https://github.com/a2aproject/a2a-js) `npm install @a2a-js/sdk`
		- [☕️ A2A Java SDK](https://github.com/a2aproject/a2a-java) using maven
		- [🔷 A2A.NET SDK](https://github.com/a2aproject/a2a-dotnet) using [NuGet](https://www.nuget.org/packages/A2A) `dotnet add package A2A`
		- [🦀 A2A Rust SDK](https://github.com/a2aproject/a2a-rs) `cargo add a2a-lf`
- 🎬 Use our [samples](https://github.com/a2aproject/a2a-samples) to see A2A in action

## Contributing

We welcome community contributions to enhance and evolve the A2A protocol!

- **Questions & Discussions:** Join our [GitHub Discussions](https://github.com/a2aproject/A2A/discussions).
- **Issues & Feedback:** Report issues or suggest improvements via [GitHub Issues](https://github.com/a2aproject/A2A/issues).
- **Contribution Guide:** See our [CONTRIBUTING.md](https://github.com/a2aproject/A2A/blob/main/CONTRIBUTING.md) for details on how to contribute.
- **Private Feedback:** Use this [Google Form](https://goo.gle/a2a-feedback).
- **Partner Program:** Google Cloud customers can join our partner program via this [form](https://goo.gle/a2a-partner).

## What's next

### Protocol Enhancements

- **Agent Discovery:**
	- Formalize inclusion of authorization schemes and optional credentials directly within the `AgentCard`.
- **Agent Collaboration:**
	- Investigate a `QuerySkill()` method for dynamically checking unsupported or unanticipated skills.
- **Task Lifecycle & UX:**
	- Support for dynamic UX negotiation *within* a task (e.g., agent adding audio/video mid-conversation).
- **Client Methods & Transport:**
	- Explore extending support to client-initiated methods (beyond task management).
		- Improvements to streaming reliability and push notification mechanisms.

## About

The A2A Protocol is an open source project under the Linux Foundation, contributed by Google. It is licensed under the [Apache License 2.0](https://github.com/a2aproject/A2A/blob/main/LICENSE) and is open to contributions from the community.