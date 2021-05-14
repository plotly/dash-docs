import dash
import dash_html_components as html
import holoviews as hv
from holoviews.plotting.plotly.dash import to_dash
from holoviews.element.tiles import CartoDark
from plotly.data import carshare

# Convert from lon/lat to web-mercator easting/northing coordinates
df = carshare()
df["easting"], df["northing"] = hv.Tiles.lon_lat_to_easting_northing(
    df["centroid_lon"], df["centroid_lat"]
)

points = hv.Points(df, ["easting", "northing"]).opts(color="crimson")
tiles = CartoDark()
overlay = tiles * points

app = dash.Dash(__name__)
components = to_dash(app, [overlay])

app.layout = html.Div(
    components.children
)

if __name__ == '__main__':
    app.run_server(debug=True)
