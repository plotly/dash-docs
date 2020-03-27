import dash_core_components as dcc
import dash_html_components as html

from dash_docs import tools
from dash_docs.reusable_components import Example, Syntax
from dash_docs.tools import load_example
from dash_docs import reusable_components

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
    reusable_components.Markdown('''
    # Interactive Visualizations

    <blockquote>
    This is the 4th chapter of the <dccLink children="Dash Tutorial" href="/"/>.
    The <dccLink href="/basic-callbacks" children="previous chapter"/> covered basic callback usage.
    The <dccLink href="/sharing-data-between-callbacks" children="next chapter"/> describes how to
    share data between callbacks.
    Just getting started? Make sure to <dccLink href="/installation" children="install the necessary dependencies"/>.
    </blockquote>

    The `dash_core_components` library includes a component called `Graph`.

    `Graph` renders interactive data visualizations using the open source
    [plotly.js](https://github.com/plotly/plotly.js) JavaScript graphing
    library. Plotly.js supports over 35 chart types and renders charts in
    both vector-quality SVG and high-performance WebGL.

    The `figure` argument in the `dash_core_components.Graph` component is
    the same `figure` argument that is used by `plotly.py`, Plotly's
    open source Python graphing library.
    Check out the [plotly.py documentation and gallery](https://plotly.com/python)
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

    '''),

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

    reusable_components.Markdown('''
    Try mousing over the points in the scatter plot on the left.
    Notice how the line graphs on the right update based off of the point that
    you are hovering over.
    '''),

    html.Hr(),

    html.H3('Generic Crossfilter Recipe'),

    Syntax(examples['crossfilter-recipe'][0], summary="""
    Here's a slightly more generic example for crossfiltering across
    a six-column data set. Each scatter plot's selection filters the
    underlying dataset.
    """),

    html.Img(
        src=tools.relpath('assets/images/gallery/select.gif'),
        alt='Dash Data Selection Example',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }),

    reusable_components.Markdown('''
    Try clicking and dragging in any of the plots to filter different regions.
    On every selection, the three graph callbacks are fired with the latest
    selected regions of each plot. A pandas dataframe is filtered based off
    of the selected points and the graphs are replotted with the selected
    points highlighted and the selected region drawn as a dashed rectangle.

    > As an aside, if you find yourself filtering and visualizing
    highly-dimensional datasets, you should consider checking out the
    [parallel coordinates](https://plotly.com/python/parallel-coordinates-plot/)
    chart type.
    '''),

    reusable_components.Markdown('''

    ### Current Limitations

    There are a few limitations in graph interactions right now.
    - It is not currently possible to customize the style of the hover
      interactions or the select box.
      This issue is being worked on in [https://github.com/plotly/plotly.js/issues/1847](https://github.com/plotly/plotly.js/issues/1847).

    ***

    There's a lot that you can do with these interactive plotting features.
    If you need help exploring your use case, open up a thread in the
    [Dash Community Forum](https://community.plotly.com/c/dash).

    ***

    The next chapter of the Dash User Guide explains how to share data between
    callbacks.
    '''),

    dcc.Link(
        'Dash Tutorial Part 5. Sharing Data Between Callbacks',
        href=tools.relpath('/sharing-data-between-callbacks')
    )

])
