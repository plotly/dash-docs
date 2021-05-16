import dash_html_components as html
import dash_vtk
from dash_docs import tools
from dash_docs import styles
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)

layout = html.Div([
    rc.Markdown(
    '''
    # Other Dash VTK Components

    ## Mesh

    This element is a helper on top of __PolyData__ which has a Python helper function that goes with it which will help you map a __vtkDataSet__ into a single property of the __Mesh__ element.

    ```py
    def Mesh(**kwargs):
        return dash_vtk.PolyData(
            **kwargs.get('state').get('mesh'),
            children=[
                dash_vtk.[kwargs.get('state').get('field').get('location')]([
                    dash_vtk.DataArray(
                      **kwargs.get('state').get('field'),
                    )
                ])
            ]
        )
    ```

Note that we assume that `state.field` exists when we use `kwargs.get('state').get('field').get('location')` in the snippet above. However, `state.field` is optional, so when it's not available the `children` is not created, and `kwargs.get('state').get('field').get('location')` would not be needed.

    The __Mesh__ element expects a single __state__ property that is internally split into 2 elements to represent the geometry and the field that you want to optionally attach to your mesh. The structure could be defined as follows:

    - __state__
      - mesh: (Contains the properties of __PolyData__)
        - points = []
        - verts = []
        - lines = []
        - polys = []
        - strips = []
        - connectivity = 'manual' # [manual, points, triangles, strips]
      - field: (Contains the properties of __DataArray__)
        - location: 'PointData' / 'CellData'
        - name: Name of the field (optional)
        - values: Array of values for the field
        - numberOfComponents: Number of components per point/cell
        - type: Name of TypedArray to use (Uint8Array, Int8Array, Float32Array, Float64Array...)

    ## Volume

    This element is a helper on top of __ImageData__ which has a Python helper function that goes with it which will help you map a __vtkImageData__ into a single property of the __Volume__ element.

    ```py
    def Volume(**kwargs):
        return dash_vtk.ImageData(
            **kwargs.get('state').get('image'),
            children=[
                dash_vtk.PointData([
                    dash_vtk.DataArray(
                      **kwargs.get('state').get('field'),
                    )
                ])
            ]
        )
    ```

    The __Volume__ element expects a single __state__ property that is internally split into 2 elements to represent the geometry and the field that you want to optionally attach to your mesh. The structure could be defined as follows:

    - __state__
      - image: (Contains the properties of __ImageData__)
        - dimensions
        - spacing
        - origin
      - field: (Contains the properties of __DataArray__)
        - values: Array of values for the field
        - numberOfComponents: Number of components per point/cell
        - type: Name of TypedArray to use (Uint8Array, Int8Array, Float32Array, Float64Array...)

    ## Algorithm

    This element allows you to create and configure a vtk.js class. This element expect only 2 properties:
    - __vtkClass__: The name of the vtkClass to instantiate.
    - __state__: The set of properties to apply on the given vtkClass.

    The current [list of classes](https://github.com/Kitware/react-vtk-js/blob/master/src/AvailableClasses.js#L4-L15) available to instantiate are:

    - __vtkClass__:
      - [vtkConcentricCylinderSource](https://kitware.github.io/vtk-js/api/Filters_Sources_ConcentricCylinderSource.html)
      - [vtkConeSource](https://kitware.github.io/vtk-js/api/Filters_Sources_ConeSource.html)
      - [vtkCubeSource](https://kitware.github.io/vtk-js/api/Filters_Sources_CubeSource.html)
      - [vtkCylinderSource](https://kitware.github.io/vtk-js/api/Filters_Sources_CylinderSource.html)
      - [vtkLineSource](https://kitware.github.io/vtk-js/api/Filters_Sources_LineSource.html)
      - [vtkPlaneSource](https://kitware.github.io/vtk-js/api/Filters_Sources_PlaneSource.html)
      - [vtkPointSource](https://kitware.github.io/vtk-js/api/Filters_Sources_PointSource.html)
      - [vtkSphereSource](https://kitware.github.io/vtk-js/api/Filters_Sources_SphereSource.html)
      - [vtkWarpScalar](https://kitware.github.io/vtk-js/api/Filters_General_WarpScalar.html)
    - __state__: See the references above for the properties available for each vtkClass.

    The following example uses a vtk source in vtk.js to generate a mesh
    
    '''),

    rc.Markdown(
        examples['t04_algorithm.py'][0], 
        style=styles.code_container
    ),

    html.Div(
        examples['t04_algorithm.py'][1], 
        className='example-container'
    ),


    rc.Markdown('''

    ## Reader

    This element is similar to the __Algorithm__ except that it focuses on vtk.js readers by allowing you to leverage their custom API.
    Like __Algorithm__, a reader expects a __vtkClass__ among those [listed below](https://github.com/Kitware/react-vtk-js/blob/master/src/AvailableClasses.js#L17-L24):

    - __vtkClass__
      - vtkPLYReader
      - vtkSTLReader
      - vtkElevationReader
      - vtkOBJReader
      - vtkPDBReader
      - vtkXMLImageDataReader
      - vtkXMLPolyDataReader

    Then use one of the properties below to feed the reader some data:
    - __url__: set of url to fetch data from (on the JS side)
    - __parseAsText__: set the text content to process
    - __parseAsArrayBuffer__: set binary data to process from base64 string

    Since the data loading is going to be asynchronous we've enabled some automatic callback to either trigger a _render_ or a _resetCamera_ once the data became available. To enable those callback, just set the following set of properties to your licking:
    - __renderOnUpdate__: True (default)
    - __resetCameraOnUpdate__: True (default)

    '''),

    rc.Markdown(
        examples['t05_reader.py'][0], 
        style=styles.code_container
    ),

    html.Div(
        examples['t05_reader.py'][1], 
        className='example-container'
    ),


    rc.Markdown('''

    ## ShareDataSet

    This element does not affect the dataset, but it allows the JavaScript side to reuse an existing __vtkDataSet__ for another __Representation__ or __filter__.

    The only property expected in a __ShareDataSet__ is a name to properly reference it elsewhere. By default a __name__ is provided so, in the case of only one _dataset_, you would not even need to specify this property.

    The following example shows how to create a view with one __Volume__ and four representations of it.
    
    '''),

    html.Details(open=False, children=[
        html.Summary('View full code'),      
        rc.Markdown(
            examples['t06_shared_dataset.py'][0], 
            style=styles.code_container
        ),
    ]),

    html.Div(
        examples['t06_shared_dataset.py'][1], 
        className='example-container'
    ),
])
