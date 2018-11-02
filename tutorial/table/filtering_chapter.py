import dash_html_components as html

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

from tutorial import tools
from tutorial import styles


examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in ['filtering_fe.py', 'filtering_be.py']
}

layout = html.Div(
    [
        dcc.Markdown(dedent(
        """
        # DataTable Filtering Syntax

        As discussed in the [interactivity chapter](), `DataTable` includes
        filtering capabilities. Users can turn on filtering options by defining
        the `filtering` attribute. `filtering=True` will initiate clientside
        (frontend) filtering. Alternatively you can specify `filtering='fe'`.
        If the DataTable is quite large, clientside filtering will likely
        become slow. Using the backend filtering option: `filtering='be'`
        will allow serverside filtering. At this time, the filter syntax for
        frontend and backend filtering differs slightly.

        > Note that we plan on improving
        > the simplicity and consistency of
        > this syntax in the near future.
        > Follow [dash-table#169](https://github.com/plotly/dash-table/issues/169)
        > for updates.

        ## Frontend Filtering

        Filtering supports equals: `eq`, greater than: `>`, and less than: `<`
        operations.
        - Strings must be wrapped in double quotes: `eq "Asia"`
        - Numerical values must be wrapped in num(): `> num(500)`

        > Note that at this time, frontend filtering must be connected to a
        > callback in order to work. See [dash-table#202](https://github.com/plotly/dash-table/issues/202)
        > for progress on this issue.

        In the example below:
        - Enter `eq "Asia"` in the "continent" column
        - Enter `> num(5000)` in the "gdpPercap" column
        - Enter `< num(80)` in the `lifeExp` column

        """
            )
        ),

        dcc.SyntaxHighlighter(
            examples['filtering_fe.py'][0],
            language='python',
            customStyle=styles.code_container
        ),

        html.Div(
            examples['filtering_fe.py'][1],
            className='example-container'
        ),

        dcc.Markdown(dedent(
        """
        ## Backend Filtering

        For large dataframes, you can perform the filtering in Python instead
        of the default clientside filtering. You can find more information on
        performing operations in python in the [Python Callbacks chapter](/datatable/callbacks).

        As mentioned above, the backend filtering syntax currently differs
        slightly from the frontend syntax.

        BAckend filtering supports equals: `eq`, greater than: `>`, and less
        than: `<` operations.
        - No quotes necessary for text: `eq Asia`
        - Numerical values accepted: `> 500`

        In the example below:
        - Enter `eq Asia` in the "continent" column
        - Enter `> 5000` in the "gdpPercap" column
        - Enter `< 80` in the `lifeExp` column
        """
        )),

        dcc.SyntaxHighlighter(
            examples['filtering_be.py'][0],
            language='python',
            customStyle=styles.code_container
        ),

        html.Div(
            examples['filtering_be.py'][1],
            className='example-container'
        ),
    ]
)
