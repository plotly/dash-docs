import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from textwrap import dedent
import dash_table

from reusable_components import Section, Chapter
from tutorial import styles
from tutorial import tools


examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in ['simple.py']
}


layout = html.Div([

    dcc.Markdown(dedent('''
    # Dash Interactive Table

    **New! Released in October, 2018**

    The Dash Table is an interactive table component designed for
    viewing, editing, and exploring large datasets.

    It's rendered with standard, semantic `<table/>` markup, making it
    easy to style, accessible, and responsive.

    This component was written from scratch in React.js
    specifically for the Dash community. Its API was designed to be
    ergonomic and its behavior is completely customizable through its
    properties.

    This is the most complex component that we've written as a pure React
    Dash component. It's already feature-rich and we're excited to
    continue to invest in its future.

    Dash Table is in `alpha`. This is more of a statement on its API rather
    than on its features. The table works really well right now, we just
    expect to make a few more breaking changes to its API and behavior
    within the next 6 months. Once the community feels good about its API,
    we'll lock it down and we'll commit to reducing the
    frequency of breaking changes.

    So, use the table and let us know what you think. Keep an eye
    on the [CHANGELOG.md](/CHANGELOG.md) to be aware of breaking changes,
    upgrade guides, and new features.

    ''')),

    Section('Quickstart', [
        dcc.SyntaxHighlighter(
            '''pip install dash-table=={}'''.format(dash_table.__version__),
            customStyle=styles.code_container
        ),

        dcc.SyntaxHighlighter(
            examples['simple.py'][0],
            language='python',
            customStyle=styles.code_container
        ),

        html.Div(examples['simple.py'][1], className='example-container'),

    ]),

    Section('Dash Interactive Table User Guide', [
        Chapter('Part 1. Styling, Sizing, and Conditional Formatting',
            '/dash-table/styling',
            '''
            Several examples on how to change the style and sizing of the
            table. This includes:
            - Table height, width
            - Text alignment
            - Per-column styles
            - Conditional formatting
            - Fixing rows and columns

            The styling API for the table has been particularly tricky for
            us to nail down, so be read this chapter to understand the nuances,
            limitations, and the APIs that we're exploring.
            '''),

        Chapter('Part 2. Sorting, Filtering, and Paging',
            '/dash-table/interactivity',
            '''
            The Dash Table is interactive. This chapter demonstrates the
            interactive features of the table and how to wire up these
            interations to Python callbacks. These actions include:
            - Paging
            - Selecting Rows
            - Sorting Columns
            - Filtering Data
            '''),

        Chapter([html.Span('Part 3. Sorting, Filtering, and Paging '), html.I('with Python')],
            '/dash-table/callbacks',
            '''
            Learn how to write your own filtering, sorting, and paging backends
            in Python with Dash. This is useful for when your datasets
            become larger than 100,000 rows.
            '''),

        Chapter('Part 4. Editable Tables',
            '/dash-table/recipes',
            '''
            The table can be a good, flexible control for models with many
            parameters.

            If your Python model has several parameters, the table can be a
            good, flexible control.

            If your models have several inputs, the Table can be a good
            This chapter covers some more complex on how to use the table as
            an interactive input, including:
            - On edit, determining which cell has changed
            - Filtering out null values
            - Adding or removing columns
            - Keeping a minimum set of rows visible
            '''),

        Chapter('Part 5. Rendering Cells as Dropdowns',
            '/dash-table/dropdowns',
            '''
            Cells can be rendered as editable Dropdowns. This is our first
            stake in bringing a full typing system to the table.
            Rendering cells as dropdowns introduces some complexity in the
            markup and so there are a few limitations that you should be aware
            of.
            '''),

        Chapter('Part 6. Table Reference',
            '/dash-table/reference',
            '''
            The full list of Table properties and their settings.
            '''
        )
    ]),

    Section('Roadmap, Sponsorships, and Contact', dcc.Markdown(dedent(
    '''
    Immediately, we're working on stability, virtualization, and
    a first-class data type system.
    Check out [our roadmap project board](https://github.com/orgs/plotly/projects/12)
    to see what's coming next.

    Many thanks to all of our customers who have sponsored the
    development of this table <3. Interested in steering the roadmap?
    [Get in touch](https://plot.ly/products/consulting-and-oem/)
    '''
    )))
])
