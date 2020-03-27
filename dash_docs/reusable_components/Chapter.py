import dash_html_components as html
import dash_core_components as dcc
from dash_docs.tools import relpath
from .Markdown import Markdown

def Chapter(name, href=None, caption=None):
    linkComponent = html.A if href.startswith('http') else dcc.Link
    return html.Div(className='toc--chapter', children=[
        html.Li(
            linkComponent(
                name,
                href=relpath(href),
                id=href,
                className='toc--chapter-link'
            ),
        ),
        html.Small(
            className='toc--chapter-content',
            children=Markdown(caption or ''),
            style={
                'display': 'block',
                'marginTop': '-10px' if caption else ''
            }
        ) if caption else None
    ])
