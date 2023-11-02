from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# csv 
df_1_2_3 = pd.read_csv('data/figure 1-2-3 GHG decadal analysis.csv')
df_8 = pd.read_csv('data/Figure 8-source data-National extremes by decade melted.csv')





layout = html.Div([
    html.H1(children='Question 1', style={'textAlign':'center'}),
    html.Div([
        html.Div(children = [])
    ], id = "score"),
    html.Div([
        html.Div(children = [])
    ], id = "question"),
    html.Div([
        html.Div(children = [])
    ], id = "dropdown"),
    html.Div([
        html.Div(children = [])
    ], id = "graph" ),
    # question
    html.Div(id='question-container'),
    html.Div(id='options-container'),
    html.Div(id='results-container', style={'display': 'none'}),
    
    # graph 
    dcc.Dropdown(df_1_2_3["gas"].unique(), 'CO2', id='dropdown-gas'),
    dcc.Graph(id='graph-content-1-2-3'),
    html.Button('Next', id='next-button'),
])


