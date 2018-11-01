from collections import OrderedDict
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

import dash_table
from .utils import html_table

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10"] * 2),
        ("Region", ["Montreal", "Vermont", "New York City"] * 2),
        ("Temperature", [1, -20, 3.512] * 2),
        ("Humidity", [10, 20, 30] * 2),
        ("Pressure", [2, 10924, 3912] * 2),
    ]
)

df = pd.DataFrame(data)

data = OrderedDict(
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

df_election = pd.DataFrame(data)
df_long = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)
df_long_columns = pd.DataFrame(
    {
        "This is Column {} Data".format(i): [1, 2]
        for i in range(10)
    }
)


def Display(example_string):
    return html.Div([
        dcc.SyntaxHighlighter(
            dedent(example_string).strip(),
            language='python',
            customStyle={'marginBottom': 10, 'borderLeft': 'thin #C8D4E3 solid'}
        ),
        eval(dedent(example_string), {
            'dash_table': dash_table,
            'df': df,
            'df_election': df_election,
            'df_long': df_long,
            'df_long_columns': df_long_columns,
            'pd': pd
        })
    ])


layout = html.Div(
    style={"marginLeft": "auto", "marginRight": "auto", "width": "80%"},
    children=[

        html.H1('Sizing and Styling'),

        html.H3('Default Style'),
        dcc.Markdown(dedent(
        '''
        By default, the width of the table's columns will expand to
        size of the cell's contents. The content will be displayed on a
        single line.
        '''
        )),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns]
        )
        '''
        ),

        html.H3('Responsive Table'),
        dcc.Markdown(dedent(
        '''
        This responsive table will expand to the container's width.
        If you resize your browser, the table will resize and the text
        will become cut-off.
        '''
        )),
        Display(
        '''
        dash_table.DataTable(
            style_table={'width': '100%'},
            content_style='grow',
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns]
        )
        '''
        ),

        html.H3('Responsive Table - Overflowing Into Multiple Lines'),
        dcc.Markdown(dedent(
        '''
        Instead of cutting off the text, you can break the text into multiple
        lines on the word breaks.

        > We find that this interface is a little too complex.
        > We're looking at simplifying this in this issue:
        > [https://github.com/plotly/dash-table/issues/188](https://github.com/plotly/dash-table/issues/188)
        '''
        )),
        Display(
        '''
        dash_table.DataTable(
            style_table={'width': '100%'},
            style_data={'whiteSpace': 'normal'},
            content_style='grow',
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
            data=df_election.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_election.columns]
        )
        '''),
        # html_table(df_election, table_style={"width": "100%"}),

        dcc.Markdown("### Responsive Table - Overflowing Into Ellipses"),
        dcc.Markdown(dedent(
        """
        With `max-width`, the content can collapse into
        ellipses once the content doesn't fit.

        Here, `max-width` is set to 0. It could be any number, the only
        important thing is that it is supplied. The behaviour will be
        the same whether it is 0 or 50.
        """
        )),
        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'width': '100%'},
            content_style='grow',
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
            style_cell={
                'whiteSpace': 'no-wrap',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0,
            },
        )
        '''),

        dcc.Markdown("### All Column Widths defined by Percent"),
        html.Div('The column widths can be definied by percents rather than pixels.'),
        # html_table(
        #     df,
        #     table_style={"width": "100%"},
        #     column_style={
        #         "Date": {"width": "30%"},
        #         "Election Polling Organization": {"width": "25%"},
        #         "Dem": {"width": "5%"},
        #         "Rep": {"width": "5%"},
        #         "Ind": {"width": "5%"},
        #         "Region": {"width": "30%"},
        #     },
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={'width': '100%'},
            content_style='grow',
            style_cell_conditional=[
                {'if': {'column_id': 'Date'},
                 'width': '30%'},
                {'if': {'column_id': 'Election Polling Organization'},
                 'width': '25%'},
                {'if': {'column_id': 'Dem'},
                 'width': '5%'},
                {'if': {'column_id': 'Rep'},
                 'width': '5%'},
                {'if': {'column_id': 'Ind'},
                 'width': '5%'},
                {'if': {'column_id': 'Region'},
                 'width': '30%'},
            ]
        )
        '''),

        dcc.Markdown("### Single Column Width Defined by Percent"),

        html.Div('The width of one column (Region=50%) can be definied by percent.'),
        # html_table(
        #     df,
        #     table_style={"width": "100%"},
        #     column_style={"Region": {"width": "50%"}},
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={'width': '100%'},
            content_style='grow',
            style_cell_conditional=[
                {'if': {'column_id': 'Region'},
                 'width': '50%'},
            ]
        )
        '''),

        dcc.Markdown("### Columns with min-width"),
        dcc.Markdown(dedent(
        '''
        Here, the min-width for the first column is 130px, or about the width of this line:
        ''')),
        html.Div(
            style={"width": 130, "height": 10, "backgroundColor": "hotpink"}
        ),
        # html_table(
        #     df,
        #     table_style={"width": "100%"},
        #     column_style={"Date": {"minWidth": "130"}},
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={'width': '100%'},
            content_style='grow',
            style_cell_conditional=[
                {'if': {'column_id': 'Date'},
                 'minWidth': 130},
            ]
        )
        '''),

        dcc.Markdown("### Underspecified Widths"),
        dcc.Markdown(dedent(
        '''
        The widths can be under-specified. Here, we're only setting the width for
        the three columns in the middle, the rest of the columns are
        automatically sized to fit the rest of the container.
        The columns have a width of 50px, or the width of this line:
        '''
        )),
        html.Div(
            style={"width": 50, "height": 10, "backgroundColor": "hotpink"}
        ),
        # html_table(
        #     df,
        #     table_style={"width": "100%"},
        #     column_style={
        #         "Dem": {"width": 50},
        #         "Rep": {"width": 50},
        #         "Ind": {"width": 50},
        #     },
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={'width': '100%'},
            content_style='grow',
            style_cell_conditional=[
                {'if': {'column_id': 'Dem'},
                 'width': 50},
                {'if': {'column_id': 'Rep'},
                 'width': 50},
                {'if': {'column_id': 'Ind'},
                 'width': 50},
            ]
        )
        '''),

        dcc.Markdown("### Widths that are smaller than the content"),
        dcc.Markdown(dedent(
        '''
        In this case, we're setting the width to 20px, which is smaller
        than the "10924" number in the "Ind" column.
        The table does not allow it.
        '''
        )),
        html.Div(
            style={"width": 20, "height": 10, "backgroundColor": "hotpink"}
        ),
        # html_table(
        #     df,
        #     table_style={"width": "100%"},
        #     column_style={
        #         "Dem": {"width": 20},
        #         "Rep": {"width": 20},
        #         "Ind": {"width": 20},
        #     },
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={'width': '100%'},
            content_style='grow',
            style_cell_conditional=[
                {'if': {'column_id': 'Dem'},
                 'width': 20},
                {'if': {'column_id': 'Rep'},
                 'width': 20},
                {'if': {'column_id': 'Ind'},
                 'width': 20},
            ]
        )
        '''),

        dcc.Markdown("### "),
        dcc.Markdown(dedent(
        '''
        ## Vertical Scrolling
        By supplying a max-height of the Table container and supplying
        `overflow-y: scroll`, the table will become scrollable if the
        table's contents are larger than the container.
        ''')),
        Display(
        '''
        dash_table.DataTable(
            data=df_long.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={
                'maxHeight': '300',
                'overflowY': 'scroll'
            },
        )
        '''),

        dcc.Markdown("### Vertical Scrolling via Fixed Rows"),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            n_fixed_rows=1
        )
        '''),

        dcc.Markdown("### Vertical Scrolling with Max Height"),
        dcc.Markdown(dedent(
        '''
        With `max-height`, if the table's contents are shorter than the
        `max-height`, then the container will be shorter.
        If you want a container with a constant height no matter the
        contents, then use `height`.

        Here, we're setting max-height to 300, or the height of this line:
        ''')),
        html.Div(
            style={"width": 5, "height": 300, "backgroundColor": "hotpink"}
        ),
        # html.Div(
        #     style={"maxHeight": 300, "overflowY": "scroll"},
        #     children=html_table(df, table_style={"width": "100%"}),
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={
                'maxHeight': '300',
                'overflowY': 'scroll'
            },
        )
        '''),

        dcc.Markdown("### Vertical Scrolling with Height"),
        dcc.Markdown("and here is `height` with the same content"),
        # html.Div(
        #     style={"height": 300, "overflowY": "scroll"},
        #     children=html_table(df, table_style={"width": "100%"}),
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={'height': '300', 'overflowY': 'scroll'},
        )
        '''),

        dcc.Markdown(dedent(
        '''
        ## Horizontal Scrolling
        With HTML tables, we can set `min-width` to be 100%.
        If the content is small, then the columns will have some extra
        space.
        But if the content of any of the cells is really large, then the
        cells will expand beyond the container and a scrollbar will appear.

        In this way, `min-width` and `overflow-x: scroll` is an alternative
        to `text-overflow: ellipses`. With scroll, the content that can't
        fit in the container will get pushed out into a scrollable zone.
        With text-overflow: ellipses, the content will get truncated by
        ellipses. Both strategies work with or without line breaks on the
        white spaces (`white-space: normal` or `white-space: nowrap`).

        These next two examples have the same styles applied:
        - `min-width: 100%`
        - `white-space: nowrap` (to keep the content on a single line)
        - A parent with `overflow-x: scroll`
        '''
        )),

        dcc.Markdown("### Two Columns, 100% Min-Width"),
        # html.Div(
        #     html_table(
        #         pd.DataFrame({"Column 1": [1, 2], "Column 2": [3, 3]}),
        #         table_style={"minWidth": "100%"},
        #         cell_style={"whiteSpace": "nowrap"},
        #     ),
        #     style={"overflowX": "scroll"},
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=pd.DataFrame({"Column 1": [1, 2], "Column 2": [3, 3]}).to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in ['Column 1', 'Column 2']],
            style_table={'minWidth': '100%'},
            style_cell={'whiteSpace': 'nowrap'}
        )
        '''),

        dcc.Markdown(dedent(
        '''
        ### Fixed Columns
        dash_table.DataTable(
            data=df_long.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            n_fixed_columns=1
        )
        '''
        )),

        dcc.Markdown("### "),
        dcc.Markdown(dedent(
        '''
        ### Long Columns, 100% Min-Width
        Here is a table with several columns with long titles,
        100% min-width, and `'white-space': 'nowrap'`
        (to keep the text on a single line)
        '''
        )),
        # html.Div(
        #     html_table(
        #         df_long_columns,
        #         table_style={"minWidth": "100%", "overflowX": "scroll"},
        #         cell_style={"whiteSpace": "nowrap"},
        #     ),
        #     style={"overflowX": "scroll"},
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=df_long_columns.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_long_columns.columns],
            style_table={'minWidth': '100%', 'overflowX': 'scroll'},
            style_cell={'whiteSpace': 'nowrap'}
        )
        '''),


        html.H1("Styling the DataTable"),

        dcc.Markdown("### Gridded"),

        html.Div(
        """
        By default, the DataTable has grey headers and borders
        around each cell. It resembles a spreadsheet and the headers are
        clearly defined.
        """
        ),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            content_style='grow',
            style_table={'width': '100%'}
        )
        '''
        ),

        dcc.Markdown(dedent(
        """
        ### Column Alignment and Column Fonts

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
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            content_style='grow',
            style_table={'width': '100%'},
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
        # html_table(
        #     df,
        #     table_style={'width': '100%'},
        #     column_style={'width': '20%', 'paddingLeft': 20},
        #     cell_style={"paddingLeft": 5, "paddingRight": 5, 'border': 'thin lightgrey solid'},
        #     header_style_by_column={
        #         "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
        #     },
        #     cell_style_by_column={
        #         "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
        #     },
        #     header_style={'backgroundColor': 'rgb(235, 235, 235)'}
        # ),

        dcc.Markdown(dedent('''
        ## Styling the Table as a List
        The gridded view is a good default view for an editable table, like a spreadsheet.
        If your table isn't editable, then in many cases it can look cleaner without the
        vertical grid lines.
        ''')),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            content_style='grow',
            style_table={'width': '100%'},
            style_as_list_view=True
        )
        '''
        ),

        # html_table(
        #     df,
        #     table_style={'width': '100%'},
        #     column_style={'width': '20%', 'paddingLeft': 20},
        #     cell_style={"paddingLeft": 5, "paddingRight": 5},
        #     header_style={'backgroundColor': 'rgb(235, 235, 235)', 'borderTop': 'thin lightgrey solid', 'borderBottom': 'thin lightgrey solid'},
        #     header_style_by_column={
        #         "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
        #     },
        #     cell_style_by_column={
        #         "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
        #     },
        # ),

        dcc.Markdown(dedent('''
        ## Row Padding

        By default, the gridded view is pretty tight.
        You can add some top and bottom row padding to
        the rows to give your data a little bit more room to breathe.
        ''')),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell={'padding': '5px'},
            content_style='grow',
            style_table={'width': '100%'}
        )
        '''
        ),

        # html_table(
        #     df,
        #     table_style={'width': '100%'},
        #     column_style={'width': '20%', 'paddingLeft': 20},
        #     cell_style={"paddingLeft": 5, "paddingRight": 5},
        #     header_style={'backgroundColor': 'rgb(235, 235, 235)', 'borderTop': 'thin lightgrey solid', 'borderBottom': 'thin lightgrey solid'},
        #     header_style_by_column={
        #         "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
        #     },
        #     cell_style_by_column={
        #         "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
        #     },
        #     row_style={'paddingTop': 10, 'paddingBottom': 10}
        # ),

        dcc.Markdown('### List Style with Minimal Headers'),

        dcc.Markdown(dedent('''
        In some contexts, the grey background can look a little heavy.
        You can lighten this up by giving it a white background and
        a thicker bottom border.
        ''')),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_as_list_view=True,
            style_cell={'padding': '5px'},
            style_header={
                'backgroundColor': 'white',
                'borderBottom': '2px lightgrey solid'
            },
            content_style='grow',
            style_table={'width': '100%'}
        )
        '''
        ),

        # html_table(
        #     df,
        #     table_style={'width': '100%'},
        #     column_style={'width': '20%', 'paddingLeft': 20},
        #     cell_style={"paddingLeft": 5, "paddingRight": 5},
        #     header_style={'borderBottom': '2px lightgrey solid'},
        #     header_style_by_column={
        #         "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
        #     },
        #     cell_style_by_column={
        #         "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
        #         "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
        #     },
        #     row_style={'paddingTop': 10, 'paddingBottom': 10}
        # ),

        dcc.Markdown(dedent('''
        ## Striped Rows

        When you're viewing datasets where you need to compare values within
        individual rows, it can sometimes be helpful to give the rows
        alternating background colors.
        We recommend using colors that are faded so as to
        not attract too much attention to the stripes.

        In particular, here are some suggested colors:
        - TODO - suggested colors
        ''')),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            content_style='grow',
            style_table={'width': '100%'},
            style_cell_conditional=[{
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }]
        )
        '''),


        dcc.Markdown('### Dark Theme with Cells'),

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
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            content_style='grow',
            style_table={'width': '100%'},
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
            data=df.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            style_as_list_view=True,
            content_style='grow',
            style_table={'width': '100%'},
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white'
            },
        )
        '''),

        dcc.Markdown(dedent('''
        ### Highlighting Certain Rows
        You can draw attention to certain rows by providing a unique
        background color, bold text, or colored text.
        ''')),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict("rows"),
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            content_style="grow",
            style_table={
                "width": "100%"
            },
            style_data_conditional=[{
                "if": {"row_index": 4},
                "backgroundColor": "#3D9970",
                'color': 'white'
            }]
        )
        '''),

        dcc.Markdown('### Highlighting Certain Columns'),

        dcc.Markdown(dedent('''
        Similarly, certain columns can be highlighted.
        ''')),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[
                {'name': i, 'id': i} for i in df.columns
            ],
            content_style='grow',
            style_table={'width': '100%'},
            style_data_conditional=[{
                'if': {'column_id': 'Temperature'},
                'backgroundColor': '#3D9970',
                'color': 'white',
            }]
        )
        '''
        ),

        # html_table(
        #     df,
        #     cell_style={'border': 'thin lightgrey solid', 'color': 'rgb(60, 60, 60)'},
        #     table_style={'width': '100%'},
        #     column_style={'width': '20%', 'paddingLeft': 20},
        #     header_style={'backgroundColor': 'rgb(235, 235, 235)'},
        #     cell_style_by_column={
        #         "Temperature": {
        #             "backgroundColor": "yellow"
        #         },
        #     }
        # ),

        dcc.Markdown('### Highlighting Certain Cells'),

        dcc.Markdown(dedent('''
        You can also highlight certain cells. For example, you may want to
        highlight certain cells that exceed a threshold or that match
        a filter elsewhere in the app.
        ''')),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[
                {'name': i, 'id': i} for i in df.columns
            ],
            content_style='grow',
            style_table={
                'width': '100%'
            },
            style_data_conditional=[{
                'if': {
                    'column_id': 'Region',
                    'filter': 'Region eq str(Montreal)'
                },
                'backgroundColor': '#3D9970',
                'color': 'white',
            }, {
                'if': {
                    'column_id': 'Humidity',
                    'filter': 'Humidity eq num(20)'
                },
                'backgroundColor': '#3D9970',
                'color': 'white',
            }]
        )
        '''
        ),

        # html_table(
        #     df,
        #     cell_style={'border': 'thin lightgrey solid', 'color': 'rgb(60, 60, 60)'},
        #     table_style={'width': '100%'},
        #     column_style={'width': '20%', 'paddingLeft': 20},
        #     header_style={'backgroundColor': 'rgb(235, 235, 235)'},
        #     conditional_cell_style=lambda cell, column: (
        #         {'backgroundColor': 'yellow'}
        #         if (
        #             (column == 'Region' and cell == 'Montreal')
        #             or
        #             (cell == 20)
        #         ) else {}
        #     )
        # ),

        dcc.Markdown(dedent(
        '''
        ### Multi-Headers
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
            content_style='grow',
            style_table={
                'width': '100%'
            },
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
        ''')
    ]
)
