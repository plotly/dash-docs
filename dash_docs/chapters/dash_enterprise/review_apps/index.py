# -*- coding: utf-8 -*-
import dash_html_components as html
from dash_docs import reusable_components as rc
import dash_core_components as dcc
from dash_docs import tools
import os

content = tools.load_markdown_files(__file__)
check_url = tools.is_in_dash_enterprise()

PAGE_CONTENT = rc.Markdown('''

    {intro}
    {setup}


'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}))

layout = html.Div([
    PAGE_CONTENT,
])
