from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_daq as daq
import plotly.graph_objects as go
import json

# csv 
wmo_logo = 'assets/wmo_logo.jpg'



# get the question 
with open('questions.json', 'r') as file:
    questions = json.load(file)

###############
#layout question 1
###############
df_1_2_3 = pd.read_csv('data/data_reshaped/figure 1-2-3 GHG decadal analysis.csv')
layout_q1 =[dcc.Dropdown(df_1_2_3["gas"].unique(), 'CO2', 
                         id='dropdown1_1',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_1_2_3[df_1_2_3["gas"]=="CO2"], x='Decade', y='averaged mole fraction'), 
                      id='graph',
                     className='graph')]


###############
# layout question 2
###############
df_8 = pd.read_csv('data/data_reshaped/Figure_08_source_data_National_extremes_by_decade.csv')
# Graphs
layout_q2 = [dcc.Dropdown(df_8["region"].unique(), 'Africa', 
                         id='dropdown2_1',
                         className='dropdown'),
                dcc.Graph(figure = px.bar(df_8[df_8["region"]=="Africa"], x='Decade', y='value'), 
                      id='graph',
                     className='graph')]


###############
#layout question 3
###############
df_9 = pd.read_csv('data/data_reshaped/Figure 9 - dec global ocean heat content (OHC) anomalies.csv')

layout_q3 =[dcc.Dropdown(df_9["depth"].unique(), '0-300m', 
                         id='dropdown3_1',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_9[df_9["depth"]=="0-300m"], x='Decades', y='value'), 
                      id='graph',
                     className='graph')]


###############
#layout question 4
###############
df_11 = pd.read_csv('data/data_reshaped/Figure 11 - dec Evolution of the global mean sea level.csv')
layout_q4 =[dcc.Graph(figure = px.bar(df_11, x='Decade', y='global mean sea level'), 
                      id='graph',
                     className='graph')]

###############
#layout question 5
###############
df_14 = pd.read_csv('data/data_reshaped/Figure 14 decade global annual mass change of reference glaciers (left).csv')
layout_q5 =[dcc.Graph(figure = px.bar(df_14, x='Decades', y='Annual Mass Change in m.w.e'), 
                      id='graph',
                     className='graph')]

###############
#layout question 6
###############
df_16 = pd.read_csv('data/data_reshaped/Figure 16 cumulative mass balance decades.csv')
layout_q6 =[dcc.Dropdown(df_16["Greenland/Antartica"].unique(), 'Greenland', 
                         id='dropdown6_1',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_16[df_16["Greenland/Antartica"]=="Greenland"], x='Decades', y='Cumulative mass balance (Gt)'), 
                      id='graph',
                     className='graph')]

###############
#layout question 7
###############
df_17 = pd.read_csv('data/data_reshaped/Figure 17 - Sea ice seasonal extremes year.csv')
layout_q7 =[dcc.Dropdown(df_17["S_N"].unique(), 'Arctic', 
                         id='dropdown7_1',
                        className='dropdown'),
            dcc.Dropdown(df_17["max_min"].unique(), 'max', 
                         id='dropdown7_2',
                         className='dropdown'),
            dcc.Graph(figure = px.line(df_17[(df_17["S_N"]=="Arctic") & (df_17["max_min"]=="max")], x='Date', y='value'), 
                      id='graph',
                     className='graph')]

###############
#layout question 8
###############
df_16 = pd.read_csv('data/data_reshaped/Figure 16 cumulative mass balance decades.csv')
layout_q8 =[dcc.Dropdown(df_16["Greenland/Antartica"].unique(), 'Greenland', 
                         id='dropdown6_1',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_16[df_16["Greenland/Antartica"]=="Greenland"], x='Decades', y='Cumulative mass balance (Gt)'), 
                      id='graph',
                     className='graph')]

###############
#layout question 9
###############
df_16 = pd.read_csv('data/data_reshaped/Figure 16 cumulative mass balance decades.csv')
layout_q9 =[dcc.Dropdown(df_16["Greenland/Antartica"].unique(), 'Greenland', 
                         id='dropdown6_1',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_16[df_16["Greenland/Antartica"]=="Greenland"], x='Decades', y='Cumulative mass balance (Gt)'), 
                      id='graph',
                     className='graph')]

###############
#layout question 10
###############
df_16 = pd.read_csv('data/data_reshaped/Figure 16 cumulative mass balance decades.csv')
layout_q10 =[dcc.Dropdown(df_16["Greenland/Antartica"].unique(), 'Greenland', 
                         id='dropdown6_1',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_16[df_16["Greenland/Antartica"]=="Greenland"], x='Decades', y='Cumulative mass balance (Gt)'), 
                      id='graph',
                     className='graph')]


quest_page_list = [layout_q1,
                   layout_q2,
                   layout_q3,
                   layout_q4,
                   layout_q5,
                   layout_q6,
                   layout_q7,
                   layout_q8,
                   layout_q9,
                   layout_q10]


###############
#layout base
###############

# answers
layout_answers =[[html.Button(children = answer, 
                              id='button_R_'+str(i), 
                              n_clicks=0, 
                              className='reponse') for i, answer in enumerate(questions[j]['options'])] for j in range(len(questions))]



layout = html.Div([

    # Header
    dcc.Store(id='q_number', data=0),
    dcc.Store(id='score', data=0),
    html.Div([html.Img(src=wmo_logo, style={'height':'100px', 'width':'100px'}),
              html.H1(children='Game', className='title')]),
    html.P("0/"+ str(len(questions)), 
           id = "score_display",
           className='score'),
    html.H5(children=questions[0]['text'],
            id = "explaina_of_quest",
            className='question_text'),

    html.Div([ 
    # Dropdown + Graph 
        html.Div([
            dcc.Dropdown(df_1_2_3["gas"].unique(), 'CO2', 
                         id='dropdown1_1',
                         className='dropdown'),
            dcc.Graph(figure = px.bar(df_1_2_3[df_1_2_3["gas"]=="CO2"], x='Decade', y='averaged mole fraction'), 
                      id='graph',
                      className='graph')
        ], id='graph_box', className='sub-page-quest-box' ),
    # Question + Answers
        html.Div([
            # Question
            html.Div([
                html.P(questions[0]['question']),
            ], id = "question",
            className='quest-box'),
            
            # Answers
            html.Div(layout_answers[0], id="answer"),
            dcc.Store(id='good_responds', data=questions[0]['answer']),
            dcc.Store(id='responded_answered', data=None)
        ], className='sub-page-quest-box')
    ], className='page-quest-box'),

    # Footer  
    html.Div([
        html.Div([
            html.Button('Next question', 
                        id='next-button', 
                        n_clicks=0, 
                        className='button',
                        style = {'display': 'none'})], className='button_box'),
        html.Div([
            html.Button('Get the result', 
                        id='answer-button', 
                        n_clicks=0, 
                        className='button',
                        style = {'display': 'none'})], className='button_box')
    ], className='page-quest-box')]
    ,className='general')



