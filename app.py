from agents.jan_sahayak import create_agent

# Initialize the agent
agent = create_agent()

print("========================================")
print("       JAN-SAHAYAKAI")
print("   Your Good Neighbour AI Agent")
print("========================================")
print("Type 'exit' to stop.\n")
print("Jan-SahayakAI is ready!")

while True:
    try:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
            
        if not user_input.strip():
            continue
            
        response = agent(user_input)
        print(f"\nJan-SahayakAI: {response}")
        
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break
    except Exception as e:
        print(f"\nError: {e}")