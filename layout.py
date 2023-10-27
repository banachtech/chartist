from dash import dcc, html
import dash_bootstrap_components as dbc

header_row = dbc.Row(dbc.Col(html.H3("FX Monitor", className="text-center"), width=12), className="mb-4")

# Currency specifications
fx_input = html.Div([
        dbc.Label("Ticker"),
        dbc.Input(id="ticker", type="text", value="EURUSD", class_name="mb-2"),
        dbc.Label("Frequency"),
        dcc.Dropdown(
            id="freq",
            options=[
                {"label": "daily", "value": "daily"},
                {"label": "weekly", "value": "weekly"}
            ],
            value="daily"
        ),
])

# Moving average specifications
ma_input = html.Div([
    dbc.Checkbox(id="ma", label="Moving Average"),
    dbc.RadioItems(
        id="ma-type",
        options=[
            {'label': 'simple', 'value': 'SMA'},
            {'label': 'exponential', 'value': 'EMA'}
        ],
        value='SMA',
        inline=True,
        class_name="mb-3 mt-1"
    ),
    dbc.Label("Window"),
    dbc.Input(id="ma-window", type="text", value="10"),
])

# Bollinger bands specifications
bb_input = html.Div([
    dbc.Checkbox(id="bb", label="Bollinger Band"),
    dbc.Label("Window"),
    dbc.Input(id="bb-window", type="text", value="10", class_name="mb-2"),
    dbc.Label("Band Size"),
    dbc.Input(id="bb-band", type="text", value="2,2"),
])

# Additional technical indicators to show in a dedicated chart
indicator = html.Div([
    dbc.Label("Indicator"),
    dbc.RadioItems(
        id="tech-indic",
        options=[
            {'label': 'RSI', 'value': 'RSI'},
            {'label': 'MACD', 'value': 'MACD'},
            {'label': 'STOCH', 'value': 'STOCH'}
        ],
        value='RSI',
        inline=True,
        class_name="mb-3 mt-1"
    ),
])

indicator_params = html.Div([
    dbc.Label("Parameter"),
    dbc.Input(id="tech-param", type="text", value="10", class_name="mb2"),
])

# Price chart with moving average and bollinger bands
price_chart = dcc.Graph(id='price-chart', figure={})

# tech indicator chart with selected indicator
tech_chart = dcc.Graph(id='tech-chart', figure={})

# Piece together layouts
layout = dbc.Container([
    header_row,
    dbc.Row([
        dbc.Col(fx_input, width=3),
        dbc.Col(ma_input, width=3),
        dbc.Col(bb_input, width=3),
        dbc.Col(html.Button("Update Plots", id="update-charts",n_clicks=0)),
    ],class_name="mt-4 mb-2"),
    dbc.Row([
        dbc.Col(dbc.Spinner(price_chart, color="primary"), width=12)
    ], class_name="mb-4"),
    dbc.Row([
        dbc.Col(indicator, width=9),
    ], class_name="mb-2"),
    dbc.Row([
        dbc.Col(dbc.Spinner(tech_chart, color="primary"), width=12),
    ], class_name="mb-2")
], fluid=True, class_name="p-4")