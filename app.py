from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import layout as lyt
import callbacks as cb

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = lyt.layout

@app.callback(
    Output("price-chart", "figure"),
    [State("ticker", "value"),
     State("freq", "value"),
     State("ma", "value"),
     State("ma-type", "value"),
     State("ma-window", "value"),
     State("bb", "value"),
     State("bb-window", "value"),
     State("bb-band", "value"),
     Input("update-charts", "n_clicks")],
     prevent_initial_call=True
)
def plot_fx_price(
        ticker: str, 
        freq: str,
        ma: bool, 
        ma_type: str, 
        ma_window: str,
        bb: bool,
        bb_window: str,
        bb_band: str,
        n: int):
    return cb.make_price_plot(ticker, freq, ma, ma_type, ma_window, bb, bb_window, bb_band)

@app.callback(
        Output("tech-chart", "figure"), 
        [Input("ticker", "value"),
         Input("freq", "value"),
         Input("tech-indic", "value"),
         Input("update-charts", "n_clicks")],
        prevent_initial_call=True)
def plot_fx_tech(ticker, freq, indicator, n):
    return cb.make_tech_plot(ticker, freq, indicator)

if __name__ == '__main__':
    app.run_server(debug=True)