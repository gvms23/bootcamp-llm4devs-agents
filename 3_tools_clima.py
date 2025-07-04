import os
import httpx
import asyncio
from dotenv import load_dotenv, find_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console

load_dotenv(find_dotenv())

client = OpenAIChatCompletionClient(model="gpt-3.5-turbo", temperature=0.7)

def temperatura_online(city: str) -> str:
    """
    Retorna a temperatura atual de uma cidade usando a API pública wttr.in.
    """
    try:
        url = f"https://wttr.in/{city}"
        params = {"format": "j1"}

        with httpx.Client() as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            temp = data["current_condition"][0]["temp_C"]

            return f"A temperatura atual em {city} é {temp}°C."
    except Exception as e:
        return f"Erro ao obter a temperatura de {city}: {e}"


def get_umidade(city: str) -> str:
    """
    Retorna a umidade relativa atual de uma cidade usando a API pública wttr.in.
    """
    try:
        url = f"https://wttr.in/{city}"
        params = {"format": "j1"}

        with httpx.Client() as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            umidade = data["current_condition"][0]["humidity"]

            return f"A umidade atual em {city} é {umidade}%."
    except Exception as e:
        return f"Erro ao obter a umidade de {city}: {e}"

def get_conselho_climatico(city: str) -> str:
    """
    Retorna um conselho simples baseado nas condições climáticas atuais da cidade.
    """
    try:
        url = f"https://wttr.in/{city}"
        params = {"format": "j1"}

        with httpx.Client() as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            weather_desc = data["current_condition"][0]["weatherDesc"][0]["value"]
            temp = int(data["current_condition"][0]["temp_C"])
            umidade = int(data["current_condition"][0]["humidity"])

            conselho = []

            if "rain" in weather_desc.lower() or "chuva" in weather_desc.lower():
                conselho.append("Leve um guarda-chuva ☔.")
            if temp >= 30:
                conselho.append("Está bem quente, não esqueça de se hidratar 💧.")
            elif temp <= 10:
                conselho.append("Está frio, vista-se bem 🧥.")
            if umidade >= 80:
                conselho.append("O clima está bem úmido, cuidado com mofo e desconforto.")
            elif umidade <= 30:
                conselho.append("O ar está seco, use hidratante e beba bastante água.")

            if not conselho:
                conselho.append("O clima está agradável, aproveite seu dia!")

            return " ".join(conselho)
    except Exception as e:
        return f"Erro ao obter o conselho climático de {city}: {e}"


agent = AssistantAgent(
    "assistant", 
    client, 
    tools=[temperatura_online, get_umidade, get_conselho_climatico],
    system_message="""
                    Você é um assistente de clima.
                    Você deve responder as perguntas sobre o clima de forma clara e objetiva. 
                    Use o mínimo de palavras possível. 
                    Se você não encontrar nenhuma tool disponível, apenas diga 'Não sei'.
                    """
    )

asyncio.run(
    Console(
        agent.run_stream(
            task="Quero fazer uma viagem para Guarujá me passe as informações e conselhos climáticos para esses dias."
        )
    )
)


