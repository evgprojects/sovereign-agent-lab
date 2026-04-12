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
FILL ME IN
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 0   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
An agent does not need to know about the tools it has an access to upfront. MCP provides dynamically discoverable tools.
When an agent connects to an MCP server it discovers all available tools. If a new tool added to MCP server, no changes
are required for the agent.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

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
Open ended task vs task with clear criteria
"""
