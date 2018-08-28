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
from textwrap import dedent as s

import tools
from utils.component_block import ComponentBlock

from server import app

examples = {
    'button': tools.load_example('tutorial/examples/core_components/button.py'),
    'tabs': tools.load_example('tutorial/examples/core_components/tabs_callback.py')
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
    html.H3(dcc.Link('Dropdown', href='/dash-core-components/dropdown')),
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
             href="/dash-core-components/dropdown"),

    html.Hr(),

    html.H3(dcc.Link('Slider', href='/dash-core-components/slider')),
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
             href="/dash-core-components/slider"),

    html.Hr(),

    html.H3(dcc.Link('RangeSlider', href='/dash-core-components/rangeslider')),
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
             href="/dash-core-components/rangeslider"),

    html.Hr(),

    html.H3(dcc.Link('Input', href='/dash-core-components/input')),
    ComponentBlock('''import dash_core_components as dcc

dcc.Input(
    placeholder='Enter a value...',
    type='text',
    value=''
)''', language='python', customStyle=styles.code_container),
    html.Br(),
    dcc.Link(html.A('Input Reference'),
             href="/dash-core-components/input"),

    html.Hr(),

    html.H3(dcc.Link('Textarea', href='/dash-core-components/textarea')),
    ComponentBlock('''import dash_core_components as dcc

dcc.Textarea(
    placeholder='Enter a value...',
    value='This is a TextArea component',
    style={'width': '100%'}
)''', language='python', customStyle=styles.code_container),

    html.Br(),
    html.Br(),
    dcc.Link(html.A('Textarea Reference'),
             href="/dash-core-components/textarea"),

    html.Hr(),

    html.H3(dcc.Link('Checkboxes', href='/dash-core-components/checklist')),
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
             href="/dash-core-components/checklist"),
    html.Hr(),
    html.H3(dcc.Link('Radio Items', href='/dash-core-components/radioitems')),
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
             href="/dash-core-components/radioitems"),

    html.Hr(),

    html.H3("Button"),
    dcc.SyntaxHighlighter(
        examples['button'][0],
        customStyle=styles.code_container, language='python'
    ),
    html.Div(examples['button'][1], className='example-container'),

    html.P([
        '''For more on `dash.dependencies.State`, see the tutorial on ''',
        dcc.Link('Dash State', href='/state'),
        '.'
    ]),

    html.Hr(),

    html.H3(dcc.Link('DatePickerSingle', href='/dash-core-components/datepickersingle')),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt(1997, 5, 10)
)
''', language='python', customStyle=styles.code_container),
    dcc.Link(html.A('More DatePickerSingle Examples and Reference'),
             href="/dash-core-components/datepickersingle"),
    html.Hr(),

    html.H3(dcc.Link('DatePickerRange', href='/dash-core-components/datepickerrange')),
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
             href="/dash-core-components/datepickerrange"),

    html.Hr(),

    html.H3(dcc.Link('Markdown', href='/dash-core-components/markdown')),
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
             href="/dash-core-components/markdown"),

    html.Hr(),

    html.H3('Interactive Tables'),
    dcc.Markdown('''
    The `dash_html_components` library exposes all of the HTML tags.
    This includes the `Table`, `Tr`, and `Tbody` tags that can be used
    to create an HTML table. See
    [Create Your First Dash App, Part 1](/getting-started-part-1)
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

    html.H3(dcc.Link('Upload Component', href='/dash-core-components/upload')),
    dcc.Markdown('''

    The `dcc.Upload` component allows users to upload files into your app
    through drag-and-drop or the system's native file explorer.
    '''.replace('    ', '')),

    html.A(
        className="image-link",
        href="https://github.com/plotly/dash-core-components/pull/73",
        children=html.Img(
            src="https://user-images.githubusercontent.com/1280389/30351245-6b93ee62-97e8-11e7-8e85-0411e9d6c98c.gif",
            alt="Dash Upload Component"
        )
    ),

    dcc.Link(html.A('More Upload Examples and Reference'),
             href="/dash-core-components/upload"),

    dcc.Markdown('''
    ***
    '''.replace('    ', '')),

    html.H3('Tabs'),
    dcc.Markdown(s('''
    The Tabs and Tab components can be used to create tabbed sections in your app.
    ''')),

    dcc.SyntaxHighlighter(
        examples['tabs'][0],
        customStyle=styles.code_container, language='python'
    ),

    html.Div(examples['tabs'][1], className='example-container'),

    dcc.Link('More Tabs Examples and Reference',
             href="/dash-core-components/tabs"),

    html.Hr(),

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
            go.Bar(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker=go.Marker(
                    color='rgb(55, 83, 109)'
                )
            ),
            go.Bar(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker=go.Marker(
                    color='rgb(26, 118, 255)'
                )
            )
        ],
        layout=go.Layout(
            title='US Export of Plastic Scrap',
            showlegend=True,
            legend=go.Legend(
                x=0,
                y=1.0
            ),
            margin=go.Margin(l=40, r=0, t=40, b=30)
        )
    ),
    style={'height': 300},
    id='my-graph'
)''', language='python', customStyle=styles.code_container),

    html.Br(),
    dcc.Markdown('View the [plotly.py docs](https://plot.ly/python).'),

    dcc.Markdown('***'),

    html.H3(dcc.Link('ConfirmDialog', href='/dash-core-components/confirm')),

    dcc.Markdown('''
The `dcc.ConfirmDialog` component send a dialog to the browser 
asking the user to confirm or cancel with a custom message.
    '''),

    ComponentBlock('''
import dash_core_components as dcc

confirm = dcc.ConfirmDialog(
    id='confirm',
    message='Danger danger! Are you sure you want to continue?'
)
    '''),

    html.Br(),

    dcc.Link('More ConfirmDialog Examples and Reference',
             href='/dash-core-components/confirm'),

    html.Br(),
    dcc.Markdown('***'),

    dcc.Markdown('There is also a `dcc.ConfirmDialogProvider`,'
                 ' it will automatically wrap a child component '
                 ' to send a `dcc.ConfirmDialog` when clicked.'),

    ComponentBlock('''
import dash_core_components as dcc
import dash_html_components as html

confirm = dcc.ConfirmDialogProvider(
    children=html.Button(
        'Click Me',
    ),
    id='danger-danger',
    message='Danger danger! Are you sure you want to continue?'
)
    '''),
    html.Br(),

    dcc.Link('More ConfirmDialogProvider Examples and Reference',
             href='/dash-core-components/confirm-provider'),

    html.Br(),

    html.Div(id='hidden', style={'display': 'none'})
])
