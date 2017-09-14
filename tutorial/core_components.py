# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event
from pandas_datareader import data as web
import core_component_examples as examples
from datetime import datetime as dt
import plotly.graph_objs as go
import json
import styles

import tools
from utils.component_block import ComponentBlock

from server import app

examples = {
    'button': tools.load_example('tutorial/examples/core_components/button.py')
}


layout = html.Div(className="gallery", children=[
    html.H1('Dash Core Components'),

    dcc.Markdown('''
        Dash ships with supercharged components for interactive user interfaces.
        A core set of components, written and maintained by the Dash team,
        is available in the `dash-core-components` library.

        The source is on GitHub at [plotly/dash-core-components](https://github.com/plotly/dash-core-components).

        These docs are using version {}.
    '''.replace('    ', '').format(dcc.__version__)),

    dcc.SyntaxHighlighter('''>>> import dash_core_components as dcc
    >>> print(dcc.__version__)
    {}'''.replace('    ', '').format(dcc.__version__),
    customStyle=styles.code_container),

    html.Hr(),
    html.H3('Dropdown'),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)''', language='python', customStyle=styles.code_container),

    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    multi=True,
    value="MTL"
)''', language='python', customStyle=styles.code_container),
    html.Br(),
    dcc.Link(html.A('More Dropdown Examples and Reference'),
             href="/dash/dash-core-components/dropdown"),

    html.Hr(),

    html.H3('Slider'),
    ComponentBlock('''import dash_core_components as dcc

dcc.Slider(
    min=-5,
    max=10,
    step=0.5,
    value=-3,
)''', language='python', customStyle=styles.code_container),

    ComponentBlock('''import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=9,
    marks={i: 'Label {}'.format(i) for i in range(10)},
    value=5,
)''', language='python', customStyle=styles.code_container),
    html.Br(),
    dcc.Link(html.A('More Slider Examples and Reference'),
             href="/dash/dash-core-components/slider"),

    html.Hr(),

    html.H3('RangeSlider'),
    ComponentBlock('''import dash_core_components as dcc

dcc.RangeSlider(
    count=1,
    min=-5,
    max=10,
    step=0.5,
    value=[-3, 7]
)''', language='python', customStyle=styles.code_container),

    ComponentBlock('''import dash_core_components as dcc

dcc.RangeSlider(
    marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
    min=-5,
    max=6,
    value=[-3, 4]
)''', language='python', customStyle=styles.code_container),
    html.Br(),
    dcc.Link(html.A('More RangeSlider Examples and Reference'),
             href="/dash/dash-core-components/rangeslider"),

    html.Hr(),

    html.H3('Input'),
    ComponentBlock('''import dash_core_components as dcc

dcc.Input(
    placeholder='Enter a value...',
    type='text',
    value=''
)''', language='python', customStyle=styles.code_container),
    html.Br(),
    dcc.Link(html.A('Input Reference'),
             href="/dash/dash-core-components/input"),

    html.Hr(),

    html.H3('Textarea'),
    ComponentBlock('''import dash_core_components as dcc

dcc.Textarea(
    placeholder='Enter a value...',
    value='This is a TextArea component',
    style={'width': '100%'}
)''', language='python', customStyle=styles.code_container),

    html.Br(),
    html.Br(),
    dcc.Link(html.A('Textarea Reference'),
             href="/dash/dash-core-components/textarea"),

    html.Hr(),

    html.H3('Checkboxes'),
    ComponentBlock('''import dash_core_components as dcc

dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF']
)''', language='python', customStyle=styles.code_container),

    ComponentBlock('''import dash_core_components as dcc

dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF'],
    labelStyle={'display': 'inline-block'}
)''', language='python', customStyle=styles.code_container),

    html.Br(),
    dcc.Link(html.A('Checklist Properties'),
             href="/dash/dash-core-components/checklist"),
    html.Hr(),
    html.H3('Radio Items'),
    ComponentBlock('''import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)''', language='python', customStyle=styles.code_container),

    ComponentBlock('''import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL',
    labelStyle={'display': 'inline-block'}
)''', language='python', customStyle=styles.code_container),
    html.Br(),
    dcc.Link(html.A('RadioItems Reference'),
             href="/dash/dash-core-components/radioitems"),

    html.Hr(),

    html.H3("Button"),
    dcc.SyntaxHighlighter(
        examples['button'][0],
        customStyle=styles.code_container, language='python'
    ),
    html.Div(examples['button'][1], className='example-container'),

    html.Hr(),

    html.H3('DatePickerSingle'),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt(1997, 5, 10)
)
''', language='python', customStyle=styles.code_container),
    dcc.Link(html.A('More DatePickerSingle Examples and Reference'),
             href="/dash/dash-core-components/datepickersingle"),
    html.Hr(),

    html.H3('DatePickerRange'),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    id='date-picker-range',
    start_date=dt(1997, 5, 3),
    end_date_placeholder_text='Select a date!'
)
''', language='python', customStyle=styles.code_container),
    html.Br(),
    dcc.Link(html.A('More DatePickerRange Examples and Reference'),
             href="/dash/dash-core-components/datepickerrange"),

    html.Hr(),

    html.H3('Markdown'),
    ComponentBlock('''import dash_core_components as dcc

    dcc.Markdown(\'\'\'
    #### Dash and Markdown

    Dash supports [Markdown](http://commonmark.org/help).

    Markdown is a simple way to write and format text.
    It includes a syntax for things like **bold text** and *italics*,
    [links](http://commonmark.org/help), inline `code` snippets, lists,
    quotes, and more.
    \'\'\')
    '''.replace('  ', ''),
        customStyle=styles.code_container,
        language='python'
    ),

    html.Br(),
    dcc.Link(html.A('More Markdown Examples and Reference'),
             href="/dash/dash-core-components/markdown"),

    html.Hr(),

    html.H3('Interactive Tables'),
    dcc.Markdown('''
    The `dash_html_components` library exposes all of the HTML tags.
    This includes the `Table`, `Tr`, and `Tbody` tags that can be used
    to create an HTML table. See
    [Create Your First Dash App, Part 1](https://plot.ly/dash/getting-started-part-1)
    for an example.

    Dash is currently incubating an interactive table component that provides
    built-in filtering, row-selection, editing, and sorting.
    Prototypes of this component are being developed in the
    [`dash-table-experiments`](https://github.com/plotly/dash-table-experiments)
    repository. Join the discussion in the
    [Dash Community Forum](https://community.plot.ly/t/display-tables-in-dash/4707/38).

    '''.replace('    ', '')),

    html.A(
        className="image-link",
        href="https://github.com/plotly/dash-table-experiments",
        children=html.Img(
            src="https://github.com/plotly/dash-table-experiments/raw/master/images/DataTable.gif",
            alt="Example of a Dash Interactive Table"
        )
    ),


    dcc.Markdown('''
    [View the Dash Table Experiments Project](https://github.com/plotly/dash-table-experiments) | [Join the discussion](https://community.plot.ly/t/display-tables-in-dash/4707/38)

    ***
    '''.replace('    ', '')),

    html.H3('Upload Component'),
    dcc.Markdown('''

    The `dcc.Upload` component is currently available in the prerelease
    channel of the `dash-core-components` package. The prerelease channel is
    used to solicit feedback from the community before releasing on the
    long-term support stable channel.
    To try it out, see the upload component
    [Pull Request on GitHub](https://github.com/plotly/dash-core-components/pull/73).
    '''.replace('    ', '')),

    html.A(
        className="image-link",
        href="https://github.com/plotly/dash-core-components/pull/73",
        children=html.Img(
            src="https://user-images.githubusercontent.com/1280389/30351245-6b93ee62-97e8-11e7-8e85-0411e9d6c98c.gif",
            alt="Dash Upload Component"
        )
    ),

    dcc.Markdown('''
    [Upload Component Pre-Release](https://github.com/plotly/dash-core-components/pull/73)

    ***
    '''.replace('    ', '')),

    html.H3('Graphs'),
    dcc.Markdown('''
    The `Graph` component shares the same syntax as the open-source
    `plotly.py` library. View the [plotly.py docs](https://plot.ly/python)
    to learn more.
    '''.replace('    ', '')),
    ComponentBlock('''import dash_core_components as dcc
import plotly.graph_objs as go

dcc.Graph(
    figure=go.Figure(
        data=[
            go.Scatter(x=[1, 2, 3], y=[3, 2, 4], mode='lines'),
            go.Scatter(x=[1, 2, 3], y=[4, 1, 5], mode='lines')
        ],
        layout=go.Layout(
            title='Quarterly Results',
            showlegend=False,
            margin=go.Margin(l=20, r=0, t=40, b=20)
        )
    ),
    style={'height': 300},
    id='my-graph'
)''', language='python', customStyle=styles.code_container),

    html.Br(),
    dcc.Markdown('View the [plotly.py docs](https://plot.ly/python).'),

    html.Div(id='hidden', style={'display': 'none'})
])
