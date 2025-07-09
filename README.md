# 🚀 Bootcamp LLM4Devs - Projeto de Agentes

Este repositório contém os estudos práticos da sessão de **Agentes** do bootcamp LLM4Devs. O projeto demonstra diferentes conceitos e implementações de agentes de IA usando a biblioteca AutoGen.

## 📋 Sobre o Projeto

Este é um projeto de estudo que explora os conceitos fundamentais de agentes de IA, desde implementações básicas até sistemas mais complexos com múltiplos agentes, ferramentas personalizadas e memória vetorial.

## 🎯 Objetivos de Aprendizado

- Compreender os conceitos básicos de agentes de IA
- Implementar agentes com ferramentas personalizadas
- Trabalhar com múltiplos agentes em equipe
- Integrar agentes com APIs externas
- Implementar sistemas de memória vetorial (RAG)
- Interagir com agentes através de interface de usuário

## 📁 Estrutura do Projeto

### 1. `1_agente.py` - Agente Básico
- **Descrição**: Implementação mais simples de um agente usando AutoGen
- **Funcionalidade**: Demonstra como criar um agente básico que responde a perguntas
- **Conceitos**: Agente assistente, cliente OpenAI, interface de console

### 2. `2_tool_temperatura.py` - Agente com Ferramenta Simples
- **Descrição**: Agente com uma ferramenta personalizada para consultar temperatura
- **Funcionalidade**: Simula uma API de temperatura (dados mockados)
- **Conceitos**: Ferramentas personalizadas, integração de funções

### 3. `3_tools_clima.py` - Agente com Múltiplas Ferramentas de Clima
- **Descrição**: Agente especializado em informações climáticas com múltiplas ferramentas
- **Funcionalidade**: 
  - Consulta temperatura real via API wttr.in
  - Verifica umidade relativa
  - Fornece conselhos climáticos baseados nas condições
- **Conceitos**: APIs externas, múltiplas ferramentas, tratamento de erros

### 4. `4_agentes_team.py` - Equipe de Agentes
- **Descrição**: Sistema com múltiplos agentes trabalhando em equipe
- **Funcionalidade**: 
  - Agente escritor: Cria conteúdo sobre Pindamonhangaba
  - Agente crítico: Avalia e critica o conteúdo
- **Conceitos**: Trabalho em equipe, condições de terminação, chat em grupo

### 5. `5_agentes_humano_team.py` - Equipe com Participação Humana
- **Descrição**: Equipe de agentes que inclui participação humana
- **Funcionalidade**: Permite que um humano participe da conversa com os agentes
- **Conceitos**: Agente proxy de usuário, interação humano-máquina

### 6. `6_rag_tools.py` - Agente com Memória Vetorial (RAG)
- **Descrição**: Agente com sistema de memória vetorial usando ChromaDB
- **Funcionalidade**: 
  - Armazena preferências do usuário
  - Consulta temperatura com base em preferências armazenadas
- **Conceitos**: RAG (Retrieval-Augmented Generation), memória vetorial, ChromaDB

## 🛠️ Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI com API key válida
- Conexão com internet (para APIs externas)

## ⚙️ Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd bootcamp-llm4devs-agents
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com sua chave da OpenAI:

```env
OPENAI_API_KEY=sua_chave_api_aqui
```

## 🚀 Como Executar

### Execução Individual dos Exemplos

Cada arquivo pode ser executado independentemente:

```bash
# Agente básico
python 1_agente.py

# Agente com ferramenta de temperatura
python 2_tool_temperatura.py

# Agente com múltiplas ferramentas de clima
python 3_tools_clima.py

# Equipe de agentes
python 4_agentes_team.py

# Equipe com participação humana
python 5_agentes_humano_team.py

# Agente com memória vetorial
python 6_rag_tools.py
```

### Ordem Recomendada de Estudo

Para melhor compreensão dos conceitos, recomenda-se seguir esta ordem:

1. **`1_agente.py`** - Conceitos básicos
2. **`2_tool_temperatura.py`** - Introdução a ferramentas
3. **`3_tools_clima.py`** - Ferramentas avançadas e APIs
4. **`4_agentes_team.py`** - Trabalho em equipe
5. **`5_agentes_humano_team.py`** - Interação humana
6. **`6_rag_tools.py`** - Memória vetorial

## 📚 Conceitos Abordados

### Agentes
- **AssistantAgent**: Agente assistente que processa tarefas
- **UserProxyAgent**: Agente que representa o usuário humano

### Ferramentas (Tools)
- Funções personalizadas que os agentes podem chamar
- Integração com APIs externas
- Tratamento de erros e validação

### Equipes de Agentes
- **RoundRobinGroupChat**: Sistema de chat em grupo
- Condições de terminação
- Coordenação entre múltiplos agentes

### Memória Vetorial
- **ChromaDB**: Banco de dados vetorial
- **RAG**: Recuperação de informações relevantes
- Persistência de dados e preferências

## 🔧 Dependências Principais

- `autogen-agentchat`: Framework principal para agentes
- `autogen-ext`: Extensões para integração com OpenAI
- `httpx`: Cliente HTTP para APIs externas
- `python-dotenv`: Gerenciamento de variáveis de ambiente

## 🌟 Funcionalidades Destacadas

### APIs Integradas
- **wttr.in**: API pública para dados climáticos
- **OpenAI GPT**: Modelo de linguagem para processamento

### Interface de Usuário
- Console interativo para comunicação com agentes
- Stream de respostas em tempo real

### Sistema de Memória
- Armazenamento persistente de preferências
- Recuperação contextual de informações

## 🤝 Contribuição

Este é um projeto de estudo do bootcamp LLM4Devs. Sinta-se à vontade para:
- Experimentar com diferentes configurações
- Adicionar novas ferramentas
- Melhorar o tratamento de erros
- Implementar novos tipos de agentes

## 📖 Recursos Adicionais

- [Documentação AutoGen](https://microsoft.github.io/autogen/)
- [LLM4Devs Bootcamp](https://llmbootcamp.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 👨‍💻 Autor

**Desenvolvido por:** Gabriel Vicente  
**Projeto:** Estudos práticos do bootcamp LLM4Devs  
**Data:** 2025

Este projeto representa meus estudos e experimentações com agentes de IA durante o bootcamp LLM4Devs.

