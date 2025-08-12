import os
import asyncio
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv(find_dotenv())
my_key = os.environ.get("my_key")

set_tracing_disabled(disabled=True)

external_client = AsyncOpenAI(
    api_key=my_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

recipe_agent = Agent(
    name="AI RecipeBot",
    instructions=(
        "You are a helpful recipe assistant. "
        "When the user tells you what ingredients they have, suggest simple and tasty recipes they can cook. "
        "List intrustions step by step in simple words, use emojies as well"
    ),
    model=llm_model
)

st.title("Recipe Bot")

question = st.text_input("What ingredients do you have?")

if question:
    runner = Runner()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(runner.run(recipe_agent, question))
    st.write(result.final_output)
