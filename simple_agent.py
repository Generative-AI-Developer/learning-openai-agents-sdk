from agents import Agent, Runner
from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-5-nano"
    
)

result = Runner.run_sync(agent, "what is capital of Pakistan?")
print(result.final_output)
