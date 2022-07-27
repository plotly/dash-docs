import dash_html_components as html
import dash_vtk
from dash_docs import tools
from dash_docs import styles
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)

layout = html.Div([
    rc.Markdown('''
    # Click and Hover Callbacks

    It's possible to create callbacks based on user clicks and hovering. First, you need to specify the `pickingModes` prop in 
    `dash_vtk.View` to be a list of modes you want to capture. The following values are accepted:
    * `"click"`
    * `"hover"`
    
    Afterwards, you need to create callbacks where the inputs and states include one of the following read-only properties of `dash_vtk.View`.
    * `clickInfo`: Called when the user clicks on an object.
    * `hoverInfo`: Called when the user hovers over an object.

    > The full documentation for `dash_vtk.View` can be found in the [API reference](/vtk/reference).

    
    ## Callback structure

    You can notice that the `clickInfo` or `hoverInfo` data will be a dictionary with various keys describing the picked object. The keys include:
    * `displayPosition`: The x,y,z coordinate with on the user's screen.
    * `ray`: A line between two points in 3D space (xyz1, xyz2) that represent the mouse position. It covers the full space under the 2D mouse position.
    * `representationId`: The ID assigned to the `dash_vtk.GeometryRepresentation` containing your object.
    * `worldPosition`:  The x, y, z coordinates in the 3D environment that you are rendering where the ray hit the object. It corresponds to the 3D coordinate on the surface of the object under your mouse.

    '''),
    
    rc.Markdown('''
    ## Output `clickInfo` to `html.Pre`

    The following example shows you how to concisely display the output of `clickInfo` inside an `html.Pre`:
    '''),
    html.Details(open=False, children=[
        html.Summary('View full code'),      
        rc.Markdown(
            examples['t07_click_info.py'][0], 
            style=styles.code_container
        ),
    ]),

    html.Div(
        examples['t07_click_info.py'][1], 
        className='example-container'
    ),

    rc.Markdown('''

    ## Update representation state with `hoverInfo`

    You can also construct more complex hover callbacks, which would affect the `actor` and `state` of your geometry representations. 
    In the [terrain mesh demo](https://dash-gallery.plotly.host/dash-vtk-explorer/pyvista-terrain-following-mesh), whenever you hover
    over the surface, a callback is fired and the output is displayed on your screen:

    ![terrain-following-mesh-hover](/assets/images/vtk/hoverInfoMesh.jpg)

    The full code can be found [here](https://github.com/plotly/dash-vtk/tree/master/demos/pyvista-terrain-following-mesh), but the 
    following snippet summarizes what is needed to capture hover events in the image above:

    ```py
    # ...

    vtk_view = dash_vtk.View(
        id="vtk-view",
        pickingModes=["hover"],
        children=[
            dash_vtk.GeometryRepresentation(id="vtk-representation", ...),
            dash_vtk.GeometryRepresentation(
                id="pick-rep",
                children=[
                    dash_vtk.Algorithm(id="pick-sphere", ...)
                ],
                # ...
            ),
        ],
    )

    app.layout = html.Div([
      # ...,
      vtk_view,
      # ...
    ])

    @app.callback(
        [
            Output("tooltip", "children"),
            Output("pick-sphere", "state"),
            Output("pick-rep", "actor"),
        ],
        [Input("vtk-view", "clickInfo"), Input("vtk-view", "hoverInfo")],
    )
    def onInfo(clickData, hoverData):
        info = hoverData if hoverData else clickData
        if info:
            if (
                "representationId" in info
                and info["representationId"] == "vtk-representation"
            ):
                return (
                    [json.dumps(info, indent=2)],
                    {"center": info["worldPosition"]},
                    {"visibility": True},
                )
            return dash.no_update, dash.no_update, dash.no_update
        return [""], {}, {"visibility": False}
    ```

    You can also use `hoverInfo` to update the state of another geometry representation. The image below shows how to update a cone position, orientation and size in order to probe the race car object:

    ![terrain-following-mesh-hover](/assets/images/vtk/hoverInfoConeState.jpg)

    Learn more by reading the [source code](https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-vehicle-geometry) or trying out the [Vehicle Geometry app](https://dash-gallery.plotly.host/dash-vehicle-geometry/).

    '''),

])
