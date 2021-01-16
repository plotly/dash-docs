import dash_html_components as html
from dash_docs import reusable_components as rc
import dash_core_components as dcc
from dash_docs import tools
import os

content = tools.load_markdown_files(__file__)
check_url = tools.is_in_dash_enterprise()

PAGE_CONTENT = rc.Markdown('''

{setup}

'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}).format(
app_manager_api = (
'[App Manager API](/Docs/app-manager-api)' if check_url else 'Dash Enterprise App Manager API '
),
app_manager_api_notes = (
'' if check_url else '''
> **To view the Dash Enterprise App Manager API docs**, visit: https://<your-dash-enterprise-hostname\>/Docs/kubernetes, 
> replacing <your-dash-enterprise-hostname\> with the hostname of your licensed 
> Dash Enterprise in your VPC. [Look up the hostname for your company’s license](https://go.plotly.com)
''')
))

layout = html.Div([
    html.H1('Dash Enterprise Continuous Integration'),
    html.Div('Implementing continuous integration and continuous delivery for Dash Apps'),
    html.Div([PAGE_CONTENT]),
])
