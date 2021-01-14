# -*- coding: utf-8 -*-
import dash_html_components as html
from dash_docs import reusable_components as rc
import dash_core_components as dcc
from dash_docs import tools
import os

content = tools.load_markdown_files(__file__)
check_url = tools.is_in_dash_enterprise()

PAGE_CONTENT_PY = [rc.Markdown('''

{buildpack_detection}
{project_folder_py}
{lifecycle_py}
# Required Files
{app_py}
{requirements_py}
{procfile_py}
# Optional Files
{checks}
{app_json}
{dokku_scale}            
{gitignore}
{runtime_py}
'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}).format(
kubernetes_notes = (
'' if check_url else '''
> **To view the Kubernetes docs**, visit: https://<your-dash-enterprise-hostname\>/Docs/kubernetes, 
> replacing <your-dash-enterprise-hostname\> with the hostname of your licensed 
> Dash Enterprise in your VPC. [Look up the hostname for your company’s license](https://go.plotly.com)
'''),
kubernetes = ('[Dash Enterprise Kubernetes](/Docs/kubernetes)' if check_url else 'Dash Enterprise Kubernetes'),
configure_system_dependencies = ('[Configuring System Dependencies](/dash-enterprise/configure-system-dependencies)'),
job_queue = ('[job queue](/Docs/dash-snapshots/usage-job-queue)' if check_url else 'job queue'),
job_queue_notes = (
'' if check_url else '''
> **To view the Job Queue docs**, visit: https://<your-dash-enterprise-hostname\>/Docs/dash-snapshots/usage-job-queue, 
> replacing <your-dash-enterprise-hostname\> with the hostname of your licensed 
> Dash Enterprise in your VPC. [Look up the hostname for your company’s license](https://go.plotly.com)
'''),
)),

html.Details(open=False, children=[
    html.Summary(children=[rc.Markdown('**Dash Enterprise supports the following Python versions:**')]),
    rc.Markdown('''{runtime_list_py}'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}))
]),

rc.Markdown('''
---
{apt_files}
{buildpacks_py}
'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}).format(
kubernetes_notes = (
'' if check_url else '''
> **To view the Kubernetes docs**, visit: https://<your-dash-enterprise-hostname\>/Docs/kubernetes, 
> replacing <your-dash-enterprise-hostname\> with the hostname of your licensed 
> Dash Enterprise in your VPC. [Look up the hostname for your company’s license](https://go.plotly.com)
'''),
kubernetes = ('[Dash Enterprise Kubernetes](/Docs/kubernetes)' if check_url else 'Dash Enterprise Kubernetes'),
configure_system_dependencies = ('[Configuring System Dependencies](/dash-enterprise/configure-system-dependencies)')
))
]

PAGE_CONTENT_CONDA = rc.Markdown('''

{buildpack_detection}
{conda}
{project_folder_conda}
{lifecycle_conda}
# Required Files
{app_py}
{requirements_conda}
{procfile_py}
# Optional Files
{checks}
{app_json}
{dokku_scale}            
{gitignore}
{runtime_conda}
{apt_files}
{buildpacks_conda}
'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}).format(
kubernetes_notes = (
'' if check_url else '''
> **To view the Kubernetes docs**, visit: https://<your-dash-enterprise-hostname\>/Docs/kubernetes, 
> replacing <your-dash-enterprise-hostname\> with the hostname of your licensed 
> Dash Enterprise in your VPC. [Look up the hostname for your company’s license](https://go.plotly.com)
'''),
kubernetes = ('[Dash Enterprise Kubernetes](/Docs/kubernetes)' if check_url else 'Dash Enterprise Kubernetes'),
configure_system_dependencies = ('[Configuring System Dependencies](/dash-enterprise/configure-system-dependencies)'),
rapids_conda_templates = ( 
'See [NVIDIA Rapids Sample App](/Docs/templates/rapids) and [Conda Sample App](/Docs/templates/conda) for more details' if check_url else '''
> **To view NVIDIA Rapids and Conda Sample Apps**, visit: https://<your-dash-enterprise-hostname\>/Docs/templates, 
> replacing <your-dash-enterprise-hostname\> with the hostname of your licensed 
> Dash Enterprise in your VPC. [Look up the hostname for your company’s license](https://go.plotly.com)'''),
job_queue = ('[job queue](/Docs/dash-snapshots/usage-job-queue)' if check_url else 'job queue')
)),


PAGE_CONTENT_R = rc.Markdown('''

{buildpack_detection}
{project_folder_r}
{lifecycle_r}
# Required Files
{app_r}
{init_r}
{procfile_r}
# Optional Files
{checks_r}
{app_json}
{dokku_scale}
{gitignore}
{runtime_r}
{apt_files_r}
{buildpacks_r}
'''.format(**{k.replace('.md', ''): v for (k, v) in content.items()}).format(
kubernetes_notes = (
'' if check_url else '''
> **To view the Kubernetes docs**, visit: https://<your-dash-enterprise-hostname\>/Docs/kubernetes, 
> replacing <your-dash-enterprise-hostname\> with the hostname of your licensed 
> Dash Enterprise in your VPC. [Look up the hostname for your company’s license](https://go.plotly.com)
'''),
kubernetes = ('[Dash Enterprise Kubernetes](/Docs/kubernetes)' if check_url else 'Dash Enterprise Kubernetes'),
configure_system_dependencies = ('[Configuring System Dependencies](/dash-enterprise/configure-system-dependencies)'),
job_queue = ('[job queue](/Docs/dash-snapshots/usage-job-queue)' if check_url else 'job queue')
)),

PYTHON_TAB = html.Div(
    PAGE_CONTENT_PY
)

CONDA_TAB = html.Div(
    PAGE_CONTENT_CONDA
)

R_TAB = html.Div(
    PAGE_CONTENT_R
)

layout = html.Div([
    html.H1('Application Structure'),
    html.Div(''),

    dcc.Tabs([
        dcc.Tab(label = 'Python', children = PYTHON_TAB),
        dcc.Tab(label = 'Conda', children = CONDA_TAB),
        dcc.Tab(label = 'R', children = R_TAB)
    ])
])

