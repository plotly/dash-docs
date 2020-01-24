# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash_docs import styles
from textwrap import dedent as s

from dash_docs import tools
from dash_docs.tutorial.utils.component_block import ComponentBlock
from dash_docs import reusable_components

examples = {
    'button': tools.load_example('tutorial/examples/core_components/button.py'),
    'tabs': tools.load_example('tutorial/examples/core_components/tabs_callback.py')
}


layout = html.Div(className="gallery", children=[
    html.H1('Dash Core Components'),

    reusable_components.Markdown('''
        Dash ships with supercharged components for interactive user interfaces.
        A core set of components, written and maintained by the Dash team,
        is available in the `dash-core-components` library.

        The source is on GitHub at [plotly/dash-core-components](https://github.com/plotly/dash-core-components).

        These docs are using version {}.
    '''.replace('    ', '').format(dcc.__version__)),

    reusable_components.Markdown('''
    ```py
    >>> import dash_core_components as dcc
    >>> print(dcc.__version__)
    {}
    ```
    '''.replace('    ', '').format(dcc.__version__),
    style=styles.code_container),

    html.Hr(),
    html.H3(dcc.Link('Dropdown', href=tools.relpath('/dash-core-components/dropdown'))),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)''', style=styles.code_container),

    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    multi=True,
    value="MTL"
)''', style=styles.code_container),
    html.Br(),
    dcc.Link('More Dropdown Examples and Reference',
             href=tools.relpath("/dash-core-components/dropdown")),

    html.Hr(),

    html.H3(dcc.Link('Slider', href=tools.relpath('/dash-core-components/slider'))),
    ComponentBlock('''import dash_core_components as dcc

dcc.Slider(
    min=-5,
    max=10,
    step=0.5,
    value=-3
)''', style=styles.code_container),

    ComponentBlock('''import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=9,
    marks={i: 'Label {}'.format(i) for i in range(10)},
    value=5,
)''', style=styles.code_container),
    html.Br(),
    dcc.Link('More Slider Examples and Reference',
             href=tools.relpath("/dash-core-components/slider")),

    html.Hr(),

    html.H3(dcc.Link('RangeSlider', href=tools.relpath('/dash-core-components/rangeslider'))),
    ComponentBlock('''import dash_core_components as dcc

dcc.RangeSlider(
    count=1,
    min=-5,
    max=10,
    step=0.5,
    value=[-3, 7]
)''', style=styles.code_container),

    ComponentBlock('''import dash_core_components as dcc

dcc.RangeSlider(
    marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
    min=-5,
    max=6,
    value=[-3, 4]
)''', style=styles.code_container),
    html.Br(),
    dcc.Link('More RangeSlider Examples and Reference',
             href=tools.relpath("/dash-core-components/rangeslider")),

    html.Hr(),

    html.H3(dcc.Link('Input', href=tools.relpath('/dash-core-components/input'))),
    ComponentBlock('''import dash_core_components as dcc

dcc.Input(
    placeholder='Enter a value...',
    type='text',
    value=''
)''', style=styles.code_container),
    html.Br(),
    dcc.Link('More Input Examples and Reference',
             href=tools.relpath("/dash-core-components/input")),

    html.Hr(),

    html.H3(dcc.Link('Textarea', href=tools.relpath('/dash-core-components/textarea'))),
    ComponentBlock('''import dash_core_components as dcc

dcc.Textarea(
    placeholder='Enter a value...',
    value='This is a TextArea component',
    style={'width': '100%'}
)''', style=styles.code_container),

    html.Br(),
    html.Br(),
    dcc.Link('Textarea Reference',
             href=tools.relpath("/dash-core-components/textarea")),

    html.Hr(),

    html.H3(dcc.Link('Checkboxes', href=tools.relpath('/dash-core-components/checklist'))),
    ComponentBlock('''import dash_core_components as dcc

dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['MTL', 'SF']
)''', style=styles.code_container),

    ComponentBlock('''import dash_core_components as dcc

dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['MTL', 'SF'],
    labelStyle={'display': 'inline-block'}
)''', style=styles.code_container),

    html.Br(),
    dcc.Link('Checklist Properties',
             href=tools.relpath("/dash-core-components/checklist")),
    html.Hr(),
    html.H3(dcc.Link('Radio Items', href=tools.relpath('/dash-core-components/radioitems'))),
    ComponentBlock('''import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)''', style=styles.code_container),

    ComponentBlock('''import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL',
    labelStyle={'display': 'inline-block'}
)''', style=styles.code_container),
    html.Br(),
    dcc.Link('RadioItems Reference',
             href=tools.relpath("/dash-core-components/radioitems")),

    html.Hr(),

    html.H3(dcc.Link('Button', href=tools.relpath('/dash-html-components/button'))),
    reusable_components.Markdown('''
    There actually is no `Button` component in `dash_core_components`.
    The regular `dash_html_components.Button` component does the job quite well,
    but we've included it here because this is the one plain `html` component
    that's commonly used as a callback input:
    '''),
    reusable_components.Markdown(
        examples['button'][0],
        style=styles.code_container
    ),
    html.Div(examples['button'][1], className='example-container'),
    html.Br(),
    dcc.Link('html.Button Reference',
             href=tools.relpath("/dash-html-components/button")),
    html.P([
        'For more on ',
        html.Code('dash.dependencies.State'),
        ', see the tutorial on ',
        dcc.Link('Dash State', href=tools.relpath('/state')),
        '.'
    ]),

    html.Hr(),

    html.H3(dcc.Link('DatePickerSingle', href=tools.relpath('/dash-core-components/datepickersingle'))),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt(1997, 5, 10)
)
''', style=styles.code_container),
    dcc.Link('More DatePickerSingle Examples and Reference',
             href=tools.relpath("/dash-core-components/datepickersingle")),
    html.Hr(),

    html.H3(dcc.Link('DatePickerRange', href=tools.relpath('/dash-core-components/datepickerrange'))),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    id='date-picker-range',
    start_date=dt(1997, 5, 3),
    end_date_placeholder_text='Select a date!'
)
''', style=styles.code_container),
    html.Br(),
    dcc.Link('More DatePickerRange Examples and Reference',
             href=tools.relpath("/dash-core-components/datepickerrange")),

    html.Hr(),

    html.H3(dcc.Link('Markdown', href=tools.relpath('/dash-core-components/markdown'))),
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
                   style=styles.code_container,
    ),

    html.Br(),
    dcc.Link('More Markdown Examples and Reference',
             href=tools.relpath("/dash-core-components/markdown")),

    html.Hr(),

    html.H3('Interactive Tables'),
    reusable_components.Markdown('''
    The `dash_html_components` library exposes all of the HTML tags.
    This includes the `Table`, `Tr`, and `Tbody` tags that can be used
    to create an HTML table. See <dccLink href="/getting-started" children="Dash Layout"/>
    for an example.

    Dash provides an interactive `DataTable` as part of the `data-table`
    project. This table includes built-in filtering, row-selection,
    editing, and sorting.

    '''.replace('    ', '')),

    html.A(
        className="image-link",
        href="https://github.com/plotly/dash-table-experiments",
        children=html.Img(
            src="assets/images/gallery/DataTable.gif",
            alt="Example of a Dash Interactive Table"
        )
    ),


    reusable_components.Markdown('''
    <dccLink href="/datatable" children="View the docs"/> or [View the source](https://github.com/plotly/dash-table)

    ***
    '''.replace('    ', '')),

    html.H3(dcc.Link('Upload Component', href=tools.relpath('/dash-core-components/upload'))),
    reusable_components.Markdown('''

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

    dcc.Link('More Upload Examples and Reference',
             href=tools.relpath("/dash-core-components/upload")),

    reusable_components.Markdown('''
    ***
    '''.replace('    ', '')),

    html.H3('Tabs'),
    reusable_components.Markdown('''
    The Tabs and Tab components can be used to create tabbed sections in your app.
    '''),

    reusable_components.Markdown(
        examples['tabs'][0],
        style=styles.code_container
    ),

    html.Div(examples['tabs'][1], className='example-container'),

    dcc.Link('More Tabs Examples and Reference',
             href=tools.relpath("/dash-core-components/tabs")),

    html.Hr(),

    html.H3(dcc.Link('Graphs', href=tools.relpath('/dash-core-components/graph'))),
    reusable_components.Markdown('''
    The `Graph` component shares the same syntax as the open-source
    `plotly.py` library. View the [plotly.py docs](https://plot.ly/python)
    to learn more.
    '''.replace('    ', '')),
    ComponentBlock('''import dash_core_components as dcc

dcc.Graph(
    figure=dict(
        data=[
            dict(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker=dict(
                    color='rgb(55, 83, 109)'
                )
            ),
            dict(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker=dict(
                    color='rgb(26, 118, 255)'
                )
            )
        ],
        layout=dict(
            title='US Export of Plastic Scrap',
            showlegend=True,
            legend=dict(
                x=0,
                y=1.0
            ),
            margin=dict(l=40, r=0, t=40, b=30)
        )
    ),
    style={'height': 300},
    id='my-graph'
)''', style=styles.code_container),

    html.Br(),
    dcc.Link('More Graphs Examples and Reference',
             href=tools.relpath("/dash-core-components/graph")),
    html.Br(),
    reusable_components.Markdown('View the [plotly.py docs](https://plot.ly/python).'),

    reusable_components.Markdown('***'),

    html.H3(dcc.Link('ConfirmDialog', href=tools.relpath('/dash-core-components/confirmdialog'))),

    reusable_components.Markdown('''
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
             href=tools.relpath('/dash-core-components/confirmdialog')),

    html.Br(),
    reusable_components.Markdown('***'),

    reusable_components.Markdown('There is also a `dcc.ConfirmDialogProvider`,'
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
             href=tools.relpath('/dash-core-components/confirmdialogprovider')),

    html.Br(),

    reusable_components.Markdown('***'),

    html.H3(dcc.Link('Store', href=tools.relpath('/dash-core-components/store'))),

    reusable_components.Markdown('''
    The store component can be used to keep data in the visitor's browser.
    The data is scoped to the user accessing the page.

    **Three types of storage (`storage_type` prop):**

    - `memory`: default, keep the data as long the page is not refreshed.
    - `local`: keep the data until it is manually cleared.
    - `session`: keep the data until the browser/tab closes.

    _For `local`/`session`, the data is serialized as json when stored._
    '''),

    ComponentBlock(s('''
    import dash_core_components as dcc

    store = dcc.Store(id='my-store', data={'my-data': 'data'})
    ''')),

    reusable_components.Markdown('_The store must be used with callbacks_'),

    dcc.Link('More Store Examples and Reference',
             href=tools.relpath('/dash-core-components/store')),

    html.Br(),

    reusable_components.Markdown('***'),
    html.H3(dcc.Link('Logout Button',
                     href=tools.relpath('/dash-core-components/logoutbutton'))),

    reusable_components.Markdown('''
    The logout button can be used to perform logout mechanism.

    It's a simple form with a submit button, when the button is clicked,
    it will submit the form to the `logout_url` prop.

    Please note that no authentication is performed in Dash by default
    and you have to implement the authentication yourself.
    '''),

    dcc.Link('More Logout Button Examples and Reference',
             href=tools.relpath('/dash-core-components/logoutbutton')),

    html.Div(id='hidden', style={'display': 'none'}),

    html.Br(),

    reusable_components.Markdown('***'),
    html.H3(dcc.Link('Loading component',
                     href=tools.relpath('/dash-core-components/loading'))),

    reusable_components.Markdown('''
    The Loading component can be used to wrap components that you want to display a spinner for, if they take too long to load.
    It does this by checking if any of the Loading components' children have a `loading_state` prop set where `is_loading` is true.
    If true, it will display one of the built-in CSS spinners.
    '''),
    ComponentBlock(s('''
    import dash_core_components as dcc
    import dash_html_components as html

    loading = dcc.Loading([
        # ...
    ])
    ''')),

    dcc.Link('More Loading Component Examples and Reference',
             href=tools.relpath('/dash-core-components/loading')),

    reusable_components.Markdown('***'),

    html.H3(dcc.Link('Location', href=tools.relpath('/dash-core-components/location'))),

    reusable_components.Markdown('''
    The location component represents the location bar in your web browser. Through its `href`, `pathname`,
    `search` and `hash` properties you can access different portions of your app's url.

    For example, given the url `http://127.0.0.1:8050/page-2?a=test#quiz`:

    - `href` = `"http://127.0.0.1:8050/page-2?a=test#quiz"`
    - `pathname` = `"/page-2"`
    - `search` = `"?a=test"`
    - `hash` = `"#quiz"`
    '''),

    reusable_components.Markdown(('''
    ```python
    import dash_core_components as dcc

    location = dcc.Location(id='url', refresh=False)
    ```
    '''), style=styles.code_container),

    html.Br(),

    dcc.Link('More Location Examples and Reference',
             href=tools.relpath('/dash-core-components/location')),

    html.Br(),
])
