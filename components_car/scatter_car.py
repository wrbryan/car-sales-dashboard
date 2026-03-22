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
        dcc.Graph(id='scatter-chart-car')
    ])

@analysis_decorator
def update_figure(df):
    fig = px.scatter(df, x='Horsepower', y='Fuel_efficiency', color='Manufacturer',
                     text='Model_Label', title='Horsepower vs Fuel Efficiency')
    fig.update_traces(textposition='top center', textfont_size=8)
    return fig