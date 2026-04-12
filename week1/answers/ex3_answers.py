"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  I'm calling to confirm a booking.                                                                                                                  
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                                                                         
And how many of those guests will need vegan meals?
Your input ->  50 vegan                                                                                                                                           
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  200 
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
Your input ->  /stop 
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  I'm calling to confirm a booking.
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  50 vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  330                                                                                                                                                
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £330 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
Your input ->  /stop 
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "A deposit of £330 exceeds the organiser's authorised limit of £300."   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  Hi. I'm calling to confirm if any of your guests require gluten free meals?                                                                        
I am afraid, I don't know the answer. At this point, I don't have access to a knowledge base.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
The agent admitted that it did not know the answer and asked if I wanted to continue with the task it knew how 
to handle.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
FILL ME IN
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I temporarily replaced now = datetime.datetime.now() with now = datetime.datetime(2026, 4, 12, 16, 50), so I did not
have to wait till after 4:45 pm. A better way would be to inject date and time, so it can be faked for testing without
changing the code, but I decided to keep ActionValidateBooking as it is.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
- The LLM handles language understanding. There is no more need to use regular expressions in python code to extract 
answers, it's now done by the LLM.
- The Python code is still needed to execute the business rules with the extracted values. For example, check the values
and escalate if some constraints are not satisfied.
- The old approach was completely deterministic, so if implemented correctly it is more trustworthy. However, if some edge
case was not covered by the regular expression, it would fail. The new approach uses a LLM, so it is probabilistic. It
can cover a wide range of possible user inputs, so it is much more flexible, however the rik is that it can hallucinate. 
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The CALM agent can not improvise a response it wasn't trained on and it can not call a tool that wasn't defined 
in flows.yml. It is a feature for the confirmation use case, as it is a structured task with a predefined logic.
"""
