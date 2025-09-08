from agents import Agent, Runner,function_tool, ModelSettings, RunContextWrapper
from dotenv import load_dotenv
from agents.agent import StopAtTools
load_dotenv()

function_tool
def get_system_prompt(ctx: RunContextWrapper , start_agent: Agent):
      print("\n[context]", ctx.context)
      print("\n[agent]", start_agent)
      return "You are a helpful assistant that can answar questions and help tasks."



agent = Agent(
    name="Haiku Agent",
    instructions=get_system_prompt,
    model="gpt-5-nano",
    model_settings=ModelSettings(max_tokens=200),  # Limit response length
#     

)
result = Runner.run_sync(agent, "hi", context={"user_name": "Asif"})# we can pass any context here eg any object
print(result.final_output)
