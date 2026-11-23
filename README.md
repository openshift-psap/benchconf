# BenchConf

Standard benchmark configurations used by Red Hat's Performance and Scale for AI Platforms Team

## Requirements

These configs are supported starting with [GuideLLM v0.7.0](https://github.com/vllm-project/guidellm/releases/tag/v0.7.0).

## Suites

### `psap-inference` — canonical inference suite

The single source of truth for PSAP inference workload shapes. Config names follow
`concurrent-<prompt>-<output>-<shape>` where `<shape>` is:

- `equal` — fixed prompt/output token counts
- `norm` — normally-distributed token counts (with min/max clamps)
- `multiturn` — multi-turn conversations with prefix caching

`smoke` is the minimal endpoint-verification workload.

All profiles share the same run semantics: increasing stream order, 275s max
duration per rate, rampup 35s, warmup 75s. smoke runs 10 requests at concurrency 1.
`smoke` runs 10 requests at concurrency 1.

### Deprecated suites

`llm-d` and `rhaiis-regression` are superseded by `psap-inference` and will be
removed once consumers migrate. The content was already aligned so the mapping is a
pure rename:

| psap-inference | old llm-d | old rhaiis-regression |
|---|---|---|
| smoke | smoke | — |
| concurrent-1k-1k-equal | concurrent-1k-1k | concurrent-1k-1k-equal |
| concurrent-2ki-128-equal | — | concurrent-2ki-128-equal |
| concurrent-512-2ki-norm | — | concurrent-512-2ki-norm |
| concurrent-8k-1k-equal | concurrent-8k-1k | concurrent-8k-1k-equal |
| concurrent-8k-800-norm | concurrent-heavy-heterogeneous | concurrent-8k-800-norm |
| concurrent-100k-1k-equal | heavy-load | concurrent-100k-1k-equal |
| concurrent-128-128-multiturn | multi-turn | concurrent-128-128-multiturn |
