# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Button('Button 1', id='btn-nclicks-1', n_clicks_timestamp=0),
    html.Button('Button 2', id='btn-nclicks-2', n_clicks_timestamp=0),
    html.Button('Button 3', id='btn-nclicks-3', n_clicks_timestamp=0),
    html.Div(id='container-button-timestamp')
])

@app.callback(Output('container-button-timestamp', 'children'),
              [Input('btn-nclicks-1', 'n_clicks_timestamp'),
               Input('btn-nclicks-2', 'n_clicks_timestamp'),
               Input('btn-nclicks-3', 'n_clicks_timestamp')])
def displayClick(btn1, btn2, btn3):
    if int(btn1) > int(btn2) and int(btn1) > int(btn3):
        msg = 'Button 1 was most recently clicked'
    elif int(btn2) > int(btn1) and int(btn2) > int(btn3):
        msg = 'Button 2 was most recently clicked'
    elif int(btn3) > int(btn1) and int(btn3) > int(btn2):
        msg = 'Button 3 was most recently clicked'
    else:
        msg = 'None of the buttons have been clicked yet'
    return html.Div([
        html.Div('btn1: {}'.format(btn1)),
        html.Div('btn2: {}'.format(btn2)),
        html.Div('btn3: {}'.format(btn3)),
        html.Div(msg)
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
