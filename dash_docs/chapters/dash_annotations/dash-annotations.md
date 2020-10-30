---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.7.3
---

# Image annotations with Dash

This tutorial shows how to annotate images with different drawing tools in plotly figures, and how to use such annotations in Dash apps.

## Annotation tools in plotly figures

With the plotly graphing library, [it is possible to draw annotations on Cartesian axes](https://plotly.com/python/shapes/#drawing-shapes-on-cartesian-plots), which are recorded as shape elements of the figure layout. 

In order to use the drawing tools of a plotly figure, one must set its dragmode to one of the available drawing tools. This can be done programmatically, by setting the `dragmode` attribute of the figure `layout`, or by selecting a drawing tool in the modebar of the figure. Since buttons corresponding to drawing tools are not included in the default modebar, one must specify the buttons to add in the `config` prop of the `dcc.Graph` containing the plotly figure.

In the figure below, you can try to draw a rectangle by left-clicking and dragging, then you can try the other drawing buttons of the modebar.

```python
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from skimage import data
import json

img = data.chelsea()
fig = px.imshow(img)
fig.update_layout(
    dragmode='drawrect')
config={'modeBarButtonsToAdd':
        ['drawline',
         'drawopenpath',
         'drawclosedpath',
         'drawcircle',
         'drawrect',
          'eraseshape']}

app = JupyterDash(__name__)
app.layout = html.Div([
    html.H3("Drag and draw annotations"),
    dcc.Graph(figure=fig, config=config),
])

app.run_server(mode='inline', port=8050)
```

## Dash callback triggered when drawing annotations

When using a plotly figure in a `dcc.Graph` component in a Dash app, drawing a shape on the figure will modify the `relayoutData` property of the `dcc.Graph`. You can therefore define a callback listening to `relayoutData`. In the example below we display the content of `relayoutData` inside an `html.Pre`, so that we can inspect the structure of `relayoutData` (when developing your app, you can also just print the variable inside the callback to inspect it). 

```python
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from skimage import data
import json

img = data.chelsea()
fig = px.imshow(img)
fig.update_layout(
    dragmode='drawrect')


app = JupyterDash(__name__)
app.layout = html.Div([
    html.H3("Drag and draw rectangle annotations"),
    dcc.Graph(id='graph-picture', figure=fig),
    dcc.Markdown('Characteristics of shapes'),
    html.Pre(id='annotations-data'),
])


@app.callback(
    Output('annotations-data', 'children'),
    [Input("graph-picture", "relayoutData")],
    prevent_initial_call=True
)
def on_new_annotation(relayout_data):
    if 'shapes' in relayout_data:
        return json.dumps(relayout_data['shapes'], indent=2)
    else:
        return dash.no_update

app.run_server(mode='inline', port=8051)
```

In the example below, we add all the available drawing tools to the modebar, so that you can inspect the characteristics of drawn shapes for the different types of shapes: rectangles, circles, lines, closed and open paths. 

Rectangles, circles or ellipses and lines are all defined by their bounding-box rectangle, that is by the coordinates of the start and end corners of the rectangle, `x0`, `y0`, `x1` and `y1`. 

As for paths, open and closed, their geometry is defined as an [SVG path](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics). 

```python
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from skimage import data
import json

img = data.chelsea()
fig = px.imshow(img)
fig.update_layout(
    dragmode='drawclosedpath')
config={'modeBarButtonsToAdd':
        ['drawline',
         'drawopenpath',
         'drawclosedpath',
         'drawcircle',
         'drawrect',
          'eraseshape']}

# Build App
app = JupyterDash(__name__)
app.layout = html.Div([
    html.H4("Drag and draw annotations - use the modebar to pick a different drawing tool"),
    dcc.Graph(id='graph-pic', figure=fig, config=config),
    dcc.Markdown('Characteristics of shapes'),
    html.Pre(id='annotations-data-pre'),
])# Define callback to update graph

@app.callback(
    Output('annotations-data-pre', 'children'),
    [Input("graph-pic", "relayoutData")],
    prevent_initial_call=True
)
def on_new_annotation(relayout_data):
    if 'shapes' in relayout_data:
        return json.dumps(relayout_data['shapes'], indent=2)
    else:
        return dash.no_update

app.run_server(mode='inline', port=8052)
```

## Changing the style of annotations

The style of annotations can be changed thanks to interactive components such as sliders, dropdowns, or color pickers. Their values can be used in a callback to define the `newshape` attribute of the figure layout, as in the following example.

```python
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
from skimage import data
import json

img = data.chelsea()
fig = px.imshow(img)
fig.update_layout(
    dragmode='drawrect',
    newshape=dict(
        fillcolor='cyan', 
        opacity=0.3,
        line=dict(color='darkblue', width=8))
)

app = JupyterDash(__name__)
app.layout = html.Div([
    html.H3("Drag and draw annotations"),
    dcc.Graph(id='graph-styled-annotations', figure=fig),
    dcc.Slider(id='opacity-slider', min=0, max=1, value=0.5, step=0.1),
    daq.ColorPicker(
        id='my-color-picker',
        label='Color Picker',
        value=dict(hex='#119DFF')
    ),
])

@app.callback(
    Output('graph-styled-annotations', 'figure'),
    [Input("opacity-slider", "value"),
     Input("my-color-picker", "value")],
    prevent_initial_call=True
)
def on_style_change(slider_value, color_value):
    fig = px.imshow(img)
    fig.update_layout(
        dragmode='drawrect',
        newshape=dict(
            opacity=slider_value,
            fillcolor=color_value['hex'])
    )
    return fig

app.run_server(mode='inline', port=8053)
```

### Extracting an image subregion defined by an annotation

Rather than the geometry of annotations, one is often interested in extracting the region of interest of the image delineated by the shape. The two examples show how to do this first for rectangles, and then for a closed path. In these two examples, the histogram of the region delineated by the latest shape is displayed.

```python
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from skimage import data, exposure
import json

img = data.camera()
fig = px.imshow(img, binary_string=True)
fig.update_layout(
    dragmode='drawrect')

fig_hist = px.histogram(img.ravel())

# Build App
app = JupyterDash(__name__)
app.layout = html.Div([
    html.H3("Drag a rectangle to show the histogram of the ROI"),
     html.Div([
         dcc.Graph(id='graph-pic-camera', figure=fig),
    ], style={'width': '60%', 'display': 'inline-block', 'padding': '0 0'}),
    
    html.Div([
        dcc.Graph(id='histogram', figure=fig_hist),
    ], style={'width': '40%', 'display': 'inline-block', 'padding': '0 0'}),

])# Define callback to update graph

@app.callback(
    Output('histogram', 'figure'),
    [Input("graph-pic-camera", "relayoutData")],
    prevent_initial_call=True
)
def on_new_annotation(relayout_data):
    if 'shapes' in relayout_data:
        last_shape = relayout_data['shapes'][-1]
        # shape coordinates are floats, we need to convert to ints for slicing
        x0, y0 = int(last_shape['x0']), int(last_shape['y0'])
        x1, y1 = int(last_shape['x1']), int(last_shape['y1'])
        roi_img = img[y0:y1, x0:x1]
        return px.histogram(roi_img.ravel())
    else:
        return dash.no_update

app.run_server(mode='inline', port=8054)
```

For a path, we need the following steps
- we retrieve the coordinates of the vertices of the path from the SVG path
- we use the function `skimage.draw.polygon` to obtain the coordinates of pixels covered by the path
- then we use the function `scipy.ndimage.binary_fill_holes` in order to set to `True` the pixels enclosed by the path.

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from skimage import data, draw
import json
from scipy import ndimage

def path_to_indices(path):
    """From SVG path to numpy array of coordinates, each row being a (row, col) point
    """
    indices_str = [el.replace('M', '').replace(
        'Z', '').split(',') for el in path.split('L')]
    return np.rint(np.array(indices_str, dtype=float)).astype(np.int)

def path_to_mask(path, shape):
    """From SVG path to a boolean array where all pixels enclosed by the path
    are True, and the other pixels are False.
    """
    cols, rows = path_to_indices(path).T
    rr, cc = draw.polygon(rows, cols)
    mask = np.zeros(shape, dtype=np.bool)
    mask[rr, cc] = True
    mask = ndimage.binary_fill_holes(mask)
    return mask

img = data.camera()
fig = px.imshow(img, binary_string=True)
fig.update_layout(
    dragmode='drawclosedpath')

fig_hist = px.histogram(img.ravel())

# Build App
app = JupyterDash(__name__)
app.layout = html.Div([
    html.H3("Draw a path to show the histogram of the ROI"),
     html.Div([
         dcc.Graph(id='graph-camera', figure=fig),
    ], style={'width': '60%', 'display': 'inline-block', 'padding': '0 0'}),
    
    html.Div([
        dcc.Graph(id='graph-histogram', figure=fig_hist),
    ], style={'width': '40%', 'display': 'inline-block', 'padding': '0 0'}),

])# Define callback to update graph

@app.callback(
    Output('graph-histogram', 'figure'),
    [Input("graph-camera", "relayoutData")],
    prevent_initial_call=True
)
def on_new_annotation(relayout_data):
    if 'shapes' in relayout_data:
        last_shape = relayout_data['shapes'][-1]
        mask = path_to_mask(last_shape['path'], img.shape)
        return px.histogram(img[mask])
    else:
        return dash.no_update

app.run_server(mode='inline', port=8055)
```

## Modifying shapes and parsing `relayoutData`

When adding a new shape, the `relayoutData` variable consists in the list of all layout shapes. It is also possible to delete a shape by selecting an existing shape, and by clicking the "delete shape" button in the modebar.

Also, existing shapes can be modified if their `editable` property is set to True. In the example below, you can
- draw a shape
- then click on the shape perimeter to select the shape
- drag one of its vertices to modify the shape

Observe that when modifying the shape, only the modified geometrical parameters are found in the `relayoutData`. 

```python
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from skimage import data
import json

img = data.chelsea()
fig = px.imshow(img)
fig.update_layout(
    dragmode='drawclosedpath')
config={'modeBarButtonsToAdd':
        ['drawline',
         'drawopenpath',
         'drawclosedpath',
         'drawcircle',
         'drawrect',
          'eraseshape']}

# Build App
app = JupyterDash(__name__)
app.layout = html.Div([
    html.H4("Draw a shape, then modify it"),
    dcc.Graph(id='fig-image', figure=fig, config=config),
    dcc.Markdown('Characteristics of shapes'),
    html.Pre(id='annotations-pre'),
])# Define callback to update graph

@app.callback(
    Output('annotations-pre', 'children'),
    [Input("fig-image", "relayoutData")],
    prevent_initial_call=True
)
def on_new_annotation(relayout_data):
    for key in relayout_data:
        if 'shapes' in key:
            return json.dumps(relayout_data[key], indent=2)
    return dash.no_update
   

app.run_server(mode='inline', port=8056)
```

The example below extends on the previous one where the histogram of a ROI is displayed. Here, we tackle both the case where a new shape is drawn, and where an existing shape is modified.

```python
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from skimage import data, exposure
import json



img = data.camera()
fig = px.imshow(img, binary_string=True)
fig.update_layout(
    dragmode='drawrect')

fig_hist = px.histogram(img.ravel())

# Build App
app = JupyterDash(__name__)
app.layout = html.Div([
    html.H3("Draw a shape, then modify it."),
     html.Div([
         dcc.Graph(id='fig-pic', figure=fig),
    ], style={'width': '60%', 'display': 'inline-block', 'padding': '0 0'}),
    
    html.Div([
        dcc.Graph(id='graph-hist', figure=fig_hist),
    ], style={'width': '40%', 'display': 'inline-block', 'padding': '0 0'}),
    html.Pre(id='annotations'),
])# Define callback to update graph

@app.callback(
    [Output('graph-hist', 'figure'),
     Output('annotations', 'children')],
    [Input("fig-pic", "relayoutData")],
    prevent_initial_call=True
)
def on_relayout(relayout_data):
    x0, y0, x1, y1 = (None,) * 4
    if 'shapes' in relayout_data:
        last_shape = relayout_data['shapes'][-1]
        x0, y0 = int(last_shape['x0']), int(last_shape['y0'])
        x1, y1 = int(last_shape['x1']), int(last_shape['y1'])
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
    elif any(['shapes' in key for key in relayout_data]):
        x0 = int([relayout_data[key] for key in relayout_data if 'x0' in key][0])
        x1 = int([relayout_data[key] for key in relayout_data if 'x1' in key][0])
        y0 = int([relayout_data[key] for key in relayout_data if 'y0' in key][0])
        y1 = int([relayout_data[key] for key in relayout_data if 'y1' in key][0])
    if all((x0, y0, x1, y1)):
        roi_img = img[y0:y1, x0:x1]
        return (px.histogram(roi_img.ravel()),
                json.dumps(relayout_data, indent=2))
    else:
        return (dash.no_update,) * 2

app.run_server(mode='inline', port=8057)
```

## Storing annotations in a dcc.Store component

When building a training set for deep learning, or in other applications, one needs to store and save image annotations for future use. This can be done using a`dcc.Store` component.

The example implements an image carousel where annotations are stored for each image. When the sequence comes back to a previously annotated image, annotations are read from the store and displayed as layout shapes on the image.

```python
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from skimage import data
import json

images = [data.chelsea(), data.astronaut()]
fig = px.imshow(images[0])
fig.update_layout(
    dragmode='drawrect',
    newshape_line_color='yellow'
)

app = JupyterDash(__name__)
app.layout = html.Div([
    dcc.Graph(id='image-carousel', figure=fig),
    html.Button('Next', id='next-btn', style={'width':'40%'}),
    dcc.Store(id='store', data={})
])



@app.callback(
    Output("store", "data"),
    [Input("image-carousel", "relayoutData")],
    [State("next-btn", "n_clicks"),
     State("store", "data")],
    prevent_initial_call=True
)
def on_new_shape(relayoutData, n_clicks, store_data):
    image_nb = n_clicks % len(images) if n_clicks is not None else 0
    store_data[image_nb] = relayoutData
    return store_data
    
    
@app.callback(
    Output('image-carousel', 'figure'),
    [Input("next-btn", "n_clicks")],
    [State("store", "data")],
    prevent_initial_call=True
)
def on_next(n_clicks, store_data):
    image_nb = n_clicks % len(images)
    print(store_data)
    fig = px.imshow(images[image_nb])
    fig.update_layout(
        dragmode='drawrect',
        newshape_line_color='yellow'
    )
    if str(image_nb) in store_data:
        fig.update_layout(shapes=store_data[str(image_nb)]['shapes'])
    return fig   

app.run_server(mode='inline', port=8058)
```
