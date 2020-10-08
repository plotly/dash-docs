# -*- coding: utf-8 -*-
import dash
import dash_html_components as html

import numpy as np
import holoviews as hv
from holoviews import streams
from holoviews.plotting.plotly.dash import to_dash

# Declare some points
points = hv.Points(np.random.randn(1000,2 ))

# Declare points as source of selection stream
selection = streams.Selection1D(source=points)

# Write function that uses the selection indices to slice points and compute stats
def selected_info(index):
    selected = points.iloc[index]
    if index:
        label = 'Mean x, y: %.3f, %.3f' % tuple(selected.array().mean(axis=0))
    else:
        label = 'No selection'
    return selected.relabel(label).opts(color='red')

# Combine points and DynamicMap
layout = points + hv.DynamicMap(selected_info, streams=[selection])

# Create App
app = dash.Dash(__name__)

# Dash display
components = to_dash(app, [layout], reset_button=True)

app.layout = html.Div(components.children)

if __name__ == '__main__':
    app.run_server(debug=True)
