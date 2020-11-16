import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from skimage import data
import json

images = [data.chelsea(), data.astronaut()]
fig = px.imshow(images[0])
fig.update_layout(dragmode="drawrect", newshape_line_color="yellow")

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id="image-carousel", figure=fig),
        html.Button("Next", id="next-btn", style={"width": "40%"}),
        dcc.Store(id="store", data={}),
    ]
)


@app.callback(
    Output("store", "data"),
    [Input("image-carousel", "relayoutData")],
    [State("next-btn", "n_clicks"), State("store", "data")],
    prevent_initial_call=True,
)
def on_new_shape(relayoutData, n_clicks, store_data):
    image_nb = n_clicks % len(images) if n_clicks is not None else 0
    store_data[image_nb] = relayoutData
    return store_data


@app.callback(
    Output("image-carousel", "figure"),
    [Input("next-btn", "n_clicks")],
    [State("store", "data")],
    prevent_initial_call=True,
)
def on_next(n_clicks, store_data):
    image_nb = n_clicks % len(images)
    print(store_data)
    fig = px.imshow(images[image_nb])
    fig.update_layout(dragmode="drawrect", newshape_line_color="yellow")
    if str(image_nb) in store_data:
        fig.update_layout(shapes=store_data[str(image_nb)]["shapes"])
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
