from collections import OrderedDict

import dash_html_components as html
import dash_core_components as dcc
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

sections_ordered = OrderedDict()
sections_ordered['What\'s Dash?'] = [
    'introduction',
    'gallery'
]
sections_ordered['Dash Tutorial'] = [
    'installation',
    'getting-started',
    'getting-started-part-2',
    'state',
    'graphing',
    'shared-state',
    'faqs'
]
sections_ordered['Component Libraries'] = [
    'dash-core-components',
    'dash-html-components',
    'datatable',
    'dashdaq'
]
sections_ordered['Creating Your Own Components'] = [
    'react-for-python-developers',
    'plugins',
    'd3-plugins'
]
sections_ordered['Beyond the Basics'] = [
    'performance',
    'live-updates',
    'external',
    'urls',
    'devtools'
]
sections_ordered['Production'] = [
    'auth',
    'deployment'
]
sections_ordered['Getting Help'] = [
    # TODO add in the dash community forum
    'support'
]
sections_ordered['Component Examples'] = [
    'dropdown-examples',
    'slider-examples',
    'range-slider-examples',
    'checklist-examples',
    'input-examples',
    'radio-item-examples',
    'button-examples',
    'datepickersingle-examples',
    'datepickerrange-examples',
    'markdown-examples',
    'link-examples',
    'tabs-example',
    'textarea-examples',
    'upload-examples',
    'booleanswitch-examples',
    'colorpicker-examples',
    'gauge-examples',
    'graduatedbar-examples',
    'indicator-examples',
    'knob-examples',
    'leddisplay-examples',
    'numericinput-examples',
    'powerbutton-examples',
    'precisioninput-examples',
    'stopbutton-examples',
    'slider-examples',
    'tank-examples',
    'thermometer-examples',
    'toggleswitch-examples',
    'darkthemeprovider-examples'
]

header = html.Div(
    className='header',
    children=html.Div(
        className='container-width',
        style={'height': '100%'},
        children=[
            html.A(html.Img(
                src='/assets/images/logo.png',
                className='logo'
            ), href='https://plot.ly/products/dash'),

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
        # Stores used by examples.
        dcc.Store(id='memory'),
        dcc.Store(id='memory-output'),
        dcc.Store(id='local', storage_type='local'),
        dcc.Store(id='session', storage_type='session'),
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
    ]
)


@app.callback(Output('chapter', 'children'),
              [Input('location', 'pathname')])
def display_content(pathname):
    if pathname is None:
        return ''
    if pathname.endswith('/') and pathname != '/':
        pathname = pathname[:len(pathname) - 1]

    if pathname.split('/')[-1] == 'all':
        pdf_contents = []
        table_of_contents = []

        for section in sections_ordered.keys():
            section_content = []
            section_toc = []
            section_id = section.replace(
                ' ', '-').replace(
                    '\'', '').replace(
                        '?', '').lower()
            section_content.append(
                html.H1(section, className='pdf-docs-section-name')
            )
            for chapter in sections_ordered[section]:
                section_content.append(html.Div(
                    chapters[chapter]['content'],
                    className='pdf-docs-chapter',
                    id=chapter
                ))
                section_toc.append(
                    html.A(chapter.replace('-', ' ').title(),
                           href='#{}'.format(chapter))
                )

            pdf_contents.append(html.Div(
                section_content,
                className='pdf-docs-section',
                id=section_id
            ))
            # add main section to table of contents
            table_of_contents.append(
                html.A(section,
                       href='#{}'.format(section_id),
                       className='toc-section-link')
            )
            # add all subsections
            table_of_contents.append(
                html.Div(section_toc,
                         className='toc-chapter-links')
            )

        # insert table of contents
        return html.Div([
            html.Div("Dash User Guide and Documentation",
                     id='pdf-docs-title'),
            html.Div([html.H1('Table of Contents')] + table_of_contents,
                     id='pdf-docs-toc'),
            html.Div(pdf_contents)
        ], id='pdf-docs')

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
        elif 'datatable/' in pathname:
            content = html.Div([
                html.Div(chapters[matched[0]]['content']),
                html.Hr(),
                dcc.Link(
                    'Back to DataTable Documentation',
                    href='/datatable'
                ),
                html.Br(),
                dcc.Link(
                    'Back to Dash Documentation',
                    href='/'
                ),
                html.Div(id='wait-for-page-{}'.format(pathname)),
            ])

        elif 'cytoscape/' in pathname:
            content = html.Div([
                html.Div(chapters[matched[0]]['content']),
                html.Hr(),
                dcc.Link(
                    'Back to Cytoscape Documentation',
                    href='/cytoscape'
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


app.index_string = '''<!DOCTYPE html>
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
            {%renderer%}
        </footer>
    </body>
</html>'''

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8060)
