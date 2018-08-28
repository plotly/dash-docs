# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.graph_objs as go
import json

from server import app
import styles
import tools

examples = [
    tools.load_example(s) for s in [
        'tutorial/examples/dynamic_content.py'
    ]
]


layout = html.Div(children=[
    dcc.Markdown('''
    ## Loading Content Dynamically

    Dash callbacks can return any type of property.
    By returning `children`, they can even dynamically
    render their content.

    This is an example that can be used in app development for
    quicker feedback.
    Instead of refreshing the page to view your layout,
    just render the layout as a response to clicking on a button.
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter(
        examples[0][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Div(examples[0][1], className="example-container")

])
