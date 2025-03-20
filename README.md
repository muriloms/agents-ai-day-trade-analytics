# Day Trade Analytics com Agentes de IA

Este repositório contém uma aplicação desenvolvida em Python com Streamlit para realizar análises avançadas em tempo real dos preços de ações listadas na Nasdaq. A aplicação utiliza agentes inteligentes baseados no modelo DeepSeek via Groq, e ferramentas de visualização interativa para apoiar estratégias de Day Trade.

## Funcionalidades principais

- **Busca e Análise de Dados Financeiros:**
  - Análise técnica e fundamentalista de ações.
  - Recomendações de analistas financeiros.
  - Visualização interativa através de gráficos.

- **Integração com IA (Agentes inteligentes):**
  - Agente de Busca Web: Busca e estrutura notícias com fontes.
  - Agente Financeiro: Análise técnica detalhada, dados fundamentais e notícias financeiras.
  - Multi AI Agent: Integra e uniformiza as respostas dos agentes.

- **Estrutura modular e adaptável:**
  - Fácil adaptação para outros mercados ou segmentos, como ações brasileiras, commodities ou análises setoriais específicas.

## Estrutura do projeto

```
src/
├── agents/
│   ├── __init__.py
│   ├── day_trade_agents.py
│   └── .env
├── pages/
│   └── 1_Day_Trade_Analytics.py
├── tools/
│   ├── __init__.py
│   ├── data_manipulation.py
│   └── plots.py
├── streamlit_app.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Como configurar e executar

### 1. Clone o repositório

```bash
git clone https://github.com/muriloms/agents-ai-day-trade-analytics.git
cd agents-ai-day-trade-analytics
```

### 2. Configuração do Ambiente (usando `uv`)

Caso não tenha instalado o **uv**, siga as instruções [aqui](https://github.com/astral-sh/uv).

Crie um ambiente virtual e instale as dependências:

```bash
uv venv create .venv
uv pip install -r requirements.txt
```

Ative o ambiente:

- Linux / macOS:
  ```bash
  source .venv/bin/activate
  ```

- Windows:
  ```cmd
  .venv\Scripts\activate
  ```

### 3. Configuração da Chave da API do Groq


Obtenha sua chave gratuitamente em [Groq API](https://console.groq.com/).

### 4. Execução da aplicação

Execute o comando abaixo na pasta raiz do projeto:

```bash
streamlit run src/streamlit_app.py
```

A aplicação estará disponível em `http://localhost:8501`

## Como utilizar

- Acesse a página inicial para visão geral.
- Navegue até "Day Trade Analytics" no menu lateral.
- Insira o símbolo do ticker desejado e clique em "Analisar".
- Visualize as análises geradas pelos agentes de IA e gráficos interativos.

---

**Objetivo:** Demonstrar técnicas avançadas de análise e integração com agentes de IA para consultoria em dados e estratégias de investimento.

