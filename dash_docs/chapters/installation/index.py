# -*- coding: utf-8 -*-
import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_daq

import plotly

from dash_docs import styles, tools
from dash_docs import reusable_components as rc

layout = html.Div([

    rc.Markdown('''
    # Dash Installation

    In your terminal, install several dash libraries.
    These libraries are under active development,
    so install and upgrade frequently. These docs are run
    using the versions listed below.
    Python 2 and 3 are supported.'''),

    rc.Markdown('''
    ```shell
    pip install dash=={}
    ```
    '''.format(
        dash.__version__,
        dash_daq.__version__
    ), style=styles.code_container),

    html.Hr(),

    rc.WorkspaceBlurb if not tools.is_in_dash_enterprise() else '',

    html.Div([
        'Ready? Now, let\'s ',
        dcc.Link('make your first Dash app', href=tools.relpath('/layout')),
        '.'
    ]),

])
