# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
from plotly.data import iris

import holoviews as hv
from holoviews.plotting.plotly.dash import to_dash
from holoviews.operation.datashader import datashade

import numpy as np
import pandas as pd

# Load iris dataset and replicate with noise to create large dataset
df_original = iris()[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
df = pd.concat([
    df_original + np.random.randn(*df_original.shape) * 0.1
    for i in range(10000)
])
dataset = hv.Dataset(df)

scatter = datashade(
    hv.Scatter(dataset, kdims=["sepal_length"], vdims=["sepal_width"])
).opts(title="Datashader with %d points" % len(dataset))

app = dash.Dash(__name__)
components = to_dash(
    app, [scatter], reset_button=True
)

app.layout = html.Div(
    [
        components.graphs[0],
        components.resets[0],
        components.store
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
