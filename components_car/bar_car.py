from dash import html, dcc
import plotly.express as px

def analysis_decorator(func):
    def wrapper(df):
        if df.empty:
            import plotly.graph_objects as go
            fig = go.Figure()
            fig.update_layout(title="No data available for selected filters")
            return fig
        return func(df)
    return wrapper

def render():
    return html.Div([
        dcc.Graph(id='bar-chart-car')
    ])

@analysis_decorator
def update_figure(df):
    fig = px.bar(df, x='Model_Label', y='Sales_in_thousands', title='Top Models by Sales')
    return fig