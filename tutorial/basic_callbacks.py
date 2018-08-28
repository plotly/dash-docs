import dash_core_components as dcc
import dash_html_components as html

import styles
import tools

examples = [
    tools.load_example(s) for s in [
        'tutorial/examples/basic_callbacks_example_1.py',
        'tutorial/examples/basic_callbacks_example_2.py',
        'tutorial/examples/basic_callbacks_events.py'
    ]
]

layout = html.Div(children=[
    dcc.Markdown('''
    ## Interactivity with Callbacks

    The heart and soul of Dash is providing an easy way to bind Python
    callbacks to web interfaces.

    With Dash's callback decorators, you can update certain components
    when other components change values. Here's a practical example.
    View the interactive app below the code.

    '''.replace('    ', '')),
    dcc.SyntaxHighlighter(
        examples[0][0], language='python', customStyle=styles.code_container
    ),
    html.Div('This code will generate an app like this:'),

    html.Div(examples[0][1], className='example-container')
])


layout.children.extend([
    dcc.Markdown('''
## Multiple Inputs

Let's extend this example by including
a secondary input element that controls
which variable we should plot.

Dash apps are "reactive" which means that
whenever values change in the front-end,
the callback functions will get called
automatically.

'''),
    dcc.SyntaxHighlighter(
        examples[1][0], language='python', customStyle=styles.code_container),
    html.Div(examples[1][1], className='example-container')
])


layout.children.extend([
    dcc.Markdown('''
## Events and States

Reactive interfaces are great when the callbacks are fast.
As a user, the delay between selected an option in the dropdown
and seeing the graph update is small and the interface feels
snappy.

An alternative to these types of reactive interfaces is subscribing
explicitly to events. Subscribing to events is great when your
callbacks takes at least a couple of seconds to run or when
you would like your users to update a set of controls before showing
them the output.

You can subscribe to event changes with the
`dash.dependencies.Event` object. Most Dash components will have
events that you can subscribe to. To see the available events of any
dash component, either call `help()` or look up a list with the
`available_events` property:

```
>>> print(html.Button.available_events)
['click']

>>> print(dcc.Graph.available_events)
['restyle', 'relayout']
```

In this example, we'll update our graph when we click on the button.
We'll pass in the currently selected values of the dropdowns through
the `state` arguments.

'''),
    dcc.SyntaxHighlighter(
        examples[2][0], language='python', customStyle=styles.code_container
    ),
    html.Div(examples[2][1], className='example-container')
])
