import dash_html_components as html
import dash_core_components as dcc
from textwrap import dedent

from tutorial import tools
from tutorial import styles


examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in [
        'editing_simple.py',
        'editing_prune_empty_cells.py',
        'editing_uploading.py',
        'editing_columns.py',
        'editing_rows_and_columns.py',
        'editing_updating_self.py'
    ]
}



layout = html.Div([

    dcc.Markdown(dedent(
    '''
    # Editable DataTable

    The DataTable is editable. Like a spreadsheet, it can be used
    as an input for controlling models with a variable number
    of inputs.

    This chapter includes recipes for:

    - Reading the contents of the DataTable
    - Filtering out null values
    - Uploading data
    - Determining which cell has changed
    - Adding or removing columns
    - Adding or removing rows

    ***

    ## Predefined Columns

    In this example, we initialize a table with 10 blank rows and
    a few predefined columns. To retrieve the data, just listen to the
    `data` property.

    A few notes:
    - If you copy and paste data that is larger than the rows, then the
    table will expand to contain the contents.
    Try it out by [copying and pasting this dataset](https://docs.google.com/spreadsheets/d/1MWj7AjngD_fH7vkVhEMIRo51Oty295kE36-DFnQElrg/edit?usp=sharing).
    - Unlike other spreadsheet programs, the DataTable has a fixed number of
    rows. So, your model has an arbitrary number of parameters
    (rows or columns), we recommend initializing your table with a
    large number of empty rows and columns.
    ''')),

    dcc.Markdown(
        examples['editing_simple.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['editing_simple.py'][1],
        className='example-container'
    ),

    dcc.Markdown(dedent('''
    ## Filtering out Empty Cells
    The DataTable will always return all of the cells in the table, even
    if the cells haven't been filled out. So, you'll likely want to filter
    out the empty values.

    When you clear a cell, the DataTable will set its contents to `''`
    (emtpy string). So, for consistency, we recommend initializing your
    empty data with `''`.

    > Heads up! In the future, when we introduce proper data types,
    > we may initialize empty data as something other than `''`. For example,
    > if the column is numerical, we'll want to avoid having any `''` in the
    > data and we may initialize emty data to `None` instead.

    In this example, we prune away any rows that have empty cells in them.
    This is just one way to prune data, you may want to clean your data
    differently in your application.

    ''')),

    dcc.Markdown(
        examples['editing_prune_empty_cells.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['editing_prune_empty_cells.py'][1],
        className='example-container'
    ),


    dcc.Markdown(dedent('''
    ## Uploading Data

    A nice recipe is to tie the [`dcc.Upload`](https://dash.plot.ly/dash-core-components/upload)
    with the Table component. After the user has uploaded the data, they
    could edit the contents or rename the rows.

    Here's an example that creates a simple "x-y" plotter: upload a CSV
    with two columns of data and we'll plot it.
    Try it out by [downloading this file](https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv)
    and then uploading it.
    '''
    )),

    dcc.Markdown(
        examples['editing_uploading.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['editing_uploading.py'][1],
        className='example-container'
    ),

    dcc.Markdown(dedent(
    '''
    ## Adding or removing columns

    In the DataTable, we've provided a built-in UI for _deleting_ columns
    but not for adding columns. We recommend using an external button to
    add columns.

    This is a simple example that plots the data in the spreadsheet as a
    heatmap. Try adding or removing columns!
    ''')),

    dcc.Markdown(
        examples['editing_columns.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['editing_columns.py'][1],
        className='example-container'
    ),

    dcc.Markdown(dedent(
    '''
    ## Adding or removing rows

    Similarly as columns, the DataTable has a built-in UI for removing rows
    but not for adding rows. You can add rows to the table through an
    external button.
    '''
    )),

    dcc.Markdown(
        examples['editing_rows_and_columns.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['editing_rows_and_columns.py'][1],
        className='example-container'
    ),

    dcc.Markdown(dedent(
    '''
    ## Updating Columns of the Same Table

    One neat application of DataTable is being able to update the table itself
    when you edit cells.

    One of the limitations in Dash is that a callback's `Output` can't be
    the same as the `Input` (circular dependencies aren't supported yet).
    So, we couldn't have `Output('table', 'data')` _and_
    `Input('table', 'data')` in the same `@app.callback`.

    However, we can work around this by using `State('table', 'data')`
    and triggering the callback with `Input('table', 'data_timestamp')`.

    This example mimics a traditional spreadsheet like excel by computing
    certain columns based off of other other columns.
    '''
    )),

    dcc.Markdown(
        examples['editing_updating_self.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['editing_updating_self.py'][1],
        className='example-container'
    ),

])
