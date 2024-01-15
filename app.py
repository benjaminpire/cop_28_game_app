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
df_1_2_3 = pd.read_csv('data/data_reshaped/figure 1-2-3 GHG decadal analysis.csv')
df_8 = pd.read_csv('data/data_reshaped/Figure_08_source_data_National_extremes_by_decade.csv')
df_9 = pd.read_csv('data/data_reshaped/Figure 9 - dec global ocean heat content (OHC) anomalies.csv')
df_11 = pd.read_csv('data/data_reshaped/Figure 11 - dec Evolution of the global mean sea level.csv')
df_16 = pd.read_csv('data/data_reshaped/Figure 16 cumulative mass balance decades.csv')
df_17 = pd.read_csv('data/data_reshaped/Figure 17 - Sea ice seasonal extremes year.csv')


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
###################################
# Start the game
@callback(
    Output('page-content', 'children', allow_duplicate=True),
    [Input('start-button', 'n_clicks'),
    Input('url', 'pathname')],
    prevent_initial_call=True
)
def start_game(n_clicks_start, pathname):
    if n_clicks_start > 0:
        return page_question.layout
    else: 
        return page_start.layout
###################################

    
###################################
# Answer the question
@callback(
    [Output(f'button_R_{i}', 'className') for i in range(len(questions[question_number]['options']))] +
    [Output(f'button_R_{i}' , 'n_clicks') for i in range(len(questions[question_number]['options']))] +
    [Output('answer-button', 'style'),
    Output('responded_answered', 'data')],
    [Input(f'button_R_{i}' , 'n_clicks') for i in range(len(questions[question_number]['options']))],
    prevent_initial_call=True
)
def answer_question(*button_clicks):
    # initiate Display|Hide the answer button
    answer_button = {'display': 'none'}
    ctx = dash.callback_context
    print("ctx.triggered_id :" + str(ctx.triggered_id))
    if not ctx.triggered_id:
        raise PreventUpdate
    clicked_button_id = ctx.triggered_id.split('_')[-1]
    print("You clicked on the button : " + str(clicked_button_id))

    button_styles = ["reponse"] * len(questions[question_number]['options'])
    button_clicks_list = list(button_clicks)

    for i, clicks in enumerate(button_clicks_list):
        if clicks > 0:
            answer_button = None
            button_styles[i] = "reponse_click"
            button_clicks_list[i] = 0
        print(f"style de la rep {i} : " + button_styles[i])



        
    return tuple(button_styles + button_clicks_list + [answer_button, clicked_button_id])

###################################



'''
###################################
# click on check 
@callback(
    [Output('score', 'data'),
    Output('next-button', 'style', allow_duplicate=True)],
    [Input('answer-button', 'n_clicks'),
    Input('good_responds', 'data'),
    Input('responded_answered', 'data'),
    Input('score', 'data')],
    prevent_initial_call=True
)
def good_answer(n_clicks_answer, good_responds, responded_answered, score):
    print(good_responds)
    print(responded_answered)
    if n_clicks_answer > 0 :
        return score+1 , None
    else: 
        return score, {'display': 'none'}

#| good_responds==responded_answered
###################################
'''











###################################
#TODOOOOOOOO
###################################
@callback(
    [Output('q_number', 'data'),
    Output('explaina_of_quest', 'children'),
    Output('graph_box', 'children'),
    Output('question', 'children'),
    Output('answer', 'children'),
    Output('score_display', 'children'),
    Output('next-button', 'style', allow_duplicate=True),
    Output('answer-button', 'style', allow_duplicate=True)],
    [Input('next-button', 'n_clicks'),
    Input('q_number', 'data'),
    Input('score', 'data')],
    prevent_initial_call=True
)
def next_question(n_clicks_next, q_number, score):
    
    if n_clicks_next > 0 | q_number<len(page_question.quest_page_list):
        q_number+= 1
        
    #elif n_clicks_next > 0 | q_number==len(page_question.quest_page_list):

    return (q_number,
            questions[q_number]['text'], 
            page_question.quest_page_list[q_number], 
            [html.P(questions[q_number]['question'])],
            page_question.layout_answers[q_number],
            (str(score) + '/' + str(len(questions))),
            None,
            None)

#    if (q_number<len(questions) & q_number<len(page_question.quest_page_list)):




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
# dropdown callbacks
###################################


#layout question 1
@callback(
    Output('graph', 'figure'),
    Input('dropdown1_1', 'value'),
)
def update_graph(value):
    dff = df_1_2_3[df_1_2_3["gas"]==value]
    return px.bar(dff, x='Decade', y='averaged mole fraction')

    
#layout question 2
@callback(
    Output('graph', 'figure', allow_duplicate=True),
    [Input('dropdown2_1', 'value')],
    prevent_initial_call=True
)
def update_graph(region):
    dff = df_8[df_8["region"]==region]
    return px.bar(dff, x='Decade', y='value')


#layout question 3
@callback(
    Output('graph', 'figure', allow_duplicate=True),
    Input('dropdown3_1', 'value'),
    prevent_initial_call=True
)
def update_graph(depth):
    dff = df_9[(df_9["depth"]==depth)]
    return px.bar(dff, x='Decades', y='value')


#layout question 6
@callback(
    Output('graph', 'figure', allow_duplicate=True),
    Input('dropdown6_1', 'value'),
    prevent_initial_call=True
)
def update_graph(region):
    dff = df_16[(df_16["Greenland/Antartica"]==region)]
    return px.bar(dff, x='Decades', y='Cumulative mass balance (Gt)')


#layout question 7
@callback(
    Output('graph', 'figure', allow_duplicate=True),
    Input('dropdown7_1', 'value'),
    Input('dropdown7_2', 'value'),
    prevent_initial_call=True
)
def update_graph(north_south, max_min):
    dff = df_17[(df_17["S_N"]==north_south) & (df_17["max_min"]==max_min)]
    return px.line(dff, x='Date', y='value')




## If app.layout.getbyid(id='page-content').children ==
    
###str(value_score) + '/' + str(len(questions))
    
## if cli sur next 



## if click sur finish 


## finish page 

if __name__ == '__main__':
    app.run(debug=True)