from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_daq as daq
import plotly.graph_objects as go
import json

# csv 

# get the question 
with open('questions.json', 'r') as file:
    questions = json.load(file)

###############
#layout question 1
###############
df_1_2_3 = pd.read_csv('data/figure 1-2-3 GHG decadal analysis.csv')
layout_q1 =[dcc.Dropdown(df_1_2_3["gas"].unique(), 'CO2', 
                         id='dropdown1_1',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_1_2_3[df_1_2_3["gas"]=="CO2"], x='Decades', y='averaged mole fraction'), 
                      id='graph',
                     className='graph')]
# answers
layout_answers =[[html.Button(children= answer, 
                              id='R1_button', 
                              n_clicks=0, 
                              className='reponse') for answer in questions[j]['options']] for j in range(len(questions))]

###############
#layout base with question 1
###############

layout = html.Div([
    dcc.Store(id='q_number', data=0),
    dcc.Store(id='score', data=1),
    html.H1(children='WMO Report Game', className='title'),
    html.P("0/"+ str(len(questions)), 
           id = "score_display",
           className='score'),
    html.Div([
        html.Div([dcc.Dropdown(df_1_2_3["gas"].unique(), 'CO2', 
                               id='dropdown1_1',
                               className='dropdown'),
                  dcc.Graph(figure = px.bar(df_1_2_3[df_1_2_3["gas"]=="CO2"], x='Decades', y='averaged mole fraction'), 
                            id='graph',
                            className='graph')], 
                 id='graph_box',
                 className='sub-page-quest-box' ),
        html.Div([
            html.Div([
                html.P(questions[0]['question']),
            ], id = "question",
            className='quest-box'),
            html.Div(layout_answers[0], id="answer")
        ], className='sub-page-quest-box')
    ], className='page-quest-box'),
    html.Button('Next', 
                id='next-button', 
                n_clicks=0, 
                className='button')],
    className='general')






###############
# layout question 2
###############
df_8 = pd.read_csv('data/Figure 8-source data-National extremes by decade melted.csv')
# Graphs
layout_graph_q2 = [dcc.Dropdown(df_8["Mesure"].unique(), 'High temp', 
                         id='dropdown2_1',
                         className='dropdown'),
            dcc.Dropdown(df_8["region"].unique(), 'RA I', 
                         id='dropdown2_2',
                         className='dropdown'),
                dcc.Graph(figure = px.bar(df_8[(df_8["Mesure"]=="High temp") & (df_8["region"]=="RA I") ], x='Decades', y='value'), 
                      id='graph',
                     className='graph')]






###############
#layout question 3
###############
df_9 = pd.read_csv('data/Figure 9 - dec global ocean heat content (OHC) anomalies.csv')

layout_q3 =[dcc.Dropdown(df_9["depth"].unique(), '0-300m', 
                         id='dropdown3_1',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_9[df_9["depth"]=="0-300m"], x='Decades', y='value'), 
                      id='graph',
                     className='graph')]


###############
#layout question 4
###############
df_11 = pd.read_csv('data/Figure 11 - dec Evolution of the global mean sea level.csv')
layout_q4 =[dcc.Graph(figure = px.bar(df_11, x='Decades', y='global mean sea level'), 
                      id='graph',
                     className='graph')]

###############
#layout question 5
###############
df_14 = pd.read_csv('data/Figure 14 decade global annual mass change of reference glaciers (left).csv')
layout_q5 =[dcc.Graph(figure = px.bar(df_14, x='Decades', y='Annual Mass Change in m.w.e'), 
                      id='graph',
                     className='graph')]


###############
#layout question 6
###############
df_16 = pd.read_csv('data/Figure 16 cumulative mass balance decades.csv')
layout_q6 =[dcc.Dropdown(df_16["Greenland/Antartica"].unique(), 'Greenland', 
                         id='dropdown6_1',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_16[df_16["Greenland/Antartica"]=="Greenland"], x='Decades', y='Cumulative mass balance (Gt)'), 
                      id='graph',
                     className='graph')]

'''
###############
#layout question 7
###############
df_17 = pd.read_csv('data/Figure 17 - Sea ice seasonal extremes decadal.csv')
layout_q7 =[dcc.Dropdown(df_17["gas"].unique(), 'CO2', 
                         id='dropdown',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_17[df_17["gas"]=="CO2"], x='Decades', y='averaged mole fraction'), 
                      id='graph',
                     className='graph')]
'''


quest_page_list = [layout_q1,
                   layout_graph_q2,
                   layout_q3,
                   layout_q4,
                   layout_q5,
                   layout_q6]



