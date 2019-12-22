import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

from reusable_components import Section, Chapter
from tutorial import styles
from tutorial import tools


examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in ['simple.py']
}


layout = html.Div([

    dcc.Markdown(dedent('''
    # Dash DataTable

    ''')),

    html.Iframe(
        src="https://ghbtns.com/github-btn.html?user=plotly&repo=dash-table&type=star&count=true&size=large",
        width="160px",
        height="30px",
        style={'border': 'none'}
    ),

    dcc.Markdown(dedent('''
    > **Released on November 2, 2018**
    >
    > Dash DataTable is an interactive table component designed for
    > viewing, editing, and exploring large datasets.
    >
    > DataTable is rendered with standard, semantic HTML `<table/>` markup,
    > which makes it accessible, responsive, and easy to style.
    >
    > This component was written from scratch in React.js specifically
    > for the Dash community. Its API was designed to be ergonomic
    > and its behavior is completely customizable through its properties.
    >
    > 7 months in the making, this is the most complex Dash
    > component that Plotly has written, all from the ground-up
    > using React and TypeScript. DataTable was designed with a
    > featureset that allows that Dash users to create complex,
    > spreadsheet driven applications with no compromises.
    > We're excited to continue to work with users and companies
    > that [invest in DataTable's future](https://plot.ly/products/consulting-and-oem/).
    >
    > With `dash-table v4.0.0` - included in `dash v1.0.0` and released on
    > June 20, 2019 - we consider the API stable. We don't expect any
    > breaking changes any time soon, but if there are they will be
    > accompanied by a new major version of dash. If you've been using
    > DataTable with `dash v0.x` / `dash-table v3.x`, check out the
    > [Dash 1.0 Migration Guide](/dash-1-0-migration) for the full list of
    > changes.
    >
    > Otherwise, check out DataTable in the docs below.
    > If you make something cool with it, we'd love to see it! Share it
    > on the [community forum](https://community.plot.ly/t/show-and-tell-community-thread/7554)!
    >
    > -- chriddyp
    ''')),

    Section('Quickstart', [
        dcc.Markdown(
            '''
            ```
            pip install dash=={}
            ```
            '''.format(dash.__version__),
            style=styles.code_container
        ),

        dcc.Markdown(
            examples['simple.py'][0],
            style=styles.code_container
        ),

        html.Div(examples['simple.py'][1], className='example-container'),

    ]),

    Section('Dash DataTable User Guide', [
        Chapter('Part 1. Sizing',
            '/datatable/sizing',
            '''
            All about sizing the DataTable. Examples include:
            - Setting the width and the height of the table
            - Responsive table design
            - Setting the widths of individual columns
            - Handling long text
            - Fixing rows and columns

            '''),

        Chapter('Part 2. Styling',
            '/datatable/style',
            '''
            The style of the DataTable is highly customizable. This chapter
            includes examples for:
            - Conditional formatting
            - Displaying multiple rows of headers
            - Highlighting rows, columns, and cells
            - Styling the table as a list view
            - Changing the colors (including a dark theme!)

            The sizing API for the table has been particularly tricky for
            us to nail down, so be sure to read this chapter to understand the nuances,
            limitations, and the APIs that we're exploring.

            '''),

        Chapter('Part 3. Sorting, Filtering, Selecting, and Paging',
            '/datatable/interactivity',
            '''
            The DataTable is interactive. This chapter demonstrates the
            interactive features of the table and how to wire up these
            interations to Python callbacks. These actions include:
            - Paging
            - Selecting Rows
            - Sorting Columns
            - Filtering Data
            '''),

        Chapter([html.Span('Part 4. Sorting, Filtering, and Paging '), html.I('with Python')],
            '/datatable/callbacks',
            '''
            In Part 3, the paging, sorting, and filtering was done entirely
            clientside (in the browser). This means that you need to
            load all of the data into the table up-front. If your data is large,
            then this can be prohibitively slow.

            In this chapter, you'll learn how to write your own filtering,
            sorting, and paging backends in Python with Dash.
            We'll do the data processing with Pandas but you could write your
            own routines with SQL or even generate the data on the fly!
            '''),

        Chapter([html.Span('Part 5. Typing ')],
            '/datatable/typing',
            '''
            In this chapter, you'll learn how to configure the table to
            - assign the column type
            - change the data presentation
            - change the data formatting
            - validate or coerce user data input
            - apply default behavior for valid and invalid data
            '''),

        Chapter('Part 6. Editable Tables',
            '/datatable/editable',
            '''
            The DataTable is editable. Like a spreadsheet, it can be used
            as an input for controlling models with a variable number
            of inputs.

            This chapter includes recipes for:

            - Determining which cell has changed
            - Filtering out null values
            - Adding or removing columns
            - Adding or removing rows
            - Ensuring that a minimum set of rows are visible
            - Running Python computations on certain columns or cells
            '''),

        Chapter('Part 7. Rendering Cells as Dropdowns',
            '/datatable/dropdowns',
            '''
            Cells can be rendered as editable Dropdowns. This is our first
            stake in bringing a full typing system to the table.
            Rendering cells as dropdowns introduces some complexity in the
            markup and so there are a few limitations that you should be aware
            of.
            '''),

        Chapter('Part 8. Virtualization',
            '/datatable/virtualization',
            '''
            Examples using DataTable virtualization.
            '''),

        Chapter('Part 9. Filtering Syntax',
            '/datatable/filtering',
            '''
            An explanation and examples of filtering syntax for both frontend
            and backend filtering in the DataTable.
            '''),

        Chapter('Part 10. Table Reference',
            '/datatable/reference',
            '''
            The full list of Table properties and their settings.
            ''')
    ]),

    Section('Roadmap, Sponsorships, and Contact', dcc.Markdown(dedent(
    '''
    Immediately, we're working on stability, virtualization, and
    a first-class data type system.
    Check out [our roadmap project board](https://github.com/orgs/plotly/projects/12)
    to see what's coming next.

    Many thanks to all of our customers who have sponsored the
    development of this table. Interested in steering the roadmap?
    [Get in touch](https://plot.ly/products/consulting-and-oem/)
    '''
    )))
])
