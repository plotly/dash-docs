import dash
from dash.dependencies import Output, Input
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(prevent_initial_callbacks=True)

app.layout = html.Div([html.Button('Download', id='btn'), dcc.Download(id='download')])

@app.callback(Output('download', 'data'), Input('btn', 'n_clicks'))
def func(n_clicks):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    else:
        return dict(content='Hello world!', filename='hello.txt')

if __name__ == '__main__':
    app.run_server(debug=True)
