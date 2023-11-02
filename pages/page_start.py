from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash

#page_start = dash.register_page(__name__, path="/page_start")


layout = html.Div([
    html.H1(children='WMO Report Game', style={'textAlign':'center'}),
    dcc.Input(id='user-name', type='text'),
    dcc.Input(id='user-age', type='text'),
    dcc.Input(id='user-prof', type='text'),
    html.Button('Start', id='start-button', n_clicks=0),
])

