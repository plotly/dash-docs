# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent as s

from tutorial import styles
from tutorial.tools import load_example, read_file

layout = html.Div([
    html.H1(["Loading states"]),
    dcc.Markdown('''
Every component in either `dash_core_components` or `dash_html_components` comes equipped with
a `loading_state` prop. This prop contains an `is_loading` bool, along with a `component_name` and `prop_name`
that tell you if the component is loading, the name of that component and the name of the property that is loading (i.e. "layout")
so that component authors can use that prop to determine what to do if the component is still loading. Dash uses this prop
with the `Loading` component to display spinners if a component is loading.

Aside from using the [`Loading`](/dash-core-components/loading_component) component, you can check if a certain component
(either from `dash_core_components` or `html_components`) is loading by checking the
`data-dash-is-loading` attribute set on that component's HTML output. This means that
you can target those components yourself with CSS, and create your own custom spinner
for them. Here's an example:
    '''),
    dcc.SyntaxHighlighter('''
# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import time

from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True

app.layout = html.Div(
    children=[
        html.Div(id="output-1"),
        dcc.Input(id="input-1", value="Input triggers local spinner"),
        html.Div(
            [
                html.Div(id="output-2"),
                dcc.Input(id="input-2", value="Input triggers nested spinner"),
            ]
        ),
    ]
)


@app.callback(Output("output-1", "children"), [Input("input-1", "value")])
def input_triggers_spinner(value):
    time.sleep(1)
    return value


@app.callback(Output("output-2", "children"), [Input("input-2", "value")])
def input_triggers_nested(value):
    time.sleep(1)
    return value


if __name__ == "__main__":
    app.run_server(debug=False)
    '''),
    html.P("You could target all components in the layout above that are loading using the following CSS:"),
    dcc.SyntaxHighlighter('''
*[data-dash-is-loading="true"]{
    visibility: hidden;
}
*[data-dash-is-loading="true"]::before{
    content: "Loading...";
    display: inline-block;
    color: magenta;
    visibility: visible;
}
    ''', language='css'),
    dcc.Markdown('''
Please also check out the docs for the [Loading component](/dash-core-components/loading_component) for an easier solution
to displaying loading spinners.
    ''')
])
