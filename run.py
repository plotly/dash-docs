import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt
import dash_table

from dash.dependencies import Input, Output

from server import app, server

from tutorial import chapter_index
from tutorial import home


def create_contents(contents):
    h = []
    for i in contents:
        if isinstance(i, list):
            h.append(create_contents(i))
        else:
            h.append(html.Li(i))
    return html.Ul(h)


chapters = {
    'index': {
        'url': '/',
        'content': home.layout,
        'name': 'Index',
        'description': ''
    }
}

chapters.update(chapter_index.chapters)

header = html.Div(
    className='header',
    children=html.Div(
        className='container-width',
        style={'height': '100%'},
        children=[
            html.A(html.Img(
                src='https://cdn.rawgit.com/plotly/dash-docs/b1178b4e/images/dash-logo-stripe.svg',
                className='logo'
            ), href='https://plot.ly/products/dash', className='logo-link'),

            html.Div(className='links', children=[
                html.A('pricing', className='link', href='https://plot.ly/dash/pricing'),
                html.A('user guide', className='link active', href='/'),
                html.A('plotly', className='link', href='https://plot.ly/'),
                html.A(children=[html.I(className="fa fa-search")], className='link', href='/search')
            ])
        ]
    )
)

app.title = 'Dash User Guide and Documentation - Dash by Plotly'

app.layout = html.Div(
    [
        header,
        html.Div([
            html.Div(id='wait-for-layout'),
            html.Div([
                html.Div(
                    html.Div(id='chapter', className='content'),
                    className='content-container'
                ),
            ], className='container-width')
        ], className='background'),
        dcc.Location(id='location', refresh=False),
        html.Div(dash_table.DataTable(id='_blank'), style={'display': 'none'}),
        html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'})
    ]
)


@app.callback(Output('chapter', 'children'),
    [Input('location', 'pathname')])
def display_content(pathname):
    if pathname is None:
        return ''
    if pathname.endswith('/') and pathname != '/':
        pathname = pathname[:len(pathname) - 1]
    matched = [c for c in chapters.keys()
               if chapters[c]['url'] == pathname]

    if matched and matched[0] != 'index':
        if 'dash-deployment-server/' in pathname:
            content = html.Div([
                html.Div(chapters[matched[0]]['content']),
                html.Hr(),
                dcc.Link(html.A('Back to Dash Deployment Server Documentation'), href='/dash-deployment-server'),
                html.Div(id='wait-for-page-{}'.format(pathname)),
            ])
        elif 'dash-table/' in pathname:
            content = html.Div([
                html.Div(chapters[matched[0]]['content']),
                html.Hr(),
                dcc.Link(
                    'Back to Dash Table Documentation',
                    href='/dash-table'
                ),
                html.Br(),
                dcc.Link(
                    'Back to Dash Documentation',
                    href='/'
                ),
                html.Div(id='wait-for-page-{}'.format(pathname)),
            ])
        else:
            content = html.Div([
                html.Div(chapters[matched[0]]['content']),
                html.Hr(),
                dcc.Link(html.A('Back to the Table of Contents'), href='/'),
                html.Div(id='wait-for-page-{}'.format(pathname)),
            ])

    else:
        content = chapters['index']['content']

    return content

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta
            name="description"
            content="Dash User Guide and Documentation. Dash is a Python framework for building analytical web apps in Python."
        >
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <!-- Global site tag (gtag.js) - AdWords: 1009791370 -->
        <script async src=""https://www.googletagmanager.com/gtag/js?id=AW-1009791370""></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', 'AW-1009791370');
        </script>
        <!-- Google Tag Manager Tag -->
        <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-N6T2RXG');</script>
    </head>
    <body>
        <!-- Google Tag Manager Tag -->
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N6T2RXG"
            height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8060)
