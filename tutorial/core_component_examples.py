import dash_core_components as dcc
import dash_html_components as html
import os as _os
import json
import dash as _dash
import pandas as pd
import styles

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
                print(holder.items()[0])
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
        elif(type(obj['defaultValue']['value']) == dict and
             len(obj['defaultValue']['value']) > 20):
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
    if('className' in df.index.tolist()):
        reindex = ['id', 'className']
    else:
        reindex = ['id']
    reindex.extend(df.loc[(df.index != 'id') &
                          (df.index != 'className')].index.tolist())
    df['Props'] = df.index
    df = df.reindex(reindex)
    df.fillna('N/A', inplace=True)
    if('Default Value' in df.index):
        df = df[['Props', 'Description', 'Type', 'Default Value']]
    else:
        df = df[['Props', 'Description', 'Type']]
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

    html.H3('Dropdown Extra Examples'),
    html.Hr(),
    html.H4('Searching Dropdown'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    searchable=True,
    clearable=False,
    placeholder="Try typing: "New York"
)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montreal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            searchable=True,
            clearable=False,
            placeholder='Try typing: "New York"'
    ),

    html.Hr(),
    html.H4('Clearing Dropdown'),
    html.P("Try selecting New York or San Francisco"),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'},
    ],
    value='MTL',
    clearable=True
)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
        id='clearable',
        options=[
            {'label': 'New York City', 'value': 'BBC'},
            {'label': 'Montreal', 'value': 'T'},
            {'label': 'San Francisco', 'value': 'F'},
        ],
        value='T',
        clearable=True
    ),

    html.Hr(),
    html.H4('Disabled Options'),
    html.P("Try selecting New York or San Francisco"),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC', 'disabled': 'True'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF', 'disabled': 'True'}
    ],
    clearable=False,
)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC', 'disabled': 'True'},
                {'label': 'Montreal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF', 'disabled': 'True'}
            ],
            clearable=False,
    ),

    html.Hr(),
    html.H4('Disabled Dropdown'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    disabled=True
)

    ''', customStyle=styles.code_container, language='python'),

    dcc.Dropdown(
        disabled=True
    ),


    html.Hr(),
    html.H4("Dropdown Proptypes"),
    generate_table(get_dataframe('Dropdown'))
])


# RangeSlider
Slider = html.Div(children=[
    html.H3('RangeSlider Extra Examples'),
    html.Hr(),
    html.H4('Slider Dots'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=20,
    value=10,
    dots=True
)

    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.Slider(
            min=0,
            max=20,
            value=10,
            dots=True
        ),
    ], className='example-container'),
    html.Hr(),
    html.H4('Vertical Slider'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=20,
    value=20,
    vertical=True
)

    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.Slider(
            min=0,
            max=20,
            value=10,
            vertical=True
        ),
    ]),
    html.Hr(),
    html.H4('Included Prop'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=20,
    value=20,
    included=False
)

    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.Slider(
            min=0,
            max=20,
            value=10,
            included=False
        ),
    ], className='example-container'),
    html.Hr(),
    html.H4("Slider Proptypes"),
    generate_table(get_dataframe('Slider'))
])


# RangeSlider
RangeSlider = html.Div(children=[
    html.H3('Slider Extra Examples'),
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
    ], className='example-container'),
    html.Hr(),
    html.H4('Pushable Handles'),
    dcc.Markdown("`Pushable` can take on two different sets of values. \
                Either a `bool` or a numerical value. \
                Try moving the handles around! "),
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
    ], className='example-container'),
    html.Hr(),
    html.H4('Included Prop'),
    dcc.Markdown("If `included=True`, the rail will not highlight between\
                the points, becoming an independent point rather than\
                continuous"),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=30,
    value=[8, 10, 15],
    included=False
)

    ''', customStyle=styles.code_container, language='python'),
    html.Div([
        dcc.RangeSlider(
            min=0,
            max=30,
            value=[8, 10, 15],
            included=False
        ),
    ], className='example-container'),
    html.Hr(),
    html.H4('Crossing Handles'),
    dcc.Markdown("If `allowCross=False`, the handles will not be allowed to\
                  cross over each other"),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RangeSlider(
    min=0,
    max=30,
    value=[8, 10, 15],
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
    ], className='example-container'),
    html.Hr(),
    html.H4("RangeSlider Proptypes"),
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
    html.H3('Graph Proptypes'),
    generate_table(get_dataframe('Graph'))
])


# DatePickerRange
DatePickerRange = html.Div(children=[
    html.H3('DatePickerRange Proptypes'),
    generate_table(get_dataframe('DatePickerRange'))
])

# DatePickerSingle
DatePickerSingle = html.Div(children=[
    html.H3('DatePickerRange Proptypes'),
    generate_table(get_dataframe('DatePickerSingle'))
])
