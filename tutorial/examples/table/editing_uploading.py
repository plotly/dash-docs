import base64
import datetime
import io
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='dash-table-upload',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%', 'height': '60px', 'lineHeight': '60px',
            'borderWidth': '1px', 'borderStyle': 'dashed',
            'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'
        },
    ),
    dash_table.Table(id='dash-table-upload-container'),
    dcc.Graph(id='dash-table-upload-graph')
])


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    if 'csv' in filename:
        # Assume that the user uploaded a CSV file
        return pd.read_csv(
            io.StringIO(decoded.decode('utf-8')))
    elif 'xls' in filename:
        # Assume that the user uploaded an excel file
        return pd.read_excel(io.BytesIO(decoded))


@app.callback(Output('dash-table-upload-container', 'dataframe'),
              [Input('dash-table-upload', 'contents')],
              [State('dash-table-upload', 'filename')])
def update_output(contents, filename):
    if contents is None:
        return [{}]
    df = parse_contents(contents, filename)
    return df.to_dict('rows')


@app.callback(Output('dash-table-upload-graph', 'figure'),
              [Input('dash-table-upload-container', 'dataframe')])
def display_graph(rows):
    df = pd.DataFrame(rows)
    return {
        'data': [{
            'x': df[df.columns[0]],
            'y': df[df.columns[1]],
            'type': 'bar'
        }]
    }


if __name__ == '__main__':
    app.run_server(debug=True)
