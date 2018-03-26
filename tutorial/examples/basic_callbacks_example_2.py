from datetime import datetime as dt

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandas_datareader import data as web
import plotly.graph_objs as go

app = dash.Dash('')

app.layout = html.Div([
    dcc.Dropdown(
        id='stock-ticker-dropdown-multiple-dropdowns',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Dropdown(
        id='column-selector-multiple-dropdowns',
        options=[
            {'label': i, 'value': i} for i in
            ['Open', 'High', 'Low', 'Close', 'High - Low']
        ],
        value='Open'
    ),

    dcc.Graph(id='graph-multiple-dropdowns')
])


@app.callback(
    Output('graph-multiple-dropdowns', 'figure'),
    [Input('stock-ticker-dropdown-multiple-dropdowns', 'value'),
     Input('column-selector-multiple-dropdowns', 'value')])
def update_graph(stock_ticker, column):
    # The order of the inputs in the callback
    # decorator match the order of the input
    # arguments of the function

    df = web.DataReader(
        stock_ticker, 'google',
        dt(2017, 1, 1), dt.now()
    )

    if column != 'High - Low':
        y = df[column]
    else:
        y = df.High - df.Low

    return go.Figure(
        data=[go.Scatter(x=df.index, y=y)],
        layout=go.Layout(
            yaxis=go.YAxis(title=column),
            margin=go.Margin(l=40, r=0, t=10, b=30)
        )
    )


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
