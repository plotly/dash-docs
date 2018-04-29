from datetime import datetime as dt

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import State, Event, Output
from pandas_datareader import data as web

app = dash.Dash('')

app.layout = html.Div([
    dcc.Dropdown(
        id='stock-ticker-dropdown-events-example',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Dropdown(
        id='column-selector-events-example',
        options=[
            {'label': i, 'value': i} for i in
            ['Open', 'High', 'Low', 'Close', 'High - Low']
        ],
        value='Open'
    ),

    html.Button('Update Graph', id='my-button-events-example'),

    dcc.Graph(id='graph-events-example')
])


@app.callback(
    Output('graph-events-example', 'figure'),
    events=[Event('my-button-events-example', 'click')],
    state=[State('stock-ticker-dropdown-events-example', 'value'),
           State('column-selector-events-example', 'value')])
def update_graph(stock_ticker, column):
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
            yaxis=go.YAxis(title=column)
        )
    )


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
