# -*- coding: utf-8 -*-
import dash
import dash_html_components as html

import numpy as np
import holoviews as hv
from holoviews.plotting.plotly.dash import to_dash

# Define an image
Y, X = (np.mgrid[0:100, 0:100]-50.)/20.
img = hv.Image(np.sin(X**2+Y**2))

def selected_hist(x_range, y_range):
    # Apply current ranges
    obj = img.select(x=x_range, y=y_range) if x_range and y_range else img

    # Compute histogram
    return hv.operation.histogram(obj)

# Define a RangeXY stream linked to the image
rangexy = hv.streams.RangeXY(source=img)

# Adjoin the dynamic histogram computed based on the current ranges
layout = img << hv.DynamicMap(selected_hist, streams=[rangexy])

# Create App
app = dash.Dash(__name__)

# Dash display
components = to_dash(
    app, [layout], reset_button=True
)

app.layout = html.Div(components.children)

if __name__ == '__main__':
    app.run_server(debug=True)
