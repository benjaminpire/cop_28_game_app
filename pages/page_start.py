from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash

#page_start = dash.register_page(__name__, path="/page_start")


layout = html.Div([
    html.H1(children='WMO Report Game', className='title'),
    html.Div([
        html.Div([dcc.Input(id='user-name', 
                      type='text', 
                      placeholder="",
                      className='input')],
                 style={'left': '10px'}, 
                 className='start-box'),
        html.Div([dcc.Input(id='user-age', 
                      type='text', 
                      placeholder="",
                      className='input')],
                 className='start-box'),

        html.Div([dcc.Input(id='user-prof', 
                      type='text',
                      placeholder="",
                      className='input')], 
                 className='start-box'),
    ],  style={'display': 'flex', 'flex-direction': 'row'} ),
    html.Div([html.Button('Start', 
                id='start-button', 
                n_clicks=0, 
                className='button')],
             className='start-box')],
    className='general')

