# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import styles
from datetime import datetime as dt
import dash
from textwrap import dedent as s

import tools
from utils.convert_props_to_table import generate_prop_table
from utils.component_block import ComponentBlock
from components import Syntax, Example

examples = {
    'date_picker_single': tools.load_example('tutorial/examples/core_components/date_picker_single.py'),
    'date_picker_range': tools.load_example('tutorial/examples/core_components/date_picker_range.py'),
    'dropdown': tools.load_example('tutorial/examples/core_components/dropdown.py'),
    'slider': tools.load_example('tutorial/examples/core_components/slider.py'),
    'slider-updatemode': tools.load_example('tutorial/examples/core_components/slider_updatemode.py'),
    'rangeslider': tools.load_example('tutorial/examples/core_components/rangeslider.py'),
    'rangeslider-nonlinear': tools.load_example('tutorial/examples/core_components/rangeslider_nonlinear.py'),
    'upload-image':  tools.load_example('tutorial/examples/core_components/upload-image.py'),
    'upload-datafile':  tools.load_example('tutorial/examples/core_components/upload-datafile.py'),
    'upload-gallery':  tools.load_example('tutorial/examples/core_components/upload-gallery.py'),
    'tabs_simple':  tools.load_example('tutorial/examples/core_components/tabs_simple.py'),
    'tabs_callback':  tools.load_example('tutorial/examples/core_components/tabs_callback_graph.py'),
}


# Dropdown
Dropdown = html.Div(children=[
    html.H1('Dropdown Examples and Reference'),
    html.Hr(),
    html.H3('Default Dropdown'),
    html.P("An example of a default dropdown without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['dropdown'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['dropdown'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3('Multi-Value Dropdown'),
    dcc.Markdown("A dropdown component with the `multi` property set to `True` \
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
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),

    html.H3('Disable Search'),
    dcc.Markdown("The `searchable` property is set to `True` by default on all \
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
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),

    html.H3('Dropdown Clear'),
    dcc.Markdown("The `clearable` property is set to `True` by default on all \
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
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),
    html.H3('Placeholder Text'),
    dcc.Markdown("The `placeholder` property allows you to define \
                 default text shown when no value is selected."),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    placeholder="Select a city",
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),
    html.H3('Disable Dropdown'),
    dcc.Markdown("To disable the dropdown just set `disabled=True`."),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    disabled=True
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),
    html.H3('Disable Options'),
    dcc.Markdown("To disable a particular option inside the dropdown \
                 menu, set the `disabled` property in the options."),
    ComponentBlock('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC', 'disabled': 'True'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF', 'disabled': 'True'}
    ],
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),
    html.H3("Dropdown Properties"),
    generate_prop_table('Dropdown')
])

# Slider
Slider = html.Div(children=[
    html.H1('Slider Examples and Reference'),
    html.Hr(),
    html.H3('Simple Slider Example'),
    html.P("An example of a basic slider tied to a callback."),
    dcc.SyntaxHighlighter(
        examples['slider'][0],
        customStyle=styles.code_container,
        language='python'
    ),

    html.Div(examples['slider'][1], className='example-container'),
    html.Hr(),
    html.H3('Marks and Steps'),
    dcc.Markdown("If slider `marks` are defined and `step` is set to `None` \
                 then the slider will only be able to select values that \
                 have been predefined by the `marks`. `marks` is a `dict` \
                 where the keys represent the numerical values and the \
                 values represent their labels."),
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
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),

    html.H3('Included and Styling Marks'),
    dcc.Markdown("By default, `included=True`, meaning the rail trailing the \
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
    dcc.Markdown("Create a logarithmic slider by setting the labels of the \
                 `marks` property \
                 to be logarithmic and adjusting the slider's output \
                 `value` in the callbacks. The `updatemode` property \
                 allows us to determine when we want a callback to be \
                 triggered. The following example has `updatemode='drag'` \
                 which means a callback is triggered everytime the handle \
                 is moved. The default setting is `mouseup` which triggers \
                 the callback when you release your mouse from the slider."),
    dcc.SyntaxHighlighter(
        examples['slider-updatemode'][0],
        customStyle=styles.code_container,
        language='python'
    ),
    html.Div(
        examples['slider-updatemode'][1],
        className='example-container',
        style={'overflow': 'hidden', 'padding': '20px'}
    ),
    html.Hr(),
    html.H3("Slider Properties"),
    generate_prop_table('Slider')
])

# RangeSlider
RangeSlider = html.Div(children=[
    html.H1("RangeSlider Examples and Reference"),
    html.Hr(),
    html.H3('Simple RangeSlider Example'),
    html.P("An example of a basic RangeSlider tied to a callback."),
    dcc.SyntaxHighlighter(
        examples['rangeslider'][0],
        customStyle=styles.code_container,
        language='python'
    ),

    html.Div(
        examples['rangeslider'][1],
        className='example-container',
        style={'overflow': 'hidden'}),

    html.Hr(),
    html.H3('Marks and Steps'),
    dcc.Markdown("If slider `marks` are defined and `step` is set to `None` \
                 then the slider will only be able to select values that \
                 have been predefined by the `marks`."),
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
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),

    html.H3('Included and Styling Marks'),
    dcc.Markdown("By default, `included=True`, meaning the rail trailing the \
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
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),

    html.H3('Multiple Handles'),
    dcc.Markdown('To create multiple handles \
                  just define more values for `value`!'),
    ComponentBlock('''import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=30,
    value=[1, 3, 4, 5, 12, 17]
)
    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.RangeSlider(
            min=0,
            max=30,
            value=[1, 3, 4, 5, 12, 17]
        ),
    ], className='example-container',
       style={'overflow': 'hidden'}),
    html.Hr(),
    html.H3('Pushable Handles'),
    dcc.Markdown("The `pushable` property is either a `boolean` or a numerical value. \
                The numerical value determines the minimum distance between \
                the handles. Try moving the handles around!"),
    ComponentBlock('''import dash_core_components as dcc
dcc.RangeSlider(
    min=0,
    max=30,
    value=[8, 10, 15, 17, 20],
    pushable=2
)
    ''', customStyle=styles.code_container, language='python'),
    html.Hr(),

    html.H3('Crossing Handles'),
    dcc.Markdown("If `allowCross=False`, the handles will not be allowed to\
                  cross over each other"),
    ComponentBlock('''import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=30,
    value=[10, 15],
    allowCross=False
)
    ''', customStyle=styles.code_container, language='python'),
    html.Hr(),

    html.H3('Non-Linear Slider and Updatemode'),
    dcc.Markdown("Create a logarithmic slider by setting `marks`\
                 to be logarithmic and adjusting the slider's output \
                 `value` in the callbacks. The `updatemode` property \
                 allows us to determine when we want a callback to be \
                 triggered. The following example has `updatemode='drag'` \
                 which means a callback is triggered everytime the handle \
                 is moved. \
                 Contrast the callback output with the first example on this \
                 page to see the difference."),
    dcc.SyntaxHighlighter(
        examples['rangeslider-nonlinear'][0],
        customStyle=styles.code_container,
        language='python'
    ),
    html.Div(examples['rangeslider-nonlinear'][1],
             className='example-container',
             style={'overflow': 'hidden', 'padding': '20px'}),
    html.Hr(),
    generate_prop_table('RangeSlider')
])


# Checklist
Checklist = html.Div(children=[
    html.H3('Checklist Properties'),
    generate_prop_table('Checklist')
])


# Input
Input = html.Div(children=[
    html.H3('Input Properties'),
    generate_prop_table('Input')
])


# RadioItems
RadioItems = html.Div(children=[
    html.H3('RadioItem Properties'),
    generate_prop_table('RadioItems')
])


# Markdown
Markdown = html.Div(children=[
    html.H1("Markdown Examples and Reference"),
    html.Hr(),
    html.H3("Syntax Guide"),
    dcc.Markdown("These examples are based on the \
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
[Dash User Guide](https://dash.plot.ly/)
''')"""),
    html.Hr(),
    html.H3("Inline Code"),
    html.P("Any block of text surrounded by ` ` will rendered as inline-code. "),

    ComponentBlock("""import dash_core_components as dcc

dcc.Markdown('''

Inline code snippet: `True`

Block code snippet:
```
import dash

app = dash.Dash()
```
''')

"""),

    html.Hr(),
    html.H3('Markdown Properties'),
    generate_prop_table('Markdown')
])

# DatePickerRange
DatePickerRange = html.Div(children=[
    html.H1("DatePickerRange Examples and Reference"),
    html.Hr(),
    html.H3("Simple DatePickerRange Example"),
    dcc.Markdown("This is a simple example of a `DatePickerRange` \
                 component tied to a callback. The `min_date_allowed` and \
                 `max_date_allowed` properties define the minimum and \
                 maximum selectable \
                 dates on the calendar while `initial_visible_month` defines \
                 the calendar month that is first displayed when the \
                 `DatePickerRange` component is opened."),
    dcc.SyntaxHighlighter(
        examples['date_picker_range'][0],
        language='python',
        customStyle=styles.code_container
    ),
    html.Div(
        examples['date_picker_range'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),
    html.Hr(),
    html.H3('Month and Display Format'),
    dcc.Markdown("The `display_format` property \
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
            html.Td(dcc.Markdown('`YYYY`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`2014`'), style={'text-align': 'left'}),
            html.Td('4 or 2 digit year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`YY`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`14`'), style={'text-align': 'left'}),
            html.Td('2 digit year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Y`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`-25`'), style={'text-align': 'left'}),
            html.Td('Year with any number of digits and sign')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Q`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1..4`'), style={'text-align': 'left'}),
            html.Td('Quarter of year. Sets month to first month in quarter.')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`M MM`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1..12`'), style={'text-align': 'left'}),
            html.Td('Month number')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`MMM MMMM`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`Jan..December`'), style={'text-align': 'left'}),
            html.Td('Month name')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`D DD`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1..31`'), style={'text-align': 'left'}),
            html.Td('Day of month')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Do`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1st..31st`'), style={'text-align': 'left'}),
            html.Td('Day of month with ordinal')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`DDD DDDD`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1..365`'), style={'text-align': 'left'}),
            html.Td('Day of year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`X`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1410715640.579`'), style={'text-align': 'left'}),
            html.Td('Unix timestamp')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`x`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1410715640579`'), style={'text-align': 'left'}),
            html.Td('Unix ms timestamp')
        ]),
    ], style={'margin': 'auto'}),
    html.Br(),
    html.H3("Display Format Examples"),
    dcc.Markdown("You can utilize any permutation of the string tokens \
                 shown in the table above to change how selected dates are \
                 displayed in the `DatePickerRange` component."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    end_date=dt.now(),
    display_format='MMM Do, YY',
    start_date_placeholder_text='MMM Do, YY'
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt
dcc.DatePickerRange(
    end_date=dt.now(),
    display_format='M-D-Y-Q',
    start_date_placeholder_text='M-D-Y-Q'
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    end_date=dt.now(),
    display_format='MMMM Y, DD',
    start_date_placeholder_text='MMMM Y, DD'
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    end_date=dt.now(),
    display_format='X',
    start_date_placeholder_text='X'
)''', language='python', customStyle=styles.code_container),

    html.Br(),

    html.H3("Month Format Examples"),
    dcc.Markdown("Similar to the `display_format`, you can set `month_format` \
                 to any permutation of the string tokens \
                 shown in the table above to change how calendar titles \
                 are displayed in the `DatePickerRange` component."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    month_format='MMM Do, YY',
    end_date_placeholder_text='MMM Do, YY',
    start_date=dt.now()
)'''),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    month_format='M-D-Y-Q',
    end_date_placeholder_text='M-D-Y-Q',
    start_date=dt.now()
)'''),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    month_format='MMMM Y',
    end_date_placeholder_text='MMMM Y',
    start_date=dt.now()
)'''),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    month_format='X',
    end_date_placeholder_text='X',
    start_date=dt.now()
)'''),

    html.Hr(),

    html.H3("Vertical Calendar and Placeholder Text"),
    dcc.Markdown("The `DatePickerRange` component can be rendered in two \
                  orientations, either horizontally or vertically. \
                  If `calendar_orientation` is set to `'vertical'`, it will \
                  be rendered vertically and will default to `'horizontal'` \
                  if not defined."),
    dcc.Markdown("The `start_date_placeholder_text` and \
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
    dcc.Markdown("The `minimum_nights` property defines the number of \
                  nights that must be in between the range of two \
                  selected dates."),
    dcc.Markdown("When the `clearable` property is set to `True` \
                  the component will be rendered with a small 'x' \
                  that will remove all selected dates when selected."),
    dcc.Markdown("The `DatePickerRange` component supports two different \
                  portal types, one being a full screen portal \
                  (`with_full_screen_portal`) and another being a simple \
                  screen overlay, like the one shown below (`with_portal`)."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    minimum_nights=5,
    clearable=True,
    with_portal=True,
    start_date=dt.now()
)'''),

    html.Hr(),

    html.H3("Right to Left Calendars and First Day of Week"),
    dcc.Markdown("When the `is_RTL` property is set to `True` \
                  the calendar will be rendered from right to left."),
    dcc.Markdown("The `first_day_of_week` property allows you to \
                  define which day of the week will be set as the first \
                  day of the week. In the example below, Tuesday is \
                  the first day of the week."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    is_RTL=True,
    first_day_of_week=3,
    start_date=dt.now()
)''', language='python', customStyle=styles.code_container),
    html.Hr(),
    html.H3('DatePickerRange Properties'),
    generate_prop_table('DatePickerRange')
])

# DatePickerSingle
DatePickerSingle = html.Div(children=[
    html.H1("DatePickerSingle Examples and Reference"),
    html.Hr(),
    html.H3("Simple DatePickerSingle Example"),
    dcc.Markdown("This is a simple example of a `DatePickerSingle` \
                 component tied to a callback. The `min_date_allowed` and \
                 `max_date_allowed` properties define the minimum and \
                 maximum selectable \
                 dates on the calendar while `initial_visible_month` defines \
                 the calendar month that is first displayed when the \
                 `DatePickerSingle` component is opened."),
    dcc.SyntaxHighlighter(
        examples['date_picker_single'][0],
        language='python',
        customStyle=styles.code_container
    ),
    html.Div(
        examples['date_picker_single'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),

    html.H3('Month and Display Format'),
    dcc.Markdown("The `display_format` property \
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
            html.Td(dcc.Markdown('`YYYY`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`2014`'), style={'text-align': 'left'}),
            html.Td('4 or 2 digit year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`YY`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`14`'), style={'text-align': 'left'}),
            html.Td('2 digit year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Y`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`-25`'), style={'text-align': 'left'}),
            html.Td('Year with any number of digits and sign')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Q`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1..4`'), style={'text-align': 'left'}),
            html.Td('Quarter of year. Sets month to first month in quarter.')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`M MM`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1..12`'), style={'text-align': 'left'}),
            html.Td('Month number')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`MMM MMMM`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`Jan..December`'), style={'text-align': 'left'}),
            html.Td('Month name')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`D DD`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1..31`'), style={'text-align': 'left'}),
            html.Td('Day of month')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Do`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1st..31st`'), style={'text-align': 'left'}),
            html.Td('Day of month with ordinal')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`DDD DDDD`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1..365`'), style={'text-align': 'left'}),
            html.Td('Day of year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`X`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1410715640.579`'), style={'text-align': 'left'}),
            html.Td('Unix timestamp')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`x`'), style={'text-align': 'left'}),
            html.Td(dcc.Markdown('`1410715640579`'), style={'text-align': 'left'}),
            html.Td('Unix ms timestamp')
        ]),
    ], style={'margin': 'auto'}),

    html.Br(),

    html.H3("Display Format Examples"),
    dcc.Markdown("You can utilize any permutation of the string tokens \
                 shown in the table above to change how selected dates are \
                 displayed in the `DatePickerSingle` component."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    date=dt.now(),
    display_format='MMM Do, YY'
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    date=dt.now(),
    display_format='M-D-Y-Q',
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    date=dt.now(),
    display_format='MMMM Y, DD'
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    date=dt.now(),
    display_format='X',
)''', language='python', customStyle=styles.code_container),
    html.Br(),
    html.H3("Month Format Examples"),
    dcc.Markdown("Similar to the `display_format`, you can set `month_format` \
                 to any permutation of the string tokens \
                 shown in the table above to change how calendar titles \
                 are displayed in the `DatePickerSingle` component."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    month_format='MMM Do, YY',
    placeholder='MMM Do, YY',
    date=dt.now()
)'''),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    month_format='M-D-Y-Q',
    placeholder='M-D-Y-Q',
    date=dt.now()
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    month_format='MMMM Y',
    placeholder='MMMM Y',
    date=dt.now()
)'''),

    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    month_format='X',
    placeholder='X',
    date=dt.now()
)''', language='python', customStyle=styles.code_container),
    html.Hr(),
    html.H3("Vertical Calendar and Placeholder Text"),
    dcc.Markdown("The `DatePickerSingle` component can be rendered in two \
                  orientations, either horizontally or vertically. \
                  If `calendar_orientation` is set to `'vertical'`, it will \
                  be rendered vertically and will default to `'horizontal'` \
                  if not defined."),
    dcc.Markdown("The `placeholder` defines the grey default \
                  text defined in the calendar input boxes when no date is \
                  selected."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    calendar_orientation='vertical',
    placeholder='Select a date',
    date=dt.now()
)'''),

    html.Hr(),

    html.H3("Calendar Clear and Portals"),
    dcc.Markdown("When the `clearable` property is set to `True` \
                  the component will be rendered with a small 'x' \
                  that will remove all selected dates when selected."),
    dcc.Markdown("The `DatePickerSingle` component supports two different \
                  portal types, one being a full screen portal \
                  (`with_full_screen_portal`) and another being a simple \
                  screen overlay, like the one shown below (`with_portal`)."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    clearable=True,
    with_portal=True,
    date=dt.now()
)'''),

    html.Hr(),

    html.H3("Right to Left Calendars and First Day of Week"),
    dcc.Markdown("When the `is_RTL` property is set to `True` \
                  the calendar will be rendered from right to left."),
    dcc.Markdown("The `first_day_of_week` property allows you to \
                  define which day of the week will be set as the first \
                  day of the week. In the example below, Tuesday is \
                  the first day of the week."),
    ComponentBlock('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    is_RTL=True,
    first_day_of_week=3,
    date=dt.now()
)'''),

    html.Hr(),
    html.H3('DatePickerSingle Properties'),
    generate_prop_table('DatePickerSingle')
])

# Link
Link = html.Div(children=[
    html.H3('Link Example'),
    dcc.Markdown('To learn more about links, see the chapter on [Dash URLs](/urls)'),
    html.H3('Link Properties'),
    generate_prop_table('Link')
])

# Textarea
Textarea = html.Div(children=[
    html.H3('Textarea Properties'),
    generate_prop_table('Textarea')
])

# Tabs
Tabs = html.Div(children=[
    html.H1('Tabs Examples and Reference'),
    html.H2('Method 1. Content as Callback'),
    dcc.Markdown(s('''
    The `Tab` component controls the style and value of the individual tab
    and the `Tabs` component hold a collection of `Tab` components.
    Attach a callback to the Tabs `value` prop and update a container's `children`
    property in your callback.
    ''')),
    dcc.SyntaxHighlighter(
        examples['tabs_callback'][0],
        customStyle=styles.code_container
    ),
    html.Div(examples['tabs_callback'][1], className='example-container'),
    dcc.Markdown(s('''
    In the example above, our callback contains all of the content. In practice,
    we'll keep the tab's content in separate files and import the data.
    For an example, see the [URLs and Multi-Page App Tutorial](/urls).
    ''')),

    html.H2('Method 2. Content as Tab Children'),
    dcc.Markdown(s('''
    Instead of displaying the content through a callback, you can embed the content
    directly as the `children` property in the `Tab` component:
    ''')),

    dcc.SyntaxHighlighter(
        examples['tabs_simple'][0],
        customStyle=styles.code_container
    ),
    html.Div(examples['tabs_simple'][1], className='example-container'),
    dcc.Markdown(s('''
    Note that this method has a couple of drawbacks:
    - It requires that you compute the children property for each individual
    tab _upfront_ and send all of the tab's content over the network _at once_.
    The callback method allows you to compute the tab's content _on the fly_
    (that is, when the tab is clicked).
    - There have been some bug reports that graphs are not getting resized
    properly if this method is being used. See [dash-core-components#256](https://github.com/plotly/dash-core-components/issues/256)
    for more details.
    - The second tab, instead of the first tab, is selected by default.
    This is a bug and will be fixed. Track our progress in  [dash-core-components#262](https://github.com/plotly/dash-core-components/issues/262).
    ''')),

    html.Hr(),

    html.H3('Tabs properties'),
    generate_prop_table('Tabs'),
    html.H3('Tab properties'),
    generate_prop_table('Tab')
])

# Upload
Upload = html.Div([
    html.H1('Upload Component'),
    dcc.Markdown(s('''
    The Dash upload component allows your app's veiwers to upload files,
    like excel spreadsheets or images, into your application.
    Your Dash app can access the contents of an upload by listening to
    the `contents` property of the `dcc.Upload` component.

    `contents` is a base64 encoded string that contains the files contents,
    no matter what type of file: text files, images, zip files,
    excel spreadsheets, etc.

    ''')),

    Syntax(examples['upload-datafile'][0], summary=dcc.Markdown(s('''
        Here's an example that parses CSV or Excel files and displays
        the results in a table. Note that this example uses the
        `DataTable` prototype from the
        [dash-table-experiments](https://github.com/plotly/dash-table-experiments)
        project.
    '''))),

    Example(examples['upload-datafile'][1]),

    html.Hr(),

    Syntax(examples['upload-image'][0], summary=dcc.Markdown(s('''
        This next example responds to image uploads by displaying them
        in the app with the `html.Img` component.
    '''))),
    Example(examples['upload-image'][1]),

    Syntax(examples['upload-gallery'][0], summary=dcc.Markdown(s('''
        The `children` attribute of the `Upload` component accepts any
        Dash component. Clicking on the children element will trigger the
        upload action, as will dragging and dropping files.
        Here are a few different ways that you could style the upload
        component using standard dash components.
    '''))),
    Example(examples['upload-gallery'][1]),

    html.Hr(),

    html.H2('Upload Component Properties'),
    generate_prop_table('Upload')
])
