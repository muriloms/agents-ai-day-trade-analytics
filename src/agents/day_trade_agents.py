
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


import os

def get_api_key() -> str:
    return os.environ.get("GROQ_API_KEY", "")

# =============================================================================
# Módulo: agentes.py
#
# Descrição:
# Este módulo define três agentes para operações financeiras e de
# busca na web. Cada agente possui documentação e instruções
# que garantem a consistência na estrutura de saída
#
# Agentes:
#   - agente_web_search: Responsável por realizar buscas na web e retornar
#                        resultados com fontes sempre identificadas.
#   - agente_financeiro: Especializado em obter informações financeiras,
#                         incluindo preços, recomendações de analistas,
#                         fundamentos e notícias de empresas, retornando
#                         os dados em formato tabular.
#   - multi_ai_agent:    Agente que integra os dois anteriores, unificando
#                        as capacidades e garantindo consistência na saída.
#
# Instruções Gerais:
#   - Sempre incluir as fontes de dados quando disponíveis.
#   - Exibir resultados utilizando tabelas para facilitar a comparação e análise.
#   - Manter a mesma estrutura de saída para consultas semelhantes (ex.: notícias)
#     independentemente do ativo consultado.
#
# =============================================================================

def create_multi_ai_agent(api_key: str = None):
    """
    Cria e retorna o agente integrado Multi AI Agent com a chave da API Groq configurada.

    Parâmetros:
        api_key (str): Chave da API do Groq a ser utilizada pelos agentes.
                       Se não for informada, pode-se usar uma chave padrão definida em config.

    Retorna:
        Agent: Instância do agente integrado com os agentes web search e financeiro configurados.
    """
    # Se a chave não for informada, utiliza a chave padrão importada (se houver)
    if not api_key:
        return None

    # Definição do agente responsável pela busca na web
    agente_web_search = Agent(
        name="Agente Web Search",
        role="Realizar buscas na web e fornecer resultados com fontes detalhadas.",
        model=Groq(id="deepseek-r1-distill-llama-70b"),
        tools=[DuckDuckGo()],
        instructions=[
            "Realize buscas detalhadas e retorne os resultados com as fontes explicitamente listadas.",
            "Padronize a saída para resultados de notícias: utilize uma estrutura de tabela com as seguintes colunas: 'Data', 'Título', 'Fonte' e 'Resumo'.",
            "Mantenha a consistência dos dados retornados, independentemente do ativo pesquisado."
        ],
        show_tool_calls=True,
        markdown=True
    )

    # Definição do agente especializado em informações financeiras
    agente_financeiro = Agent(
        name="Agente Financeiro",
        role="Fornecer informações financeiras, fundamentadas em análise técnica.",
        model=Groq(id="deepseek-r1-distill-llama-70b", api_key=api_key),
        tools=[YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True
        )],
        instructions=[
            "Construa uma análise financeira com base nas informações obtidas. Utilize no máximo 5 linhas.",
            "Seja direto e técnico na análise"
        ],
        show_tool_calls=True,
        markdown=True
    )

    # Definição do agente integrado que utiliza os dois agentes acima
    multi_ai_agent = Agent(
        name="Multi AI Agent",
        role="Integrar as funcionalidades dos agentes de busca web e financeiro, fornecendo respostas completas e uniformes.",
        model=Groq(id="llama-3.3-70b-versatile", api_key=api_key),
        team=[agente_web_search, agente_financeiro],
        instructions=[
            "Sempre inclua as fontes dos dados apresentados.",
            "Seja breve, direto e técnico na análise financeira",
            "Para as notícias, utilize tabelas para exibir resultados, mantendo a mesma estrutura para consultas similares (ex.: notícias de ativos).",
            "Quando realizar uma consulta por um ativo, retorne a estrutura de notícias com as colunas: 'Data', 'Título', 'Fonte', 'Link' e 'Resumo'"
        ],
        show_tool_calls=True,
        markdown=True
    )

    return multi_ai_agent


# Definição do agente responsável pela busca na web
agente_web_search = Agent(
    name="Agente Web Search",
    role="Realizar buscas na web e fornecer resultados com fontes detalhadas.",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGo()],
    instructions=[
        # Instruções para a consulta web:
        "Realize buscas detalhadas e retorne os resultados com as fontes explicitamente listadas.",
        "Padronize a saída para resultados de notícias: utilize uma estrutura de tabela com as seguintes colunas: 'Data', 'Título', 'Fonte' e 'Resumo'.",
        "Mantenha a consistência dos dados retornados, independentemente do ativo pesquisado."
    ],
    show_tool_calls=True,
    markdown=True
)

# Definição do agente especializado em informações financeiras
agente_financeiro = Agent(
    name="Agente Financeiro",
    role="Fornecer informações financeiras, fundamentadas em análise técnica.",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True  # Ativação do módulo de notícias
    )],
    instructions=[
        # Instruções para consulta de dados financeiros:
        "Certifique-se de que os dados exibidos sejam uniformes para diferentes ativos, facilitando a comparação.",
        "Inclua análises comparativas quando aplicável, e sempre liste as fontes dos dados."
    ],
    show_tool_calls=True,
    markdown=True
)

# Definição do agente que integra os agentes de busca e financeiro
multi_ai_agent = Agent(
    name="Multi AI Agent",
    role="Integrar as funcionalidades dos agentes de busca web e financeiro, fornecendo respostas completas e uniformes.",
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[agente_web_search, agente_financeiro],
    instructions=[
        # Instruções gerais para o agente integrado:
        "Sempre inclua as fontes dos dados apresentados.",
        "Utilize tabelas para exibir resultados, mantendo a mesma estrutura para consultas similares (ex.: notícias de ativos).",
        "Quando realizar uma consulta por um ativo, retorne a estrutura de notícias com as colunas: 'Data', 'Título', 'Fonte', 'Link' e 'Resumo', mesmo que a consulta seja feita em momentos distintos ou para ativos diferentes.",
        "Garanta que a saída seja consistente e permita a comparação direta entre diferentes consultas de ativos."
    ],
    show_tool_calls=True,
    markdown=True
)

