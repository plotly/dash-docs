import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
from skimage import data

img = data.chelsea()
fig = px.imshow(img)
fig.update_layout(
    dragmode="drawrect",
    newshape=dict(fillcolor="cyan", opacity=0.3, line=dict(color="darkblue", width=8)),
)

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H3("Drag and draw annotations"),
        dcc.Graph(id="graph-styled-annotations", figure=fig),
        html.Pre('Opacity of annotations'),
        dcc.Slider(id="opacity-slider", min=0, max=1, value=0.5, step=0.1, tooltip={'always_visible':True}),
        daq.ColorPicker(
            id="annotation-color-picker", label="Color Picker", value=dict(hex="#119DFF")
        ),
    ]
)


@app.callback(
    Output("graph-styled-annotations", "figure"),
    Input("opacity-slider", "value"),
    Input("annotation-color-picker", "value"),
    prevent_initial_call=True,
)
def on_style_change(slider_value, color_value):
    fig = px.imshow(img)
    fig.update_layout(
        dragmode="drawrect",
        newshape=dict(opacity=slider_value, fillcolor=color_value["hex"]),
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
