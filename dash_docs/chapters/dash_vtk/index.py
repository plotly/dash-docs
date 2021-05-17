import dash_html_components as html
import dash_core_components as dcc
from dash_docs import reusable_components as rc

layout = html.Div([
    rc.Markdown('''
    # Dash VTK

    Dash VTK aims to integrate VTK/vtk.js visualization into the Dash framework.

    [VTK](https://vtk.org/) stands for _Visualization Toolkit_ and is a popular library written in C++ which is also available in Python for doing data processing and visualization in the scientific and medical fields. Typically VTK is used to visualize 3D geometries from simulations or sensors such as LIDAR scanner. For the medical world, VTK is used to render 3D images (i.e. CT, MRI, ...) by doing volume rendering and/or slicing.

    [Vtk.js](https://kitware.github.io/vtk-js/) on the other hand is a subset of VTK that focuses on the rendering aspect of it but in the JavaScript world. Vtk.js takes the same architecture and object decomposition as its big brother VTK/C++ but makes it friendly to use inside your browser.

    Dash VTK enables its users to use VTK on the server side for any data processing and provides the infrastructure to push the visualization to the client side for a better experience.
    Dash VTK does not require VTK but can seamlessly leverage it for looking at point clouds, a CFD simulation or anything 3D mesh or 3D images related.
    '''),

    rc.Section('User Guide', [])
])
