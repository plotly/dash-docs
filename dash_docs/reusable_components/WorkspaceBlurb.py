import dash_core_components as dcc
import dash_html_components as html

WorkspaceBlurb = html.Div([
    html.Blockquote([dcc.Markdown(
        '''
        Write, deploy, and scale Dash apps on a Dash Enterprise Kubernetes cluster.
        [Pricing](https://plotly.com/get-pricing/) | 
        [Dash Enterprise Demo](https://plotly.com/get-demo/) | 
        [Dash Enterprise Overview](https://plotly.com/dash/)
        '''),
    ])
])
