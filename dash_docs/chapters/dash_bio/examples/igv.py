import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

HOSTED_GENOME_DICT = [
    {'value': 'mm10', 'label': 'Mouse (GRCm38/mm10)'},
    {'value': 'rn6', 'label': 'Rat (RGCS 6.0/rn6)'},
    {'value': 'gorGor4', 'label': 'Gorilla (gorGor4.1/gorGor4)'},
    {'value': 'panTro4', 'label': 'Chimp (SAC 2.1.4/panTro4)'},
    {'value': 'panPan2', 'label': 'Bonobo (MPI-EVA panpan1.1/panPan2)'},
    {'value': 'canFam3', 'label': 'Dog (Broad CanFam3.1/canFam3)'},
    {'value': 'ce11', 'label': 'C. elegans (ce11)'}
]

app.layout = html.Div([
    dcc.Loading(
        id='igv-container'
    ),
    html.Hr(),
    html.P('Select the genome to display below.'),
    dcc.Dropdown(
        id='igv-genome-select',
        options=HOSTED_GENOME_DICT,
        value='ce11'
    )
])



# Return the IGV component with the selected genome.
@app.callback(
    Output('igv-container', 'children'),
    Input('igv-genome-select', 'value')
)
def return_igv(genome):
    return (
        html.Div([
            dashbio.Igv(
                id='default-igv',
                genome=genome,
                minimumBases=100,
            )
        ])
    )


if __name__ == '__main__':
    app.run_server(debug=True)
