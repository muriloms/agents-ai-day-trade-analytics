import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plot_stock_price(hist: pd.DataFrame, ticker: str) -> 'plotly.graph_objs._figure.Figure':
    """
    Cria e retorna um gráfico de linha representando o preço de fechamento das ações.

    Parameters:
        hist (pd.DataFrame): DataFrame contendo o histórico da ação com as colunas "Date" e "Close".
        ticker (str): Código ou nome da ação para inclusão no título do gráfico.
    
    Returns:
        plotly.graph_objs._figure.Figure: Objeto do gráfico de linha.
    """
    fig = px.line(
        hist, 
        x="Date", 
        y="Close", 
        title=f"{ticker} Preços das Ações (Últimos 6 Meses)", 
        markers=True
    )
    return fig

def plot_candlestick(hist: pd.DataFrame, ticker: str) -> 'plotly.graph_objs._figure.Figure':
    """
    Cria e retorna um gráfico de candlestick para representar a variação dos preços da ação.

    Parameters:
        hist (pd.DataFrame): DataFrame contendo o histórico da ação com as colunas "Date", "Open", "High", "Low" e "Close".
        ticker (str): Código ou nome da ação para inclusão no título do gráfico.

    Returns:
        plotly.graph_objs._figure.Figure: Objeto do gráfico de candlestick.
    """
    fig = go.Figure(
        data=[go.Candlestick(
            x=hist['Date'],
            open=hist['Open'],
            high=hist['High'],
            low=hist['Low'],
            close=hist['Close']
        )]
    )
    fig.update_layout(title=f"{ticker} Candlestick Chart (Últimos 6 Meses)")
    return fig

def plot_media_movel(hist: pd.DataFrame, ticker: str) -> 'plotly.graph_objs._figure.Figure':
    """
    Calcula as médias móveis simples (SMA) e exponencial (EMA) de 20 períodos e cria um gráfico de linha com esses dados.

    Parameters:
        hist (pd.DataFrame): DataFrame contendo o histórico da ação com a coluna "Close".
                             As colunas "SMA_20" e "EMA_20" serão calculadas e adicionadas.
        ticker (str): Código ou nome da ação para inclusão no título do gráfico.

    Returns:
        plotly.graph_objs._figure.Figure: Objeto do gráfico de linha com as médias móveis.
    """
    hist = hist.copy()  # Evita modificar o DataFrame original
    hist['SMA_20'] = hist['Close'].rolling(window=20).mean()
    hist['EMA_20'] = hist['Close'].ewm(span=20, adjust=False).mean()
    
    fig = px.line(
        hist, 
        x='Date', 
        y=['Close', 'SMA_20', 'EMA_20'],
        title=f"{ticker} Médias Móveis (Últimos 6 Meses)",
        labels={'value': 'Price (USD)', 'Date': 'Date'}
    )
    return fig

def plot_volume(hist: pd.DataFrame, ticker: str) -> 'plotly.graph_objs._figure.Figure':
    """
    Cria e retorna um gráfico de barras representando o volume de negociação da ação.

    Parameters:
        hist (pd.DataFrame): DataFrame contendo o histórico da ação com as colunas "Date" e "Volume".
        ticker (str): Código ou nome da ação para inclusão no título do gráfico.

    Returns:
        plotly.graph_objs._figure.Figure: Objeto do gráfico de barras.
    """
    fig = px.bar(
        hist, 
        x='Date', 
        y='Volume', 
        title=f"{ticker} Trading Volume (Últimos 6 Meses)"
    )
    return fig
