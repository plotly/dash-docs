from collections import OrderedDict
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import dash_table
from dash_docs import reusable_components as rc
from dash_docs import datasets

from dash_docs.tools import load_examples
examples = load_examples(__file__)

layout = html.Div(
    children=[

        html.H1('DataTable Tooltips'),
        rc.Markdown(
        '''
        The table tooltips are supported through many different that allow for tooltips that
        are defined by column, conditionally, and statically.

        The following props are used to configure the table's tooltip behavior and will be
        covered in the examples below:
        - `tooltip`: Column based tooltip configuration applied to all rows
        - `tooltip_conditional`: Conditional tooltips overriding `tooltip`
        - `tooltip_data`: Statically defined tooltip for each row/column combination
        - `tooltip_header`: Statically defined tooltip for each header column and optionally each header row
        - `tooltip_delay`: Table-wide default delay before the tooltip is displayed (this can be customized further)
        - `tooltip_duration`: Table-wide default duration before the tooltip disappears (this can be customized further)

        See <dccLink children="DataTable Reference" href="/datatable/reference"/> for detailed prop descriptions.
        '''
        ),
        html.H2('Tooltips, Delay, and Duration'),
        rc.Markdown(
        '''
        The simplest way of defining tooltips for a table is with the `tooltip` prop. `tooltip` defines
        up to one tooltip per column.

        The display and delay time can be customize for the entire table and overriden per tooltip.
        '''
        ),

        rc.Syntax(examples['tooltip.py'][0]),
        html.Div(examples['tooltip.py'][1], className = 'example-container'),

        html.H2('Conditional Tooltips'),
        rc.Markdown(
        '''
        Tooltips can also be customized based on conditions. If both `tooltip_conditional` and `tooltip` would
        display a tooltip for a cell, the conditional tooltip takes priority. If multiple conditions match the
        data row, the last match has priority.
        '''
        ),

        rc.Syntax(examples['tooltip_conditional.py'][0]),
        html.Div(examples['tooltip_conditional.py'][1], className = 'example-container'),

        html.H2('Data Tooltips'),
        rc.Markdown(
        '''
        Sometimes displaying the same tooltip or defining conditional tooltips is not enough and it is necessary
        to define a different tooltip for each cell. `tooltip_data` has priority over `tooltip` but not
        `tooltip_conditional`.
        '''
        ),

        rc.Syntax(examples['tooltip_data.py'][0]),
        html.Div(examples['tooltip_data.py'][1], className = 'example-container'),

        html.H2('Header Tooltips'),
        rc.Markdown(
        '''
        Similarly to `tooltip_data`, tooltips can be defined on headers with `tooltip_header`. `tooltip_header` has
        priority over `tooltip`.
        '''
        ),

        rc.Syntax(examples['tooltip_header.py'][0]),
        html.Div(examples['tooltip_header.py'][1], className = 'example-container'),

    ]
)
