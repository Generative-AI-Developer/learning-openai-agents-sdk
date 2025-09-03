from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool, ModelSettings
from dotenv import load_dotenv
load_dotenv()
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

# enable_verbose_stdout_logging()

@function_tool
def get_weather(location: str) -> str:
      return f"The weather in {location} is sunny"

@function_tool
def add_numbers(a: int, b: int) -> int:
      return a + b

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-5-nano",
    tools=[get_weather, add_numbers],
    model_settings=ModelSettings(max_tokens=300)  # Limit response length    
)

async def stream_agent():
    result = Runner.run_streamed(agent, "what is the weather in Karachi and add 5 and 10?")

    async for event in result.stream_events():
            print(f"\nFinal: {event.type}\n")
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                  print(f"[DATA]:{event.data}")
asyncio.run(stream_agent())                  
        


# result = Runner.run_sync(agent, "what is the capital of Pakistan?")
# print(result.final_output)    
