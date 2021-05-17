import dash_html_components as html
import dash_vtk
from dash_docs import tools
from dash_docs import styles
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)

layout = html.Div([
    rc.Markdown('''
    # Structure of Datasets

    In vtk.js because we mostly focus on Rendering we only have 2 types of data structures. We have a `vtkPolyData` that can be used for geometry rendering and a `vtkImageData` that can be used for volume rendering. In proper VTK, we have more types of DataSets and we have several filters that help you convert from one type to another.

    Here we explain some of the foundation of those data structures so you could create them by hand if you wanted to.

    ## ImageData

    An ImageData is an implicit grid that is axis aligned as shown in the picture below.

    ![ImageData](/assets/images/vtk/imagedata.jpg)

    The set of properties that can be given to `ImageData` are as follow:
    - __origin__: location of the bottom left corner of the grid in the 3D world
    - __dimensions__: how many points we have along each axis
    - __spacing__: what is the uniform spacing along each axis between the points

    A concrete example would be a grid of 5 points or 4 cells along each axis which will go from `[-2, 2]` along each axis.

    
    ```py
    dash_vtk.ImageData(
      dimension=[5,5,5],
      origin=[-2,-2,-2],
      spacing=[1,1,1],
    )
    ```
    
    '''),

    html.Details(open=False, children=[
        html.Summary('View full code'),      
        rc.Markdown(
            examples['t02_imagedata.py'][0], 
            style=styles.code_container
        ),
    ]),

    html.Div(
        examples['t02_imagedata.py'][1], 
        className='example-container'
    ),

    rc.Markdown('''

    ## PolyData

    A PolyData is a surface mesh composed of `points` and `cells`. The cells can be:
    - __verts__: Vertex or point to show as a tiny square on the screen
    - __lines__: Lines that connect points into a one segment or multi segment line
    - __polys__: Polygons which are convex surfaces such as triangles, rectangles, circles...
    - __strips__: Triangle strips efficiently combine triangles together with no repeated points just for connectivity

    The way cells are defined is via an index-based array that maps to a given point index. For example let's pretend you want to create a line with 2 segments, you will need at least 3 points defined in the `points` array. If those points are defined first in your `points` array, then the `lines` array should be filled as follows:

    ```py
    nb_points = 3
    lines = [nb_points, 0, 1, 2]
    ```

    To create 2 lines independent of each other, you can do it as follows:

    ```py
    lines = [
      3, 0, 1, 2,        # First line of 2 segments / 3 points
      2, 3, 4,           # Second line of 1 segment / 2 points
      4, 10, 11, 12, 14  # Third line of 3 segments / 4 points
    ]
    ```

    You can see a concrete example in the image below

    
    ![PolyData](/assets/images/vtk/polydata.jpg)

    '''),

    html.Details(open=False, children=[
        html.Summary('View full code'),      
        rc.Markdown(
            examples['t03_polydata.py'][0], 
            style=styles.code_container
        ),
    ]),

    html.Div(
        examples['t03_polydata.py'][1], 
        className='example-container'
    ),

    rc.Markdown('''

    The `dash_vtk.PolyData` element has an additional property to automatically generate cells based on some assumption of the order of the points defined in the `points` array. That property is named __connectivity__ and defaults to `manual`, meaning no automatic action is taken. But that property can be set to `points` to automatically set the vertex to actually see the points provided or `triangles` which uses each set of 3 consecutive points to create a triangle and finally `strips` which consumes all the points in a single strip of triangles.

    ## Fields

    Having a grid is a good start, but most likely you would want to attach a field to a given mesh so you can start looking at it in a 3D context.

    Fields are arrays that map to either __Points__ or __Cells__. They could be scalars or vectors of different size.

    The diagram below tries to explain the difference between fields located on points vs cells in term of rendering, but it also truly has a different meaning based on the type of data that you have.

    ![Fields](/assets/images/vtk/fields.jpg)

    The example below shows how to attach fields to a dataset (PolyData and/or ImageData).

    Caution: By convention, we always attach data to points in an ImageData for doing VolumeRendering and the array must be registered as scalars.

    [ImageData code](./tutorials/t02_imagedata.py) | [PolyData code](./tutorials/t03_polydata.py)
    ```py
    dash_vtk.ImageData(
      dimensions=[5,5,5],
      origin=[-2,-2,-2],
      spacing=[1,1,1],
      children=[
        dash_vtk.PointData([
          dash_vtk.DataArray(
            registration="setScalars",
            values=range(5*5*5),
          )
        ])
      ],
    )

    dash_vtk.PolyData(
      points=[
        0,0,0,
        1,0,0,
        0,1,0,
        1,1,0,
      ],
      lines=[3, 1, 3, 2],
      polys=[3, 0, 1, 2],
      children=[
        dash_vtk.PointData([
          dash_vtk.DataArray(
            name='onPoints',
            values=[0, 0.33, 0.66, 1],
          )
        ]),
        dash_vtk.CellData([
          dash_vtk.DataArray(
            name='onCells',
            values=[0, 1],
          )
        ])
      ],
    )
    ```
    '''),
])
