# -*- coding: utf-8 -*-
from textwrap import dedent as s
import dash_core_components as dcc
import dash_html_components as html
from chapter_index import chapters

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
        html.Li(
            linkComponent(
                name,
                href=href,
                style={'paddingLeft': 0},
                id=href
            )
        ),
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
        Chapter(chapters['introduction']['name'],
                chapters['introduction']['url']),
        Chapter('Announcement',
                'https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503'),
        Chapter(chapters['gallery']['name'],
                chapters['gallery']['url']),
        Chapter('Winter 2018 Workshops',
                'https://plotcon.plot.ly/workshops'),
    ]),

    Section('Dash Tutorial', [
        Chapter(chapters['installation']['name'],
                chapters['installation']['url']),
        Chapter(chapters['getting-started']['name'],
                chapters['getting-started']['url'],
                chapters['getting-started']['description']),
        Chapter(chapters['getting-started-part-2']['name'],
                chapters['getting-started-part-2']['url'],
                chapters['getting-started-part-2']['description']),
        Chapter(chapters['state']['name'],
                chapters['state']['url'],
                chapters['state']['description']),
        Chapter(chapters['graphing']['name'],
                chapters['graphing']['url'],
                chapters['graphing']['description']),
        Chapter(chapters['shared-state']['name'],
                chapters['shared-state']['url'],
                chapters['shared-state']['description'])
    ]),

    Section('Component Libraries', [
        Chapter(chapters['dash-core-components']['name'],
                chapters['dash-core-components']['url'],
                chapters['dash-core-components']['description']),
        Chapter(chapters['dash-html-components']['name'],
                chapters['dash-html-components']['url'],
                chapters['dash-html-components']['description']),
        Chapter(chapters['plugins']['name'],
                chapters['plugins']['url'],
                chapters['plugins']['description'])
    ]),

    Section('Advanced Usage', [
        Chapter(chapters['performance']['name'],
                chapters['performance']['url'],
                chapters['performance']['description']),
        Chapter(chapters['live-updates']['name'],
                chapters['live-updates']['url'],
                chapters['live-updates']['description']),
        Chapter(chapters['external']['name'],
                chapters['external']['url'],
                chapters['external']['description']),
        Chapter(chapters['urls']['name'],
                chapters['urls']['url'],
                chapters['urls']['description'])
    ]),

    Section('Production', [
        Chapter(chapters['auth']['name'],
                chapters['auth']['url']),
        Chapter(chapters['deployment']['name'],
                chapters['deployment']['url']),
    ]),

    Section('Getting Help', [
        Chapter('FAQ', 'https://community.plot.ly/c/dash'),
        Chapter(chapters['support']['name'],
                chapters['support']['url'])
    ]),

    Section('Plotly On-Premises', [
        Chapter('About Plotly On-Premises',
                'https://plot.ly/products/on-premise'),
        Chapter(chapters['deployment-onpremise']['name'],
                chapters['deployment-onpremise']['url'])],
        description="""Plotly On-Premises is Plotly's commercial offering for
                       hosting and sharing Dash apps.""",
        headerStyle={'color': '#0D76BF'}
    )
])
