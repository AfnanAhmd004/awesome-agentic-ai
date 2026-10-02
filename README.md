# Awesome Agentic AI: robotics, industry and quant edition

A **curated, opinionated** map of agentic AI for people who have to make it work on real machines and real money: robot fleets, factories, aerospace systems and trading desks.

Most "awesome" lists are long. This one is short on purpose:
- Every entry says **why it matters**.
- Every link is **checked in CI**.
- The **use-case playbook** at the end pairs each application with the failure mode that will hurt you and the control that prevents it.

**Contents:**
- [Start here](#start-here)
- [Foundational papers](#foundational-papers)
- [Frameworks and runtimes](#frameworks-and-runtimes)
- [Protocols](#protocols)
- [Evaluation and observability](#evaluation-and-observability)
- [Embodied agents and robotics](#embodied-agents-and-robotics)
- [Agents for finance and quant](#agents-for-finance-and-quant)
- [Safety and governance](#safety-and-governance)
- [Use-case playbook](#use-case-playbook)
- [Build it yourself](#build-it-yourself)
- [Contributing](#contributing)

---

## Start here

If you read five things, read these.

- [ReAct](https://arxiv.org/abs/2210.03629) - Interleaving reasoning with tool calls; the loop inside almost every agent today.
- [SayCan](https://arxiv.org/abs/2204.01691) - Grounding language-model plans in what a robot can actually do (affordances); the template for LLMs in robotics.
- [Indirect prompt injection](https://arxiv.org/abs/2302.12173) - Why any agent that reads documents, web pages or logs can be hijacked by them.
- [SWE-bench](https://arxiv.org/abs/2310.06770) - What a realistic, verifiable agent benchmark looks like.
- [TradingAgents](https://arxiv.org/abs/2412.20138) - A multi-agent trading-firm design (analysts, bull/bear debate, trader, risk team) that is easy to study and critique.

## Foundational papers

**Reasoning and acting**
- [ReAct](https://arxiv.org/abs/2210.03629) - Thought → action → observation loops with tools.
- [Self-Consistency](https://arxiv.org/abs/2203.11171) - Sample several reasoning paths and vote; the simplest ensemble that works.
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601) - Search over intermediate reasoning steps instead of a single chain.
- [Reflexion](https://arxiv.org/abs/2303.11366) - Agents that improve from verbal feedback on their own failures.

**Tool use**
- [Toolformer](https://arxiv.org/abs/2302.04761) - Models that learn when and how to call APIs.
- [Gorilla](https://arxiv.org/abs/2305.15334) - Fine-tuning for accurate API calls at scale, with retrieval over documentation.
- [HuggingGPT](https://arxiv.org/abs/2303.17580) - An LLM as a controller that dispatches sub-tasks to specialist models.
- [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) - The original RAG paper; grounding generation in retrieved documents.

**Multi-agent systems**
- [Generative Agents](https://arxiv.org/abs/2304.03442) - Memory, reflection and planning for believable simulated agents.
- [CAMEL](https://arxiv.org/abs/2303.17760) - Role-playing agent pairs that cooperate on tasks.
- [AutoGen](https://arxiv.org/abs/2308.08155) - Multi-agent conversation as a programming model.
- [MetaGPT](https://arxiv.org/abs/2308.00352) - Encoding standard operating procedures into a team of role agents.
- [ChatDev](https://arxiv.org/abs/2307.07924) - A simulated software company of communicating agents.
- [Multiagent Debate](https://arxiv.org/abs/2305.14325) - Agents critiquing each other to improve factuality and reasoning.
- [Agentless](https://arxiv.org/abs/2407.01489) - A strong reminder that a simple fixed pipeline can beat a complex agent.

**Programming language models**
- [DSPy](https://arxiv.org/abs/2310.03714) - Declarative LM pipelines whose prompts and few-shot examples are optimised automatically.

## Frameworks and runtimes

**Code-first orchestration**
- [LangGraph](https://github.com/langchain-ai/langgraph) - Stateful agent graphs with persistence, streaming and human-in-the-loop.
- [LangChain](https://github.com/langchain-ai/langchain) - Broad integration layer for models, tools and retrievers.
- [AutoGen](https://github.com/microsoft/autogen) - Microsoft's multi-agent framework.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Role-based agent crews with task delegation.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Enterprise SDK for adding LLM agents to C#, Python and Java applications.
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for retrieval and agents over your own documents.
- [Haystack](https://github.com/deepset-ai/haystack) - Production pipelines for RAG and agents.
- [smolagents](https://github.com/huggingface/smolagents) - Minimal library where agents act by writing code.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Type-safe agents with validated, structured outputs.
- [DSPy](https://github.com/stanfordnlp/dspy) - Implementation of the DSPy paper.
- [Agno](https://github.com/agno-agi/agno) - Framework for multi-agent systems with memory and knowledge.
- [CAMEL](https://github.com/camel-ai/camel) - Framework for studying and building multi-agent societies.
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - Implementation of the MetaGPT multi-agent framework.
- [ChatDev](https://github.com/OpenBMB/ChatDev) - Implementation of ChatDev.

**Vendor agent SDKs**
- [Claude Agent SDK (Python)](https://github.com/anthropics/claude-agent-sdk-python) - Anthropic's SDK for building agents on the same harness as Claude Code.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Lightweight multi-agent workflows with handoffs and guardrails.
- [Agent Development Kit](https://github.com/google/adk-python) - Google's code-first toolkit for building and deploying agents.

**Visual and low-code builders**
- [n8n](https://github.com/n8n-io/n8n) - Workflow automation with AI and agent nodes; self-hostable.
- [Langflow](https://github.com/langflow-ai/langflow) - Visual builder for agent and RAG flows.
- [Flowise](https://github.com/FlowiseAI/Flowise) - Drag-and-drop builder for LLM apps and agents.
- [Dify](https://github.com/langgenius/dify) - LLM app platform with workflows, RAG and agent capabilities.

**Agents that use computers and code**
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Open platform for software-engineering agents.
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - Agent-computer interface design for fixing real GitHub issues.
- [browser-use](https://github.com/browser-use/browser-use) - Let agents operate websites.

## Protocols

- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) - Open standard for connecting models to tools and data; specification and docs.
- [MCP reference servers](https://github.com/modelcontextprotocol/servers) - Reference implementations to learn the protocol from.
- [Agent2Agent (A2A)](https://github.com/a2aproject/A2A) - Open protocol for agents built on different frameworks to communicate.

## Evaluation and observability

**Benchmarks**
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Resolve real GitHub issues; graded by the repository's own tests.
- [GAIA](https://arxiv.org/abs/2311.12983) - General-assistant questions that are easy for people and hard for agents.
- [AgentBench](https://github.com/THUDM/AgentBench) - LLMs as agents across operating-system, database, web and game environments.
- [WebArena](https://github.com/web-arena-x/webarena) - Realistic, self-hosted websites for web agents.
- [OSWorld](https://github.com/xlang-ai/OSWorld) - Multimodal agents operating real desktop applications.
- [τ-bench](https://github.com/sierra-research/tau-bench) - Tool-agent-user interaction with policies; introduced pass^k for reliability.

**Evaluation tooling**
- [Inspect](https://github.com/UKGovernmentBEIS/inspect_ai) - The UK AI Security Institute's framework for LLM and agent evaluations.
- [promptfoo](https://github.com/promptfoo/promptfoo) - Test prompts and agents in CI, including red-teaming.
- [DeepEval](https://github.com/confident-ai/deepeval) - Unit-test-style metrics for LLM applications.
- [Ragas](https://github.com/explodinggradients/ragas) - Metrics for retrieval-augmented generation.
- [LLM-as-a-judge](https://arxiv.org/abs/2306.05685) - The MT-Bench / Chatbot Arena paper; documents position and verbosity bias in model judges.

**Tracing and observability**
- [Langfuse](https://github.com/langfuse/langfuse) - Open-source tracing, evals and prompt management.
- [Phoenix](https://github.com/Arize-ai/phoenix) - Open-source LLM tracing and evaluation from Arize.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry instrumentation for LLM applications.

## Embodied agents and robotics

**Language models as planners and programmers**
- [SayCan](https://arxiv.org/abs/2204.01691) - Combine what the LLM says is useful with what the robot can do.
- [Inner Monologue](https://arxiv.org/abs/2207.05608) - Closed-loop planning with feedback from the environment.
- [Code as Policies](https://arxiv.org/abs/2209.07753) - LLMs write robot policy code that calls perception and control APIs.
- [ProgPrompt](https://arxiv.org/abs/2209.11302) - Program-like prompts for situated task plans.
- [VoxPoser](https://arxiv.org/abs/2307.05973) - LLMs compose 3D value maps that a motion planner follows.
- [Eureka](https://arxiv.org/abs/2310.12931) - LLMs write reward functions for reinforcement learning ([code](https://github.com/eureka-research/Eureka)).
- [Voyager](https://arxiv.org/abs/2305.16291) - Lifelong learning agent with a growing skill library ([code](https://github.com/MineDojo/Voyager)).

**Vision-language-action models**
- [RT-2](https://arxiv.org/abs/2307.15818) - Web-scale vision-language knowledge transferred to robot actions.
- [OpenVLA](https://github.com/openvla/openvla) - Open-source 7B vision-language-action model ([paper](https://arxiv.org/abs/2406.09246)).
- [Octo](https://github.com/octo-models/octo) - Generalist robot policy trained on Open X-Embodiment ([paper](https://arxiv.org/abs/2405.12213)).
- [openpi](https://github.com/Physical-Intelligence/openpi) - Open weights and code for the π0 family of models ([paper](https://arxiv.org/abs/2410.24164)).
- [Isaac GR00T](https://github.com/NVIDIA/Isaac-GR00T) - NVIDIA's open foundation model for humanoid robots.

**Robot learning stacks and simulators**
- [LeRobot](https://github.com/huggingface/lerobot) - Datasets, policies and tools for real-world robot learning.
- [MuJoCo](https://github.com/google-deepmind/mujoco) - Fast, accurate physics for robotics research.
- [Isaac Lab](https://github.com/isaac-sim/IsaacLab) - GPU-parallel robot learning on Isaac Sim.
- [Genesis](https://github.com/Genesis-Embodied-AI/Genesis) - Fast physics and simulation platform for robotics and embodied AI.
- [Nav2](https://github.com/ros-planning/navigation2) - The ROS 2 navigation stack: what your agent's "go to" tool should ultimately call.

## Agents for finance and quant

- [TradingAgents](https://github.com/TauricResearch/TradingAgents) - Multi-agent LLM trading framework ([paper](https://arxiv.org/abs/2412.20138)).
- [FinRL](https://github.com/AI4Finance-Foundation/FinRL) - Deep reinforcement learning for trading ([paper](https://arxiv.org/abs/2011.09607)).
- [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) - Open-source financial LLMs ([paper](https://arxiv.org/abs/2306.06031)).
- [Qlib](https://github.com/microsoft/qlib) - Microsoft's AI-oriented quantitative investment platform.
- [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund) - Educational multi-agent proof of concept with investor-persona agents.

> **Read before trusting any LLM trading backtest.** Language models may have seen the "future" of historical periods in their training data, so backtests over those periods are optimistic. Count every variant you tried and deflate the Sharpe ratio accordingly. Fill and cost assumptions usually matter more than the model.

## Safety and governance

- [Indirect prompt injection](https://arxiv.org/abs/2302.12173) - Attacks that arrive through retrieved content, not the user.
- [OWASP Top 10 for LLM applications](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) - The standard checklist: prompt injection, excessive agency, insecure output handling and more.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - The AI RMF and its generative-AI profile (NIST AI 600-1).
- [Constitutional AI](https://arxiv.org/abs/2212.08073) - Training harmlessness from a written set of principles and AI feedback.

## Use-case playbook

Original guidance: where agents pay off in robotics, industry, aerospace and finance, what will go wrong, and the control that prevents it.

| Use case | Agent pattern | What goes wrong | Control that works |
|---|---|---|---|
| Robot-fleet maintenance triage | Tool agent: telemetry, manual retrieval, work orders | One site-wide cause (heat, network, a bad update) becomes dozens of tickets | Fleet-level correlation before per-robot diagnosis; write rate limits |
| Operator assistant on a robot cell | RAG + read-only tools | Asked to bypass an interlock "just this shift" | Safety functions never depend on the LLM; refusal tests with pass^k on critical cases |
| Natural-language task planning for robots | LLM planner → skill library (SayCan / Code as Policies) | Plans that are fluent but infeasible | Affordance or feasibility scoring, simulation before execution, a human gate on new plans |
| Machine-vision inspection | Classical checks + model, agent only for exception handling | Model drift silently raises escapes | Independent checks per defect type, traceability logs, a line-stop interlock outside the agent |
| Space / aerospace operations (e.g. space situational awareness) | Agents for tasking, triage and reporting over sensor pipelines | Overconfident summaries of uncertain detections | Report uncertainty explicitly; keep the human in command authority; replay-based evaluation |
| Engineering knowledge assistant | Deep-research agent with citations | Plausible numbers that the source never said | Claim-level verification against cited passages; abstain when coverage is low |
| Alpha research assistant | Analyst agents + quant tools | Lookahead, data snooping, LLM "memory" of history | Point-in-time data, purged walk-forward, deflated Sharpe, out-of-sample periods after the model's training cutoff |
| Trading execution | Agent proposes, deterministic system executes | Runaway orders, stale data | Pre-trade limits in code, kill switch owned by humans, fail-closed on bad data |
| Business automation (leads, reports, tickets) | Workflow engine with LLM steps | Malformed or hallucinated outputs flowing downstream | Validate every LLM output before use; rule-based fallback; grounding checks on numbers |

## Build it yourself

Small, tested reference implementations of the patterns above:

| Pattern | Repository |
|---|---|
| Stateful agent graph: checkpoints, human approval, crash recovery | [agent-graph](https://github.com/AfnanAhmd004/agent-graph) |
| Multi-agent coordination: voting, routing, debate, Byzantine agents | [agent-swarm](https://github.com/AfnanAhmd004/agent-swarm) |
| Agent evaluation: pass^k and a CI release gate | [agent-evals](https://github.com/AfnanAhmd004/agent-evals) |
| Specialist agent library with a router and playbooks | [agent-roster](https://github.com/AfnanAhmd004/agent-roster) |
| Language-to-robot-plan with a symbolic checker and closed-loop replanning (SayCan-style) | [vlm-robot-planner](https://github.com/AfnanAhmd004/vlm-robot-planner) |
| Robot-fleet operations agent with a model-independent safety layer | [robot-ops-agent](https://github.com/AfnanAhmd004/robot-ops-agent) |
| Deep research with claim verification and abstention | [deep-research-agent](https://github.com/AfnanAhmd004/deep-research-agent) |
| n8n workflows with LLM guardrails, tested in a real n8n | [n8n-ai-workflows](https://github.com/AfnanAhmd004/n8n-ai-workflows) |
| Multi-agent trading research with debate and risk controls | [agentic-trading-lab](https://github.com/AfnanAhmd004/agentic-trading-lab) |

## Contributing

An entry earns its place if it is **primary** (the paper, or the official repository), **maintained or historically important**, and comes with a **one-line reason** a practitioner would care. Format: `- [Name](url) - Why it matters.` CI checks every link and the format (`python scripts/check_list.py`).

## License

MIT
