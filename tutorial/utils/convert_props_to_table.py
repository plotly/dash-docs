# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_core_components as dcc
import json
import os
import pandas as pd
import dash


_current_path = os.path.join(os.path.dirname(os.path.abspath(dcc.__file__)),
                              'metadata.json')


def js_to_py_type(type_object):
    js_type_name = type_object['name']

    # wrapping everything in lambda to prevent immediate execution
    js_to_py_types = {
        'array': lambda: 'list',
        'bool': lambda: 'boolean',
        'number': lambda: 'number',
        'component_name': lambda: 'component_name',
        'object': lambda: 'dict',

        'any': lambda: 'boolean | number | component_name | dict | list',
        'element': lambda: 'dash component',
        'node': lambda: (
            'a list of or a singular dash component, component_name or number'
        ),

        # React's PropTypes.oneOf
        'enum': lambda: 'one of: {}'.format(', '.join([
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
            'dict with component_names as keys and values of type {}'
        ).format(js_to_py_type(type_object['value'])),


        # React's PropTypes.shape
        'shape': lambda: (
            'dict containing key(s): {}\n{}'.format(
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
        obj['id']['Description'] = 'Optional identifier used to reference\
                              component in callbacks'
    if 'className' in obj:
        obj['className']['Description'] = '''Sets the class name of the element (the value of an
                                             element's html class attribute)'''
    if 'type' in obj and obj['type'] != None and 'name' in obj['type']:
        obj['Type'] = js_to_py_type(obj['type'])
    if 'defaultValue' in obj:
        if obj['defaultValue']['value'] == 'true':
            obj['defaultValue']['value'] = '`True`'
        elif obj['defaultValue']['value'] == 'false':
            obj['defaultValue']['value'] = '`False`'
        elif type(obj['defaultValue']['value']) == dict:
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


def get_dataframe(component_name):
    prefix = 'src/components/'
    suffix = '.react.js'
    fullString = prefix+component_name+suffix
    df = pd.DataFrame(metadata[fullString]
                              ['props']).transpose()
    if 'dashEvents' in df.index.tolist():
        df.drop(['dashEvents'], inplace=True)
    if 'fireEvent' in df.index:
        df.drop(['fireEvent'], inplace=True)
    if 'setAttribute' in df.index:
        df.drop(['setAttribute'], inplace=True)
    if 'dashFireEvent' in df.index:
        df.drop(['dashFireEvent'], inplace=True)
    if 'className' in df.index.tolist():
        reindex = ['id', 'className']
    else:
        reindex = ['id']
    reindex.extend(df.loc[(df.index != 'id') &
                          (df.index != 'className')].index.tolist())
    df['Attribute'] = df.index
    df = df.reindex(reindex)
    df.fillna('', inplace=True)
    if 'Default Value' in df.columns.values.tolist():
        df = df[['Attribute', 'Description', 'Type', 'Default Value']]
    else:
        df = df[['Attribute', 'Description', 'Type']]

    if 'config' in df['Attribute']:
        df.set_value('config', 'Type',
                     'dict, check Plotly.js docs for more information')
        df.set_value('config', 'Default Value',
                     "{}")
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
                internalRow.append(html.Td('Array of Dict: ' +
                                           str(dataframe.iloc[i][col][1])))
            else:
                if col == 'Type':
                    internalRow.append(html.Td(
                        dcc.Markdown(dataframe.iloc[i][col]\
                            .replace('true', '`True`')\
                            .replace('false', '`False`')\
                            .replace('\n', '\n\n')\
                            .replace('    ', '')
                        ),
                        style={'text-align': 'left'}))
                elif col == 'Description':
                    internalRow.append(
                        html.Td(dcc.Markdown(
                            dataframe.iloc[i][col]\
                                .replace('true', '`True`')\
                                .replace('false', '`False`')
                        ),
                        style={'font-size': '0.95em'})
                    )
                else:
                    internalRow.append(html.Td(
                        dcc.Markdown(
                            dataframe.iloc[i][col]
                        )
                    ))
        rows.append(html.Tr(internalRow))
    table = html.Table(
            [html.Tr([html.Th(col, style={'text-align': 'left'}) for col in
                     dataframe.columns])] + rows)

    return table

def generate_prop_table(component_name):
    return generate_table(get_dataframe(component_name))
