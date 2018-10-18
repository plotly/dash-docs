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
    for example in ['interactivity_simple.py', 'interactivity_connected_to_graph.py']
}

layout = html.Div(
    [

        dcc.Markdown(
            dedent(
                """
        # Dash Table Interactivity

        `Table` includes several features for modifying and transforming the
        view of the data. These include:

        - Sorting by column (`sorting=True`)
        - Filtering by column (`filtering=True`)
        - Editing the cells (`editable=True`)
        - Deleting rows (`row_deletable=True`)
        - Deleting columns (`columns[i].deletable=True`)
        - Selecting rows (`row_selectable='single' | 'multi'`)

        > A quick note on filtering. We have defined our own
        > syntax for performing filtering operations. Here are some
        > examples for this particular dataset:
        > - `lt num(50)` in the `lifeExp` column
        > - `eq "Canada"` in the `country` column
        """
            )
        ),

        dcc.SyntaxHighlighter(
            examples['interactivity_simple.py'][0],
            language='python',
            customStyle=styles.code_container
        ),

        html.Div(
            examples['interactivity_simple.py'][1],
            className='example-container'
        ),

            dcc.Markdown(dedent(
        """
        By default, these transformations are done clientside.
        Your Dash callbacks can respond to these modifications
        by listening to the `dataframe` property as an `Input`.

        Note that if `dataframe` is an `Input` then the entire
        `dataframe` will be passed over the network: if your dataframe is
        large, then this will become slow. For large dataframes, you have
        two options:
        - Use `dataframe_indicies` instead
        - Perform the sorting or filtering in Python instead

        Issues with this example:
        - Row selection callbacks don't work yet: `derived_viewport_indices`
        isn't getting updated on row selection and `selected_rows` doesn't
        track the underlying data (e.g. it will always be [1, 3] even after sorting or filtering)
        """
        )),

        dcc.SyntaxHighlighter(
            examples['interactivity_connected_to_graph.py'][0],
            language='python',
            customStyle=styles.code_container
        ),

        html.Div(
            examples['interactivity_connected_to_graph.py'][1],
            className='example-container'
        ),

    ]
)
