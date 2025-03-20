import re
import streamlit as st

import os

# Importa o agente integrado (Multi AI Agent) da pasta agents/
from agents import create_multi_ai_agent

# Importa as funções de extração e plotagem de dados da pasta tools/
from tools import extract_financial_data
from tools import (
    plot_stock_price,
    plot_candlestick,
    plot_media_movel,
    plot_volume
)

# -----------------------------------------------------------------------------
# Configuração da página do Streamlit
st.set_page_config(
    page_title="Day Trade Analytics",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

# -----------------------------------------------------------------------------
# Barra Lateral com instruções
st.sidebar.title("Instruções")
st.sidebar.markdown(
    """
    ### Como Utilizar a App:
    
    - Insira o símbolo do ticker da ação desejada no campo central.
    - Clique no botão **Analisar** para obter a análise em tempo real com visualizações e insights gerados por IA.
    
    ### Exemplos de tickers válidos:
    - MSFT (Microsoft)
    - TSLA (Tesla)
    - AMZN (Amazon)
    - GOOG (Alphabet)
    
    Mais tickers podem ser encontrados aqui: [NASDAQ Stocks](https://stockanalysis.com/list/nasdaq-stocks/)
    
    """
)

# Seção de Configuração para a chave da API Groq
with st.sidebar.expander("Configuração da API Groq"):
    groq_api_key = st.text_input("Digite sua chave da API do Groq:", type="password")
    if groq_api_key:
        st.success("Chave configurada com sucesso!")
    else:
        st.info("Insira a chave da API para ativar os recursos do Groq.")

# -----------------------------------------------------------------------------
# Título principal e cabeçalho
st.header(":chart_with_upwards_trend: Day Trade Analytics em Tempo Real com Agentes de IA")

# -----------------------------------------------------------------------------
# Interface principal - Entrada do usuário
ticker = st.text_input("Digite o Código (símbolo do ticker):").upper()

if st.button("Analisar"):
    if ticker:
        with st.spinner("Buscando os Dados em Tempo Real. Aguarde..."):
            # Extrai os dados do ticker (função definida em tools/extract.py)
            hist = extract_financial_data(ticker)

            if groq_api_key == "":
                st.error("Insira uma chave da API válida")
            else:
                st.subheader("Análise Gerada Por IA")
                # Executa o time de Agentes de IA para processar a consulta do ativo
                multi_ai_agent = create_multi_ai_agent(groq_api_key)

                ai_response = multi_ai_agent.run(
                    f"Resumir a recomendação do analista e compartilhar as últimas notícias para {ticker}"
                )

                # Remove linhas indesejadas da resposta (ex.: logs ou chamadas internas)
                clean_response = re.sub(
                    r"(Running:[\s\S]*?\n\n)|(^transfer_task_to_finance_ai_agent.*\n?)",
                    "",
                    ai_response.content,
                    flags=re.MULTILINE
                ).strip()

                st.markdown(clean_response)

            st.subheader("Visualização dos Dados")
            # Renderiza os gráficos utilizando as funções definidas em tools/graphics.py
            st.plotly_chart(plot_stock_price(hist, ticker))
            st.plotly_chart(plot_candlestick(hist, ticker))
            st.plotly_chart(plot_media_movel(hist, ticker))
            st.plotly_chart(plot_volume(hist, ticker))
    else:
        st.error("Ticker inválido. Insira um símbolo de ação válido.")
