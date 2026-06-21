---
title: "AI 语音技术详解：从 ASR、TTS 到实时语音 Agent 的工程化落地 — JavaGuide"
tags:
  - source
  - ai-voice
  - javaguide
  - realtime
  - asr
  - tts
created: 2026-06-21
updated: 2026-06-21
source: "https://javaguide.cn/ai/system-design/ai-voice.html"
author: "Guide (JavaGuide)"
---

# AI 语音技术详解：从 ASR、TTS 到实时语音 Agent 的工程化落地 — JavaGuide

> 拆解 AI 语音系统的工程链路，涵盖音频采集、VAD、ASR、LLM、TTS、流式播放、打断处理、低延迟优化以及云端 API、本地模型、端云混合选型。基于 interview-guide 项目实战代码讲解。

## Core Contributions

1. **完整语音对话链路**：音频采集→前处理（AEC/NS/AGC）→VAD 检测→音频上传→ASR 转写（流式增量结果）→上下文组装→LLM 推理→TTS 合成（流式音频块）→音频下行→状态回写。强调：实时语音不能等用户说完才开始工作，能并行的事提前启动。

2. **ASR 三条技术路线**：云端 API（OpenAI/Azure/Deepgram，接入快但成本和数据合规受限）、开源通用模型（Whisper/faster-whisper/FunASR，可本地部署）、领域定制模型（金融/医疗专用，适配好但成本高）。选型建议：实时对话不要只看离线 WER，更应关注首段延迟、增量结果稳定性、端点检测准确率。

3. **TTS 技术路线与实时策略**：传统流水线（文本规范化→文本分析→声学模型→声码器）vs 端到端模型（VALL-E/Fish Speech/CosyVoice）。对实时语音 Agent 来说，单句音质不是最关键的，流式可播放性才是。建议按语义边界切分（句号>分号>逗号>超长句强制切分）。

4. **VAD 的"隐形守门人"角色**：端侧 VAD（WebRTC VAD/Silero VAD）响应快但部署和调参成本高，服务端 VAD（DashScope server_vad/OpenAI turn detection）客户端简单但有网络延迟。建议：VAD 不要只当开关用，应输出一组对话控制信号（speech_start/speech_end/maybe_barge_in/noise_only）。

5. **打断处理的三层含义**：播放层打断（停止当前音频）、生成层打断（取消 LLM/TTS 生成）、上下文层打断（正确记录已播放和未播放内容）。状态机视角的打断：几乎可以从任何状态进入（listening/thinking/speaking/tool_calling）。

6. **级联式 vs 原生 Realtime API 对比**：级联式（ASR+LLM+TTS）可控、易审计、可独立优化，但每层都有延迟；原生 Speech-to-Speech（OpenAI Realtime/Gemini Live/Qwen-Omni）延迟低、语气保留好，但更黑盒、成本模型变化快。

7. **interview-guide 完整工程实现**：前端（AudioRecorder+AudioWorklet+@ricky0123/vad-web）→后端（Spring Boot WebSocket 会话管理、QwenAsrService、DashscopeLlmService、QwenTtsService），含完整的 Java/TypeScript 代码示例。

## Key Insights

- "文本 Agent 接上麦克风和扬声器，只能得到一个能说话的 Demo"
- "云端模型决定上限，端侧工程决定下限"
- "AI 语音 Agent 要围绕实时音频流设计成一套可取消、可观测、可降级的对话系统"
- "模型负责理解和生成，工程负责让它在噪声、弱网、打断、取消和成本约束下还能稳定工作"

## Related Pages

- [[wiki/concepts/agent-skills-system]] — Agent Skills
- [[wiki/concepts/react-reasoning-acting]] — ReAct 模式
- [[wiki/concepts/prompt-engineering]] — Prompt Engineering
- [[wiki/sources/llm-operation-mechanism-javaguide]] — LLM 运行机制
