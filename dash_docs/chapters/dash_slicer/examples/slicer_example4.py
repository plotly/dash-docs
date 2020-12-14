import json
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import imageio
from dash_slicer import VolumeSlicer


app = dash.Dash(__name__, update_title=None)

vol = imageio.volread("imageio:stent.npz")
slicer = VolumeSlicer(app, vol)

app.layout = html.Div([slicer.graph, slicer.slider, html.Div(id='info'), *slicer.stores])

@app.callback(
    Output("info", "children"),
    [Input(slicer.state.id, "data")]
)
def update_info(state):
    return json.dumps(state, indent=4)


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_props_check=False)