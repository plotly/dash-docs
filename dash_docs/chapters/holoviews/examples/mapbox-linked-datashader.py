import dash
import dash_html_components as html
import holoviews as hv
from holoviews.plotting.plotly.dash import to_dash
from holoviews.operation.datashader import datashade
import pandas as pd
import numpy as np
from plotly.data import carshare
from plotly.colors import sequential

# Mapbox token (replace with your own token string)
mapbox_token = open(".mapbox_token").read()

# Convert from lon/lat to web-mercator easting/northing coordinates
df_original = carshare()
df_original["easting"], df_original["northing"] = hv.Tiles.lon_lat_to_easting_northing(
    df_original["centroid_lon"], df_original["centroid_lat"]
)

# Duplicate carshare dataframe with noise to produce a larger dataframe
df = pd.concat([df_original] * 5000)
df["easting"] = df["easting"] + np.random.randn(len(df)) * 400
df["northing"] = df["northing"] + np.random.randn(len(df)) * 400

# Build HoloViews Dataset and visual elements
dataset = hv.Dataset(df).redim.label(car_hours="Car Hours")
points = hv.Points(
    df, ["easting", "northing"]
).opts(color="crimson")
tiles = hv.Tiles("").opts(mapboxstyle="light", accesstoken=mapbox_token)
overlay = tiles * datashade(points, cmap=sequential.Plasma).opts(width=800)

# Build histogram of car_hours column
hist = hv.operation.histogram(dataset, dimension="car_hours", normed=False)

# Use plot hook to set the default drag mode to horizontal box selection
def set_hist_dragmode(plot, element):
    fig = plot.state
    fig['layout']['dragmode'] = "select"
    fig['layout']['selectdirection'] = "h"

hist.opts(hooks=[set_hist_dragmode], color="rebeccapurple", margins=(50, 50, 50, 30))

# Link selections across datashaded points and histogram
selection_linker = hv.selection.link_selections.instance()
linked_points = selection_linker(
    tiles * datashade(points, cmap=sequential.Plasma)
).opts(title="Datashader with %d points" % len(dataset), margins=(50, 0, 50, 30))
linked_hist = selection_linker(hist)

# Build app
app = dash.Dash(__name__)
components = to_dash(app, [linked_points, linked_hist], reset_button=True)

app.layout = html.Div(
    components.children
)

if __name__ == '__main__':
    app.run_server(debug=True)
