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


# csv 
df_1_2_3 = pd.read_csv('data/figure 1-2-3 GHG decadal analysis.csv')
df_8 = pd.read_csv('data/Figure 8-source data-National extremes by decade melted.csv')


# get the question 

with open('questions.json', 'r') as file:
    questions = json.load(file)
    

#########
#demain tu fais un csv avec url de pages, question exct....
#########

# Define the app layout as HTML and css
app.layout = html.Div([
    dcc.Location(id='url',pathname = "/page_start", refresh=True),
    html.Div(id='page-content', children = page_start.layout, className='general'),
])

@callback(
    Output('page-content', 'children'),
    [Input('start-button', 'n_clicks'),
    Input('url', 'pathname')],
)


def start_survey(n_clicks, pathname):
    if n_clicks > 0:
        return page_question.layout                
    else: 
        return page_start.layout

@callback(
    Output('graph', 'figure'),
    Input('dropdown', 'value')
)
def update_graph(value):
    dff = df_1_2_3[df_1_2_3["gas"]==value]
    return px.bar(dff, x='Decades', y='averaged mole fraction')
    
## If app.layout.getbyid(id='page-content').children ==
    
###str(value_score) + '/' + str(len(questions))
    
## if cli sur next 



## if click sur finish 


## finish page 

if __name__ == '__main__':
    app.run(debug=True)
