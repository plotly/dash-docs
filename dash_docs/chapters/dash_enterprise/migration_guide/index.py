# coding=utf-8
import dash_html_components as html
from dash_docs import reusable_components as rc
import dash_core_components as dcc
from dash_docs import tools
from textwrap import dedent
import os

content = tools.load_markdown_files(__file__)
check_url = tools.is_in_dash_enterprise()

PAGE_CONTENT = rc.Markdown(''' 

{intro}

'''.format(**{k.replace('.md', ''): dedent(v) for (k, v) in content.items()}).format(
url_sample_app=(
'''
If you haven't already created a dash app, we recommend trying out a 
Dash Enterprise [Sample App or Template](/Docs/templates) Every sample 
app and template is deploy ready and contains all of the necessary 
configuration files. 
''' 
if check_url else 
'''  
To view the Dash Enterprise Sample Apps & Templates, visit: https://<your-dash-enterprise-hostname\>/Docs/template,
 replacing <your-dash-enterprise-hostname\> with the hostname of your licensed Dash Enterprise in your VPC.   
[Look up the hostname for your company’s license](go.plotly.com).
'''),
url_requirements=(
'''
see our [Application Structure Docs](/Docs/requirements) for more details.
'''
if check_url else 
'''
To view the Application Structure Docs, visit: https://<your-dash-enterprise-hostname\>Docs/requirements,
replacing <your-dash-enterprise-hostname\> with the hostname of your licensed Dash Enterprise in your VPC.   
[Look up the hostname for your company’s license](go.plotly.com).
'''),
url_workspaces=('''
See our [Workspaces Docs](/Docs/workspaces) for more details.
'''
if check_url else 
'''
To view the Application Structure Docs, visit: https://<your-dash-enterprise-hostname\>/Docs/requirements,
replacing <your-dash-enterprise-hostname\> with the hostname of your licensed Dash Enterprise in your VPC.   
[Look up the hostname for your company’s license](go.plotly.com).
'''),
url_workspaces_ide=(
'''
See our [Workspaces IDE](/Docs/workspaces/ide) for more details.
'''
if check_url else 
'''
To view Workspace IDE Docs, visit: https://<your-dash-enterprise-hostname>/Docs/workspaces/ide,
replacing <your-dash-enterprise-hostname\> with the hostname of your licensed Dash Enterprise in your VPC.   
[Look up the hostname for your company’s license](go.plotly.com).
'''),
url_initialize=(
'''
See our [Initialization Docs](/dash-enterprise/initialize) for more details.
'''
if check_url else 
'''
To view Initialization Docs, visit: https://<your-dash-enterprise-hostname>/Docs/initialize,
replacing <your-dash-enterprise-hostname\> with the hostname of your licensed Dash Enterprise in your VPC.   
[Look up the hostname for your company’s license](go.plotly.com).
'''),
url_deployment=(
'''
See our [Deployment Docs](/dash-enterprise/deployment) for more details.
'''
if check_url else 
'''
To view Deployment Docs, visit: https://<your-dash-enterprise-hostname>/Docs/performance,
replacing <your-dash-enterprise-hostname\> with the hostname of your licensed Dash Enterprise in your VPC.   
[Look up the hostname for your company’s license](go.plotly.com).
'''),
url_performance=(
'''
See our [App Performance Docs](/performance) for recommendations.
'''
if check_url else 
'''        
To view App Performance Docs, visit: https://<your-dash-enterprise-hostname>/Docs/performance,
replacing <your-dash-enterprise-hostname\> with the hostname of your licensed Dash Enterprise in your VPC.   
[Look up the hostname for your company’s license](go.plotly.com).
''')
))

layout = html.Div([
    html.H1('Preparing an App for Dash Enterprise'),
    html.H2('Migrating from Local Development to Dash Enterprise'),
    html.Div([PAGE_CONTENT]),
])
