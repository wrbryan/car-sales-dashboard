from dash import html

BACKGROUND_IMAGE_URL = "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=1350&q=80"


def render(children):
    return html.Div(
        style={
            'backgroundImage': f'url({BACKGROUND_IMAGE_URL})',
            'backgroundSize': 'cover',
            'backgroundPosition': 'center',
            'backgroundRepeat': 'no-repeat',
            'minHeight': '100vh',
            'color': '#ffffff',
            'fontFamily': 'Arial, sans-serif'
        },
        children=[
            html.Div(
                style={
                    'backgroundColor': 'rgba(0, 0, 0, 0.45)',
                    'minHeight': '100vh',
                    'padding': '20px'
                },
                children=children
            )
        ]
    )