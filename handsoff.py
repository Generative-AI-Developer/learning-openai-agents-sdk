from agents import Agent, Runner, ModelSettings, handoff
from dotenv import load_dotenv
load_dotenv()
import asyncio

billing_agent = Agent(
    name="Billing agent",
    instructions="You are a helpful assistant",
    model="gpt-5-nano"
    
)

refund_agent = Agent(
    name="Refund agent",
    instructions="You are a helpful assistant",
    model="gpt-5-nano"
    
)

triage_agent = Agent(
    name="Triage agent",
    instructions="You are a helpful assistant. Your job is to decide which agent is best suited to handle the user's request. "
                 "If the request is about billing, choose the Billing agent. If the request is about refunds, choose the Refund agent. "
                 "If the request is about something else, respond that you cannot help with that.",
    handoffs=[billing_agent, refund_agent],
    model="gpt-5-nano",
    model_settings=ModelSettings(max_tokens=300)  # Limit response length
)

async def main():
    result = await Runner.run(triage_agent, "Send my billing details.")
    print(result.final_output)
    print("last agent", result.last_agent.name)
if __name__ == "__main__":
    asyncio.run(main())    
    