# Agentic Traces Resources

This document contains links to repositories and datasets related to AI agent execution traces, benchmarking, and analysis.

## Datasets

### 1. Exgentic Agent LLM Traces v2
**Link:** https://huggingface.co/datasets/Exgentic/agent-llm-traces-v2

**Description:** Contains **OpenTelemetry execution traces from 10,057 AI agent runs** across 6 benchmarks (AppWorld, SWE-bench, BrowseCompPlus, τ²-bench variants). This dataset provides 241,674 chat spans with standardized attributes (messages, tokens, model parameters, tool definitions) covering 5 models (DeepSeek-V3.2, Kimi-K2.5, Claude Opus 4.5, Gemini 3 Pro Preview, GPT-5.2) and 4 harness types. It enables replay testing and behavioral analysis of agent systems by providing clean records of what benchmarked models actually did during task execution. Tasks span personal assistance, research, software engineering, and customer service scenarios.

---

### 2. SemiAnalysis Claude Code Traces (No Subagents)
**Link:** https://huggingface.co/datasets/semianalysisai/cc-traces-weka-no-subagents-051226

**Description:** Contains **949 real production traces from Claude Code CLI sessions**, capturing multi-turn agentic conversations for inference benchmarking and KV-cache research. Includes ~136,000 individual model requests with complete request/response sequences and KV block hashes (64-token blocks). Features mean 143 requests per trace (max 13,685), input sequence lengths averaging ~178K tokens with p99 at ~720K, and ~75% mean prefix-cache hit rate. Primarily uses `claude-opus-4-7`. Ideal for benchmarking inference engines with realistic agentic workloads and KV-cache research without requiring re-tokenization.

---

### 3. Inferact Codex SWE-bench Pro Traces
**Link:** https://huggingface.co/datasets/Inferact/codex_swebenchpro_traces

**Description:** Execution traces from running an AI coding agent (Codex) on **SWE-bench Pro benchmark tasks**. Contains 610 successful agentic workflow runs across 11 open-source repositories with 20,230 total LLM calls (averaging 33 calls per trial). Documents real agentic coding workloads with detailed metrics on LLM API calls, token usage, caching behavior, and timing data. Features 94.2% cache hit rate, 131:1 input-to-output token ratio, and 53.9% task pass rate. Useful for understanding how AI coding agents interact with LLMs in real software engineering tasks and optimizing caching strategies.

---

## Repositories & Tools

### 4. AIPerf - Agentic Benchmarking Tool
**Link:** https://github.com/SemiAnalysisAI/aiperf/tree/cjq/agentx-v0.4

**Description:** A comprehensive benchmarking tool designed to **measure the performance of generative AI models** served by various inference solutions. Provides detailed performance metrics with support for multiple API types (OpenAI, HuggingFace, NVIDIA NIM, Cohere) and various workload patterns. Features scalable multiprocess architecture, real-time dashboard UI, diverse benchmarking modes (concurrency testing, request-rate control, trace replay), and extensive metrics covering latency, throughput, token timing, and GPU telemetry. Supports benchmarking text generation, embeddings, rankings, audio, vision, and image/video generation models. Includes multi-turn conversation testing, prefix synthesis for KV cache studies, and DAG-based sub-agent workflows.

---

### 5. Agentic Coding Analysis
**Link:** https://github.com/callanjfox/agentic-coding-analysis

**Description:** Tools for **analyzing Claude's prompt caching behavior** and generating compact trace files for KV cache replay testing. Helps understand how Claude Code's KV cache behaves in production conversations by tracking cache hit rates, TTL effects, and working set patterns. Processes SQLite databases from claude-code-proxy plus JSONL conversation files to generate compact JSON trace files that achieve 95-97% accuracy simulating cache behavior against actual API metrics. Produces interactive visualizations showing cache metrics, TTL impact, and working set evolution. Includes support for both parent conversations and sub-agent spawning, with traces feeding into kv-cache-tester for infrastructure replay testing.

---

## Summary

These resources provide comprehensive data and tools for:
- **Analyzing agentic AI behavior** across multiple benchmarks and real-world scenarios
- **Benchmarking inference performance** with realistic multi-turn conversations
- **Understanding KV-cache patterns** in production agentic workloads
- **Optimizing infrastructure** for long-context AI applications
- **Researching prompt caching** efficiency and strategies
