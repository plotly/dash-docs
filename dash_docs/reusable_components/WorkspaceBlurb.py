import dash_core_components as dcc
import dash_html_components as html

WorkspaceBlurb = html.Div([
  dcc.Markdown(
'''
> Dash Enterprise is the fastest way to write & deploy Dash apps and
> Jupyter notebooks. Dash Enterprise can be installed on the Kubernetes
> services of
> [AWS](https://plotly.com/dash/aws/?utm_source=docs&utm_medium=workspace&utm_campaign=nov&utm_content=aws),
> [Azure](https://plotly.com/dash/azure/?utm_source=docs&utm_medium=workspace&utm_campaign=nov&utm_content=azure),
> [GCP](https://plotly.com/dash/on-premises-linux/?utm_source=docs&utm_medium=workspace&utm_campaign=nov&utm_content=linux),
> or an
> [on-premise Linux Server](https://plotly.com/dash/on-premises-linux/?utm_source=docs&utm_medium=workspace&utm_campaign=nov&utm_content=linux).
> 10% of the Fortune 500 uses Dash Enterprise to productionize AI and data science apps.
> [Find out if your company is using Dash Enterprise](https://go.plotly.com/company-lookup)
''',
  )
])
