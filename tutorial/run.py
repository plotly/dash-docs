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
import auth
import authentication
import basic_callbacks
import callbacks_with_dependencies
import changelog
import core_component_examples as examples
import core_components
import deployment
import dynamic_content
import external_css_and_js
import gallery
import getting_started_part_1
import getting_started_part_2
import graphing
import home
import html_component_appendix
import html_components
import installation
import introduction
import live_updates
import on_premise_deployment
import open_problems
import performance
import plugins
import sharing_state
import state
import support
import urls

dcc._js_dist[0]['external_url'] = (
    'https://cdn.plot.ly/plotly-basic-1.31.0.min.js'
)

css = [
    'https://cdn.rawgit.com/plotly/dash-app-stylesheets/8485c028c19c393e9ab85e1a4fafd78c489609c2/dash-docs-base.css',
    'https://cdn.rawgit.com/plotly/dash-app-stylesheets/30b641e2e89753b13e6557b9d65649f13ea7c64c/dash-docs-custom.css',
    'https://fonts.googleapis.com/css?family=Dosis'
]
js = ['https://cdn.rawgit.com/chriddyp/ca0d8f02a1659981a0ea7f013a378bbd/raw/e79f3f789517deec58f41251f7dbb6bee72c44ab/plotly_ga.js']


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
        'url': '/dash/',
        'content': home.layout
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

    'state': {
        'url': '/dash/state',
        'content': state.layout
    },

    'graphing': {
        'url': '/dash/interactive-graphing',
        'content': graphing.layout
    },

    'shared-state': {
        'url': '/dash/sharing-data-between-callbacks',
        'content': sharing_state.layout
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
    },

    'dropdown-examples': {
        'url': '/dash/dash-core-components/dropdown',
        'content': examples.Dropdown
    },

    'slider-examples': {
        'url': '/dash/dash-core-components/slider',
        'content': examples.Slider
    },

    'range-slider-examples': {
        'url': '/dash/dash-core-components/rangeslider',
        'content': examples.RangeSlider
    },

    'checklist-examples': {
        'url': '/dash/dash-core-components/checklist',
        'content': examples.Checklist
    },

    'input-examples': {
        'url': '/dash/dash-core-components/input',
        'content': examples.Input
    },

    'radio-item-examples': {
        'url': '/dash/dash-core-components/radioitems',
        'content': examples.RadioItems
    },

    'datepickersingle-examples': {
        'url': '/dash/dash-core-components/datepickersingle',
        'content': examples.DatePickerSingle
    },

    'datepickerrange-examples': {
        'url': '/dash/dash-core-components/datepickerrange',
        'content': examples.DatePickerRange
    },

    'markdown-examples': {
        'url': '/dash/dash-core-components/markdown',
        'content': examples.Markdown
    },

    'link-examples': {
        'url': '/dash/dash-core-components/link',
        'content': examples.Link
    },

    'textarea-examples': {
        'url': '/dash/dash-core-components/textarea',
        'content': examples.Textarea
    },

    'upload-examples': {
        'url': '/dash/dash-core-components/upload',
        'content': examples.Upload
    }
}

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
                html.A('pricing', className='link', href='https://plot.ly/products/on-premise'),
                html.A('workshops', className='link', href='https://plotcon.plot.ly/workshops'),
                html.A('user guide', className='link active', href='https://plot.ly/dash/'),
                html.A('plotly', className='link', href='https://plot.ly/')
            ])
        ]
    )
)

app.title = 'Dash User Guide and Documentation - Dash by Plotly'

app.layout = html.Div(
    [html.Link(rel='stylesheet', href=css_link) for css_link in css] +
    [html.Script(type='text/javascript', src=js_link) for js_link in js] +
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
            dcc.Link(html.A('Back to the Table of Contents'), href='/dash/'),
            html.Div(id='wait-for-page-{}'.format(pathname)),
        ])
    else:
        content = chapters['index']['content']

    return content


app.css.append_css({'external_url': css})
app.scripts.append_script({'external_url': js})

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8050)
