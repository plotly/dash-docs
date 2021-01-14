import dash_html_components as html
from dash_docs import reusable_components as rc
import dash_core_components as dcc
from dash_docs import tools
import os

content = tools.load_markdown_files(__file__)

PAGE_CONTENT = rc.Markdown('''

{setup}

'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()})
)

layout = html.Div([
    html.H1('Dash Enterprise Continuous Integration'),
    html.Div(''),
    PAGE_CONTENT
])

# {designate_admin}
# {ssh}
# {ci_script}