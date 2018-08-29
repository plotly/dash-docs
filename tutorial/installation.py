# -*- coding: utf-8 -*-
import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html

import plotly
from textwrap import dedent as s

from tutorial import styles

layout = html.Div([

    dcc.Markdown('''
    # Dash Installation

    In your terminal, install several dash libraries.
    These libraries are under active development,
    so install and upgrade frequently.
    Python 2 and 3 are supported.'''.replace('    ', '')),

    dcc.SyntaxHighlighter('''pip install dash=={}  # The core dash backend
        pip install dash-html-components=={}  # HTML components
        pip install dash-core-components=={}  # Supercharged components
    '''.replace('    ', '').format(
        dash.__version__,
        html.__version__,
        dcc.__version__,
    ), customStyle=styles.code_container),

    html.Div([
        'Ready? Now, let\'s ',
        dcc.Link('make your first Dash app', href='/getting-started'),
        '.'
    ]),
    
    html.Hr(),
    
    dcc.Markdown(containerProps={'style': {'fontWeight': '10rem'}}, children=s('''
    > A quick note on checking your versions and on upgrading:
    > These docs are run using the versions listed above and these versions should be the _latest_ versions available. To check which version that you have installed, you can run e.g. 
    ```
    >>> import dash_core_components  # similarly `import dash`, `import dash_html_components`, etc
    >>> print(dash_core_components.__version__)
    ```
    > To see the latest changes of any package, check the GitHub repo's `CHANGELOG.md` file:
    > - `dash`: https://github.com/plotly/dash/blob/master/CHANGELOG.md
    > - `dash-core-components`: https://github.com/plotly/dash-core-components/blob/master/CHANGELOG.md
    > - `dash-html-components`: https://github.com/plotly/dash-html-components/blob/master/CHANGELOG.md
    > Finally, note that the `plotly` package and the `dash_renderer` package are important package dependencies that are installed automatically alongside `dash-core-components` and `dash` respectively. These docs are using `dash-renderer==0.12.0` and `plotly==3.1.1` and their changelogs are located here:
    > - `dash-renderer`: https://github.com/plotly/dash-renderer/blob/master/CHANGELOG.md
    > - `plotly`: https://github.com/plotly/plotly.py/blob/master/CHANGELOG.md 
    '''))

])
