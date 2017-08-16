import dash_core_components as dcc
import dash_html_components as html
import os as _os
import json
import dash as _dash
import pandas as pd

_current_path = _os.path.join(_os.path.dirname(_os.path.abspath(dcc.__file__)),
                              'metadata.json')

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
        if obj['type']['name'] == 'enum':
            holder = {'Possible values': []}
            for i in obj['type']['value']:
                holder['Possible values'].append(i['value'])
            obj['Type'] = holder.items()[0]
        elif obj['type']['name'] == 'arrayOf':
            objVal = obj['type']['value']
            holder = {'Array Of': []}
            if('value' in objVal):
                for i in objVal['value']:
                    holder['Array Of'].append(str(i))
                obj['Type'] = holder.items()[0]
            else:
                obj['Type'] = objVal['name']
        elif obj['type']['name'] == 'union':
            print(obj)
        else:
            obj['Type'] = obj['type']['name']
        obj.pop('type')
    if 'defaultValue' in obj:
        if(obj['defaultValue']['value'] == 'true'):
            obj['defaultValue']['value'] = 'True'
        elif(obj['defaultValue']['value'] == 'false'):
            obj['defaultValue']['value'] = 'False'
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
    df = pd.DataFrame(metadata[prefix + string + suffix]
                              ['props']).transpose().drop(['dashEvents',
                                                           'setProps'])
    if('className' in df.index.tolist()):
        reindex = ['id', 'className']
    else:
        reindex = ['id']
    reindex.extend(df.loc[(df.index != 'id') & (df.index != 'className')].index.tolist())
    df['Props'] = df.index
    df = df.reindex(reindex)
    df.fillna('N/A', inplace=True)
    df = df[['Props', 'Description', 'Type', 'Default Value']]
    return df

def generate_table(dataframe):
    rows = []
    for i in range(len(dataframe)):
        internalRow = []
        for col in dataframe.columns:
            # Body
            if(type(dataframe.iloc[i][col]) == tuple):
                internalRow.append(html.Td(dataframe.iloc[i][col][0] + ': ' +
                                   str([str(j) for j in dataframe.iloc[i][col]
                                                                      [1]])))
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
            [html.Tr([html.Th(col, style={'text-align': 'center'}) for col in dataframe.columns])] + rows)

    return table

print("Hello")
table = generate_table(get_dataframe('Checklist'))

dropdown = html.Div(children=[
    html.H4("Dropdown Proptypes"),
    generate_table(get_dataframe('Checklist')),
    # html.Table([
    #     html.Tr([
    #         html.Th('Property', style={'width': '20%'}),
    #         html.Th('Description \n', style={'width': '60%'}),
    #         html.Th('Type', style={'width': '20%'}),
    #     ]),
    #     html.Tr([
    #         html.Td([
    #             dcc.Markdown('`id`')
    #         ]),
    #         html.Td('Optional identifier used to reference component in callbacks'),
    #         html.Td('string'),
    #     ]),
    #     html.Tr([
    #         html.Td([
    #             dcc.Markdown('`className`')
    #         ]),
    #         html.Td('''Sets the class name of the element (the value of an \
    #                  element's html class attribute)'''),
    #         html.Td('string'),
    #     ]),
    #     html.Tr([
    #         html.Td([
    #             dcc.Markdown('`clearable`')
    #         ]),
    #         html.Td('''Whether or not the dropdown \n \n is "clearable", that is,\
    #                    whether or not a small "x" appears on the right of the\
    #                    dropdown that removes the selected value.'''),
    #         html.Td('boolean'),
    #     ]),
    #     html.Tr([
    #         html.Td([
    #             dcc.Markdown('`disabled`')
    #         ]),
    #         html.Td('''If true, the element is disabled'''),
    #         html.Td('boolean'),
    #     ]),
    #     html.Tr([
    #         html.Td([
    #             dcc.Markdown('`multi`')
    #         ]),
    #         html.Td('''If true, the user can select multiple values'''),
    #         html.Td('boolean'),
    #     ]),
    #     html.Tr([
    #         html.Td([
    #             dcc.Markdown('`options`')
    #         ]),
    #         html.Td('''If true, the user can select multiple values'''),
    #         html.Td('boolean'),
    #     ]),
    #     html.Tr([
    #         html.Td([
    #             dcc.Markdown('`placeholder`')
    #         ]),
    #         html.Td('''The grey, default text shown when no
    #                    option is selected'''),
    #         html.Td('string'),
    #     ]),
    #     html.Tr([
    #         html.Td([
    #             dcc.Markdown('`searchable`')
    #         ]),
    #         html.Td('''if True you can type to narrow down list of values'''),
    #         html.Td('boolean'),
    #     ]),
    #     html.Tr([
    #         html.Td([
    #             dcc.Markdown('`value`')
    #         ]),
    #         html.Td('''The value of currently selected or
    #                    highlighted item(s)'''),
    #         html.Td('string or list'),
    #     ]),
    # ]),
])
