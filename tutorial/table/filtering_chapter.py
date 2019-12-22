from textwrap import dedent

import dash_html_components as html
import dash_core_components as dcc

from tutorial import tools
from tutorial import styles


examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in ['filtering_fe.py', 'filtering_be.py']
}

layout = html.Div(
    [
        dcc.Markdown(dedent("""
        # DataTable Filtering

        As discussed in the [interactivity chapter](), `DataTable` includes
        filtering capabilities. Users can turn on filtering options by defining
        the `filtering` attribute. `filter_action='native'` will initiate clientside
        (front-end) filtering. Alternatively you can specify `filter_action='native'`.
        If the DataTable is quite large, clientside filtering will likely
        become slow. Using the back-end filtering option: `filter_action='custom'`
        will allow serverside filtering.

        ## Filtering Syntax

        To filter on a column you can enter either an operator and a value
        (for example `> 5000`) or just a value (`5000`) to use the default
        operator for that column's data type.

        Simple strings can be entered plain:
        - `= Asia` in the "continent" column
        - `B` in the "country" column matches all countries that contain a
          capital B

        But if you have spaces or special characters (including `-`,
        particularly in dates)  you need to wrap them in quotes.
        Single quotes `'`, double quotes `"`, or backticks `` ` `` all work.
        - `= "Bosnia and Herzegovina"`
        - `>='2008-12-01'`

        If you have quotes in the string, you can use a different quote, or
        escape the quote character. So `eq 'Say "Yes!"'` and
        `="Say \\"Yes!\\""` are the same.

        Numbers can be entered plain (previously they needed to be wrapped in
        `num()`):
        - `> 5000` in the "gdpPercap" column
        - `< 80` in the `lifeExp` column

        ## Operators

        Many operators have two forms: a symbol (`=`) and a word (`eq`) that
        can be used interchangeably.

        """)),
        html.Table([html.Tr([
            html.Td([
                html.H4(
                    html.P([html.Code('='), ' ', html.Code('eq')]),
                    style={'margin': '0'}),
                dcc.Markdown('Default operator for `number` columns')]),
            html.Td(dcc.Markdown(dedent("""
            Are the two numbers equal? Regardless of type, will first try to
            convert both sides to numbers and compare the numbers. If either
            cannot be converted to a number, looks for an exact match.
            """)))
        ]), html.Tr([
            html.Td([
                html.H4(html.P(html.Code('contains')), style={'margin': '0'}),
                dcc.Markdown('Default operator for `text` and `any` columns')
            ]),
            html.Td(dcc.Markdown(dedent("""
            Does the text value contain the requested substring?
            May match the beginning, end, or anywhere in the middle. The match
            is case-sensitive and exact.
            """)))
        ]), html.Tr([
            html.Td([
                html.H4(
                    html.P(html.Code('datestartswith')),
                    style={'margin': '0'}),
                dcc.Markdown('Default operator for `datetime` columns')]),
            html.Td(dcc.Markdown(dedent("""
            Does the datetime start with the given parts? Enter a partial
            datetime, this will match any date that has at least as much
            precision and starts with the same pieces. For example,
            `datestartswith '2018-03-01'` will match `'2018-03-01 12:59'` but
            not `'2018-03'` even though we interpret `'2018-03-01'` and
            `'2018-03'` both to mean the first instant of March, 2018.
            """)))
        ]), html.Tr([
            html.Td(html.H4(html.P([
                html.Code('>'), ' ', html.Code('gt'), u' \u00a0 ',
                html.Code('<'), ' ', html.Code('lt'), html.Br(),
                html.Code('>='), ' ', html.Code('ge'), u' \u00a0 ',
                html.Code('<='), ' ', html.Code('le'), html.Br(),
                html.Code('!='), ' ', html.Code('ne')
            ]), style={'margin': '0'})),
            html.Td(dcc.Markdown(dedent("""
            Comparison: greater than, less than, greater or equal, less or
            equal, and not equal. Two strings compare by their dictionary
            order, with numbers and most symbols coming before letters, and
            uppercase coming before lowercase.
            """)))
        ])]),
        html.Br(),

        dcc.Markdown(dedent("""

        ## Frontend Filtering Example:

        """)),
        dcc.Markdown(
            examples['filtering_fe.py'][0],
            style=styles.code_container
        ),

        html.Div(
            examples['filtering_fe.py'][1],
            className='example-container'
        ),

        dcc.Markdown(dedent("""
        ## Back-end Filtering

        For large dataframes, you can perform the filtering in Python instead
        of the default clientside filtering. You can find more information on
        performing operations in python in the
        [Python Callbacks chapter](/datatable/callbacks).

        The syntax is (now) the same as front-end filtering, but it's up to the
        developer to implement the logic to apply these filters on the Python
        side.
        In the future we may accept any filter strings, to allow you to
        write your own expression query language.

        > Note: we're planning on adding a structured query object
        > to make it easier and more robust to manage back-end filter logic.
        > Follow
        > [dash-table#169](https://github.com/plotly/dash-table/issues/169)
        > for updates.

        Example:
        """)),

        dcc.Markdown(
            examples['filtering_be.py'][0],
            style=styles.code_container
        ),

        html.Div(
            examples['filtering_be.py'][1],
            className='example-container'
        ),
    ]
)
