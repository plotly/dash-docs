# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import os as _os
import json
import dash as _dash
import pandas as pd
import styles
from datetime import datetime as dt
import dash

_current_path = _os.path.join(_os.path.dirname(_os.path.abspath(dcc.__file__)),
                              'metadata.json')

def js_to_py_type(type_object):
    js_type_name = type_object['name']

    if js_type_name == 'shape' and 'number' in type_object['value']:
        print(type_object)
    # wrapping everything in lambda to prevent immediate execution
    js_to_py_types = {
        'array': lambda: 'list',
        'bool': lambda: 'boolean',
        'number': lambda: 'number',
        'string': lambda: 'string',
        'object': lambda: 'dict',

        'any': lambda: 'boolean | number | string | dict | list',
        'element': lambda: 'dash component',
        'node': lambda: (
            'a list of or a singular dash component, string or number'
        ),

        # React's PropTypes.oneOf
        'enum': lambda: 'a value equal to: {}'.format(', '.join([
            '{}'.format(str(t['value'])) for t in type_object['value']
        ])),

        # React's PropTypes.oneOfType
        'union': lambda: '{}'.format(' | '.join([
            '{}'.format(js_to_py_type(subType))
            for subType in type_object['value'] if js_to_py_type(subType) != ''
        ])),

        # React's PropTypes.arrayOf
        'arrayOf': lambda: 'list {}'.format(
            'of {}'.format(js_to_py_type(type_object['value']))
            if (js_to_py_type(type_object['value']) != '')
            else ''
        ),

        # React's PropTypes.objectOf
        'objectOf': lambda: (
            'dict with strings as keys and values of type {}'
        ).format(js_to_py_type(type_object['value'])),


        # React's PropTypes.shape
        'shape': lambda: (
            'dict containing key(s) {}\n{}'.format(
                ', '.join(
                    ["'{}'".format(t) for t in list(type_object['value'].keys())]
                ),
                '\n. Those keys have the following types: \n{}'.format(
                    '\n'.join([
                        '  - ' + argument_doc(
                            prop_name,
                            prop,
                            prop.get('description', '')
                        ) for
                        prop_name, prop in list(type_object['value'].items())
                    ])
                )
            )
        )
    }

    if 'computed' in type_object and type_object['computed']:
        return ''
    if js_type_name in js_to_py_types:
        return js_to_py_types[js_type_name]()
    else:
        return ''


def argument_doc(arg_name, type_object, description):
    js_type_name = type_object['name']
    py_type_name = js_to_py_type(type_object)

    if '\n' in py_type_name:
        return (
            '{name}: {description}. '
            '{name} has the following type: {type}'
        ).format(
            name=arg_name,
            type=py_type_name,
            description=description
        )
    else:
        return '{name} ({type}){description}'.format(
            name=arg_name,
            type='{}'.format(py_type_name) if py_type_name else '',
            description=(
                ': {}'.format(description) if description != '' else ''
            )
        )


# object_hook_handler allows the user to define a
# specific method of parsing
# in this case we remove unneeded elements and format
# property types to display in a html.Table
def object_hook_handler(obj):
    if 'required' in obj:
        obj.pop('required')
    if 'id' in obj:
        obj['id']['Description'] = "Optional identifier used to reference\
                              component in callbacks"
    if 'className' in obj:
        obj['className']['Description'] = '''Sets the class name of the element (the value of an
                                             element's html class attribute)'''
    if 'type' in obj and obj['type'] != None and 'name' in obj['type']:
        obj['Type'] = js_to_py_type(obj['type'])
    if 'defaultValue' in obj:
        if(obj['defaultValue']['value'] == 'true'):
            obj['defaultValue']['value'] = 'True'
        elif(obj['defaultValue']['value'] == 'false'):
            obj['defaultValue']['value'] = 'False'
        elif(type(obj['defaultValue']['value']) == dict):
            obj['defaultValue']['value'] = 'Checkout plotly.js docs for\
                                            more info'
        obj['Default Value'] = obj['defaultValue']['value']
        obj.pop('defaultValue')
    if 'description' in obj:
        obj['Description'] = obj['description']
        obj.pop('description')
    return obj


with open(_current_path, 'r') as f:
    metadata = json.load(f, object_hook=object_hook_handler)


def get_dataframe(string):
    prefix = 'src/components/'
    suffix = '.react.js'
    fullString = prefix+string+suffix
    df = pd.DataFrame(metadata[fullString]
                              ['props']).transpose()
    if('dashEvents' in df.index.tolist()):
        df.drop(['dashEvents'], inplace=True)
    if('fireEvent' in df.index):
        df.drop(['fireEvent'], inplace=True)
    if('setProps' in df.index):
        df.drop(['setProps'], inplace=True)
    if('dashFireEvent' in df.index):
        df.drop(['dashFireEvent'], inplace=True)
    if('className' in df.index.tolist()):
        reindex = ['id', 'className']
    else:
        reindex = ['id']
    reindex.extend(df.loc[(df.index != 'id') &
                          (df.index != 'className')].index.tolist())
    df['Props'] = df.index
    df = df.reindex(reindex)
    df.fillna('N/A', inplace=True)
    if('Default Value' in df.columns.values.tolist()):
        df = df[['Props', 'Description', 'Type', 'Default Value']]
    else:
        df = df[['Props', 'Description', 'Type']]

    if('config' in df['Props']):
        df.set_value('config', 'Type',
                     "Check Plotly.js docs for more information")
        df.set_value('config', 'Default Value',
                     "dict")
    return df


def generate_table(dataframe):
    rows = []
    for i in range(len(dataframe)):
        internalRow = []
        for col in dataframe.columns:
            # Body
            if(type(dataframe.iloc[i][col]) == tuple and
               type(dataframe.iloc[i][col][1][0]) != dict):
                internalRow.append(html.Td(dataframe.iloc[i][col][0] + ': ' +
                                   str([str(j) for j in dataframe.iloc[i][col]
                                                                      [1]])))
            elif(type(dataframe.iloc[i][col]) == tuple and
                 type(dataframe.iloc[i][col][1][0]) == dict):
                internalRow.append(html.Td("Array of Dict: " +
                                           str(dataframe.iloc[i][col][1])))
            else:
                if(col == 'Props'):
                    internalRow.append(html.Td(dcc.Markdown('`' +
                                       dataframe.iloc[i][col] + '`'),
                                       style={'text-align': 'center'}))
                elif(col == 'Description'):
                    internalRow.append(html.Td(dataframe.iloc[i][col],
                                       style={'font-size': '0.95em'}))
                else:
                    internalRow.append(html.Td(dataframe.iloc[i][col]))
        rows.append(html.Tr(internalRow))
    table = html.Table(
            [html.Tr([html.Th(col, style={'text-align': 'center'}) for col in
                     dataframe.columns])] + rows)

    return table


# Dropdown
Dropdown = html.Div(children=[
    html.H2('Dropdown Examples and Reference'),
    html.Hr(),
    html.H4('Default Dropdown'),
    html.P("An example of a default dropdown without \
            any extra properties."),
    dcc.SyntaxHighlighter('''import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
       value='NYC'
    ),
    html.Div(id='output-container')
)

@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
       value='NYC'
    ),
    html.Div(id='output-container-dropdown'),

    html.Hr(),
    html.H4('Multi-Value Dropdown'),
    dcc.Markdown("A dropdown component with the `multi` property set to `True` \
                  will allow the user to select more than one value \
                  at a time."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['MTL', 'NYC'],
    multi=True
)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
        id='multi-value',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'NYC'],
        multi=True
    ),
    html.Hr(),

    html.H4('Disable Search'),
    dcc.Markdown("The `searchable` property is set to `True` by default on all \
            `Dropdown`s. To prevent searching the dropdown \
            value, just set the `searchable` property to `False`. \
            Try searching for 'New York' on this dropdown below and compare \
            it to the other dropdowns on the page to see the difference."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    searchable=False
)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        searchable=False
    ),
    html.Hr(),

    html.H4('Dropdown Clear'),
    dcc.Markdown("The `clearable` property is set to `True` by default on all \
            `Dropdown`s. To prevent the clearing of the selected dropdwon \
            value, just set the `clearable` property to `False`"),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'},
    ],
    value='MTL',
    clearable=False
)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
        id='clearable',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
        value='MTL',
        clearable=False
    ),

    html.Hr(),
    html.H4('Placeholder Text'),
    dcc.Markdown("The `placeholder` property allows you to define \
                 default text shown when no value is selected."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    placeholder="Select a value!",
)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        placeholder="Select a value!",
    ),

    html.Hr(),
    html.H4('Disable Dropdown'),
    dcc.Markdown("To disable the dropdown just set `disabled=True`."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    disabled=True
)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        disabled=True
    ),

    html.Hr(),
    html.H4('Disable Options'),
    dcc.Markdown("To disable certain options displayed inside the dropdown \
                 menu. Just set define the `disabled` property in the options \
                 declaration."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC', 'disabled': 'True'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF', 'disabled': 'True'}
    ],
)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC', 'disabled': 'True'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF', 'disabled': 'True'}
        ],
    ),

    html.Div(id='hidden-div', style={'display': 'none'}),
    html.Hr(),
    html.H4("Dropdown Properties"),
    generate_table(get_dataframe('Dropdown'))
])

# Slider
Slider = html.Div(children=[
    html.H3('Slider Examples and Reference'),
    html.Hr(),
    html.H4('Simple Slider Example'),
    html.P("An example of a basic slider tied to a callback."),
    dcc.SyntaxHighlighter('''import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.layout = html.Div([
    dcc.Slider(
        id='my-slider',
        min=0,
        max=20,
        step=0.5,
        value=10,
    ),
    html.Div(id='output-container')
)

@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)

    ''', customStyle=styles.code_container, language='python'),

    html.Div([
        dcc.Slider(
            id='my-slider',
            min=0,
            max=20,
            step=0.5,
            value=10
        ),
    ], className='example-container'),
    html.Div(id='output-container-slider'),
    html.Hr(),
    html.H4('Marks and Steps'),
    dcc.Markdown("If slider `marks` are defined and `step` is set to `None` \
                 then the slider will only be able to select values that \
                 have been predefined by the `marks`."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=10,
    step=None,
    marks={
        0: 0,
        3: 3,
        5: 5,
        7.65: 7.65,
        10: 10
    }
)

    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.Slider(
            min=0,
            max=10,
            step=None,
            marks={
                0: 0,
                3: 3,
                5: 5,
                7.65: 7.65,
                10: 10
            }
        )
    ], className='example-container',
        style={'overflow': 'hidden', 'padding': '20px'}),
    html.Hr(),

    html.H4('Included and Styling Marks'),
    dcc.Markdown("By default, `included=True`, meaning the rail trailing the \
                 handle will be highlighted. To have the handle act as a \
                 discrete value set `included=False`. To style `marks`, \
                 include a style css attribute alongside the key value."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Markdown('`included=True`'),
# Slider has included=True by default
dcc.Slider(
    min=0,
    max=100,
    value=65,
    marks={
        0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26°C'},
        37: {'label': '37°C'},
        100: {'label': '100°C', 'style': {'color': '#f50'}}
    }
),

dcc.Markdown('`included==False`'),
dcc.Slider(
    min=0,
    max=100,
    value=37,
    marks={
        0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26°C'},
        37: {'label': '37°C'},
        100: {'label': '100°C', 'style': {'color': '#f50'}}
    },
    included=False
)

    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.Markdown('`included=True`'),
        dcc.Slider(
            min=0,
            max=100,
            value=65,
            marks={
                0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
                26: {'label': '26°C'},
                37: {'label': '37°C'},
                100: {'label': '100°C', 'style': {'color': '#f50'}}
            }
        )
    ], className='example-container',
        style={
            'overflow': 'hidden',
            'padding': '10px 20px 30px 20px',
            'font-weight': 'bolder'
            }),
    html.Div([
        dcc.Markdown('`included=False`'),
        dcc.Slider(
            min=0,
            max=100,
            value=37,
            marks={
                0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
                26: {'label': '26°C'},
                37: {'label': '37°C'},
                100: {'label': '100°C', 'style': {'color': '#f50'}}
            },
            included=False
        )
    ], className='example-container',
        style={
            'overflow': 'hidden',
            'padding': '10px 20px 30px 20px',
            'font-weight': 'bolder'
            }),
    html.Hr(),
    html.H4('Non-Linear Slider and Updatemode'),
    dcc.Markdown("Dash doesn't natively support non-linear sliders but you\
                 can recreate a logarithmic slider by setting `marks`\
                 to be logarithmic and adjusting the slider's output \
                 `value` in the callbacks. The `updatemode` property \
                 allows us to determine when we want a callback to be \
                 triggered. The following example has `updatemode='drag'` \
                 which means a callback is triggered everytime the handle \
                 is moved. \
                 Contrast the callback output with the first example on this \
                 page to see the difference."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import *
import dash

app = dash.Dash('')

# Use the following function when accessing the value of 'my-slider'
# in callbacks to transorm the output value to logarithmic
def transform_value(value):
    return 10 ** value

app.layout = html.Div([
    dcc.Slider(
        id='my-slider',
        marks={(i): '{}'.format(10 ** i) for i in range(4)},
        max=3,
        value=2,
        step=0.01,
        updatemode='drag'
    ),
    html.Div(id='output-container')
])

@app.callback(Output('output-container', 'children'),
              [Input('my-slider', 'value')])
def display_value(value):
    return 'Linear Value: {} | \
            Log Value: {:0.2f}'.format(value, transform_value(value))

    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.Slider(
            id='non-linear-slider',
            marks={(i): '{}'.format(10 ** i) for i in range(4)},
            max=3,
            value=2,
            step=0.01,
            updatemode='drag'
        )
    ], className='example-container',
        style={'overflow': 'hidden', 'padding': '20px'}),
    html.Div(id='output-container-slider-non-linear'),
    html.Hr(),
    html.H4("Slider Properties"),
    generate_table(get_dataframe('Slider'))
])

# RangeSlider
RangeSlider = html.Div(children=[
    html.H2("RangeSlider Examples and Reference"),
    html.Hr(),
    html.H4('Simple RangeSlider Example'),
    html.P("An example of a basic RangeSlider tied to a callback."),
    dcc.SyntaxHighlighter('''import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.layout = html.Div([
    dcc.RangeSlider(
        id='my-range-slider',
        min=0,
        max=20,
        step=0.5,
        value=[5, 15]
    ),
    html.Div(id='output-container-range-slider')
)

@app.callback(
    dash.dependencies.Output('output-container-range-slider', 'children'),
    [dash.dependencies.Input('my-range-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)

    ''', customStyle=styles.code_container, language='python'),

    html.Div([
        dcc.RangeSlider(
            id='my-range-slider',
            min=0,
            max=20,
            step=0.5,
            value=[5, 15]
        ),
    ], className='example-container',
       style={'overflow': 'hidden'}),
    html.Div(id='output-container-range-slider'),
    html.Hr(),
    html.H4('Marks and Steps'),
    dcc.Markdown("If slider `marks` are defined and `step` is set to `None` \
                 then the slider will only be able to select values that \
                 have been predefined by the `marks`."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=10,
    step=None,
    marks={
        0: 0,
        3: 3,
        5: 5,
        7.65: 7.65,
        10: 10
    },
    value=[3, 7.65]
)

    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.RangeSlider(
            min=0,
            max=10,
            step=None,
            marks={
                0: 0,
                3: 3,
                5: 5,
                7.65: 7.65,
                10: 10
            },
            value=[3, 7.65]
        )
    ], className='example-container',
        style={'overflow': 'hidden', 'padding': '20px 10px 30px 20px'}),
    html.Hr(),
    html.H4('Included and Styling Marks'),
    dcc.Markdown("By default, `included=True`, meaning the rail trailing the \
                 handle will be highlighted. To have the handle act as a \
                 discrete value set `included=False`. To style `marks`, \
                 include a style css attribute alongside the key value."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

    dcc.Markdown('`included=True`'),
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
    ),

    dcc.Markdown('`included==False`'),
    dcc.RangeSlider(
        min=0,
        max=100,
        value=[37, 65, 75],
        marks={
            0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
            26: {'label': '26°C'},
            37: {'label': '37°C'},
            100: {'label': '100°C', 'style': {'color': '#f50'}}
        },
    included=False
    )

    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.Markdown('`included=True`'),
        dcc.RangeSlider(
            min=0,
            max=100,
            value=[65, 87],
            marks={
                0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
                26: {'label': '26°C'},
                37: {'label': '37°C'},
                100: {'label': '100°C', 'style': {'color': '#f50'}}
            }
        )
    ], className='example-container',
        style={
            'overflow': 'hidden',
            'padding': '10px 20px 30px 20px',
            'font-weight': 'bolder'
            }),
    html.Div([
        dcc.Markdown('`included=False`'),
        dcc.RangeSlider(
            min=0,
            max=100,
            value=[37, 46, 75],
            marks={
                0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
                26: {'label': '26°C'},
                37: {'label': '37°C'},
                100: {'label': '100°C', 'style': {'color': '#f50'}}
            },
            included=False
        )
    ], className='example-container',
        style={
            'overflow': 'hidden',
            'padding': '10px 20px 30px 20px',
            'font-weight': 'bolder'
            }),
    html.Hr(),
    html.H4('Multiple Handles'),
    dcc.Markdown('To create multiple handles \
                  just define more values for `value`!'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

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
    html.H4('Pushable Handles'),
    dcc.Markdown("The `pushable` property can take on two different \
                sets of values. \
                Either a `bool` or a numerical value. \
                Try moving the handles around! The numerical value determines \
                the minimum distance between the handles before they get \
                pushed."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
dcc.RangeSlider(
    min=0,
    max=30,
    value=[8, 10, 15, 17, 20],
    pushable=2
)
    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.RangeSlider(
            min=0,
            max=30,
            value=[8, 10, 15, 17, 20],
            pushable=2
        ),
    ], className='example-container',
       style={'overflow': 'hidden'}),
    html.Hr(),
    html.H4('Crossing Handles'),
    dcc.Markdown("If `allowCross=False`, the handles will not be allowed to\
                  cross over each other"),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=30,
    value=[10, 15],
    allowCross=False
)
    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.RangeSlider(
            min=0,
            max=30,
            value=[10, 15],
            allowCross=False
        ),
    ], className='example-container',
        style={'overflow': 'hidden'}),
    html.Hr(),
    html.H4('Non-Linear Slider and Updatemode'),
    dcc.Markdown("Dash doesn't natively support non-linear sliders but you\
                 can recreate a logarithmic slider by setting `marks`\
                 to be logarithmic and adjusting the slider's output \
                 `value` in the callbacks. The `updatemode` property \
                 allows us to determine when we want a callback to be \
                 triggered. The following example has `updatemode='drag'` \
                 which means a callback is triggered everytime the handle \
                 is moved. \
                 Contrast the callback output with the first example on this \
                 page to see the difference."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import *
import dash

app = dash.Dash('')

# Use the following function when accessing the value of 'my-range-slider'
# in callbacks to transorm the output value to logarithmic
def transform_value(value):
    if(type(value) == list):
        valueList = []
        for i in value:
            valueList.append(10 ** i)
        return valueList
    else:
        return 10 ** value

app.layout = html.Div([
    dcc.RangeSlider(
        id='non-linear-range-slider',
        marks={(i): '{}'.format(10 ** i) for i in range(4)},
        max=3,
        value=[0.1, 2],
        dots=False,
        step=0.01,
        updatemode='drag'
    ),
    html.Div(id='output-container')
])

@app.callback(
    Output('output-container-range-slider-non-linear', 'children'),
    [Input('non-linear-range-slider', 'value')])
def update_output(value):
    transformed_value=transform_value(value)
    return 'Linear Value: [{}, {}] |
            Log Value: [{:0.2f}, {:0.2f}]'.format(value[0], value[1],
                                       transformed_value[0],
                                       transformed_value[1])

    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.RangeSlider(
            id='non-linear-range-slider',
            marks={(i): '{}'.format(10 ** i) for i in range(4)},
            max=3,
            value=[0.1, 2],
            dots=False,
            step=0.01,
            updatemode='drag'
        )
    ], className='example-container',
        style={'overflow': 'hidden', 'padding': '20px'}),
    html.Div(id='output-container-range-slider-non-linear'),
    html.Hr(),
    generate_table(get_dataframe('RangeSlider'))
])


# Checklist
Checklist = html.Div(children=[
    html.H3('Checklist Properties'),
    generate_table(get_dataframe('Checklist'))
])


# Input
Input = html.Div(children=[
    html.H3('Input Properties'),
    generate_table(get_dataframe('Input'))
])


# RadioItems
RadioItems = html.Div(children=[
    html.H3('RadioItem Properties'),
    generate_table(get_dataframe('RadioItems'))
])


# Markdown
Markdown = html.Div(children=[
    html.H2("Markdown Examples and Reference"),
    html.Hr(),
    html.H3("Syntax Guide"),
    dcc.Markdown("These examples are based on the \
    [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)."),
    html.Br(),
    html.H4("Headers"),
    dcc.Markdown('''

> \# This is an <h1> tag
>
> \## This is an <h2> tag
>
> \###### This is an <h6> tag
'''),
    html.H4("Emphasis"),
    dcc.Markdown('''
>\*This text will be italic*
>
>\_This will also be italic_
>
>
>\**This text will be bold**
>
>\__This will also be bold__
>
>
>\_You \**can** combine them_
'''),
    html.Hr(),
    html.H3("Lists"),
    html.H4("Unordered"),
    dcc.Markdown('''
>\* Item 1
>
>\* Item 2
>
>  &nbsp;&nbsp;&nbsp; \* Item 2a
>
>  &nbsp;&nbsp;&nbsp; \* Item 2b

Renders as:
* Item 1
* Item 2
  * Item 2a
  * Item 2b
'''),
    html.H4("Unordered"),
    dcc.Markdown('''
>1\. Item 1
>
>1\. Item 2
>
>1\. Item 3
>
>   &nbsp;&nbsp;&nbsp; 1. Item 3a
>
>   &nbsp;&nbsp;&nbsp; 1. Item 3b

Renders as:
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b
'''),
    html.Hr(),
    html.H3("Block Quotes"),
    dcc.Markdown('''
>
> \>
>
> \> Block quotes are a great way to highlight a certain block of text!
>
> \>
>

Renders as:
>
> Block quotes are a great way to highlight a certain block of text!
>

'''),
    html.Hr(),
    html.H3("Images"),
    dcc.Markdown('''
>![Dash Logo]\(/images/logo.png)
>
>Format: ![Alt Text]\(url)
'''),
    html.Hr(),
    html.H3("Links"),
    dcc.Markdown('''
> https://plot.ly/dash/ - automatic!
>
>\[Dash User Guide](https://plot.ly/dash/)
'''),
    html.Hr(),
    html.H3("Inline Code"),
    html.P("Any block of text surronded by ` ` will rendered as inline-code"),
    dcc.Markdown("`Markdown` is awesome! Try it out!"),
    dcc.Markdown('''To insert code block, and utilize syntax highlighting,
              use the `dcc.SyntaxHighlighter` component. See an example of
              how it works in the Dash User Guide [here](https://github.com/plotly/dash-docs/blob/378fe7cfec89616470ad3c7de16a43eee0298631/tutorial/core_components.py#L61)
              .'''),
    html.H3('Markdown Properties'),
    generate_table(get_dataframe('Markdown'))
])


# Graph
Graph = html.Div(children=[
    html.H2('Graph Reference Guide'),
    html.Hr(),
    html.H4('Graph Properties'),
    generate_table(get_dataframe('Graph'))
])


# DatePickerRange
DatePickerRange = html.Div(children=[
    html.H2("DatePickerRange Examples and Reference"),
    html.Hr(),
    html.H4("Simple DatePickerRange Example"),
    dcc.Markdown("The following is a simple example of a `DatePickerRange` \
                 component tied to a callback. The `min_date_allowed` and \
                 `max_date_allowed` properties define the minimum and \
                 maximum selectable \
                 dates on the calender while `initial_visible_month` defines \
                 the calendar month that is first displayed when the \
                 `DatePickerRange` component is opened."),
    dcc.SyntaxHighlighter('''import dash
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt

app = dash.Dash()
app.layout = html.Div([
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2017, 9, 19),
        initial_visible_month=dt(2017, 8, 5),
        end_date=dt(2017, 8, 25)
    ),
    html.Div(id='output-container-date-picker-range')
)


@app.callback(
    dash.dependencies.Output(
        'output-container-date-picker-range', 'children'
    ),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_output(start_date, end_date):
    string_prefix = "You have selected: "
    if start_date is not None:
        start_date = dt.strptime(start_date, '%Y-%m-%d')
        start_date_string = start_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + "Start Date: " + start_date_string + " | "
    if end_date is not None:
        end_date = dt.strptime(end_date, '%Y-%m-%d')
        end_date_string = end_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + "End Date: " + end_date_string
    if(len(string_prefix) == len("You have selected: ")):
        return "Select a date to see it displayed here"
    else:
        return string_prefix

if __name__ == '__main__':
    app.run_server(debug=True)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2017, 9, 19),
        initial_visible_month=dt(2017, 8, 5),
        end_date=dt(2017, 8, 25)
    ),
    html.Div(id='output-container-date-picker-range'),
    html.Hr(),
    html.H3('Month and Display Format'),
    dcc.Markdown("The `display_format` property \
                 determines how selected dates are displayed \
                 in the `DatePickerRange` component. The `month_format` \
                 property determines how calendar headers are displayed when \
                 the calendar is opened."),
    html.P("Both of these properties are specified through \
            strings that utilize a combination of any \
            of the following tokens."),
    html.Table([
        html.Tr([
            html.Th('String Token', style={'text-align': 'center', 'width': '20%'}),
            html.Th('Example', style={'text-align': 'center', 'width': '20%'}),
            html.Th('Description', style={'text-align': 'center', 'width': '40%'})
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`YYYY`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`2014`'), style={'text-align': 'left'}),
            html.Td('4 or 2 digit year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`YY`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`14`'), style={'text-align': 'left'}),
            html.Td('2 digit year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Y`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`-25`'), style={'text-align': 'left'}),
            html.Td('Year with any number of digits and sign')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Q`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1..4`'), style={'text-align': 'left'}),
            html.Td('Quarter of year. Sets month to first month in quarter.')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`M MM`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1..12`'), style={'text-align': 'left'}),
            html.Td('Month number')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`MMM MMMM`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`Jan..December`'), style={'text-align': 'left'}),
            html.Td('Month name')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`D DD`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1..31`'), style={'text-align': 'left'}),
            html.Td('Day of month')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Do`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1st..31st`'), style={'text-align': 'left'}),
            html.Td('Day of month with ordinal')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`DDD DDDD`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1..365`'), style={'text-align': 'left'}),
            html.Td('Day of year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`X`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1410715640.579`'), style={'text-align': 'left'}),
            html.Td('Unix timestamp')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`x`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1410715640579`'), style={'text-align': 'left'}),
            html.Td('Unix ms timestamp')
        ]),
    ], style={'margin': 'auto'}),
    html.Br(),
    html.Br(),
    html.H4("Display Format Examples"),
    dcc.Markdown("You can utilize any permutation of the string tokens \
                 shown in the table above to change how selected dates are \
                 displayed in the `DatePickerRange` component."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    end_date=dt.now(),
    display_format='MMM Do, YY',
    start_date_placeholder_text='MMM Do, YY'
),

dcc.DatePickerRange(
    end_date=dt.now(),
    display_format='M-D-Y-Q',
    start_date_placeholder_text='M-D-Y-Q'
),

dcc.DatePickerRange(
    end_date=dt.now(),
    display_format='MMMM Y, DD',
    start_date_placeholder_text='MMMM Y, DD'
),

dcc.DatePickerRange(
    end_date=dt.now(),
    display_format='X',
    start_date_placeholder_text='X'
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerRange(
        end_date=dt.now(),
        display_format='MMM Do, YY',
        start_date_placeholder_text='MMM Do, YY'
    ),

    dcc.DatePickerRange(
        end_date=dt.now(),
        display_format='M-D-Y-Q',
        start_date_placeholder_text='M-D-Y-Q'
    ),

    dcc.DatePickerRange(
        end_date=dt.now(),
        display_format='MMMM Y, DD',
        start_date_placeholder_text='MMMM Y, DD'
    ),

    dcc.DatePickerRange(
        end_date=dt.now(),
        display_format='X',
        start_date_placeholder_text='X'
    ),
    html.Br(),
    html.Br(),
    html.H4("Month Format Examples"),
    dcc.Markdown("Similar to the `display_format`, you can set `month_format` \
                 to any permutation of the string tokens \
                 shown in the table above to change how calendar titles \
                 are displayed in the `DatePickerRange` component."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    month_format='MMM Do, YY',
    end_date_placeholder_text='MMM Do, YY'
),

dcc.DatePickerRange(
    month_format='M-D-Y-Q',
    end_date_placeholder_text='M-D-Y-Q'
),

dcc.DatePickerRange(
    month_format='MMMM Y',
    end_date_placeholder_text='MMMM Y'
),

dcc.DatePickerRange(
    month_format='X',
    end_date_placeholder_text='X'
)

''', language='python', customStyle=styles.code_container),
    html.P("Open the calendars below to see the difference!"),
    dcc.DatePickerRange(
        month_format='MMM Do, YY',
        end_date_placeholder_text='MMM Do, YY'
    ),

    dcc.DatePickerRange(
        month_format='M-D-Y-Q',
        end_date_placeholder_text='M-D-Y-Q'
    ),

    dcc.DatePickerRange(
        month_format='MMMM Y',
        end_date_placeholder_text='MMMM Y'
    ),

    dcc.DatePickerRange(
        initial_visible_month=dt(2012, 9, 1),
        month_format='X',
        end_date_placeholder_text='X'
    ),

    html.Hr(),
    html.H4("Vertical Calendar and Placholder Text"),
    dcc.Markdown("The `DatePickerRange` component can be rendered in two \
                  orientations, either horizontally or vertically. \
                  If `calendar_orientation` is set to `'vertical'`, it will \
                  be rendered vertically and will default to `'horizontal'` \
                  if not defined."),
    dcc.Markdown("As you may have also noticed in the \
                  previous examples `start_date_placeholder_text` and \
                  `end_date_placeholder_text` define the grey default text \
                  defined in the calendar input boxes when no date is \
                  selected."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    start_date_placeholder_text="Select",
    end_date_placeholder_text=" me!",
    calendar_orientation='vertical',
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerRange(
        start_date_placeholder_text="Select",
        end_date_placeholder_text=" me!",
        calendar_orientation='vertical',
    ),
    html.Hr(),

    html.H4("Minimum Nights, Calendar Clear and Portals"),
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
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    minimum_nights=5,
    clearable=True,
    with_portal=True
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerRange(
        clearable=True,
        minimum_nights=5,
        with_portal=True
    ),

    html.Hr(),

    html.H4("Right to Left Calendars and First Day of Week"),
    dcc.Markdown("When the `is_RTL` property is set to `True` \
                  the calendar will be rendered from right to left."),
    dcc.Markdown("The `first_day_of_week` property allows you to \
                  define which day of the week will be set as the first \
                  day of the week. In the example below, Tuesday is \
                  the first day of the week."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    is_RTL=True,
    first_day_of_week=3
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerRange(
        is_RTL=True,
        first_day_of_week=3
    ),

    html.Hr(),
    html.H3('DatePickerRange Properties'),
    generate_table(get_dataframe('DatePickerRange'))
])

# DatePickerSingle
DatePickerSingle = html.Div(children=[
    html.H3("DatePickerSingle Examples and Reference"),
    html.Hr(),
    html.H4("Simple DatePickerSingle Example"),
    dcc.Markdown("The following is a simple example of a `DatePickerSingle` \
                 component tied to a callback. The `min_date_allowed` and \
                 `max_date_allowed` properties define the minimum and \
                 maximum selectable \
                 dates on the calender while `initial_visible_month` defines \
                 the calendar month that is first displayed when the \
                 `DatePickerSingle` component is opened."),
    dcc.SyntaxHighlighter('''import dash
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt

app = dash.Dash()
app.layout = html.Div([
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2017, 9, 19),
        initial_visible_month=dt(2017, 8, 5),
        date=dt(2017, 8, 25)
    ),
    html.Div(id='output-container-date-picker-single')
)


@app.callback(
    dash.dependencies.Output(
        'output-container-date-picker-single', 'children'
    ),
    [dash.dependencies.Input('my-date-picker-single', 'date')])
def update_output(date):
    string_prefix = "You have selected: "
    if date is not None:
        date = dt.strptime(date, '%Y-%m-%d')
        date_string = date.strftime('%B %d, %Y')
        string_prefix = string_prefix + "Start Date: " + date_string
        return string_prefix

if __name__ == '__main__':
    app.run_server(debug=True)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2017, 9, 19),
        initial_visible_month=dt(2017, 8, 5),
        date=dt(2017, 8, 25)
    ),
    html.Div(id='output-container-date-picker-single'),
    html.Hr(),
    html.H3('Month and Display Format'),
    dcc.Markdown("The `display_format` property \
                 determines how selected dates are displayed \
                 in the `DatePickerSingle` component. The `month_format` \
                 property determines how calendar headers are displayed when \
                 the calendar is opened."),
    html.P("Both of these properties are specified through \
            strings that utilize a combination of any \
            of the following tokens."),
    html.Table([
        html.Tr([
            html.Th('String Token', style={'text-align': 'center', 'width': '20%'}),
            html.Th('Example', style={'text-align': 'center', 'width': '20%'}),
            html.Th('Description', style={'text-align': 'center', 'width': '40%'})
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`YYYY`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`2014`'), style={'text-align': 'left'}),
            html.Td('4 or 2 digit year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`YY`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`14`'), style={'text-align': 'left'}),
            html.Td('2 digit year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Y`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`-25`'), style={'text-align': 'left'}),
            html.Td('Year with any number of digits and sign')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Q`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1..4`'), style={'text-align': 'left'}),
            html.Td('Quarter of year. Sets month to first month in quarter.')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`M MM`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1..12`'), style={'text-align': 'left'}),
            html.Td('Month number')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`MMM MMMM`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`Jan..December`'), style={'text-align': 'left'}),
            html.Td('Month name')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`D DD`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1..31`'), style={'text-align': 'left'}),
            html.Td('Day of month')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`Do`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1st..31st`'), style={'text-align': 'left'}),
            html.Td('Day of month with ordinal')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`DDD DDDD`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1..365`'), style={'text-align': 'left'}),
            html.Td('Day of year')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`X`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1410715640.579`'), style={'text-align': 'left'}),
            html.Td('Unix timestamp')
        ]),
        html.Tr([
            html.Td(dcc.Markdown('`x`'), style={'text-align': 'right'}),
            html.Td(dcc.Markdown('`1410715640579`'), style={'text-align': 'left'}),
            html.Td('Unix ms timestamp')
        ]),
    ], style={'margin': 'auto'}),
    html.Br(),
    html.Br(),
    html.H4("Display Format Examples"),
    dcc.Markdown("You can utilize any permutation of the string tokens \
                 shown in the table above to change how selected dates are \
                 displayed in the `DatePickerSingle` component."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    date=dt.now(),
    display_format='MMM Do, YY'
),

dcc.DatePickerSingle(
    date=dt.now(),
    display_format='M-D-Y-Q',
),

dcc.DatePickerSingle(
    date=dt.now(),
    display_format='MMMM Y, DD'
),

dcc.DatePickerSingle(
    date=dt.now(),
    display_format='X',
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerSingle(
        date=dt.now(),
        display_format='MMM Do, YY'
    ),

    dcc.DatePickerSingle(
        date=dt.now(),
        display_format='M-D-Y-Q',
    ),

    dcc.DatePickerSingle(
        date=dt.now(),
        display_format='MMMM Y, DD'
    ),

    dcc.DatePickerSingle(
        date=dt.now(),
        display_format='X',
    ),
    html.Br(),
    html.Br(),
    html.H4("Month Format Examples"),
    dcc.Markdown("Similar to the `display_format`, you can set `month_format` \
                 to any permutation of the string tokens \
                 shown in the table above to change how calendar titles \
                 are displayed in the `DatePickerSingle` component."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    month_format='MMM Do, YY',
    placeholder='MMM Do, YY'
),

dcc.DatePickerSingle(
    month_format='M-D-Y-Q',
    placeholder='M-D-Y-Q'
),

dcc.DatePickerSingle(
    month_format='MMMM Y',
    placeholder='MMMM Y'
),

dcc.DatePickerSingle(
    month_format='X',
    placeholder='X'
)

''', language='python', customStyle=styles.code_container),
    html.P("Open the calendars below to see the difference!"),
    dcc.DatePickerSingle(
        month_format='MMM Do, YY',
        placeholder='MMM Do, YY'
    ),

    dcc.DatePickerSingle(
        month_format='M-D-Y-Q',
        placeholder='M-D-Y-Q'
    ),

    dcc.DatePickerSingle(
        month_format='MMMM Y',
        placeholder='MMMM Y'
    ),

    dcc.DatePickerSingle(
        month_format='X',
        placeholder='X'
    ),

    html.Hr(),
    html.H4("Vertical Calendar and Placholder Text"),
    dcc.Markdown("The `DatePickerSingle` component can be rendered in two \
                  orientations, either horizontally or vertically. \
                  If `calendar_orientation` is set to `'vertical'`, it will \
                  be rendered vertically and will default to `'horizontal'` \
                  if not defined."),
    dcc.Markdown("As you may have also noticed in the \
                  previous examples `placeholder` defines the grey default \
                  text defined in the calendar input boxes when no date is \
                  selected."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    placeholder="Select me!",
    calendar_orientation='vertical',
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerRange(
        start_date_placeholder_text="Select",
        end_date_placeholder_text=" me!",
        calendar_orientation='vertical',
    ),
    html.Hr(),

    html.H4("Calendar Clear and Portals"),
    dcc.Markdown("When the `clearable` property is set to `True` \
                  the component will be rendered with a small 'x' \
                  that will remove all selected dates when selected."),
    dcc.Markdown("The `DatePickerSingle` component supports two different \
                  portal types, one being a full screen portal \
                  (`with_full_screen_portal`) and another being a simple \
                  screen overlay, like the one shown below (`with_portal`)."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    clearable=True,
    with_portal=True
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerRange(
        clearable=True,
        with_portal=True
    ),

    html.Hr(),

    html.H4("Right to Left Calendars and First Day of Week"),
    dcc.Markdown("When the `is_RTL` property is set to `True` \
                  the calendar will be rendered from right to left."),
    dcc.Markdown("The `first_day_of_week` property allows you to \
                  define which day of the week will be set as the first \
                  day of the week. In the example below, Tuesday is \
                  the first day of the week."),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    is_RTL=True,
    first_day_of_week=3
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerSingle(
        is_RTL=True,
        first_day_of_week=3
    ),

    html.Hr(),
    html.H3('DatePickerSingle Properties'),
    generate_table(get_dataframe('DatePickerSingle'))
])

# Link
Link = html.Div(children=[
    html.H3('Link Properties'),
    generate_table(get_dataframe('Link'))
])

# Textarea
Textarea = html.Div(children=[
    html.H3('Textarea Properties'),
    generate_table(get_dataframe('Textarea'))
])
