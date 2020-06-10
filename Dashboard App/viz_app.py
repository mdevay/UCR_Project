# This is the script to run the dashboard app

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import tab_1, tab_2


# now lets start working on the dash server

app.config['suppress_callback_exceptions'] = True

app.title="Visualization of the FBI Uniform Crime Reporting Data"

colors = {
    'background' : "#fffafa",
    'text_1' : "#191970",
    'text_2' : "#202030"
}

app.layout=html.Div(style={'backgroundColor' : colors['background']},
    children=[

        html.Div(id='header',
            children = [
            html.Br(),
            html.H1(
                children = "Dashboard - FBI Uniform Crime Reporting Data",
                style={
                    'textAlign' : 'center',
                    'color' : colors['text_1']
                }
            ),

            html.H4(
                children = "An Exploration of the Effects of Cannabis Policy on Crime Rates",
                style={
                    'textAlign' : 'center',
                    'color' : colors['text_2']
                }
            ),
            html.H6(
                children = "by: Matthew DeVay",
                style={
                    'textAlign' : 'center'
                }
            ),
            html.Br(),
            ]
        ),

        dcc.Tabs(id='tabs', value='tab_1', children=[
            dcc.Tab(label='Map', value='tab_1'),
            dcc.Tab(label='Time Series', value='tab_2'),
            dcc.Tab(label='Other Graphs', value='tab_3')
        ]),

        html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])

def render_content(tab):
    if tab == 'tab_1':
        return tab_1.layout

    elif tab == 'tab_2':
        return tab_2.layout
    elif tab == 'tab_3':
        return html.Div([
            html.H3('Tab content 3')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
