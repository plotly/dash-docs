import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape
from textwrap import dedent

from reusable_components import Section, Chapter
from tutorial import styles
from tutorial import tools

examples = {
    example: tools.load_example('tutorial/examples/cytoscape/{}'.format(example))
    for example in ['simple.py']
}

layout = html.Div([

    dcc.Markdown(dedent('''
    # Dash Cytoscape

    ''')),

    html.Iframe(
        src="https://ghbtns.com/github-btn.html?user=plotly&repo=dash-cytoscape&type=star&count=true&size=large",
        width="160px",
        height="30px",
        style={'border': 'none'}
    ),

    dcc.Markdown(dedent('''
    > **New! Released on February 5th, 2019**
    >
    > Dash Cytoscape is a graph visualization component for creating easily
    > customizable, high-performance, interactive, and web-based networks. It
    > extends and renders [Cytoscape.js](http://js.cytoscape.org), and
    > offers deep integration with Dash layouts and callbacks, enabling the
    > creation of powerful networks in conjunction with the rich collection of
    > Dash components, as well as established computational biology and network
    > science libraries such as Biopython and networkX.
    >
    > -- xhlulu
    ''')),

    Section('Quickstart', [
        dcc.Markdown(
            '''
            ```
            pip install dash-cytoscape=={}
            ```
            '''.format(dash_cytoscape.__version__),
            style=styles.code_container
        ),

        dcc.Markdown(
            examples['simple.py'][0],
            style=styles.code_container
        ),

        html.Div(examples['simple.py'][1], className='example-container'),

    ]),

    Section('Dash Cytoscape User Guide', [
        dcc.Markdown(dedent('''
        > Dash Cytoscape graphs are interactive! Scroll to zoom and drag on
        > the canvas to move the entire graph around. You can move nodes by
        > *dragging* it, or by *clicking, holding, and moving your mouse*
        > to the desired location (and click again to release).
        >
        > This also work in mobile! Tap-and-hold on a node to move it, or on
        > the canvas to move the entire graph. Pinch your fingers outwards to
        > zoom in, or pinch them together to zoom out.
        ''')),

        Chapter(
            'Part 1. Elements',
            '/cytoscape/elements',
            '''
            Elements in Cytoscape are designed to be clear, simple and
            declarative. This chapter will get you started with examples
            for:
            - Data and position dictionaries
            - Mutability properties
            - Defining groups and classes
            - Compound nodes
            '''
        ),

        Chapter(
            'Part 2. Layout',
            '/cytoscape/layout',
            '''
            Make your graphs interpretable by using the built-in
            collection of easy-to-modify layouts. We show you how to:
            - Display pre-determined and random layouts
            - Represent your graph as a circle, a grid or a tree
            - Finetune your representations by modifying the default options
            - Use physics-based simulations to generate your layout
            '''
        ),

        Chapter(
            'Part 3. Styling',
            '/cytoscape/styling',
            '''
            Modify the color, shape and style of your elements with a syntax
            similar to CSS. Cytoscape incldues a wide variety of properties,
            equiping you with everything you need to display your graphs with
            aesthetics, creativity, and understandability in mind. This chapter
            covers:
            - Basic style properties for nodes and edges
            - Using selectors to modify specific groups of elements
            - Organize your edges with curve and line properties
            - Advanced node styling with pie charts and images
            '''
        ),

        Chapter(
            'Part 4. Dash Callbacks',
            '/cytoscape/callbacks',
            '''
            Update your layout, elements, or style with other Dash components
            using callbacks. This chapter covers:
            - Adding and removing elements
            - Modifying the layout and the stylesheet
            - Advanced usage of callbacks
            '''
        ),

        Chapter(
            'Part 5. Event Callbacks for User Interactions',
            '/cytoscape/events',
            '''
            Dash Cytoscape fires callbacks whenever the user interact with the
            graph you created, which can be used to update the graph itself,
            or to interact with other components. This chapter includes
            examples for:
            - Simple integrations with HTML components
            - Different types of data returned
            - Node versus edges callbacks
            - Tap, hover or select callbacks
            '''
        ),

        Chapter(
            'Part 6. Cytoscape with Biopython',
            '/cytoscape/biopython',
            '''
            We show how Dash Cytoscape can be applied can be applied in
            bioinformatics and computational biology. We will go through the
            process of building a phylogeny tree using the Biopython library.\
            '''
        ),


        Chapter(
            'Part 7. Component Reference',
            '/cytoscape/reference',
            '''
            You can find here all the properties of the `Cytoscape` component.
            '''
        )
    ]),

    Section('Roadmap, Sponsorships, and Contact', dcc.Markdown(dedent(
        '''
        In the near future, we would like to support integration with
        biopython and networkX, expand object-oriented declarations, and offer more
        support for layout options. Check out our [open issues](https://github.com/plotly/dash-cytoscape/issues)
        for more details.

        The development for this component was sponsored by one of our
        commercial partners. Interested in steering the roadmap?
        [Get in touch](https://plot.ly/products/consulting-and-oem/).
        '''
    )))
])
