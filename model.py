import yfinance as yf

import pandas as pd

import plotly.graph_objs as go

import plotly.express as px

@app.callback([
    Output("component-id-1", "property"),
    Output(# Output of component-id-2),
    ],
  [Input(# Input of component-id-2)],
  [State("component-id-4", "property")])
def update_data(arg1, arg2):  # input parameter(s)
    # your function here
    return output1, output2

ticker = yf.Ticker(val)
inf = ticker.info
df = pd.DataFrame().from_dict(inf, orient="index").T
return # df's first element of 'longBusinessSummary', df's first element value of 'logo_url', df's first element value of 'shortName'

df = yf.download(# input parameter, start_date str, end_date str )
df.reset_index(inplace=True)
fig = get_stock_price_fig(df)
return # plot the graph of fig using DCC function

def get_stock_price_fig(df):
    fig = px.line(df,
                  x= # Date str,
                  y= # list of 'Open' and 'Close',
                  title="Closing and Opening Price vs Date")
    return fig

def get_more(df):
    df['EWA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    fig = px.scatter(df,
                    x= # Date str,
                    y= # EWA_20 str,
                    title="Exponential Moving Average vs Date")

    fig.update_traces(mode= # appropriate mode)
    
    return fig