import dash_html_components as html
import dash_vtk
from dash_docs import reusable_components as rc

components = [
    "Algorithm",
    "Calculator",
    "CellData",
    "DataArray",
    "FieldData",
    "GeometryRepresentation",
    "ImageData",
    "Mesh",
    "PointCloudRepresentation",
    "PointData",
    "PolyData",
    "Reader",
    "ShareDataSet",
    "SliceRepresentation",
    "View",
    "Volume",
    "VolumeController",
    "VolumeDataRepresentation",
    "VolumeRepresentation"
]

sections = [html.H1("Dash VTK Reference")]

for component in components:
    sections.extend([
        html.H2(component),
        rc.ComponentReference(component, dash_vtk)
    ])


layout = html.Div(sections)
