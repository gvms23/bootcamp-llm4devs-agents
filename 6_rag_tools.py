import os
import asyncio
import httpx
from dotenv import load_dotenv, find_dotenv

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_core.memory import MemoryContent, MemoryMimeType
from autogen_ext.memory.chromadb import ChromaDBVectorMemory, PersistentChromaDBVectorMemoryConfig

# Carregar variáveis de ambiente
load_dotenv(find_dotenv())

# Função para buscar temperatura
def get_temperatura_atual(cidade: str, units: str = "celsius") -> str:
    try:
        url = f"https://wttr.in/{cidade}"
        params = {"format": "j1"}

        with httpx.Client() as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            current = data["current_condition"][0]
            if units.lower() == "celsius":
                temp = current["temp_C"]
                unit_symbol = "C"
            elif units.lower() == "fahrenheit":
                temp = current["temp_F"]
                unit_symbol = "F"
            else:
                return f"Unidade de temperatura inválida: {units}"

            return f"A temperatura atual em {cidade} é {temp}°{unit_symbol}."
    except Exception as e:
        return f"Erro ao obter a temperatura de {cidade}: {e}"

# Função principal
async def main():
    chroma = ChromaDBVectorMemory(
        PersistentChromaDBVectorMemoryConfig(
            collection_name="preferences",
            persistence_path="chroma.db",
            embedding_model="text-embedding-3-small",
            k=3,
            score_threshold=0.4,
        )
    )

    # ADICIONANDO conteúdo à memória corretamente (assíncrono)
    await chroma.add(MemoryContent(
        content="A unidade de temperatura deve estar em celsius",
        mime_type=MemoryMimeType.TEXT,
        metadata={"category": "preferences", "type": "unidade"}
    ))

    model_client = OpenAIChatCompletionClient(
        model="gpt-3.5-turbo",
        temperature=0.7,
    )

    agent = AssistantAgent("assistant", model_client, tools=[get_temperatura_atual], memory=[chroma])

    await Console(agent.run_stream(task="Qual é a temperatura em Pindamonhangaba?"))

    await chroma.close()

# Executar
if __name__ == "__main__":
    asyncio.run(main())
