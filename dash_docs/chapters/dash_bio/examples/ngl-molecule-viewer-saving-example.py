import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import dash_bio_utils.ngl_parser as ngl_parser


'''
### Saving an Image

An image with the selected parameters can be saved as a `.PNG` by flagging the `downloadImage` 
property. With the `imageParameters` optional dict, we can specify whether to enable `antialias`, 
`transparency`, or `trim`, and set the `filename` for the saved image. 
'''

app = dash.Dash(__name__)

data_path =  "https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/"


app.layout = html.Div([
    html.Button(id='save-ngl', n_clicks=0, children="Download Image"),
    dcc.Input(id='file-ngl', placeholder="Enter filename"),
    dashbio.NglMoleculeViewer(id="download-ngl"),
])


@app.callback(
    [Output("download-ngl", 'data'),
     Output("download-ngl", "molStyles"),
     Output("download-ngl", "downloadImage"),
     Output("download-ngl", "imageParameters")],
    [Input("save-ngl", "n_clicks")],
    [State("file-ngl", "value")]
)
def return_molecule(n_clicks, filename):
    molstyles_dict = {
        "representations": ["cartoon", "axes+box"],
        "chosenAtomsColor": "red",
        "chosenAtomsRadius": 1,
        "molSpacingXaxis": 100,
    }

    data_list = [ngl_parser.get_data(data_path=data_path, pdb_id='1BNA', color='red',
                                     reset_view=False, local=False)]

    imageParameters = {
        "antialias": True,
        "transparent": True,
        "trim": True,
        "defaultFilename": filename
    }

    downloadImage = False

    if n_clicks > 0:
        downloadImage=True

    return data_list, molstyles_dict, downloadImage, imageParameters

if __name__ == '__main__':
    app.run_server(debug=True)
