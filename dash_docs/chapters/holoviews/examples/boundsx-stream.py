# -*- coding: utf-8 -*-
import dash
import dash_html_components as html

import pandas as pd
import numpy as np
import holoviews as hv
from holoviews import streams
from holoviews.plotting.plotly.dash import to_dash

n = 200
np.random.seed(20)
xs = np.linspace(0, 1, n)
ys = np.cumsum(np.random.randn(n))
df = pd.DataFrame({'x': xs, 'y': ys})
curve = hv.Scatter(df)


def make_from_boundsx(boundsx):
    sub = df.set_index('x').loc[boundsx[0]:boundsx[1]]
    return hv.Table(sub.describe().reset_index().values, 'stat', 'value')


dmap = hv.DynamicMap(
    make_from_boundsx, streams=[streams.BoundsX(source=curve, boundsx=(0, 0))]
)

layout = curve + dmap

# Create App
app = dash.Dash(__name__)

# Dash display
components = to_dash(
    app, [layout], reset_button=True
)

app.layout = html.Div(components.children)

if __name__ == '__main__':
    app.run_server(debug=True)
