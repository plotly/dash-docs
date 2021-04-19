# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash_docs.chapter_index import URLS, URL_TO_CONTENT_MAP, DASH_ENTERPRISE_URLS

from dash_docs.convert_to_html import convert_to_html
from dash_docs.reusable_components import TOC, WorkspaceBlurb
from dash_docs.tools import merge, relpath

styles = {
    'underline': {
        'border-bottom': 'thin lightgrey solid',
        'margin-top': '50px'
    }
}

layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Dash open-source', children=[
            html.H2('Dash Python User Guide'),

            html.Blockquote([dcc.Markdown(
                '''
                Dash brings low-code data apps to these languages: 
                
                [Python](dash.plotly.com) | 
                [R](dashr.plotly.com) | 
                [Julia](https://dashjulia.plotly.com) | 
                [.NET](https://github.com/plotly/Dash.NET)
                '''),
            ]),

            WorkspaceBlurb,

            TOC(URLS)
        ]),

        dcc.Tab(label='Dash Enterprise', children=[
            html.Div(TOC([DASH_ENTERPRISE_URLS])),
            html.Img(
                src=relpath('/assets/images/dds/app-architecture.jpg'),
                alt='Dash App Architecture Diagram'
            )
        ])

    ])
])


# Ugly side effect:
# home isn't in chapter_index because it's created dynamically in this file
# from the URLS: importing it into chapter_index would be a circular import.
# Since it's not in chapter_index, it's also not in the server-side rendering
# dict.
# So, we add it here as a side effect from importing.
URL_TO_CONTENT_MAP['/'] = layout
