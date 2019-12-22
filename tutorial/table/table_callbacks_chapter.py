from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

import dash_table
from tutorial import styles, tools


examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in [
        'callbacks_paging.py',
        'callbacks_paging_and_sorting.py',
        'callbacks_paging_multicolumn_sorting.py',
        'callbacks_filtering.py',
        'callbacks_sorting_filtering.py',
        'callbacks_filtering_graph.py'
    ]
}

layout = html.Div([
    dcc.Markdown('# DataTable - Python Callbacks'),

    dcc.Markdown(dedent(
    '''
    ### Backend Paging

    With backend paging, we can load data into our table progressively.
    Instead of loading all of the data at once, we'll only load data
    as the user requests it when they click on the "previous" and "next"
    buttons.

    Since backend paging integrates directly with your Dash callbacks, you can
    load your data from any Python data source.
    ''')),

    dcc.Markdown(
        examples['callbacks_paging.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['callbacks_paging.py'][1],
        className='example-container'
    ),

    html.Hr(),

    dcc.Markdown(dedent('''
    With backend paging, we can have front-end sorting and filtering
    but it will only filter and sort the data that exists on the page.

    This should be avoided. Your users will expect
    that sorting and filtering is happening on the entire dataset and,
    with large pages, might not be aware that this is only occuring
    on the current page.

    Instead, we recommend implmenting sorting and filtering on the
    backend as well. That is, on the entire underlying dataset.

    **Note for returning users - changed property names:**
    - Sorted fields are now in `sort_by`, not `sorting_settings`
    - The filter string is now in `filter`, not `filtering_settings`
    ''')),

    dcc.Markdown('### Backend Paging with Sorting'),

    dcc.Markdown(
        examples['callbacks_paging_and_sorting.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['callbacks_paging_and_sorting.py'][1],
        className='example-container'
    ),

    dcc.Markdown('### Backend Paging with Multi Column Sorting'),

    dcc.Markdown(dedent('''
    Multi-column sort allows you to sort by multiple columns.
    This is useful when you have categorical columns with repeated
    values and you're interested in seeing the sorted values for
    each category.

    In this example, try sorting by continent and then any other column.
    ''')),

    dcc.Markdown(
        examples['callbacks_paging_multicolumn_sorting.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['callbacks_paging_multicolumn_sorting.py'][1],
        className='example-container'
    ),

    dcc.Markdown('### Backend Paging with Filtering'),

    dcc.Markdown(dedent('''
    DataTable's front-end filtering has its own filtering expression
    language.

    Currently, backend filtering must parse the same filtering language.
    If you write an expression that is not "valid" under the filtering
    language, then it will not be passed to the backend.

    This limitation will be removed in the future to allow you to
    write your own expression query language.

    In this example, we've written a Pandas backend for the filtering
    language. It supports `eq`, `<`, and `>`. For example, try:

    - Enter `eq Asia` in the "continent" column
    - Enter `> 5000` in the "gdpPercap" column
    - Enter `< 80` in the `lifeExp` column

    > Note that unlike the front-end filtering, our backend filtering
    > expression language doesn't require or support `num()` or wrapping
    > items in double quotes (`"`).
    > We will improve this syntax in the future,
    > follow [dash-table#169](https://github.com/plotly/dash-table/issues/169)
    > for more.

    ''')),

    dcc.Markdown(
        examples['callbacks_filtering.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['callbacks_filtering.py'][1],
        className='example-container'
    ),

    dcc.Markdown('### Backend Paging with Filtering and Multi-Column Sorting'),
    dcc.Markdown(
        examples['callbacks_sorting_filtering.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['callbacks_sorting_filtering.py'][1],
        className='example-container'
    ),

    dcc.Markdown('### Connecting Backend Paging with a Graph'),

    dcc.Markdown(dedent('''
    This final example ties it all together: the graph component
    displays the current page of the `data`.
    ''')),
    dcc.Markdown(
        examples['callbacks_filtering_graph.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['callbacks_filtering_graph.py'][1],
        className='example-container'
    ),

])
