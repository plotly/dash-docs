import json

import dash
import dash_vtk
import dash_html_components as html
from dash.dependencies import Input, Output

# Get it here: https://github.com/plotly/dash-vtk/blob/master/demos/data/cow-nonormals.obj
with open("datasets/cow-nonormals.obj", 'r') as file:
    txt_content = file.read()

view = dash_vtk.View(
    id="click-info-view",
    pickingModes=["click"],
    children=[
        dash_vtk.GeometryRepresentation(id="cow-geometry", children=[
            dash_vtk.Reader(
                vtkClass="vtkOBJReader",
                parseAsText=txt_content,
            ),
        ]),
    ],
)

# Dash setup
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Div(view, style={"width": "100%", "height": "300px"}),
    html.B("Output of clickInfo (try clicking on the object above):"),
    html.Pre(
        id="click-info-output",
        style={'overflowX': 'scroll'}
    )
])


@app.callback(
    Output('click-info-output', 'children'),
    Input('click-info-view', 'clickInfo')
)
def display_clicked_content(click_info):
    return json.dumps(click_info, indent=2)


if __name__ == "__main__":
    app.run_server(debug=True)
