from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import json
import dash


app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=['style.css'])
image_path = 'assets/background.jpg'

html.Img(src=image_path)

# Import the diferent pages 
from pages import page_start
from pages import page_question
from pages import page_end

page_number = 1

# csv 
df_1_2_3 = pd.read_csv('data/figure 1-2-3 GHG decadal analysis.csv')
df_8 = pd.read_csv('data/Figure 8-source data-National extremes by decade melted.csv')
df_9 = pd.read_csv('data/Figure 9 - dec global ocean heat content (OHC) anomalies.csv')
df_11 = pd.read_csv('data/Figure 11 - dec Evolution of the global mean sea level.csv')
df_16 = pd.read_csv('data/Figure 16 cumulative mass balance decades.csv')
df_17 = pd.read_csv('data/Figure 17 - Sea ice seasonal extremes decadal.csv')


# get the question 
with open('questions.json', 'r') as file:
    questions = json.load(file)

question_number = 0

#########
#demain tu fais un csv avec url de pages, question exct....
#########

# Define the app layout as HTML and css
app.layout = html.Div([
    dcc.Location(id='url',pathname = "/page_start", refresh=True),
    html.Div(id='page-content', children = page_start.layout, className='general'),
])



###################################
# Game process callbacks 
###################################


@callback(
    Output('page-content', 'children', allow_duplicate=True),
    [Input('start-button', 'n_clicks'),
    Input('url', 'pathname')],
    prevent_initial_call=True
)
def start_survey(n_clicks_start, pathname):
    if n_clicks_start > 0:
        return page_question.layout 
    else: 
        return page_start.layout


@callback(
    [Output('q_number', 'data'),
    Output('graph_box', 'children'),
    Output('question', 'children'),
    Output('answer', 'children'),
    Output('score_display', 'children')],
    [Input('next-button', 'n_clicks'),
    Input('q_number', 'data'),
    Input('score', 'data')]
)
def next_question(n_clicks_next, q_number, score):
    
    if n_clicks_next > 0:
        q_number+= 1
        
#    if (q_number<len(questions) & q_number<len(page_question.quest_page_list)):
    return (q_number, 
            page_question.quest_page_list[q_number], 
            [html.P(questions[q_number]['question'])],
            page_question.layout_answers[q_number],
            (str(score) + '/' + str(len(questions))))

#####
##TODO 
"""
@callback(
    [Output('score_display', 'children')],
    [Input('clicks', 'n_clicks')],
)
def answer_question():
"""    
#####




'''
@callback(
    Output('page-content', 'children', allow_duplicate=True),
    [Input('next-button', 'n_clicks'),
    Input('url', 'pathname'),
    Input('q_number', 'data')],
    prevent_initial_call=True
)
def display_end (n_clicks_end, pathname, q_number):
    if ((n_clicks_end > 0)|(q_number>len(questions))):
        return page_end.layout 
    else: 
        return page_question.layout
'''     


###################################
# score management callbacks 
###################################





###################################
# dropdown callbacks
###################################
@callback(
    Output('graph', 'figure'),
    Input('dropdown1_1', 'value'),
)
def update_graph(value):
    dff = df_1_2_3[df_1_2_3["gas"]==value]
    return px.bar(dff, x='Decades', y='averaged mole fraction')

    
    
@callback(
    Output('graph', 'figure', allow_duplicate=True),
    [Input('dropdown2_1', 'value'),
    Input('dropdown2_2', 'value')],
    prevent_initial_call=True
)
def update_graph(mesure, region):
    dff = df_8[(df_8["Mesure"]==mesure) & (df_8["region"]==region)]
    return px.bar(dff, x='Decades', y='value')


@callback(
    Output('graph', 'figure', allow_duplicate=True),
    Input('dropdown3_1', 'value'),
    prevent_initial_call=True
)
def update_graph(depth):
    dff = df_9[(df_9["depth"]==depth)]
    return px.bar(dff, x='Decades', y='value')


@callback(
    Output('graph', 'figure', allow_duplicate=True),
    Input('dropdown6_1', 'value'),
    prevent_initial_call=True
)
def update_graph(depth):
    dff = df_16[(df_16["Greenland/Antartica"]==depth)]
    return px.bar(dff, x='Decades', y='Cumulative mass balance (Gt)')




## If app.layout.getbyid(id='page-content').children ==
    
###str(value_score) + '/' + str(len(questions))
    
## if cli sur next 



## if click sur finish 


## finish page 

if __name__ == '__main__':
    app.run(debug=True)