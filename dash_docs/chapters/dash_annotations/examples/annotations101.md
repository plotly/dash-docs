# Image annotations with Dash

This tutorial shows how to annotate images with different drawing tools in plotly figures, and how to use such annotations in Dash apps.

## Annotation tools in plotly figures

With the plotly graphing library, [it is possible to draw annotations on Cartesian axes](https://plotly.com/python/shapes/#drawing-shapes-on-cartesian-plots), which are recorded as shape elements of the figure layout. 

In order to use the drawing tools of a plotly figure, one must set its dragmode to one of the available drawing tools. This can be done programmatically, by setting the `dragmode` attribute of the figure `layout`, or by selecting a drawing tool in the modebar of the figure. Since buttons corresponding to drawing tools are not included in the default modebar, one must specify the buttons to add in the `config` prop of the `dcc.Graph` containing the plotly figure.

In the figure below, you can try to draw a rectangle by left-clicking and dragging, then you can try the other drawing buttons of the modebar.
