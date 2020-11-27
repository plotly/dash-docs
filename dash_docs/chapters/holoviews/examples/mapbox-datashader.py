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

# Duplicate carshare dataframe with Gaussian noise to produce a larger dataframe
df = pd.concat([df_original] * 5000)
df["easting"] = df["easting"] + np.random.randn(len(df)) * 400
df["northing"] = df["northing"] + np.random.randn(len(df)) * 400

# Build Dataset and graphical elements
dataset = hv.Dataset(df)
points = hv.Points(
    df, ["easting", "northing"]
).opts(color="crimson")
tiles = hv.Tiles("").opts(mapboxstyle="light", accesstoken=mapbox_token)
overlay = tiles * datashade(points, cmap=sequential.Plasma)
overlay.opts(
    title="Mapbox Datashader with %d points" % len(df),
    width=800,
    height=500
)

# Build App
app = dash.Dash(__name__)
components = to_dash(app, [overlay], reset_button=True)

app.layout = html.Div(
    components.children
)

if __name__ == '__main__':
    app.run_server(debug=True)
