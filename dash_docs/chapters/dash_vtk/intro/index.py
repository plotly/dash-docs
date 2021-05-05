import dash_html_components as html
import dash_vtk

from dash_docs import tools
from dash_docs import styles
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)


layout = html.Div([

    rc.Markdown('''

    # 3D Visualization explained

    In VTK, we have 3 main types of objects that are key for understanding its visualization principals.
    First we have the __View__ which is just a container for any __Representation__ of __DataSource__ that you want to see.

    ## View

    The view is a 3D View that can do Geometry rendering for meshes or Volume rendering for 3D images.
    The view can be configured to act as a 2D one when using parallel projection and preventing rotation when interacting with it. The __View__ component can be configured with the following set of properties.

    ```python
    dash_vtk.View(
      id='vtk-view',
      background=[0, 0, 0],           # RGB array of floating point values between 0 and 1.
      interactorSettings=[...],       # Binding of mouse events to camera action (Rotate, Pan, Zoom...)
      cameraPosition=[x,y,z],         # Where the camera should be initially placed in 3D world
      cameraViewUp=[dx, dy, dz],      # Vector to use as your view up for your initial camera
      cameraParallelProjection=False, # Should we see our 3D work with perspective or flat with no depth perception
      triggerRender=0,                # Timestamp meant to trigger a render when different
      triggerResetCamera=0,           # Timestamp meant to trigger a reset camera when different
      # clickInfo,                    # Read-only property to retrieve picked representation id and picking information
      # hoverInfo                     # Read-only property to retrieve picked representation id and picking information
    )
    ```

    For the __interactorSettings__ we expect a list of mouse event type linked to an action. The example below is what is used as default:

    ```js
    interactorSettings=[
      {
        button: 1,
        action: 'Rotate',
      }, {
        button: 2,
        action: 'Pan',
      }, {
        button: 3,
        action: 'Zoom',
        scrollEnabled: true,
      }, {
        button: 1,
        action: 'Pan',
        shift: true,
      }, {
        button: 1,
        action: 'Zoom',
        alt: true,
      }, {
        button: 1,
        action: 'ZoomToMouse',
        control: true,
      }, {
        button: 1,
        action: 'Roll',
        alt: true,
        shift: true,
      }
    ]
    ```

    A mouse event can be identified with the following set of properties:
    - __button__: 1/2/3       # Which button should be down
    - __shift__: True/False   # Is the `Shift` key down
    - __alt__: True/False     # Is the `Alt` key down
    - __control__: True/False # Is the `Ctrl` key down
    - __scrollEnabled__: True/False # Some action could also be triggered by scroll
    - __dragEnabled__: True/False   # Mostly used to disable default drag behavior

    And the `action` could be one of the following:
    - __Pan__: Will pan the object on the plane normal to the camera
    - __Zoom__: Will zoom closer or further from the object based on the drag direction
    - __Roll__: Will rotate the object around the view direction
    - __ZoomToMouse__: Will zoom while keeping the location that was initially under the mouse at the same spot

    ## Representation

    A representation is responsible for converting a __DataSource__ into something visual that will be available inside the __View__.

    So far we are exposing to `dash_vtk` 3 core types of __Representation__:
    - __GeometryRepresentation__: The geometry representation will expect a mesh and will render it as geometry rendering (think triangle sets).
    - __VolumeRepresentation__: The volume representation will expect a 3D image and will render it using a Volume Rendering technique that will let you see through (foggy object).
    - __SliceRepresentation__: The slice representation will expect a 3D image and will slice it along a given axis.

    Representations should be put inside the children of a __View__.

    ## DataSource

    A __DataSource__ can be many things but it is mostly something that can produce data. In other words it could be a `dataset` or a `filter` that consume some data and generate new ones or even a `reader` that will read somekind of input (file, url...) and produce some data. Any __DataSource__ can be placed inside the children of another __DataSource__ that will act as a filter or simply passed to a __Representation__.

    In `dash_vtk` we have several objects that falls into that category. The list below gives you an overview of those but more details information can be found later.
    - __Algorithm__: Allows you to instantiate a vtk.js algorithm that could either be a filter (vtkWarpScalar) or a source (vtkLineSource, vtkConeSource, vtkPlaneSource, vtkSphereSource, vtkCylinderSource).
    - __ImageData__: What we've been calling a 3D image so far. This element will let you define each piece that comprises a 3D image.
    - __PolyData__: A surface mesh (points, triangles...). This element will let you define the various piece of a mesh.
    - __Reader__: Similar to an __Algorithm__ except that readers have a common API and this element lets you leverage those.
    - __ShareDataSet__: Allows you to capture any __DataSource__ and make it available in another processing pipeline or representation without duplicating the data that gets sent from the server to the client.
    - __Mesh__: Similar to __PolyData__ except that it has a Python helper function to help you map a __vtkDataSet__ into a single property of the __Mesh__.
    - __Volume__: Similar to __ImageData__ except that it has a Python helper function to help you map a __vtkImageData__ into a single property of the __Volume__.

    ## Geometry Rendering

    Now that we have those core concepts down we can show some examples of rendering a mesh using `dash-vtk`.

    '''),

    html.Details(open=False, children=[
        html.Summary('View full code'),      
        rc.Markdown(
            examples['t00_geometry_rendering.py'][0], 
            style=styles.code_container
        ),
    ]),

    html.Div(
        examples['t00_geometry_rendering.py'][1], 
        className='example-container'
    ),

    rc.Markdown('''
    ```python
    # Use helper to get a mesh structure that can be passed as-is to a Mesh
    from dash_vtk.utils import to_mesh_state
    mesh_state = to_mesh_state(dataset)

    content = dash_vtk.View([
        dash_vtk.GeometryRepresentation([
            dash_vtk.Mesh(state=mesh_state)
        ]),
    ])

    # Dash setup
    app = dash.Dash(__name__)
    server = app.server

    app.layout = html.Div(
        style={"width": "100%", "height": "calc(100vh - 15px)"},
        children=[content],
    )

    if __name__ == "__main__":
        app.run_server(debug=True)
    ```

    ## Volume Rendering

    The previous example was using a 3D image and extracting its mesh to render. Let's keep the same data but show it as Volume Rendering.

    '''),

    
    rc.Markdown(
        examples['t01_volume_rendering.py'][0], 
        style=styles.code_container
    ),

    html.Div(
        examples['t01_volume_rendering.py'][1], 
        className='example-container'
    ),


])
