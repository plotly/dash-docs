import dash
import dash_html_components as html
import dash_core_components as dcc
import textwrap
import re
import inspect

def convert_docstring_to_markdown(docstring):
    if not docstring:
        return '\n\(No docstring available)\n'

    lines = docstring.split('\n')

    # For some reason the second block of lines is indented
    docstring = lines[0] + textwrap.dedent('\n'.join(lines[1:]))

    # Replace ':param <variable>' with `<variable>`
    docstring = re.sub(r'\:param (\w*)\:', r'**`\1`**\n\n', docstring)

    docstring = re.sub(r'\:type (\w*)\:', r'\ntype:', docstring)

    # Remove leading ': from rst Example
    docstring = docstring.replace(':Example:', 'Example:')

    docstring = docstring.replace(
        ':return:', '\n\nreturns:'
    )

    docstring = docstring.replace('``', '`')

    return docstring

app = dash.Dash(__name__)

SKIP = ['dash', 'json', 'dedent']

def doc_signature(obj, method, prefix):
    try:
        signature = str(inspect.signature(getattr(obj, method)))
    except:
        signature = ''

    try:
        name = method.__name__
    except:
        name = str(method)

    if not prefix:
        try:
            prefix = obj.__name__
        except:
            prefix = str(obj)
    prefix_signature = prefix

    return html.Div(
        [
            html.H2(
                html.Code("{}.{}".format(prefix, name)),
                className="docs-article",
            ),
            html.Pre(
                className="docs-article",
                children=html.Code(
                    "{}.{}{}".format(
                        prefix_signature,
                        name,
                        signature
                        .replace(",", ",\n   ")
                        .replace("(", "(\n    ")
                        .replace(")", "\n)")
                        .replace("    self,\n", "")
                        .replace("\n    self\n", ""),
                    )
                ),
            ),
        ]
    )

PUBLIC_API = [
    # app,
    # dash.Dash,
    # dash.resources,
    dict(obj=dash, prefix='', skip=[
        'fingerprint',
    ], preamble=dcc.Markdown(
    '''
    # The `dash` module
    ```
    import dash
    ```
    '''
    )),

    dict(obj=app, prefix='app', skip=[
        'css',
        'dependencies',
        'dispatch',
        'exceptions',
        'logger',
        'registered_paths',
        'renderer',
        'resources',
        'routes',
        'scripts',
        'serve_component_suites',
        'serve_layout',
        'serve_reload_hash',
        'validation_layout'
    ], preamble=dcc.Markdown(
    '''
    # The `app` Object
    ```
    import dash
    app = dash.Dash(__name__)
    ```
    '''
    ), override=dict(
        server=dcc.Markdown(
            '''
            The Flask server associated with this app.
            Often used in conjunction with `gunicorn` when running the app
            in production with multiple workers:
            
            `app.py`
            ```
            app = dash.Dash(__name__)
            
            # expose the flask variable in the file
            server = app.server  
            ```
            
            `Procfile`
            ```
            gunicorn app:server
            ```
            '''
        ),
        title=dcc.Markdown(
            '''
            Configures the document.title (the text that appears in a browser tab).

            Default is "Dash".
            
            This is now configurable in the `dash.Dash(title='...')` constructor 
            instead of as a property of `app`. We have kept this property
            in the `app` object for backwards compatibility.
            '''
            
            
        )
    )),

    dict(obj=dash.dependencies, prefix='', skip=[], preamble=dcc.Markdown(
    '''
    # The `dash.dependencies` module
    
    The classes in `dash.dependencies` are all used in the `app.callback`
    signature.
    '''
    )),

    dict(obj=dash.exceptions, prefix='', skip=[], preamble=dcc.Markdown(
    '''
    # The `dash.exceptions` module
    
    Dash will raise exceptions under certain scenarios. 
    Dash will always use a special exception class that can be caught to 
    handle this particular scenario.
    These exception classes are in this module.
    '''
    ), global_override='')
]


def public_methods(obj):
    methods = []    
    for method in dir(obj):
        if (obj and
                not method.startswith('_') and 
                method not in SKIP and 
                'dash' in str(obj) and 
                'class' not in method and
                'development' not in method):
            methods.append(method)
    return methods

def create_docstrings():
    docstring = []
    for docitem in PUBLIC_API:
        docstring.append(docitem['preamble']),
        for method in public_methods(docitem['obj']):
            if method not in docitem['skip']:
                docstring.append(doc_signature(docitem['obj'], method, docitem['prefix']))
                if 'override' in docitem and method in docitem['override']:
                    docstring.append(docitem['override'][method])
                elif 'global_override' in docitem:
                    docstring.append(docitem['global_override'])
                else:
                    docstring.append(dcc.Markdown(convert_docstring_to_markdown(getattr(docitem['obj'], method).__doc__)))
        docstring.append(html.Hr())
    return docstring          

layout = html.Div([

    dcc.Markdown(
    '''
    # API Reference
    
    This page displays the docstrings for the public methods of the
    `dash` module including the `app` object.
    
    Curious about the implementation details? 
    [Browse the Dash source code](https://github.com/plotly/dash).
    '''
    ),

    html.Div(create_docstrings()),

])

