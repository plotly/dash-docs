import dash_html_components as html
import dash_core_components as dcc
import dash

METHODS = [
    method
    for method in dir(dash)
    if not method.startswith("_")
]


import dash
import dash_html_components as html
import dash_core_components as dcc
import textwrap
import re

def convert_method_name_to_markdown(obj, method):
    method_name = f'{obj}.{method}'
    method_name = method_name.replace("<class 'dash.dash.Dash'>", 'app')
    return method_name

def convert_docstring_to_markdown(docstring):
    if not docstring:
        return '\n\nUndocumented\n'

    lines = docstring.split('\n')

    # For some reason the second block of lines is indented
    docstring = lines[0] + textwrap.dedent('\n'.join(lines[1:]))

    # Replace ':param <variable>' with `<variable>`
    docstring = re.sub(r'\:param (\w*)\:', r'**`\1`**\n\n', docstring)

    docstring = re.sub(r'\:type (\w*)\:', r'\ntype:', docstring)

    # Remove leading ': from rst Example
    docstring = docstring.replace(':Example:', 'Example:')

    docstring = docstring.replace('``', '`')

    return docstring

app = dash.Dash(__name__)

SKIP = ['dash']

PUBLIC_API = [
    dash.Dash,
    dash.resources,
    dash.exceptions,
    dash.dependencies,
    dash
]

DOCSTRINGS = ''
def recursively_create_docstrings(obj):
    docstring = ''
    for method in dir(obj):
        if (obj and not method.startswith('_') and 
                method not in SKIP and 
                'dash' in str(obj) and 
                'class' not in method and
                'development' not in method):
            print(str(obj))
            print(method)
            try:
                getattr(obj, method).__doc__
            except:
                print(f'Error accessing {obj}.{method}')
                continue
            docstring = docstring + f'\n\n***\n\n**`{convert_method_name_to_markdown(obj, method)}`**\n\n' + (convert_docstring_to_markdown(getattr(obj, method).__doc__)) 
            docstring = docstring + recursively_create_docstrings(getattr(obj, method))
                
    return docstring

def public_methods(obj):
    methods = []    
    for method in dir(obj):
        if (obj and not method.startswith('_') and 
                method not in SKIP and 
                'dash' in str(obj) and 
                'class' not in method and
                'development' not in method):
            methods.append(method)
    return methods

def create_docstrings():
    docstring = ''
    for obj in PUBLIC_API:
        for method in public_methods(obj):
            docstring = docstring + f'\n\n***\n\n**`{convert_method_name_to_markdown(obj, method)}`**\n\n' + (convert_docstring_to_markdown(getattr(obj, method).__doc__)) 
    return docstring          

layout = html.Div([

    dcc.Markdown(create_docstrings()),
])
