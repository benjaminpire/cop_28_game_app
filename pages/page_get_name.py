from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash

dash.register_page(__name__)


layout = html.Div([
    html.H1('WMO Report Game'),
    dcc.Input(id='user-name', type='text'),
    dcc.Input(id='user-age', type='text'),
    dcc.Input(id='user-prof', type='text'),
    html.Button('Begin', id='start-button', n_clicks=0),
])

@callback(
    Output('url', 'pathname',allow_duplicate=True),
    [Input('start-button', 'n_clicks')],
    prevent_initial_call=True
)

def start_survey(n_clicks):
    if n_clicks > 0:
        return '/page_co2_ghg_analysis'
    raise PreventUpdate

