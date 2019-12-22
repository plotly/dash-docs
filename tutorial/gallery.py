# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_core_components as dcc
from textwrap import dedent

layout = html.Div(className='gallery', children=[
    dcc.Markdown(dedent('''
    ## The Dash App Gallery has moved!

    It is now at [https://dash-gallery.plotly.host/Portal/](https://dash-gallery.plotly.host/Portal/)
    '''))
])
