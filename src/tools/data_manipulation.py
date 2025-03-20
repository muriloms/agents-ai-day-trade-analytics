
import yfinance as yf

def extract_financial_data(ticker:str, period:str = "6mo"):

    # Cria um objeto Ticker do Yahoo Finance para a ação especificada
    stock = yf.Ticker(ticker)
    
    # Obtém o histórico de preços da ação para o período definido
    hist = stock.history(period=period)
    
    # Reseta o índice do DataFrame para transformar a coluna de data em uma coluna normal
    hist.reset_index(inplace=True)
    
    return hist