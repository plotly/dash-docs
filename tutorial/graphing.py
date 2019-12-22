from textwrap import dedent as s
import dash_core_components as dcc
import dash_html_components as html

from tutorial.tools import load_example
from tutorial.components import Example, Syntax

examples = {
    'simple-graph-events': load_example(
        'tutorial/examples/graph_callbacks_simple.py'),
    'world-indicators': load_example(
        'tutorial/examples/getting_started_crossfilter.py'
    ),
    'crossfilter-recipe': load_example(
        'tutorial/examples/crossfilter_recipe.py'
    )
}

layout = html.Div([
    dcc.Markdown('''
    # Interactive Visualizations

    > This is the *5th* chapter of the [Dash Tutorial](/).
    > The [previous chapter](/state) covered callbacks with `State`
    > and the [next chapter](/sharing-data-between-callbacks) describes how to
    > share data between callbacks.
    > Just getting started? Make sure to [install the necessary dependencies](/installation).

    The `dash_core_components` library includes a component called `Graph`.

    `Graph` renders interactive data visualizations using the open source
    [plotly.js](https://github.com/plotly/plotly.js) JavaScript graphing
    library. Plotly.js supports over 35 chart types and renders charts in
    both vector-quality SVG and high-performance WebGL.

    The `figure` argument in the `dash_core_components.Graph` component is
    the same `figure` argument that is used by `plotly.py`, Plotly's
    open source Python graphing library.
    Check out the [plotly.py documentation and gallery](https://plot.ly/python)
    to learn more.

    Dash components are described declaratively by a set of attributes.
    All of these attributes can be updated by callback functions, but only
    a subset of these attributes are updated through user interaction, such as  
    when you click on an option in a `dcc.Dropdown` component and the
    `value` property of that component changes.

    The `dcc.Graph` component has four attributes that can change
    through user-interaction: `hoverData`, `clickData`, `selectedData`,
    `relayoutData`.
    These properties update when you hover over points, click on points, or
    select regions of points in a graph.

    '''.replace('    ', '')),

    Syntax(
        examples['simple-graph-events'][0],
        summary="""
            Here's an simple example that
            prints these attributes in the screen.
    """),
    Example(examples['simple-graph-events'][1]),

    html.Hr(),

    html.H3('Update Graphs on Hover'),

    Syntax(examples['world-indicators'][0], summary="""
    Let's update our world indicators example from the previous chapter
    by updating time series when we hover over points in our scatter plot.
    """),
    Example(examples['world-indicators'][1]),

    dcc.Markdown(s('''
    Try mousing over the points in the scatter plot on the left.
    Notice how the line graphs on the right update based off of the point that
    you are hovering over.
    ''')),

    html.Hr(),

    html.H3('Generic Crossfilter Recipe'),

    Syntax(examples['crossfilter-recipe'][0], summary="""
    Here's a slightly more generic example for crossfiltering across
    a six-column data set. Each scatter plot's selection filters the
    underlying dataset.
    """),

    html.Img(
        src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/select.gif',
        alt='Dash Data Selection Example',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }),

    dcc.Markdown(s('''
    Try clicking and dragging in any of the plots to filter different regions.
    On every selection, the three graph callbacks are fired with the latest
    selected regions of each plot. A pandas dataframe is filtered based off
    of the selected points and the graphs are replotted with the selected
    points highlighted and the selected region drawn as a dashed rectangle.

    > As an aside, if you find yourself filtering and visualizing
    highly-dimensional datasets, you should consider checking out the
    [parallel coordinates](https://plot.ly/python/parallel-coordinates-plot/)
    chart type.
    ''')),

    dcc.Markdown(s('''

    ### Current Limitations

    There are a few limitations in graph interactions right now.
    - It is not currently possible to customize the style of the hover
      interactions or the select box.
      This issue is being worked on in [https://github.com/plotly/plotly.js/issues/1847](https://github.com/plotly/plotly.js/issues/1847).

    ***

    There's a lot that you can do with these interactive plotting features.
    If you need help exploring your use case, open up a thread in the
    [Dash Community Forum](https://community.plot.ly/c/dash).

    ***

    The next chapter of the Dash User Guide explains how to share data between
    callbacks.
    ''')),

    dcc.Link(
        'Dash Tutorial Part 6. Sharing Data Between Callbacks',
        href='/sharing-data-between-callbacks'
    )

])
