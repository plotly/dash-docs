import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

HOSTED_GENOME_DICT = [
    {'value': 'mm10', 'label': 'Mouse (GRCm38/mm10)'},
    {'value': 'hg19', 'label': 'Human (GRCh37/hg19)'}
]

HOSTED_GENOME_TRACKS = {
    'mm10': {
        'range': {
            'contig': 'chr17',
            'start': 7512284,
            'stop': 7512644
        },
        'reference': {
            'label': 'mm10',
            'url': 'https://hgdownload.cse.ucsc.edu/goldenPath/mm10/bigZips/mm10.2bit'
        },
        'tracks': [
            {
                'viz': 'scale',
                'label': 'Scale'
            },
            {
                'viz': 'location',
                'label': 'Location'
            }]
    },
    'hg19': {
        'range': {
            'contig': 'chr17',
            'start': 7512284,
            'stop': 7512644
        },
        'reference': {
            'label': 'hg19',
            'url': 'https://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/hg19.2bit'
        },
        'tracks': [{
                'viz': 'scale',
                'label': 'Scale'
            },
            {
                'viz': 'location',
                'label': 'Location'
            },
            {
                'viz': 'genes',
                'label': 'genes',
                'source': 'bigBed',
                'sourceOptions': {'url': 'http://www.biodalliance.org/datasets/ensGene.bb'}
            }]
    }
}

app.layout = html.Div([
    dcc.Loading(
        id='pileup-container'
    ),
    html.Hr(),
    html.P('Select the genome to display below.'),
    dcc.Dropdown(
        id='pileup-genome-select',
        options=HOSTED_GENOME_DICT,
        value='hg19'
    )
])


# Return the Pileup component with the selected genome.
@app.callback(
    Output('pileup-container', 'children'),
    Input('pileup-genome-select', 'value')
)
def return_pileup(genome):

    if HOSTED_GENOME_TRACKS.get(genome) is None:
        raise Exception("No tracks for genome %s" % genome)

    return (
        html.Div([
            dashbio.Pileup(
                id = 'default-pileup',
                range = HOSTED_GENOME_TRACKS[genome]['range'],
                reference = HOSTED_GENOME_TRACKS[genome]['reference'],
                tracks = HOSTED_GENOME_TRACKS[genome]['tracks']
            )
        ])
    )


if __name__ == '__main__':
    app.run_server(debug=True)
