from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

import dash_table
from .utils import section_title
from tutorial import styles, tools


examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in [
        'typing_formatting.py',
        'typing_formatting.1.py'
    ]
}

layout = html.Div([
    dcc.Markdown('# DataTable - Typing'),

    dcc.Markdown(dedent(
    '''
    This section will provide an overview of the DataTable's capabilities for typing, formatting,
    presentation and user input processing.
    ''')),

    dcc.Markdown(dedent(
    '''
    ### Typing
    The DataTable provides support for per-column typing and allows for data validation and
    coercion behaviors to be configured on a per-column basis, so as to fit the needs of various
    usage scenarios.

    The following types are currently supported:
    - `numeric`: includes both integers and floats
    - `text`: string, sequence of characters
    - `datetime`: string in the form 'YYYY-MM-DD HH:MM:SS.ssssss' or some truncation thereof
    - `any`: any type of data

    Additional types and specialized sub-types will be added in the future.

    By default, the column type is `any`.
    ''')),

    dcc.Markdown(dedent(
    '''
    ### Presentation
    The DataTable provides multiple presentation schemes that can vary depending on the column's
    type.

    The following types are supported by all types:
    - `input`: a text input field
    - `dropdown`: see [DataTable Dropdowns](/datatable/dropdowns) for more details

    Additional presentations will be added in the future.

    By default, the column presentation is `input`.
    ''')),

    dcc.Markdown(dedent(
    '''
    ### User Input Processing
    The DataTable provides a configurable input processing system that can accept, reject or
    apply a default value when an input is provided. It can be configured to validate or coerce
    the input to make it fit with the expected data type. Specific validation cases can be
    configured on a per-column basis.

    See the table's [reference](/datatable/reference) `on_change.action`, `on_change.failure`
    and `validation` column nested properties for details.
    ''')),

    dcc.Markdown(dedent(
    '''
    ### Formatting
    The DataTable provides a configurable data formatting system that modifies how the data
    is presented to the user.

    The formatting can be configured by:
    - explicitly writing the column `format` nested property
    - using preconfigured Format Templates
    - using the general purpose Format object

    At the moment, only `type='numeric'` formatting can be configured.
    ''')),

    dcc.Markdown(dedent(
    '''
    ### Examples
    ''')),


    section_title('DataTable with template formatting'),
    dcc.Markdown(dedent(
    '''
    This table contains two columns formatted by templates. The `Variation (%)` column is further
    configured by changing the sign behavior so that both the "+" and "-" sign are visible. Additional
    configuration changes can be chained after a ```Format(...)``` and a ```FormatTemplate.<template>(...)``` calls.
    ''')),
    dcc.Markdown(
        examples['typing_formatting.1.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['typing_formatting.1.py'][1],
        className='example-container'
    ),

    section_title('DataTable with formatting'),
    dcc.Markdown(dedent(
    '''
    This table contains columns with type `numeric` and `datetime`. The "max" columns have the default
    behavior and will not allow for invalid data to be passed in. The "min" columns are more permissive.
    The "Min Temperature (F)" column will default invalid entries to `None` and display "N/A". The "Min
    Temperature (Date)" column will not try to validate or coerce the data.

    Both temperature columns are using the Format helper object to create the desired formatting. The
    equivalent manual configuration is shown as comments in the code below. One can always see the resulting
    configuration for a given Format object by using ```Format(...).to_plotly_json()```.
    ''')),
    dcc.Markdown(
        examples['typing_formatting.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['typing_formatting.py'][1],
        className='example-container'
    )
])
