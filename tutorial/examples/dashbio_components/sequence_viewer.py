import dash
import dash_bio as dashbio
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dashbio.SequenceViewer(
        id='my-sequence-viewer',
        sequence='MALWMRLLPLLALLALWGPDPAAA\
        FVNQHLCGSHLVEALYLVCGERGFFYTPKTRREA\
        EDLQVGQVELGGGPGAGSLQPLALEGSLQKRGI\
        VEQCCTSICSLYQLENYCN'.replace('    ', ''),
    ),
    html.Div(id='sequence-viewer-output')
])


@app.callback(
    dash.dependencies.Output('sequence-viewer-output', 'children'),
    [dash.dependencies.Input('my-sequence-viewer', 'mouseSelection')]
)
def update_output(value):
    if value is None:
        return 'There is no mouse selection.'
    return 'The mouse selection is {}.'.format(value['selection'])


if __name__ == '__main__':
    app.run_server(debug=True)
