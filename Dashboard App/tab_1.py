import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from dash.dependencies import Input, Output
from app import app

import plotly.graph_objects as go

with open('data.pkl', "rb") as pickle_in:
    df = pickle.load(pickle_in)

with open('legal.pkl', "rb") as pickle_in:
    legal_df = pickle.load(pickle_in)

col_list = list(df.drop(columns=['state', 'st', 'population', "decrim", "medical", "recreational"]).columns)

col_list.sort()

crimes = [{'label':col, "value":col} for col in col_list]




app.config['suppress_callback_exceptions'] = True

layout = html.Div(
    id = "tab_1_content",
    children = [
        html.Div(
            children = [
            html.Br(),
            html.Label('Crime Category Selection'),
            dcc.Dropdown(
                id='crime_selector',
                options=crimes,
                value='Arson'
            ),
            html.Br(),
            html.Label('Year Selection'),
            dcc.Slider(
                id='year_selector',
                min = df.index.min(),
                max = df.index.max(),
                value = df.index.max(),
                marks = {str(year) : str(year) for year in df.index},
                step = 1
            )],
        style = {'columnCount' : 2}
        ),
        dcc.Graph(
            id = "map_1",
            style = {"height": 750}
        )

    ]
)
app.config['suppress_callback_exceptions'] = True


@app.callback(
    Output('map_1', 'figure'),
    [Input('crime_selector', 'value'),
     Input('year_selector', 'value')],
    )

def update_year(crime, year):
    data = df[df.index == year]
    data.index = range(len(data))
    data['text'] = data['state'].copy() + ", " + crime + ", " + data[crime].astype(str).copy() + " arrests for " + str(year)
    fig = go.Figure(
        data=go.Choropleth(
            locations=data['st'],
            z=data[crime] / data['population'] * 100000,
            locationmode='USA-states',
            colorscale='Blues',
            autocolorscale=False,
            text = data['text'],
            marker_line_color='white', # line markers between states
            colorbar_title="Arrests per 100,000 people"
        )
    )

    fig.update_layout(
        title_text=f"{year}, Arrest Rate for {crime}",
        geo = dict(
            scope='usa',
            projection=go.layout.geo.Projection(type = 'albers usa'),
            showlakes=True, # lakes
            lakecolor='rgb(255, 255, 255)'),
    )

    return fig
