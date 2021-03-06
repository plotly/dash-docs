import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import dash_bio_utils.ngl_parser as ngl_parser

'''
### Multiple Molecules

Multiple molecules can be visualized by adding entries to the data list. In the example below, we 
use multiple dropdown selections to add molecules to the stage. Each molecule can have its own set 
of atoms and residues highlighted. Individual molecules can be interacted with by holding down the 
`CTRL` key. If adding or removing molecules from the stage, make sure the `resetView` prop is set to 
false.
'''

app = dash.Dash(__name__)

data_path =  "https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/"

# PDB examples
dropdown_options = [
    {"label": "1BNA", "value": "1BNA"},
    {"label": "MPRO", "value": "MPRO"},
    {"label": "PLPR", "value": "PLPR"},
    {"label": "5L73", "value": "5L73"},
    {"label": "NSP2", "value": "NSP2"}
]

app.layout = html.Div([
    dcc.Dropdown(id="multi-dropdown", options=dropdown_options, value=["1BNA", "MPRO"],
                 multi=True),
    dashbio.NglMoleculeViewer(id="multiple-ngl"),
])


@app.callback(
    [Output("multiple-ngl", 'data'),
     Output("multiple-ngl", "molStyles")],
    [Input("multi-dropdown", "value")]
)
def return_molecule(value):
    if (value is None):
        raise PreventUpdate

    molstyles_dict = {
        "representations": ["cartoon", "axes+box"],
        "chosenAtomsColor": "white",
        "chosenAtomsRadius": 1,
        "molSpacingXaxis": 100,
    }
    data_list = [ngl_parser.get_data(data_path=data_path, pdb_id=molecule, color='red',
                            reset_view=True, local=False)
                 for molecule in value]

    return data_list, molstyles_dict

if __name__ == '__main__':
    app.run_server(debug=True)
