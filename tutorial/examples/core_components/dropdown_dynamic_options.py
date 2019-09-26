import dash
from dash.exceptions import PreventUpdate
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

options=[
    {'label': 'New York City', 'value': 'NYC'},
    {'label': 'Montreal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = dcc.Dropdown(id='my-dynamic-dropdown')


@app.callback(
    dash.dependencies.Output('my-dynamic-dropdown', 'options'),
    [dash.dependencies.Input('my-dynamic-dropdown', 'search_value')],
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o['label']]


if __name__ == '__main__':
    app.run_server(debug=True)
