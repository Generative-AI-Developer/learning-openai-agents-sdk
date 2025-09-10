from agents import Agent, Runner, ModelSettings, handoff
from dotenv import load_dotenv
load_dotenv()
import asyncio



refund_agent = Agent(
    name="Refund agent",
    instructions="You are a helpful assistant",
    model="gpt-5-nano",
    model_settings=ModelSettings(max_tokens=400)  # Limit response length
 
)

general_agent = Agent(
    name="General agent",
    instructions=(
        "You are a helpful assistant. If the user's request is about a refund, "
        " handoff to the Refund agent."
        "Otherwise, respond generally."
    ),

    handoffs=[handoff(agent=refund_agent,
             tool_description_override="handle a refund request",
             is_enabled=False        
)],
    model="gpt-5-nano",
    model_settings=ModelSettings(max_tokens=400)  # Limit response length
)

async def main():
    result = await Runner.run(general_agent, "hi")
    print(result.final_output)
    print("last agent:", result.last_agent.name)

if __name__ == "__main__":
    asyncio.run(main())
