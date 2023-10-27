import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('data.csv', parse_dates=True, index_col = 'timestamp')

def make_price_plot(
        ticker: str, 
        freq: str,
        ma: bool, 
        ma_type: str, 
        ma_window: str,
        bb: bool,
        bb_window: str,
        bb_band: str) -> go.Figure:  
    
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'],
                name=ticker)]) 
    if ma:
        fig.add_trace(go.Scatter(x=df.index, y=df['sma'], mode='lines', name='sma'))
    if bb:
        fig.add_trace(go.Scatter(x=df.index, y=df['bb_lower'], mode='lines', name='BB_LOWER'))
        fig.add_trace(go.Scatter(x=df.index, y=df['bb_upper'], mode='lines', name='BB_UPPER'))
    return fig
    
def make_tech_plot(
        ticker: str,
        freq: str,
        indicator: str
):
    traces = None
    if indicator == 'RSI':
        traces = [go.Scatter(x=df.index, y=df['rsi'], mode="lines", name='rsi')]
    elif indicator == 'MACD':
        traces = [go.Scatter(x=df.index, y=df['macd'], mode="lines", name='macd')]
    elif indicator == 'STOCH':
        traces = [
            go.Scatter(x=df.index, y=df['percent_k'], mode="lines", name='percent_k'),
            go.Scatter(x=df.index, y=df['percent_d'], mode="lines", name='percent_d')
        ]
    return {"data": traces}
