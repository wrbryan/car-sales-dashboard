from dash import html, dcc
import dash_bootstrap_components as dbc

def render(manufacturers):
    return dbc.Row([
        dbc.Col([
            html.Label("Select Manufacturers:"),
            dcc.Dropdown(
                id='manufacturer-dropdown',
                options=[{'label': m, 'value': m} for m in manufacturers],
                value=[],
                multi=True,
                searchable=True
            )
        ], width=12),
        dbc.Col([
            html.Label("Select Models:"),
            dcc.Dropdown(
                id='model-dropdown',
                options=[],
                value=[],
                multi=True,
                searchable=True,
                placeholder='Models will appear after manufacturer selection'
            )
        ], width=12),
        dbc.Col([
            html.Div(id='models-list', style={'marginTop': '0.5rem'})
        ], width=12)
    ])
