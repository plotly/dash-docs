import dash_html_components as html
import dash_table
from tutorial.utils.convert_props_to_table import generate_prop_table


layout = html.Div([
    html.H1('Dash Interactive Table Reference'),
    generate_prop_table('DataTable', dash_table)
])
