import dash_core_components as dcc
import dash_html_components as html

def image(vendor):
    return html.A(
        [
            html.Img(
                src='/assets/images/dds/{}-logo.png'.format(vendor)
            ),
            html.Div(
                'Install Dash Enterprise on {}'.format(vendor),
                className='label'
            )
        ],
        href='https://go.plotly.com/dash-{}'.format(vendor.lower()),
        className='azure'
    )


WorkspaceBlurb = html.Div([
    html.Blockquote([dcc.Markdown(
        '''
        Dash Enterprise is the fastest way to write & deploy Dash apps and
        Jupyter notebooks. Dash Enterprise can be installed on the Kubernetes
        services of
        [AWS](https://go.plotly.com/dash-aws),
        [Azure](https://go.plotly.com/dash-azure),
        GCP,
        or an
        [on-premise Linux Server](https://plotly.com/dash/on-premises-linux/?utm_source=docs&utm_medium=workspace&utm_campaign=nov&utm_content=linux).
        10% of the Fortune 500 uses Dash Enterprise to productionize AI and data science apps.
        [Find out if your company is using Dash Enterprise](https://go.plotly.com/company-lookup)
        '''),

        html.Div([
            image('Azure'),
            html.Div(className='spacer'),
            image('AWS'),
        ], className='azure-parent')

    ])
])
