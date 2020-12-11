import inspect

import dash_html_components as html
import dash_core_components as dcc
from dash_docs import styles
from dash_docs import tools
from dash_docs import reusable_components as rc
import dash_slicer

try:
    from dash_slicer.docs import get_reference_docs
except ImportError:
    get_reference_docs = lambda: "TODO"  # while waiting for a new release


examples = tools.load_examples(__file__)


layout = html.Div([
    rc.Markdown(f'''

    # Introduction to Dash Slicer

    The ``dash_slicer`` library provides an easy way to visualize 3D image data
    by slicing along one dimension. Multiple views on the same data can be linked,
    to help with navigation.

    Install Dash Slicer with:

    ```pip install -U dash-slicer```

    The source is on GitHub at [plotly/dash-slicer](https://github.com/plotly/dash-slicer).

    ## Guide

    ### A first example

    Let's get started with a simple example.
    (The examples on this page are build with dash-slicer version {dash_slicer.__version__})
    '''),

    rc.Markdown(
        examples['slicer_example1.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['slicer_example1.py'][1], className='example-container'),

    rc.Markdown('''
    In the code above, we first load a 3D numpy array (a volumetric image). Then
    we instantiate a `VolumeSlicer` object with that data. This object is not
    a Dash component, but has attributes that are. Its `graph` and `slider`
    are placed in the layout, as well as a handful of `Store` objects that the
    slicer needs to function.

    If the server is run in debug mode, consider setting `dev_tools_props_check`
    to False, because it has a big impact on the performance.

    ### Multiple slicers

    In the next example, we create multiple slicers, one for each dimension,
    and put them in a layout, just like we did in the previous example.
    '''),

    rc.Markdown(
        examples['slicer_example2.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['slicer_example2.py'][1], className='example-container'),

    rc.Markdown('''
    You can see how the slicers are "linked"; each shows the positions
    of the other slicers. This linking is based on what we call the
    scene_id. This is a property that can be provided when you
    instantiate a `VolumeSlicer`. By default, the scene_id is derived
    from the volume. That's why the linking in this example works: each
    slicer is given the same numpy array object. By explicitly setting
    the scene_id, multiple views on different data can be linked as
    well.

    In addition to using the sliders, you can click in one of the
    views to make the other views go to the clicked location. Try it!
    Thanks to this navigation mode, you can optionally omit sliders in the layout when two or more views are present.

    ### Anisotropic data

    In the next example, we make the data non-isotropic. This means
    that the distance between voxels is not equal for all dimensions.
    The voxel-spacing can be provided via the `spacing` argument.
    Similarly, an `origin` can also be provided. You can zoom into the
    view on the right to see that the voxels are elongated.
    '''),

    rc.Markdown(
        examples['slicer_example3.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['slicer_example3.py'][1], className='example-container'),

    rc.Markdown('''

    ### Reacting to the slicer state

    This example illustrates how your application can react to the slicer's
    position and view by using the `state` store as an input. Note that the
    id of this store is a dict, which makes it possible to write a
    [pattern matching Input](https://dash.plotly.com/pattern-matching-callbacks)
    to collect the states of all slicers with a certain scene_id.
    See the reference docs for details.
    '''),

    rc.Markdown(
        examples['slicer_example4.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['slicer_example4.py'][1], className='example-container'),

    rc.Markdown('''

    ### More examples

    More examples are available at the
    [dash-slicer repository](https://github.com/plotly/dash-slicer/tree/main/examples).
    '''),


    html.H2('Reference'),
    rc.Markdown(get_reference_docs()),
])
