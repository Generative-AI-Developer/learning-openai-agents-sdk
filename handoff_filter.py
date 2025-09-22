from agents import Agent, Runner, ModelSettings, handoff, function_tool
from dotenv import load_dotenv
load_dotenv()
import asyncio
from agents.extensions import handoff_filters

@function_tool
def weather_in_city(city: str) -> str:
    return f"The weather in {city} is sunny."

refund_agent = Agent(
    name="Refund agent",
    instructions="You are a helpful assistant",

    model="gpt-4o-mini",
    model_settings=ModelSettings(max_tokens=100)  # Limit response length
 
)

general_agent = Agent(
    name="General agent",
    instructions=(
         "You are a helpful assistant. If the user's request is about a refund, "
         " handoff to the Refund agent."
         "Otherwise, respond generally." 
        ),
    # tools=[weather_in_city],    
    handoffs=[handoff(agent=refund_agent,
         tool_name_override="refund_order",         
         tool_description_override="handle a refund request",
        #  is_enabled=True,
         input_filter=handoff_filters.remove_all_tools
         )],
 
                               
    model="gpt-4o-mini",
    model_settings=ModelSettings(max_tokens=100)  # Limit response length
)

async def main():
    result = await Runner.run(general_agent, "What is the weather is Karachi also refund my orders - details are order id: 1234 reson: wrong item delivered")
    print(result.final_output)
    print("last agent:", result.last_agent.name)

if __name__ == "__main__":
    asyncio.run(main())
