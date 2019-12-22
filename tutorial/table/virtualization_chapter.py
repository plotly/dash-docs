import dash_html_components as html

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

from tutorial import tools
from tutorial import styles


examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in ['virtualization.py']
}

layout = html.Div(
    [
        dcc.Markdown(dedent(
        """
        # Virtualization

        In addition to pagination, `DataTable` also has virtualization capabilities
        for viewing large datasets. Virtualization saves browser resources while
        still permitting the user to scroll through the entire dataset. It achieves this
        by only a rendering a subset of the data at any instant.

        The virtualiztion backend makes a few assumptions about the style of
        your `DataTable` which must be adhered to in order to ensure that the
        table scrolls smoothly.

        - the width of the columns is fixed
        - the height of the rows is always the same
        - runtime styling changes will not affect width and height compared to
        the table's first rendering

        The example below prevents runtime style changes by fixing the column
        widths and setting the white-space CSS property in the cells to normal.
        """
            )
        ),

        dcc.Markdown(
            examples['virtualization.py'][0],
            style=styles.code_container
        ),

        html.Div(
            examples['virtualization.py'][1],
            className='example-container'
        ),

    ]
)
