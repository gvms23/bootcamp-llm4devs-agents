import asyncio
from dotenv import load_dotenv, find_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console

load_dotenv(find_dotenv())

client = OpenAIChatCompletionClient(model="gpt-3.5-turbo")

def temperatura(cidade: str) -> str:
    """Retorna a temperatura atual da cidade."""
    return f"A temperatura atual em {cidade} é de 25 graus Celsius."

agent = AssistantAgent("assistant", client, tools=[temperatura])

asyncio.run(Console(agent.run_stream(task="Qual é a temperatura em Pindamonhangaba?")))


