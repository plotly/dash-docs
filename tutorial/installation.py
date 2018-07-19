# -*- coding: utf-8 -*-
import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html

import plotly

import styles

layout = html.Div([

    dcc.Markdown('''
    # Dash Installation

    In your terminal, install several dash libraries.
    These libraries are under active development,
    so install and upgrade frequently.
    Python 2 and 3 are supported.'''.replace('    ', '')),

    dcc.SyntaxHighlighter('''pip install dash=={}  # The core dash backend
        pip install dash-renderer=={}  # The dash front-end
        pip install dash-html-components=={}  # HTML components
        pip install dash-core-components=={}  # Supercharged components
        pip install plotly --upgrade  # Plotly graphing library used in examples
    '''.replace('    ', '').format(
        dash.__version__,
        dash_renderer.__version__,
        html.__version__,
        dcc.__version__,
        plotly.__version__
    ), customStyle=styles.code_container),

    html.Div([
        'Ready? Now, let\'s ',
        dcc.Link('make your first Dash app', href='/getting-started'),
        '.'
    ])

])
