import json
import six.moves.urllib.request as urlreq

import dash
import dash_bio as dashbio
import dash_html_components as html
import dash_core_components as dcc


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = urlreq.urlopen("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/needle_PIK3CA.json").read().decode("utf-8")

mdata = json.loads(data)

app.layout = html.Div([
    "Show or hide range slider",
    dcc.Dropdown(
        id='needleplot-rangeslider',
        options=[
            {'label': 'Show', 'value': True},
            {'label': 'Hide', 'value': False}
        ],
        clearable=False,
        multi=False,
        value=True
    ),
    dashbio.NeedlePlot(
        id='my-dashbio-needleplot',
        mutationData=mdata
    )
])


@app.callback(
    dash.dependencies.Output('my-dashbio-needleplot', 'rangeSlider'),
    [dash.dependencies.Input('needleplot-rangeslider', 'value')]
)
def update_needleplot(show_rangeslider):
    return show_rangeslider


if __name__ == '__main__':
    app.run_server(debug=True)
