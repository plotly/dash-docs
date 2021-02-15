import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_bio_utils.ngl_parser as ngl_parser

'''
### Stage

Similar to the molecular styles, the stage parameters can also be set. The background color, quality
of the render, and the camera perspective are part of the `stageParameters` prop, and can be passed
as keys of a `dict`. 
'''

app = dash.Dash(__name__)

data_path =  "https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/"


app.layout = html.Div([
    dcc.Dropdown(id="color-dropdown", value='white',
                 options=[{"label": s.capitalize(), "value": s} for s in ["black", "white"]]),
    dcc.Dropdown(id="quality-dropdown", value='auto',
                     options=[{"label": s.capitalize(), "value": s}
                              for s in ["auto", "low", "medium", "high"]]),
    dcc.Dropdown(id="camera-dropdown", value='perspective',
                     options=[{"label": s.capitalize(), "value": s}
                              for s in ["perspective", "orthographic"]]),
    dashbio.NglMoleculeViewer(id="stage-ngl"),
])


@app.callback(
    [Output("stage-ngl", 'data'),
     Output("stage-ngl", "molStyles"),
     Output("stage-ngl", "stageParameters")],
    [Input("color-dropdown", "value"),
     Input("quality-dropdown", "value"),
     Input("camera-dropdown", "value")]
)
def return_molecule(color, quality, camera):
    molstyles_dict = {
        "representations": ["cartoon", "axes+box"],
        "chosenAtomsColor": "white",
        "chosenAtomsRadius": 1,
        "molSpacingXaxis": 100,
    }

    stage_params = {
        "quality": quality,
        "backgroundColor": color,
        "cameraType": camera
    }

    data_list = [ngl_parser.get_data(data_path=data_path, pdb_id=molecule, color='red',
                            reset_view=True, local=False)
                 for molecule in ['1BNA', 'PLPR']]

    return data_list, molstyles_dict, stage_params

if __name__ == '__main__':
    app.run_server(debug=True)
