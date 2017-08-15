import time
import six
import os

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, State, Event, Output

from server import app, server
import introduction
import html_components
import core_components
import basic_callbacks
import html_component_appendix
import callbacks_with_dependencies
import dynamic_content
import external_css_and_js
import open_problems
import architecture
import live_updates
import changelog
import plugins
import gallery
import performance
import support
import deployment
import authentication
import installation
import getting_started_part_1
import getting_started_part_2
import urls
import auth
import on_premise_deployment

dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-1.27.1.min.js'

def create_contents(contents):
    h = []
    for i in contents:
        if isinstance(i, list):
            h.append(create_contents(i))
        else:
            h.append(html.Li(i))
    return html.Ul(h)


toc = html.Div(
create_contents([

    dcc.Link(html.A('Introduction'), href="/dash/introduction"),

    html.A('Announcement Letter',
           href="https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503"),

    dcc.Link(html.A('Gallery'), href="/dash/gallery"),

    dcc.Link(html.A('Installation'), href="/dash/installation"),

    dcc.Link(html.A('Create Your First App - Part 1'), href="/dash/getting-started"),

    dcc.Link(html.A('Create Your First App - Part 2'), href="/dash/getting-started-part-2"),

    dcc.Link(html.A('Performance'), href="/dash/performance"),

    dcc.Link(html.A('Live Updates'), href="/dash/live-updates"),

    dcc.Link(html.A('External CSS and JS'), href="/dash/external-resources"),

    dcc.Link(html.A('Dash Core Components'), href="/dash/dash-core-components"),

    dcc.Link(html.A('Dash HTML Components'), href="/dash/dash-html-components"),

    dcc.Link(html.A('Build Your Own Components'), href="/dash/plugins"),

    dcc.Link(html.A('URL Support'), href="/dash/urls"),

    dcc.Link(html.A('Authentication'), href="/dash/authentication"),

    dcc.Link(html.A('Deployment'), href="/dash/deployment"),


    html.A('FAQ', href="https://community.plot.ly/c/dash"),

    dcc.Link(html.A('Support and Contact'), href="/dash/support")

]), className="toc-chapters"
)

chapters = {
    'index': {
        'url': '/dash/',
        'content': html.Div([
            html.H1('Dash User Guide'),
            toc
        ], className="toc")
    },

    'introduction': {
        'url': '/dash/introduction',
        'content': introduction.layout
    },

    'installation': {
        'url': '/dash/installation',
        'content': installation.layout
    },

    'getting-started': {
        'url': '/dash/getting-started',
        'content': getting_started_part_1.layout
    },

    'getting-started-part-2': {
        'url': '/dash/getting-started-part-2',
        'content': getting_started_part_2.layout
    },

    'dash-core-components': {
        'url': '/dash/dash-core-components',
        'content': core_components.layout
    },

    'dash-html-components': {
        'url': '/dash/dash-html-components',
        'content': [
            html_components.layout,
            # html_component_appendix.layout
        ]
    },

    'external': {
        'url': '/dash/external-resources',
        'content': external_css_and_js.layout
    },

    'plugins': {
        'url': '/dash/plugins',
        'content': plugins.layout
    },

    'gallery': {
        'url': '/dash/gallery',
        'content': gallery.layout
    },

    'live-updates': {
        'url': '/dash/live-updates',
        'content': live_updates.layout
    },

    'performance': {
        'url': '/dash/performance',
        'content': performance.layout
    },

    'urls': {
        'url': '/dash/urls',
        'content': urls.layout
    },

    'deployment': {
        'url': '/dash/deployment',
        'content': deployment.layout
    },

    'deployment-onpremise': {
        'url': '/dash/deployment/on-premise',
        'content': on_premise_deployment.layout
    },

    'auth': {
        'url': '/dash/authentication',
        'content': auth.layout
    },

    'support': {
        'url': '/dash/support',
        'content': support.layout
    }
}

header = html.Div(
    className='header',
    children=html.Div(
        className='container-width',
        style={'height': '100%'},
        children=[
            html.A(html.Img(
                src="https://cdn.rawgit.com/plotly/dash-docs/b1178b4e/images/dash-logo-stripe.svg",
                className="logo"
            ), href='https://plot.ly/products/dash', className="logo-link"),

            html.Div(className="links", children=[
                html.A('pricing', className="link", href="https://plot.ly/products/on-premise"),
                html.A('user guide', className="link active", href="https://plot.ly/dash/"),
                html.A('plotly', className="link", href="https://plot.ly/")
            ])
        ]
    )
)

app.title = 'Dash User Guide and Documentation - Dash by Plotly'

app.layout = html.Div([
    html.Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
    html.Meta(
        name='description',
        content=('Dash User Guide and Documentation. '
                 'Dash is a Python framework for building '
                 'reactive web apps developed by Plotly.')
    ),
    header,
    html.Div([
        html.Div([
            html.Div(
                html.Div(id="chapter", className="content"),
                className="content-container"
            ),
        ], className="container-width")
    ], className="background"),
    dcc.Location(id='location', refresh=False)
])


@app.callback(Output('chapter', 'children'), [Input('location', 'pathname')])
def display_content(pathname):
    if pathname is None:
        return html.Div()
    matched = [c for c in chapters.keys()
               if chapters[c]['url'] == pathname]

    if matched and matched[0] != 'index':
        content = html.Div([
            html.Div(chapters[matched[0]]['content']),
            html.Hr(),
            dcc.Link(html.A('Back to the Table of Contents'), href='/dash/')
        ])
    else:
        content = chapters['index']['content']

    return content


app.css.append_css({
    'external_url': (
        'https://cdn.rawgit.com/plotly/dash-app-stylesheets/8485c028c19c393e9ab85e1a4fafd78c489609c2/dash-docs-base.css',
        'https://cdn.rawgit.com/plotly/dash-app-stylesheets/30b641e2e89753b13e6557b9d65649f13ea7c64c/dash-docs-custom.css',
        'https://fonts.googleapis.com/css?family=Dosis'
    )
})

if 'DYNO' in os.environ:
    app.scripts.config.serve_locally = True
    app.scripts.append_script({
        'external_url': 'https://cdn.rawgit.com/chriddyp/ca0d8f02a1659981a0ea7f013a378bbd/raw/e79f3f789517deec58f41251f7dbb6bee72c44ab/plotly_ga.js'
    })
else:
    app.scripts.config.serve_locally = True

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8050)
