import dash_html_components as html
import dash_vtk
from dash_docs import reusable_components as rc


layout = html.Div([
    rc.Markdown('''
    # Advanced Demos

    __dash_vtk__ provides several advanced examples that should re-enforce what has been described so far.

    We've converted several examples from [PyVista](https://docs.pyvista.org/) to show you how to enable rendering on the client side using __dash_vtk__.

    Then we made several examples using plain VTK for both a CFD example and some medical ones.

    ## Point Cloud creation

    [dash_vtk](https://github.com/plotly/dash-vtk/blob/master/demos/pyvista-point-cloud/app.py) | [PyVista](https://docs.pyvista.org/examples/00-load/create-point-cloud.html)

    ![Preview](/assets/images/vtk/pyvista-point-cloud.jpg)

    ## Terrain following mesh

    [dash_vtk](https://github.com/plotly/dash-vtk/blob/master/demos/pyvista-terrain-following-mesh/app.py) | [PyVista](https://docs.pyvista.org/examples/00-load/terrain-mesh.html)
    ![Preview](/assets/images/vtk/pyvista-terrain-following-mesh.jpg)

    ## VTK dynamic streamlines example

    This example leverages plain VTK on the server side while providing UI controls in __dash__ and leverages __dash_vtk__ to enable local rendering of dynamically computed streamlines inside a wind tunnel.

    [dash_vtk](https://github.com/plotly/dash-vtk/blob/master/demos/usage-vtk-cfd/app.py)

    ![CFD Preview](/assets/images/vtk/usage-vtk-cfd.jpg)

    ## Medical examples

    [Real medical image](https://github.com/plotly/dash-vtk/blob/master/demos/volume-rendering/app.py)

    ![Real medical image](/assets/images/vtk/volume-rendering.jpg)


    [Randomly generated volume](https://github.com/plotly/dash-vtk/blob/master/demos/synthetic-volume-rendering/app.py)

    ![Randomly generated volume](/assets/images/vtk/synthetic-volume-rendering.jpg)

    [Multi-View with slicing](https://github.com/plotly/dash-vtk/blob/master/demos/slice-rendering/app.py)

    ![Multi-View with slicing](/assets/images/vtk/slice-rendering.jpg)

    ''')
])
