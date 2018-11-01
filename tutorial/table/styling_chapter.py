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
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
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

        html.H3('Default Styles'),
        dcc.Markdown(dedent(
        '''
        By default, the table will expand to the width of its container.
        The width of the columns is determined automatically in order to
        accommodate the content in the cells.
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

        dcc.Markdown(dedent(
        '''
        > The set of examples on this page are rendered with a few different
        > dataframes that have different sizes and shapes. In particular,
        > some of the dataframes have a large number of columns or have cells
        > with long contents. If you'd like to follow along on your own
        > machine, then open up the menu below to copy and paste
        > the code behind these datasets.
        '''
        )),

        html.Details(open=False, children=[
            html.Summary('View the Datasets'),
            dcc.SyntaxHighlighter(dedent(
            '''
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

            election_data = OrderedDict(
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

            df_election = pd.DataFrame(election_data)
            df_long = pd.DataFrame(
                OrderedDict([(name, col_data * 10) for (name, col_data) in election_data.items()])
            )
            df_long_columns = pd.DataFrame(
                {
                    "This is Column {} Data".format(i): [1, 2]
                    for i in range(10)
                }
            )
            '''))
        ]),

        dcc.Markdown(dedent(
        '''
        The default styles work well for a small number of columns and short
        text. However, if you are rendering a large number of columns or
        cells with long contents, then you'll need to employ one of the
        following "overflow strategies" to keep the table within its container.

        > Heads up! In the future, we may modify our default styles to
        > better accommodate wide content while keeping the table full-width
        > and responsive. Subscribe to [plotly/dash-table#197](https://github.com/plotly/dash-table/issues/197) for more.
        '''
        )),

        dcc.Markdown(dedent(
        '''
        ### Overflow Strategies - Multiple Lines

        If your cells contain contain text with spaces, then you can overflow
        your content into multiple lines.

        > We find that this interface is a little too complex.
        > We're looking at simplifying this in this issue:
        > [https://github.com/plotly/dash-table/issues/188](https://github.com/plotly/dash-table/issues/188)
        '''
        )),
        Display(
        '''
        dash_table.DataTable(
            style_data={'whiteSpace': 'normal'},
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
            data=df_election.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_election.columns]
        )
        '''),

        dcc.Markdown(dedent(
        """
        ### Overflow Strategies - Overflowing Into Ellipses

        Alternatively, you can keep the content on a single line but display
        a set of ellipses if the content is too long to fit into the cell.

        Here, `max-width` is set to 0. It could be any number, the only
        important thing is that it is supplied. The behaviour will be
        the same whether it is 0 or 50.

        If you want to just hide the content instead of displaying ellipses,
        then set `textOverflow` to `'clip'` instead of `'ellipsis'`.
        """
        )),
        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
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

        dcc.Markdown(dedent(
        '''
        ### Overflow Strategies - Horizontal Scroll

        Instead of trying to fit all of the content in the container, you could
        overflow the entire container into a scrollable container.
        '''
        )),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'overflowX': 'scroll'},
        )
        '''),

        dcc.Markdown(dedent(
        '''
        Note how we haven't explicitly set the width of the individual columns
        yet. The widths of the columns have been computed dynamically depending
        on the width of the table and the width of the cells contents.
        In the example above, by providing a scrollbar, we're effectively
        giving the table as much width as needs in order to fit the entire
        width of the cell contents on a single line.

        We can combine some of these strategies by bounding the `maxWidth` of
        a column and overflowing into multiple lines (or ellipses) if the
        content exceeds that width while rendering the table within a
        scrollable horizontal container. If the column's contents don't
        exceed the `maxWidth`, then the column will only take up the
        necessary amount of horizontal space.
        '''
        )),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'overflowX': 'scroll'},
            style_cell={
                'minWidth': '0px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        )
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'overflowX': 'scroll'},
            style_cell={
                'minWidth': '0px', 'maxWidth': '180px',
                'whiteSpace': 'no-wrap',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        )
        '''),

        dcc.Markdown(dedent(
        '''
        Alternatively, you can fix the width of each column by adding `width`.
        In this case, the column's width will be constant, even if its contents
        are shorter or wider.
        '''
        )),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        )
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'no-wrap',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
        )
        '''),

        # dcc.Markdown("### Individual Column Widths"),
        # dcc.Markdown(dedent('''
        # The column widths can be defined by
        # percents rather than pixels and the columns
        # can be styled independently with `style_cell_conditional`
        # ''')),
        # Display(
        # '''
        # dash_table.DataTable(
        #     data=df_election.to_dict('rows'),
        #     columns=[{'id': c, 'name': c} for c in df_election.columns],
        #     style_cell_conditional=[
        #         {'if': {'column_id': 'Date'},
        #          'width': '30%'},
        #         {'if': {'column_id': 'Election Polling Organization'},
        #          'width': '25%'},
        #         {'if': {'column_id': 'Dem'},
        #          'width': '5%'},
        #         {'if': {'column_id': 'Rep'},
        #          'width': '5%'},
        #         {'if': {'column_id': 'Ind'},
        #          'width': '5%'},
        #         {'if': {'column_id': 'Region'},
        #          'width': '30%'},
        #     ],
        #     style_cell={
        #         # all three widths are needed
        #         'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        #         'whiteSpace': 'no-wrap',
        #         'overflow': 'hidden',
        #         'textOverflow': 'ellipsis',
        #     },
        #     css=[{
        #         'selector': '.dash-cell div.dash-cell-value',
        #         'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
        #     }],
        #
        # )
        # '''),

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
            style_cell_conditional=[
                {'if': {'column_id': 'Region'},
                 'width': '50%'},
            ]
        )
        '''),

        # dcc.Markdown("### Underspecified Widths"),
        # dcc.Markdown(dedent(
        # '''
        # The widths can be under-specified. Here, we're only setting the width for
        # the three columns in the middle, the rest of the columns are
        # automatically sized to fit the rest of the container.
        # The columns have a width of 50px, or the width of this line:
        # '''
        # )),
        # html.Div(
        #     style={"width": 50, "height": 10, "backgroundColor": "hotpink"}
        # ),
        # # html_table(
        # #     df,
        # #     table_style={"width": "100%"},
        # #     column_style={
        # #         "Dem": {"width": 50},
        # #         "Rep": {"width": 50},
        # #         "Ind": {"width": 50},
        # #     },
        # # ),
        # Display(
        # '''
        # dash_table.DataTable(
        #     data=df_election.to_dict('rows'),
        #     columns=[{'id': c, 'name': c} for c in df_election.columns],
        #     style_cell_conditional=[
        #         {'if': {'column_id': 'Dem'},
        #          'width': 50},
        #         {'if': {'column_id': 'Rep'},
        #          'width': 50},
        #         {'if': {'column_id': 'Ind'},
        #          'width': 50},
        #     ]
        # )
        # '''),

        # dcc.Markdown("### Widths that are smaller than the content"),
        # dcc.Markdown(dedent(
        # '''
        # In this case, we're setting the width to 20px, which is smaller
        # than the "10924" number in the "Ind" column.
        # The table does not allow it.
        # '''
        # )),
        # html.Div(
        #     style={"width": 20, "height": 10, "backgroundColor": "hotpink"}
        # ),
        # # html_table(
        # #     df,
        # #     table_style={"width": "100%"},
        # #     column_style={
        # #         "Dem": {"width": 20},
        # #         "Rep": {"width": 20},
        # #         "Ind": {"width": 20},
        # #     },
        # # ),
        # Display(
        # '''
        # dash_table.DataTable(
        #     data=df_election.to_dict('rows'),
        #     columns=[{'id': c, 'name': c} for c in df_election.columns],
        #     style_cell_conditional=[
        #         {'if': {'column_id': 'Dem'},
        #          'width': 20},
        #         {'if': {'column_id': 'Rep'},
        #          'width': 20},
        #         {'if': {'column_id': 'Ind'},
        #          'width': 20},
        #     ]
        # )
        # '''),

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
            data=df_long.to_dict('rows'),
            columns=[{'id': c, 'name': c} for c in df_long.columns],
            n_fixed_rows=1,
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
        )
        '''
        ),

        dcc.Markdown(dedent(
        """
        ### Column Alignment

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

        # dcc.Markdown(dedent('''
        # ## Row Padding
        #
        # By default, the gridded view is pretty tight.
        # You can add some top and bottom row padding to
        # the rows to give your data a little bit more room to breathe.
        # ''')),
        # Display(
        # '''
        # dash_table.DataTable(
        #     data=df.to_dict('rows'),
        #     columns=[{'id': c, 'name': c} for c in df.columns],
        #     style_cell={'padding': '5px'},
        # )
        # '''
        # ),

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
        a bold text.
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
                'fontWeight': 'bold'
            },
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
