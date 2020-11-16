import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from skimage import data
import json

img = data.chelsea()
fig = px.imshow(img)
fig.update_layout(dragmode="drawclosedpath")
config = {
    "modeBarButtonsToAdd": [
        "drawline",
        "drawopenpath",
        "drawclosedpath",
        "drawcircle",
        "drawrect",
        "eraseshape",
    ]
}

# Build App
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H4("Draw a shape, then modify it"),
        dcc.Graph(id="fig-image", figure=fig, config=config),
        dcc.Markdown("Characteristics of shapes"),
        html.Pre(id="annotations-pre"),
    ]
) 


@app.callback(
    Output("annotations-pre", "children"),
    [Input("fig-image", "relayoutData")],
    prevent_initial_call=True,
)
def on_new_annotation(relayout_data):
    for key in relayout_data:
        if "shapes" in key:
            return json.dumps(key + ': ' + relayout_data[key], indent=2)
    return dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
