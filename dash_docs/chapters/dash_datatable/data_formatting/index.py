from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import dash_table
from dash_docs import styles, tools
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)

layout = html.Div([
    rc.Markdown('# DataTable - Number Formatting'),

    rc.Markdown(
    '''
    `DataTable` offers extensive number formatting and localization possibilities with the columns nested prop `format` and
    table-wide localization prop `local_format`.

    Most formatting and localization for columns can be done through the `dash_table.FormatTemplate`
    and `dash_table.Format` Python helpers but it's also possible to use the `d3-format`
    `specifier` and `locale` directly.
    '''),

    rc.Markdown(
    '''
    See [d3-format](https://github.com/d3/d3-format) for additional syntax details.
    '''),

    rc.Markdown(
    '''
    ## Using FormatTemplate

    The FormatTemplate provides the following predefined templates:

    - Money
    - Percentage
    '''),

    rc.Markdown(
        examples['data_formatting_formattemplate.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_formattemplate.py'][1],
        className='example-container'
    ),

    rc.Markdown(
    '''
    ## Using Format Helper
    '''),

    rc.Markdown('''
    ### Group

    Grouping is defined with the format nested props `group` and `groups`.
    `group` takes values `True` and `Group.yes` to toggle digit grouping.
    `groups` takes a list of numbers used to define the digits grouping pattern.
    If the number has more digits than what's defined in `groups`, it cycles through the
    list again until it runs out of numbers to group.
    '''),

    rc.Markdown(
        examples['data_formatting_format_group.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_group.py'][1],
        className='example-container'
    ),

    rc.Markdown('''
    ### Align and Fill

    Alignment and filling is defined with the format nested props `align`, `fill`, and `padding_width`.
    The `Align` helper takes values `left`, `right`, and `center`.
    `fill` is single character that will be used for filling.
    `padding_width` is the minimum length of the filled string.
    If the formatted number requires more space than `padding_width` allows for, it will do so.
    '''),

    rc.Markdown(
        examples['data_formatting_format_fill.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_fill.py'][1],
        className='example-container'
    ),

    rc.Markdown('''
    ### Padding and Padding Width

    Padding and padding width is defined with the format nested props `padding` and `padding_width` and they behave similarly
    to `fill` and `padding_width`, but do not allow alignment.
    '''),

    rc.Markdown(
        examples['data_formatting_format_padding.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_padding.py'][1],
        className='example-container'
    ),

    rc.Markdown('''
    ### Precision and Scheme
    '''),

    rc.Markdown(
        examples['data_formatting_format_precision.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_precision.py'][1],
        className='example-container'
    ),

    rc.Markdown('''
    ### Sign

    When to display a sign and what type of sign to display is defined with the format nested prop `sign`.
    The `Sign` helper takes values `negative` (show sign when negative), `positive` (always show sign), `parantheses` (when negative)
    '''),

    rc.Markdown(
        examples['data_formatting_format_sign.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_sign.py'][1],
        className='example-container'
    ),

    rc.Markdown('''
    ### Symbol

    Displaying of symbols is defined with the format nested prop `symbol` and the prefix/suffix symbols are defined with the locale nested prop `symbol`.
    The `Symbol` helper takes values `yes` and `no`.
    The locale `symbol` nested prop is a list of strings of length 2 of the form `[prefix, suffix]`. Strings in symbol can be of any length.
    '''),

    rc.Markdown(
        examples['data_formatting_format_symbol.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_symbol.py'][1],
        className='example-container'
    ),

    rc.Markdown('## Localization'),

    rc.Markdown(
        examples['data_formatting_format_localization.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_localization.py'][1],
        className='example-container'
    )
])
