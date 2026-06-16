---
title: "Production-Grade ML Pipelines: Flyte™ vs. Kubeflow"
source: "https://www.union.ai/blog-post/production-grade-ml-pipelines-flyte-vs-kubeflow"
author:
  - "[[Samhita Alla]]"
published: 2026-01-06
created: 2026-06-15
description: "Kubernetes-native machine learning orchestrators are rocking the ML world: Kubeflow and Flyte™."
tags:
  - "clippings"
---
Want to deploy ML models in production without worrying about managing infrastructure? Meet Flyte™ and Kubeflow. Both are Kubernetes-native platforms that help orchestrate ML workflows and infrastructure. Flyte™ and Kubeflow are uncompromisingly scalable and robust thanks to their Kubernetes compliance, but they offer much different developer experiences. Both address demand for infrastructure orchestrators that support ML orchestration, but Flyte™’s modus operandi is quite different from Kubeflow’s.

## High-Level Comparison

It’s no secret that ML is compute-intensive and complex, and ML orchestrators can speed both pipeline iteration and deployment. Deployment, however, is considered an outlier by ML practitioners focused on building ML pipelines, not working with tools like Docker and Kubernetes to handle resource allocation and infrastructure automation.

Kubeflow Pipelines (KFP) is a platform to build, deploy and scale ML pipelines using Docker containers. In a nutshell, it is an infrastructure orchestrator for ML pipelines that can help put together core ML components to build full-stack pipelines. KFP is one part of the Kubeflow ecosystem and is more comparable with Flyte™. Kubeflow orchestration entails a significant learning curve for many ML engineers because it requires them to understand and code infrastructure constructs. Kubeflow Pipelines v2 is a huge improvement over v1 but imposes a significant overhead for the end users of Kubeflow, especially data scientists, data engineers and ML engineers:

1. Kubeflow is built as a thin layer on top of Kubernetes that automates some Kubernetes management systems. It offers limited management of Kubernetes configuration in Python, but it still requires the user to know how Kubernetes works.
2. If ML practitioners are unfamiliar with Kubernetes, [it’s hard to get Kubeflow deployed, even locally.](https://www.kubeflow.org/docs/components/pipelines/v1/installation/localcluster-deployment/)
3. Kubeflow has a significant learning curve and requires a lot of effort to get it off the ground.
4. The v2 Python DSL isn’t purely Pythonic, which makes it difficult for Python developers to handle.
5. Kubeflow Pipelines v2 supports only a minimal set of type annotations, which makes using it as an extension to Python code cumbersome, error-prone and difficult.
6. Pages labeled “out of date” make it hard to trust Kubeflow documentation.

> *“... \[T\]rying to figure out when we’d done something wrong versus when the problem was outdated documentation. This slowed everything down.” —* [*Kubeflow: Not Yet Ready for Production?*](https://www.datarevenue.com/en-blog/kubeflow-not-ready-for-production)

7. Kubeflow is prone to dependency hell.

> *“For example, upgrading the KFServing component required upgrading Istio. … This upgrade broke access to the dashboard because the newer Istio version was incompatible with AWS authentication.” —* [*Kubeflow: Not Yet Ready for Production?*](https://www.datarevenue.com/en-blog/kubeflow-not-ready-for-production)

Flyte™ was built to make data scientists happy, and data scientists needn’t necessarily know Kubernetes. Although Flyte™’s built primarily on Kubernetes, its primitives abstract away Kubernetes constructs from ML practitioners. The Python SDK of Flyte is identical to writing Python code, and the local deployment requires just two commands: flytectl demo start and pyflyte register <package-or-module>. When using Flyte, ML practitioners don’t need to tinker with Kubernetes constructs (at least on the user side).

Flyte™’s fundamentally different from Kubeflow in three ways:

1. **Flyte™ lets ML practitioners create without having to navigate infrastructure jargon and Kubernetes details.** It segregates the user and the platform teams and lets the user team — data scientists, ML practitioners and data engineers — focus on building models instead of setting up infrastructure. **Kubeflow requires Kubernetes and DevOps expertise**, which may slow down the development of ML pipelines because not all ML practitioners are comfortable with Kubernetes and Ops. Flyte™ is built on Kubernetes, too, and it offers an abstraction that can be removed for complicated use cases; however, 80% of use cases require minimal knowledge of Kubernetes.
2. **Flyte™’s Python SDK (**[**Flytekit**](https://github.com/flyteorg/flytekit)**) lets ML practitioners write Python code, while Kubeflow Python SDK feels like a new/infrastructure DSL**.
3. **Flyte™ supports varied data types and transformations:** You can pass Pandas DataFrames among Flyte™ tasks, load a DataFrame to a BigQuery table using [structured datasets](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/type_system/structured_dataset.html#structureddataset-with-uri-argument), offload data to and download data from cloud URIs using [FlyteFiles](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/flyte_basics/files.html), and more. **Meanwhile, Kubeflow enforces a type system, but it doesn’t support data types beyond fundamental Python types and artifacts/files**. Kubeflow needs to be told what to do when it encounters another type, such as an s3 URI. Flyte™, however, automates the interaction with S3 (and GCS); supports intra- and intercommunication among different cloud services and the local file system; and reduces the need to write boilerplate code.

> *“We've migrated about 50% of all training pipelines over to Flyte™ from Kubeflow. In several cases we saw an 80% reduction in boilerplate between workflows and tasks vs. the Kubeflow pipeline and components.Overall, Flyte™ is a far simpler system to reason about with respect to how the code actually executions, and it's more self-serve for our research team to handle.”  
> —Rahul Mehta, ML Infrastructure/Platform Lead @* [*Theorem LP*](https://www.theoremlp.com/)

## Feature Comparison

When choosing an [orchestrator](https://www.union.ai/blog-post/orchestration-for-data-machine-learning-and-infrastructure), it’s vital to consider the features you need as well as the ease with which you can deploy and iterate. It’s important to be able to iterate on your ML pipelines quickly, catch bugs early on, deploy seamlessly on any cloud provider, and ultimately alleviate the complexity and pain points of ML practitioners.

With Kubeflow, there’s no question about deployment — it scales really well. It also has an extensive number of integrations. However, the developer experience isn’t too good.

The following table offers a feature comparison between Flyte™ and Kubeflow.

Multi-Tenancy

Type Checking

Caching

Sub DAG

Data Lineage

Scalability

Map Tasks

Dynamic DAGs

~

Retries

Reruns

Scheduling

Branching

Task Timeout

Spark Support

Extensible

Notifications

Recovery

Intratask Checkpointing

Note: Kubeflow Pipelines v2 is in the pre-release stage and not yet stable. The v2 docs are being continually improved, and links to v2 documentation are not yet stable.

Flyte™ ticks all the boxes, whereas Kubeflow, although performant and scalable, requires Kubernetes and DevOps expertise. Let’s take a look at the features in more detail:

### Components and Tasks

[Flyte tasks](https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.task.html#flytekit-task) are independent units of execution that when run in a specific order produce a [Flyte workflow](https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.workflow.html). The functional equivalents in Kubeflow are [component](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/components) and [pipeline](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/pipelines/), respectively. However, Kubeflow’s way of constructing pipelines isn’t as straightforward as Flyte™’s because:

1. The output type annotation needs to be declared in the input arguments declaration in case of [custom container components](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/components/#3-custom-container-components) and [output artifacts](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/component-io/#output-artifacts).
2. An output from a [lightweight Python component](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/components/#1-lighweight-python-function-based-components) can be passed as an input to a downstream component only using the.output attribute of the source task.
3. Kubeflow’s [containerized](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/components/#2-containerized-python-components) and [custom container components](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/components/#3-custom-container-components) are inclined to infrastructure DSL, unlike [lightweight components](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/components/#1-lighweight-python-function-based-components) which are Pythonic. Code imported from different modules must be refactored to use containerized components, which generates friction in the developer experience and hinders development cycles.
4. Kubeflow prefers containerized and custom container components to lightweight components for production usage — thus moving a step closer to infrastructure DSL.

> *“Lightweight components should be used if your component implementation can be written as a standalone Python function and does not require an abundance of source code. … For more involved components and for production usage, prefer containerized components and custom container components for their increased flexibility.” —* [*Kubeflow pipelines v2 docs*](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/components/)

5. Single-component executions aren’t supported, which might be useful in cases where a standalone component’s functionality needs to be tested.

Flyte™ addresses all the above pain points because:

- Flyte™’s tasks are akin to Python functions. Inputs and outputs can be handled like a typical Python function that doesn’t need to call attributes. In addition, output type annotations needn’t be declared as part of input arguments declaration.
- All Flyte™ task variants — including dynamic workflows, reference tasks and map tasks — may use different decorators, but the fundamental behavior remains the same.
- Code can be imported from Flyte™ modules the same way as Python modules. Registered tasks can also be imported using the [reference\_task](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/flyte_basics/reference_task.html) decorator.
- Flyte™ task is very much preferred for production usage and can adapt to all kinds of use cases.
- Single-task executions are supported by Flyte™ and can simplify iterating on the task’s definition without having to write a new workflow definition.
![](https://cdn.prod.website-files.com/690e5501abec15e3292c8f97/691d049262a2cbe71bbb17ee_64028677e7e50aef800a58b7_635475e60af27db6d6ccb589_6352d8ce482c5598ad08adb7_DFiNVyR8r0p81bAGX_JEKziIX6SrmHxxig3eKeelzQkdFBd_6ele2-lvZPepXG1QZ4eQ1W2PYnjaGH_FFgGe21x1c90zQRjsAcHbkzyQ9WAJpkvcMo5uqDpTkrJuXEThjtVNSgOBRmnbh2bwwNCLH-MnvLCzNBzga_5IVxqa_bVLN1bvfKty7yoHDg.webp)

Workflow nodes on the Flyte™ UI

> *Flyte™ also supports* [*workflow offloading*](https://github.com/flyteorg/flyte/issues/2705) *and launch-plan composition, and it doesn’t repeat tasks multiple times. Hence, workflows can be gigantic — in some cases, up to 100k+ nodes!*

### Launch Plans

Often you’ll want to trigger a workflow/pipeline with different sets of inputs. For example, you may want to share a workflow with all the inputs set with a colleague who can then simply kick off the execution. You may also want to share a workflow with a different set of inputs with another colleague. In such a case, it’s beneficial to create launch plans to launch your workflows.

Kubeflow enables scheduling a pipeline multiple times with different sets of inputs; however, for one-off executions, in order to create multiple experiments, you ought to compile, get the IR YAML file and create an experiment. A single pipeline can have multiple experiments, but the code needs to be compiled prior to creating an experiment. Moreover, no other parameters apart from the input arguments can be provided during the compilation step.

Flyte™ enables ML practitioners to create [launch plans](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/flyte_basics/lp.html) that bind a partial or complete list of inputs along with optional run-time overrides (like a service account, notifications or annotations.) This critical feature enhances team collaboration and enables you to issue run-time overrides right from your Python code.

![](https://cdn.prod.website-files.com/690e5501abec15e3292c8f97/691d049262a2cbe71bbb17e5_64028677e7e50a2eb90a58b9_635475e64f90fd3187a4a546_6352d8cfd33e6aa63e1f5821_QjAC5t7y1uJlTrDIVQhn_JatATq3iuwaPCxSPH4ERKBmm-q_69sCV0NZEqwrDX3XY3VuSwS5n8f8imE8DsNwsBN2kw57afXcb09op-m_xtutUWnQKZKY4-IDyhBWcb6s2P1ve8dxHZM5QGBSbJQc_dMso1ItnYSK73OqvhLe1VO_yRv2bbfyvo0HUg.webp)

Launch plan selection on the Flyte™ UI

### Map Tasks

Map tasks are helpful to run an operation over a static/dynamic list of inputs. Use cases of map tasks include:

- Several inputs running through the same code logic
- Multiple data batches processed in parallel
- Hyperparameter optimization

With Kubeflow ParallelFor — a parallel for loop over a set of items — data passing isn’t easy to implement because the [collection of outputs over a dynamic set of items isn’t straightforward](https://github.com/kubeflow/pipelines/issues/3412). Also, ParallelFor in Kubeflow is a high-level construct. The Flyte equivalent to ParallelFor is a deeper integration called [map task](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/control_flow/map_task.html) that enables quicker iterations with little overhead and works well for large fan-out tasks. Because Flyte can run map tasks within a single workflow node, it doesn’t create a node for every instance, which boosts performance.

### Dynamism in DAGs

For the most part, ML is dynamic, so it’s important to be able to construct dynamic DAGs. Here are some example use cases taken from the [Flyte dynamic workflows blog post](https://blog.flyte.org/dynamic-workflows-in-flyte):

- If a dynamic modification is required in the code logic, such as determining the number of training regions, programmatically stopping the training if the error surges, introducing validation steps dynamically, or data-parallel and sharded training
- During feature extraction, if there’s a need to decide on the parameters dynamically
- Building an AutoML pipeline
- Tuning hyperparameters dynamically while a pipeline is in progress

Kubeflow supports dynamism with [DSL recursion](https://www.kubeflow.org/docs/components/pipelines/v1/sdk/dsl-recursion/), which presents its own set of problems: It’s a little awkward to construct dynamic DAGs with recursion, [it doesn’t work well with deep workflows](https://github.com/kubeflow/pipelines/issues/1065), output cannot be dynamically resolved and types are ignored. Moreover, KFP v2 doesn’t yet provide support for recursion.

In Flyte, dynamic workflows enable the construction of dynamic DAGs. When a Flyte task is decorated with @dynamic, Flyte evaluates the code at runtime and determines DAG structure. [Flyte dynamic workflows](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/control_flow/dynamics.html) offer much more flexibility to compose and run dynamic DAGs:

- Dynamism isn’t restricted to recursion
- Data passing isn’t any different from general Flyte tasks
- Types are respected

### Type Checking

Python is a dynamically typed programming language. That means it checks types at runtime as opposed to compile-time. It also supports the concept of [gradual typing](https://peps.python.org/pep-0483/), which means you can gradually introduce types into your code. Putting type hints to work in Python is increasingly becoming important because:

- Type hints help catch certain errors before running the code
- Type hints help document your code
- Type hints improve IDEs and linters

Flyte is a strong supporter of type validation and it already [provides full support for various Python types](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/type_system/flyte_python_types.html#sphx-glr-auto-core-type-system-flyte-python-types-py). ML-specific types like [torch.Tensor](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/type_system/pytorch_types.html), [torch.nn.Module](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/type_system/pytorch_types.html), np.ndarray and Spark DataFrame type [pyspark.DataFrame](https://docs.flyte.org/projects/cookbook/en/latest/auto/integrations/kubernetes/k8s_spark/dataframe_passing.html) are also natively supported by Flyte, which ensure that ML pipelines are foolproof.

Flyte also type-checks input arguments in launch forms on the UI.

![](https://cdn.prod.website-files.com/690e5501abec15e3292c8f97/691d049262a2cbe71bbb17e0_64028677e7e50aed5c0a58b8_635475e64f90fd1f0ba4a547_6352d8cfd7ab143634f9ee64_53npQvTwGvQtme5PzJ-t3DI2wZoMCw_qQVdcMsJYTpaIhuQgtDjZXckwYlY0utVhWnadF_U3OoIksn-K1s1657Fn_kcKeZ5z8pkzce3aC8z75GwnRcXTOx5FkhHDfodf6Aqe_LLLpWFjoE0i_fDPhOSbPu7en6uLNGsOmi8Ah-9oqocPg4pQSBMLPw.webp)

Why haven’t you given day\_of\_week? By the way, number is an integer!

Kubeflow’s type-checking is brittle. Only a handful of types are validated by Kubeflow — and not on the UI. Boilerplate code often finds its way into Kubeflow code, e.g., if specifying an [output artifact](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/component-io/#output-artifacts), a dataset/model artifact needs to be saved to the output artifact.path every time it’s returned as an output of a Kubeflow component. pandas.DataFrame — a standard data structure widely used in data-intensive fields — isn’t supported either. Moreover, no ML-specific types are supported by Kubeflow, although Kubeflow’s primarily used for ML pipelines.

### Notifications

Notifications are particularly helpful when a job fails. Imagine not getting notified when a critical pipeline fails and goes unnoticed. Kubeflow doesn’t provide any native support to notify users; the notification mechanism can only be implemented by relying on [Argo](https://github.com/kubeflow/pipelines/issues/3516), [VertexAI](https://cloud.google.com/vertex-ai/docs/pipelines/email-notifications) or a [custom handler](https://stackoverflow.com/a/57586000/9695360). Flyte, on the other hand, [supports sending notifications via email, Slack and PagerDuty](https://docs.flyte.org/en/latest/deployment/cluster_config/notifications.html). Users can also schedule notifications to alert them when a workflow succeeds or fails.

### Raw Containers

Often you may want to rely on a custom Docker image that you built to run your pipelines. Kubeflow supports providing custom Docker images with containerized components. Custom images can be built by running kfp component build src/ --push-image where src contains all the source code. The pipeline can then be compiled and executed like any other Kubeflow pipeline.

Flyte supports raw containers using the [ContainerTask](https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.ContainerTask.html#flytekit.ContainerTask%5C) class. Custom images can be provided using the target\_image argument of @task but to have more control over the container, a ContainerTask can be used. The registration and execution of code on the Flyte backend follows the same pattern as that of a regular @task which simplifies the iteration of workflows.

### Fast Registration

[As per the Kubeflow docs](https://www.kubeflow.org/docs/components/pipelines/v2/author-a-pipeline/components/), containerized components can be used in production; however, the additional build step that needs to be triggered to build the Docker image hinders the iteration of pipelines because the image needs to be built every time there’s a code change.

In Flyte, a custom image can be provided while registering the workflows using the command pyflyte register --image <image> <package-or-module> when additional dependencies are required than those provided by the default [flytekit image](https://github.com/flyteorg/flytekit/blob/master/Dockerfile.py3.10); however, a docker image need not be built every time there’s a code change. This is known as [fast registration](https://docs.flyte.org/projects/cookbook/en/latest/auto/deployment/deploying_workflows.html#fast-registration) which is enabled by default in the pyflyte register command. It saves time and speeds development.

### Type Transformers

Kubeflow’s type system currently supports a fairly limited set of types, and [there’s no plug-in support available to add custom types](https://github.com/kubeflow/pipelines/issues/6304). Flyte, on the other hand, enables adding custom types using [Type Transformers](https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.extend.TypeTransformer.html#flytekit-extend-typetransformer), e.g., refer to [PyTorch2ONNX](https://github.com/flyteorg/flytekit/blob/b7ecdf60768bf8b03a849947d5e2cab0fccde1e3/plugins/flytekit-onnx-pytorch/flytekitplugins/onnxpytorch/schema.py#L85-L140) type. Type Transformers are simple to understand and contribute to the Flyte type system.

### Model Serving

Kubeflow ships with several serving integrations to serve ML models, including [BentoML](https://www.bentoml.com/), [Seldon](https://www.seldon.io/), [Triton](https://developer.nvidia.com/nvidia-triton-inference-server) and [KServe](https://kserve.github.io/website/0.9/). Flyte doesn’t currently ship with any model serving integrations, but [UnionML](https://github.com/unionai-oss/unionml) — an ML wrapper built on Flyte, supports FastAPI for serving and BentoML — is slated for the upcoming UnionML release.

### Intra-Task Checkpoints

Checkpointing is an important feature when training ML models. Training is expensive, and storing snapshots of the model lets you continue subsequent executions from the failed state instead of running them from the beginning.

[Flyte provides an intra-task checkpointing feature](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/control_flow/checkpoint.html#sphx-glr-auto-core-control-flow-checkpoint-py) that can be leveraged from within @task. This feature supports the use of AWS spot instances or GCP preemptible instances to lower costs.

Kubeflow allows running pipelines on spot instances. However, no checkpointing feature is provided by it, and thus, the progress of execution is bound to be lost.

### Backend Plugins

Kubeflow can be extended to accommodate other platforms but the integrations for the most part are bulky in the case of backend plugins.

Because [Flyte backend plugins](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/extend_flyte/backend_plugins.html) don’t require you to run pods for simple API calls, integrations are less bulky. For easier debugging, the Flyte UI includes queries to services and other relevant details.

![](https://cdn.prod.website-files.com/690e5501abec15e3292c8f97/691d049262a2cbe71bbb17e8_64028677e7e50a47630a58b5_635475e66e708a42c15c70c0_6352d8cec122e414ecbe8ee9_gzbvNqAwpwtxxGtkBZrgjWyj0bTKpW9yDjQZiflossiifDryoAoC06OEp8D9Q59-Jsf8H36f-bOn1rB7wxGT29m0ShRmfTyL_Zfva3i9Y5RJqZ4XCSq5hwZCIWKFo1N1K2_al0SZo5rwpBxsGzNBq3TMO8pkdD5IY4eu6Z9zm4lN9nTs_uXzNPUQXw.webp)

Link to Athena query console on the Flyte UI

### Recovery Mode

Recovery mode in Flyte makes it easy to recover an individual execution by copying all successful node executions and running from the failed nodes. The “recover” button on the Flyte UI helps recover a failed execution. This is a critical feature for compute-intensive ML workflows; running a workflow from scratch when an abrupt failure crops up irrespective of the status of a task consumes resources unnecessarily. Ideally, skipping successful task node executions means better resource management and quicker iterations.

![](https://cdn.prod.website-files.com/690e5501abec15e3292c8f97/691d049262a2cbe71bbb17eb_64028677e7e50a19500a58b6_635475e6d7135d3149f6043c_6352d8ce844a1705cee6af08_fLOL_7H7s5zq5_kldsgfkun7a1zk88JhfrTOS_XDDr7XdAln5xq3tfgbFBnC0_3_2aZ4-hotp1HxV6AF0EjsrDoQ2glf41gK05SYPdiN85BWMJW66zIo08Wnqh_5uwthXYIlm9pXzbyQDVXxpCkjEqOisblouOro9V73fwIx6glKDXfYgAtn2s1CkQ.webp)

Recover button on the Flyte UI

Kubeflow doesn’t currently support recovering partial executions. Without checkpointing or recovery mode, pipelines must run from scratch after an abrupt failure.

In the next section, let’s look at how Kubeflow’s code ergonomics differ from Flyte's.

## Code Ergonomics Comparison

In this section, we compare Flyte and Kubeflow approaches to defining simple and advanced ML pipelines, using passages copied from the Kubeflow [quickstart guide](https://www.kubeflow.org/docs/components/pipelines/v2/quickstart/). This should also serve as a migration guide in case you want to migrate from Kubeflow to Flyte.

### Simple Pipeline

#### Kubeflow Pipelines v2

###### Code

```python
from kfp import dsl
from kfp import client

@dsl.component
def addition_component(num1: int, num2: int) -> int:
    return num1 + num2

@dsl.pipeline(name='addition-pipeline')
def my_pipeline(a: int, b: int, c: int = 10):
    add_task_1 = addition_component(num1=a, num2=b)
    add_task_2 = addition_component(num1=add_task_1.output, num2=c)
```

###### Trigger code via CLI

```bash
kfp dsl compile --py path/to/pipeline.py --output path/to/output.yaml

kfp run create --experiment-name my-experiment --package-file path/to/output.yaml
```

###### Trigger code via Python SDK

```python
endpoint = '<KFP_ENDPOINT>'
kfp_client = client.Client(host=endpoint)
run = kfp_client.create_run_from_pipeline_func(
    my_pipeline,
    arguments={
        'a': 1,
        'b': 2    },

)
url = f'{endpoint}/#/runs/details/{run.run_id}'
print(url)
```

#### Flyte

###### Code

```python
from flytekit import task, workflow

@task
def addition_component(num1: int, num2: int) -> int:
   return num1 + num2

@workflow
def my_pipeline(a: int, b: int, c: int = 10):
   add_task_1 = addition_component(num1=a, num2=b)
   add_task_2 = addition_component(num1=add_task_1, num2=c)
```

###### Trigger code via CLI

```bash
pyflyte run --remote example.py my_pipeline --a 1 --b 2
```

###### Trigger code via Python SDK

```python
from flytekit.configuration import Config
from flytekit.remote import FlyteRemote

from <your-module> import my_pipeline

remote = FlyteRemote(
   config=Config.auto(),
   default_project="flytesnacks",
   default_domain="development",
)

registered_workflow = remote.register_script(
   my_pipeline,
   source_path="../../", # depends on where __init__.py file is present
   module_name="<your-module>",
)

execution = remote.execute(
   registered_workflow,
   inputs={"a": 100, "b": 19},
)
print(f"Execution successfully started: {execution.id.name}")
```

A Flyte workflow / task can be triggered:

- from the CLI
- on the UI
- Programmatically using the [FlyteRemote](https://docs.flyte.org/projects/flytekit/en/latest/design/control_plane.html) API

### Advanced ML Pipeline

#### Kubeflow Pipelines v2

###### Code

```python
from typing import List

from kfp import client
from kfp import dsl
from kfp.dsl import Dataset
from kfp.dsl import Input
from kfp.dsl import Model
from kfp.dsl import Output

@dsl.component(packages_to_install=['pandas==1.3.5'])
def create_dataset(iris_dataset: Output[Dataset]):
    import pandas as pd

    csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    col_names = [
        'Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Labels'
    ]
    df = pd.read_csv(csv_url, names=col_names)

    with open(iris_dataset.path, 'w') as f:
        df.to_csv(f)

@dsl.component(packages_to_install=['pandas==1.3.5', 'scikit-learn==1.0.2'])
def normalize_dataset(
    input_iris_dataset: Input[Dataset],
    normalized_iris_dataset: Output[Dataset],
    standard_scaler: bool,
    min_max_scaler: bool,
):
    if standard_scaler is min_max_scaler:
        raise ValueError(
            'Exactly one of standard_scaler or min_max_scaler must be True.')

    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.preprocessing import StandardScaler

    with open(input_iris_dataset.path) as f:
        df = pd.read_csv(f)
    labels = df.pop('Labels')

    if standard_scaler:
        scaler = StandardScaler()
    if min_max_scaler:
        scaler = MinMaxScaler()

    df = pd.DataFrame(scaler.fit_transform(df))
    df['Labels'] = labels
    with open(normalized_iris_dataset.path, 'w') as f:
        df.to_csv(f)

@dsl.component(packages_to_install=['pandas==1.3.5', 'scikit-learn==1.0.2'])
def train_model(
    normalized_iris_dataset: Input[Dataset],
    model: Output[Model],
    n_neighbors: int,
):
    import pickle

    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier

    with open(normalized_iris_dataset.path) as f:
        df = pd.read_csv(f)

    y = df.pop('Labels')
    X = df

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train, y_train)
    with open(model.path, 'wb') as f:
        pickle.dump(clf, f)

@dsl.pipeline(name='iris-training-pipeline')
def my_pipeline(
    standard_scaler: bool,
    min_max_scaler: bool,
    neighbors: List[int],
):
    create_dataset_task = create_dataset()

    normalize_dataset_task = normalize_dataset(
        input_iris_dataset=create_dataset_task.outputs['iris_dataset'],
        standard_scaler=standard_scaler,
        min_max_scaler=min_max_scaler)

    with dsl.ParallelFor(neighbors) as n_neighbors:
        train_model(
            normalized_iris_dataset=normalize_dataset_task
            .outputs['normalized_iris_dataset'],
            n_neighbors=n_neighbors)
```

###### Trigger code via CLI

```bash
kfp dsl compile --py path/to/pipeline.py --output path/to/output.yaml

kfp run create --experiment-name my-experiment --package-file path/to/output.yaml
```

###### Trigger code via Python SDK

```python
endpoint = '<KFP_UI_URL>'
kfp_client = client.Client(host=endpoint)
run = kfp_client.create_run_from_pipeline_func(
    my_pipeline,
    arguments={
        'min_max_scaler': True,
        'standard_scaler': False,
        'neighbors': [3, 6, 9]
    },
)
url = f'{endpoint}/#/runs/details/{run.run_id}'
print(url)
```

#### Flyte

###### Code

```python
from dataclasses import dataclass
from typing import List

import pandas as pd
from dataclasses_json import dataclass_json
from flytekit import map_task, task, workflow
from flytekit.types.structured import StructuredDataset
from sklearn.base import ClassifierMixin
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler

COL_NAMES = ["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width", "Labels"]

@dataclass_json
@dataclass
class TrainInputs:
   normalized_iris_dataset: StructuredDataset
   n_neighbors: int

@task
def create_dataset() -> pd.DataFrame:
   csv_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
   df = pd.read_csv(csv_url, names=COL_NAMES)
   return df

@task
def normalize_dataset(
   input_iris_dataset: pd.DataFrame, standard_scaler: bool, min_max_scaler: bool
) -> pd.DataFrame:
   if standard_scaler is min_max_scaler:
       raise ValueError(
           "Exactly one of standard_scaler or min_max_scaler must be True."
       )

   labels = input_iris_dataset.pop("Labels")

   if standard_scaler:
       scaler = StandardScaler()
   if min_max_scaler:
       scaler = MinMaxScaler()

   df = pd.DataFrame(
       scaler.fit_transform(input_iris_dataset),
       columns=set(COL_NAMES) - set(["Labels"]),
   )
   df["Labels"] = labels
   return df

@task
def train_model(input: TrainInputs) -> ClassifierMixin:
   df = input.normalized_iris_dataset.open(pd.DataFrame).all()
   y = df.pop("Labels")
   X = df

   X_train, _, y_train, _ = train_test_split(X, y, random_state=0)

   clf = KNeighborsClassifier(n_neighbors=input.n_neighbors)
   clf.fit(X_train, y_train)

   return clf

@task
def prepare_map_inputs(
   list_neighbors: List[int], normalized_iris_dataset: StructuredDataset
) -> List[TrainInputs]:
   return [
       TrainInputs(normalized_iris_dataset, neighbor) for neighbor in list_neighbors
   ]

@workflow
def my_pipeline(standard_scaler: bool, min_max_scaler: bool, neighbors: List[int]):
   create_dataset_task = create_dataset()
   normalize_dataset_task = normalize_dataset(
       input_iris_dataset=create_dataset_task,
       standard_scaler=standard_scaler,
       min_max_scaler=min_max_scaler,
   )
   map_task(train_model)(
       input=prepare_map_inputs(
           list_neighbors=neighbors, normalized_iris_dataset=normalize_dataset_task
       )
   )
```

###### Trigger code via CLI

```bash
pyflyte run --remote --image ghcr.io/flyteorg/flytecookbook:core-latest test.py my_pipeline --standard_scaler --neighbors '[3,6,9]'
```

###### Trigger code via Python SDK

```python
from flytekit.configuration import Config, ImageConfig
from flytekit.remote import FlyteRemote

from <your-module> import my_pipeline

remote = FlyteRemote(
   config=Config.auto(),
   default_project="flytesnacks",
   default_domain="development",
)

registered_workflow = remote.register_script(
   my_pipeline,
   source_path="../../", # depends on where __init__.py file is present
   module_name="<your-module>",
   image_config=ImageConfig.from_images("ghcr.io/flyteorg/flytecookbook:core-latest"),
)

execution = remote.execute(
   registered_workflow,
   inputs={"standard_scaler": True, "min_max_scaler": False, "neighbors": [3, 6, 9]},
)
print(f"Execution successfully started: {execution.id.name}")
```

Flyte is more closely aligned with Pythonic syntax than Kubeflow, which seems to have its own DSL. The code execution experience remains the same but local deployment (spinning up a relevant cluster) is [far easier with Flyte](https://docs.flyte.org/en/latest/getting_started/index.html) than [with Kubeflow](https://www.kubeflow.org/docs/components/pipelines/v1/installation/localcluster-deployment/).

### The Problem with Triggering Executions in Kubeflow

The Trigger(CLI) sections in the above tables specify the commands to run to compile and execute the workflow/pipeline. Kubeflow CLI provides two commands to compile-and-create the execution on the Kubeflow backend:

- kfp dsl compile --py <python-file> --output <compiled-result-path>
- kfp run create --experiment-name <> --package-file <pipeline-package>

If the python-file consists of multiple components or pipelines, --function argument can be used to specify the component/pipeline that needs to be compiled. With Flyte, however, multiple tasks and workflows can be serialized/compiled and registered with a single command.

The following three commands serialize and register code on the Flyte backend:

- pyflyte run --remote <python-file> <workflow-or-task>
- pyflyte register <package-or-module>
- pyflyte --pkgs <package> package + flytectl register files --project <project> --domain <domain> --archive <archive> --version <version>

pyflyte run is a lightweight, convenient command that operates on a single file and is easy to implement. pyflyte register is more of a production-grade command that can register multiple workflows and tasks at the same time. pyflyte package + flytectl register is helpful when there are multiple [FlyteAdmins](https://docs.flyte.org/en/latest/concepts/admin.html) and can compile-register-execute multiple tasks and workflows.

### Providing Custom Images

A component in Kubeflow and a task in Flyte may need to be associated with custom images if the dependencies are specialized (This is a standard use case in ML workflows), in which case the Kubeflow component is called a “containerized component.

###### Kubeflow Pipelines v2

```python
@dsl.component(
   base_image='python:3.7',
   target_image='gcr.io/my-project/my-component:v1',
   packages_to_install=['tensorflow'],
)
def train_model(
   dataset: Input[Dataset],
   model: Output[Model],
   num_epochs: int,
):
   ...
```

###### Flyte

```python
@task(
   container_image="ghcr.io/my-project/my-component:v1"
)
def train_model(
   dataset: pd.DataFrame,
   model: FlyteFile,
   num_epochs: int
):
   ...
```

## Union Cloud: Hosted Flyte™

Your choice of orchestrator plays a vital role in determining how quickly you can get your pipelines into production and the time you spend fixing errors that hinder the development and deployment processes.

[Union Cloud](https://www.union.ai/cloud), a hosted version of Flyte, simplifies the maintenance and deployment of Flyte, freeing data and ML teams from infrastructure setup and constraints. In no time, you can get your Flyte cluster up and running to deploy your workflows. [Join our waitlist](https://www.union.ai/waitlist) to try Union Cloud!

## Conclusion

Kubeflow is a sophisticated tool for ML practitioners who are well-versed in Kubernetes or OK with the learning curve it imposes. For teams who want to hit the ground running right away, Kubeflow may be an impediment, and [Kubeflow alternatives](https://neptune.ai/blog/the-best-kubeflow-alternatives) have long been a [topic of discussion](https://www.reddit.com/r/MachineLearning/comments/evsdet/d_alternatives_to_kubeflow/).

Flyte was designed to help ML practitioners create production-grade ML pipelines in no time. Flyte leverages the scalability offered by Kubernetes but abstracts away its language to make it more accessible to ML teams. We also recommend you check out [UnionML](https://github.com/unionai-oss/unionml) for a simplified experience while leveraging the ML capabilities of Flyte.

Many companies have made the transition from Kubeflow to Flyte, and we’ve heard teams tell us about the time they’ve saved developing and deploying ML pipelines. We hope Flyte can help you, too.

**Flyte Resources:**

- [GitHub](https://github.com/flyteorg/flyte)
- [Docs](https://docs.flyte.org/)
- [Slack](https://slack.flyte.org/)
- [Blog](https://blog.flyte.org/)
- [Twitter](https://twitter.com/flyteorg)
- [YouTube Channel](https://www.youtube.com/channel/UCNduEoLOToNo3nFVly-vUTQ/playlists)

**Kubeflow Resources:**

- [GitHub](https://github.com/kubeflow/kubeflow)
- [Docs](https://www.kubeflow.org/docs/)
- [Blog](https://blog.kubeflow.org/)
- [Slack](https://www.kubeflow.org/docs/about/community/#kubeflow-slack)
- [Twitter](https://twitter.com/kubeflow/)

Let us know what you think of this piece. We’d love to hear from you!

[

Try the devbox

](https://www.union.ai/get-devbox)

A free, local sandbox to explore the Union.ai platform.

[

Chat with an engineer

](https://www.union.ai/get-started)

No items found.