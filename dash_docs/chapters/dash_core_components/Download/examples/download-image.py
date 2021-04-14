import dash
from dash.dependencies import Output, Input
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(prevent_initial_callbacks=True, )
app.layout = html.Div([html.Button("Download", id="btn"), dcc.Download(id="download-image")])

@app.callback(Output("download-image", "data"), Input("btn", "n_clicks"), prevent_initial_call=True)
def func(n_clicks):
    return dcc.send_file("./dash_docs/assets/images/gallery/dash-community-components.png")

if __name__ == '__main__':
    app.run_server(debug=True)
