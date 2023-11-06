from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_daq as daq
import plotly.graph_objects as go
import json

# csv 
df_1_2_3 = pd.read_csv('data/figure 1-2-3 GHG decadal analysis.csv')
df_8 = pd.read_csv('data/Figure 8-source data-National extremes by decade melted.csv')

# get the question 
with open('questions.json', 'r') as file:
    size_questions = len(json.load(file))


layout = html.Div([
    html.H1(children='WMO Report Game', className='title'),
    html.Div([
        html.Div([
            html.Div([
                html.P("0/"+ str(size_questions), 
                       id = "score",
                       className='score')],
                className='score-box'),
            html.Div([
                html.P('Dash converts Python classes into HTML'),
            ], id = "question",
            className='quest-box'),
            
            
            
            html.Button('Next', 
                          id='R1-button', 
                          n_clicks=0, 
                          className='reponse'),
            html.Button('Next', 
                          id='R2-button', 
                          n_clicks=0, 
                          className='reponse'),
            html.Button('Next', 
                          id='R3-button', 
                          n_clicks=0, 
                          className='reponse')
        ], className='page-quest-box'),
        html.Div([
            dcc.Dropdown(df_1_2_3["gas"].unique(), 'CO2', 
                         id='dropdown',
                        className='dropdown'),
            dcc.Graph(figure = px.bar(df_1_2_3[df_1_2_3["gas"]=="CO2"], x='Decades', y='averaged mole fraction'), 
                      id='graph',
                     className='graph'),
        ], className='page-quest-box' ),
    ],  
    style={'display': 'flex', 'flex-direction': 'row','justify-content': 'space-around' } ),
    html.Div([html.Button('Next', 
                          id='next-button', 
                          n_clicks=0, 
                          className='button')],
             className='start-box')], 
    className='general')


