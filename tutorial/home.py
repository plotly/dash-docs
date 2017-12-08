# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent as s

from tools import merge

styles = {
    'underline': {
        'border-bottom': 'thin lightgrey solid',
        'margin-top': '50px'
    }
}


def Chapter(name, href=None, caption=None):
    linkComponent = html.A if href.startswith('http') else dcc.Link
    return html.Div([
        html.Li(linkComponent(name, href=href, style={'paddingLeft': 0})),
        html.Small(dcc.Markdown(s(caption or '')), style={
            'display': 'block',
            'marginTop': '-10px' if caption else ''
        }) if caption else None
    ])


def Section(title, links, description=None, headerStyle={}):
    return html.Div([
        html.H2(title, style=merge(styles['underline'], headerStyle)),
        (
            html.Div(description)
            if description is not None else None
        ),
        html.Ul(links)
    ])


layout = html.Div(className='toc', children=[
    html.H1('Dash User Guide'),

    Section("What's Dash?", [
        Chapter('Introduction', '/dash/introduction'),
        Chapter('Announcement', 'https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503'),
        Chapter('Dash App Gallery', '/dash/gallery'),
        Chapter('Winter 2018 Workshops', 'https://plotcon.plot.ly/workshops'),
    ]),

    Section('Dash Tutorial', [
        Chapter('Part 1. Installation', '/dash/installation'),
        Chapter(
            'Part 2. The Dash Layout',
            '/dash/getting-started',
            '''The Dash `layout` describes what your app will
            look like and is composed of a set of declarative Dash components.
        '''),
        Chapter(
            'Part 3. Basic Callbacks',
            '/dash/getting-started-part-2',
            '''Dash apps are made interactive through Dash Callbacks:
            Python functions that are automatically called whenever an input
            component's property changes. Callbacks can be chained, allowing
            one update in the UI to trigger several updates across the app.'''
        ),
        Chapter(
            'Part 4. Callbacks With State',
            '/dash/state',
            '''Basic callbacks are fired whenever the values change. Use
            Dash `State` with Dash `Inputs` to pass in extra values whenever
            the `Inputs` change. `State` is useful for UIs that contain
            forms or buttons.'''
        ),
        Chapter(
            'Part 5. Interactive Graphing and Crossfiltering',
            '/dash/interactive-graphing',
            '''Bind interactivity to the Dash `Graph` component whenever you
            hover, click, or select points on your chart.'''
        ),
        Chapter(
            'Part 6. Sharing Data Between Callbacks',
            '/dash/sharing-data-between-callbacks',
            '''`global` variables will break your Dash apps. However, there
            are other ways to share data between callbacks. This chapter is
            useful for callbacks that run expensive data processing tasks or
            process large data.
            '''
        )
    ]),

    Section('Component Libraries', [
        Chapter('Dash Core Components', '/dash/dash-core-components', '''
            The Dash Core Component library contains a set of higher-level
            components like sliders, graphs, dropdowns, tables, and more.
        '''),
        Chapter('Dash HTML Components', '/dash/dash-html-components', '''
            Dash provides all of the available HTML tags as user-friendly
            Python classes. This chapter explains how this works and the few
            important key differences between Dash HTML components and standard
            html.
        '''),
        Chapter('Build Your Own Components', '/dash/plugins', '''
            Dash components are built with [React.js](https://reactjs.org/).
            Dash provides a React → Dash toolchain that generates a
            Dash-compatible interface to these components in Python.
        ''')
    ]),

    Section('Advanced Usage', [
        Chapter('Performance', '/dash/performance'),
        Chapter('Live Updates', '/dash/live-updates'),
        Chapter('External CSS and JS', '/dash/external-resources'),
        Chapter('URL Routing and Multiple Apps', '/dash/urls')
    ]),

    Section('Production', [
        Chapter('Authentication', '/dash/authentication'),
        Chapter('Deployment', '/dash/deployment'),
    ]),

    Section('Getting Help', [
        Chapter('FAQ', 'https://community.plot.ly/c/dash'),
        Chapter('Support and Contact', href='/dash/support')
    ]),

    Section('Plotly On-Premises', [
        Chapter(
            'About Plotly On-Premises',
            'https://plot.ly/products/on-premise'
        ),
        Chapter(
            'Deploying Dash Apps on Plotly On-Premises',
            '/dash/deployment/on-premise'
        )],
        description="""Plotly On-Premises is Plotly's commercial offering for
        hosting and sharing Dash apps.""",
        headerStyle={'color': '#0D76BF'}
    )
])
