For a path, we need the following steps
- we retrieve the coordinates of the vertices of the path from the SVG path
- we use the function `skimage.draw.polygon` to obtain the coordinates of pixels covered by the path
- then we use the function `scipy.ndimage.binary_fill_holes` in order to set to `True` the pixels enclosed by the path.

