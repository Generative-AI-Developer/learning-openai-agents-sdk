from agents import Agent, Runner,function_tool, ModelSettings
from dotenv import load_dotenv
from agents.agent import StopAtTools
load_dotenv()



@function_tool
def get_weather(city: str) -> str:
      return f"The weather in {city} is sunny"

@function_tool
def get_support_details(city: str) -> str:
      return f"The support details for {city} are 123-456-7890"



agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model="gpt-5-nano",
    tools=[get_support_details, get_weather],
    model_settings=ModelSettings(max_tokens=400),  # Limit response length    
    # tool_use_behavior="stop_on_first_tool",
    # tool_use_behavior=StopAtTools(stop_at_tool_names=["get_weather"])
    model_settings=ModelSettings(tool_choice="none"),# ??
    reset_tool_choice=False# ??


)


result = Runner.run_sync(agent, "What is the weather in Karachi? also share support details for same city?", max_turns=2)
print(result.final_output)
