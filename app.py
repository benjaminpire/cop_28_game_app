from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import json
import dash

app = Dash(__name__, suppress_callback_exceptions=True)


# Import the diferent pages 
from pages import page_start
from pages import page_question
from pages import page_end


# get the question 
with open('questions.json', 'r') as file:
    questions = json.load(file)

#########
#demain tu fais un csv avec url de pages, question exct....
#########

# Define the app layout as HTML and css
app.layout = html.Div([
    dcc.Location(id='url',pathname = "/page_start", refresh=True),
    html.Div(id='page-content', children = page_start.layout),
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


if __name__ == '__main__':
    app.run(debug=True)
