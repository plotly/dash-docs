import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from skimage import data
import json

img = data.camera()
fig = px.imshow(img, binary_string=True)
fig.update_layout(dragmode="drawrect")

fig_hist = px.histogram(img.ravel())

# Build App
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H3("Drag a rectangle to show the histogram of the ROI"),
        html.Div(
            [dcc.Graph(id="graph-pic-camera", figure=fig),],
            style={"width": "60%", "display": "inline-block", "padding": "0 0"},
        ),
        html.Div(
            [dcc.Graph(id="histogram", figure=fig_hist),],
            style={"width": "40%", "display": "inline-block", "padding": "0 0"},
        ),
    ]
)


@app.callback(
    Output("histogram", "figure"),
    [Input("graph-pic-camera", "relayoutData")],
    prevent_initial_call=True,
)
def on_new_annotation(relayout_data):
    if "shapes" in relayout_data:
        last_shape = relayout_data["shapes"][-1]
        # shape coordinates are floats, we need to convert to ints for slicing
        x0, y0 = int(last_shape["x0"]), int(last_shape["y0"])
        x1, y1 = int(last_shape["x1"]), int(last_shape["y1"])
        roi_img = img[y0:y1, x0:x1]
        return px.histogram(roi_img.ravel())
    else:
        return dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
