---
title: "Google MLOps白皮书（上）|MLOps生命周期及核心能力"
source: "https://zhuanlan.zhihu.com/p/557745130"
author:
  - "dreaming (Zhihu)"
published: 2022-08-25
created: 2026-06-29
description: "Google MLOps白皮书中文翻译：MLOps生命周期7阶段、核心技术能力（实验/数据处理/模型训练/评估/部署/在线实验/监控/流程/注册/特征库/元数据跟踪）"
tags:
  - source
  - mlops
  - machine-learning
  - google-cloud
  - whitepaper
---
[收录于 · MLOps技术分享](https://www.zhihu.com/column/c_1533571465966743552)

10 人赞同了该文章

目录

收起

01 内容摘要

02 MLOps生命周期概述和核心能力

03 构建支持ML的系统

04 MLOps的生命周期

05 MLOps：端到端工作流

06 MLOps的技术功能

07 实验

08 数据处理

09 模型训练

10 模型评估

11 模型部署

12 在线实验

13 模型监控

14 ML流程

15 模型注册

16 数据集和特征库

17 ML元数据和工件跟踪

## 01 内容摘要

在各个行业中， [DevOps](https://zhida.zhihu.com/search?content_id=212075994&content_type=Article&match_order=1&q=DevOps&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODI5MDI4MzIsInEiOiJEZXZPcHMiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMTIwNzU5OTQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.l11VZ3fXxZdVac6wNYGrv62K0c4299guHNAeZ4sfapk&zhida_source=entity) 和DataOps已经作为提高质量和缩短产品上线时间的方法，被软件工程和数据工程领域广泛采用。

随着机器学习（ML）系统的快速发展，需要在ML工程的背景下开发类似的方法，以处理ML实际应用的独特复杂性。这就是MLOps的应用领域。MLOps是一套标准化流程和技术能力，用于快速、可靠地构建、部署和运维ML系统。

我们之前发布了 [谷歌云](https://zhida.zhihu.com/search?content_id=212075994&content_type=Article&match_order=1&q=%E8%B0%B7%E6%AD%8C%E4%BA%91&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODI5MDI4MzIsInEiOiLosLfmrYzkupEiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMTIwNzU5OTQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.1oz7jUnOXVLqIwLZ2oZOm1_u4HWEetVoch1IonY7qIg&zhida_source=entity) 的人工智能实施框架，为‘希望建立有效的人工智能（AI）能力，以改变其业务的技术leader’提供指导。该框架涵盖围绕人、数据、技术和流程的人工智能挑战，分为六个不同主题：学习、领导、访问、安全、扩展和自动化。

当前文档更深入地探讨了“规模和自动化”主题，以说明构建和操作ML系统方面的需求。 **规模** 关系到您使用云管理的ML服务的程度，这些服务可以扩展到大量数据、大量数据处理和ML工作，并减少操作开销。 **自动化** 涉及到您能够在生产中高效、频繁和可靠地部署、执行和操作数据处理和ML流程技术的程度。

我们概述了MLOps的框架，该框架定义了MLOps的核心流程和技术能力。企业相关部门可以使用此框架帮助建立成熟的MLOps实践，以构建和运维ML系统。采用该框架可以帮助组织改进团队之间的协作，提高ML系统的可靠性和可扩展性，并缩短开发周期。这些好处反过来推动创新，并有助于从ML投资中获得整体业务价值。

本文档面向希望了解MLOps的技术leader和企业架构师，也适用于那些希望了解MLOps在实践中的细节的团队。本文件假设读者熟悉基本机器学习概念以及CI/CD等开发和部署实践。

该文件分为两部分。第一部分是MLOps生命周期和核心能力概述，面向所有读者。它介绍了MLOps的过程和功能，以及它们对于成功采用基于ML的系统的重要性。

第二部分是对MLOps过程和能力的深入研究。本部分面向希望了解任务具体细节的读者，如运行连续训练流程、部署模型和监控ML模型的预测性能。

本期介绍了白皮书的第一部分——MLOps生命周期和核心能力，第二部分内容将在下一期推出。

企业部门可以使用该框架来确定构建集成的ML平台的差距，并关注Google AI Adoption Framework中的规模以及自动化。是否（或在何种程度上）在您的组织中采用这些流程和功能取决于您的业务环境。例如，与购买或构建功能的成本（例如，工程开发的时间成本）相比，您必须确定框架创建的业务价值。

## 02 MLOps生命周期概述和核心能力

尽管人们越来越认识到AI/ML是数字转型的关键支柱，但成功的部署和有效的运维是从人工智能中获取价值的瓶颈。

只有50%的组织跨过了试点和概念验证的阶段。此外，在2019年之前开始人工智能试点的组织中，有72%的组织甚至无法在生产中部署一个应用程序。 [Algorithmia](https://zhida.zhihu.com/search?content_id=212075994&content_type=Article&match_order=1&q=Algorithmia&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODI5MDI4MzIsInEiOiJBbGdvcml0aG1pYSIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIxMjA3NTk5NCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.JkaLnK8thK0_76vSaImjCH88ezZv9X3I8ZduIy64UVA&zhida_source=entity) 对企业机器学习应用现状的调查发现，55%被调查的公司没有部署ML模型。

总而言之，模型无法投入生产，如果投入生产，它们就会崩溃，因为它们无法适应环境的变化。

这是由于各种问题造成的。企业机器学习部门的工作高度依赖人工，并且大都是一次性的工作，它们没有可复用或可复制的组件，其过程涉及数据科学家与IT之间的相互配合。

[Deloitte](https://zhida.zhihu.com/search?content_id=212075994&content_type=Article&match_order=1&q=Deloitte&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODI5MDI4MzIsInEiOiJEZWxvaXR0ZSIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIxMjA3NTk5NCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.Iem6XkrssD0do5v-jEfWQ4919rImg-wVY_OQHV4HbtY&zhida_source=entity) 将人才缺乏和整合问题确定为可能阻碍或破坏人工智能计划的因素。Algorithmia的调查强调，部署、扩展和版本控制工作中的挑战仍然阻碍团队从ML投资中获得价值。 [Capgemini](https://zhida.zhihu.com/search?content_id=212075994&content_type=Article&match_order=1&q=Capgemini&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODI5MDI4MzIsInEiOiJDYXBnZW1pbmkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMTIwNzU5OTQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.ZCEPKx5ZUX20BLMMaPj1sqCdtRPFANiu8fBaBlSy7Ug&zhida_source=entity) 研究指出，组织在实现大规模部署方面面临的三大挑战是缺乏中高级人才、缺乏变革管理流程、缺乏创新能力，缺乏实现规模化的强有力的治理模式。

这些研究和其他研究的共同主题是，ML系统不能以一种与其他IT（如数据操作和DevOps）隔离的特殊方式构建。如果不应用良好的软件工程实践，同时考虑到使运维ML不同于其他类型软件运维这一因素，ML系统也无法构建。

企业组织需要自动化和简化的ML流程。这个过程不仅仅帮助企业在生产中成功地部署ML模型，当企业在不断变化的环境中将ML应用程序的数量扩展到更多用例时，它还帮助管理风险，并帮助确保应用程序仍然符合业务目标。

[McKinsey](https://zhida.zhihu.com/search?content_id=212075994&content_type=Article&match_order=1&q=McKinsey&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODI5MDI4MzIsInEiOiJNY0tpbnNleSIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIxMjA3NTk5NCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.0DJYdi1KUcP5GsNPR5g1dJTBzEzEo21UGYSP2flPix8&zhida_source=entity) 对人工智能的全球调查发现，标准框架和开发流程的到位是高效的ML团队的区别因素之一。

这就是ML工程的关键所在。ML工程是构建支持ML的系统的中心，涉及生产级ML系统的开发和运行。ML工程是软件工程学科的超集，其具有独特的复杂性。这些复杂性包括：

- 为训练ML模型准备和维护高质量的数据。
- 跟踪生产中的模型，以检测性能是否下降。
- 对新数据源、ML算法和超参数进行持续实验，然后跟踪这些实验。
- 通过不断利用新数据对模型进行再训练，保持模型的准确性。
- 避免由于训练环境和部署环境之间的数据或运行时依赖项的不同而导致的训练-部署偏差。
- 处理对模型公平性和对抗性攻击的担忧。

MLOps是ML工程的一种方法，它将ML系统开发（ML元素）与ML系统运维（Ops元素）结合起来。它提倡将ML系统构建的关键步骤形式化和（如果有益）自动化。MLOps为快速、可靠地构建、部署和运维ML系统提供了一套标准化过程和技术能力。

以DevOps和DataOps支持应用工程和数据工程（分析）的方式，MLOps支持ML开发和部署。不同之处在于，当您部署web服务时，您关心的是效率、每秒查询数、负载平衡等。当您部署ML模型时，您还需要担心数据的变化、模型的变化、用户试图钻空子等。这就是MLOps的意义所在。

与不遵循MLOps实践的系统相比，MLOps做法可以带来以下好处：

• 开发周期更短，因此上市时间更短；

• 团队之间更好的协作；

• 提高ML系统的可靠性、性能、可扩展性和安全性；

• 简化运营和治理流程；

• 提高ML项目的投资回报率。

在本节中，您将了解MLOps的生命周期和工作流程，以及稳健的MLOps实现所需的各个功能。

## 03 构建支持ML的系统

构建支持ML的系统是一项综合性的任务，它将数据工程、ML工程和应用工程任务结合起来，如图1所示。

![[raw/assets/9f7fc86b8dff516b892ca3896d40711d_MD5.jpg]]

图1 数据工程、ML工程和应用工程的关系

数据工程涉及摄取、整合、管理和提炼数据，以促进广泛的操作任务、数据分析任务和ML任务。数据工程对于分析和ML计划的成功至关重要。如果一个组织没有强大的数据工程流程和技术，它可能无法成功地进行下游商业智能、高级分析或ML项目。

通过使用数据工程团队创建的专业数据，ML模型在生产中被构建和部署。模型是大量应用系统的组件，如商业智能系统、商业应用、过程控制系统和嵌入式系统。

将ML模型集成到应用中是一项关键任务，首先需要确保应用程序有效地使用部署的模型，然后监控模型性能。除此之外，您还应该收集和监控相关的业务KPI（例如，点击率、收入提升和用户体验），业务KPI有助于您了解ML模型对业务的影响，并相应地进行调整。

## 04 MLOps的生命周期

MLOps生命周期包括七个集成和迭代过程，如图2所示。

![[raw/assets/6c66be1043af3934699f86915d9c8a9d_MD5.jpg]]

图2 MLOps生命周期

这些过程可以包括以下内容：

**• ML开发** 涉及到实验和开发一个健壮且可重复的模型训练过程（训练流程代码），该过程包括从数据准备和转换到模型训练和评估的多个任务。

**• 训练操作** 涉及打包、测试和部署可重复且可靠的训练流程这一过程自动化。

**• 持续训练** 涉及重复执行训练流程以响应新数据或代码更改或按计划执行，可能带有新的训练设置。

**• 模型部署** 涉及将模型打包、测试和部署到服务环境，以进行在线实验和生产服务。

**• 预测服务** 指为生产中部署的模型提供服务，以进行推理。

**• 持续监控** 指监控已部署模型的有效性和效率.

**• 数据和模型管理** 管理ML工件以支持可审计性、可追溯性和合规性的一个中心、交叉功能。数据和模型管理还可以促进ML资产的共享性、可重用性和可发现性。

## 05 MLOps：端到端工作流

图3展示了MLOps流程如何相互作用的简化但规范的流程，重点放在高级控制流程以及关键输入和输出上。

![[raw/assets/95e4f1cea29fdeb0257949375777a8f0_MD5.jpg]]

图3 MLOps流程

这不是一个瀑布式工作流，它必须顺序地通过所有流程，可以跳过一些过程，或者重复给定的阶段或过程的子序列。该图显示了以下流程：

1\. ML开发阶段的核心是实验。当数据科学家和ML研究人员原型化模型架构和训练例程时，他们创建标注数据集，并使用特征和其他可复用的ML工件（通过数据和模型管理过程管理）。这个过程的主要输出是一个形式化的训练过程，包括数据预处理、模型架构和模型训练设置。

2\. 如果ML系统需要持续训练（模型的重复再训练），则训练过程作为训练流程进行操作。这需要一个CI/CD例程，以便于在目标执行环境中构建、测试和部署这套流程。

3\. 基于再训练触发器，持续训练流程被重复执行，并将生成一个模型作为输出。当有新数据可用或检测到模型性能衰减时，将重新训练模型。由训练流程生成的其他训练工件和元数据，也会一直被跟踪。如果流程生成了一个成功的候选模型，那么该候选模型将作为注册模型被模型管理过程跟踪。

4\. 对注册模型进行注释、审核并批准发布，然后将其部署到生产环境中。如果您使用的是无代码解决方案，则此过程可能相对不透明，或者它可能涉及构建用于渐进交付的自定义CI/CD流程。

5\. 部署的模型使用您指定的部署模式提供预测：在线、批处理或流式预测。除了服务预测之外，服务运行时还可以生成模型解释并捕获服务日志，以供连续监控过程使用。

6\. 持续监控过程监控模型的预测有效性和服务。性能监测的主要关注点是检测模型衰减，例如数据和概念漂移。性能监测还可以监控模型部署的效率指标，如延迟、吞吐量、硬件资源利用率和执行错误。

## 06 MLOps的技术功能

为了有效实施上一节概述的MLOps的关键流程，企业组织需要建立一套核心技术功能。这些功能可以由单个集成ML平台提供，或者它们可以通过组合最适合特定任务的供应商工具来创建，也可以作为定制服务开发，或者作为这些方法的组合来创建。

在大多数情况下，流程是分阶段部署的，而不是在单个部署中一次性部署。企业组织采用这些流程和能力的计划应与业务优先级以及组织的技术和技能成熟度保持一致。例如，许多组织从关注ML开发、模型部署和预测服务的过程开始。对于这些企业组织，如果他们正在试验数量相对较少的ML系统，则可能不需要持续训练和持续监控。

图4显示了MLOps通常需要的核心技术功能集。它们被抽象为功能组件，可以具有特定产品和技术的多对多映射。

![[raw/assets/efecaa769d9e8a23fd5d363effcd5bb7_MD5.jpg]]

图4 核心MLOps技术能力

为了支持任何IT工作负载，一些基础功能是必要的，例如可靠、可扩展和安全的计算基础设施。大多数企业组织已经在这些功能上进行了投资，并可以通过利用这些功能进行ML工作流而获益。这些功能可能跨越多个云，甚至部分在本地运行。理想情况下，这将包括高级功能，如专门的ML加速器。

此外，企业组织需要标准化的配置管理和CI/CD能力，以快速、可靠地构建、测试、发布和操作软件系统，包括ML系统。

在这些基础能力之上，还有一组核心MLOps能力。这些包括实验、数据处理、模型训练、模型评估、模型服务、在线实验、模型监控、ML流程和模型注册。最后，支持集成和交互的两个交叉能力是ML元数据和工件仓库以及ML数据集和特征仓库。

以下各节概述了各MLOps能力的特点。

## 07 实验

实验功能使您的数据科学家和ML研究人员能够协作执行探索性数据分析，创建原型模型架构，并实现训练计划。ML环境还应允许他们编写模块化、可复用和可测试的源代码，并进行版本控制。实验中的关键功能包括：

• 提供与Git等版本控制工具集成的notebook环境。

• 跟踪实验，包括数据、超参数，以及评估再现性和对比的指标的信息。

• 分析和可视化数据和模型。

• 支持探索数据集、查找实验和审查实施。

• 与平台中的其他数据服务和ML服务集成。

## 08 数据处理

数据处理功能允许您在ML开发、持续训练流程和预测服务中大规模地准备和转换大量数据。数据处理的关键功能包括：

• 支持交互式执行（例如从笔记本电脑上执行），用于快速实验和生产中的长期作业。

• 为各种数据源和服务提供数据连接器，以及各种数据结构和格式的数据编码器和解码器。

• 为结构化（表格）和非结构化数据（文本、图像等）提供丰富高效的数据转换和ML特征工程。

• 支持可扩展批处理和流数据处理。

## 09 模型训练

模型训练功能使您能够高效、经济地运行用于训练ML模型的强大算法。模型训练应能够根据模型和用于训练的数据集的大小进行缩放。模型训练中的关键功能包括：

• 支持通用ML框架并支持自定义运行时的环境。

• 支持针对多个GPU和多人的不同策略的大规模分布式训练。

• 支持按需使用ML加速器。

• 允许大规模高效超参数调整和目标优化。

• 理想情况下，提供内置的AutoML功能，包括自动特征选择和工程设计以及自动模型架构搜索和选择。

## 10 模型评估

通过模型评估功能，您可以交互式地在实验过程中和在生产过程中自动评估模型的有效性。模型评估中的关键功能包括：

• 在评估规模化的数据集上对模型进行批量评分。

• 在数据的不同切片上计算模型的预定义或自定义评估指标。

• 不同的持续训练的执行中，跟踪训练模型的预测性能。

• 可视化并比较不同模型的性能。

• 为假设分析和认知偏见和公平性问题提供工具。

• 使用各种可解释的人工智能技术实现模型行为解释。

## 11 模型部署

模型部署功能允许您在生产环境中部署模型。模型部署中的关键功能包括：

• 支持低延迟、近乎实时（在线）的预测和高吞吐量的批量（离线）预测。

• 为通用ML服务框架（例如，TensorFlow Serving、 [TorchServe](https://zhida.zhihu.com/search?content_id=212075994&content_type=Article&match_order=1&q=TorchServe&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODI5MDI4MzIsInEiOiJUb3JjaFNlcnZlIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjEyMDc1OTk0LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.MOFJp9PUlq_QN-RV_mk-mq0cazusgbGiYsFEiHd5Bik&zhida_source=entity) 、Nvidia Triton以及Scikit learn和XGBoost等其他模型）和自定义的运行环境，提供内嵌支持。

• 启用复合的预测例程，其中在聚合结果之前分层或同时调用多个模型，以及任何所需的预处理或后处理例程。

• 允许高效使用具有自动缩放功能的ML推理加速器，以匹配工作负载，并平衡成本和延迟。

• 使用给定模型预测的特征属性等技术支持模型解释性。

• 支持预测服务请求的记录和分析响应。

## 12 在线实验

在线实验的功能使您能够在新模型发布到生产环境之前，了解新训练的模型与当前模型（如果有）相比在生产环境中的表现。例如，推送给服务人群的一小部分，您可以使用在线实验来了解新推荐系统对点击率和会话率的影响。在线实验的结果应与模型注册功能集成，以便于决定将模型发布到生产环境中。在线实验通过帮助您决定放弃性能不佳的模型，并提升性能良好的模型，从而提高ML版本的可靠性。在线实验中的关键功能包括：

•支持金丝雀和影子部署（canary and shadow）。

•支持流量分流和A/B测试。

•支持多臂老虎机（MAB）测试。

## 13 模型监控

模型监控功能允许您跟踪生产中部署模型的效率和有效性，以确保预测质量和业务连续性。如果您的模型已过时，需要调查和更新，此功能将通知您。模型监控中的关键功能包括：

• 测量模型效率指标，如延迟和服务资源利用率。

• 检测数据偏差，包括模式异常、数据和概念转移和漂移。

• 将监测与模型评估能力相结合，以便在ground truth标签可用时持续评估部署模型的有效性性能。

## 14 ML流程

ML流程功能允许您在生产中对复杂的ML训练和预测流程进行仪表化、编排和自动化。ML工作流协调不同的组件，其中每个组件执行流程中的特定任务。ML流程中的关键功能包括：

• 按需、按计划或响应特定事件触发流程。

• 在ML开发期间启用本地交互式执行以进行调试。

• 与ML元数据跟踪功能集成，以捕获流程执行参数并生成工件。

• 为通用ML任务提供一组内置组件，还允许自定义组件。

• 在不同的环境中运行，包括本地机器和可扩展的云平台。

• 可选地，提供基于GUI的用于设计和构建流程的工具。

## 15 模型注册

模型注册功能允许您在中央仓库中管理ML模型的生命周期。这确保了生产模型的质量并支持模型发现。模型注册的关键功能包括：

• 将你培训和部署的ML模型进行注册、组织、跟踪和版本化。

• 为可部署性存储模型元数据和运行依赖。

• 维护模型文档和报告，例如使用模型卡

• 与模型评估和部署功能集成，并跟踪模型的在线和离线评估指标。

• 管理模型启动流程：审查、批准、发布和回滚。这些决策基于许多离线性能和公平性指标以及在线实验结果。

## 16 数据集和特征库

数据集和特征仓库功能允许您统一ML数据资产的定义和存储。拥有一个新的、高质量数据资产的中央仓库可以实现共享性、可发现性和可复用性。仓库还为模型训练和推理提供数据一致性。这有助于数据科学家和ML研究人员节省数据准备和特征工程方面的时间，通常数据准备和特征工程会占用他们大量的时间。数据和特征仓库中的关键功能包括：

• 支持数据资产的共享性、可发现性、可重用性和版本控制。

• 为事件流和在线预测工作负载提供实时摄取和低延迟服务。

• 允许高吞吐量批量摄取，并用于提取、转换、加载（ETL）过程和模型训练，以及对工作负载进行评分。

• 启用特征版本point-in-time查询。

• 支持各种数据模式，包括表格数据、图像和文本。

ML数据资产可以在实体特征级别或完整数据集级别进行管理。例如，特征仓库可能包含一个名为客户的实体，其中包括年龄、邮政编码和性别等功能。另一方面，数据集存储库可能包括客户流失数据集，其中包括来自客户和产品实体的特征，以及购买活动和web活动事件日志。

## 17 ML元数据和工件跟踪

在MLOps生命周期的不同过程中产生了各种类型的ML工件，包括描述性统计和数据模式、训练模型和评估结果。ML元数据是关于这些工件的信息，包括它们的位置、类型、属性以及与实验和运行的关联。ML元数据和工件跟踪功能是所有其他MLOps功能的基础。这样的能力可以实现复杂的ML任务和流程的复现性以及调试。ML元数据和工件跟踪中的关键功能包括：

• 提供ML工件的可追溯性和沿袭跟踪。

• 共享和跟踪实验及流程的参数配置。

• 存储、访问、调查、可视化、下载和归档ML工件。

• 与所有其他MLOps能力集成。

---

本文翻译自Google MLOps白皮书：MLOps实践者指南

发布于 2022-08-25 20:48

赞同 10