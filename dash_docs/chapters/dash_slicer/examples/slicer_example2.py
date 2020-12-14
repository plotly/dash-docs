import dash
import dash_html_components as html
import imageio
from dash_slicer import VolumeSlicer


app = dash.Dash(__name__, update_title=None)

vol = imageio.volread("imageio:stent.npz")
slicer0 = VolumeSlicer(app, vol, axis=0)
slicer1 = VolumeSlicer(app, vol, axis=1)
slicer2 = VolumeSlicer(app, vol, axis=2)

app.layout = html.Div(
    style={
        "display": "grid",
        "gridTemplateColumns": "33% 33% 33%",
    },
    children=[
        html.Div([slicer0.graph, html.Br(), slicer0.slider, *slicer0.stores]),
        html.Div([slicer1.graph, html.Br(), slicer1.slider, *slicer1.stores]),
        html.Div([slicer2.graph, html.Br(), slicer2.slider, *slicer2.stores]),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_props_check=False)
