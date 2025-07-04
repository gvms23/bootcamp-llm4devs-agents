import os
import httpx
from dotenv import load_dotenv, find_dotenv
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

load_dotenv(find_dotenv())
client = OpenAIChatCompletionClient(model="gpt-3.5-turbo")

agente_escritor = AssistantAgent(
                    "escritor", 
                    client,
                    system_message=
                        "Você é um assistente de conteúdos sobre Pindamonhangaba - SP."
                        "escreva 50 palavras sobre o conteúdo fornecido."
                )        
agente_critico = AssistantAgent(
                    "critico", 
                    client, 
                    system_message=
                        "Você é um crítico de conteúdos. "
                        "Sugira críticas sobre o conteúdo fornecido."
                        "Quando achar que o conteúdo está bom, escreva: 'ACEITO'."
                )

text_termination = TextMentionTermination("ACEITO")

team = RoundRobinGroupChat(
            [agente_escritor, agente_critico], 
            termination_condition=text_termination) 
            #max_turns=3

asyncio.run(
    Console(
        team.run_stream(task="Escreva sobre pontos turísticos de Pindamonhangaba")
    )
)
