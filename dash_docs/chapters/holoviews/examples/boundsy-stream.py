# -*- coding: utf-8 -*-
import dash
import dash_html_components as html

import numpy as np
import holoviews as hv
from holoviews import streams
from holoviews.plotting.plotly.dash import to_dash

xs = np.linspace(0, 1, 200)
ys = xs*(1-xs)
curve = hv.Curve((xs,ys))
scatter = hv.Scatter((xs,ys)).opts(size=1)

bounds_stream = streams.BoundsY(source=curve,boundsy=(0,0))

def make_area(boundsy):
    return hv.Area(
        (xs, np.minimum(ys, boundsy[0]), np.minimum(ys, boundsy[1])),
        vdims=['min','max']
    )

def make_items(boundsy):
    times = [
        "{0:.2f}".format(x)
        for x in sorted(np.roots([-1,1,-boundsy[0]])) +
                 sorted(np.roots([-1,1,-boundsy[1]]))
    ]
    return hv.ItemTable(
        sorted(zip(['1_entry', '2_exit', '1_exit', '2_entry'], times))
    )

area_dmap = hv.DynamicMap(make_area, streams=[bounds_stream])
table_dmap = hv.DynamicMap(make_items, streams=[bounds_stream])

layout = (curve * scatter * area_dmap + table_dmap)

# Create App
app = dash.Dash(__name__)

# Dash display
components = to_dash(app, [layout], reset_button=True)

app.layout = html.Div(
    [components.graphs[0], components.resets[0], components.store]
)

if __name__ == '__main__':
    app.run_server(debug=True)
