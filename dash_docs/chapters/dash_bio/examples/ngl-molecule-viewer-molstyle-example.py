import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import dash_bio_utils.ngl_parser as ngl_parser


representation_options = [
    {"label": "backbone", "value": "backbone"},
    {"label": "ball+stick", "value": "ball+stick"},
    {"label": "cartoon", "value": "cartoon"},
    {"label": "hyperball", "value": "hyperball"},
    {"label": "licorice", "value": "licorice"},
    {"label": "axes+box", "value": "axes+box"},
    {"label": "helixorient", "value": "helixorient"}
]

'''
### Molecule Styles

Molecule styles and representations can be styled with the `molStyles` property which accepts a 
`dict` of arguments. Molecule representations can be combined and stacked together by setting a 
`list` of representations. The following representations are available:

* Molecules Styles: `backbone`, `ball+stick`, `cartoon`, `hyperball`, `licorice`, `line`, `ribbon`,
`rope`, `spacefill`, `surface`, `trace`, `tube`

* Additional Representations: `axes`, `axes+box`, `helixorient`, `unitcell`

With the `sideByside` key, we can choose whether multiple molecules should be represented 
side-by-side or intertwined. Note that in `sideByside` mode, the molecules cannot be 
independently rotated or panned. 
'''

app = dash.Dash(__name__)

data_path =  "https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/"


app.layout = html.Div([
    dcc.Dropdown(id="molstyle-dropdown", options=representation_options,
                 multi=True, value=["cartoon", "axes+box"]),
    dcc.RadioItems(
        id="molstyle-radio",
        options=[
            {'label': 'sideByside', 'value': "True"},
            {'label': 'Independent', 'value': "False"},
        ],
        value="False"
    ),
    dashbio.NglMoleculeViewer(id="molstyle-ngl"),
])


@app.callback(
    [Output("molstyle-ngl", 'data'),
     Output("molstyle-ngl", "molStyles")],
    [Input("molstyle-dropdown", "value"),
     Input("molstyle-radio", "value")]
)
def return_molecule(style, sidebyside):

    sidebyside_bool = sidebyside == "True"

    molstyles_dict = {
        "representations": style,
        "chosenAtomsColor": "red",
        "chosenAtomsRadius": 1,
        "molSpacingXaxis": 100,
        "sideByside": sidebyside_bool
    }

    data_list = [ngl_parser.get_data(data_path=data_path, pdb_id=molecule, color='red',
                                     reset_view=True, local=False)
                 for molecule in ['NSP2', 'NSP4']]

    return data_list, molstyles_dict

if __name__ == '__main__':
    app.run_server(debug=True)
