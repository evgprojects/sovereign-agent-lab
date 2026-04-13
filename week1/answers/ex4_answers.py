"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "FILL_ME_IN"
QUERY_1_VENUE_ADDRESS = "FILL_ME_IN"
QUERY_2_FINAL_ANSWER  = "FILL_ME_IN"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Only mcp_venue_server.py code needed to be updated. The agent code didn't need updating at all.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 2   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
An agent does not need to know about the tools it has an access to upfront. MCP provides dynamically discoverable tools.
When an agent connects to an MCP server it discovers all available tools. If a new tool added to MCP server, no changes
are required for the agent.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- Real tools. Instead of using hardcoded data, the agent is integrated with real tools that can search the web, 
send emails and communicate via messangers.
- Planning. The agent has an access to two models: a thinking model for complex planning and a fast model for execution.
- Memory. The agent should have memory, so it does not need to rediscover facts. That will lower the costs, reduce 
latency and allow agent self-improvement.
- Guardrails. To validate agent's input to prevent attacks on the agent, and to validate agent output to prevent harmful
content to be exposed to the user or other human. 
- Observability / traceability. All agent input, output and tool calls should be auditable to allow troubleshooting if
 anything goes wrong. 
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The autonomous LangGraph agent is best for research open-ended tasks where the execution path is not predetermined, 
like finding an appropriate venue based on some constraints. The Rasa agent is best for tasks with deterministic rules.
Swapping the two would not work well: the Rasa agent is too constraint and not autonomous enough to do research, and the
 autonomous agent can go astray, when all it needs is a predefined flow.
"""