import asyncio
from dotenv import load_dotenv, find_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console

load_dotenv(find_dotenv())

client = OpenAIChatCompletionClient(model="gpt-3.5-turbo")
agent = AssistantAgent("assistant", client)

asyncio.run(Console(agent.run_stream(task="Oi, tudo bem?")))