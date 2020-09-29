# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

from dash_docs import styles
from dash_docs import tools
from dash_docs.tutorial.utils.convert_props_to_list import generate_prop_info
from dash_docs.tutorial.utils.component_block import ComponentBlock
from dash_docs.reusable_components import Syntax, Example
from dash_docs import reusable_components

examples = {
    'confirm': tools.load_example('tutorial/examples/core_components/confirm.py'),
    'confirm-provider': tools.load_example('tutorial/examples/core_components/confirm_provider.py'),
    'date_picker_single': tools.load_example('tutorial/examples/core_components/date_picker_single.py'),
    'date_picker_range': tools.load_example('tutorial/examples/core_components/date_picker_range.py'),
    'dropdown': tools.load_example('tutorial/examples/core_components/dropdown.py'),
    'dropdown-dynamic-options': tools.load_example('tutorial/examples/core_components/dropdown_dynamic_options.py'),
    'graph-config': tools.load_example('tutorial/examples/core_components/export_graph_to_chart_studio.py'),
    'input-all-types': tools.load_example('tutorial/examples/core_components/input_all_types.py'),
    'input-basic': tools.load_example('tutorial/examples/core_components/input-basic.py'),
    'input-number-type': tools.load_example('tutorial/examples/core_components/input_number_type.py'),
    'rangeslider': tools.load_example('tutorial/examples/core_components/rangeslider.py'),
    'rangeslider-nonlinear': tools.load_example('tutorial/examples/core_components/rangeslider_nonlinear.py'),
    'slider': tools.load_example('tutorial/examples/core_components/slider.py'),
    'slider-updatemode': tools.load_example('tutorial/examples/core_components/slider_updatemode.py'),
    'store-clicks': tools.load_example('tutorial/examples/core_components/store_clicks.py'),
    'store-share': tools.load_example('tutorial/examples/core_components/store_share.py'),
    'tabs_callback':  tools.load_example('tutorial/examples/core_components/tabs_callback_graph.py'),
    'tabs_simple':  tools.load_example('tutorial/examples/core_components/tabs_simple.py'),
    'tabs_styled_with_classes':  tools.load_example('tutorial/examples/core_components/tabs_styled_with_classes.py'),
    'tabs_styled_with_classes_css':  tools.read_file('assets/tabs-styled-with-classes.css'),
    'tabs_styled_with_inline':  tools.load_example('tutorial/examples/core_components/tabs_styled_with_inline.py'),
    'tabs_styled_with_props':  tools.load_example('tutorial/examples/core_components/tabs_styled_with_props.py'),
    'upload-datafile':  tools.load_example('tutorial/examples/core_components/upload-datafile.py'),
    'upload-gallery':  tools.load_example('tutorial/examples/core_components/upload-gallery.py'),
    'upload-image':  tools.load_example('tutorial/examples/core_components/upload-image.py'),
    'button_basic': tools.load_example('tutorial/examples/core_components/button_basic.py'),
    'button_n_clicks_timestamp': tools.load_example('tutorial/examples/core_components/button_n_clicks_timestamp.py'),
    'logout_button': tools.load_example('tutorial/examples/core_components/logout_button.py'),
    'loading_component': tools.load_example('tutorial/examples/core_components/loading_component.py')
}


# Dropdown
Dropdown = html.Div(children=[
    html.H1('Dropdown Examples and Reference'),
    html.Hr(),
    html.H3('Default Dropdown'),
    html.P("An example of a default dropdown without \
            any extra properties."),
    reusable_components.Markdown(
        examples['dropdown'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['dropdown'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3('Multi-Value Dropdown'),
    reusable_components.Markdown("A dropdown component with the `multi` property set to `True` \
                  will allow the user to select more than one value \
                  at a time."),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['MTL', 'NYC'],
    multi=True
)''', style=styles.code_container),
    html.Hr(),

    html.H3('Disable Search'),
    reusable_components.Markdown("The `searchable` property is set to `True` by default on all \
            `Dropdown` components. To prevent searching the dropdown \
            value, just set the `searchable` property to `False`. \
            Try searching for 'New York' on this dropdown below and compare \
            it to the other dropdowns on the page to see the difference."),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    searchable=False
)''', style=styles.code_container),
    html.Hr(),

    html.H3('Dropdown Clear'),
    reusable_components.Markdown("The `clearable` property is set to `True` by default on all \
            `Dropdown` components. To prevent the clearing of the selected dropdown \
            value, just set the `clearable` property to `False`"),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'},
    ],
    value='MTL',
    clearable=False
)''', style=styles.code_container),

    html.Hr(),
    html.H3('Placeholder Text'),
    reusable_components.Markdown("The `placeholder` property allows you to define \
                 default text shown when no value is selected."),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    placeholder="Select a city",
)''', style=styles.code_container),

    html.Hr(),
    html.H3('Disable Dropdown'),
    reusable_components.Markdown("To disable the dropdown just set `disabled=True`."),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    disabled=True
)''', style=styles.code_container),

    html.Hr(),
    html.H3('Disable Options'),
    reusable_components.Markdown("To disable a particular option inside the dropdown \
                 menu, set the `disabled` property in the options."),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC', 'disabled': True},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF', 'disabled': True}
    ],
)''', style=styles.code_container),

    html.H3('Dynamic Options'),
    html.P("This is an example on how to update the options on the server \
           depending on the search terms the user types. For example purpose \
           the options are empty on first load, as soon as you start typing \
           they will be loaded with the corresponding values."),
    reusable_components.Markdown(
        examples['dropdown-dynamic-options'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['dropdown-dynamic-options'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3("Dropdown Properties"),
    generate_prop_info('Dropdown')
])

# Graph
Graph = html.Div(children=[
    html.H1('Graph Examples and Reference'),
    html.Hr(),
    reusable_components.Markdown("""
    A Graph component. Graph can be used to render any plotly-powered data visualization,
    passed as the `figure` argument.
    """),
    html.H2('Primer on Plotly Graphing Library'),
    reusable_components.Markdown("""
        - The [**Plotly Graphing Library**](https://plotly.com/python),
        known as the package package `plotly`, generates "figures".
        These are used in `dcc.Graph` with e.g. `dcc.Graph(figure=fig)`
        with `fig` a plotly figure.
        - **To get started with plotly**, learn how its documentation is organized:
            1. Learn the architecture of the `figure`: https://plotly.com/python/creating-and-updating-figures/
            2. Every chart type has a set of examples at a unique URL.
            Familiarize yourself with the structure of these pages. Google is your friend.
            For example "Plotly Python Histogram Charts" is documented at
            https://plotly.com/python/histogram
            3. Plotly Express is the recommended high-level interface.
            Understand where it fits in by reading 1.
            Once you understand its structure, you can see all of the arguments in the
            "API Reference" page documented here: https://plotly.com/python-api-reference/plotly.express.html
            3. Every aspect of a chart is configurable.
            Read through 1 to understand the low-level `figure` interface and how to
            modify the properties of a generated figure.
            Once you understand it, view _all_ of the
            properties by visiting the "Figure Reference" page at https://plotly.com/python/reference.
            4. If you can't generate the graph easily with `px`, then learn the
            `graph_objects` structure by reading 1 and understanding
            the structure of the figure via https://plotly.com/python/reference.
        - Plotly supports 40-50 different chart types. Learn more by navigating
        https://plotly.com/python/
        - In development, you can create figures by running Dash apps or
        in other environments like Jupyter, your console, and more.
        If you are using the interface outside of Dash, then calling
        `fig.show()` will always display the graph (either in your browser
        or inline directly in your environment). To see all of these rendering
        environments, see https://plotly.com/python/renderers/.
    """),
    html.H2('Examples'),
    html.P("Simple graph defined from a dictionary with the same structure as a plotly figure"),
    ComponentBlock('''import dash_core_components as dcc
dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
''', style=styles.code_container),
    html.P("Graph defined directly from a plotly figure object"),
    ComponentBlock('''import dash_core_components as dcc
import plotly.graph_objects as go
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
''', style=styles.code_container),


    html.H2('Interactive Graphing'),
    reusable_components.Markdown("""
    The <dccLink href="/interactive-graphing" children="Interactive Visualizations"/> tutorial explains how
    to capture user interaction events with a `dcc.Graph`, and how to update the
    `figure` property in callbacks.

    Some advanced features are documented in [community forum](https://community.plotly.com/) posts:

    - How to preserve the UI state (zoom level etc.) of a Graph when updating the Graph in a callback
    https://community.plotly.com/t/preserving-ui-state-like-zoom-in-dcc-graph-with-uirevision/15793
    - Graph transitions for smooth transitions or animations on Graph updates
    https://community.plotly.com/t/exploring-a-transitions-api-for-dcc-graph/15468
    """),

    html.H2('Graph Resizing and Responsiveness'),
    reusable_components.Markdown("""

    There are quite a few options that you can take advantage of if
    you want the size of your graph to be reactive.

    The default `plotly.js` behavior dictates that the graph should
    resize upon window resize. However, in some cases, you might want
    to resize the graph based on the size of its parent container
    instead. (You can set the size of the parent container with the
    `style.height` and `style.width` properties.)

    The `responsive` property of the `dcc.Graph` component allows you
    to define your desired behavior. In short, it accepts as a value
    `True`, `False`, or `'auto'`:

    * `True` forces the graph to be responsive to window and parent
      resize, regardless of any other specifications in
      `figure.layout` or `config`
    * `False` forces the graph to be non-responsive to window and
      parent resize, regardless of any other specifications in
      `figure.layout` or `config`
    * `'auto'` preserves the legacy behavior (size and resizability
      are determined by values specified in `figure.layout` and
      `config.responsive`)

    """),

    html.H3('How Resizing Works - Advanced'),
    reusable_components.Markdown("""

    The properties of `dcc.Graph` that can control the size of the
    graph (other than `responsive`) are:

    * `figure.layout.height` - explicitly sets the height
    * `figure.layout.width` - explicitly sets the width
    * `figure.layout.autosize` - if `True`, sets the height and width
      of the graph to that of its parent container
    * `config.responsive` - if `True`, changes the height and width of
      the graph upon window resize

    The `responsive` property works in conjunction with the above
    properties in the following way:

    * `True`: `config.responsive` and `figure.layout.autosize` are
    overriden with `True` values, and `figure.layout.height` and
    `figure.layout.width` are unset
    * `False`: `config.responsive` and `figure.layout.autosize` are
      both overriden with `False` values
    * `'auto'`: the resizability of the plot is determined the
      same way as it used to be (i.e., with the four properties above)

  """),

    html.H3('Graph Properties'),
    generate_prop_info('Graph')
])

# Slider
Slider = html.Div(children=[
    html.H1('Slider Examples and Reference'),
    html.Hr(),
    html.H3('Simple Slider Example'),
    html.P("An example of a basic slider tied to a callback."),
    reusable_components.Markdown(
        examples['slider'][0],
        style=styles.code_container,
    ),

    html.Div(examples['slider'][1], className='example-container'),
    html.Hr(),
    html.H3('Marks and Steps'),
    reusable_components.Markdown("If slider `marks` are defined and `step` is set to `None` \
                 then the slider will only be able to select values that \
                 have been predefined by the `marks`. Note that the default \
                 is `step=1`, so you must explicitly specify `None` to get \
                 this behavior.`marks` is a `dict` where the keys represent \
                 the numerical values and the values represent their labels."),
    ComponentBlock('''import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=10,
    step=None,
    marks={
        0: '0 °F',
        3: '3 °F',
        5: '5 °F',
        7.65: '7.65 °F',
        10: '10 °F'
    },
    value=5
)''', style=styles.code_container),
    html.Hr(),

    html.H3('Included and Styling Marks'),
    reusable_components.Markdown("By default, `included=True`, meaning the rail trailing the \
                 handle will be highlighted. To have the handle act as a \
                 discrete value set `included=False`. To style `marks`, \
                 include a style css attribute alongside the key value."),

    ComponentBlock('''import dash_core_components as dcc

# Slider has included=True by default
dcc.Slider(
    min=0,
    max=100,
    value=65,
    marks={
        0: {'label': '0 °C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26 °C'},
        37: {'label': '37 °C'},
        100: {'label': '100 °C', 'style': {'color': '#f50'}}
    }
)'''),
    ComponentBlock('''import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=100,
    value=65,
    marks={
        0: {'label': '0 °C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26 °C'},
        37: {'label': '37 °C'},
        100: {'label': '100 °C', 'style': {'color': '#f50'}}
    },
    included=False
)'''),

    html.Hr(),
    html.H3('Non-Linear Slider and Updatemode'),
    reusable_components.Markdown("Create a logarithmic slider by setting the labels of the \
                 `marks` property \
                 to be logarithmic and adjusting the slider's output \
                 `value` in the callbacks. The `updatemode` property \
                 allows us to determine when we want a callback to be \
                 triggered. The following example has `updatemode='drag'` \
                 which means a callback is triggered everytime the handle \
                 is moved. The default setting is `mouseup` which triggers \
                 the callback when you release your mouse from the slider."),
    reusable_components.Markdown(
        examples['slider-updatemode'][0],
        style=styles.code_container,
    ),
    html.Div(
        examples['slider-updatemode'][1],
        className='example-container',
        style={'overflow': 'hidden', 'padding': '20px'}
    ),
    html.Hr(),
    html.H3("Slider Properties"),
    generate_prop_info('Slider')
])

# RangeSlider
RangeSlider = html.Div(children=[
    html.H1("RangeSlider Examples and Reference"),
    html.Hr(),
    html.H3('Simple RangeSlider Example'),
    html.P("An example of a basic RangeSlider tied to a callback."),
    reusable_components.Markdown(
        examples['rangeslider'][0],
        style=styles.code_container,
    ),

    html.Div(
        examples['rangeslider'][1],
        className='example-container',
        style={'overflow': 'hidden'}),

    html.Hr(),
    html.H3('Marks and Steps'),
    reusable_components.Markdown("If slider `marks` are defined and `step` is set to `None` \
                 then the slider will only be able to select values that \
                 have been predefined by the `marks`. \
                 Note that the default is `step=1`, so you must explicitly \
                 specify `None` to get this behavior."),
    ComponentBlock('''import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=10,
    step=None,
    marks={
        0: '0 °F',
        3: '3 °F',
        5: '5 °F',
        7.65: '7.65 °F',
        10: '10 °F'
    },
    value=[3, 7.65]
)''', style=styles.code_container),
    html.Hr(),

    html.H3('Included and Styling Marks'),
    reusable_components.Markdown("By default, `included=True`, meaning the rail trailing the \
                 handle will be highlighted. To have the handle act as a \
                 discrete value set `included=False`. To style `marks`, \
                 include a style css attribute alongside the key value."),
    ComponentBlock('''import dash_core_components as dcc

# RangeSlider has included=True by default
dcc.RangeSlider(
    min=0,
    max=100,
    value=[10, 65],
    marks={
        0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26°C'},
        37: {'label': '37°C'},
        100: {'label': '100°C', 'style': {'color': '#f50'}}
    }
)'''),

    ComponentBlock('''import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=100,
    value=[10, 65],
    marks={
        0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26°C'},
        37: {'label': '37°C'},
        100: {'label': '100°C', 'style': {'color': '#f50'}}
    },
    included=False
)''', style=styles.code_container),
    html.Hr(),

    html.H3('Multiple Handles'),
    reusable_components.Markdown('To create multiple handles \
                  just define more values for `value`!'),
    ComponentBlock('''import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=30,
    value=[1, 3, 4, 5, 12, 17]
)
    ''', style=styles.code_container),
    html.Hr(),
    html.H3('Pushable Handles'),
    reusable_components.Markdown("The `pushable` property is either a `boolean` or a numerical value. \
                The numerical value determines the minimum distance between \
                the handles. Try moving the handles around!"),
    ComponentBlock('''import dash_core_components as dcc
dcc.RangeSlider(
    min=0,
    max=30,
    value=[8, 10, 15, 17, 20],
    pushable=2
)
    ''', style=styles.code_container),
    html.Hr(),

    html.H3('Crossing Handles'),
    reusable_components.Markdown("If `allowCross=False`, the handles will not be allowed to\
                  cross over each other"),
    ComponentBlock('''import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=30,
    value=[10, 15],
    allowCross=False
)
    ''', style=styles.code_container),
    html.Hr(),

    html.H3('Non-Linear Slider and Updatemode'),
    reusable_components.Markdown("Create a logarithmic slider by setting `marks`\
                 to be logarithmic and adjusting the slider's output \
                 `value` in the callbacks. The `updatemode` property \
                 allows us to determine when we want a callback to be \
                 triggered. The following example has `updatemode='drag'` \
                 which means a callback is triggered everytime the handle \
                 is moved. \
                 Contrast the callback output with the first example on this \
                 page to see the difference."),
    reusable_components.Markdown(
        examples['rangeslider-nonlinear'][0],
        style=styles.code_container,
    ),
    html.Div(examples['rangeslider-nonlinear'][1],
             className='example-container',
             style={'overflow': 'hidden', 'padding': '20px'}),
    html.Hr(),
    generate_prop_info('RangeSlider')
])


# Checklist
Checklist = html.Div(children=[
    html.H3('Checklist Properties'),
    generate_prop_info('Checklist')
])


# Input
Input = html.Div(children=[
    html.H1('Input Examples and Reference'),
    html.Hr(),
    html.H3('Supported Input Types'),
    Syntax(examples['input-all-types'][0]),
    Example(examples['input-all-types'][1]),
    html.Br(),
    html.H3('Debounce delays the Input processing'),
    Syntax(examples['input-basic'][0]),
    Example(examples['input-basic'][1]),
    html.Br(),
    html.H3('Number Input'),
    reusable_components.Markdown("""

    *fixed and enhanced in Dash v1.1*

    Number type is now close to native HTML5 `input` behavior across
    browsers. We also apply a strict number casting in callbacks:
    valid number converts into corresponding number types, and invalid number
    converts into None. E.g.
    `dcc.Input(id='range', type='number', min=2, max=10, step=1)` typing 3 and
    11 will return respectively integer three and None in Python callbacks.

    ##### Important Notice

    There is a limitation when converting numbers like 1.0 or 0.0, the
    corresponding number type in callbacks is **Integer** instead of **Float**.
    Please add extra guard casting like `float()` within callbacks if needed.
    """),
    Syntax(examples['input-number-type'][0]),
    Example(examples['input-number-type'][1]),
    html.Br(),
    html.H3('Input Properties'),
    generate_prop_info('Input')
])


# RadioItems
RadioItems = html.Div(children=[
    html.H3('RadioItem Properties'),
    generate_prop_info('RadioItems')
])

# Button
Button = html.Div(children=[
    html.H1('Button Examples and Reference'),
    html.Hr(),
    html.Br(),
    html.H3('Button Basic Example'),
    html.Hr(),
    reusable_components.Markdown("An example of a default button without any extra properties \
    and `n_clicks` in the callback. `n_clicks` is an integer that represents \
    that number of times the button has been clicked. Note that the original \
    value is `None`."),
    Syntax(examples['button_basic'][0]),
    Example(examples['button_basic'][1]),
    html.Br(),
    html.H3('Button with n_clicks_timestamp'),
    html.Hr(),
    reusable_components.Markdown("This example utilizes the `n_clicks_timestamp` property, \
    which returns an integer representation of time. This is useful for \
    determining when the button was last clicked."),
    Syntax(examples['button_n_clicks_timestamp'][0]),
    Example(examples['button_n_clicks_timestamp'][1]),
    html.Br(),
    html.H3('Button Properties'),
    html.Hr(),
    generate_prop_info('Button', html)
])


# Markdown
Markdown = html.Div(children=[
    html.H1("Markdown Examples and Reference"),
    html.Hr(),
    html.H3("Syntax Guide"),
    reusable_components.Markdown("These examples are based on the \
    [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/).\
    The Dash Markdown component uses the \
    [CommonMark](http://commonmark.org/) specification of Markdown."),
    html.Br(),
    html.H3("Headers"),
    ComponentBlock("""import dash_core_components as dcc

dcc.Markdown('''

# This is an <h1> tag

## This is an <h2> tag

###### This is an <h6> tag
''')"""),
    html.H3("Emphasis"),
    ComponentBlock("""import dash_core_components as dcc

dcc.Markdown('''
*This text will be italic*

_This will also be italic_


**This text will be bold**

__This will also be bold__

_You **can** combine them_
''')"""),
    html.Hr(),
    html.H3("Lists"),
    html.H3("Unordered"),
    ComponentBlock("""import dash_core_components as dcc

dcc.Markdown('''
* Item 1
* Item 2
  * Item 2a
  * Item 2b
''')"""),
    html.Hr(),
    html.H3("Block Quotes"),
    ComponentBlock("""import dash_core_components as dcc

dcc.Markdown('''
>
> Block quotes are used to highlight text.
>

''')"""),
    html.Hr(),
    html.H3("Links"),
    ComponentBlock("""import dash_core_components as dcc

dcc.Markdown('''
[Dash User Guide](/)
''')"""),
    html.Hr(),
    html.H3("Inline Code"),
    html.P("Any block of text surrounded by ` ` will rendered as inline-code. "),
    # Don't use ComponentBlock for markdown block quotes... too complicated to
    # get all the nested quotes right!
    reusable_components.Markdown("""
    ````py
    import dash_core_components as dcc

    dcc.Markdown('''

    Inline code snippet: `True`

    Block code snippet:
    ```py
    import dash

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    ```
    ''')
    ````
    """),
    html.Div(reusable_components.Markdown('''

    Inline code snippet: `True`

    Block code snippet:
    ```py
    import dash

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    ```
    '''), className='example-container'),

    reusable_components.Markdown('''

    Only certain languages are supported by default in
    `dcc.Markdown`. For more details about how to customize the
    languages and colour schemes, please see ["Syntax Highlighting
    With
    Markdown"](https://dash.plotly.com/external-resources#md-syntax-highlight).
    '''),

    html.Hr(),
    html.H3('Markdown Properties'),
    generate_prop_info('Markdown')
])

# DatePickerRange
DatePickerRange = html.Div(children=[
    html.H1("DatePickerRange Examples and Reference"),
    html.Hr(),
    html.H3("Simple DatePickerRange Example"),
    reusable_components.Markdown("This is a simple example of a `DatePickerRange` \
                 component tied to a callback. The `min_date_allowed` and \
                 `max_date_allowed` properties define the minimum and \
                 maximum selectable \
                 dates on the calendar while `initial_visible_month` defines \
                 the calendar month that is first displayed when the \
                 `DatePickerRange` component is opened."),
    reusable_components.Markdown(
        examples['date_picker_range'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['date_picker_range'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),
    html.Hr(),
    html.H3('Month and Display Format'),
    reusable_components.Markdown("The `display_format` property \
                 determines how selected dates are displayed \
                 in the `DatePickerRange` component. The `month_format` \
                 property determines how calendar headers are displayed when \
                 the calendar is opened."),
    html.P("Both of these properties are configured through \
            strings that utilize a combination of any \
            of the following tokens."),
    html.Table([
        html.Tr([
            html.Th('String Token', style={'text-align': 'left', 'width': '20%'}),
            html.Th('Example', style={'text-align': 'left', 'width': '20%'}),
            html.Th('Description', style={'text-align': 'left', 'width': '60%'})
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`YYYY`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`2014`'), style={'text-align': 'left'}),
            html.Td('4 or 2 digit year')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`YY`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`14`'), style={'text-align': 'left'}),
            html.Td('2 digit year')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`Y`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`-25`'), style={'text-align': 'left'}),
            html.Td('Year with any number of digits and sign')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`Q`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1..4`'), style={'text-align': 'left'}),
            html.Td('Quarter of year. Sets month to first month in quarter.')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`M MM`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1..12`'), style={'text-align': 'left'}),
            html.Td('Month number')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`MMM MMMM`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`Jan..December`'), style={'text-align': 'left'}),
            html.Td('Month name')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`D DD`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1..31`'), style={'text-align': 'left'}),
            html.Td('Day of month')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`Do`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1st..31st`'), style={'text-align': 'left'}),
            html.Td('Day of month with ordinal')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`DDD DDDD`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1..365`'), style={'text-align': 'left'}),
            html.Td('Day of year')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`X`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1410715640.579`'), style={'text-align': 'left'}),
            html.Td('Unix timestamp')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`x`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1410715640579`'), style={'text-align': 'left'}),
            html.Td('Unix ms timestamp')
        ]),
    ]),
    html.Br(),
    html.H3("Display Format Examples"),
    reusable_components.Markdown("You can utilize any permutation of the string tokens \
                 shown in the table above to change how selected dates are \
                 displayed in the `DatePickerRange` component."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    end_date=dt(2017,6,21,23,59,59,999999),
    display_format='MMM Do, YY',
    start_date_placeholder_text='MMM Do, YY'
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt
dcc.DatePickerRange(
    end_date=dt(2017,6,21),
    display_format='M-D-Y-Q',
    start_date_placeholder_text='M-D-Y-Q'
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    end_date=dt(2017,6,21),
    display_format='MMMM Y, DD',
    start_date_placeholder_text='MMMM Y, DD'
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    end_date=dt(2017,6,21),
    display_format='X',
    start_date_placeholder_text='X'
)''', style=styles.code_container),

    html.Br(),

    html.H3("Month Format Examples"),
    reusable_components.Markdown("Similar to the `display_format`, you can set `month_format` \
                 to any permutation of the string tokens \
                 shown in the table above to change how calendar titles \
                 are displayed in the `DatePickerRange` component."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    month_format='MMM Do, YY',
    end_date_placeholder_text='MMM Do, YY',
    start_date=dt(2017,6,21)
)'''),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    month_format='M-D-Y-Q',
    end_date_placeholder_text='M-D-Y-Q',
    start_date=dt(2017,6,21)
)'''),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    month_format='MMMM Y',
    end_date_placeholder_text='MMMM Y',
    start_date=dt(2017,6,21)
)'''),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    month_format='X',
    end_date_placeholder_text='X',
    start_date=dt(2017,6,21)
)'''),

    html.Hr(),

    html.H3("Vertical Calendar and Placeholder Text"),
    reusable_components.Markdown("The `DatePickerRange` component can be rendered in two \
                  orientations, either horizontally or vertically. \
                  If `calendar_orientation` is set to `'vertical'`, it will \
                  be rendered vertically and will default to `'horizontal'` \
                  if not defined."),
    reusable_components.Markdown("The `start_date_placeholder_text` and \
                  `end_date_placeholder_text` define the grey default text \
                  defined in the calendar input boxes when no date is \
                  selected."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    start_date_placeholder_text="Start Period",
    end_date_placeholder_text="End Period",
    calendar_orientation='vertical',
)'''),

    html.Hr(),

    html.H3("Minimum Nights, Calendar Clear, and Portals"),
    reusable_components.Markdown("The `minimum_nights` property defines the number of \
                  nights that must be in between the range of two \
                  selected dates."),
    reusable_components.Markdown("When the `clearable` property is set to `True` \
                  the component will be rendered with a small 'x' \
                  that will remove all selected dates when selected."),
    reusable_components.Markdown("The `DatePickerRange` component supports two different \
                  portal types, one being a full screen portal \
                  (`with_full_screen_portal`) and another being a simple \
                  screen overlay, like the one shown below (`with_portal`)."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    minimum_nights=5,
    clearable=True,
    with_portal=True,
    start_date=dt(2017,6,21)
)'''),

    html.Hr(),

    html.H3("Right to Left Calendars and First Day of Week"),
    reusable_components.Markdown("When the `is_RTL` property is set to `True` \
                  the calendar will be rendered from right to left."),
    reusable_components.Markdown("The `first_day_of_week` property allows you to \
                  define which day of the week will be set as the first \
                  day of the week. In the example below, Tuesday is \
                  the first day of the week."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    is_RTL=True,
    first_day_of_week=3,
    start_date=dt(2017,6,21)
)''', style=styles.code_container),
    html.Hr(),
    html.H3('DatePickerRange Properties'),
    generate_prop_info('DatePickerRange')
])

# DatePickerSingle
DatePickerSingle = html.Div(children=[
    html.H1("DatePickerSingle Examples and Reference"),
    html.Hr(),
    html.H3("Simple DatePickerSingle Example"),
    reusable_components.Markdown("This is a simple example of a `DatePickerSingle` \
        component tied to a callback. You can use either date objects \
        (`datetime.date` or `datetime.datetime`) or strings in the form \
        `YYYY-MM-DD` to provide dates to Dash components. Strings are \
        preferred because that's the form dates take as callback arguments. \
        Be aware that any time information included in a datetime object \
        or string will be ignored. The `min_date_allowed` and `max_date_allowed` \
        properties define the minimum and maximum selectable dates on the calendar \
        while `initial_visible_month` defines the calendar month that is \
        first displayed when the `DatePickerSingle` component is opened."),
    reusable_components.Markdown(
        examples['date_picker_single'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['date_picker_single'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),

    html.H3('Month and Display Format'),
    reusable_components.Markdown("The `display_format` property \
                 determines how selected dates are displayed \
                 in the `DatePickerSingle` component. The `month_format` \
                 property determines how calendar headers are displayed when \
                 the calendar is opened."),
    html.P("Both of these properties are configured through \
            strings that utilize a combination of any \
            of the following tokens."),
    html.Table([
        html.Tr([
            html.Th('String Token', style={'text-align': 'left', 'width': '20%'}),
            html.Th('Example', style={'text-align': 'left', 'width': '20%'}),
            html.Th('Description', style={'text-align': 'left', 'width': '60%'})
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`YYYY`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`2014`'), style={'text-align': 'left'}),
            html.Td('4 or 2 digit year')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`YY`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`14`'), style={'text-align': 'left'}),
            html.Td('2 digit year')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`Y`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`-25`'), style={'text-align': 'left'}),
            html.Td('Year with any number of digits and sign')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`Q`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1..4`'), style={'text-align': 'left'}),
            html.Td('Quarter of year. Sets month to first month in quarter.')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`M MM`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1..12`'), style={'text-align': 'left'}),
            html.Td('Month number')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`MMM MMMM`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`Jan..December`'), style={'text-align': 'left'}),
            html.Td('Month name')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`D DD`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1..31`'), style={'text-align': 'left'}),
            html.Td('Day of month')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`Do`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1st..31st`'), style={'text-align': 'left'}),
            html.Td('Day of month with ordinal')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`DDD DDDD`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1..365`'), style={'text-align': 'left'}),
            html.Td('Day of year')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`X`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1410715640.579`'), style={'text-align': 'left'}),
            html.Td('Unix timestamp')
        ]),
        html.Tr([
            html.Td(reusable_components.Markdown('`x`'), style={'text-align': 'left'}),
            html.Td(reusable_components.Markdown('`1410715640579`'), style={'text-align': 'left'}),
            html.Td('Unix ms timestamp')
        ]),
    ]),

    html.Br(),

    html.H3("Display Format Examples"),
    reusable_components.Markdown("You can utilize any permutation of the string tokens \
                 shown in the table above to change how selected dates are \
                 displayed in the `DatePickerSingle` component."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    date='2017-06-21',
    display_format='MMM Do, YY'
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    date=dt(2017,6,21),
    display_format='M-D-Y-Q',
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    date=dt(2017,6,21),
    display_format='MMMM Y, DD'
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    date=dt(2017,6,21),
    display_format='X',
)''', style=styles.code_container),
    html.Br(),
    html.H3("Month Format Examples"),
    reusable_components.Markdown("Similar to the `display_format`, you can set `month_format` \
                 to any permutation of the string tokens \
                 shown in the table above to change how calendar titles \
                 are displayed in the `DatePickerSingle` component."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    month_format='MMM Do, YY',
    placeholder='MMM Do, YY',
    date=dt(2017,6,21)
)'''),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    month_format='M-D-Y-Q',
    placeholder='M-D-Y-Q',
    date=dt(2017,6,21)
)'''),

    ComponentBlock('''import dash_core_components as dcc
import datetime

dcc.DatePickerSingle(
    month_format='MMMM Y',
    placeholder='MMMM Y',
    date=datetime.date(2020,2,29)
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    month_format='X',
    placeholder='X',
    date=dt(2017,6,21,0,0,0,0)
)''', style=styles.code_container),
    html.Hr(),
    html.H3("Vertical Calendar and Placeholder Text"),
    reusable_components.Markdown("The `DatePickerSingle` component can be rendered in two \
                  orientations, either horizontally or vertically. \
                  If `calendar_orientation` is set to `'vertical'`, it will \
                  be rendered vertically and will default to `'horizontal'` \
                  if not defined."),
    reusable_components.Markdown("The `placeholder` defines the grey default \
                  text defined in the calendar input boxes when no date is \
                  selected."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    calendar_orientation='vertical',
    placeholder='Select a date',
    date=dt(2017,6,21)
)'''),

    html.Hr(),

    html.H3("Calendar Clear and Portals"),
    reusable_components.Markdown("When the `clearable` property is set to `True` \
                  the component will be rendered with a small 'x' \
                  that will remove all selected dates when selected."),
    reusable_components.Markdown("The `DatePickerSingle` component supports two different \
                  portal types, one being a full screen portal \
                  (`with_full_screen_portal`) and another being a simple \
                  screen overlay, like the one shown below (`with_portal`)."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    clearable=True,
    with_portal=True,
    date=dt(2017,6,21)
)'''),

    html.Hr(),

    html.H3("Right to Left Calendars and First Day of Week"),
    reusable_components.Markdown("When the `is_RTL` property is set to `True` \
                  the calendar will be rendered from right to left."),
    reusable_components.Markdown("The `first_day_of_week` property allows you to \
                  define which day of the week will be set as the first \
                  day of the week. In the example below, Tuesday is \
                  the first day of the week."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    is_RTL=True,
    first_day_of_week=3,
    date=dt(2017,6,21)
)'''),

    html.Hr(),
    html.H3('DatePickerSingle Properties'),
    generate_prop_info('DatePickerSingle')
])

# Link
Link = html.Div(children=[
    html.H3('Link Example'),
    reusable_components.Markdown('To learn more about links, see the chapter on <dccLink href="/urls" children="Dash URLs"/>'),
    html.H3('Link Properties'),
    generate_prop_info('Link')
])

# Textarea
Textarea = html.Div(children=[
    html.H3('Textarea Properties'),
    generate_prop_info('Textarea')
])

# Tabs
Tabs = html.Div(children=[
    html.H1('Tabs Examples and Reference'),
    reusable_components.Markdown('''
    The Tabs and Tab components can be used to create tabbed sections in your app.
    The `Tab` component controls the style and value of the individual tab
    and the `Tabs` component hold a collection of `Tab` components.

    **Table of Contents**
    -  Method 1. Content as Callback
    -  Method 2. Content as Tab children
    - Styling the Tabs component
        - with CSS classes
        - with inline styles
        - with props
    ***
    '''),

    html.H2('Method 1. Content as Callback'),
    reusable_components.Markdown('''
    Attach a callback to the Tabs `value` prop and update a container's `children`
    property in your callback.
    '''),
    reusable_components.Markdown(
        examples['tabs_callback'][0],
        style=styles.code_container
    ),
    html.Div(examples['tabs_callback'][1], className='example-container'),
    reusable_components.Markdown('''
    In the example above, our callback contains all of the content. In practice,
    we'll keep the tab's content in separate files and import the data.
    For an example, see the <dccLink children="URLs and Multi-Page App Tutorial" href="/urls"/>.
    '''),

    html.H2('Method 2. Content as Tab Children'),
    reusable_components.Markdown('''
    Instead of displaying the content through a callback, you can embed the content
    directly as the `children` property in the `Tab` component:
    '''),

    reusable_components.Markdown(
        examples['tabs_simple'][0],
        style=styles.code_container
    ),
    html.Div(examples['tabs_simple'][1], className='example-container'),
    reusable_components.Markdown('''
    Note that this method has a drawback: it requires that you compute the children property for each individual
    tab _upfront_ and send all of the tab's content over the network _at once_.
    The callback method allows you to compute the tab's content _on the fly_
    (that is, when the tab is clicked).
    '''),

    html.H2('Styling the Tabs component'),
    html.H3('With CSS classes'),
    reusable_components.Markdown('''
    Styling the Tabs (and Tab) component can either be done using CSS classes by providing your own to the `className` property:
    '''),

    reusable_components.Markdown(
        examples['tabs_styled_with_classes'][0],
        style=styles.code_container
    ),
    html.Div(examples['tabs_styled_with_classes'][1], className='example-container'),

    html.Br(),

    reusable_components.Markdown('''
    Notice how the container of the Tabs can be styled as well by supplying a class to the `parent_className` prop, which we use here to draw a border below it, positioning the actual Tabs (with padding) more in the center.
    We also added `display: flex` and `justify-content: center` to the regular `Tab` components, so that labels with multiple lines will not break the flow of the text.

    The corresponding CSS file (`assets/tabs.css`) looks like this.
    Save the file in an `assets` folder (it can be named anything you want).
    Dash will automatically include this CSS when the app is loaded.
    <dccLink
        children="Learn more about including CSS in your app"
        href="/external-resources"
    />.
    '''),

    reusable_components.Markdown(
        '```css\n' + examples['tabs_styled_with_classes_css'] + '\n```',
        style=styles.code_container
    ),


    html.Br(),

    html.H3('With inline styles'),
    reusable_components.Markdown('''
    An alternative to providing CSS classes is to provide style dictionaries directly:
    '''),

    reusable_components.Markdown(
        examples['tabs_styled_with_inline'][0],
        style=styles.code_container
    ),
    html.Div(examples['tabs_styled_with_inline'][1], className='example-container'),

    html.Br(),

    reusable_components.Markdown('''
    Lastly, you can set the colors of the Tabs components in the `color` prop, by specifying the "border", "primary", and "background" colors in a dict. Make sure you set them
    all, if you're using them!
    '''),

    reusable_components.Markdown(
        examples['tabs_styled_with_props'][0],
        style=styles.code_container
    ),
    html.Div(examples['tabs_styled_with_props'][1], className='example-container'),

    html.Hr(),

    html.H3('Tabs properties'),
    generate_prop_info('Tabs'),
    html.H3('Tab properties'),
    generate_prop_info('Tab')
])

# Graphs
Graphs = html.Div([
    html.H1('Graph Reference'),
    reusable_components.Markdown('''
    Customize the [Plotly.js config options](https://plotly.com/javascript/configuration-options/) of your graph using
    the `config` property. The example below uses the `showSendToCloud` and `plotlyServerURL` options include a
    save button in the modebar of the graph which exports the figure to URL specified by `plotlyServerURL`.

    '''),
    Syntax(examples['graph-config'][0]),
    Example(examples['graph-config'][1]),
    html.H3('Graph Properties'),
    generate_prop_info('Graph')
])

# Upload
Upload = html.Div([
    html.H1('Upload Component'),
    reusable_components.Markdown('''
    The Dash upload component allows your app's viewers to upload files,
    like excel spreadsheets or images, into your application.
    Your Dash app can access the contents of an upload by listening to
    the `contents` property of the `dcc.Upload` component.

    `contents` is a base64 encoded string that contains the files contents,
    no matter what type of file: text files, images, zip files,
    excel spreadsheets, etc.

    '''),

    Syntax(examples['upload-datafile'][0], summary=reusable_components.Markdown('''
        Here's an example that parses CSV or Excel files and displays
        the results in a table. Note that this example uses the
        `DataTable` from the
        [dash-table](https://github.com/plotly/dash-table)
        project.
    ''')),

    Example(examples['upload-datafile'][1]),

    html.Hr(),

    Syntax(examples['upload-image'][0], summary=reusable_components.Markdown('''
        This next example responds to image uploads by displaying them
        in the app with the `html.Img` component.
    ''')),
    Example(examples['upload-image'][1]),

    Syntax(examples['upload-gallery'][0], summary=reusable_components.Markdown('''
        The `children` attribute of the `Upload` component accepts any
        Dash component. Clicking on the children element will trigger the
        upload action, as will dragging and dropping files.
        Here are a few different ways that you could style the upload
        component using standard dash components.
    ''')),
    Example(examples['upload-gallery'][1]),

    html.Hr(),

    html.H2('Upload Component Properties'),
    generate_prop_info('Upload')
])

# ConfirmDialog
ConfirmDialog = html.Div([
    html.H1('ConfirmDialog component'),
    reusable_components.Markdown('''
    ConfirmDialog is used to display the browser's native "confirm" modal,
    with an optional message and two buttons ("OK" and "Cancel").
    This ConfirmDialog can be used in conjunction with buttons when the user
    is performing an action that should require an extra step of verification.
    '''),
    Syntax(examples['confirm'][0]),
    Example(examples['confirm'][1]),
    generate_prop_info('ConfirmDialog')
])

# ConfirmDialogProvider
ConfirmDialogProvider = html.Div([
    html.H1('ConfirmDialogProvider component'),
    reusable_components.Markdown('''
    Send a <dccLink href="/dash-core-components/confirmdialog" children="ConfirmDialog"/> when the user
    clicks the children of this component, usually a button.
    '''),
    Syntax(examples['confirm-provider'][0]),
    Example(examples['confirm-provider'][1]),
    generate_prop_info('ConfirmDialogProvider')
])


Store = html.Div([
    html.H1('Store component'),
    reusable_components.Markdown('''
    Store json data in the browser.

    ## limitations.

    - The store will not work properly if there is no callback associated.
    - `modified_timestamp` is read only.

    ### local/session specifics

    - The store will not work properly if it's not included in the initial layout.
    - The maximum browser [storage space](https://demo.agektmr.com/storage/) is determined by the following factors:
        - your own hard drive size
        - mobile or laptop
        - the browser, under which a sophisticated algorithm is implemented within *Quota Management*
        - storage encoding where UTF-16 can end up saving only half of the size of UTF-8

      It's generally safe to store up to 2MB in most environments, and 5~10MB in most desktop-only applications.

    ### Retrieving the initial store data

    If you use the `data` prop as an output, you cannot get the
    initial data on load with the `data` prop. To counter this,
    you can use the `modified_timestamp` as `Input` and the `data` as `State`.

    This limitation is due to the initial None callbacks blocking the true
    data callback in the request queue.

    See https://github.com/plotly/dash-renderer/pull/81 for further discussion.
    '''),
    html.H2('Store clicks example'),
    Syntax(examples['store-clicks'][0]),
    Example(examples['store-clicks'][1]),

    html.H2('Share data between callbacks'),

    Syntax(examples['store-share'][0]),
    Example(examples['store-share'][1]),

    generate_prop_info('Store'),
])


LogoutButton = html.Div([
    html.H1('LogoutButton'),

    reusable_components.Markdown('''
    Please note that no authentication is performed in Dash by default
    and you have to implement the authentication yourself.

    ## List of packages that provide authentication methods:

    - [flask-login](https://flask-login.readthedocs.io/en/latest/)
    - [dash-auth](https://github.com/plotly/dash-auth)

    You can also use these packages for custom authentication:

    ### Password hashes:
    - [bcrypt](https://github.com/pyca/bcrypt/)
    - [passlib](https://passlib.readthedocs.io/en/stable/)

    ### Session/cookies
    - [flask-session](https://pythonhosted.org/Flask-Session/)
    - [itsdangerous](https://pythonhosted.org/itsdangerous/)
    - [pyjwt](https://github.com/jpadilla/pyjwt)
    '''),

    html.H2('Custom authentication example'),

    Syntax(examples['logout_button'][0]),
    Example(examples['logout_button'][1]),

    generate_prop_info('LogoutButton')
])

# Loading component
LoadingComponent = html.Div([
    html.H1('Loading Component'),

    reusable_components.Markdown('''
    Here’s a simple example that wraps the outputs for a couple of `Input` components in the `Loading` component. As you can see, you can define the type of spinner you would like to show (refer to the reference table below for all possible types of spinners).
    You can modify other attributes as well, such as `fullscreen=True` if you would like the spinner to be displayed fullscreen. Notice that, the Loading component traverses all
    of it's children to find a loading state, as demonstrated in the second callback, so that even nested children will get picked up.
    '''),

    Syntax(examples['loading_component'][0]),
    Example(examples['loading_component'][1]),
    reusable_components.Markdown('''
    Please also check out <dccLink href="/loading-states" children="this section on loading states"/> if you want a more customizable experience.
    '''),
    generate_prop_info('Loading')
])

# Location
Location = html.Div([
    html.H1('Location Component'),

    reusable_components.Markdown('''
    The location component represents the location bar in your web browser. Through its `href`, `pathname`,
    `search` and `hash` properties you can access different portions of your app's url.

    For example, given the url `http://127.0.0.1:8050/page-2?a=test#quiz`:

    - `href` = `"http://127.0.0.1:8050/page-2?a=test#quiz"`
    - `pathname` = `"/page-2"`
    - `search` = `"?a=test"`
    - `hash` = `"#quiz"`
    '''),

    generate_prop_info('Location')
])
