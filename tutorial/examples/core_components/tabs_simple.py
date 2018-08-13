# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    html.H1('Dash Tabs component demo', style={
            'textAlign': 'center', 'margin': '48px 0', 'fontFamily': 'system-ui'}),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Tab one', children=[
            html.Div([
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2],
                                'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5],
                             'type': 'bar', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Dash Data Visualization'
                        }
                    }
                )
            ])
        ]),
        dcc.Tab(label='Tab two', children=[
            html.Div([
                html.H1("This is the content in tab 2"),
                html.P("A graph here would be nice!")
            ])
        ]),
        dcc.Tab(label='Tab three', children=[
            html.Div([
                html.H1("This is the content in tab 3"),
            ])
        ]),
    ]
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)