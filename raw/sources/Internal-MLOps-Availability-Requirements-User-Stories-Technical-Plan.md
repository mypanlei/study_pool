---

## title: 内部 MLOps 平台 Availability 提升需求拆解与落地计划
created_at: 2026-06-02
updated_at: 2026-06-02
tags: [AI, MLOps, Availability, SLA, SLO, SLI, SRE, User Story, 需求分析, 执行计划]

# 内部 MLOps 平台 Availability 提升需求拆解与落地计划

> 本文将内部 MLOps 平台 Availability 提升工作按“需求拆解 → User Stories → 技术分析 → 落地执行计划”的顺序重新组织。  
> 目标是让计划更贴近 ML developer 的真实使用体验，同时便于在内网环境执行、衡量和验收。

## 0. Background and Motivation

### 0.1 客户承诺背景

客户需求的核心是：

> ML workflow solution availability should be at least 99.9%.

这里的 ML workflow platform 不是单一工具，而是覆盖 **CDPA → data generation → model training → model delivery** 的端到端工作流平台。它必须在开发、集成、运维和维护的完整生命周期内保持可用，而不是只在临时 demo 或 ad hoc test 中可用。

从客户和团队视角看，99.9% availability 的动机包括：

- 支撑 customer-facing commitments，避免平台不稳定影响对客户交付的可信度。
- 让 MLCA team、Customer 等团队能够稳定执行 Kubeflow workflow。
- 在并发请求或突发流量下自动扩容资源，避免系统明显卡顿或排队失控。
- 在升级 Kubeflow、NVIDIA drivers、Kubernetes、MLflow 等 stack 时，不中断或尽量少影响正在运行的 workflows。
- 在基础设施失败后，workflow 能从最近 checkpoint 恢复，而不是从头开始。
- 在系统损坏或完全丢失后，能通过 backup 和 restore 快速恢复。
- 将 workflows 调度到合适节点，提高资源利用率和成本效率。
- 采集系统指标并在异常时主动告警。

### 0.2 为什么已有生产或测试环境仍需要 availability study

即使平台已经在 production 或 testing 中运行，仍然需要专门做 availability study，原因是当前缺少一套可证明、可复盘、可对齐的可用性定义和证据链：


| 问题                  | 为什么必须研究                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------- |
| 缺少统一测量口径            | 当前未必能清楚回答单个组件和端到端 workflow 的实际 availability 是多少                                                           |
| 99.9% 不是单一数字        | 需要定义纳入哪些服务、统计窗口、planned maintenance、partial degradation 和依赖 SLA                                           |
| 依赖服务复杂              | Cluster、storage、image registry、identity service、network、Artifactory、Gerrit 等依赖由不同团队提供，需要 back-to-back OLA |
| 冗余和成本需要权衡           | 需要决定保留多少 headroom、哪些组件要 replicas、failover、backup 和 restore                                                |
| 自动化边界不清             | auto-scaling、failover、health check、recovery playbook 哪些要自动化，哪些可人工处理，会直接影响可达到的 availability                |
| 故障和恢复语义不清           | 需要定义 workflow metadata 的 RTO、RPO，以及部分降级时什么算 available 或 unavailable                                       |
| 容量和调度影响体验           | GPU、CPU、memory、storage 的 sizing、scaling 和 placement 需要绑定真实 spike scenarios 和 job placement use cases      |
| 需要向 stakeholders 证明 | 需要 dashboard、SLO、error budget、incident postmortem 和定期 review 来证明是否达到 99.9%                                |


### 0.3 本文对客户需求的解释原则

本方案将客户的 99.9% availability 需求拆成三层：


| 层级    | 解释                                                        |
| ----- | --------------------------------------------------------- |
| 用户感知层 | ML developers 和客户团队能否完成端到端 workflow 的关键动作                 |
| 平台能力层 | MLOps 平台是否具备监控、扩缩容、恢复、备份、调度、升级和故障处理能力                     |
| 责任边界层 | 哪些由平台团队负责，哪些依赖 IT 上游服务，哪些属于 scheduled maintenance 或容量 SLO |


因此，本计划不会把“99.9%”当成一个抽象口号，而是转化为可执行的 user stories、技术控制点、指标和 Go or No-Go 条件。

## 1. 总体思路

### 1.1 目标不是先写 99.9%，而是先定义“谁的什么体验要可用”

MLOps 平台主要服务对象是 **ML developers**。因此 availability 不能只从 Kubeflow Pod、MLflow Pod、Ingress Pod 是否存活出发，而要从开发者是否能完成关键工作出发。

本计划采用以下逻辑：

```mermaid
flowchart TD
  businessGoal[Business Goal] --> userJourney[ML Developer Journeys]
  userJourney --> userStories[User Stories]
  userStories --> sliDefinition[SLI Definition]
  sliDefinition --> technicalAnalysis[Technical Analysis]
  technicalAnalysis --> executionPlan[Implementation Plan]
  executionPlan --> measurableReview[SLO Review]
```



核心判断标准：

> 如果 ML developer 无法登录、查询实验、提交 pipeline、记录 metric、访问 model registry、上传下载 artifact 或查看运行状态，即使底层 Pod 还活着，也应视为用户感知 availability 受损。

### 1.2 推荐的第一阶段目标

第一阶段不要直接承诺“完整 MLOps platform 端到端 99.9%”。建议定义为：

> **ML Developer Core Journey Availability internal SLO：核心 ML developer 工作旅程在月度统计周期内达到 99.9% 可用性。**

这比“平台所有东西都 99.9%”更实际，因为它：

- 面向真实用户体验。
- 范围可控。
- 指标可测。
- 能区分平台团队可控故障和上游 IT 依赖故障。
- 能逐步扩展到 Notebook、GPU capacity、KServe serving、training success 等二阶段 SLO。

### 1.3 采用成熟但内网可执行的实践


本方案不建议直接照搬公有云 SLA 条款，因为内部 MLOps 平台有内网、上游 IT 依赖、工具集升级和容量约束。更实际的做法是采用成熟 SRE/SLO 方法论和可自建工具，把它们映射到内网执行流程。

| 成熟实践 | 参考链接 | 可借鉴点 | 内网落地方式 | 第一阶段产出 |
| -------- | -------- | -------- | ------------ | ------------ |
| Google SRE SLI/SLO/Error Budget | [Google SRE Workbook - Implementing SLOs](https://sre.google/workbook/implementing-slos/), [Google SRE Book - Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) | 用用户相关 SLI 定义 SLO，用 error budget 平衡可靠性和发布速度；不要追求 100% 可用性 | 建立月度 SLO review、error budget policy、P1/P2 RCA、发布冻结规则 | `ML Developer Core Journey Availability` SLO、43.2 分钟月度 error budget、月度 review 模板 |
| Google Art of SLOs | [Google SRE - Art of SLOs](https://sre.google/resources/practices-and-processes/art-of-slos/) | 从用户交互和用户感知出发，而不是从组件存活出发 | 按 ML developer journey 设计 SLI，例如 login、pipeline submission、MLflow metric round-trip、artifact round-trip | user journey SLI 清单、synthetic probe 设计 |
| OpenSLO | [OpenSLO Specification](https://github.com/OpenSLO/OpenSLO), [OpenSLO website](https://openslo.com/) | 将 SLO 声明为代码，便于评审、版本化、复用和跨工具迁移 | 在 Gerrit/Git 中维护 `slo/*.yaml`，由 Jenkins 校验 schema，再生成 PrometheusRule 或 dashboard 配置 | SLO-as-code 目录、OpenSLO 风格 YAML、变更评审流程 |
| Prometheus Blackbox Exporter | [Prometheus Blackbox Exporter](https://github.com/prometheus/blackbox_exporter/), [Prometheus multi-target exporter pattern](https://prometheus.io/docs/guides/multi-target-exporter/) | 从用户视角探测 HTTP、HTTPS、DNS、TCP、ICMP、gRPC 等端点 | 在内网 `monitoring` namespace 部署 blackbox exporter，从平台外部或独立探测节点模拟 ML developer 访问 | login、DNS、TLS、portal、API endpoint 黑盒探测 |
| Prometheus Operator | [Prometheus Operator](https://prometheus-operator.dev/) | 用 Kubernetes CRD 管理 Prometheus、ServiceMonitor、PrometheusRule 和 Alertmanager | 通过 GitOps 管理 ServiceMonitor、PrometheusRule、Alertmanager routing，减少手工配置 | `ServiceMonitor`、`PrometheusRule`、Alertmanager receiver |
| Sloth | [Sloth Prometheus SLO Generator](https://sloth.dev/), [Sloth GitHub](https://github.com/slok/sloth) | 基于 Google SRE 方法自动生成 Prometheus SLO recording rules、burn-rate alerts 和 dashboard | 初期可手写 PrometheusRule；成熟后用 Sloth CLI 或 Operator 从 SLO spec 生成规则 | SLO recording rules、multi-window burn-rate alerts |
| Pyrra | [Pyrra website](https://pyrra.dev/), [Pyrra GitHub](https://github.com/pyrra-dev/pyrra) | 让 Prometheus SLO 更易管理，支持 Kubernetes CRD 和 UI | 如果团队需要更轻量的 SLO UI，可在内网部署 Pyrra 管理 SLO | SLO UI、error budget dashboard |
| Grafana | [Grafana dashboards documentation](https://grafana.com/docs/grafana/latest/dashboards/) | 用 dashboard 展示 SLO、error budget、burn rate、incident 和趋势 | 建立 executive view、ML developer journey view、dependency view、upgrade impact view | 月度 SLO dashboard 和 stakeholder review dashboard |
| Alertmanager | [Prometheus Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) | 告警分组、抑制、路由和升级 | P1/P2 直接路由到 on-call；P3 进入 ticket；上游依赖告警同步对应 IT owner | P1/P2 routing、on-call receiver、ITSM webhook |
| ITIL 变更管理和维护窗口 | [ITIL change enablement overview](https://www.axelos.com/resource-hub/blog/what-is-change-enablement), 组织内部 change management 流程 | planned maintenance 要有通知、审批、窗口、回滚、维护后验证和超窗处理 | K8s、Kubeflow、MLflow、NVIDIA drivers 等升级进入 change calendar；维护后跑 core journey canary；超窗转 incident | upgrade checklist、maintenance window policy、planned maintenance report |

第一阶段建议采用“轻工具、强流程”的落地顺序：

1. 先用 Prometheus、Blackbox Exporter、Grafana、Alertmanager 建立最小闭环。
2. SLO 先可以用 PrometheusRule 手写，避免工具导入阻塞。
3. 当 SLO 数量稳定后，再引入 OpenSLO、Sloth 或 Pyrra 做 SLO-as-code 和规则生成。
4. 所有 SLO、alert、dashboard、runbook 和 upgrade checklist 都进入 Gerrit/Git 评审，避免运维知识只存在个人经验里。


## 2. 需求层面拆解

### 2.1 Stakeholders


本需求建议按 5 类 stakeholder 管理，避免把每个工具 owner 都直接提升为同一层级的业务 stakeholder。Platform、DevOps、IAM、DevTools、Cloud 等更适合归并到 MLOps team 或 IT team 下面，再通过 dependency registry 和 RACI 明确责任。

| Stakeholder 分类 | 包含角色或团队 | 核心关注点 | 需要从计划中得到什么 | 典型决策权 |
| ---------------- | ------------- | ---------- | -------------------- | ---------- |
| Customer | 外部客户、内部客户、使用 ML workflow solution 的交付对象 | 端到端 ML workflow solution 是否能支撑 customer-facing commitment，尤其是 99.9% availability 是否可信 | SLA 范围、证据、例外项、恢复能力、月度 availability 报告 | 是否接受 SLA/SLO 口径；是否接受 planned maintenance 和 exclusions |
| ML developers | MLCA team、模型开发团队、数据科学家、pipeline 使用者 | 能否稳定完成 CDPA、data generation、model training、model delivery、实验追踪、artifact 和 model registry 操作 | 清晰的用户旅程 SLI、故障通知、恢复预期、容量和调度透明度 | 提供用户场景优先级；确认哪些 journey 最关键 |
| MLOps team | Platform team、MLOps platform owner、SRE/on-call、部分 DevOps 执行角色 | 平台能力、SLO 达成、故障恢复、runbook、RCA、error budget、Kubeflow/MLflow 等工具集升级 | 可执行 backlog、SLO dashboard、告警规则、runbook、升级 checklist、Go/No-Go 标准 | 定义平台方案；推进 HA、监控、恢复和运营闭环 |
| IT team | IT IAM、IT DevTools、IT Cloud、storage、network、image registry、Artifactory、Gerrit、Jenkins、Kubernetes cloud、GPU/CPU/memory 资源 owner | 上游服务 OLA、维护窗口、容量、基础设施稳定性、升级和变更影响 | dependency registry、back-to-back OLA、维护日历、升级路径、RTO/RPO 和容量模型 | 承诺上游 OLA；批准或执行基础设施变更和维护 |
| Business owners | 产品负责人、项目负责人、交付负责人、工程管理层 | 业务连续性、成本、风险、客户承诺、发布节奏和资源投入 | 月度 SLO review、error budget、成本和容量权衡、RCA action、SLA readiness 结论 | 是否正式承诺 SLA；是否冻结发布；是否投入冗余和自动化成本 |

简化后的责任关系：

| 问题 | Primary owner | Supporting stakeholders | 说明 |
| ---- | ------------- | ----------------------- | ---- |
| 99.9% SLA/SLO 口径 | Business owners | Customer、MLOps team | Business owner 负责承诺，Customer 确认接受范围，MLOps team 提供可证明数据 |
| ML developer journey SLI | MLOps team | ML developers、Business owners | MLOps team 负责定义和实现，ML developers 确认旅程是否真实代表使用体验 |
| 上游 IT 依赖和 OLA | IT team | MLOps team、Business owners | IT team 负责基础服务目标，MLOps team 负责把依赖影响纳入报告 |
| Toolset upgrade break | MLOps team | IT team、ML developers、Business owners | MLOps team 和 IT team 执行升级，Business owners 决定维护窗口可接受性 |
| Incident 和 RCA | MLOps team | IT team、ML developers | MLOps team 牵头，若根因在上游 IT 服务，则 IT team 必须参与 RCA 和 permanent fix |
| 容量和成本权衡 | Business owners | IT team、MLOps team、ML developers | Business owners 决定成本边界，IT/MLOps 提供容量模型，ML developers 提供真实 spike scenario |


### 2.2 需求分层


| 层级              | 需求                                                                        | 说明                                   | 是否第一阶段 |
| --------------- | ------------------------------------------------------------------------- | ------------------------------------ | ------ |
| 业务需求            | ML developers 能稳定使用 MLOps 完成日常模型开发                                        | 这是所有技术工作的上层目标                        | 是      |
| 用户体验需求          | 登录、实验查询、pipeline 控制面、MLflow 写读、model registry、artifact round-trip 可用      | 直接体现用户感知 availability                | 是      |
| 可观测性需求          | 在用户大规模报障前发现核心路径故障                                                         | 从 ticket-driven 转向 alert-driven      | 是      |
| 架构需求            | 核心入口、API、状态层、制品层无明显单点                                                     | 支撑 99.9% 的基础                         | 是      |
| 上游依赖需求          | Azure 鉴权、Gerrit/Git、Jenkins、Kubernetes cloud、GPU、CPU、memory 有 owner 和 OLA | 内部平台通常无法单独保证端到端 SLA                  | 是      |
| 工具集升级需求         | K8s、Kubeflow、MLflow 等 toolsets 定期升级时要有维护窗口、回滚、canary 和计入口径                | 升级是必要活动，但会影响 ML developer 用户旅程       | 是      |
| 运维需求            | P1/P2 分级、on-call、runbook、RCA、error budget review                          | 让可靠性持续运营                             | 是      |
| 容量需求            | GPU、CPU、memory、storage 不足可预警、可解释、可规划                                      | 容量不直接混入 availability，但要单独治理          | 是      |
| 端到端 workflow 需求 | CDPA、data generation、model training、model delivery 能稳定串联                  | 客户承诺关注的是完整 workflow solution，而不是单个工具 | 是      |
| 弹性伸缩需求          | 并发请求或突发流量下自动扩容 server resources                                           | 支撑 spike scenarios 和多人同时请求           | 是      |
| 故障恢复需求          | 基础设施失败后从 last saved checkpoint 恢复                                         | 避免 workflow 从头重跑导致时间和资源浪费            | 是      |
| 备份恢复需求          | 系统损坏或完全丢失后可快速 restore                                                     | 支撑灾难恢复和数据保护                          | 是      |
| 调度放置需求          | workflows 能调度到合适节点                                                        | 提升利用率、成本和成功率                         | 是      |
| 扩展需求            | Notebook、KServe、训练任务成功率、GPU scheduling latency                            | 第二阶段逐步扩展                             | 否      |


### 2.3 第一阶段 In Scope


| 范围                       | 内容                                                                       | 理由                                                                      |
| ------------------------ | ------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| ML developer login       | Azure 鉴权、Dashboard 或平台门户入口                                               | 登录失败是最直接的不可用                                                            |
| Experiment visibility    | MLflow 和 KFP experiment、run、metric 查询                                    | 开发者需要查看实验与运行结果                                                          |
| Pipeline control plane   | 提交 pipeline、获取 run id、查询 run status                                      | 平台核心控制面能力                                                               |
| MLflow tracking          | log metric、log param、query run                                           | 实验追踪核心路径                                                                |
| Model registry query     | 查询 registered model 和 model version                                      | 模型资产管理核心路径                                                              |
| Artifact round-trip      | 上传和下载小型 canary artifact                                                  | 验证制品链路、对象存储和权限                                                          |
| Ingress/Auth/DNS/TLS     | 用户入口依赖链路                                                                 | 影响全部用户路径                                                                |
| 上游 IT 依赖                 | Azure 鉴权、Gerrit/Git、Jenkins、Kubernetes cloud、GPU、CPU、memory              | 必须纳入依赖治理和维护窗口                                                           |
| Toolset upgrades         | Kubernetes、Kubeflow、MLflow、Istio、cert-manager、KServe、Argo、Prometheus 等升级 | 升级可能造成 planned service break，必须纳入 change calendar 和 availability report |
| End-to-end workflow      | CDPA、data generation、model training、model delivery 的关键链路                 | 客户需求关注 workflow solution 是否可用                                           |
| Resource management      | 并发请求、突发流量、autoscaling、headroom                                           | 支撑 spike scenarios，避免系统 lagging                                         |
| Failure recovery         | checkpoint、retry、resume、workflow metadata 恢复                             | 支撑基础设施失败后的恢复                                                            |
| Backup and restore       | metadata、artifact、配置、镜像、workflow 定义恢复                                    | 支撑系统损坏或丢失后的快速恢复                                                         |
| Scheduling and placement | node selector、affinity、taint/toleration、queue、quota                      | 支撑利用率、成本和合适节点调度                                                         |


### 2.4 第一阶段 Out of Scope


| 不纳入第一阶段 99.9% 的内容                 | 原因                   | 替代治理方式                                   |
| --------------------------------- | -------------------- | ---------------------------------------- |
| 任意训练任务成功率                         | 受用户代码、数据、镜像、依赖影响大    | 单独定义 training job success SLO            |
| 任意 Notebook 创建成功率                 | 受容量、镜像、用户环境影响明显      | 第二阶段纳入 notebook spawn SLI                |
| GPU 一定有空闲                         | 容量不是控制面 availability | 定义 GPU capacity SLO 和 queue waiting time |
| CPU 和 memory 无限可用                 | 容量规划问题不等同平台不可用       | 定义 resource headroom 和 quota SLO         |
| KServe 在线推理 endpoint availability | 推理数据面应独立治理           | 单独建立 serving SLO                         |
| 用户网络和客户端问题                        | 平台无法直接控制             | SLA exclusions 中说明                       |


### 2.5 非功能需求


| 类别                  | 需求                                            | 可衡量标准                                                            |
| ------------------- | --------------------------------------------- | ---------------------------------------------------------------- |
| Availability        | 核心 ML developer journey 月度可用性达到 99.9%         | 月度 downtime 小于等于 43.2 分钟                                         |
| Detection           | 核心故障由监控主动发现                                   | P1 中 synthetic probe 或 alert 首发现比例大于 80%                         |
| Response            | P1 快速确认                                       | P1 acknowledge 小于等于 5 分钟                                         |
| Recovery            | P1 快速缓解                                       | P1 mitigation 小于等于 30 分钟                                         |
| Observability       | 核心用户旅程有 SLI 和 dashboard                       | 每个核心 journey 都有 success rate、latency、error budget                |
| Resilience          | 单 Pod 或单节点故障不导致核心旅程整体不可用                      | 演练通过，或生产事件中未造成整体中断                                               |
| Dependency          | 上游 IT 服务有 owner、OLA、维护窗口                      | 依赖清单覆盖率 100%                                                     |
| Change Safety       | 生产变更可审计、可回滚                                   | 关键配置通过 GitOps 或等价流程发布                                            |
| Upgrade Safety      | 工具集升级影响可预测、可回滚、可验证                            | 100% 生产升级有维护窗口、pre-check、rollback plan、post-upgrade canary 和影响记录 |
| RTO                 | 关键 workflow control plane 故障后恢复时间可定义          | P1 mitigation 小于等于 30 分钟；具体 RTO 按组件细分                            |
| RPO                 | workflow metadata 和 tracking metadata 数据丢失可定义 | 关键 metadata RPO 按业务确认，备份和恢复演练可证明                                 |
| Partial Degradation | 部分降级时有明确 available/unavailable 判定             | 例如可提交 job 但 GPU 极度受限，应计入 capacity degradation 而非简单 available     |


## 3. User Stories

### Epic 1：用户感知 SLO 与指标体系


| Story ID | User Story                                               | 验收标准                                                                                     | 指标                                                  |
| -------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------- |
| US-01    | 作为 ML developer，我希望能稳定登录 MLOps 平台，以便开始日常实验和 pipeline 工作。 | canary user 每 5 分钟完成一次登录 journey；失败连续 2 次触发告警；登录失败能区分 Azure 鉴权、Ingress、TLS、Dashboard 问题。 | login journey success rate、auth callback latency    |
| US-02    | 作为 ML developer，我希望能查看实验和运行记录，以便判断模型训练和实验结果。             | canary 每 1 分钟查询 MLflow 或 KFP experiment 和 run；返回合法结果；失败进入 SLO 统计。                        | experiment query success rate、P95 latency           |
| US-03    | 作为 ML developer，我希望能提交 pipeline run，以便启动训练或数据处理流程。       | canary pipeline 可提交并返回 run id；提交失败可区分 KFP API、DB、Argo、Auth 或 Git 依赖问题。                   | pipeline submission success rate、submission latency |
| US-04    | 作为 ML developer，我希望能查看 pipeline 运行状态，以便定位失败和跟踪进度。        | canary run status 查询成功；能返回状态、metadata 和日志链接；失败触发 P2 或 P1。                                | pipeline status query success rate                  |
| US-05    | 作为 ML developer，我希望能记录并读取 MLflow metrics，以便比较实验效果。       | canary run 写入 metric 后可再次读取且值一致；失败能定位 backend store 或 tracking server。                   | metric round-trip success rate                      |
| US-06    | 作为 ML developer，我希望能访问 model registry，以便查看模型版本和注册状态。     | canary 查询 registered model 和 model version 成功；失败能定位 MLflow registry、backend DB 或权限问题。    | model registry query success rate                   |
| US-07    | 作为 ML developer，我希望能上传和下载 artifact，以便保存模型、日志和中间结果。       | canary artifact 上传下载成功并 checksum 一致；失败能定位 artifact store、权限、网络或容量问题。                     | artifact round-trip success rate                    |


### Epic 2：上游依赖与维护窗口治理


| Story ID | User Story                                                               | 验收标准                                                                                    | 指标                                                           |
| -------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| US-08    | 作为 platform owner，我希望知道 Azure 鉴权维护或故障对 MLOps 登录的影响，以便合理解释 availability。  | Azure 鉴权 owner、维护窗口、升级路径记录在 dependency registry；登录 probe 能标记 auth dependency failure。   | auth upstream incident count、maintenance impact minutes      |
| US-09    | 作为 ML developer，我希望 Git 和 Jenkins 故障不会被误判为 MLOps 内部故障，以便问题能被正确升级。        | Gerrit/Git 和 Jenkins 有 canary probe；影响 pipeline 或发布时自动标记 upstream DevTools dependency。  | Git fetch success rate、Jenkins critical job availability     |
| US-10    | 作为 platform owner，我希望 Kubernetes cloud、GPU、CPU、memory 维护可提前感知，以便避开高风险发布。 | IT 维护日历进入 MLOps change calendar；维护期间冻结高风险发布；维护后执行 canary。                               | planned maintenance coverage、post-maintenance canary success |
| US-11    | 作为 business owner，我希望月报能区分用户感知不可用和平台团队可控不可用，以便正确治理责任边界。                  | 月报同时输出 user-facing availability、platform-owned availability、upstream dependency impact。 | 三类 availability report 按月输出                                  |
| US-11A   | 作为 business owner，我希望上游服务 SLA 被纳入总体 SLA 模型，以便避免 MLOps 对不可控依赖做过度承诺。       | dependency registry 记录每个关键上游服务的 SLA 或 OLA、统计窗口、排除项、owner、升级路径和 error budget 消耗；月报展示 upstream budget consumption。 | upstream SLA coverage、upstream error budget consumed |


### Epic 3：可观测性与告警


| Story ID | User Story                                                              | 验收标准                                                                            | 指标                              |
| -------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------- |
| US-12    | 作为 on-call engineer，我希望在用户提单前收到核心 journey 故障告警，以便缩短 MTTA。               | 核心 journey probe 接入 Alertmanager；P1 告警能路由到 on-call；告警包含可能根因。                    | alert detection ratio、MTTA      |
| US-13    | 作为 platform engineer，我希望 dashboard 能展示 SLO 和 error budget，以便做月度 review。 | Grafana 展示 core journey availability、burn rate、error budget、top failed journey。 | error budget consumed、burn rate |
| US-14    | 作为 DevOps engineer，我希望组件指标能帮助定位 journey 失败原因，以便快速恢复。                    | Dashboard、KFP、MLflow、Ingress、Auth、DB、artifact store、CoreDNS、node pool 有诊断指标。    | root cause identification time  |


### Epic 4：架构加固与恢复能力


| Story ID | User Story                                                      | 验收标准                                                                           | 指标                                                        |
| -------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------- |
| US-15    | 作为 ML developer，我希望单个 Pod 或节点故障不会让我无法使用核心平台能力。                  | Dashboard、KFP API、MLflow、Ingress、Auth、CoreDNS、Istio Gateway 多副本并配置 PDB。        | single pod or node failure drill pass                     |
| US-16    | 作为 platform engineer，我希望 MLflow 和 KFP 状态层没有单点，以便避免数据层故障导致全平台中断。 | MLflow backend store、KFP metadata DB 使用 HA DB；artifact store 使用对象存储或 HA MinIO。 | DB availability、artifact availability、restore test result |
| US-17    | 作为 on-call engineer，我希望有明确 runbook，以便 P1 能在 30 分钟内缓解。           | 登录、KFP、MLflow、artifact、Ingress、Auth、DB、上游依赖均有 runbook。                         | P1 mitigation time、runbook coverage                       |


### Epic 5：运营闭环与 SLA readiness


| Story ID | User Story                                                   | 验收标准                                                                        | 指标                                    |
| -------- | ------------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------- |
| US-18    | 作为 platform owner，我希望每月 review SLO，以便持续决定优先做稳定性还是功能发布。       | 每月 SLO review 固定召开；输出 error budget、P1/P2、RCA action、下月 reliability backlog。 | monthly SLO review completion         |
| US-19    | 作为 engineering manager，我希望 error budget 消耗能影响发布策略，以便避免稳定性恶化。 | error budget 超过阈值时触发发布冻结或收紧；策略写入变更流程。                                       | release freeze events、budget consumed |
| US-20    | 作为 business owner，我希望正式 SLA 前有连续数据证明，以便承诺真实可信。               | 连续 2 到 3 个月 core journey SLO 大于等于 99.9%；P1 MTTR 小于等于 30 分钟。                 | SLA readiness score                   |


### Epic 6：工具集升级与计划维护治理


| Story ID | User Story                                                                                                | 验收标准                                                                                                                                  | 指标                                                                                          |
| -------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| US-21    | 作为 DevOps engineer，我希望定期升级 Kubernetes、Kubeflow、MLflow 等 toolsets 时有明确维护窗口和回滚方案，以便升级不会变成不可控 service break。 | 每次生产升级都有 change ticket、影响评估、维护窗口、rollback plan、owner、pre-check 和 post-upgrade canary。                                                 | upgrade change coverage、rollback readiness                                                  |
| US-22    | 作为 ML developer，我希望工具集升级造成的不可用能提前通知，并在窗口结束后快速恢复，以便安排实验和 pipeline。                                         | 升级至少提前通知；维护窗口说明影响范围；窗口结束后 core journey canary 通过；超窗自动转 incident。                                                                      | planned maintenance notice coverage、post-upgrade canary success、maintenance overrun minutes |
| US-23    | 作为 business owner，我希望月报能区分 planned upgrade break、unplanned break 和 upgrade overrun，以便判断 99.9% 是否真实可靠。     | 月报分别输出 gross user-facing availability、net SLA availability、planned upgrade minutes、upgrade overrun minutes、upgrade-related incidents。 | planned upgrade impact minutes、upgrade-related P1/P2 count                                  |


### Epic 7：客户用例驱动的端到端 workflow 可用性


| Story ID | User Story                                                                                                          | 验收标准                                                                                                             | 指标                                                                   |
| -------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| US-24    | 作为 MLCA team 或 Customer，我希望能稳定执行 Kubeflow workflow，以便完成从 data generation 到 model training 再到 model delivery 的端到端流程。 | 定义一条代表性 canary workflow；能提交、调度、运行、记录 metadata、产出 artifact 并完成状态查询；失败可定位到 CDPA、KFP、MLflow、artifact、cluster 或上游依赖。 | end-to-end workflow canary success rate、workflow stage failure count |
| US-25    | 作为 ML developer，我希望多人同时请求时平台能自动扩容或保持足够 headroom，以便突发流量下系统不明显 lagging。                                               | 定义 spike scenario；关键 API、workflow submission 和 artifact 操作在并发压力下满足 success rate 和 latency threshold；容量不足时有告警。    | autoscaling reaction time、resource headroom、P95 latency under spike  |
| US-26    | 作为 ML developer，我希望基础设施失败后 workflow 能从最近 checkpoint 恢复，以便避免从头重跑。                                                    | 对支持 checkpoint 的 workflow 定义 checkpoint interval、resume procedure 和验证用例；模拟 node 或 pod failure 后能从 checkpoint 恢复。 | checkpoint resume success rate、lost work duration                    |
| US-27    | 作为 platform owner，我希望系统损坏或完全丢失后能通过 backup 和 restore 快速恢复，以便满足灾难恢复要求。                                                | metadata DB、MLflow tracking data、artifact、workflow definitions、GitOps config 有备份；至少每季度做 restore drill。           | restore drill success、RTO、RPO                                        |
| US-28    | 作为 platform engineer，我希望 workflows 能被调度到合适节点，以便提升资源利用率和成本效率。                                                        | 定义 node placement 策略、GPU/CPU queue、quota 和 priority；workflow 能按资源需求调度到合适 node pool。                              | scheduling success rate、queue waiting time、resource utilization      |
| US-29    | 作为 on-call engineer，我希望平台能采集系统 metrics 并在异常时告警，以便提前发现容量、故障和性能问题。                                                    | 关键组件、workflow、资源池和上游依赖都有 metrics；异常能触发告警；告警关联 runbook。                                                           | alert coverage、false negative count、anomaly detection lead time      |


## 4. 技术分析

### 4.1 SLI 设计分析

组件指标不能直接等价为用户体验。建议采用三层指标：


| 指标层级                        | 用途                  | 示例                                                                                           |
| --------------------------- | ------------------- | -------------------------------------------------------------------------------------------- |
| User Journey SLI            | 判断用户感知 availability | login journey success rate、pipeline submission success rate、artifact round-trip success rate |
| Dependency SLI              | 判断上游依赖是否影响用户旅程      | Azure auth success、Git fetch success、Jenkins job availability、Kubernetes API latency         |
| Component Diagnostic Metric | 定位根因                | Pod readiness、DB connection、Ingress 5xx、PVC usage、CoreDNS latency                            |


第一阶段 SLO 应以 User Journey SLI 为准，Dependency SLI 和 Component Metric 用于解释失败原因。

### 4.2 推荐 SLO 组合


| SLO                                    | 目标            | 统计周期           | 是否第一阶段 |
| -------------------------------------- | ------------- | -------------- | ------ |
| ML Developer Core Journey Availability | 99.9%         | Calendar month | 是      |
| P1 MTTA                                | 小于等于 5 分钟     | Calendar month | 是      |
| P1 MTTR                                | 小于等于 30 分钟    | Calendar month | 是      |
| User-ticket first detection ratio      | 小于 20%        | Calendar month | 是      |
| Upstream dependency impact reporting   | 100% P1/P2 标记 | Calendar month | 是      |
| GPU scheduling latency                 | 待基线后设定        | Rolling 7 days | 第二阶段   |
| Notebook spawn success rate            | 99.5% 到 99.9% | Calendar month | 第二阶段   |
| KServe endpoint availability           | 按业务重要性单独定义    | Calendar month | 第二阶段   |


### 4.3 监控与探测方案

内网可执行的方案不依赖外部 SaaS：


| 能力              | 推荐实现                                        | 最小可行版本                                   |
| --------------- | ------------------------------------------- | ---------------------------------------- |
| Synthetic probe | Blackbox Exporter 和自定义 canary job           | 先实现 HTTP、Auth、MLflow、KFP、artifact canary |
| Metrics         | Prometheus、kube-state-metrics、node-exporter | 复用现有 Prometheus，缺口用 ServiceMonitor 补齐    |
| SLO rules       | Sloth、Pyrra 或手写 PrometheusRule              | 初期可手写，成熟后改 SLO-as-code                   |
| Dashboard       | Grafana                                     | 先做一个 executive view 和一个 journey view     |
| Alerting        | Alertmanager、邮件、Teams、短信或 ITSM webhook      | P1/P2 先接 on-call，P3 保留 ticket            |
| Logs            | Loki、ELK 或 OpenSearch                       | 最小要求是能按 incident 查询关键服务日志                |


### 4.4 上游依赖技术风险


| 上游依赖             | 对用户旅程的影响                  | 技术处理                                                                |
| ---------------- | ------------------------- | ------------------------------------------------------------------- |
| Azure 鉴权         | 登录失败，所有入口不可用              | login probe、token refresh probe、IAM owner 升级路径                      |
| Gerrit/Git       | pipeline 代码拉取失败，发布受阻      | Git fetch canary、mirror、维护窗口同步                                      |
| Jenkins          | CI/CD 和平台发布受阻             | critical job canary、发布冻结策略                                          |
| Kubernetes cloud | Pod 调度、API、节点池、网络和存储异常    | Kubernetes API probe、node pool dashboard、cloud maintenance calendar |
| GPU              | 训练或推理排队                   | capacity SLO、queue waiting time、quota 和优先级                          |
| CPU 和 memory     | 控制面或用户任务资源不足              | platform node pool 隔离、resource headroom alert                       |
| Storage          | artifact、metadata、PVC 受影响 | artifact canary、PVC usage、object store availability                 |


### 4.4.1 上游 SLA 纳入与误差预算分摊

上游服务本身也有 SLA 或 OLA，例如 Azure 鉴权、Gerrit、Jenkins、Kubernetes cloud、storage、image registry、network、Artifactory 等。它们必须纳入 availability study，否则 MLOps 总体 99.9% 会被不可控依赖拖垮。

核心原则：

> 用户感知可用性必须记录上游影响；正式 SLA 承诺必须明确责任边界；平台工程必须通过依赖准入、冗余、降级和错误预算分摊降低上游 SLA 对总体 SLA 的不可控影响。

#### 4.4.1.1 为什么不能只看单个上游 SLA

如果一个用户旅程依赖多个串行服务，总体可用性大致会被这些依赖共同限制。简化估算如下：

```text
EndToEndAvailability ≈ A_mloops * A_auth * A_cluster * A_storage * A_registry * A_network
```

例如，如果核心路径依赖 5 个都只有 99.9% 的串行服务，理论乘积约为：

```text
0.999^5 = 0.995
```

这意味着即使每个依赖单独看都是 99.9%，端到端路径也可能只有约 99.5%。因此，如果 MLOps 要对外承诺 99.9%，不能简单接受所有上游 99.9% 并串起来，而要做以下处理：

1. 缩小正式 SLA 范围，只承诺平台可控和已治理的 user journeys。
2. 要求关键上游服务提供高于或等于 MLOps 目标的 back-to-back OLA。
3. 对关键上游依赖做缓存、镜像、冗余、降级或绕过。
4. 将上游影响从 gross user-facing availability 中展示出来，但在 net SLA 中按合同和 OLA 边界处理。
5. 将上游故障纳入 RCA 和 problem management，而不是简单标记为 out of scope。

#### 4.4.1.2 上游 SLA 分类

| 上游依赖类型 | 示例 | 对 MLOps 的影响 | 建议处理方式 |
|---|---|---|---|
| Critical blocking dependency | Azure 鉴权、Kubernetes API、Ingress/DNS、storage、artifact store | 一旦不可用，核心 user journey 直接失败 | 必须有 OLA、监控、升级路径、RCA；目标 SLA 应高于或等于 MLOps 目标 |
| Critical but reducible dependency | Gerrit/Git、image registry、Artifactory、Jenkins | 影响新 workflow、发布或镜像拉取，但可通过缓存或镜像降低影响 | 建立 mirror、cache、read-only fallback；故障时限制新提交但保护已运行 workflow |
| Capacity dependency | GPU、CPU、memory、storage quota | 影响调度等待和性能，不一定等于控制面不可用 | 单独定义 capacity SLO、queue waiting time、headroom |
| Operational dependency | IT 维护日历、变更审批、on-call escalation | 影响 planned maintenance 和 incident 协同 | 纳入 change calendar、maintenance policy 和 escalation matrix |

#### 4.4.1.3 三种报告口径

| 口径 | 是否包含上游 SLA 影响 | 用途 |
|---|---|---|
| Gross user-facing availability | 包含所有上游导致的用户感知不可用 | 反映客户和 ML developer 的真实体验 |
| Net SLA availability | 按 SLA/OLA 边界扣除合规的上游 planned maintenance 或明确排除项 | 用于正式对客户或业务承诺 |
| Platform-owned controllable availability | 只衡量 MLOps team 可直接控制的部分，同时单独展示 upstream impact | 用于 MLOps team 内部工程改进 |

#### 4.4.1.4 错误预算分摊建议

30 天 99.9% 的总 error budget 是 **43.2 分钟**。建议不要让所有依赖无限制消耗同一个预算，而是先做预算分摊：

| Budget bucket | 建议占比 | 30 天预算 | 示例 |
|---|---:|---:|---|
| MLOps platform owned | 50% | 21.6 分钟 | Kubeflow、MLflow、Ingress、artifact、platform config |
| Upstream critical dependencies | 30% | 13.0 分钟 | Azure auth、Kubernetes cloud、storage、network |
| Planned maintenance and upgrades | 10% | 4.3 分钟 | 合规但有用户影响的 planned upgrade 透明展示 |
| Unknown or unclassified | 10% | 4.3 分钟 | 尚未归因或跨团队问题 |

这不是合同条款，而是内部治理模型。它的作用是让上游团队知道：如果某个 upstream dependency 单月反复消耗 20 到 30 分钟，即使 MLOps team 本身没有故障，端到端 99.9% 也会失守。

#### 4.4.1.5 上游依赖准入规则

任何纳入核心 user journey 的上游依赖，都应满足以下准入条件：

| 条件 | 最低要求 |
|---|---|
| Owner | 有明确 IT owner 和 escalation path |
| SLA 或 OLA | 有可查的 availability target、统计窗口、排除项 |
| Monitoring | MLOps dashboard 能看到该依赖的健康状态或 canary |
| Maintenance | planned maintenance 进入 MLOps change calendar |
| Incident | 上游故障能关联到 MLOps incident 和 RCA |
| Mitigation | 至少有一种降级、缓存、镜像、重试、绕过或人工恢复方案 |
| Reporting | 月报中能区分 upstream planned maintenance、upstream unplanned outage、platform-owned outage |

如果关键上游依赖无法满足这些条件，就不应无条件纳入正式 99.9% SLA；要么降低承诺，要么增加冗余和降级设计，要么在 SLA exclusions 中明确。

#### 4.4.1.6 降低上游 SLA 不确定性的技术手段

| 上游风险 | 降低影响的手段 |
|---|---|
| Azure 鉴权短时不可用 | token 缓存、会话续期、登录链路 probe、IAM escalation |
| Gerrit/Git 不可用 | repo mirror、read-only cache、pipeline 使用 pinned commit |
| Jenkins 不可用 | 关键 job 备份、手动 emergency procedure、发布冻结 |
| Image registry 或 Artifactory 不可用 | 节点侧镜像缓存、registry mirror、关键镜像预拉取 |
| Kubernetes cloud 节点池维护 | 多 node pool、PDB、topology spread、控制面和 workload 隔离 |
| Storage 抖动或不可用 | 对象存储冗余、重试、备份、artifact checksum 和 canary |
| GPU 资源不足 | queue、quota、priority、capacity forecast、preemption policy |


### 4.5 架构加固分析


| 层级         | 当前常见风险                                                | 第一阶段技术动作                                  |
| ---------- | ----------------------------------------------------- | ----------------------------------------- |
| 入口层        | Ingress、Auth、DNS、TLS 单点或无告警                           | 多副本、PDB、TLS 到期告警、login journey probe      |
| Kubeflow 层 | Dashboard、KFP API 单副本或缺少 PDB                          | 多副本、readiness、PDB、HPA、KFP query probe     |
| MLflow 层   | Tracking server 单实例，backend store 或 artifact store 单点 | Tracking server 多副本，HA DB，对象存储            |
| 状态层        | DB、PVC、MinIO 单点                                       | HA DB、对象存储、备份恢复演练                         |
| 可观测性       | 用户先发现故障                                               | synthetic probe、burn-rate alert、dashboard |
| 变更治理       | 手工变更难回滚                                               | GitOps、staging 验证、rollback checklist      |
| 运维流程       | ticket-driven，MTTR 不稳定                                | on-call、runbook、RCA、error budget          |


### 4.6 Toolset 升级造成 service break 是否计入

Kubernetes、Kubeflow、MLflow、Istio、cert-manager、KServe、Argo、Prometheus 等 toolsets 定期升级是必要活动，但它们对 availability 的计入口径要明确区分。建议采用 **三口径统计**：


| 口径                                       | 是否计入升级维护影响                                            | 用途                          |
| ---------------------------------------- | ----------------------------------------------------- | --------------------------- |
| Gross user-facing availability           | 计入所有用户感知不可用，包括计划升级窗口                                  | 反映 ML developer 真实体验，用于内部改进 |
| Net SLA availability                     | 不计入合规的 scheduled maintenance，但计入超窗、未通知、回滚失败、升级引发的额外故障 | 用于正式 SLA 或业务承诺口径            |
| Platform-owned controllable availability | 计入平台团队可控故障；合规计划维护单独列出，不和 incident 混淆                  | 用于平台团队工程治理                  |


建议规则如下：


| 场景                                       | 是否计入 Gross user-facing availability | 是否计入 Net SLA availability   | 是否计入 Platform-owned controllable availability | 说明                     |
| ---------------------------------------- | ----------------------------------- | --------------------------- | --------------------------------------------- | ---------------------- |
| 提前公告、已批准、在维护窗口内完成、post-upgrade canary 通过 | 是，作为 planned maintenance impact 展示  | 通常不计入                       | 不计入故障，但计入 planned maintenance minutes         | 这是成熟 SLA 常见排除项，但必须透明披露 |
| 提前公告但超出维护窗口                              | 窗口内和超窗都展示；超窗单独标记                    | 超窗部分计入                      | 超窗部分计入                                        | 超窗说明升级可控性不足            |
| 未提前公告的升级中断                               | 是                                   | 计入                          | 计入                                            | 对用户等同非计划中断             |
| 升级失败导致回滚或长时间不可用                          | 是                                   | 计入失败和超窗部分                   | 计入                                            | 应生成 P1/P2 和 RCA        |
| 升级窗口内发现 unrelated 上游 IT 故障               | 是                                   | 按 root cause 和 SLA/OLA 边界判断 | 按 owner 判断                                    | 不能因为在维护窗口内就自动排除所有问题    |
| 零停机 rolling upgrade，无用户旅程失败              | 不产生 downtime                        | 不计入                         | 不计入                                           | 只记录 change success     |


因此，回答“是否 taken into account”：

> **要纳入统计和报告，但不一定全部扣减正式 SLA。**  
> 对 ML developer 真实体验，planned upgrade break 必须展示；对正式 SLA，只有满足提前通知、批准窗口、窗口内完成、影响范围明确、维护后验证通过的 scheduled maintenance 才可排除。任何未公告、超窗、失败回滚或升级引发的额外 service break 都应计入。

### 4.7 升级技术控制点


| 控制点                 | 最小要求                                                               | 衡量指标                        |
| ------------------- | ------------------------------------------------------------------ | --------------------------- |
| 版本兼容矩阵              | Kubernetes、Kubeflow、MLflow、Istio、KServe、Argo、cert-manager 版本兼容关系明确 | upgrade pre-check pass      |
| Staging 验证          | 生产升级前在 staging 跑 core journey canary                               | staging canary success      |
| 维护窗口                | 明确开始、结束、影响范围、owner、回滚条件                                            | maintenance notice coverage |
| 回滚方案                | 数据库 schema、CRD、manifest、Helm chart、Kustomize overlay 均有回滚路径        | rollback readiness          |
| 灰度或 rolling upgrade | 能 rolling 的组件优先 rolling，减少用户感知中断                                   | zero-downtime upgrade ratio |
| Post-upgrade canary | 升级后验证 login、experiment query、pipeline、MLflow、registry、artifact     | post-upgrade canary success |
| RCA                 | 超窗或失败升级必须 RCA                                                      | upgrade-related RCA closure |


### 4.8 端到端 ML workflow 技术分析

客户需求中的 workflow solution 应覆盖：

```mermaid
flowchart LR
  cdpa[CDPA] --> dataGeneration[Data Generation]
  dataGeneration --> modelTraining[Model Training]
  modelTraining --> modelDelivery[Model Delivery]
  modelTraining --> mlflowTracking[MLflow Tracking]
  modelTraining --> artifacts[Artifacts]
  modelDelivery --> registry[Model Registry]
```



端到端 availability 不应简单等于所有组件 availability 相乘后得到一个不可执行的数字，而应先定义 **representative workflow canary**：


| 阶段              | 成功标准                                 | 主要依赖                                    | 失败信号                                          |
| --------------- | ------------------------------------ | --------------------------------------- | --------------------------------------------- |
| CDPA 触发         | workflow 输入准备完成                      | CDPA、Git、Auth、API                       | input generation failed                       |
| Data generation | 数据生成 job 成功产出数据或 metadata            | KFP、Kubernetes、storage                  | job failed、PVC issue、node issue               |
| Model training  | training job 能调度、运行并上报状态             | GPU/CPU/memory、Kubernetes、NVIDIA driver | pending timeout、driver issue、OOM、node failure |
| Tracking        | metric、param、run status 写入成功         | MLflow、backend DB                       | tracking write failed                         |
| Artifact        | model artifact 上传成功                  | object store、network、permission         | artifact upload failed                        |
| Model delivery  | model version 或 delivery package 可查询 | registry、artifact、delivery pipeline     | registry query failed                         |


第一阶段不建议把所有真实训练任务成功率纳入 99.9%，但建议把一条轻量级 canary workflow 纳入 availability study，用来证明平台控制面和关键数据链路是可用的。

### 4.9 RTO、RPO 和部分降级定义

客户需求明确提到 checkpoint resume 和 backup/restore，因此必须补充 RTO、RPO 与 partial degradation 语义。


| 对象                             | 建议 RTO              | 建议 RPO                            | 说明                  |
| ------------------------------ | ------------------- | --------------------------------- | ------------------- |
| MLOps portal、Auth、Ingress      | 30 分钟内 mitigation   | 不涉及业务数据                           | 影响登录和入口             |
| KFP control plane              | 30 分钟内 mitigation   | metadata RPO 由 DB 备份策略决定          | 影响 workflow 提交和查询   |
| MLflow tracking                | 30 分钟内 mitigation   | tracking metadata RPO 由 DB 备份策略决定 | 影响实验记录和模型注册         |
| Artifact store                 | 4 小时内 mitigation    | artifact RPO 按对象存储复制和备份策略定义       | 影响模型、日志和中间结果        |
| Representative workflow canary | 4 小时内恢复可执行          | checkpoint interval 以内            | 用于验证端到端流程           |
| 完整灾难恢复                         | 1 到 2 个工作日内恢复最小可用平台 | 按业务确认                             | 取决于备份、镜像、配置和基础设施可用性 |


Partial degradation 需要明确定义：


| 场景                                  | 建议分类                             | 是否计入 core availability                     |
| ----------------------------------- | -------------------------------- | ------------------------------------------ |
| 用户无法登录                              | Unavailable                      | 是                                          |
| 用户能登录但无法提交 pipeline                 | Unavailable for pipeline journey | 是                                          |
| 用户能提交 job，但 GPU 资源极度不足导致长时间 Pending | Capacity degradation             | 不直接计入 core availability，但计入 capacity SLO   |
| MLflow 查询可用但写 metric 失败             | Partial unavailable              | 计入 metric round-trip journey               |
| Artifact 下载慢但未失败                    | Performance degradation          | 若超过 latency threshold，可计入 degraded minutes |
| Notebook 创建失败但核心 workflow canary 可用 | Second-stage SLO impact          | 第一阶段单独报告                                   |


### 4.10 容量、扩缩容和调度分析

客户用例要求“many people send requests at the same time”时系统可扩容并避免 lagging。因此 availability study 必须包含 sizing 和 spike scenario，而不是只看平时平均负载。


| 能力          | 技术问题                                           | 第一阶段输出                                  |
| ----------- | ---------------------------------------------- | --------------------------------------- |
| Headroom    | 平时保留多少 CPU、memory、GPU、DB connection、storage 空间 | headroom target 和告警阈值                   |
| Autoscaling | HPA、Cluster Autoscaler、Karpenter 或内部扩容机制是否可用   | autoscaling reaction time 和扩容限制         |
| Queueing    | 并发 workflow 是否排队，队列是否公平                        | queue waiting time、priority class、quota |
| Placement   | GPU job、CPU job、控制面 Pod 是否分离                   | node pool、taints、tolerations、affinity   |
| Cost        | 99.9% 和 spike handling 需要多少冗余成本                | capacity model 和成本区间                    |


建议至少定义 3 个 spike scenarios：

1. 多名用户同时登录和查询实验。
2. 多个 pipeline 同时提交。
3. 多个 training jobs 同时请求 GPU 或高 memory 节点。

每个 scenario 都要有成功率、P95 latency、queue waiting time 和资源利用率指标。

## 5. 落地执行计划

### 5.1 执行原则

1. **先测量，再承诺**：没有连续数据前，只能说 target 或 internal SLO，不能说已具备 SLA。
2. **先用户旅程，再组件指标**：SLO 以 ML developer core journey 为准，组件指标用于定位。
3. **先止血，再重构**：先修复 Top 故障和监控缺口，再做 HA 架构改造。
4. **先内网可执行，再追求完美工具链**：PrometheusRule 手写可先跑起来，后续再上 OpenSLO 或 Sloth。
5. **上游依赖要透明**：Azure 鉴权、Git、Jenkins、Kubernetes cloud、GPU、CPU、memory 维护必须进入报告。
6. **升级维护要三口径统计**：K8s、Kubeflow、MLflow 等升级造成的 planned break 要进入 gross user-facing availability；只有合规 scheduled maintenance 才可从 net SLA availability 中排除。
7. **端到端 workflow 要有代表性 canary**：用轻量级 workflow 验证 CDPA、data generation、model training、model delivery 的关键链路。

### 5.2 阶段 0：需求冻结与基线设计

周期：1 到 2 周。


| 工作包                        | 具体任务                                                           | Owner                               | 交付物                             | 验收标准                                         |
| -------------------------- | -------------------------------------------------------------- | ----------------------------------- | ------------------------------- | -------------------------------------------- |
| SLO scope                  | 冻结 ML Developer Core Journey 范围                                | Platform owner、业务方                  | SLO scope 文档                    | 范围、排除项、统计周期被确认                               |
| Customer motivation        | 固化客户 99.9% 背景和 use cases                                       | Business owner、Platform owner       | Motivation and use case summary | 客户承诺、use cases、scope 和 reference diagram 被记录 |
| User journey mapping       | 梳理登录、实验查询、pipeline、MLflow、registry、artifact 路径                 | Platform team                       | Journey map                     | 每条 journey 有成功标准                             |
| E2E workflow canary design | 设计 CDPA、data generation、training、delivery 的代表性 canary workflow | Platform team、MLCA team             | Canary workflow design          | 每个阶段有输入、输出、成功标准和失败分类                         |
| Dependency registry        | 梳理 Azure 鉴权、Git、Jenkins、Kubernetes cloud、GPU、CPU、memory        | Platform team、IT owners             | Dependency registry             | 每个依赖有 owner、影响、升级路径                          |
| Upstream SLA model         | 收集关键上游服务 SLA/OLA，并建立 error budget 分摊模型                    | MLOps team、IT team、Business owners  | Upstream SLA and OLA matrix     | 关键依赖有 SLA/OLA、统计窗口、排除项和 budget bucket      |
| Upgrade policy             | 定义 K8s、Kubeflow、MLflow 等升级的 downtime 计入口径                      | Platform owner、DevOps、业务方           | Upgrade maintenance policy      | 明确 gross、net SLA、platform-owned 三口径          |
| RTO and RPO                | 定义 workflow metadata、artifact、tracking data 的 RTO/RPO          | Platform owner、DB team、Storage team | RTO/RPO matrix                  | RTO/RPO 被业务方和 owner 确认                       |
| Baseline schema            | 定义 incident 字段和 downtime 统计口径                                  | SRE 或 DevOps                        | Incident template               | 能记录 MTTA、MTTR、root cause、upstream impact     |


阶段验收：

- 有一份被平台、DevOps、IT 和业务方认可的 SLO scope。
- 能说明第一阶段哪些纳入 99.9%，哪些只做容量或依赖报告。
- 有 dependency registry 初版。
- 有 upstream SLA/OLA matrix，能判断哪些依赖可纳入 99.9%，哪些需要 exclusion、冗余或降级。
- 能回答 K8s、Kubeflow、MLflow 升级造成的 service break 哪些计入、哪些排除、如何披露。
- 有一条代表性 E2E workflow canary 设计和 RTO/RPO 初版。

### 5.3 阶段 1：最小可观测性和 SLI 建立

周期：2 到 4 周。


| 工作包                 | 具体任务                                                                                | Owner                   | 交付物                      | 验收标准                                          |
| ------------------- | ----------------------------------------------------------------------------------- | ----------------------- | ------------------------ | --------------------------------------------- |
| Synthetic probes    | 实现 login、experiment query、pipeline submission、metric round-trip、artifact round-trip | Platform team、DevOps    | Canary probes            | 每个核心 journey 有 success metric                 |
| E2E workflow canary | 实现轻量级 CDPA 到 model delivery canary                                                  | Platform team、MLCA team | E2E canary workflow      | 每日或每小时可运行并输出阶段性成功率                            |
| Prometheus metrics  | 暴露或采集 `mlops_developer_journey_success_total` 等指标                                   | DevOps                  | Prometheus metrics       | Prometheus 可查询 core journey 成功率               |
| Capacity baseline   | 建立 CPU、memory、GPU、storage、DB connection、queue waiting time baseline                 | DevOps、IT Cloud         | Capacity baseline report | 能看到 headroom 和容量瓶颈                            |
| Upstream SLI probes | 为关键上游依赖建立 canary 或健康指标                                                               | IT team、MLOps team      | Upstream dependency dashboard | Azure auth、Git、Jenkins、Kubernetes API、storage、registry 状态可见 |
| Dashboard           | 建 Grafana executive view 和 journey view                                             | SRE 或 DevOps            | Grafana dashboard        | 能看到 30 天 availability、error budget、失败 journey |
| Alerting            | 接入 Alertmanager 和 on-call                                                           | SRE 或 DevOps            | P1/P2 alert rules        | 连续失败能触发 P1/P2                                 |
| Baseline report     | 回填近 3 个月 service break                                                              | Platform team           | Baseline report          | 输出当前 availability、MTTA、MTTR、Top root cause    |


阶段验收：

- 平台能回答“过去 30 天 core journey availability 是多少”。
- 至少 5 条核心 user journey 有 synthetic probe。
- E2E workflow canary 可运行，并能定位失败阶段。
- P1 不再只依赖用户提单发现。

### 5.4 阶段 2：止血和重复故障治理

周期：2 到 4 周。


| 工作包                      | 具体任务                                                  | Owner                    | 交付物                        | 验收标准                                        |
| ------------------------ | ----------------------------------------------------- | ------------------------ | -------------------------- | ------------------------------------------- |
| Top root cause fix       | 修复 downtime 排名前 5 的根因                                 | Platform team、DevOps     | Fix backlog                | 同根因 P1 下月不重复                                |
| Runbook                  | 编写登录、KFP、MLflow、artifact、Ingress、Auth、DB、上游依赖 runbook | Platform team            | Runbook set                | P1 runbook 覆盖率 100%                         |
| Workload hardening       | 补齐 replicas、readiness、liveness、startup、resources、PDB  | DevOps                   | Kustomize patches          | 核心服务无单副本                                    |
| Control plane isolation  | 平台控制面与用户 workload 隔离                                  | IT Cloud、DevOps          | Node pool 和 quota 设计       | 用户训练压力不拖垮控制面                                |
| Autoscaling and headroom | 定义 spike scenarios、headroom、HPA 或集群扩容策略               | DevOps、IT Cloud          | Capacity and scaling model | spike scenario 下 success rate 和 latency 可衡量 |
| Checkpoint and resume    | 为支持 checkpoint 的 workflow 建立恢复验证                      | Platform team、MLCA team  | Checkpoint test report     | 模拟故障后可从 checkpoint 恢复                       |
| Maintenance process      | 建立 IT 维护窗口联动流程                                        | Platform owner、IT owners | Maintenance checklist      | 维护前通知、维护后 canary                            |
| Toolset upgrade process  | 建立 K8s、Kubeflow、MLflow 升级流程                           | DevOps、Platform team     | Upgrade checklist          | 每次升级有 pre-check、窗口、回滚、post-upgrade canary   |


阶段验收：

- service break 频率下降。
- P1 MTTA 小于等于 5 分钟。
- P1 mitigation 有 runbook 可执行。
- 至少 1 个月没有同根因 P1 重复。
- 工具集升级超窗或失败会自动转 incident，并进入 RCA。

### 5.5 阶段 3：HA 架构改造

周期：4 到 8 周。


| 工作包                      | 具体任务                                                             | Owner                              | 交付物                        | 验收标准                                           |
| ------------------------ | ---------------------------------------------------------------- | ---------------------------------- | -------------------------- | ---------------------------------------------- |
| MLflow HA                | Tracking server 多副本，backend store 外置 HA DB，artifact store 对象存储化  | Platform team                      | MLflow HA deployment       | metric round-trip 和 registry query 稳定          |
| KFP HA                   | KFP API 多副本，metadata DB HA，artifact store HA                     | Platform team                      | KFP HA deployment          | pipeline submission 和 status query 稳定          |
| Ingress/Auth HA          | Ingress、Gateway、Auth 多副本和 PDB                                    | DevOps、IAM team                    | HA entry path              | 登录 journey 不因单 Pod 或单节点失败中断                    |
| DB and artifact recovery | 建立备份恢复和演练                                                        | DB team、Storage team               | Restore drill record       | RPO/RTO 明确且演练通过                                |
| Backup and restore       | 备份 metadata、artifact、workflow definitions、GitOps config          | Platform team、DB team、Storage team | Backup and restore runbook | 系统损坏或丢失后有最小恢复路径                                |
| Scheduling and placement | 建立 node placement、queue、quota、priority 策略                        | DevOps、IT Cloud                    | Scheduling policy          | workflow 调度到合适 node pool，queue waiting time 可见 |
| GitOps                   | 生产配置进入 GitOps 或等价流程                                              | Platform team、DevOps               | GitOps repo                | 生产变更可审计、可回滚                                    |
| Upgrade hardening        | 对 K8s、Kubeflow、MLflow 升级做 staging、canary、rolling 或 blue-green 策略 | DevOps、Platform team               | Upgrade playbook           | 升级后 core journey canary 通过，失败可回滚               |


阶段验收：

- 单 Pod 或单节点故障不导致核心 journey 整体不可用。
- MLflow 和 KFP 状态层不依赖 SQLite、本地文件、单 PVC 或单实例 DB。
- 至少完成一次 DB 或 artifact restore 演练。

### 5.6 阶段 4：SLO 运营和 SLA readiness

周期：连续 2 到 3 个自然月。


| 工作包                          | 具体任务                                                      | Owner                             | 交付物                          | 验收标准                |
| ---------------------------- | --------------------------------------------------------- | --------------------------------- | ---------------------------- | ------------------- |
| Monthly SLO review           | 每月 review availability、error budget、P1/P2、Top root cause  | Platform owner、SRE、业务方            | SLO review report            | 连续输出月报              |
| RCA closure                  | P1/P2 做 RCA 并关闭 permanent fix                             | Platform team                     | RCA records                  | P1/P2 RCA 完成率 100%  |
| Error budget policy          | 按预算消耗调整发布策略                                               | Engineering manager               | Policy and decision log      | 预算超阈值触发发布治理         |
| Upstream report              | 输出 upstream dependency impact                             | Platform owner、IT owners          | Upstream impact report       | 上游故障和维护影响可解释        |
| Upstream budget review       | Review 上游依赖的 error budget 消耗和 OLA 达成                  | Business owners、IT team、MLOps team | Upstream budget report       | 能看到上游依赖是否威胁总体 99.9% |
| Upgrade report               | 输出 planned upgrade impact、overrun、rollback、change failure | DevOps、Platform owner             | Upgrade impact report        | 每次升级影响可解释、可追踪       |
| Capacity and recovery review | review spike、headroom、checkpoint、restore、placement        | Platform owner、IT Cloud、MLCA team | Capacity and recovery report | 容量、恢复和调度风险有 backlog |
| SLA readiness                | 判断是否可对业务承诺 99.9%                                          | Business owner、Platform owner     | Go or No-Go decision         | 连续 2 到 3 个月达标       |


阶段验收：

- ML Developer Core Journey availability 连续 2 到 3 个月大于等于 99.9%。
- P1 MTTR 稳定小于等于 30 分钟。
- P1 主要由监控主动发现。
- 上游 planned maintenance 和非计划故障有清晰归因。
- 工具集升级的 planned maintenance minutes、overrun minutes 和 upgrade-related incidents 可单独解释。
- E2E workflow canary、capacity baseline、checkpoint resume 和 backup/restore drill 有连续证据。

## 6. 衡量体系

### 6.1 核心度量


| 指标                                | 目标                              | 说明                                                         |
| --------------------------------- | ------------------------------- | ---------------------------------------------------------- |
| Core journey monthly availability | 大于等于 99.9%                      | 最核心的用户感知 SLO                                               |
| Monthly unplanned downtime        | 小于等于 43.2 分钟                    | 30 天自然月 99.9% error budget                                 |
| P1 MTTA                           | 小于等于 5 分钟                       | 衡量发现和响应速度                                                  |
| P1 MTTR                           | 小于等于 30 分钟                      | 衡量恢复能力                                                     |
| Synthetic probe coverage          | 核心 journey 100%                 | 登录、实验、pipeline、MLflow、registry、artifact                    |
| User-ticket first detection ratio | 小于 20%                          | 衡量是否仍然依赖用户报障                                               |
| Repeat P1 root cause              | 0                               | 衡量 RCA 和 permanent fix 有效性                                 |
| Dependency owner coverage         | 100%                            | Azure、Git、Jenkins、Kubernetes cloud、GPU、CPU、memory 均有 owner |
| Upstream SLA coverage             | 100% critical dependencies       | 关键上游服务都有 SLA 或 OLA 记录 |
| Upstream error budget consumed    | 单独统计，超过阈值触发治理                  | 衡量上游依赖对总 43.2 分钟预算的消耗 |
| Upstream unplanned outage minutes | 趋近 0，且必须 RCA                    | 非计划上游中断对 MLOps 用户旅程的影响 |
| Dependency mitigation coverage    | 关键依赖 100% 有缓解方案                | cache、mirror、retry、fallback、escalation、manual procedure |
| Runbook coverage                  | 100% P1 场景                      | 核心故障都有恢复步骤                                                 |
| Planned upgrade impact minutes    | 单独统计                            | K8s、Kubeflow、MLflow 等升级造成的计划维护影响                           |
| Upgrade overrun minutes           | 目标为 0                           | 超出批准维护窗口的不可用时间，应计入 net SLA 和 controllable availability     |
| Upgrade change failure rate       | 趋近 0                            | 升级导致回滚、P1/P2 或额外 service break 的比例                         |
| Post-upgrade canary success       | 100%                            | 升级后核心 ML developer journey canary 必须通过                     |
| E2E workflow canary success rate  | 单独统计并逐步纳入 SLO                   | CDPA、data generation、training、delivery 的代表性 workflow 成功率   |
| Autoscaling reaction time         | 按 spike scenario 设定             | 从突发请求到资源扩容完成的时间                                            |
| Resource headroom                 | 按容量模型设定                         | CPU、memory、GPU、storage、DB connection 的余量                   |
| Queue waiting time                | 按 workload 类型设定                 | workflow 或 training job 等待调度的时间                            |
| Checkpoint resume success rate    | 目标 100% for supported workflows | 支持 checkpoint 的 workflow 在基础设施失败后能恢复                       |
| Restore drill success             | 目标 100%                         | 备份恢复演练成功率                                                  |
| RTO and RPO compliance            | 按对象定义                           | workflow metadata、tracking metadata、artifact 的恢复目标达成情况     |


### 6.2 月报模板

每月 SLO review 建议固定输出：

1. 本月 ML Developer Core Journey Availability。
2. 本月 user-facing availability 和 platform-owned availability。
3. Error budget consumed。
4. P1/P2 事件列表。
5. Top failed journey。
6. Top root cause。
7. Upstream dependency impact。
8. Upstream SLA/OLA attainment 和 upstream error budget consumed。
9. Planned maintenance impact。
10. Toolset upgrade impact，包括 planned minutes、overrun、rollback、post-upgrade canary。
11. E2E workflow canary status。
12. Capacity and spike scenario status。
13. Checkpoint resume、backup restore 和 RTO/RPO compliance。
14. RCA action closure status。
15. 下月 reliability backlog。

## 7. 最小可执行 Backlog

如果只能先做最现实的一批工作，建议按以下顺序：


| 优先级 | Backlog                               | 为什么先做                                           | 完成定义                                                                                 |
| --- | ------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------ |
| P0  | 冻结 ML Developer Core Journey SLO      | 没有范围就无法衡量                                       | 范围、排除项、统计口径确认                                                                        |
| P0  | 建立 5 条核心 synthetic probes             | 先把用户感知路径量起来                                     | login、experiment query、pipeline submission、metric round-trip、artifact round-trip 有指标 |
| P0  | 建立 dependency registry                | 上游 IT 依赖会影响端到端体验                                | Azure、Git、Jenkins、Kubernetes cloud、GPU、CPU、memory 有 owner                            |
| P0  | 建立 upstream SLA/OLA matrix            | 避免总体 SLA 被不可控依赖拖垮                               | 每个关键依赖有 SLA/OLA、排除项、统计窗口、owner 和 budget bucket                             |
| P0  | 定义工具集升级计入口径                           | K8s、Kubeflow、MLflow 升级会造成 planned service break | gross、net SLA、platform-owned 三口径确认                                                   |
| P0  | 设计 E2E workflow canary                | 客户关注完整 workflow solution                        | CDPA、data generation、training、delivery 的 canary 设计完成                                 |
| P0  | 定义 RTO/RPO 和 partial degradation      | 需要明确失败和恢复语义                                     | RTO/RPO matrix 和 partial degradation rules 确认                                        |
| P0  | 输出近 3 个月 baseline report              | 先知道当前差距                                         | availability、MTTA、MTTR、Top root cause 可见                                             |
| P0  | 建立 P1/P2 alert 和 on-call 路由           | 不再等用户提单                                         | 核心 journey 连续失败能触发 on-call                                                           |
| P1  | 建立 capacity baseline 和 spike scenario | 自动扩容和 headroom 需要可衡量                            | spike test、headroom 和 queue waiting time 可见                                          |
| P1  | 建立 upgrade checklist                  | 降低升级造成 service break 的概率                        | pre-check、staging、窗口、回滚、post-upgrade canary 完成                                       |
| P1  | 修复 Top 5 重复根因                         | 最快减少 service break                              | 下月同根因 P1 不重复                                                                         |
| P1  | 补齐多副本、PDB、probes、resources            | 降低单点和维护中断风险                                     | 核心服务无单副本                                                                             |
| P1  | MLflow 和 KFP 状态层 HA 设计                | 状态层是 99.9% 最大风险                                 | HA DB 和 artifact store 方案评审通过                                                        |
| P1  | 建立 checkpoint、backup 和 restore 验证     | 满足故障恢复和灾备需求                                     | checkpoint resume test 和 restore drill 完成                                            |
| P1  | 建立 runbook 和 RCA 模板                   | 降低 MTTR 和复发                                     | P1 runbook 覆盖率 100%                                                                  |
| P2  | SLO-as-code 和 Sloth/OpenSLO           | 提高长期治理质量                                        | SLO YAML 可评审、可发布                                                                     |


## 8. 执行资产与模板

本节合并原独立执行计划中更偏落地操作的内容。后续执行时以本文为唯一主文档，避免需求文档和执行文档分叉。

### 8.1 Incident 基线记录字段

近 3 个月 service break baseline 建议统一记录以下字段，用于计算 availability、MTTA、MTTR、error budget 和 Top root cause：

| 字段 | 说明 |
| ---- | ---- |
| Incident ID | 全局唯一事件编号，建议与 ticket 或 incident 平台关联 |
| Severity | P1、P2、P3 |
| Affected Service | Dashboard、KFP API、MLflow、Ingress、Auth、DB、Artifact store、upstream dependency 等 |
| User Impact | 全部用户不可用、部分 namespace 不可用、单租户不可用、性能严重降级 |
| Alert Start Time | 告警首次触发时间 |
| Acknowledge Time | on-call 确认时间 |
| Incident Start Time | 确认影响平台可用性的开始时间 |
| Mitigation Time | 主要用户路径恢复时间 |
| Full Recovery Time | 根因修复且服务完全恢复时间 |
| Detection Source | synthetic probe、Prometheus alert、用户 ticket、人工巡检 |
| Root Cause Category | 容量、配置、变更、版本兼容、状态层、网络、认证、证书、存储、节点、上游 IT 维护、上游 IT 故障 |
| Upstream Dependency | 是否涉及 Azure auth、Gerrit/Git、Jenkins、Kubernetes cloud、GPU、CPU、memory 等上游服务 |
| Maintenance Window | 是否为已批准维护窗口内事件，是否超出窗口 |
| Immediate Mitigation | 回滚、重启、扩容、切流、恢复备份、禁用异常变更 |
| Permanent Fix | 长期修复动作 |
| Repeat Incident | 是否与历史事件同根因 |
| Counted Downtime Minutes | 计入 availability 的不可用分钟数 |

### 8.2 根因分类与治理动作

| 根因分类 | 典型表现 | 优先治理动作 |
| -------- | -------- | ------------ |
| 状态层单点 | DB、MinIO、PVC、SQLite、本地文件异常导致服务不可用 | HA DB、对象存储、备份恢复、连接池监控 |
| 入口链路故障 | Ingress、Istio Gateway、DNS、TLS、Auth 异常 | 多副本、PDB、配置回滚、证书告警 |
| 资源不足 | CPU、memory、ephemeral storage、DB connection、PVC 满 | requests、limits、HPA、容量告警、配额治理 |
| 节点问题 | NodeNotReady、驱逐、节点维护影响平台 Pod | node pool 隔离、PDB、topology spread |
| 版本兼容 | Kubeflow、Istio、Knative、KServe、Kubernetes 版本不兼容 | 版本矩阵、staging 验证、GitOps 回滚 |
| 配置变更 | VirtualService、Secret、ConfigMap、RBAC、NetworkPolicy 变更错误 | 变更评审、preflight check、canary、rollback |
| 镜像和制品 | ImagePullBackOff、镜像仓库不可用、artifact 下载失败 | 镜像缓存、registry HA、artifact store HA |
| 认证和权限 | 登录失败、token refresh 失败、RBAC 变更影响访问 | auth probe、权限审计、回滚策略 |
| 可观测性缺失 | 用户先发现故障，监控未触发 | synthetic probe、P1 alert、告警链路自监控 |

### 8.3 SLO-as-code 最小模板

建议在内网 Gerrit/Git 中建立 `slo/` 目录，将 SLO、告警、dashboard 和 runbook 作为代码进行评审和发布：

```text
slo/
  mlops-developer-journey.yaml
  prometheus-rules/
  dashboards/
  runbooks/
```

统一指标命名建议：

| 指标 | 含义 |
| ---- | ---- |
| `mlops_developer_journey_success_total` | 按 journey 统计成功次数 |
| `mlops_developer_journey_total` | 按 journey 统计总次数 |
| `mlops_developer_journey_duration_seconds` | 按 journey 统计耗时 |
| `mlops_upstream_dependency_success_total` | 上游依赖探测成功次数 |
| `mlops_upstream_dependency_total` | 上游依赖探测总次数 |

第一阶段执行方式：

1. Gerrit/Git 评审 SLO YAML。
2. Jenkins 校验 YAML schema 和 PromQL 查询。
3. Sloth、OpenSLO 或内部脚本生成 Prometheus recording rules 和 burn-rate alerts。
4. Argo CD 或 Jenkins 将 PrometheusRule 发布到 monitoring namespace。
5. Grafana dashboard 展示 SLO、error budget、burn rate 和 top failed journeys。

### 8.4 Kubernetes 加固和 GitOps 目录模板

关键 workload 至少满足以下标准：

| 能力 | 最低标准 |
| ---- | -------- |
| Replicas | 生产环境 2 到 3 副本，入口类服务优先 3 副本 |
| Readiness probe | 只在服务可接受真实流量时成功 |
| Liveness probe | 检测不可恢复的进程卡死，避免过度重启 |
| Startup probe | 对启动慢的组件单独配置，避免启动期间被 liveness 误杀 |
| Resource requests | CPU 和 memory requests 基于 P95 使用量和扩容策略设定 |
| Resource limits | memory limit 必须设置，CPU limit 根据服务特性谨慎设置 |
| PDB | 最小可用副本至少为 1，核心入口服务建议 `maxUnavailable` 为 1 |
| Topology spread | 副本分布到不同节点或故障域 |
| PriorityClass | 平台控制面优先级高于用户训练 workload |

推荐 GitOps 或 Kustomize 结构：

```text
kubeflow-platform/
  base/
    upstream-release-lock/
    shared-components/
  env/
    dev/
    staging/
    prod/
  patches/
    reliability/
      replicas/
      probes/
      pdb/
      resources/
      topology-spread/
    security/
      auth/
      network-policy/
      secrets/
      tls/
    observability/
      servicemonitor/
      prometheusrule/
      grafana-dashboard/
  runbooks/
  change-management/
```

### 8.5 HA 改造重点

| 组件 | 当前常见风险 | 目标状态 |
| ---- | ------------ | -------- |
| MLflow Tracking Server | 单实例、无 PDB、无 readiness | 多副本、PDB、readiness、HPA |
| MLflow Backend Store | SQLite、本地文件、单实例 DB | HA PostgreSQL 或 MySQL |
| MLflow Artifact Store | 本地文件、单 PVC、单 MinIO | 企业对象存储或 HA MinIO |
| KFP API Server | 单副本、无 HPA、无 PDB | 多副本、HPA、PDB、readiness |
| KFP Metadata DB | 单实例 MySQL 或 PVC | HA PostgreSQL 或 MySQL |
| Ingress Controller | 入口层单点或配置不可回滚 | 2 到 3 副本、PDB、配置审查、5xx 告警 |
| Istio Gateway | 路由层单点 | 多副本、PDB、VirtualService 变更回滚 |
| Auth | 登录和 token 链路不可观测 | login synthetic probe、证书和 secret 监控 |
| CoreDNS | 集群服务发现风险 | 多副本、PDB、CPU 资源保障、DNS latency 告警 |
| cert-manager | 证书过期不可预警 | issuer 健康检查、证书剩余天数告警、续期演练 |

### 8.6 Runbook 与 RCA 模板

第一阶段至少建立以下 runbook：

| Runbook | 触发条件 | 核心动作 |
| ------- | -------- | -------- |
| Dashboard 不可访问 | Dashboard probe 失败 | 检查 Ingress、Auth、Dashboard Pod、recent rollout、logs，必要时回滚 |
| KFP API 不可用 | KFP API probe 失败 | 检查 API Pod、DB connection、metadata DB、Argo、recent rollout |
| MLflow API 不可用 | MLflow probe 失败 | 检查 tracking server、backend store、artifact store、DB connection |
| Ingress 5xx 升高 | Ingress 5xx 告警 | 定位 upstream service、查看 route config、回滚 VirtualService 或 Ingress 变更 |
| Auth 登录失败 | login flow probe 失败 | 检查 auth provider、TLS、redirect URI、secret、token issuer |
| 证书即将过期 | cert alert | 检查 cert-manager、issuer、challenge、secret，同步更新证书 |
| DB connection 耗尽 | DB connection 告警 | 检查连接池、慢查询、异常客户端、扩容或重启泄漏服务 |
| NodeNotReady | 平台节点不可用 | 检查副本分布、驱逐 Pod、隔离节点、确认 PDB 是否阻塞 |
| ImagePullBackOff | 平台 Pod 拉镜像失败 | 检查 registry、imagePullSecret、镜像 tag、网络和镜像缓存 |

每个 P1/P2 RCA 至少包含：

| 部分 | 内容要求 |
| ---- | -------- |
| Summary | 事件一句话描述、影响范围、持续时间 |
| Timeline | Alert、acknowledge、mitigation、full recovery 的时间线 |
| Impact | 受影响服务、受影响用户范围、计入 downtime 分钟数 |
| Root Cause | 技术根因和触发条件 |
| Detection Gap | 是否由监控发现；若由用户 ticket 发现，说明监控缺口 |
| Mitigation | 当次恢复动作和效果 |
| Permanent Fix | 防止复发的工程动作 |
| Prevention Owner | 每个修复动作的 owner |
| Due Date | 每个修复动作的完成日期 |
| Verification | 如何证明修复有效，例如 probe、演练、回归测试 |

### 8.7 SLA readiness 最小文档内容

当 internal SLO 连续 2 到 3 个自然月达标后，正式 SLA 文档至少包含：

| 章节 | 内容 |
| ---- | ---- |
| Service Scope | 纳入 SLA 的服务和链路 |
| Availability Target | 99.9% monthly availability |
| Measurement Method | 统计周期、probe、request success rate、downtime 计算公式 |
| Exclusions | 用户错误、计划维护、不可抗力、未纳入第三方依赖、容量超配请求 |
| Incident Process | P1/P2/P3 分级、响应时间、升级路径 |
| Maintenance Window | 计划维护通知、维护窗口、超窗处理 |
| Upstream Dependency OLA | Azure auth、Gerrit/Git、Jenkins、Kubernetes cloud、GPU、CPU、memory 等上游服务的 owner、OLA、维护窗口和升级路径 |
| Support Hours | 支持时间、on-call 覆盖、升级联系人 |
| Reporting | 月度 availability report、RCA report、error budget report |
| Dependency Responsibility | 第三方服务和基础设施责任边界 |

### 8.8 90 天执行路线图

| 时间 | 重点 | 主要交付 |
| ---- | ---- | -------- |
| Day 0 到 Day 14 | 定义与测量 | 冻结 SLO 范围和排除项，建立 dependency registry 和 upstream SLA/OLA matrix，回填近 3 个月 baseline，上线核心 synthetic probes |
| Day 15 到 Day 45 | 止血与稳定化 | 修复 downtime Top 5 根因，补齐 replicas、resources、probes、PDB，建立 runbook、告警、维护窗口联动和 upgrade checklist |
| Day 46 到 Day 90 | HA 改造 | 完成 MLflow、KFP、Ingress/Auth、DB、artifact store 的 HA 设计和关键改造，建立 GitOps 发布流程，完成 restore drill |
| Day 91 之后 | SLO 运营与 SLA 准备 | 连续 2 到 3 个自然月执行 SLO review，管理 error budget，输出月报、RCA 和 SLA readiness 结论 |

## 9. Go or No-Go

正式对业务承诺 99.9% 前，需要满足以下 Go 条件：


| 维度           | Go 条件                                                     | No-Go 信号                                     |
| ------------ | --------------------------------------------------------- | -------------------------------------------- |
| 数据           | 连续 2 到 3 个月 core journey availability 大于等于 99.9%          | 无法回答过去 30 天真实可用性                             |
| 用户感知         | 核心 user journey 均有 SLI 和 probe                            | 只看 Pod 或组件健康                                 |
| 发现能力         | P1 主要由监控主动发现                                              | 仍主要靠用户提单                                     |
| 恢复能力         | P1 MTTR 小于等于 30 分钟                                        | 单次 P1 超过 43.2 分钟                             |
| 架构           | 核心入口、API、状态层无明显单点                                         | MLflow、KFP、Ingress、Auth 或 DB 单实例             |
| 上游依赖         | 上游 IT owner、OLA、维护窗口和升级路径明确                               | Azure、Git、Jenkins、Kubernetes cloud 维护无预警影响平台 |
| 上游 SLA         | 关键依赖 SLA/OLA、排除项、预算分摊和缓解手段明确                          | 上游服务 SLA 低于 MLOps 目标但仍被无条件纳入 99.9% |
| 工具集升级        | K8s、Kubeflow、MLflow 升级有维护窗口、回滚、post-upgrade canary 和三口径统计 | 升级经常超窗、回滚失败或造成未解释 service break              |
| 端到端 workflow | representative workflow canary 连续运行并可解释失败阶段               | 只测组件，不知道完整 workflow 是否可用                     |
| 恢复能力         | checkpoint resume、backup restore、RTO/RPO 有演练证据            | 系统损坏后无法证明能恢复                                 |
| 容量和调度        | spike、headroom、queue waiting time、placement 有指标           | 突发流量或 GPU 紧张时无法解释 availability               |
| 流程           | on-call、runbook、RCA、error budget 已运行                      | 故障后才临时组织人处理                                  |


## 10. 与现有文档关系

本文已经合并原独立执行计划的路线图、基线统计、SLO-as-code、Kubernetes 加固、HA 改造、SRE 运营和 SLA readiness 内容。后续应以本文作为唯一主文档，避免需求文档和执行文档分叉。

- [[Internal-MLOps-Platform-99.9-Availability-Assessment]]：回答“当前平台为什么不能直接承诺 99.9%，差距在哪里”。
- 本文：回答“从需求到 user story，再到技术分析、执行资产和落地计划，如何组织成可执行项目”。

## 11. 缩写词表

| 缩写 | 全称 | 中文含义 | 在本文中的用法 |
| ---- | ---- | -------- | -------------- |
| API | Application Programming Interface | 应用程序接口 | Kubeflow、MLflow、Kubernetes 等服务的访问接口 |
| CDPA | Context-specific CDPA workflow stage | 客户背景中的 ML workflow 上游阶段 | 端到端 workflow 的起点，后续衔接 data generation、model training 和 model delivery |
| CI/CD | Continuous Integration and Continuous Delivery | 持续集成和持续交付 | Jenkins、Gerrit/Git、镜像构建和平台发布流程 |
| CPU | Central Processing Unit | 中央处理器 | 普通训练、控制面服务和平台组件的计算资源 |
| CRD | Custom Resource Definition | Kubernetes 自定义资源定义 | PrometheusRule、ServiceMonitor、Kubeflow 相关资源的扩展机制 |
| DB | Database | 数据库 | MLflow backend store、Kubeflow metadata、workflow 状态数据的存储 |
| DNS | Domain Name System | 域名解析系统 | 平台入口、服务发现和用户访问链路的基础依赖 |
| E2E | End-to-End | 端到端 | 从 CDPA 到 model delivery 的完整 ML workflow |
| GPU | Graphics Processing Unit | 图形处理器 | 模型训练、推理或高性能计算所需的加速资源 |
| HA | High Availability | 高可用 | 通过多副本、故障切换、备份恢复等方式减少单点故障 |
| HPA | Horizontal Pod Autoscaler | Kubernetes Pod 水平自动扩缩容 | 根据负载自动调整服务副本数，应对突发访问 |
| IAM | Identity and Access Management | 身份与访问管理 | Azure authentication、用户登录、权限校验等能力 |
| IT | Information Technology | 信息技术团队或基础设施团队 | Azure auth、Gerrit、Jenkins、Kubernetes cloud、GPU/CPU/memory 等上游服务 owner |
| ITSM | IT Service Management | IT 服务管理 | 变更、故障、维护窗口、工单和升级路径管理 |
| K8s | Kubernetes | 容器编排平台 | 内部 MLOps 平台的运行底座 |
| KFP | Kubeflow Pipelines | Kubeflow 工作流编排组件 | pipeline 提交、运行状态查询和 workflow canary 的核心组件 |
| KPI | Key Performance Indicator | 关键绩效指标 | 可用于管理层跟踪 availability、MTTR、RCA 完成率等结果指标 |
| ML | Machine Learning | 机器学习 | 本方案服务的模型开发、训练和交付领域 |
| MLCA | Machine Learning Customer/Application team | 客户背景中的模型开发或应用团队 | 代表需要执行 Kubeflow workflow 的用户团队 |
| MLOps | Machine Learning Operations | 机器学习工程运营 | 支撑模型开发、训练、追踪、交付和运维的平台实践 |
| MTTR | Mean Time To Recovery | 平均恢复时间 | 衡量故障从发生到恢复的平均耗时 |
| OLA | Operational Level Agreement | 运营级协议 | IT team 对 MLOps team 提供的内部服务目标，用于支撑上层 SLA |
| P1 | Priority 1 | 一级故障 | 核心用户旅程大范围不可用，需要立即响应 |
| P2 | Priority 2 | 二级故障 | 严重降级或局部不可用，需要优先处理 |
| PDB | PodDisruptionBudget | Pod 中断预算 | 控制维护或升级时可同时不可用的 Pod 数量 |
| RCA | Root Cause Analysis | 根因分析 | P1/P2 故障后的复盘，明确根因、影响和长期修复动作 |
| RPO | Recovery Point Objective | 恢复点目标 | 故障后可接受的最大数据丢失时间 |
| RTO | Recovery Time Objective | 恢复时间目标 | 故障后可接受的最大恢复时间 |
| SLA | Service Level Agreement | 服务等级协议 | 对客户或业务正式承诺的服务等级 |
| SLI | Service Level Indicator | 服务等级指标 | 衡量 SLO 的指标，例如 success rate、latency、downtime |
| SLO | Service Level Objective | 服务等级目标 | 内部或对外定义的可靠性目标，例如 core journey 99.9% |
| SRE | Site Reliability Engineering | 站点可靠性工程 | 用工程化方式管理 availability、error budget、incident 和自动化恢复 |
| TLS | Transport Layer Security | 传输层安全协议 | 平台入口 HTTPS 证书和安全通信能力 |
| YAML | YAML Ain't Markup Language | 常用配置文件格式 | Kubernetes、OpenSLO、PrometheusRule、GitOps 配置常用格式 |

## 12. Sources

- [[Internal-MLOps-Platform-99.9-Availability-Assessment]]
- [[ML-Platform-Availability-SLA-Commercial-Assessment]]
- [Google SRE Workbook - Implementing SLOs](https://sre.google/workbook/implementing-slos/)
- [Google SRE Book - Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [Google SRE - SLO Implementation Case Studies](https://sre.google/workbook/slo-engineering-case-studies/)
- [Google SRE - Art of SLOs](https://sre.google/resources/practices-and-processes/art-of-slos/)
- [OpenSLO Specification](https://github.com/OpenSLO/OpenSLO)
- [OpenSLO website](https://openslo.com/)
- [Prometheus Blackbox Exporter](https://github.com/prometheus/blackbox_exporter/)
- [Prometheus multi-target exporter pattern](https://prometheus.io/docs/guides/multi-target-exporter/)
- [Prometheus Operator](https://prometheus-operator.dev/)
- [Prometheus Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/)
- [Sloth Prometheus SLO Generator](https://sloth.dev/)
- [Sloth GitHub](https://github.com/slok/sloth)
- [Pyrra](https://pyrra.dev/)
- [Pyrra GitHub](https://github.com/pyrra-dev/pyrra)
- [Grafana dashboards documentation](https://grafana.com/docs/grafana/latest/dashboards/)
- [ITIL change enablement overview](https://www.axelos.com/resource-hub/blog/what-is-change-enablement)

## Update History

- 2026-06-02：将原独立执行计划的关键内容整合进本文，新增执行资产与模板章节，覆盖 incident baseline 字段、根因分类、SLO-as-code、Kubernetes 加固和 GitOps 目录、HA 改造、runbook、RCA、SLA readiness 和 90 天路线图；后续不再单独维护独立执行计划文档。
- 2026-06-02：按评审使用场景补充缩写词表，只解释 SLA、SLO、SLI、SRE、OLA、RTO、RPO、RCA、K8s、KFP、PDB、HPA 等常见缩写，便于本文内部直接引用。
- 2026-06-02：补充上游服务 SLA/OLA 纳入方法，明确端到端 availability 的串行依赖风险、gross user-facing availability、net SLA availability、platform-owned controllable availability 三口径、43.2 分钟 error budget 分摊、上游依赖准入规则、缓解手段、upstream SLA/OLA matrix、upstream budget review 和 Go/No-Go 条件。
- 2026-06-02：扩展“采用成熟但内网可执行的实践”章节，补充 Google SRE、OpenSLO、Prometheus Blackbox Exporter、Prometheus Operator、Sloth、Pyrra、Grafana、Alertmanager 和 ITIL change enablement 的参考链接、可借鉴点、内网落地方式与第一阶段产出。
- 2026-06-02：按 Customer、ML developers、MLOps team、IT team、Business owners 五类重新归并 stakeholders，补充各类包含角色、关注点、计划输出、典型决策权，以及 SLA/SLO、用户旅程 SLI、上游依赖、工具集升级、incident/RCA、容量成本权衡的责任关系。
- 2026-06-02：补充客户 background 和 motivation，明确 ML workflow platform 覆盖 CDPA、data generation、model training、model delivery；加入客户 use cases，包括 Kubeflow workflow 执行、autoscaling、stack update、checkpoint resume、backup/restore、scheduling/placement、observability，并扩展需求、user stories、技术分析、落地计划、指标、月报和 Go/No-Go。
- 2026-06-02：补充 DevOps 定期升级 Kubernetes、Kubeflow、MLflow 等 toolsets 造成 service break 的计入口径，明确 gross user-facing availability、net SLA availability、platform-owned controllable availability 三口径，并增加升级 user stories、技术控制点、执行工作包、指标、月报和 Go/No-Go 条件。
- 2026-06-02：创建内部 MLOps 平台 Availability 提升的需求拆解、user stories、技术分析和落地计划，强调 ML developer 用户旅程、内网可执行 SLO 工具链、上游 IT 依赖治理、可衡量验收标准和分阶段落地。

