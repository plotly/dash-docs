import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from skimage import data, exposure
import json

img = data.camera()
fig = px.imshow(img, binary_string=True)
fig.update_layout(dragmode="drawrect")

fig_hist = px.histogram(img.ravel())

# Build App
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H3("Draw a shape, then modify it."),
        html.Div(
            [dcc.Graph(id="fig-pic", figure=fig),],
            style={"width": "60%", "display": "inline-block", "padding": "0 0"},
        ),
        html.Div(
            [dcc.Graph(id="graph-hist", figure=fig_hist),],
            style={"width": "40%", "display": "inline-block", "padding": "0 0"},
        ),
        html.Pre(id="annotations"),
    ]
)


@app.callback(
    Output("graph-hist", "figure"),
    Output("annotations", "children"),
    Input("fig-pic", "relayoutData"),
    prevent_initial_call=True,
)
def on_relayout(relayout_data):
    x0, y0, x1, y1 = (None,) * 4
    if "shapes" in relayout_data:
        last_shape = relayout_data["shapes"][-1]
        x0, y0 = int(last_shape["x0"]), int(last_shape["y0"])
        x1, y1 = int(last_shape["x1"]), int(last_shape["y1"])
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
    elif any(["shapes" in key for key in relayout_data]):
        x0 = int([relayout_data[key] for key in relayout_data if "x0" in key][0])
        x1 = int([relayout_data[key] for key in relayout_data if "x1" in key][0])
        y0 = int([relayout_data[key] for key in relayout_data if "y0" in key][0])
        y1 = int([relayout_data[key] for key in relayout_data if "y1" in key][0])
    if all((x0, y0, x1, y1)):
        roi_img = img[y0:y1, x0:x1]
        return (px.histogram(roi_img.ravel()), json.dumps(relayout_data, indent=2))
    else:
        return (dash.no_update,) * 2


if __name__ == "__main__":
    app.run_server(mode="inline", port=8057)
