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
        if (obj['type']['name'] == 'enum'):
            holder = {'Possible values': []}
            for i in obj['type']['value']:
                holder['Possible values'].append(i['value'])
            obj['Type'] = holder.items()[0]
        elif (obj['type']['name'] == 'arrayOf'):
            objVal = obj['type']['value']
            holder = {'Array Of': [{}]}
            if(objVal['name'] == 'shape'):
                for i in objVal['value']:
                    holder['Array Of'][0][i] = objVal['value'][i]['name']
                obj['Type'] = holder.items()[0]
            elif('value' in objVal):
                for i in objVal['value']:
                    holder['Array Of'].append(str(i))
                obj['Type'] = holder.items()[0]
            else:
                obj['Type'] = "Array of: [" + objVal['name'] + "]"
        elif (obj['type']['name'] == 'union'):
            objVal = obj['type']['value']
            holder = []
            for i in objVal:
                holder.append(i['name'])
                if(len(i) > 1):
                    holder[-1] = "Array of: [" + str(i['value']['name']) + "]"
            obj['Type'] = "One of the following: " + str(holder)
        elif (obj['type']['name'] == 'shape'):
            objVal = obj['type']
            holder = {}
            if('value' in objVal):
                for i in objVal['value']:
                    holder[i] = objVal['value'][i]['name']
            if(len(holder.keys()) > 5):
                obj['Type'] = 'dict'
                obj['Default Value'] = "Check plotly.js docs for more info"
            else:
                obj['Type'] = "Dict of: " + str(holder)
        else:
            obj['Type'] = obj['type']['name']
        obj.pop('type')

    if 'defaultValue' in obj:
        if(obj['defaultValue']['value'] == 'true'):
            obj['defaultValue']['value'] = 'True'
        elif(obj['defaultValue']['value'] == 'false'):
            obj['defaultValue']['value'] = 'False'
        elif(type(obj['defaultValue']['value']) == dict):
            print(obj['defaultValue']['value'])
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
        print(df)
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
        df.set_value('config', 'Default Value',
                     "Check Plotly.js docs for more information")

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
                    internalRow.append(html.Td(str(dataframe.iloc[i][col])))
        rows.append(html.Tr(internalRow))
    table = html.Table(
            [html.Tr([html.Th(col, style={'text-align': 'center'}) for col in
                     dataframe.columns])] + rows)

    return table


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
    html.H4("Dropdown Proptypes"),
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

# Use the following function when accessing the value of 'my-slider'
# in callbacks to transorm the output value to logarithmic
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import *
import dash

app = dash.Dash('')

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
    html.H4("Slider Proptypes"),
    generate_table(get_dataframe('Slider'))
])

# RangeSlider
RangeSlider = html.Div(children=[
    html.H2("RangeSlider Examples and Reference"),
    html.Hr(),
    html.H4('Simple RangeSlider Example'),
    html.P("An example of a basic RangeSlider tied to a callback"),
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
    html.H3('Checklist Proptypes'),
    generate_table(get_dataframe('Checklist'))
])


# Input
Input = html.Div(children=[
    html.H3('Input Proptypes'),
    generate_table(get_dataframe('Input'))
])


# RadioItems
RadioItems = html.Div(children=[
    html.H3('RadioItem Proptypes'),
    generate_table(get_dataframe('RadioItems'))
])


# Markdown
Markdown = html.Div(children=[
    html.H3('Markdown Proptypes'),
    generate_table(get_dataframe('Markdown'))
])


# Graph
Graph = html.Div(children=[
    html.H2('Graph Reference Guide'),
    html.Hr(),
    html.H4('Graph PropTypes'),
    generate_table(get_dataframe('Graph'))
])


# DatePickerRange
DatePickerRange = html.Div(children=[
    html.H2("DatePickerRange Extra Examples"),
    html.H4('Month and Display Format'),
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
    html.Hr(),
    html.H3('DatePickerRange Proptypes'),
    generate_table(get_dataframe('DatePickerRange'))
])

# DatePickerSingle
DatePickerSingle = html.Div(children=[
    html.H3("DatePickerSingle Extra Examples"),
    html.Hr(),
    html.H4('Calendar Orientation'),
    dcc.Markdown('Calendar can either be displayed vertically or horizontally'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    calendar_orientation='vertical',
    placeholder='Test it here!'
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerSingle(
        id='date-picker-single',
        calendar_orientation='vertical',
        placeholder='Test it here!'
    ),
    html.Hr(),
    html.H4('Show outside days'),
    dcc.Markdown('To show days outside the curret calender month,\
                 `show_outside_days` needs to be set to True'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    show_outside_days=True,
    placeholder='With Outside Days'
),

dcc.DatePickerSingle(
    id='date-picker-single',
    show_outside_days=False,
    placeholder='Without Outside Days'
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerSingle(
        id='date-picker-single',
        show_outside_days=True,
        placeholder='True'
    ),

    dcc.DatePickerSingle(
        id='date-picker-single',
        show_outside_days=False,
        placeholder='False'
    ),
    html.Hr(),
    html.H4('Display Formats'),
    dcc.Markdown('You can show months in a variety of display formats.\
                  Display formats denote how, your selected dates will look'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt.now(),
    display_format='MM YY, DD'
),

dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt.now(),
    display_format='M, YYYY, DD'
),

dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt.now(),
    display_format='MMMM Y, DD'
),

dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt.now(),
    display_format='MMMM || Y || DD'
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerSingle(
        id='date-picker-single',
        date=dt.now(),
        display_format='MM YY, DD'
    ),

    dcc.DatePickerSingle(
        id='date-picker-single',
        date=dt.now(),
        display_format='M, YYYY, DD'
    ),

    dcc.DatePickerSingle(
        id='date-picker-single',
        date=dt.now(),
        display_format='MMMM Y, DD'
    ),

    dcc.DatePickerSingle(
        id='date-picker-single',
        date=dt.now(),
        display_format='MMMM || Y || DD'
    ),
    html.Hr(),
    html.H4('Month Formats'),
    dcc.Markdown('This prop determines how the month formats will be\
                 displayed. Click on the date pickers below to see the\
                 results.'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    placeholder='Select me!',
    month_format='MM YY'
),

dcc.DatePickerSingle(
    id='date-picker-single',
    placeholder='Select me too!',
    month_format='M, YYYY'
),

dcc.DatePickerSingle(
    id='date-picker-single',
    placeholder='Try me!',
    month_format='MMMM Y'
),

dcc.DatePickerSingle(
    id='date-picker-single',
    placeholder='Click me!',
    month_format='MMMM || Y'
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerSingle(
        id='date-picker-single',
        placeholder='Select me!',
        month_format='MM YY'
    ),

    dcc.DatePickerSingle(
        id='date-picker-single',
        placeholder='Select me too!',
        month_format='M, YYYY'
    ),

    dcc.DatePickerSingle(
        id='date-picker-single',
        placeholder='Try me!',
        month_format='MMMM Y'
    ),

    dcc.DatePickerSingle(
        id='date-picker-single',
        placeholder='Click me!',
        month_format='MMMM || Y'
    ),
    html.Hr(),
    html.H4('Min, Max and Initial Visible Month'),
    dcc.Markdown('The `min_date_allowed` prop determines the minimum\
                 selectable date on the calendar, the `max_date_allowed`\
                 determines the maximum selectable date on the calendar'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    min_date_allowed=dt(2017, 8, 5),
    max_date_allowed=dt(2017, 8, 27),
    initial_visible_month=dt(2017, 8, 1)
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerSingle(
        id='date-picker-single',
        min_date_allowed=dt(2017, 8, 5),
        max_date_allowed=dt(2017, 8, 27),
        initial_visible_month=dt(2017, 8, 1)
    ),
    html.Hr(),
    html.H4('Clearable Property'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    min_date_allowed=dt(2017, 8, 5),
    date=dt(2017, 8, 15),
    max_date_allowed=dt(2017, 8, 27),
    clearable=True,
    initial_visible_month=dt(2017, 8, 1)
)

''', language='python', customStyle=styles.code_container),
    dcc.DatePickerSingle(
        id='date-picker-single',
        min_date_allowed=dt(2017, 8, 5),
        date=dt(2017, 8, 15),
        max_date_allowed=dt(2017, 8, 27),
        clearable=True,
        initial_visible_month=dt(2017, 8, 1)
    ),
    html.Hr(),
    html.H3('DatePickerSingle Proptypes'),
    generate_table(get_dataframe('DatePickerSingle'))
])

# Link
Link = html.Div(children=[
    html.H3('Link Proptypes'),
    generate_table(get_dataframe('Link'))
])

# Textarea
Textarea = html.Div(children=[
    html.H3('Textarea Proptypes'),
    generate_table(get_dataframe('Textarea'))
])
