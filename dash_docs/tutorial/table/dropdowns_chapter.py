
import dash_core_components as dcc
import dash_html_components as html

from .utils import section_title
from dash_docs import tools
from dash_docs import styles
from dash_docs import reusable_components

examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in ['dropdown_per_column.py', 'dropdown_per_row.py']
}


layout = html.Div([

    reusable_components.Markdown('''
    # DataTable Dropdowns

    The DataTable includes support for per-column and
    per-cell dropdowns. In future releases, this will
    be tightly integrated with a more formal typing system.

    For now, use the dropdown renderer as a way to limit the
    options available when editing the values with an editable table.

    '''),

    section_title('DataTable with Per-Column Dropdowns'),
    reusable_components.Markdown(
        examples['dropdown_per_column.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['dropdown_per_column.py'][1],
        className='example-container'
    ),

    section_title('DataTable with Per-Row Dropdowns'),
    reusable_components.Markdown(
        examples['dropdown_per_row.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['dropdown_per_row.py'][1],
        className='example-container'
    ),

])
