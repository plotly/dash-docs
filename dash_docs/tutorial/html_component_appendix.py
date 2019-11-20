import dash_core_components as dcc
import dash_html_components as html
from dash_docs import reusable_components

layout = html.Div([
    html.Div(style={'marginTop': '60px'}),

    html.H2('Appendix - Common HTML Components'),

    html.Hr(),

    reusable_components.Markdown('html.H1("H1 Element")', style={'borderLeft': 'thin solid lightgrey'}),
    html.H1('H1 Element'),

    html.Hr(),

    reusable_components.Markdown('html.H2("H2 Element")', style={'borderLeft': 'thin solid lightgrey'}),
    html.H2('H2 Element'),

    html.Hr(),

    reusable_components.Markdown('html.H3("H3 Element")', style={'borderLeft': 'thin solid lightgrey'}),
    html.H3('H3 Element'),

    html.Hr(),

    reusable_components.Markdown('html.H4("H4 Element")', style={'borderLeft': 'thin solid lightgrey'}),
    html.H4('H4 Element'),

    html.Hr(),

    reusable_components.Markdown('html.H5("H5 Element")', style={'borderLeft': 'thin solid lightgrey'}),
    html.H5('H5 Element'),

    html.Hr(),

    reusable_components.Markdown('html.H6("H6 Element")', style={'borderLeft': 'thin solid lightgrey'}),
    html.H6('H6 Element'),

    html.Hr(),

    reusable_components.Markdown('html.Div("Generic Div Element")', style={'borderLeft': 'thin solid lightgrey'}),
    html.Div('Generic Div Element')
])
