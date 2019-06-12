from collections import OrderedDict
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

import dash_table
from .utils import CreateDisplay

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(data)

data_election = OrderedDict(
    [
        (
            "Date",
            [
                "July 12th, 2013 - July 25th, 2013",
                "July 12th, 2013 - August 25th, 2013",
                "July 12th, 2014 - August 25th, 2014",
            ],
        ),
        (
            "Election Polling Organization",
            ["The New York Times", "Pew Research", "The Washington Post"],
        ),
        ("Rep", [1, -20, 3.512]),
        ("Dem", [10, 20, 30]),
        ("Ind", [2, 10924, 3912]),
        (
            "Region",
            [
                "Northern New York State to the Southern Appalachian Mountains",
                "Canada",
                "Southern Vermont",
            ],
        ),
    ]
)

df_election = pd.DataFrame(data_election)
df_long = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)
df_long_columns = pd.DataFrame(
    {
        "This is Column {} Data".format(i): [1, 2]
        for i in range(10)
    }
)

Display = CreateDisplay({
    'dash_table': dash_table,
    'df': df,
    'df_election': df_election,
    'df_long': df_long,
    'df_long_columns': df_long_columns,
    'pd': pd
})


layout = html.Div(
    style={"marginLeft": "auto", "marginRight": "auto", "width": "80%"},
    children=[

        html.H1("Styling the DataTable"),

        dcc.Markdown("## Default Styles"),

        dcc.Markdown(dedent(
        """
        By default, the DataTable has grey headers and borders
        around each cell. It resembles a spreadsheet and the headers are
        clearly defined.
        """
        )),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
        )
        '''
        ),

        dcc.Markdown(dedent(
        """
        ## Column Alignment

        When displaying numerical data, it's a good practice to use
        monospaced fonts, to right-align the data, and to provide the same
        number of decimals throughout the column.

        > Note that it's not possible to modify the number of decimal places
        > in css. `dash-table` will provide formatting options in the future,
        > until then you'll have to modify your data before displaying it.
        > Relevant issue: [https://github.com/plotly/dash-table/issues/189](https://github.com/plotly/dash-table/issues/189)

        For textual data, left-aligning the text is usually easier to read.

        In both cases, the column headers should have the same alignment
        as the cell content.
        """
        )),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell={'textAlign': 'left'},
            style_cell_conditional=[
                {
                    'if': {'column_id': 'Region'},
                    'textAlign': 'left'
                }
            ]
        )
        '''
        ),

        dcc.Markdown(dedent('''
        ## Styling the Table as a List
        The gridded view is a good default view for an editable table as it looks and feels like a spreadsheet.
        If your table isn't editable, then in many cases it can look cleaner without the
        vertical grid lines.
        ''')),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'left'
                } for c in ['Date', 'Region']
            ],

            style_as_list_view=True,
        )
        '''
        ),

        dcc.Markdown('## List Style with Minimal Headers'),

        dcc.Markdown(dedent('''
        In some contexts, the grey background can look a little heavy.
        You can lighten this up by giving it a white background and
        a bold text.
        ''')),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_as_list_view=True,
            style_cell={'padding': '5px'},
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold'
            },
            style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'left'
                } for c in ['Date', 'Region']
            ],
        )
        '''
        ),

        dcc.Markdown(dedent('''
        ## Striped Rows

        When you're viewing datasets where you need to compare values within
        individual rows, it can sometimes be helpful to give the rows
        alternating background colors.
        We recommend using colors that are faded so as to
        not attract too much attention to the stripes.
        ''')),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            style_cell_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                }
            ] + [
                {
                    'if': {'column_id': c},
                    'textAlign': 'left'
                } for c in ['Date', 'Region']
            ],
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold'
            }
        )
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            style_cell_conditional=[{
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }]
        )
        '''),

        dcc.Markdown(dedent(
        '''
        ## Multi-Headers

        Multi-headers are natively supported in the `DataTable`.
        Just set `name` inside `columns` as a list of strings instead of a
        single string and toggle `merge_duplicate_headers=True`.
        `DataTable` will check the neighbors of each header row and, if they
        match, will merge them into a single cell automatically.
        '''
        )),
        Display(
        '''
        dash_table.DataTable(
            columns=[
                {"name": ["", "Year"], "id": "year"},
                {"name": ["City", "Montreal"], "id": "montreal"},
                {"name": ["City", "Toronto"], "id": "toronto"},
                {"name": ["City", "Ottawa"], "id": "ottawa", "hidden": True},
                {"name": ["City", "Vancouver"], "id": "vancouver"},
                {"name": ["Climate", "Temperature"], "id": "temp"},
                {"name": ["Climate", "Humidity"], "id": "humidity"},
            ],
            data=[
                {
                    "year": i,
                    "montreal": i * 10,
                    "toronto": i * 100,
                    "ottawa": i * -1,
                    "vancouver": i * -10,
                    "temp": i * -100,
                    "humidity": i * 5,
                }
                for i in range(10)
            ],
            merge_duplicate_headers=True,
        )
        '''),

        dcc.Markdown('## Dark Theme with Cells'),

        dcc.Markdown(dedent(
        """
        You have full control over all of the elements in the table.
        If you are viewing your table in an app with a dark background,
        you can provide inverted background and font colors.
        """
        )),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white'
            },
        )
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            style_as_list_view=True,
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white'
            },
        )
        '''),

        dcc.Markdown(dedent('''
        ## Conditional Formatting - Highlighting Certain Rows
        You can draw attention to certain rows by providing a unique
        background color, bold text, or colored text.
        ''')),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            style_data_conditional=[{
                "if": {"row_index": 4},
                "backgroundColor": "#3D9970",
                'color': 'white'
            }]
        )
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            style_as_list_view=True,
            style_data_conditional=[{
                "if": {"row_index": 4},
                "fontWeight": "bold"
            }]
        )
        '''),

        dcc.Markdown('## Conditional Formatting - Highlighting Columns'),

        dcc.Markdown(dedent('''
        Similarly, certain columns can be highlighted.
        ''')),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {'name': i, 'id': i} for i in df.columns
            ],
            style_data_conditional=[{
                'if': {'column_id': 'Temperature'},
                'backgroundColor': '#3D9970',
                'color': 'white',
            }]
        )
        '''
        ),

        dcc.Markdown('## Conditional Formatting - Highlighting Cells'),

        dcc.Markdown(dedent('''
        You can also highlight certain cells. For example, you may want to
        highlight certain cells that exceed a threshold or that match
        a filter elsewhere in the app.

        The `filter` keyword in `style_data_conditional` uses the same
        filtering expression language as the table's interactive filter UI.
        See the [DataTable filtering chapter](/datatable/filtering) for more
        info.

        > Note, the filtering expression language is subject to change.
        > Please subscribe to [dash-table#169](https://github.com/plotly/dash-table/issues/169)
        > for more info.
        ''')),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {'name': i, 'id': i} for i in df.columns
            ],
            style_data_conditional=[
                {
                    'if': {
                        'column_id': 'Region',
                        'filter': '{Region} eq "Montreal"'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                },
                {
                    'if': {
                        'column_id': 'Humidity',
                        'filter': '{Humidity} eq 20'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                },
                {
                    'if': {
                        'column_id': 'Temperature',
                        'filter': '{Temperature} > 3.9'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                },
            ]
        )
        '''
        ),

    ]
)
