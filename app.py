import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from datetime import datetime as dt

app = dash.Dash(__name__,
)

server = app.server

app.layout = html.Div([
html.Div([
            html.P("Welcome to the Stock Dash App!", className="start"),
            html.Br(),
            html.Div([
              html.P("Input Stock Code", className="start1"),
              dcc.Input(id="input1", placeholder="Type something...", type="text",className="inp"),
              html.Button('Submit', id='submit-val', n_clicks=0,className="inputs1")
            ]),
            html.Div([]),
            html.Div([

              html.Br(),
              html.Button('Stock price ', id='input2', n_clicks=0,className="inputs"),
              html.Button('Indicators ', id='input3', n_clicks=0,className="inputs"),
              html.Br(),
              html.Br(),
              dcc.DatePickerRange(
                month_format='MMM Do, YY',
                end_date_placeholder_text='MMM Do, YY',
                start_date=dt(2017, 6, 21)),
               html.Br(),
               html.Br(),  
              dcc.Input(id="input", placeholder="No of days to forecast...", type="text",className="inp"),
              html.Button('Forecast ', id='stb2', n_clicks=0,className="inputs")

              # Stock price button
              # Indicators button
              # Number of days of forecast input
              # Forecast button
              ]),
          ],
        className="nav")
,
html.Div(
          [
            html.Div(
                  [  # Logo
                    # Company Name
                  ],
                className="header"),
            html.Div( #Description
              id="description", className="decription_ticker"),
            html.Div([
                # Stock price plot
            ], id="graphs-content"),
            html.Div([
                # Indicator plot
            ], id="main-content"),
            html.Div([
                # Forecast plot
            ], id="forecast-content")
          ],
        className="content")
])

if __name__ == '__main__':
    app.run_server(debug=True)