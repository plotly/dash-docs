import dash_core_components as dcc
import dash_html_components as html

from dash_docs.tutorial.components import Example, Syntax
from dash_docs import tools
from dash_docs import reusable_components

examples = {
    'prevent-update': tools.load_example('tutorial/examples/prevent_update.py'),
    'prevent-update-button': tools.load_example('tutorial/examples/prevent_update_button.py'),
}

layout = html.Div([
    html.H1('Dash PreventUpdate'),

    reusable_components.Markdown('''
        ## Dash State
        <blockquote>
        This is the 4th chapter of the <dccLink children="Dash Tutorial" href="/"/>.
        The <dccLink href="/getting-started-part-2" children="previous chapter"/> covered Dash Callbacks
        and the <dccLink href="/interactive-graphing" children="next chapter"/> covers interactive
        graphing and crossfiltering.
        Just getting started? Make sure to
        <dccLink href="/installation" children="install the necessary dependencies"/>.
        </blockquote>
    '''),


        ## Using PreventUpdate in Callback
    reusable_components.Markdown('''
        In certain situations, you don't want to update the callback output. You can
        achieve this by raising a `PreventUpdate` exception in the callback function.
    '''),
    Syntax(examples['prevent-update-button'][0]),
    Example(examples['prevent-update-button'][1]),

    reusable_components.Markdown('''
        This example illustrates how you can show an error while keeping the previous
        input, using `dash.no_update` to update the output partially.
    '''),
    Syntax(examples['prevent-update'][0]),
    Example(examples['prevent-update'][1]),

    dcc.Link(
        'Dash Tutorial Part 5. Interactive Graphing',
        href=tools.relpath('/interactive-graphing')),

])
