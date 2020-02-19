# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash_docs.chapter_index import URLS

from dash_docs.reusable_components import TOC
from dash_docs.tools import merge

styles = {
    'underline': {
        'border-bottom': 'thin lightgrey solid',
        'margin-top': '50px'
    }
}

layout = html.Div([
    html.H1('Dash User Guide'),

    dcc.Markdown(
        '''
        *This user guide is for the Python implementation of Dash.
        Dash is also available in R.
        View the [Dash for R User Guide & Documentation](https://dashr.plotly.com)*
        ''', style={'fontSize': 14}
    ),

    TOC(URLS)
])
