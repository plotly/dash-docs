# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
from plotly.data import iris

import holoviews as hv
from holoviews.plotting.plotly.dash import to_dash

# Load dataset
df = iris()
dataset = hv.Dataset(df)

scatter = hv.Scatter(dataset, kdims=["sepal_length"], vdims=["sepal_width"])
hist = hv.operation.histogram(
    dataset, dimension="petal_width", normed=False
)

app = dash.Dash(__name__)
components = to_dash(app, [scatter, hist])

app.layout = html.Div(components.children)

if __name__ == "__main__":
    app.run_server(debug=True)
