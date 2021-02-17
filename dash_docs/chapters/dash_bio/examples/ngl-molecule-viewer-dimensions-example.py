import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_bio_utils.ngl_parser as ngl_parser


'''
### Height and Width

The Height and Width (in px or as a number) of the container in which the molecules will be 
displayed.
'''

app = dash.Dash(__name__)

data_path =  "https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/"


app.layout = html.Div([
    dcc.Slider(id='height-ngl', min=300, max=800, value=600,
                    step=100, marks={300: '300px',800: '800px'}),
    dcc.Slider(id='width-ngl', min=300, max=800, value=600,
                    step=100, marks={300: '300px', 800: '800px'}),
    dashbio.NglMoleculeViewer(id="dimensions-ngl"),
])


@app.callback(
    [Output("dimensions-ngl", 'data'),
     Output("dimensions-ngl", "molStyles"),
     Output("dimensions-ngl", "height"),
     Output("dimensions-ngl", "width")],
    [Input("height-ngl", "value"),
     Input("width-ngl", "value")]
)
def return_molecule(height, width):
    molstyles_dict = {
        "representations": ["cartoon", "axes+box"],
        "chosenAtomsColor": "red",
        "chosenAtomsRadius": 1,
        "molSpacingXaxis": 100,
    }

    data_list = [ngl_parser.get_data(data_path=data_path, pdb_id='1BNA', color='red',
                                     reset_view=True, local=False)]


    return data_list, molstyles_dict, height, width

if __name__ == '__main__':
    app.run_server(debug=True)
