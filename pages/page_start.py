from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash

#page_start = dash.register_page(__name__, path="/page_start")


layout = html.Div([
    html.H1(children='WMO Report Game', className='title'),
    html.Div([

        html.Div([
            html.H3('Age'),            
            dcc.Input(id='user-age', 
                      type='text', 
                      placeholder="",
                      className='input')],
                 className='start-box'),

        html.Div([
            html.H3('Current ocupation'),            
            dcc.Input(id='user-prof', 
                      type='text',
                      placeholder="",
                      className='input')], 
                 className='start-box'),
    ],  style={'display': 'flex', 'flex-direction': 'row'} ),
    html.Button('Start', 
                id='start-button', 
                n_clicks=0, 
                className='button')])

