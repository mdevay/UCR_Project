import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from dash.dependencies import Input, Output
from app import app
import plotly.io as pio

pio.renderers.default = 'browser'

import plotly.graph_objects as go

with open('data.pkl', "rb") as pickle_in:
    df = pickle.load(pickle_in)

with open('legal.pkl', "rb") as pickle_in:
    legal_df = pickle.load(pickle_in)

col_list = list(df.drop(columns=['state', 'st', 'population', "decrim", "medical", "recreational"]).columns)

df['total'] = df[col_list].apply(np.sum, axis=1)

col_list.append('total')
col_list.sort()

crimes = [{'label':col, "value":col} for col in col_list]

states = [{'label':state, "value":state} for state in legal_df['State']]

layout = html.Div(
    id = "tab_2_content",
    children = [
        html.Div(
            children = [
            html.Br(),
            html.Br(),
            html.Label('Crime Category Selection'),
            dcc.Dropdown(
                id='crime_sel',
                options=crimes,
                value='Arson',
                style = {'width' : "80%",
                         'verticalAlign' : "middle"},
                multi=True
            ),
            html.Br(),
            html.Label('State Selection'),
            dcc.Dropdown(
                id='state_sel',
                options = states,
                value='Texas',
                multi=True,
                style = {'width' : "80%",
                         'verticalAlign' : "middle"}
            )],
        style = {'columnCount' : 2,
                 'vertical-align' : "middle"}
        ),
        html.Br(),
        dcc.Graph(
            id = "graph_1",
            style = {"height": 750}
        ),
        html.Div(id='test')

    ]
)
app.config['suppress_callback_exceptions'] = True


@app.callback(
    Output('graph_1', 'figure'),
    [Input('crime_sel', 'value'),
     Input('state_sel', 'value')],
    )

def update_year(crimes, states):
    df['year'] = df.index.copy()
    crimes_list = []
    states_list = []
    if type(crimes) == str:
        crimes_list.append(crimes)
    else:
        crimes_list = crimes_list + list(crimes)
    if type(states) == str:
        states_list.append(states)
    else:
        states_list = states_list + list(states)
    traces = []
    for state in states_list:
        data = df[df['state'] == state]
        for crime in crimes_list:
            traces.append(
                go.Scatter(
                    x = data.index,
                    y = data[crime] / data['population'] * 100000,
                    mode="lines",
                    name = state + " - " + crime
                )
            )


    fig = go.Figure(data=traces)




    fig.update_layout(
        title_text=f"Per Capita Arrests for {crimes} in {states} ",
    )

    return fig
