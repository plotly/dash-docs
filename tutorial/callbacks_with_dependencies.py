# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from tutorial import styles
from tutorial import tools

examples = [
    tools.load_example(s) for s in [
        'tutorial/examples/callbacks_with_dependencies.py'
    ]
]

layout = [
    dcc.Markdown('''
    ## Callback Resolution

    A core feature in Dash is callback dependency resolution.


    A common real-world example is with forms.
    Often, the options of one dropdown depend on the value of another
    dropdown.
    A third component might depend on the values of both components.


    When the first dropdown changes,
    the second dropdown is triggered to change but the third component
    shouldn't update until both dropdowns have finished updating.
    If Dash updated the third component without waiting for the
    second dropdown to update, then its callback could get called with
    inconsistent state.


    In this example, each dropdown's options and values depend on the
    previous dropdown. We've inserted a 2 second delay in each of the
    callbacks to illustrate the order in which components get updated.


    Note how the text component depends on the values of all of the
    dropdowns but doesn't get updated until all three dropdowns have
    finished updating.'''.replace('    ', '')),
    dcc.Markdown(
        examples[0][0],
        style=styles.code_container
    ),
    html.Div(examples[0][1], className='example-container')
]
