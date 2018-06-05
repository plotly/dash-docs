import time
import six
import os
from datetime import datetime as dt

import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt

from dash.dependencies import Input, State, Event, Output

from server import app, server

import architecture
import authentication
import basic_callbacks
import callbacks_with_dependencies
import changelog
import chapter_index
import dynamic_content
import home
import html_component_appendix
import open_problems

css = [
    'https://cdn.rawgit.com/plotly/dash-app-stylesheets/8485c028c19c393e9ab85e1a4fafd78c489609c2/dash-docs-base.css',
    'https://cdn.rawgit.com/plotly/dash-app-stylesheets/30b641e2e89753b13e6557b9d65649f13ea7c64c/dash-docs-custom.css',
    'https://fonts.googleapis.com/css?family=Dosis',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
]
js = ['https://cdn.rawgit.com/chriddyp/ca0d8f02a1659981a0ea7f013a378bbd/raw/e79f3f789517deec58f41251f7dbb6bee72c44ab/plotly_ga.js',
      'https://cdn.jsdelivr.net/npm/instantsearch.js@2.3/dist/instantsearch.min.js',
      'https://codepen.io/plotly/pen/ZvPmYv.js'
]

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
                html.A('workshops', className='link', href='https://plotcon.plot.ly/'),
                html.A('user guide', className='link active', href='/'),
                html.A('plotly', className='link', href='https://plot.ly/'),
                html.A(children=[html.I(className="fa fa-search")], className='link', href='/search')
            ])
        ]
    )
)

app.title = 'Dash User Guide and Documentation - Dash by Plotly'

app.layout = html.Div(
    [html.Link(rel='stylesheet', href=css_link) for css_link in css] +
    [
        html.Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        html.Meta(
            name='description',
            content=('Dash User Guide and Documentation. '
                     'Dash is a Python framework for building '
                     'reactive web apps developed by Plotly.')
        ),
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
        content = html.Div([
            html.Div(chapters[matched[0]]['content']),
            html.Hr(),
            dcc.Link(html.A('Back to the Table of Contents'), href='/'),
            html.Div(id='wait-for-page-{}'.format(pathname)),
        ])
    else:
        content = chapters['index']['content']

    return content


app.css.append_css({'external_url': css})
app.scripts.append_script({'external_url': js})

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8050)
