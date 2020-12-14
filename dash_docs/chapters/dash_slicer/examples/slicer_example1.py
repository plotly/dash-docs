import dash
import dash_html_components as html
import imageio
from dash_slicer import VolumeSlicer


app = dash.Dash(__name__, update_title=None)

vol = imageio.volread("imageio:stent.npz")
slicer = VolumeSlicer(app, vol)

app.layout = html.Div([slicer.graph, slicer.slider, *slicer.stores])


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_props_check=False)