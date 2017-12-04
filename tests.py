import unittest

from tutorial import introduction
from tutorial import getting_started
from tutorial import html_components
from tutorial import core_components
from tutorial import basic_callbacks
from tutorial import html_component_appendix
from tutorial import callbacks_with_dependencies
from tutorial import dynamic_content
from tutorial import external_css_and_js
from tutorial import open_problems
from tutorial import architecture
from tutorial import graph_callbacks
from tutorial import live_updates
from tutorial import urls

chapters = [
    introduction,
    getting_started,
    html_components,
    core_components,
    basic_callbacks,
    html_component_appendix,
    callbacks_with_dependencies,
    dynamic_content,
    external_css_and_js,
    open_problems,
    architecture,
    graph_callbacks,
    live_updates,
    urls
]

from tutorial.server import app

with open('tutorial/examples/getting_started.py', 'r') as f:
    example = f.read()

    # Use the global app assignment
    if 'app = dash.Dash' not in example:
        raise Exception("Didn't declare app")
    example = example.replace('app = dash.Dash', '# app = dash.Dash')
    local_variables = {'app': app}

    # return the layout instead of assigning it to the global app
    if 'app.layout = ' not in example:
        raise Exception('app.layout not assigned')
    example = example.replace('app.layout = ', 'layout = ')

    # Remove the "# Run the server" commands
    if 'app.run_server' not in example:
        raise Exception('app.run_server missing')
    example = example.replace(
        '\n    app.run_server',
        'print("Running")\n    # app.run_server'
    )

    output = {}
    exec(example, local_variables, output)
