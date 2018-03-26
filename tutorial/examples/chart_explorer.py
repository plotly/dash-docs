from collections import OrderedDict

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py

graphs = OrderedDict([
    ['scatter', {
        'figure': py.get_figure(),
        'label': 'Scatter'
    ],
    ['bar', {
        'figure': py.get_figure(),
        'label': 'Bar'
    }],
    ['surface': {
        'figure': py.get_figure(),
        'label': 'Surface'
    }],
    ['multiple-axes': {
        'figure':
        'label':
    }],
    ['error-bars': {
        'figure': py.get_figure('https://plot.ly/~chriddyp/674'),
        'label': 'Error Bars'
    }]
])

html.Div([
    dcc.RadioItems()
])
