from dash import html, dcc
import dash_bootstrap_components as dbc

def render(manufacturers):
    return dbc.Row([
        dbc.Col([
            html.Label("Select Manufacturers:", style={'color': '#ffffff', 'fontWeight': '600', 'textShadow': '1px 1px 3px rgba(0,0,0,0.9)'}),
            dcc.Dropdown(
                id='manufacturer-dropdown',
                options=[{'label': m, 'value': m} for m in manufacturers],
                value=[],
                multi=True,
                searchable=True
            )
        ], width=12),
        dbc.Col([
            html.Label("Select Models:", style={'color': '#ffffff', 'fontWeight': '600', 'textShadow': '1px 1px 3px rgba(0,0,0,0.9)'}),
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
            html.Div(id='models-list', style={'marginTop': '0.5rem', 'color': '#ffffff', 'fontWeight': '600', 'textShadow': '1px 1px 3px rgba(0,0,0,0.9)'})
        ], width=12)
    ])
