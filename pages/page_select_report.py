from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash

wmo_logo = 'assets/img/wmo_logo.jpg'
decadal_report_logo = 'assets/img/decadal.png'


layout = html.Div([
    html.Img(src=wmo_logo, style={'height':'150px', 'width':'150px'}),
    html.Div([
        html.Div([
            html.H5(children='The WMO game'),
            html.Button(children=html.Img(src=decadal_report_logo, 
                                          style={'height':'200px', 'width':'200px'}),
                        id='decadal_version', 
                        n_clicks=0, 
                        className='button_version')],
            style={'display':'flex', 'flex-direction':'column'},
            className='question_text')],
        className='start-box'),
    html.Button('Select', 
                id='select_button', 
                n_clicks=0, 
                className='button',
                style = {'display': 'none'})], className='general')


