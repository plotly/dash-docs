import dash_core_components as dcc
import dash_html_components as html

from dash_docs.tutorial.components import Example, Syntax
from dash_docs import tools
from dash_docs import reusable_components

layout = html.Div([
    html.H1('Clientside Callbacks'),

    reusable_components.Markdown('''
    Sometimes callbacks can incur a significant overhead, especially when they :
    - receive and/or return very large quantities of data (transfer time)
    - are called very often (network latency, queuing, handshake)
    - are part of a callback chain that requires multiple roundtrips
    between the browser and Dash


    When the overhead cost of a callback becomes too great and that no
    other optimization is possible, the callback can be modified to be run
    directly in the browser instead of a making a request to Dash.

    The syntax for the callback is almost exactly the same; you use
    `Input` and `Output` as you normally would when declaring a callback,
    but you also define a JavaScript function as the first argument to the
    `@app.callback` decorator.

    For example, the following callback:

'''),

    Syntax('''
    @app.callback(
        Output('out-component', 'value'),
        [Input('in-component1', 'value'), Input('in-component2', 'value')]
    )
def large_params_function(largeValue1, largeValue2):
    largeValueOutput = someTransform(largeValue1, largeValue2)

    return largeValueOutput
    '''),

    reusable_components.Markdown('''

    ***

    Can be rewritten to use JavaScript like so:

'''),

    Syntax('''
    from dash.dependencies import Input, Output

app.clientside_callback(
    """
    function(largeValue1, largeValue2) {
        return someTransform(largeValue1, largeValue2);
    }
    """,
    Output('out-component', 'value'),
    [Input('in-component1', 'value'), Input('in-component2', 'value')]
)
    '''),

    reusable_components.Markdown('''

    ***

    You also have the option of defining the function in a `.js` file in
        your `assets/` folder. To achieve the same result as the code above,
        the contents of the `.js` file would look like this:

'''),

    Syntax('''
    window.dash_clientside = Object.assign({}, window.dash_clientside, {
        clientside: {
            large_params_function: function(largeValue1, largeValue2) {
            return someTransform(largeValue1, largeValue2);
            }
        }
    });
    '''),

    reusable_components.Markdown('''

    ***

    In Dash, the callback would now be written as:

'''),

    Syntax('''
    from dash.dependencies import ClientsideFunction, Input, Output

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='large_params_function'
    ),
    Output('out-component', 'value'),
    [Input('in-component1', 'value'), Input('in-component2', 'value')]
)
    '''),

    reusable_components.Markdown('''
    ***

    **Note**: There are a few limitations to keep in mind:

    1. Clientside callbacks execute on the browser's main thread and wil block
    rendering and events processing while being executed.
    2. Dash does not currently support asynchronous clientside callbacks and will
    fail if a `Promise` is returned.
    3. Clientside callbacks are not possible if you need to refer to global
    variables on the server or a DB call is required.
''')

])
