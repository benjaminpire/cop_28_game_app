from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash

#page_start = dash.register_page(__name__, path="/page_start")
wmo_logo = 'assets/wmo_logo.jpg'
decadal_report_logo = 'assets/decadal.png'


layout = html.Div([
    html.Img(src=wmo_logo, style={'height':'150px', 'width':'150px'}),
    html.Div([
        html.Div([
            html.H5(children='The WMO game'),
            html.H1(children='Do you want to understand climate change and its consequences ?')],
            style={'display':'flex', 'flex-direction':'column'},
            className='question_text')],
        className='start-box'),
    html.Div([
        html.Button(children=html.Img(src=decadal_report_logo, style={'height':'200px', 'width':'200px'}),
                    id='decadal_version', 
                    n_clicks=0, 
                    className='button_version')],
        className='start-box'),
    html.Button('Start', 
                id='start-button', 
                n_clicks=0, 
                className='button')], className='general')



