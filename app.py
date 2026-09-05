from strands import Agent
from tools.civic import create_civic_complaint

SYSTEM_PROMPT = """
You are Jan-SahayakAI, an AI-powered Good Neighbour Agent.

Help residents identify and resolve civic problems.

When the user wants to prepare a civic complaint,
collect the issue, location, and description.

Use the civic complaint tool when you have the
required information.

Never invent information.
"""

agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    model="anthropic.claude-sonnet-4-6",
    tools=[create_civic_complaint]
)

print("Jan-SahayakAI is ready!")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    response = agent(user_input)

    print("\nJan-SahayakAI:", response)