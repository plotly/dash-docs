import dash_html_components as html
import dash_core_components as dcc

from dash_docs import styles
from dash_docs import tools
from dash_docs import reusable_components

print('Loading examples')
examples = [
    tools.load_example(s) for s in [
        'tutorial/examples/graph_callbacks_simple.py',
        'tutorial/examples/graph_callbacks_crossfiltering.py',
        'tutorial/examples/graph_callbacks_same_graph.py'
    ]
]


layout = [reusable_components.Markdown('''
# Graph Callbacks

Dash renders graphs using the interactive
[plotly.js](https://github.com/plotly/plotly.js) graphing library.

Plotly.js graphs are natively interactive.
- Hover over points to see their values
- Click and drag on the graph to zoom into regions
- Double click to zoom out
- Shift + Click + Drag to pan regions
- Select points using the lasso or the rectangle in the graph bar

With dash, these events update the `Graph` component's
`clickData`, `hoverData`, and `selectedData` values.

By setting those properties as `Input` properties, you can
update your Dash application in response to these events.

'''),
          reusable_components.Markdown(examples[0][0], style=styles.code_container),

          html.Div(examples[0][1], className="example-container")
]


layout.extend([
    reusable_components.Markdown('''

***

## Crossfiltering Between Graphs

One of the really powerful things that you can do with these types of
variables is cross filtering between charts, allowing you to interact
with multiple dimensions of data across multiple views at once.

Here's a simple example.

In this example, we use the `customdata` property to add extra
metadata for the points that we've hovered over or selected.
'''),

    reusable_components.Markdown(examples[1][0], style=styles.code_container),
    html.Div(
        examples[1][1],
        className="example-container",
        style=dict({'paddingBottom': '30px'})
    )
])

layout.extend([
    reusable_components.Markdown('''

This graph is highly interactive. Hovering over values will trigger our
callbacks and highlight the associated point (country) in the other graph.

The exact same filtering operation occurs if you select multiple points
by clicking and dragging on the plot with the lasso. The slider ties it
together by filtering the data by selected year.

***

It's also possible to update the same the graph in response to these events.
Here's another take on this dataset. Hovering over a value will replot the
chart with that country's historical trajectory.
'''),

    reusable_components.Markdown(
        examples[2][0],
        style=styles.code_container
    ),

    html.Div(
        examples[2][1],
        className="example-container",
        style=dict(paddingBottom='30px')
    )
])
