
import dash_html_components as html
import dash_core_components as dcc

from dash_docs import tools
from dash_docs import styles
from dash_docs import reusable_components

examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in ['filtering_fe.py', 'filtering_be.py', 'filtering_advanced.py', 'filtering_advanced_derived.py']
}

layout = html.Div(
    [
        reusable_components.Markdown("""
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

        """),
        html.Table([html.Tr([
            html.Td([
                html.H4(
                    html.P([html.Code('='), ' ', html.Code('eq')]),
                    style={'margin': '0px'}),
                reusable_components.Markdown('Default operator for `number` columns')]),
            html.Td(reusable_components.Markdown("""
            Are the two numbers equal? Regardless of type, will first try to
            convert both sides to numbers and compare the numbers. If either
            cannot be converted to a number, looks for an exact match.
            """))
        ]), html.Tr([
            html.Td([
                html.H4(html.P(html.Code('contains')), style={'margin': '0px'}),
                reusable_components.Markdown('Default operator for `text` and `any` columns')
            ]),
            html.Td(reusable_components.Markdown("""
            Does the text value contain the requested substring?
            May match the beginning, end, or anywhere in the middle. The match
            is case-sensitive and exact.
            """))
        ]), html.Tr([
            html.Td([
                html.H4(
                    html.P(html.Code('datestartswith')),
                    style={'margin': '0px'}),
                reusable_components.Markdown('Default operator for `datetime` columns')]),
            html.Td(reusable_components.Markdown("""
            Does the datetime start with the given parts? Enter a partial
            datetime, this will match any date that has at least as much
            precision and starts with the same pieces. For example,
            `datestartswith '2018-03-01'` will match `'2018-03-01 12:59'` but
            not `'2018-03'` even though we interpret `'2018-03-01'` and
            `'2018-03'` both to mean the first instant of March, 2018.
            """))
        ]), html.Tr([
            html.Td(html.H4(html.P([
                html.Code('>'), ' ', html.Code('gt'), u' \u00a0 ',
                html.Code('<'), ' ', html.Code('lt'), html.Br(),
                html.Code('>='), ' ', html.Code('ge'), u' \u00a0 ',
                html.Code('<='), ' ', html.Code('le'), html.Br(),
                html.Code('!='), ' ', html.Code('ne')
            ]), style={'margin': '0px'})),
            html.Td(reusable_components.Markdown("""
            Comparison: greater than, less than, greater or equal, less or
            equal, and not equal. Two strings compare by their dictionary
            order, with numbers and most symbols coming before letters, and
            uppercase coming before lowercase.
            """))
        ])]),
        html.Br(),

        reusable_components.Markdown("""

        ## Frontend Filtering Example:

        """),
        reusable_components.Markdown(
            examples['filtering_fe.py'][0],
            style=styles.code_container
        ),

        html.Div(
            examples['filtering_fe.py'][1],
            className='example-container'
        ),

        reusable_components.Markdown("""
        ## Back-end Filtering

        For large dataframes, you can perform the filtering in Python instead
        of the default clientside filtering. You can find more information on
        performing operations in python in the
        <dccLink href="/datatable/callbacks" children="Python Callbacks chapter"/>.

        The syntax is (now) the same as front-end filtering, but it's up to the
        developer to implement the logic to apply these filters on the Python
        side.
        In the future we may accept any filter strings, to allow you to
        write your own expression query language.

        Example:
        """),

        reusable_components.Markdown(
            examples['filtering_be.py'][0],
            style=styles.code_container
        ),

        html.Div(
            examples['filtering_be.py'][1],
            className='example-container'
        ),

        reusable_components.Markdown("---"),

        reusable_components.Markdown("""
        # Advanced filter usage

        Filter queries can be as simple or as complicated as you want
        them to be. When something is typed into a column filter, it
        is automatically converted to a filter query on that column
        only.
        """),

        reusable_components.Markdown(
            examples['filtering_advanced.py'][0],
            style=styles.code_container
        ),

        html.Div(
            examples['filtering_advanced.py'][1],
            className='example-container'
        ),

        reusable_components.Markdown("""

        The `filter_query` property is written to when the user
        filters the data by using the column filters. For example, if
        a user types `ge 100000000` in the `pop` column filter, and
        `Asia` in the `continent` column filter, `filter_query` will
        look like this:

        >`{pop} ge 100000000 && {continent} contains "Asia"`

        Try typing those values into the column filters in the app
        above, and ensure that the "Read filter_query" option is
        selected.

        The `filter_query` property can also be written to. This might
        be useful when performing more complex filtering,
        like if you want to filter a column based on two (or more)
        conditions. For instance, say that we want countries with a
        population greater than 100 million, but less than 500
        million. Then our `filter_query` would be as follows:

        >`{pop} ge 100000000 and {pop} le 500000000`

        Select the "Write to filter_query" option in the app above,
        and try it out by copying and pasting the filter query above
        into the input box.

        Say that we now want to get a bit more advanced, and
        cross-filter between columns; for instance, we only want the
        results that are located in Asia. Now, our filter query
        becomes:

        >`{pop} ge 100000000 and {pop} le 500000000 and {continent} eq "Asia"`

        We can make the expression even more complex. For example,
        let's say we want all of those countries with the populations
        that fall within our boundaries and that are in Asia, but for
        some reason we also want to include Singapore. This results in
        a filter query that is a little more long-winded:

        >`(({pop} ge 100000000 and {pop} le 500000000) or {country} eq "Singapore") and {continent} eq "Asia"`

        Note that we've grouped expressions together using
        parentheses. This is part of the filtering syntax. Just as is
        true in mathematical expressions, the expressions in the
        innermost parentheses are evaluated first.

        ## Symbol-based versus letter-based operators

        An important thing to notice is that the two types of
        relational operators that can be used in the column filters
        (symbol-based, like `>=`, and letter-based, like `ge`) are not
        converted into one another when `filter_query` is being
        constructed from the values in the column filters. Therefore,
        if using `filter_query` to implement backend filtering, it's
        necessary to take both of these forms of the
        "greater-than-or-equal-to" operator into account when parsing
        the query string (or ensure that the user only uses the ones
        that the backend can parse).

        However, in the case of the logical operator `and/&&`, when
        the table is constructing the query string, the symbol-based
        representation will always be used.

        ## Derived filter query structure

        The `derived_filter_query_structure` prop is a dictionary
        representation of the query syntax tree. You can use the value
        of this property to implement backend filtering.

        For a query that describes a relationship between two values,
        there are three components: the operation, the left-hand side,
        and the right-hand side. For instance, take the following
        query:

        >`{pop} ge 100000000`

        The operation here is `ge` (i.e., `>=`), the left-hand side is
        the field `pop` (corresponding to the column `pop`), and the
        right-hand side is the value `100000000`. As the queries
        become increasingly complex, so do the query structures. Try
        it out by expanding the "Derived filter query structure" in
        the example app above.

        Note that for all operators, there are two keys `subType` and
        `value` that correspond to, respectively, the symbol-based
        representation and the originally inputted representation of
        the operator. So, in the case of the query above, `subType`
        will be `>=` and `value` will be `ge `; if our query string
        were `{pop} >= 100000000` instead, both `subType` and `value`
        will be `>=`.

        ### Backend filtering with `pandas` and `derived_filter_query_structure`

        It's likely that your data are already in a `pandas`
        dataframe. Using the `derived_filter_query_structure` in
        conjunction with `pandas` filters can enable you to do some
        pretty heavy lifting with the table! You can see an example of
        this below.

        """),

        reusable_components.Markdown(
            examples['filtering_advanced_derived.py'][0],
            style=styles.code_container
        ),

        html.Div(
            examples['filtering_advanced_derived.py'][1],
            className='example-container'
        )

    ]
)
