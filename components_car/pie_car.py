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
    return html.Div(dcc.Graph(id="pie_chart_car"))

@analysis_decorator
def update_figure(df):
    fig = px.pie(df, values='Sales_in_thousands', names='Model_Label', title='Top Models by Sales')
    fig.update_traces(textfont_color='#ffffff')
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0.45)',
        paper_bgcolor='rgba(0, 0, 0, 0.45)',
        title_font_color='#ffffff',
        title_font_size=16,
        font_color='#ffffff',
        legend=dict(
            font=dict(color='#ffffff'),
            bgcolor='rgba(0, 0, 0, 0)'
        )
    )
    return fig