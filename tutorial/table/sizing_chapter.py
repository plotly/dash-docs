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

        html.H1('DataTable Sizing'),

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
            data=df.to_dict('records'),
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
            dcc.Markdown(dedent(
            '''
            ```python
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
            ```
            '''))
        ]),

        html.Hr(),

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
            data=df_election.to_dict('records'),
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
            data=df_election.to_dict('records'),
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
            data=df_election.to_dict('records'),
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
            data=df_election.to_dict('records'),
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
            data=df_election.to_dict('records'),
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
            data=df_election.to_dict('records'),
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
            data=df_election.to_dict('records'),
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

        dcc.Markdown(dedent(
        '''
        ### Horizontal Scrolling via Fixed Columns

        You can also add a horizontal scrollbar to your table by fixing
        the leftmost columns with `fixed_columns`.

        > Note that fixing columns introduces some changes to the underlying
        > markup of the table and may impact the way that your columns
        > are rendered or sized.
        > For more information, subscribe to [dash-table#201](https://github.com/plotly/dash-table/issues/201).
        '''
        )),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            fixed_columns={ 'headers': True, 'data': 1 },
        )
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            fixed_columns={ 'headers': True, 'data': 1 },
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


        dcc.Markdown("### Individual Column Widths"),

        dcc.Markdown(dedent(
        '''
        The widths of individual columns can be supplied through the
        `style_cell_conditional` property. These widths can be specified as
        percentages or fixed pixels. You can supply the widths for _all_ of the
        columns or just a few of them.
        '''
        )),

        # html_table(
        #     df,
        #     table_style={"width": "100%"},
        #     column_style={"Region": {"width": "50%"}},
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell_conditional=[
                {'if': {'column_id': 'Date'},
                 'width': '30%'},
                {'if': {'column_id': 'Region'},
                 'width': '30%'},
            ]
        )
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell_conditional=[
                {'if': {'column_id': 'Temperature'},
                 'width': '130px'},
                {'if': {'column_id': 'Humidity'},
                 'width': '130px'},
                {'if': {'column_id': 'Pressure'},
                 'width': '130px'},
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
        #     data=df_election.to_dict('records'),
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
        #     data=df_election.to_dict('records'),
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
        ## Table Height and Vertical Scrolling

        By default, the table's height will expand in order
        to render all of the rows.

        You can constrain the height of the table by setting a `maxHeight`
        and adding a scrollbar with `overflowY: 'scroll'`.
        With `maxHeight`, the table's contents will only become scrollable
        if the contents are taller than that height.
        ''')),
        Display(
        '''
        dash_table.DataTable(
            data=df_long.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={
                'maxHeight': '300',
                'overflowY': 'scroll'
            },
        )
        '''),

        dcc.Markdown(dedent(
        '''
        ### Vertical Scrolling via Fixed Rows

        In the example above, the headers become hidden when you scroll down.

        You can keep these headers visible by supplying `fixed_rows={ 'headers': True, 'data': 0 }`.
    
        > Note that fixing rows introduces some changes to the underlying
        > markup of the table and may impact the way that your
        > columns are rendered or sized.
        > In particular, you'll need to set an explicit pixel-based widths
        > for each of the columns.
        > For more information, subscribe to [dash-table#201](https://github.com/plotly/dash-table/issues/201).
        ''')),
        Display(
        '''
        dash_table.DataTable(
            data=df_long.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_long.columns],
            fixed_rows={ 'headers': True, 'data': 0 },
            style_cell={'width': '150px'}
        )
        '''),

        dcc.Markdown("### Height vs Max Height"),
        dcc.Markdown(dedent(
        '''
        With `max-height`, if the table's contents are shorter than the
        `max-height`, then the container will be shorter.
        If you want a container with a constant height no matter the
        contents, then use `height`.

        Here, we're setting max-height to 300, or the height of the pink line.
        Note how the table renders shorter than this line.
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
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={
                'maxHeight': '300px',
                'overflowY': 'scroll',
                'border': 'thin lightgrey solid'
            },
        )
        '''),

        dcc.Markdown('''
        and here is `height` with the same content. Note how the table's
        container takes up all 300px.

        '''),
        # html.Div(
        #     style={"height": 300, "overflowY": "scroll"},
        #     children=html_table(df, table_style={"width": "100%"}),
        # ),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={
                'height': '300px',
                'overflowY': 'scroll',
                'border': 'thin lightgrey solid'
            },
        )
        '''),

    ]
)
