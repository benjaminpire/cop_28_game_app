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
from pages import page_select_report
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
with open('assets/json/questions_state_clim_dec_report.json', 'r') as file:
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
###################################
# Game process callbacks
###################################
## Start the game
###################################
@callback(
    Output('page-content', 'children', allow_duplicate=True),
    [Input('start_button', 'n_clicks'),
    Input('url', 'pathname')],
    prevent_initial_call=True
)
def start_game(n_clicks_start, pathname):
    if n_clicks_start > 0:
        print("/n")
        print("###########")
        print("Start Game")
        print("###########")
        return page_select_report.layout
    else: 
        return page_start.layout
###################################
## Select the report
###################################
@callback(
    Output('select_button', 'style', allow_duplicate=True),
    [Input('decadal_version', 'n_clicks')],
    prevent_initial_call=True
)
def select_version(n_clicks_version):
    if n_clicks_version > 0:
        return None
    else: 
        return {'display': 'none'}
###################################
## Validation of the selected report
###################################
@callback(
    Output('page-content', 'children', allow_duplicate=True),
    [Input('select_button', 'n_clicks'),
    Input('url', 'pathname')],
    prevent_initial_call=True
)
def validate_version(n_clicks_select, pathname):
    if n_clicks_select > 0:
        print("###########")
        print("###########")
        print("###########")
        print("Play the Game")
        print("###########")
        print("###########")
        print("###########")
        return page_question.layout
    else: 
        return page_select_report.layout
###################################


    
###################################
## Answer the question
###################################
@callback(
    [Output(f'button_R_{i}', 'className') for i in range(len(questions[question_number]['options']))] +
    [Output(f'button_R_{i}' , 'n_clicks') for i in range(len(questions[question_number]['options']))] +
    [Output('answer_button', 'style'),
    Output('responded_answered', 'data')],
    [Input(f'button_R_{i}' , 'n_clicks') for i in range(len(questions[question_number]['options']))],
    prevent_initial_call=True
)
def answer_question(*button_clicks):
    # initiate Display|Hide the answer button
    answer_button = {'display': 'none'}
    ctx = dash.callback_context
    if not ctx.triggered_id:
        raise PreventUpdate
    clicked_button_id = int(ctx.triggered_id.split('_')[-1])
    print("###########")
    print("You clicked on the button : " + str(clicked_button_id))
    print("###########")

    button_styles = ["reponse"] * len(questions[question_number]['options'])
    button_clicks_list = list(button_clicks)

    for i, clicks in enumerate(button_clicks_list):
        if clicks > 0:
            answer_button = None
            button_styles[i] = "reponse_click"
            button_clicks_list[i] = 0
    return tuple(button_styles + button_clicks_list + [answer_button, clicked_button_id])

###################################
## click on check and check the answer
###################################
@callback(
    [Output('score_display', 'data'),
    Output('next_button', 'style', allow_duplicate=True),
    Output('success_message', 'style'),
    Output('success_message', 'children'),
    Output('answer_button', 'n_clicks')],
    [Input('answer_button', 'n_clicks'),
    Input('responded_answered', 'data'),
    Input('score', 'data')],
    prevent_initial_call=True
)
def good_answer(n_clicks_check, responded_answered, score):
    print("You answered : " + str(responded_answered))
    print("The correct answer : " + str(questions[question_number]['answer']))
    if (n_clicks_check > 0) & (responded_answered == questions[question_number]['answer']) :
        n_clicks_check = 0
        return score+1 , None, {'color': 'green'}, 'Success !!', n_clicks_check
    elif (n_clicks_check > 0) & (responded_answered != questions[question_number]['answer']): 
        n_clicks_check = 0
        return score, {'display': 'none'}, {'color': 'red'}, 'Fail !!', n_clicks_check
    else :
        n_clicks_check = 0
        return score, {'display': 'none'}, {'display': 'none'}, None, n_clicks_check

###################################
## Click on next to go to the next question
###################################
@callback(
    [Output('q_number', 'data'),
    Output('explaina_of_quest', 'children'),
    Output('graph_box', 'children'),
    Output('question', 'children'),
    Output('answer', 'children'),
    Output('score_display', 'children'),
    Output('next_button', 'style', allow_duplicate=True),
    Output('answer_button', 'style', allow_duplicate=True)],
    [Input('next_button', 'n_clicks'),
    Input('q_number', 'data'),
    Input('score', 'data')],
    prevent_initial_call=True
)
def next_question(n_clicks_next, q_number, score):
    
    if n_clicks_next > 0 | q_number<len(page_question.quest_page_list):
        q_number+= 1
        question_number=q_number
        print("###########")
        print("Next Question")
        print("###########")
        print("You are at the question : " + str(q_number+1))
        return (q_number,
                questions[q_number]['text'], 
                page_question.quest_page_list[q_number], 
                [html.P(questions[q_number]['question'])],
                page_question.layout_answers[q_number],
                (str(score) + '/' + str(len(questions))),
                {'display': 'none'},
                {'display': 'none'})
        
    elif n_clicks_next > 0 | q_number==len(page_question.quest_page_list):
        return (q_number,
                questions[q_number]['text'], 
                page_question.quest_page_list[q_number], 
                [html.P(questions[q_number]['question'])],
                page_question.layout_answers[q_number],
                (str(score) + '/' + str(len(questions))),
                None,
                None)
    else :
        return (q_number,
                questions[q_number]['text'], 
                page_question.quest_page_list[q_number], 
                [html.P(questions[q_number]['question'])],
                page_question.layout_answers[q_number],
                (str(score) + '/' + str(len(questions))),
                None,
                None)



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