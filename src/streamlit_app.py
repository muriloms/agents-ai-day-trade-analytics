import streamlit as st

# Configuração da página inicial do Streamlit
st.set_page_config(
    page_title="Experimento- Home",
    page_icon=":thought_balloon:",
    layout="wide"
)

# Título principal
st.title(":microscope: Experimento")

# Subtítulo / Cabeçalho
st.header(":chart_with_upwards_trend: Day trade analytics com agentes AI")

# Seção de Apresentação
st.markdown(
    """
    ### Finalidade da App:
    
    Este aplicativo realiza análises de preços de ações da Nasdaq em tempo real utilizando Agentes de IA com modelo DeepSeek através do Groq para apoio a estratégias de Day Trade . 

    ---
    
    **Funcionalidades Principais:**
    - Análise de preços e gráficos interativos dos ativos.
    - Informações financeiras detalhadas e recomendações de analistas.
    - Busca e estruturação padronizada de notícias com fontes.
    - Integração de múltiplos agentes de IA para respostas completas e consistentes.
    
    Explore as funcionalidades navegando pelas subpáginas e configurando a chave da API do Groq para ativar todos os recursos.

    ---
    Este aplicativo é uma referência modular que pode ser adaptada para outras áreas além do mercado da Nasdaq. 
    Por exemplo, podemos customizá-lo para:

    - Mercado de Ações Brasileiras: Monitorar e analisar dados de ações da B3, com gráficos e notícias específicas para o cenário econômico brasileiro.
    - Mercado Futuro e Commodities: Integrar dados de futuros e commodities, permitindo acompanhar tendências e identificar oportunidades no mercado de hedge e trading.
    - Análise de Notícias de Segmentos Específicos: Adaptar a estrutura para coletar e analisar notícias de setores como eSports, games ou entretenimento, oferecendo insights baseados em análises de sentimento e tendências.
    - Aplicações de Consultoria Multissetorial: Servir como base para dashboards personalizados em diferentes setores, como tecnologia, moda, saúde e educação, agregando dados e notícias para uma visão estratégica de mercado.
    """
)

