import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import dash_bio_utils.ngl_parser as ngl_parser

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


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
    dcc.Markdown('''
    ### NglMoleculeViewer Controls
    
    * Rotate Stage: Left-click on the viewer and move the mouse to rotate the stage.
    * Zoom: Use the mouse scroll-wheel to zoom in and out of the viewer.
    * Pan: Right click on the viewer to pan the stage.
    * Individual Molecule Interaction: Left click on the molecule to interact with, then hold the 
    `CTRL` key and use right and left click mouse buttons to rotate and pan individual molecules.
    '''),
    dcc.Dropdown(id="default-dropdown", options=dropdown_options, placeholder="Select a molecule",
                 value = "1BNA"),
    dashbio.NglMoleculeViewer(id="default-ngl"),
])


@app.callback(
    [Output("default-ngl", 'data'),
     Output("default-ngl", "molStyles")],
    [Input("default-dropdown", "value")]
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

    data_list = [ngl_parser.get_data(data_path=data_path, pdb_id=value, color='red',
                                     reset_view=True, local=False)]

    return data_list, molstyles_dict

if __name__ == '__main__':
    app.run_server(debug=True)
