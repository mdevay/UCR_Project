import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

if __name__ == '__main__':
    app
