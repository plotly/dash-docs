from textwrap import dedent

import dash_core_components as dcc
import dash_html_components as html

from .utils import section_title
from tutorial import tools
from tutorial import styles


examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in ['dropdown_per_column.py', 'dropdown_per_row.py']
}


layout = html.Div([

    dcc.Markdown(dedent('''
    # DataTable Dropdowns

    The DataTable includes support for per-column and
    per-cell dropdowns. In future releases, this will
    be tightly integrated with a more formal typing system.

    For now, use the dropdown renderer as a way to limit the
    options available when editing the values with an editable table.

    ''')),

    section_title('DataTable with Per-Column Dropdowns'),
    dcc.SyntaxHighlighter(
        examples['dropdown_per_column.py'][0],
        language='python',
        customStyle=styles.code_container
    ),
    html.Div(
        examples['dropdown_per_column.py'][1],
        className='example-container'
    ),

    section_title('DataTable with Per-Row Dropdowns'),
    dcc.SyntaxHighlighter(
        examples['dropdown_per_row.py'][0],
        language='python',
        customStyle=styles.code_container
    ),
    html.Div(
        examples['dropdown_per_row.py'][1],
        className='example-container'
    ),

])
