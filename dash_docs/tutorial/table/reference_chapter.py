import dash_html_components as html
import dash_table
from dash_docs.tutorial.utils.convert_props_to_list import generate_prop_info


layout = html.Div([
    html.H1('dash_table.DataTable Reference'),
    generate_prop_info('DataTable', dash_table)
])
