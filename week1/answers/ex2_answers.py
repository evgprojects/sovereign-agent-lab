"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "check_pub_availability", "calculate_catering_cost",
                       "get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = ""

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True   # True or False

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "placeholder"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://placehold.co/1200x628/1a1a2e/eaeaea?text=The+Haymarket+Vaults+%7C+160+guests&id=2ef939fbbaf6"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
Because the agent was made resilient to failures. If image generation endpoint throws an error, the error is caught by 
the agent, and it returns the placeholder.  
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
<think>
  Okay, let's see. The user wanted to check The Bow Bar first for 160 vegan guests. The first tool response showed that
 The Bow Bar's capacity is only 80, which is too small. So, they don't meet the requirements. Then, the assistant 
 checked The Albanach next. The response for The Albanach says it has a capacity of 180, which is more than the 
 required 160, and they do have vegan options. The status is available and meets_all_constraints is true. 
 That means The Albanach is a suitable venue.

Now, the user's original request was to check The Bow Bar first, and if not possible, check any other available venue.
 Since The Albanach meets all the requirements, the assistant should inform the user that The Albanach is available and
  provide the details. The user might need to know the address and other info to proceed. Also, maybe check if they 
  need further assistance like calculating catering costs or generating a flyer once the venue is confirmed. But the 
  immediate answer is to present The Albanach as the available option.
</think>

The Albanach is available and meets all your requirements:
- **Capacity**: 180 (exceeds your 160-guest requirement)
- **Vegan options**: Available
- **Address**: 2 Hunter Square, Edinburgh
- **Status**: Available

Would you like assistance with next steps like calculating catering costs or generating an event flyer for this venue?
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
<think>
Okay, let's see. The user is looking for a venue in Edinburgh that can accommodate 300 people with vegan options. They
 provided a list of known venues: The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar. I checked
  each one using the check_pub_availability function.

First, The Albanach had a capacity of 180, which is under 300, so that's out. Then The Haymarket Vaults with 160, also
 too small. The Guilford Arms had 200 capacity but didn't offer vegan options. Finally, The Bow Bar, which has a 
 capacity of 80 and is vegan-friendly, but it's already full. None of the venues meet both the capacity and availability
  requirements. The user might need to look for other options outside the provided list or adjust their requirements.
</think>

None of the known Edinburgh venues can accommodate 300 guests with vegan options. The closest options have:
- The Albanach (180 capacity, vegan available)
- The Haymarket Vaults (160 capacity, vegan available)
- The Guilford Arms (200 capacity, no vegan)
- The Bow Bar (80 capacity, vegan available but full)

Would you like to:
1. Adjust guest count or dietary requirements?
2. Search for alternative venues outside this list?
3. Get help with a smaller-scale event?
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = """
I don't have access to real-time train schedules or transportation data. For the most accurate information about the 
last train from Edinburgh Waverley to London, I recommend checking:
1. The National Rail website (www.nationalrail.co.uk)
2. The ScotRail app or website
3. Real-time departure boards at the station

Would you like help with anything related to Edinburgh pubs, weather, event planning, or catering estimates instead?"
"""

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
I think this behaviour would be acceptable in a real booking system. Instead of hallucinating the answer, the agent 
responded that it does not have access to real-time train schedules and suggested some sources to check. It gracefully
handled out-of-scope scenario.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
The LangGraph agent also admitted that it dit not have the right tools to handle out-of-scope scenario, but it 
suggested some sources that the user could check to find the answer to their question. In this way, it was more helpful
than Rasa agent, but if it hallucinated it would be worse.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
I was surprised by the agent reasoning that justified the choice of The Albanach instead of The Haymarket Vaults. Both
answers would satisfy the given constraints. However, the agent did not pick one randomly, but used the following logic:
'They checked both The Albanach and The Haymarket Vaults, and both are available. The Albanach has a capacity of 180, 
which is more than enough, and The Haymarket Vaults have exactly 160. Since both meet the requirements, the user might
 prefer the one with extra space, so The Albanach is probably the better choice.'
 Such behaviour might or might not be desirable. One one hand, the agent might fill gaps in the specification. On another
 hand it might make a wrong choice. Asking the user to confirm if they want extra spaces would be desirable in this
 context.  
"""