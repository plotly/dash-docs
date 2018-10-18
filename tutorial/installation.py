# -*- coding: utf-8 -*-
import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html
import dash_table

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
        pip install dash-table=={}  # Interactive table component (new!)
    '''.replace('    ', '').format(
        dash.__version__,
        html.__version__,
        dcc.__version__,
        dash_table.__version__
    ), customStyle=styles.code_container),

    html.Div([
        'Ready? Now, let\'s ',
        dcc.Link('make your first Dash app', href='/getting-started'),
        '.'
    ]),

    html.Hr(),

    dcc.Markdown(s('''
    > A quick note on checking your versions and on upgrading.
    > These docs are run using the versions listed above and these
    > versions should be the latest versions available.
    > To check which version that you have installed, you can run e.g.
    > ```
    > >>> import dash_core_components
    > >>> print(dash_core_components.__version__)
    > ```
    > To see the latest changes of any package, check the GitHub repo's CHANGELOG.md file:
    > - [dash changelog](https://github.com/plotly/dash/blob/master/CHANGELOG.md)
    > - [dash-core-components changelog](https://github.com/plotly/dash-core-components/blob/master/CHANGELOG.md)
    > - [dash-html-components changelog](https://github.com/plotly/dash-html-components/blob/master/CHANGELOG.md)
    > - [dash-table changelog](https://github.com/plotly/dash-table/blob/master/CHANGELOG.md)
    >
    > Finally, note that the plotly package and the dash-renderer package are
    > important package dependencies that are installed automatically
    > with dash-core-components and dash respectively.
    > These docs are using dash-renderer=={} and plotly=={}
    > and their changelogs are located here:
    > - [dash-renderer changelog](https://github.com/plotly/dash-renderer/blob/master/CHANGELOG.md)
    > - [plotly changelog](https://github.com/plotly/plotly.py/blob/master/CHANGELOG.md)
    >
    > All of these packages adhere to [semver](https://semver.org/).
    '''.format(dash_renderer.__version__, plotly.__version__)))

])
