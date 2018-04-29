from datetime import datetime as dt

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from pandas_datareader import data as web

app = dash.Dash('')

# Describe the layout of the app
app.layout = html.Div([
    dcc.Dropdown(
        id='section3-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='section3-graph')
])

# Bind a function to a dash app with dash's "callback" decorator
# This "callback" decorator describes how input components should
# update output components.
#
# The first argument is an object that describes the component
# containing the ID  of the output component ("section3-graph")
# and the particular property of that component that this function
#  should update ("figure").
#
# The second argument is a list of Input components. Similarly,
# the first argument is the ID of the component ("section3-dropdown")
# and the second argument is property of the input component ("value").
#
# Whenever the "value" property changes in the application, for example
# when you select a new dropdown item, this function will get called
# with that value. Dash expects that this function will return an
# object that will update whatever output component that you subscribed to,
# in this case a "figure" object.
@app.callback(
    Output('section3-graph', 'figure'),
    [Input('section3-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    # Get some new data from Google finance with Pandas
    df = web.DataReader(
        selected_dropdown_value, 'google',
        dt(2017, 1, 1), dt.now()
    )

    # Construct a figure and return it to dash's front-end
    # This will end up updating the Graph's `figure` property
    # in the front-end of the application.
    return go.Figure(
        data=[{
            'x': df.index,
            'y': df.Close
        }],
        layout={'margin': {'l': 30, 'r': 0, 'b': 20, 't': 10}}
    )


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
