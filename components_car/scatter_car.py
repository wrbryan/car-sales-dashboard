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
    fig.update_traces(textposition='top center', textfont_size=8, textfont_color='#ffffff')
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0.45)',
        paper_bgcolor='rgba(0, 0, 0, 0.45)',
        title_font_color='#ffffff',
        title_font_size=16,
        xaxis_title_font_color='#ffffff',
        yaxis_title_font_color='#ffffff',
        xaxis=dict(tickfont=dict(color='#ffffff'), gridcolor='rgba(255,255,255,0.2)'),
        yaxis=dict(tickfont=dict(color='#ffffff'), gridcolor='rgba(255,255,255,0.2)'),
        legend=dict(
            font=dict(color='#ffffff'),
            bgcolor='rgba(0, 0, 0, 0)'
        ),
        font_color='#ffffff'
    )
    return fig