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
        dcc.Graph(id='horizontal-bar-chart-car')
    ])

@analysis_decorator
def update_figure(df):
    fig = px.bar(df, x='Sales_in_thousands', y='Model_Label', orientation='h', title='Top Models by Sales (Horizontal)')
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0.45)',
        paper_bgcolor='rgba(0, 0, 0, 0.45)',
        title_font_color='#ffffff',
        title_font_size=16,
        xaxis_title_font_color='#ffffff',
        yaxis_title_font_color='#ffffff',
        xaxis=dict(tickfont=dict(color='#ffffff'), gridcolor='rgba(255,255,255,0.2)'),
        yaxis=dict(tickfont=dict(color='#ffffff'), gridcolor='rgba(255,255,255,0.2)'),
        font_color='#ffffff'
    )
    return fig