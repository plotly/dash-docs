# -*- coding: utf-8 -*-
import dash
import dash_html_components as html

from dash_docs import styles, tools
from dash_docs import reusable_components as rc

layout = html.Div([

    rc.Markdown("""
    # Dash Installation

    In your terminal, install `dash`.
    """),

    rc.Markdown("""
    ```shell
    pip install dash
    ```
    """, style=styles.code_container),

    html.Br(),

    rc.Markdown("""
    This brings along three component libraries
    that make up the core of Dash: `dash_html_components`, `dash_core_components`,
    `dash_table`, as well as the `plotly` graphing library. These libraries are
    under active development, so install and upgrade frequently.
    
    If you prefer [Jupyter notebook](https://plotly.com/dash/workspaces/?tab=jupyter-notebooks) 
    or JupyterLab as your development environment, we recommend installing [jupyter-dash](https://github.com/plotly/jupyter-dash):
    """),

    rc.Markdown("""
    ```shell
    pip install jupyter-dash
    ```
    """, style=styles.code_container),

    html.Br(),    
    
    rc.Markdown("""
    These docs are running `dash` version `{}`.
    Python 2 and 3 are supported.

    We also recommend installing [Pandas](https://pandas.pydata.org/), which is
    required by [Plotly Express](https://plotly.com/python/plotly-express/) and
    used in many of our examples.
    """.format(dash.__version__)),

    rc.Markdown("""
    ```shell
    pip install pandas
    ```
    """, style=styles.code_container),

    rc.Markdown("Ready? Now, let's [make your first Dash app](/layout)."),

    rc.WorkspaceBlurb if not tools.is_in_dash_enterprise() else "",
])
