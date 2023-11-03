from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_daq as daq

# csv 
df_1_2_3 = pd.read_csv('data/figure 1-2-3 GHG decadal analysis.csv')
df_8 = pd.read_csv('data/Figure 8-source data-National extremes by decade melted.csv')





layout = html.Div([
    html.H1(children='WMO Report Game', className='title'),
    html.Div([
        html.Div([
            html.Div(children = [])
        ], id = "score"),
        html.Div([
            html.Div(children = [])
        ], id = "question"),
    ]),

    html.Div([
        html.Div([
            html.Div(children = [])
        ], id = "dropdown", className='dropdown'),
        html.Div([
            html.Div(children = [])
        ], id = "graph" ),
    ]),

    html.Div([
        dcc.Graph(id='measurement-plot'),
    ],
    ),


    

    # graph 
    dcc.Dropdown(df_1_2_3["gas"].unique(), 'CO2', id='dropdown-gas'),
    html.Div([html.Button('Next', 
                          id='next-button', 
                          n_clicks=0, 
                          className='button')],
             className='start-box')], 
    className='general')


