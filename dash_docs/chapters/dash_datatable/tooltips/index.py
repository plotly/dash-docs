from collections import OrderedDict
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import dash_table
from dash_docs import reusable_components as rc
from dash_docs import datasets
from dash_docs.run import app

Display = rc.CreateDisplay({
    'dash_table': dash_table,
    'html': html,
    'df': datasets.df_regions,
    'df_regions': datasets.df_regions,
    'df_election': datasets.df_election,
    'df_long': datasets.df_long,
    'df_long_columns': datasets.df_long_columns,
    'df_15_columns': datasets.df_15_columns,
    'df_moby_dick': datasets.df_moby_dick,
    'df_numeric': datasets.df_numeric,
    'pd': pd,
    'app': app
})


layout = html.Div(
    children=[

        html.H1('DataTable Tooltips'),
        rc.Markdown(
        '''
        DataTable Tooltips allow you to provide additional information about table
        cells or headers when hovering your mouse over cells.

        These properties can be used to specify `DataTable` tooltips:
        - `tooltip`: Column based tooltip configuration applied to all rows
        - `tooltip_conditional`: Conditional tooltips overriding `tooltip`
        - `tooltip_data`: Statically defined tooltip for each row/column combination
        - `tooltip_header`: Statically defined tooltip for each header column and optionally each header row
        - `tooltip_delay`: Table-wide default delay before the tooltip is displayed
        - `tooltip_duration`: Table-wide default duration before the tooltip disappears. Set to `None` to prevent the tooltip from disappearing.

        See <dccLink children="DataTable Reference" href="/datatable/reference"/> for detailed descriptions.

        ## Tooltips on Individual Cells

        Use tooltips on individual cells if your data is abbreviated, cut-off,
        or if you'd like to display more context about your data.

        This example displays the same data in the cell within the header:
        '''
        ),

        Display(
        '''
        df = df_election # no-display
        result = dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            tooltip_data=[
                {
                    column: {'value': str(value), 'type': 'markdown'}
                    for column, value in row.items()
                } for row in df.to_dict('rows')
            ],

            # Overflow into ellipsis
            style_cell={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0,
            },
            tooltip_delay=0,
            tooltip_duration=None
        )
        '''),

        rc.Markdown(
        '''
        The shape of the `toolip_data` is a list of dictionaries, where
        each dictionary's key matches the `column.id`  and each dictionary's
        value is a dict with `value` & `type`. Alternatively, it can be a single
        value and `type` will be a string instead of `markdown`.
        '''
        ),

        Display(
        '''
        result = dash_table.DataTable(
            data=[
                {'shop': 'Bakersfield', 'sales': 4, 'goal': 10},
                {'shop': 'Berkeley', 'sales': 10, 'goal': 1},
                {'shop': 'Big Bear Lake', 'sales': 5, 'goal': 4}
            ],
            columns=[
                {'id': 'shop', 'name': 'Store Location'},
                {'id': 'sales', 'name': 'Sales Revenue'},
                {'id': 'goal', 'name': 'Revenue Goal'},
            ],
            tooltip_data=[
                {
                    'shop': 'Location at Bakersfield',
                    'sales': '$4M in Revenue',
                    'goal': {'value': '6M **under** Goal', 'type': 'markdown'}
                },
                {
                    'shop': 'Location at Berkeley',
                    'sales': '$10M in Revenue',
                    'goal': {'value': '9M **over** Goal', 'type': 'markdown'}
                },
                {
                    'shop': 'Location at Big Bear Lake',
                    'sales': '$5M in Revenue',
                    'goal': {'value': '1M **over** Goal', 'type': 'markdown'}
                },
            ],
            tooltip_delay=0,
            tooltip_duration=None
        )
        '''),

        rc.Markdown(
        '''
        This example displays different content in each column than what
        is displayed in the cell.
        '''
        ),
        Display(
        '''
        df = pd.DataFrame({
            'shop': ['Bakersfield', 'Berkely', 'Big Bear Lake'],
            'sales': [3, 1, 5],
            'goal': [10, 1, 4],
            'address': [
                '3000 Mall View Road, Suite 1107\\n\\nBakersfield, CA\\n\\n93306',
                '2130 Center Street, Suite 102\\n\\nBerkeley, CA\\n\\n94704',
                '652 Pine Knot Avenue\\n\\nBig Bear Lake, CA\\n\\n92315'
            ]
        })
        result = dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in ['shop', 'sales', 'goal']],
            tooltip_data=[{
                'shop': {'value': row['address'], 'type': 'markdown'},
                'sales': {
                    'value': 'Sales were **{} {}** than the goal'.format(
                        str(abs(row['goal'] - row['sales'])),
                        'less' if row['goal'] > row['sales'] else 'more'
                    ),
                    'type': 'markdown'
                },
                'goal': 'Goal was {}'.format(
                    'not achieved' if row['goal'] > row['sales'] else 'achieved'
                ),
            } for row in df.to_dict('rows')],

            tooltip_delay=0,
            tooltip_duration=None
        )
        '''),


        rc.Markdown(
        '''
        ## Tooltips in Column Headers

        If your column headers are abbreviated or cut-off
        (<dccLink children="See DataTable Width" href="/datatable/width"/>),
        then place a tooltip in the header with `tooltip_header`.

        We recommend providing some light styling to the header to indicate that
        it is "hoverable". We use the dotted underline with `text-decoration`.
        This [isn't supported in IE11](https://caniuse.com/?search=text-decoration-style).

        In this example, the headers are cut-off because they are too long.
        Our tooltip is the original name of the column.
        '''
        ),

        Display(
        '''
        df = df_election # no-display
        result = dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            tooltip_header={i: i for i in df.columns},

            # Style headers with a dotted underline to indicate a tooltip
            style_header={
                'textDecoration': 'underline',
                'textDecorationStyle': 'dotted',
            },

            # Overflow into ellipsis
            style_cell={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0,
            },
            tooltip_delay=0,
            tooltip_duration=None
        )
        '''),

        rc.Markdown(
        '''
        Alternatively, you can specify a different name within `tooltip_header`
        or specify a subset of columns:
        '''
        ),

        Display(
        '''
        df = df_election # no-display
        result = dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            tooltip_header={
                'Rep': 'Republican',
                'Dem': 'Democrat',
                'Ind': 'Independent',
            },

            # Style headers with a dotted underline to indicate a tooltip
            style_header_conditional=[{
                'if': {'column_id': col},
                'textDecoration': 'underline',
                'textDecorationStyle': 'dotted',
            } for col in ['Rep', 'Dem', 'Ind']],

            # Overflow into ellipsis
            style_cell={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0,
            },
            tooltip_delay=0,
            tooltip_duration=None
        )
        '''),

        rc.Markdown(
        '''
        _Note that ellipses aren't displayed in headers. This is a bug, subscribe to
        [plotly/dash-table#735](https://github.com/plotly/dash-table/issues/735)
        for details._

        If your `DataTable` has multiple rows of headers, then use a list
        as the value of the `tooltip_header` items.

        For merged cells, the values must repeat in each cell.
        '''
        ),

        Display(
        '''
        result = dash_table.DataTable(
            columns=[
                {"name": ["", "Year"], "id": "year"},
                {"name": ["City", "Montreal"], "id": "montreal"},
                {"name": ["City", "Toronto"], "id": "toronto"},
                {"name": ["City", "Ottawa"], "id": "ottawa"},
                {"name": ["City", "Vancouver"], "id": "vancouver"},
                {"name": ["Climate", "Temperature"], "id": "temp"},
                {"name": ["Climate", "Humidity"], "id": "humidity"},
            ],
            data=[{
                "year": i, "montreal": i * 10, "toronto": i * 100,
                "ottawa": i * -1, "vancouver": i * -10, "temp": i * -100,
                "humidity": i * 5,
            } for i in range(10)],
            merge_duplicate_headers=True,

            tooltip_header={
                'year': ['', 'Year the measurement was taken'],
                'montreal': ['Average Measurements Across City', 'Montreal, QC, Canada'],
                'toronto': ['Average Measurements Across City', 'Toronto, ON, Canada'],
                'ottawa': ['Average Measurements Across City', 'Ottawa, ON, Canada'],
                'vancouver': ['Average Measurements Across City', 'Vancouver, BC, Canada'],
                'temp': ['Average for a Year', 'Celcius'],
                'humidity': ['Average for a Year', 'Percentage'],
            },

            style_header={
                'textDecoration': 'underline',
                'textDecorationStyle': 'dotted',
            },
        )
        '''
        ),

        rc.Markdown(
        '''
        ## A Single Tooltip in the Column

        As an alternative or in addition to column header tooltips, place a
        tooltip to appear on the entire column with the `tooltip` property.

        This can also be helpful with large tables where the user
        may lose track of the column headers.

        If the tooltip is specified for both headers and cells, you can use
        the `use_with` property instead of specifying a separate `tooltip_header`
        and `tooltip`.
        '''
        ),


        Display(
        '''
        df = df_election # no-display
        result = dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            tooltip ={i: {
                'value': i,
                'use_with': 'both'  # both refers to header & data cell
            } for i in df.columns},

            # Style headers with a dotted underline to indicate a tooltip
            style_header={
                'textDecoration': 'underline',
                'textDecorationStyle': 'dotted',
            },

            # Overflow into ellipsis
            style_cell={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0,
            },
            tooltip_delay=0,
            tooltip_duration=None
        )
        '''),

        rc.Markdown(
        '''
        ## Conditional Tooltips

        Tooltips can also be customized based on conditions.
        The `tooltip_conditional` has the same syntax as the `style_data_conditional`
        property, see the <dccLink href="/datatable/conditional-formatting" children="conditional formatting"/>
        chapter for many examples.

        If both `tooltip_conditional` and `tooltip` would display a tooltip for
        a cell, the conditional tooltip takes priority. If multiple conditions match the
        data row, the last match has priority.
        '''
        ),

        Display(
        '''
        df = df_regions  # no-display
        result = dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],

            tooltip_conditional=[
                {
                    'if': {
                        'filter_query': '{Region} contains "New"'
                    },
                    'type': 'markdown',
                    'value': 'This row is significant.'
                }
            ],

            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{Region} contains "New"'
                    },
                    'backgroundColor': '#0074D9',
                    'color': 'white',
                    'textDecoration': 'underline',
                    'textDecorationStyle': 'dotted',
                }
            ],
            tooltip_delay=0,
            tooltip_duration=None
        )
        '''
        ),

        rc.Markdown(
        '''
        ## Images in Tooltips

        Markdown supports images with this syntax: `![alt](src)`
        where `alt` refers to the image's [alt text](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Img)
        and `src` is the path to the image (the `src` property).

        The `src` can refer to images within your project's "assets" folder
        or absolute URLs. If referring to an image in the `assets` folder,
        we recommend using `app.get_relative_path` so that the image URL
        is correct when working locally and when deploying to Dash Enterprise.
        '''
        ),

        Display(
        '''
        result = dash_table.DataTable(
            data=[
                {'shop': 'Bakersfield', 'sales': 4, 'goal': 10},
                {'shop': 'Berkeley', 'sales': 10, 'goal': 1},
                {'shop': 'Big Bear Lake', 'sales': 5, 'goal': 4}
            ],
            columns=[
                {'id': 'shop', 'name': 'Store Location'},
                {'id': 'sales', 'name': 'Sales Revenue'},
                {'id': 'goal', 'name': 'Revenue Goal'},
            ],
            tooltip_data=[
                {
                    'shop': {
                        'value': 'Location at Bakersfield\\n\\n![Bakersfield]({})'.format(
                            app.get_relative_path('/assets/images/table/bakersfield.jpg')
                        ),
                        'type': 'markdown'
                    }
                },
                {
                    'shop': {
                        'value': 'Location at Berkeley\\n\\n![Berkeley]({})'.format(
                            app.get_relative_path('/assets/images/table/berkeley.jpg')
                        ),
                        'type': 'markdown'
                    }
                },
                {
                    'shop': {
                        'value': 'Location at Big Bear Lake\\n\\n![Big Bear Lake](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Big_Bear_Valley%2C_California.jpg/1200px-Big_Bear_Valley%2C_California.jpg)',
                        'type': 'markdown'
                    }
                },
            ],

            # Style headers with a dotted underline to indicate a tooltip
            style_data_conditional=[{
                'if': {'column_id': 'shop'},
                'textDecoration': 'underline',
                'textDecorationStyle': 'dotted',
            }],

            tooltip_delay=0,
            tooltip_duration=None
        )
        '''),

        rc.Markdown(
        '''
        ## Tables in Tooltips

        Markdown supports tables with a syntax that looks like this:
        ```
        | City       | Value     | Return     |
        | :------------- | :----------: | -----------: |
        |  Montreal   | 41,531    | 431.245 |
        | Seattle   | 53,153 | 12.431 |
        ```
        '''
        ),
        rc.Markdown(
        '''
        | City       | Value     | Return     |
        | :------------- | :----------: | -----------: |
        |  Montreal   | 41,531    | 431.245 |
        | Seattle   | 53,153 | 12.431 |
        '''
        ),

        rc.Markdown(
        '''
        This can be specified within a table's value:
        '''
        ),
        Display(
        '''
        markdown_table = """
        | City       | Value     | Return     |
        | :------------- | :----------: | -----------: |
        |  Montreal   | 41,531    | 431.245 |
        | Seattle   | 53,153 | 12.431 |
        """

        result = dash_table.DataTable(
            data=[
                {'shop': 'Bakersfield', 'sales': 4, 'goal': 10},
                {'shop': 'Berkeley', 'sales': 10, 'goal': 1},
                {'shop': 'Big Bear Lake', 'sales': 5, 'goal': 4}
            ],
            columns=[
                {'id': 'shop', 'name': 'Store Location'},
                {'id': 'sales', 'name': 'Sales Revenue'},
                {'id': 'goal', 'name': 'Revenue Goal'},
            ],
            tooltip={
                c: {'value': markdown_table, 'type': 'markdown'}
                for c in df.columns
            },
            tooltip_delay=0,
            tooltip_duration=None
        )
        '''),

        rc.Markdown(
        '''
        ## Styling Tooltips

        Tooltips can be styled with the `dash-tooltips` CSS class. This can
        be specified within a CSS file inside your `assets/` folder
        or within the table itself with the `css` property.
        '''
        ),

        Display(
        '''
        df = df_regions # no-display
        result = dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            tooltip_data=[
                {
                    column: {'value': str(value), 'type': 'markdown'}
                    for column, value in row.items()
                } for row in df.to_dict('rows')
            ],
            css=[{
                'selector': '.dash-tooltip',
                'rule': 'background-color: white; font-family: monospace;'
            }],

            tooltip_delay=0,
            tooltip_duration=None
        )
        '''),

        rc.Markdown(
        '''
        ## Customizing Delay & Duration

        Set `tooltip_delay` to `0` for the tooltips to appear immediately.

        Set `tooltip_duration` to `None` in order for the tooltips to remain
        visible while you are hovering over them. Otherwise, they will disappear
        after `tooltip_duration` milliseconds.
        '''
        ),

    ]
)
