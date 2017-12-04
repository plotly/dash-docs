# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-1', type='text', value='Montréal'),
    dcc.Input(id='input-2', type='text', value='Canada'),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'),
              [Input('input-1', 'value'),
               Input('input-2', 'value')])
def update_output(input1, input2):
    return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True)
