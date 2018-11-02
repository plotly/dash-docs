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
    for example in ['interactivity_connected_to_graph.py']
}

layout = html.Div(
    [

        dcc.Markdown(
            dedent(
                """
        # DataTable Interactivity

        `Table` includes several features for modifying and transforming the
        view of the data. These include:

        - Sorting by column (`sorting=True`)
        - Filtering by column (`filtering=True`)
        - Editing the cells (`editable=True`)
        - Deleting rows (`row_deletable=True`)
        - Deleting columns (`columns[i].deletable=True`)
        - Selecting rows (`row_selectable='single' | 'multi'`)

        A quick note on filtering. We have defined our own
        syntax for performing filtering operations. Here are some
        examples for this particular dataset:

        - Enter `eq "Asia"` in the "continent" column
        - Enter `> num(5000)` in the "gdpPercap" column
        - Enter `< num(80)` in the `lifeExp` column

        > Note that you need to wrap strings in double quotes (`"`) and
        > numbers in `num`.
        > We will improve this syntax in the future,
        > follow [dash-table#169](https://github.com/plotly/dash-table/issues/169)
        > for more.

        """
            )
        ),

            dcc.Markdown(dedent(
        """
        By default, these transformations are done clientside.
        Your Dash callbacks can respond to these modifications
        by listening to the `data` property as an `Input`.

        Note that if `data` is an `Input` then the entire
        `data` will be passed over the network: if your dataframe is
        large, then this will become slow. For large dataframes, you can
        perform the [sorting or filtering in Python instead](/datatable/callbacks).
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
