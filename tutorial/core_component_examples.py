import dash_core_components as dcc
import dash_html_components as html
import os as _os
import json
import dash as _dash

_current_path = _os.path.join(_os.path.dirname(_os.path.abspath(dcc.__file__)),
                              'metadata.json')

def object_hook_handler(obj):
    if 'required' in obj:
        obj.pop('required')
    if 'id' in obj:
        obj['id']['Description'] = "Optional identifier used to reference\
                              component in callbacks"
    if 'type' in obj and obj['type'] != None and 'name' in obj['type']:
        if obj['type']['name'] == 'enum':
            holder = {'Possible values': []}
            for i in obj['type']['value']:
                holder['Possible values'].append(i['value'])
            obj['Type'] = holder['Possible values']
        elif obj['type']['name'] == 'arrayOf':
            objVal = obj['type']['value']
            holder = {'Array Of': []}
            if('value' in objVal):
                for i in objVal['value']:
                    holder['Array Of'].append(str(i))
                print(holder.items()[0])
                obj['Type'] = holder.items()[0]
            else:
                obj['Type'] = objVal['name']
        else:
            obj['Type'] = obj['type']['name']
        obj.pop('type')
    if 'defaultValue' in obj:
        obj['Default Value'] = obj['defaultValue']['value']
        obj.pop('defaultValue')
    if 'description' in obj:
        obj['Description'] = obj['description']
        obj.pop('description')
    return obj

with open(_current_path, 'r') as f:
    metadata = json.load(f, object_hook=object_hook_handler)


dropdown = html.Div([
    html.H4("Dropdown Proptypes"),
    html.Table([
        html.Tr([
            html.Th('Property', style={'width': '20%'}),
            html.Th('Description', style={'width': '60%'}),
            html.Th('Type', style={'width': '20%'}),
        ]),
        html.Tr([
            html.Td([
                dcc.Markdown('`id`')
            ]),
            html.Td('Optional identifier used to reference component in callbacks'),
            html.Td('string'),
        ]),
        html.Tr([
            html.Td([
                dcc.Markdown('`className`')
            ]),
            html.Td('''Sets the class name of the element (the value of an \
                     element's html class attribute)'''),
            html.Td('string'),
        ]),
        html.Tr([
            html.Td([
                dcc.Markdown('`clearable`')
            ]),
            html.Td('''Whether or not the dropdown is "clearable", that is,\
                       whether or not a small "x" appears on the right of the\
                       dropdown that removes the selected value.'''),
            html.Td('boolean'),
        ]),
        html.Tr([
            html.Td([
                dcc.Markdown('`disabled`')
            ]),
            html.Td('''If true, the element is disabled'''),
            html.Td('boolean'),
        ]),
        html.Tr([
            html.Td([
                dcc.Markdown('`multi`')
            ]),
            html.Td('''If true, the user can select multiple values'''),
            html.Td('boolean'),
        ]),
        html.Tr([
            html.Td([
                dcc.Markdown('`options`')
            ]),
            html.Td('''If true, the user can select multiple values'''),
            html.Td('boolean'),
        ]),
        html.Tr([
            html.Td([
                dcc.Markdown('`placeholder`')
            ]),
            html.Td('''The grey, default text shown when no
                       option is selected'''),
            html.Td('string'),
        ]),
        html.Tr([
            html.Td([
                dcc.Markdown('`searchable`')
            ]),
            html.Td('''if True you can type to narrow down list of values'''),
            html.Td('boolean'),
        ]),
        html.Tr([
            html.Td([
                dcc.Markdown('`value`')
            ]),
            html.Td('''The value of currently selected or
                       highlighted item(s)'''),
            html.Td('string or list'),
        ]),
    ]),
])
