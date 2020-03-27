# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_core_components as dcc
from dash_docs import reusable_components

layout = html.Div(className='gallery', children=[
    reusable_components.Markdown('''
    ## The Dash App Gallery has moved!

    It is now at [https://dash-gallery.plotly.host/Portal/](https://dash-gallery.plotly.host/Portal/)
    ''')
])
