import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape
from textwrap import dedent

from dash_docs.reusable_components import Section, Chapter
from dash_docs import styles
from dash_docs import tools
from dash_docs import reusable_components

examples = {
    example: tools.load_example('tutorial/examples/cytoscape/{}'.format(example))
    for example in ['simple.py']
}

preamble = html.Div([

    reusable_components.Markdown(dedent('''
    # Dash Cytoscape

    ''')),

    html.Iframe(
        src="https://ghbtns.com/github-btn.html?user=plotly&repo=dash-cytoscape&type=star&count=true&size=large",
        width="160px",
        height="30px",
        style={'border': 'none'}
    ),

    reusable_components.Markdown(dedent('''
    > Released on February 5th, 2019**
    >
    > Dash Cytoscape is a graph visualization component for creating easily
    > customizable, high-performance, interactive, and web-based networks. It
    > extends and renders [Cytoscape.js](http://js.cytoscape.org), and
    > offers deep integration with Dash layouts and callbacks, enabling the
    > creation of powerful networks in conjunction with the rich collection of
    > Dash components, as well as established computational biology and network
    > science libraries such as Biopython and networkX.
    >
    > -- xhlulu and the Dash Team
    ''')),

    Section('Quickstart', [
        reusable_components.Markdown(
            '''
            ```shell
            pip install dash-cytoscape=={}
            ```
            '''.format(dash_cytoscape.__version__),
            style=styles.code_container
        ),

        reusable_components.Markdown(
            examples['simple.py'][0],
            style=styles.code_container
        ),

        html.Div(examples['simple.py'][1], className='example-container'),

        reusable_components.Markdown(dedent('''
        > Dash Cytoscape graphs are interactive! Scroll to zoom and drag on
        > the canvas to move the entire graph around. You can move nodes by
        > *dragging* it, or by *clicking, holding, and moving your mouse*
        > to the desired location (and click again to release).
        >
        > This also work in mobile! Tap-and-hold on a node to move it, or on
        > the canvas to move the entire graph. Pinch your fingers outwards to
        > zoom in, or pinch them together to zoom out.
        ''')),
    ]),

    Section('Dash Cytoscape User Guide', [])

])
