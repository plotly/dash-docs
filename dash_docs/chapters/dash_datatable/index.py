import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash_docs.reusable_components import Section, Chapter
from dash_docs import styles
from dash_docs import tools
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)

preamble = html.Div([

    rc.Markdown('''
    # Dash DataTable

    '''),

    html.Iframe(
        src="https://ghbtns.com/github-btn.html?user=plotly&repo=dash-table&type=star&count=true&size=large",
        width="160px",
        height="30px",
        style={'border': 'none'}
    ),

    rc.Markdown('''
    #### Dash DataTable is an interactive table component designed for
    #### viewing, editing, and exploring large datasets.

    This component was written from scratch in React.js specifically
    for the Dash community. Its API was designed to be ergonomic
    and its behavior is completely customizable through its properties.
    DataTable is rendered with standard, semantic HTML `<table/>` markup,
    which makes it accessible, responsive, and easy to style.

    For production Dash applications, DataTable is intended to bse used with
    [Python data pipelines](https://plotly.com/dash/job-queue/) for ingesting
    the table data and [Design Kit](https://plotly.com/dash/design-kit) for
    DataTable styling.
    '''),

    Section('Quickstart', [
        rc.Markdown(
            '''
            ```shell
            pip install dash=={}
            ```
            '''.format(dash.__version__),
            style=styles.code_container
        ),

        rc.Markdown(
            examples['simple.py'][0],
            style=styles.code_container
        ),

        html.Div(examples['simple.py'][1], className='example-container'),

    ]),

    Section('User Guide', []),
])
