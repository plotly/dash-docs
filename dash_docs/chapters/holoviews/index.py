# -*- coding: utf-8 -*-
import dash_html_components as html

from dash_docs import styles
from dash_docs.tools import load_examples
from dash_docs import reusable_components as rc

examples = load_examples(__file__)

layout = html.Div([

    rc.Markdown('''
    # HoloViews Overview
    
    HoloViews is an ambitious project that aims to provide a flexible grammar of
    visualization types and plot interactions. HoloViews specifications can be
    displayed using a variety of technologies, including Plotly.js and Dash.
    
    While HoloViews can be used to create a large variety of visualizations, for Dash
    users it is particularly helpful for two use cases: Automatically linking selections 
    across multiple figures and displaying large data sets using Datashader.
    
    HoloViews also provides a uniform interface to a variety of data structures, 
    making it easy to start out by visualizing small pandas DataFrames and then scale
    up to GPU accelerated RAPIDS cudf DataFrames, or larger than memory Dask DataFrames.
    
    For more background information, see the main HoloViews documentation at 
    https://holoviews.org/  

    ## HoloViews Elements and Containers
    
    The visualization primitives in HoloViews are called elements. Elements
    in HoloViews are analogous to Plotly traces, and there are specific elements for
    [`Scatter`](http://holoviews.org/reference/elements/plotly/Scatter.html#elements-plotly-gallery-scatter),
    [`Area`](http://holoviews.org/reference/elements/plotly/Area.html#elements-plotly-gallery-area),
    [`Bars`](http://holoviews.org/reference/elements/plotly/Bars.html#elements-plotly-gallery-bars),
    [`Histogram`](http://holoviews.org/reference/elements/plotly/Histogram.html#elements-plotly-gallery-histogram),
    [`Heatmap`](http://holoviews.org/reference/elements/plotly/HeatMap.html#elements-plotly-gallery-heatmap),
    etc.
    
    Elements can be grouped together into various containers including the
    [`Overlay`](http://holoviews.org/reference/containers/plotly/Overlay.html#containers-plotly-gallery-overlay)
    container for overlaying multiple compatible elements on the same axes, and the
    [`Layout`](http://holoviews.org/reference/containers/plotly/Layout.html#containers-plotly-gallery-layout)
    container for displaying multiple elements side by side as separate subplots.
    Additionally, HoloViews supports several more advanced "Dimensioned" containers 
    to aid in the visualization of multi-dimensional datasets including the
    [`HoloMap`](http://holoviews.org/reference/containers/plotly/HoloMap.html#containers-plotly-gallery-holomap),
    [`Gridspace`](http://holoviews.org/reference/containers/plotly/GridSpace.html#containers-plotly-gallery-gridspace),
    [`NdLayout`](http://holoviews.org/reference/containers/plotly/NdLayout.html#containers-plotly-gallery-ndlayout),
    and 
    [`Ndoverlay`](http://holoviews.org/reference/containers/plotly/NdOverlay.html#containers-plotly-gallery-ndoverlay)
    containers.
    
    Finally, the
    [`DynamicMap`](https://holoviews.org/reference/containers/plotly/DynamicMap.html#containers-plotly-gallery-dynamicmap)
    is a special container than produces elements dynamically, often
    in response to user interaction events. This documentation page does not discuss
    the creation of general `DynamicMap` instances, but it's helpful to understand
    that the `datashade` and `link_selections` transformations discussed below both 
    produce either `DynamicMap` instances, or containers of `DynamicMap` instances.
    
    ## HoloViews Datasets
    
    While it's possible to build HoloViews elements directly from external data 
    structures like numpy arrays and pandas DataFrames, HoloViews also provides a 
    `Dataset` class that aims to serve as a universal interface to these data 
    structures. The recommended workflow is to first wrap the original data structure 
    (e.g. the pandas DataFrame) in a `Dataset` instance, and then construct 
    elements using this `Dataset`.
    
    This workflow has two main advantages:
    
    1. It makes it easy to swap out data structures in the future. For example, you
       could develop a visualization using a small pandas DataFrame and then later
       switch to a GPU accelerated cuDF DataFrame or a larger-than-memory dask 
       DataFrame.
    
     2. It allows HoloViews to associate each visualization element with all of the 
       dimensions (i.e. columns in the case of a DataFrame) in the original `Dataset`.
       This is what makes it possible for HoloViews to automate the process of
       linking selections across visualizations that do not all display the same 
       dimensions. See the following sections for some examples of using the 
       `link_selections` function to accomplish this.
    
    The examples in this documentation page use `Dataset` instances that wrap tabular
    data structures. But Datasets also support wrapping gridded datasets like numpy 
    [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)
    and xarray 
    [`DataArray`](http://xarray.pydata.org/en/stable/generated/xarray.DataArray.html) 
    objects. See the
    [Tabular Datasets](http://holoviews.org/user_guide/Tabular_Datasets.html)
    documentation page for more information on wrapping tabular data structures, and
    see the 
    [Gridded Datasets](http://holoviews.org/user_guide/Gridded_Datasets.html)
    documentation page for more information on wrapping gridded data structures. 
     
    ## Building Dash Components from HoloViews Objects
    
    HoloViews elements and containers can be converted into Dash components using the
    `holoviews.plotting.plotly.dash.to_dash` function. This function inputs
    a `dash.Dash` app instance and a list of HoloViews objects, and returns a 
    `namedtuple` with the following properties.
    
    - `graphs`: This is a list of converted `Graph` components with the same 
        length as the input list of HoloViews objects. By default, these will have 
        type `dash_core_components.Graph`, but an alternative graph component class
        (e.g. `dash_design_kit.Graph`) can be specified using the `graph_class`
        argument to the `to_dash` function. 
    - `resets`: If the `reset_button=True` argument is passed to 
        `to_dash`, the `resets` property will hold a length 1 list
        containing a Dash component that represents a reset button. When clicked,
        this button will reset the graphs to their initial state. This will reset
        both the figure viewports and other interactive states like the active
        selection produced by the `link_selection` examples below. If 
        `reset_button=False`, the default, then this list will be empty.
    - `store`: A Dash [`Store`](/dash-core-components/store) component that is used
        internally to maintain the joint interactive state of all of the converted 
        Dash components.  
    - `kdims`: For Dimensioned HoloViews containers, the `kdims`
        property holds a dictionary from key-dimension names to Dash components
        that represent sliders for each key dimension. Dimensioned Containers are
        not discussed further here; see the
        [Dimensioned Containers](http://holoviews.org/user_guide/Dimensioned_Containers.html)
        section in the HoloViews documentation for more information.
    - `children`: This is a list that contains all of the components above. This can
        be assigned directly to the `children` property of an `html.Div` component if
        no additional layout structure is needed.

    After calling `to_dash`, each of the resulting components must be 
    included somewhere in the app's layout. This can be done by *either*:
      - including the `children` list as the `children` property of an `html.Div` 
      component.
      - including all of the components stored in `graphs`, `resets`, `kdims`, and
      `store` somewhere in the app's layout.
    
    ## Display Simple HoloViews Elements with Dash
    
    This example loads the iris dataset included in plotly.py and wraps it in a 
    HoloViews `Dataset`. This `Dataset` is then used to construct a
    [`Scatter`](http://holoviews.org/reference/elements/plotly/Scatter.html#elements-plotly-gallery-scatter)
    element and a
    [`Histogram`](http://holoviews.org/reference/elements/plotly/Histogram.html#elements-plotly-gallery-histogram)
    element.  The `Histogram` element is created using the 
    [`histogram`](http://holoviews.org/Reference_Manual/holoviews.operation.html#holoviews.operation.histogram)
    operation which is what executes the histogram binning algorithm. 
     
    These two elements are converted into two Dash `Graph` components using the
    `to_dash` function, and are placed into a `Div` component along with the
    associated `Store` component.
    '''),
    rc.Markdown(
        examples['holoviews-scatter.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['holoviews-scatter.py'][1], className="example-container"),
    rc.Markdown('''
    ## Styling Figures Produced by HoloViews
    
    There are two general approaches that can be used to customize the appearance
    of the Plotly figures produced by HoloViews.
    
    ### Options System
    The first is the HoloViews options system. This approach uses the syntax:
    
    ```python
    element.opts(option1=value1, option2=value2)
    ```
    
    This is very analogous to the `fig.update()` syntax that is used to update Plotly
    `plotly.graph_object.Figure` objects. The available options for a particular
    element type can be discovered from a Python or IPython REPL using the
    `holoviews.help` function. For example:
    
    ```python
    import holoviews as hv
    hv.extension("plotly")
    hv.help(hv.Scatter)
    ```
    
    A slightly different syntax is used to style elements inside a container. Here is
    an example of how `Scatter` element options would be applied to a container that
    contains or produces `Scatter` elements: 
    
    ```python
    from holoviews import opts
    container.opts(opts.Scatter(option1=value1, option2=value2))
    ``` 
    
    This makes it possible to target options to elements of specific types within
    a container. This is the approach that must be used to apply options to the
    `DynamicMap` instances produced by the `datashade` and `link_selections`
    transformations discussed below.
    
    The example below customizes the appearance of a `Scatter` element using the 
    `size` and `color` options. 
    
    See the
    [Applying Customizations](http://holoviews.org/user_guide/Applying_Customizations.html)
    section of the HoloViews documentation for more information on styling figures
    usng the options system.
    
    ### Plot Hooks
    HoloViews aims to expose the most common plot options through the `opts` syntax
    above, but the coverage of possible plotly configuration options is not exhaustive.
    HoloViews provides a system called "plot hooks" to make it possible to apply arbitrary 
    figure customizations.  Every element has a special option named `hooks` that may
    be set to a list of functions that should be applied to the figure that HoloViews
    generates before it is displayed.
    
    The example below uses a plot hook to change the default drag tool from
    `zoom` to `pan`. 
    
    See the
    [Plot hooks](http://holoviews.org/user_guide/Customizing_Plots.html#Plot-hooks)
    section in the HoloViews documentation for more information.    
    '''),
    rc.Markdown(
        examples['holoviews-scatter-styled.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['holoviews-scatter-styled.py'][1], className="example-container"),
    rc.Markdown('''
    ## Linked Selections with HoloViews
    
    One HoloViews feature that is particularly convenient for Dash users is the ability
    to automatically link selections across figures without the need to manually define
    any callback functions.
    
    This can be done by first creating a `link_selections` instance
    (called `selection_linker` in the examples below) using the
    `link_selections.instance()` method, and then calling this object as a function
    with the elements or containers to be linked.
 
    When these linked elements are passed to the `to_dash` function, Dash
    callbacks to achieve this interactive linking behavior are automatically generated
    and registered with the provided `dash.Dash` app instance.
    
    This example shows how the `reset_button=True` argument to `to_dash` can
    be used to create a Dash button component. When this button is clicked, the plot
    viewport and selection states are reset to their original values. 
     
    For more background on linked selections in Holoviews, see the
    [Linked Brushing](http://holoviews.org/user_guide/Linked_Brushing.html)
    documentation section.
    
    Try using the box-selection tool to select regions of space in each figure and
    notice how the selection of the corresponding data is displayed in both figures.
    Note that only box selection is supported right now. Lasso selection support
    is not yet implemented.    
    '''),
    rc.Markdown(
        examples['link-selections.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['link-selections.py'][1], className="example-container"),
    rc.Markdown('''
    ## Visualizing a Large Datasets with Datashader
    Another HoloViews feature that is particularly convenient for Dash users is the
    integration with [Datashader](https://datashader.org/).
    
    Datashader is a Python library for quickly creating a variety of principled
    visualizations of large datasets.
     
    While the Plotly `scattergl` trace can handle hundreds of thousands of points, 
    Datashader can handle tens to hundreds of millions. The difference is that rather
    than passing the entire dataset from the Python server to the browser for rendering,
    Datashader rasterizes the dataset to a heatmap or image, and only this heatmap or
    image is transferred to the browser for rendering.
    
    To effectively use Datashader in an interactive context, it's necessary to rerender
    the dataset each time the figure viewport changes. This can be accomplished in 
    Dash by installing a callback function that listens for changes to the
    `relayoutData` prop.  Because of how HoloViews packages data lazily (without 
    rendering it immediately), replaying this pipeline of transformations can be 
    accomplished without manually defining any callbacks, making Datashader much easier 
    to use than if invoked without HoloViews.

    This example loads the iris dataset included in plotly.py and then duplicates
    it many times with added noise to generate a DataFrame with 1.5 million rows.
    This large pandas DataFrame is wrapped in a HoloViews `Dataset` and then used to
    construct a `Scatter` element.
    
    The `datashade` operation is used to transform the `Scatter` element into
    a datashaded scatter element that automatically updates in response to zoom / pan
    events. The `to_dash` function is then used to build a single Dash
    `Graph` component and a reset button.
    
    Try zooming and panning on this figure and notice how the datashaded image is
    automatically updated. The reset button can be used to reset to the initial figure
    viewport.
    
    For more information on using datashader through HoloViews, see the
    [Large Data](http://holoviews.org/user_guide/Large_Data.html) section of the
    HoloViews documentation.
    '''),
    rc.Markdown(
        examples['datashader.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['datashader.py'][1], className="example-container"),
    rc.Markdown('''
    ## Combining Datashader and Linked Selections
    
    This examples shows how the two previous examples can be combined to support
    linking selections across a histogram and a datashaded scatter plot of 1.5 million
    points.

    Try using the box-selection tool to select regions of space in each figure and
    notice how the selection of the corresponding data is displayed in both figures.
    Also, try zooming and panning on datashaded scatter figure and notice how the
    datashaded image is automatically updated. The reset button can be used to reset 
    to the initial figure viewport and clear the current selection.
    '''),
    rc.Markdown(
        examples['datashader-link-selections.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['datashader-link-selections.py'][1], className="example-container"),
    rc.Markdown('''
    ## Map Overlay
    Most 2-dimensional HoloViews elements can be displayed on top of a map by
    overlaying them on top of a `Tiles` element.  There are three approaches to 
    configuring the map that is displayed by a `Tiles` element:
    
      1. Construct a `holoviews.Tiles` element with a WMTS tile server url.
         E.g. `Tiles("https://maps.wikimedia.org/osm-intl/{Z}/{X}/{Y}@2x.png")`
      2. Construct a `Tiles` element with a predefined tile server url using a
         function from the `holoviews.element.tiles.tile_sources` module. E.g. `CartoDark()`
      3. Construct a `holoviews.Tiles` element with an empty string, then use `.opts`
         to supply a mapbox token and style.
         E.g. `Tiles("").opts(mapboxstyle="light", accesstoken="pk...")`
    
    > **Coordinate Systems:**  Unlike the native plotly mapbox traces which accept
      geographic positions in longitude and latitude coordinates, HoloViews expects
      geographic positions to be supplied in Web Mercator coordinates 
      (https://epsg.io/3857).  Rather than "longitude" and "latitude", horizontal and
      vertical coordinates in Web Mercator are commonly called "easting" and "northing"
      respectively. HoloViews provides `Tiles.lon_lat_to_easting_northing` and 
      `Tiles.easting_northing_to_lon_lat` for converting between coordinate systems.
    
    This example displays a scatter plot of the `plotly.data.carshare` dataset on top
    of the predefined `StamenTerrain` WMTS map.
    '''),
    rc.Markdown(
        examples['mapbox-points.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['mapbox-points.py'][1],
             className="example-container"),
    rc.Markdown('''
    ## Visualizing a Large Geographic Datasets with Datashader
    This example demonstrates how to use datashader to display a large geographic
    scatter plot on top of a vector tiled Mapbox map. A large dataset is synthesized
    by repeating the carshare dataset and adding Gaussian noise to the positional
    coordinates.
    
    Using mapbox maps requires a free mapbox account and an associated access token.
    
    > This example assumes the mapbox access token is stored in a local file named
      `.mapbox_token`. To run this example yourself, either create a file with this name
      in your working directory that contains your token, or assign the `mapbox_token`
      variable to a string containing your token.
    '''),
    rc.Markdown(
        examples['mapbox-datashader.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['mapbox-datashader.py'][1],
             className="example-container"),
    rc.Markdown('''
    ## Mapbox datashader and linked selections
    This example demonstrates how the `link_selections` transformation described above
    can be used with geographic scatter plots.  Here, the scatter plot is also
    datashaded, but `link_selections` will work with plain `Scatter` elements
    as well. 
    '''),
    rc.Markdown(
        examples['mapbox-linked-datashader.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['mapbox-linked-datashader.py'][1],
             className="example-container"),
    rc.Markdown('''
    ### GPU Accelerating Datashader and Linked Selections with RAPIDS

    Many HoloViews operations, including `datashade` and `link_selections`, can be
    accelerated on modern NVIDIA GPUs using technologies from the
    [RAPIDS](https://developer.nvidia.com/rapids)
    ecosystem. All of the previous examples can be GPU accelerated simply by
    replacing the pandas DataFrame passed to the `Dataset` constructor with a
    [`cuDF`](https://github.com/rapidsai/cudf) DataFrame.
    '''),
    html.A(href="https://developer.nvidia.com/rapids", children=[
        html.Img(
            src="/assets/images/integration/RAPIDS-logo-white.svg",
            style={
                "display": "block",
                "width": "70%",
                "margin-left": "auto",
                "margin-right": "auto",
                "margin-bottom": "0.75em",
            }
        )
    ]),
    rc.Markdown('''
    The `cudf.from_pandas` function can be used to construct a cuDF DataFrame from a
    pandas DataFrame. So adding GPU acceleration to each of the prior examples can be
    done simply by replacing the `dataset = hv.Dataset(df)` statements with:

    ```python
    import cudf
    dataset = hv.Dataset(cudf.from_pandas(df))
    ```

    '''),
    rc.Markdown('''
    ## Advanced HoloViews
    While motivated by Datashader and linked selections use cases, the
    `to_dash` transformation supports arbitrary HoloViews objects and has
    full support for the elements and stream types supported by the HoloViews Plotly
    backend.

    To demonstrate this, here are Dash ports of some of the interactive Plotly examples
    from the HoloViews documentation.
    '''),
    rc.Markdown('''
    ### Bounds & selection stream example
    Based on
    https://holoviews.org/reference/streams/plotly/Bounds.html#streams-plotly-gallery-bounds

    > A linked streams example demonstrating how to use Bounds and Selection
    streams together.
    '''),
    rc.Markdown(
        examples['bounds-stream.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['bounds-stream.py'][1], className="example-container"),
    rc.Markdown('''
    ### BoundsX stream example
    Based on
    https://holoviews.org/reference/streams/plotly/BoundsX.html#streams-plotly-gallery-boundsx

    > A linked streams example demonstrating how to use BoundsX streams.
    '''),
    rc.Markdown(
        examples['boundsx-stream.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['boundsx-stream.py'][1], className="example-container"),
    rc.Markdown('''
    ### BoundsY stream example
    Based on
    https://holoviews.org/reference/streams/plotly/BoundsY.html#streams-plotly-gallery-boundsy

    > A linked streams example demonstrating how to use BoundsY streams.
    '''),
    rc.Markdown(
        examples['boundsy-stream.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['boundsy-stream.py'][1], className="example-container"),
    rc.Markdown('''
    ### RangeXY stream example
    Based on
    https://holoviews.org/reference/streams/plotly/RangeXY.html#streams-plotly-gallery-rangexy

    > A linked streams example demonstrating how to use multiple Selection1D
    streams on separate Points objects.
    '''),
    rc.Markdown(
        examples['rangexy-stream.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['rangexy-stream.py'][1], className="example-container"),
    rc.Markdown('''
    ### Multiple selection streams example
    Based on
    https://holoviews.org/reference/streams/plotly/Selection1D_paired.html#streams-plotly-gallery-selection1d-paired

    > A linked streams example demonstrating how to use multiple Selection1D streams
    on separate Points objects.
    '''),
    rc.Markdown(
        examples['selection1d-paired-stream.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['selection1d-paired-stream.py'][1], className="example-container"),
    rc.Markdown('''
    ### Point Selection1D stream example
    Based on
    https://holoviews.org/reference/streams/plotly/Selection1D_points.html#streams-plotly-gallery-selection1d-points

    > A linked streams example demonstrating how to use Selection1D to get
    currently selected points and dynamically compute statistics of selection.
    '''),
    rc.Markdown(
        examples['selection1d-points-stream.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['selection1d-points-stream.py'][1],className="example-container"),
    rc.Markdown('''
    ### DynamicMap Container
    Based on
    https://holoviews.org/reference/containers/plotly/DynamicMap.html#containers-plotly-gallery-dynamicmap

    > A DynamicMap is an explorable multi-dimensional wrapper around a callable
    that returns HoloViews objects.
    '''),
    rc.Markdown(
        examples['dynamic-map.py'][0],
        style=styles.code_container
    ),
    html.Div(examples['dynamic-map.py'][1], className="example-container"),
])
