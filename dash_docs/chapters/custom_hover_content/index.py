import dash_core_components as dcc
import dash_html_components as html

from dash_docs.tools import load_examples
from dash_docs import reusable_components as rc

examples = load_examples(__file__)

layout = html.Div([
    rc.Markdown('''
    # Custom Hover Content

    *New - released March 2021 with Dash X.X*

    When you hover over items, Plotly plots show customizable hover information.
    This built-in behavior is often enough, but sometimes you may wish to display
    more complicated information including Dash content like images, custom HTML,
    or even other plots. In this case, built-in Dash and Plotly.js features allow
    you to build and position your own hover boxes.

    ## A basic example

    The first example illustrates how to build custom hover boxes from Dash
    content. The basic mechanism is that we simply hide built-in Plotly hovers
    and replace them with carefully positioned HTML elements.

    To hide the hovers, we set both `'hoverinfo': 'skip'` and `'hovertemplate': None`.
    Setting `skip` hides visual display of hover content while still emitting
    hover events.

    The second step is to attach a Dash callback to `hoverData`. The example
    below shows the `hoverData` ouptut of `my-graph` connected to the `children`
    property of the HTML div, `my-hovers`.

    The final step is to construct and attach the HTML hover content. This step
    may experience the greatest amount of variation, depending on your needs.
    The example below constructs a single hover box for each hovered item,
    centered on the bounding box of each hovered item and opening either to the
    left or right, depending on the position on the plot.

    Positioning items with CSS can be complicated, but the bounding box
    coordinates returned by Plotly are carefully constructed to make this step
    as easy as possible. The bounding box is computed relative to the CSS
    [offset parent](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/offsetParent).
    What this means for us is that as long as the custom Dash hover content is
    a *sibling* of the graph element, other details like positioning, margins,
    or padding shouldn't matter.

    The bounding box properties returned are:

    - `offsetX0`: distance from the left to the left edge of the bounding box
    - `offsetX1`: distance from the left to the right edge of the bounding box
    - `offsetY0`: distance from the top to the top edge of the bounding box
    - `offsetY1`: distance from the top to the bottom edge of the bounding box

    Additional notes are that it's advisable to \`round\` all pixel coordinates
    to avoid fractional offsets, and that additional CSS properties like
    `pointer-events: none` may be used to prevent the hover box from capturing
    pointer events and remaining open while the mouse is within it.

    The example below illustrates using these properties to position the hover
    content.

    '''),

    rc.Syntax(examples['basic_hover.py'][0]),
    rc.Example(examples['basic_hover.py'][1]),

    rc.Markdown('''
    ## Adding a loading indicator

    While Dash is generating and returning the hover content, nothing is
    displayed on the screen. This may result a laggy and confusing UI. To
    resolve this, we may use a client-side callback to position a hover box
    with a loading indicator while Dash is generating the actual hover content.

    To accomplish this, we may use the `data-dash-is-loading` data attribute
    of the hover content which, in a fortunate turn of events, is `true` exactly
    while Dash is generating the content. Thus we add a single loading hover,
    position it using a client-side callback, and control its visibility with
    the following CSS:

    ```
    /* By default, hide the loader */
    .hover-loader {
        display: none;
    }

    /* Don't display hovers while server-side computation is taking place */
    [data-dash-is-loading=true] .hover {
        display: none;
    }

    /* Show a loader when the hover immediately preceeding it is loading */
    [data-dash-is-loading=true] + .hover-loader {
        display: block;
    }
    ```

    '''),

    rc.Syntax(examples['loading_indicator.py'][0]),
    rc.Example(examples['loading_indicator.py'][1]),


])
