---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0010-scientific-knowledge-systems-and-agents
type: theme
title: Scientific Knowledge Systems And Agents
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs: []
related:
- question:0007-source-reliability-agent-curation
- theme:0004-observation-and-measurement-bias
- theme:0008-causal-discovery-and-structure-learning
- theme:0011-source-reliability-and-truth-discovery
source_refs:
- paper:Zeng2026
- report:0015-llm-assisted-causal-and-scientific-reasoning-synthesis
- report:0017-source-reliability-truth-discovery-and-knowledge-systems-synthesis
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Scientific knowledge systems and agents covers methods for representing, retrieving, evaluating, and acting on scientific knowledge.
It includes knowledge graph evolution, scientific-agent tool use, benchmarked scientific context understanding, LLM-assisted hypothesis generation, and systems that connect unstructured literature to structured reasoning.

## Why It Matters

The cancer federation is a knowledge system as much as a document collection.
This theme helps meta decide which agentic or knowledge-graph methods could improve routing, synthesis, source tracing, and cross-project consistency.

## Boundaries

This theme is not a general AI theme.
Use it only when a method affects scientific knowledge representation, context understanding, tool orchestration, hypothesis generation, or graph maintenance.
LLM papers focused mainly on causal discovery belong primarily under `theme:0008-causal-discovery-and-structure-learning`.

## Guardrails

- Do not treat LLM-generated hypotheses as evidence.
- Do not let retrieval or agent convenience erase source provenance.
- Do not use knowledge graph structure as a substitute for evidence strength.
- Do not adopt an agent workflow without an evaluation target and failure-mode check.
