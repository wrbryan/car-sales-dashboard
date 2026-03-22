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
    fig.update_layout(
        plot_bgcolor='rgba(255, 255, 255, 0.1)',
        paper_bgcolor='rgba(255, 255, 255, 0.1)',
        title_font_color='#ffffff',
        title_font_size=16,
        xaxis_title_font_color='#ffffff',
        yaxis_title_font_color='#ffffff',
        font_color='#ffffff'
    )
    return fig