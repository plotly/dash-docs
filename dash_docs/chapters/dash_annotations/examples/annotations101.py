import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from skimage import data

img = data.chelsea()
fig = px.imshow(img)
fig.update_layout(dragmode="drawrect")
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

app = dash.Dash(__name__)
app.layout = html.Div(
    [html.H3("Drag and draw annotations"), dcc.Graph(figure=fig, config=config),]
)

if __name__ == "__main__":
    app.run_server(debug=True)
