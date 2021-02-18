import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import dash_bio_utils.ngl_parser as ngl_parser

'''
### Selecting Molecule Chains and Atoms

The molecule data must be entered in a specific format to define how many molecules should be shown
and/or which chains on those molecules are shown. Specific ranges of amino acids and atoms on the 
molecule can be highlighted as well. To see which filtering options are available to use
with a particular molecule, it may be helpful to view the PDB file entries for a range of atoms 
which specify the atom names, the residues they belong to, and a one-letter code for the chain.

The following format needs to be used:
```
pdbID1.chain:start-end@atom1,atom2
```
 * . indicates that only one chain should be shown
 * : indicates that a specific amino acids range should be shown (e.g. 1-50)
 * @ indicates that chosen atoms should be highlighted (e.g. @50,100,150)


 
 The `ngl_parser` helper function can help simplify this process by generating the 
 appropriate data format based on the string provided in the above format as the `pdb_id` argument.
 It will return a dictionary with the contents of the PDB file, selected residues and ranges, and 
 atoms highlighted in the color selected. Specify whether the data path is locally or remotely 
 hosted with the `local` boolean argument.   
 
 The color and radius of chosen atoms can be set through the `molStyles` property with the
 "chosenAtomsColor" and "chosenAtomsRadius" keys.
'''

app = dash.Dash(__name__)

data_path =  "https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/"


app.layout = html.Div([
    dcc.Input(id="chain-input", placeholder="Eg. 5L73.A:629-819@700,750,800", value="5L73.A:629-819@700,750,800"),
    dcc.Dropdown(id="chain-color", value='black',
                 options=[{"label": s.capitalize(), "value": s} for s in ["black", "white","red", "blue"]]),
    dashbio.NglMoleculeViewer(id="chain-ngl"),
])


@app.callback(
    [Output("chain-ngl", 'data'),
     Output("chain-ngl", "molStyles")],
    [Input("chain-input", "value"),
     Input("chain-color", "value")]
)
def return_molecule(value, color):
    if (value is None):
        raise PreventUpdate

    molstyles_dict = {
        "representations": ["cartoon", "axes+box"],
        "chosenAtomsColor": color,
        "chosenAtomsRadius": 1,
        "molSpacingXaxis": 100,
    }
    data_list = [ngl_parser.get_data(data_path=data_path, pdb_id=value, color="red",
                            reset_view=True, local=False)]

    return data_list, molstyles_dict

if __name__ == '__main__':
    app.run_server(debug=True)
