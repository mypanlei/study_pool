---
title: "Announcing the Agent2Agent Protocol (A2A)- Google Developers Blog"
source: "https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/"
author:
  - "[[Rao Surapaneni]]"
  - "[[Miku Jha]]"
  - "[[Michael Vakoc]]"
  - "[[Todd Segal]]"
published: 2025-04-09
created: 2026-06-18
description: "Explore A2A, Google's new open protocol empowering developers to build interoperable AI solutions."
tags:
  - "clippings"
---
developers.googleblog.com 使用 Cookie 来提供和提升服务质量并分析流量。如果您同意，Cookie 还将用于投放广告并个性化您看到的内容和广告。 [了解更多](https://policies.google.com/technologies/cookies?hl=en)

## 宣布推出 Agent2Agent 协议 (A2A)

2025年4月9日

[拉奥·苏拉帕内尼](https://developers.googleblog.com/en/search/?author=Rao+Surapaneni) 副总裁兼总经理 业务应用平台

[米库·贾](https://developers.googleblog.com/en/search/?author=Miku+Jha) 人工智能/机器学习合作伙伴工程总监 Google Cloud

[迈克尔·瓦科克](https://developers.googleblog.com/en/search/?author=Michael+Vakoc) 产品经理 Google Cloud

[托德·西格尔](https://developers.googleblog.com/en/search/?author=Todd+Segal) 首席工程师 业务应用平台

![A2A协议](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/image2.original_6xqVyTd.jpg)

## 代理互操作性的新时代

人工智能代理为人们提供了一个独特的机会，可以通过自主处理许多日常重复性或复杂的任务来提高工作效率。如今，企业正越来越多地构建和部署自主代理，以帮助扩展、自动化和优化工作场所的各个流程——从订购新笔记本电脑到协助客户服务代表，再到协助供应链规划。

为了最大限度地发挥智能体人工智能的优势，至关重要的是，这些智能体能够在动态的多智能体生态系统中跨越孤立的数据系统和应用程序进行协作。即使智能体是由不同的供应商或使用不同的框架构建的，使其能够相互互操作，也能提高自主性，成倍提升生产力，同时降低长期成本。

**  
今天，我们正式发布名为 Agent2Agent (A2A) 的全新开放协议。该协议得到了** 包括 Atlassian、Box、Cohere、Intuit、Langchain、MongoDB、PayPal、Salesforce、SAP、ServiceNow、UKG 和 Workday 在内的 50 多家技术合作伙伴以及埃森哲、波士顿咨询公司 (BCG)、凯捷、Cognizant、德勤、HCLTech、Infosys、毕马威、麦肯锡、普华永道、塔塔咨询服务公司 (TCS) 和威普罗在内的领先服务提供商的支持和贡献。A2A 协议将使 AI 代理能够相互通信、安全地交换信息，并在各种企业平台或应用程序之上协调行动。我们相信，A2A 框架将为客户带来显著价值，客户的 AI 代理现在能够跨整个企业应用程序环境运行。

这种合作努力标志着人们对未来的共同愿景：无论底层技术如何，人工智能代理都能无缝协作，实现复杂企业工作流程的自动化，并推动前所未有的效率和创新水平。

A2A 是一种开放协议，是对 Anthropic 的模型上下文协议 (MCP) 的补充，后者为智能体提供有用的工具和上下文信息。凭借 Google 在扩展智能体系统方面的内部专业知识，我们设计了 A2A 协议，旨在解决我们在为客户部署大规模多智能体系统时遇到的挑战。A2A 使开发者能够构建可与其他使用该协议构建的智能体连接的智能体，并为用户提供灵活组合来自不同提供商的智能体的功能。至关重要的是，企业可以从这种标准化的方法来管理其跨不同平台和云环境的智能体。我们相信，这种通用的互操作性对于充分发挥协作式 AI 智能体的潜力至关重要。

![Google Cloud - 为 Agent 2 Agent 协议做出贡献的合作伙伴包括：埃森哲、Arize、Articul、ask-ai、Atlassian、BCG、Box、c3.ai、凯捷、Chronosphere、Cognizant、Cohere、Colibra、Contextual.ai、Cotality、Datadog 等。](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/image1_yEPzdSr.original.png)

## A2A 设计原则

A2A 是一种开放协议，它为代理之间的协作提供了一种标准方式，不受底层框架或供应商的限制。在与合作伙伴共同设计该协议时，我们遵循了以下五个关键原则：

- **拥抱智能体能力** ：A2A 致力于让智能体以其自然、非结构化的方式进行协作，即使它们不共享记忆、工具和上下文。我们正在实现真正的多智能体场景，而不将智能体限制为“工具”。
- **基于现有标准：** 该协议基于现有的流行标准构建，包括 HTTP、SSE、JSON-RPC，这意味着它更容易与企业日常使用的现有 IT 堆栈集成。
- **默认安全** ：A2A 旨在支持企业级身份验证和授权，在发布时与 OpenAPI 的身份验证方案保持一致。
- **支持长时间运行的任务：** 我们设计的 A2A 具有很高的灵活性，能够胜任各种场景，从快速任务到深度研究，后者在人工参与的情况下可能需要数小时甚至数天才能完成。在此过程中，A2A 可以向用户提供实时反馈、通知和状态更新。
- **模态无关：** 代理世界不仅限于文本，因此我们将 A2A 设计为支持各种模态，包括音频和视频流。

## A2A 的运作方式

![图示流程图，展示了远程代理和客户端代理之间的数据流，以实现安全协作、任务和状态管理、用户体验协商以及能力发现。](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/image5_VkAG0Kd.original.png)

A2A 促进“客户端”代理和“远程”代理之间的沟通。客户端代理负责制定和传达任务，而远程代理负责执行这些任务，力求提供正确的信息或采取正确的行动。这种交互涉及以下几个关键功能：

- **能力发现：** 代理可以使用 JSON 格式的“代理卡”来宣传其能力，使客户端代理能够识别可以执行任务的最佳代理，并利用 A2A 与远程代理进行通信。
- **Task management:** The communication between a client and remote agent is oriented towards task completion, in which agents work to fulfill end-user requests. This “task” object is defined by the protocol and has a lifecycle. It can be completed immediately or, for long-running tasks, each of the agents can communicate to stay in sync with each other on the latest status of completing a task. The output of a task is known as an “artifact.”
- **Collaboration:** Agents can send each other messages to communicate context, replies, artifacts, or user instructions.
- **User experience negotiation:** Each message includes “parts,” which is a fully formed piece of content, like a generated image. Each part has a specified content type, allowing client and remote agents to negotiate the correct format needed and explicitly include negotiations of the user’s UI capabilities–e.g., iframes, video, web forms, and more.

See the full details of how the protocol works in our [draft specification](https://github.com/google/A2A).

## A real-world example: candidate sourcing

<video controls=""><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/A2A_demo_v4.mp4" type="video/mp4"><p>Sorry, your browser doesn't support playback for this video</p></video>

right click to view in new tab

Hiring a software engineer can be significantly simplified with A2A collaboration. Within a unified interface like Agentspace, a user (e.g., a hiring manager) can task their agent to find candidates matching a job listing, location, and skill set. The agent then interacts with other specialized agents to source potential candidates. The user receives these suggestions and can then direct their agent to schedule further interviews, streamlining the candidate sourcing process. After the interview process completes, another agent can be engaged to facilitate background checks. This is just one example of how AI agents need to collaborate across systems to source a qualified job candidate.

## The future of agent interoperability

A2A has the potential to unlock a new era of agent interoperability, fostering innovation and creating more powerful and versatile agentic systems. We believe that this protocol will pave the way for a future where agents can seamlessly collaborate to solve complex problems and enhance our lives.

We’re committed to building the protocol in collaboration with our partners and the community in the open. We’re releasing the protocol as open source and setting up clear pathways for contribution.

Review the [full specification draft](https://github.com/google/A2A), try out code samples, and see example scenarios on the [A2A website](https://google.github.io/A2A) and learn how you can contribute.

We are working with partners to launch a production-ready version of the protocol later this year.

## Feedback from our A2A partners

We're thrilled to have a growing and diverse ecosystem of partners actively contributing to the definition of the A2A protocol and its technical specification. Their insights and expertise are invaluable in shaping the future of AI interoperability.

Here's what some of our key partners are saying about the A2A protocol:

### Technology & Platform Partners

### ask-ai.com

> <sup>Ask-AI is excited to collaborate with Google on the A2A protocol, shaping the future of AI interoperability and seamless agent collaboration, advancing its leadership in Enterprise AI for Customer Experience.</sup>*<sup><br>– CEO Alon Talmor PhD</sup>*

### Atlassian

> <sup>With Atlassian's investment in Rovo agents, the development of a standardized protocol like A2A will help agents successfully discover, coordinate, and reason with one another to enable richer forms of delegation and collaboration at scale.</sup>*<sup><br>– Brendan Haire VP, Engineering of AI Platform. Atlassian</sup>*

### Articul8

> <sup>At Articul8, we believe that AI must collaborate and interoperate to truly scale across the enterprise. We’re excited to support the development of the A2A interoperability protocol – an initiative that aligns perfectly with our mission to deliver domain-specific GenAI capabilities that seamlessly operate across complex systems and workflows. We’re enabling Articul8's ModelMesh (an 'Agent-of-Agents') to treat A2A as a first-class citizen, enabling secure, seamless communication between intelligent agents.<br>–</sup> *<sup>Arun Subramaniyan, Founder &amp; CEO of Articul8</sup>*

### Arize AI

> <sup>Arize AI is proud to partner with Google as a launch partner for the A2A interoperability protocol, advancing seamless, secure interaction across AI agents as part of Arize's commitment to open-source evaluation and observability frameworks positions.</sup>*<sup><br>– Jason Lopatecki, Cofounder &amp; CEO, Arize AI</sup>*

**BCG**

> <sup>BCG helps redesign organizations with intelligence at the core. Open and interoperable capabilities like A2A can accelerate this, enabling sustained, autonomous competitive advantage.<br>–</sup> *<sup>Djon Kleine, Managing Director &amp; Partner at BCG</sup>*

### Box

> <sup>We look forward to expanding our partnership with Google to enable Box agents to work with Google Cloud’s agent ecosystem using A2A, innovating together to shape the future of AI agents while empowering organizations to better automate workflows, lower costs, and generate trustworthy AI outputs.</sup>*<sup><br>– Ketan Kittur, VP Product Management, Platform and Integrations at Box</sup>*

### C3 AI

> <sup>At C3 AI, we believe that open, interoperable systems are key to making Enterprise AI work and deliver value in the real world–and A2A has the potential to help customers break down silos and securely enable AI agents to work together across systems, teams, and applications.<br>–</sup> *<sup>Nikhil Krishnan - C3 AI SVP and Chief Technology Officer, Data Science</sup>*

### Chronosphere

> <sup>A2A will enable reliable and secure agent specialization and coordination to open the door for a new era of compute orchestration, empowering companies to deliver products and services faster, more reliably, and enabling them to refocus their engineering efforts on driving innovation and value.</sup>*<sup><br>– Rob Skillington, Founder /CTO</sup>*

### Cognizant

> <sup>"As a pioneer in enterprise multi-agent systems, Cognizant is committed and actively pursuing agent interoperability as a critical requirement for our clients."<br>-</sup> *<sup>Babak Hodjat, CTO - AI</sup>*

### Cohere

> <sup>At Cohere, we’re building the secure AI infrastructure enterprises need to adopt autonomous agents confidently, and the open A2A protocol ensures seamless, trusted collaboration—even in air-gapped environments—so that businesses can innovate at scale without compromising control or compliance.</sup>*<sup><br>– Autumn Moulder, VP of Engineering at Cohere</sup>*

### Confluent

> <sup>A2A enables intelligent agents to establish a direct, real-time data exchange, simplifying complex data pipelines to fundamentally change how agents communicate and facilitate decisions.</sup>*<sup><br>– Pascal Vantrepote, Senior Director of Innovation, Confluent</sup>*

### Cotality (formerly CoreLogic)

> <sup>A2A opens the door to a new era of intelligent, real-time communication and collaboration, which Cotality will bring to clients in home lending, insurance, real estate, and government—helping them to improve productivity, speed up decision-making.</sup>*<sup><br>– Sachin Rajpal, Managing Director, Data Solutions, Cotality</sup>*

### DataStax

> <sup>DataStax is excited to be part of A2A and explore how it can support Langflow, representing an important step toward truly interoperable AI systems that can collaborate on complex tasks spanning multiple environments.</sup>*<sup><br>– Ed Anuff, Chief Product Officer, DataStax</sup>*

### Datadog

> <sup>We're excited to see Google Cloud introduce the A2A protocol to streamline the development of sophisticated agentic systems, which will help Datadog enable its users to build more innovative, optimized, and secure agentic AI applications.</sup>*<sup><br>– Yrieix Garnier, VP of Product at Datadog</sup>*

### Elastic

> <sup>Supporting the vision of open, interoperable agent ecosystems, Elastic looks forward to working with Google Cloud and other industry leaders on A2A and providing its data management and workflow orchestration experience to enhance the protocol.</sup>*<sup><br>– Steve Kearns, GVP and GM of Search, Elastic</sup>*

### GrowthLoop

> <sup>A2A has the potential to accelerate GrowthLoop's vision of Compound Marketing for our customers—enabling our AI agents to seamlessly collaborate with other specialized agents, learn faster from enterprise data, and rapidly optimize campaigns across the marketing ecosystem, all while respecting data privacy on the customer's cloud infrastructure.</sup>*<sup><br>– Anthony Rotio, Chief Data Strategy Officer, GrowthLoop</sup>*

### Harness

> <sup>Harness is thrilled to support A2A and is committed to simplifying the developer experience by integrating AI-driven intelligence into every stage of the software lifecycle, empowering teams to gain deeper insights from runtime data, automate complex workflows, and enhance system performance.</sup>*<sup><br>– Gurashish Brar, Head of Engineering at Harness.</sup>*

### Incorta

> <sup>Incorta is excited to support A2A and advance agent communication for customers,making the future of enterprise automation smarter, faster, and truly data-driven.</sup>*<sup><br>– Osama Elkady CEO Incorta</sup>*

### Intuit

> <sup>Intuit strongly believes that an open-source protocol such as A2A will enable complex agent workflows, accelerate our partner integrations, and move the industry forward with cross-platform agents that collaborate effectively.</sup>*<sup><br>– Tapasvi Moturu, Vice President, Software Engineering for Agentic Frameworks, at Intuit</sup>*

### JetBrains

> <sup>We’re excited to be a launch partner for A2A, an initiative that enhances agentic collaboration and brings us closer to a truly multi-agent world, empowering developers across JetBrains IDEs, team tools, and Google Cloud.</sup>*<sup><br>– Vladislav Tankov, Director of AI, JetBrains</sup>*

### JFrog

> <sup>JFrog is excited to join the A2A protocol, an initiative we believe will help to overcome many of today’s integration challenges and be a key driver for the next generation of agentic applications.</sup>*<sup><br>– Yoav Landman, CTO and Co-founder, JFrog</sup>*

### LabelBox

> <sup>A2A is a key step toward realizing the full potential of AI agents, supporting a future where AI can truly augment human capabilities, automate complex workflows and drive innovation.</sup>*<sup><br>– Manu Sharma Founder &amp; CEO</sup>*

### LangChain

> <sup>LangChain believes agents interacting with other agents is the very near future, and we are excited to be collaborating with Google Cloud to come up with a shared protocol which meets the needs of the agent builders and users.</sup>*<sup><br>– Harrison Chase Co-Founder and CEO at LangChain</sup>*

### MongoDB

> <sup>By combining the power of MongoDB’s robust database infrastructure and hybrid search capabilities with A2A and Google Cloud’s cutting edge AI models, businesses can unlock new possibilities across industries like retail, manufacturing, and beyond to redefine the future of AI applications.</sup>*<sup><br>– Andrew Davidson, SVP of Products at MongoDB</sup>*

### Neo4j

> <sup>Neo4j is proud to partner with Google Cloud, combining our graph technology's knowledge graph and GraphRAG capabilities with A2A to help organizations unlock new levels of automation and intelligence while ensuring agent interactions remain contextually relevant, explainable and trustworthy.</sup>*<sup><br>– Sudhir Hasbe, Chief Product Officer at Neo4j</sup>*

### New Relic

> <sup>We believe the collaboration between Google Cloud’s A2A protocol and New Relic’s Intelligent Observability platform will provide significant value to our customers by simplifying integrations, facilitating data exchange across diverse systems, and ultimately creating a more unified AI agent ecosystem.</sup>*<sup><br>– Thomas Lloyd, Chief Business and Operations Officer, New Relic</sup>*

### Pendo

> <sup>We’re proud to partner on Google Cloud’s A2A protocol, which will be a critical step toward enabling AI agents to work together effectively, while maintaining trust and usability at scale.<br>–</sup> *<sup>Rahul Jain, Co-founder &amp; CPO at Pendo</sup>*

### PayPal

> <sup>PayPal supports Google Cloud’s A2A protocol, which represents a new way for developers and merchants to create next-generation commerce experiences, powered by agentic AI.</sup>*<sup><br>-Prakhar Mehrotra, SVP &amp; Head of Artificial Intelligence at PayPal</sup>*

### PwC

> <sup>At PwC, we believe the future of enterprise AI lies in seamless collaboration—not just between people and systems, but between agents themselves—which is why we’re proud to support agent2agent in collaboration with PwC’s agent OS, helping set the standard for secure, scalable agent interoperability across the enterprise."<br>-</sup> *<sup>Dallas Dolen, Global Google Cloud Alliance Leader</sup>*

### SAP

> <sup>SAP is committed to collaborating with Google Cloud and the broader ecosystem to shape the future of agent interoperability through the A2A protocol—a pivotal step toward enabling SAP Joule and other AI agents to seamlessly work across enterprise platforms and unlock the full potential of end-to-end business processes.</sup>*<sup><br>– Walter Sun, SVP &amp; Global Head of AI Engineering</sup>*

### Salesforce

> <sup>Salesforce is leading with A2A standard support to extend our open platform, enabling AI agents to work together seamlessly across Agentforce and other ecosystems to turn disconnected capabilities into orchestrated solutions and deliver an enhanced digital workforce for customers and employees.</sup>*<sup><br>– Gary Lerhaupt, VP Product Architecture</sup>*

### ServiceNow

> <sup>ServiceNow and Google Cloud are collaborating to set a new industry standard for agent-to-agent interoperability, and we believe A2A will pave the way for more efficient and connected support experiences.</sup>*<sup><br>– Pat Casey, Chief Technology Officer &amp; EVP of DevOps, ServiceNow</sup>*

### Supertab

> <sub>With Google Cloud’s A2A protocol and Supertab Connect, agents will be able to pay for, charge for, and exchange services — just like human businesses do.</sub>*<sub><br>– Cosmin Ene, Founder of Supertab</sub>*

### UiPath

> <sup>As a leader in enterprise automation and a pioneer in agentic orchestration, UiPath is excited to partner with Google on adopting and enhancing the A2A protocol and establishing an industry standard for seamless agent-to-agent communication – which is a significant step towards a future in which AI agents, robots and humans collaborate seamlessly to drive transformative business outcomes.<br>–</sup> *<sup>Graham Sheldon, Chief Product Officer</sup>*

### UKG

> <sub>We're thrilled at UKG to be collaborating with Google Cloud on the new A2A protocol, a framework that will allow us to build even smarter, more supportive human capital and workforce experiences that anticipate and respond to employee needs like never before.</sub>*<sub><br>– Eli Tsinovoi, Head of AI at UKG</sub>*

### Weights & Biases

> <sup>Weights &amp; Biases is proud to collaborate with Google Cloud on the A2A protocol, setting a critical open standard that will empower organizations to confidently deploy, orchestrate, and scale diverse AI agents, regardless of underlying technologies.</sup>*<sup><br>– Shawn Lewis, CTO and co-founder at Weights &amp; Biases</sup>*

### Services Partners

### Accenture

> <sup>The multi-agent A2A protocol from Google Cloud is the bridge that will unite domain specific agents across diverse platforms to solve complex challenges, enabling seamless communication and collective intelligence for smarter and effective agentic solutions.</sup>*<sup><br>– Scott Alfieri, AGBG Global lead, Accenture</sup>*

### Capgemini

> <sup>At Capgemini, we are excited to partner with Google Cloud in the A2A interoperability initiative. Allowing AI Agents to communicate across the ecosystem of platforms can truly accelerate the value of agentic AI for enterprises.</sup>  
> *<sup>– Herschel Parikh, Global Google Cloud Partner Executive, Capgemini</sup>*

### Deloitte

> <sup>Agent-to-agent interoperability is a foundational element of enabling the evolution of agentic AI architectures, and Google Cloud’s A2A initiative to bring together an ecosystem of technology industry participants to co-develop and support this protocol will immensely accelerate agentic AI adoption.</sup>*<sup><br>– Gopal Srinivasan, Deloitte</sup>*

### EPAM

> <sup>We are already leading the way in the A2A space by focusing on industry solutions that provide real business value—saving time, reducing overhead and helping our clients drive revenue and enhance processes like the development of FDA documentation during the drug discovery process.</sup>*<sup><br>– Marc Cerro, VP of Global Google Cloud Partnership at EPAM</sup>*

### HCLTech

> <sup>HCLTech is at the forefront of the agentic enterprise, and we are proud to partner with Google Cloud in defining agent-to-agent interoperability and advancing agentic AI possibilities through the open A2A standard.</sup>*<sup><br>– Vijay Guntur, Chief Technology Officer and Head of Ecosystems, HCLTech</sup>*

### KPMG

> <sup>At KPMG, we are excited to be part of this emerging initiative as A2A provides the essential standard we need for different AI agents to truly collaborate effectively and responsibly, which will enable customers and businesses to seamlessly harness AI for innovation and efficiency gains.</sup>*<sup><br>– Sherif AbdElGawad, Partner, Google Cloud &amp; AI Leader, KPMG</sup>*

**Quantiphi**

> <sup>The ability for agents to dynamically discover capabilities and build user experiences across platforms is crucial for unlocking the true potential of enterprises. We see the A2A protocol as a pivotal step to empower businesses to build such interoperable agents.</sup>*<sup><br>-Asif Hasan, Co-founder of Quantiphi</sup>*

### TCS (Tata Consultancy Services)

> <sup>The A2A protocol is the foundation for the next era of agentic automation, where Semantic Interoperability takes prominence, and we're proud to lead this transformative journey.</sup>*<sup><br>– Anupam Singhal, President, Manufacturing business, Tata Consultancy Services (TCS)</sup>*

### Wipro

> <sup>Because the future of AI lies in seamless collaboration, open protocols like A2A will be the foundation of an ecosystem where AI agents drive innovation at scale.</sup>*<sup><br>– Nagendra P Bandaru, Managing Partner and Global Head – Technology Services (Wipro)</sup>*

## Learn more about A2A

To learn more about the A2A framework, delve into the [**full specification draft**](https://github.com/google/A2A) and explore [**available code samples to**](https://google.github.io/A2A) examine the protocol's structure experiment with its code.

We encourage you to contribute to the protocol's evolution and help us define the future of agent interoperability by [submitting ideas](https://docs.google.com/forms/d/e/1FAIpQLScS23OMSKnVFmYeqS2dP7dxY3eTyT7lmtGLUa8OJZfP4RTijQ/viewform), [contributing to the documentation](https://github.com/google/A2A/blob/main/CONTRIBUTING.md), and engaging with the community.