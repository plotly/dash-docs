# -*- coding: utf-8 -*-
import dash
import dash_html_components as html

import numpy as np
import holoviews as hv
from holoviews import streams
from holoviews.plotting.plotly.dash import to_dash

# Declare distribution of Points
points = hv.Points(
    np.random.multivariate_normal((0, 0), [[1, 0.1], [0.1, 1]], (1000,))
)

# Declare points selection
sel = streams.Selection1D(source=points)

# Declare DynamicMap computing mean y-value of selection
mean_sel = hv.DynamicMap(
    lambda index: hv.HLine(points['y'][index].mean() if index else -10),
    kdims=[], streams=[sel]
)

# Declare a Bounds stream and DynamicMap to get box_select geometry and draw it
box = streams.BoundsXY(source=points, bounds=(0,0,0,0))
bounds = hv.DynamicMap(lambda bounds: hv.Bounds(bounds), streams=[box])

# Declare DynamicMap to apply bounds selection
dmap = hv.DynamicMap(lambda bounds: points.select(x=(bounds[0], bounds[2]),
                                                  y=(bounds[1], bounds[3])),
                     streams=[box])

# Compute histograms of selection along x-axis and y-axis
yhist = hv.operation.histogram(
    dmap, bin_range=points.range('y'), dimension='y', dynamic=True, normed=False
)
xhist = hv.operation.histogram(
    dmap, bin_range=points.range('x'), dimension='x', dynamic=True, normed=False
)

# Combine components and display
layout = points * mean_sel * bounds << yhist << xhist

# Create App
app = dash.Dash(__name__)
components = to_dash(
    app, [layout], reset_button=True
)

app.layout = html.Div(
    [components.graphs[0], components.resets[0], components.store]
)

if __name__ == "__main__":
    app.run_server(debug=True)
