import dash_html_components as html
import dash_core_components as dcc
from dash_docs.tools import relpath
from .Markdown import Markdown

def Chapter(name, href=None, caption=None, className='', chapter='', icon=''):
    linkComponent = html.A if href.startswith('http') else dcc.Link
    return html.Div(className='toc--chapter', children=[
        html.Li([
            html.I(className=icon, style={'width': 25}) if icon != '' else None,
            linkComponent(
                name,
                href=relpath(href),
                id=href,
                className='toc--chapter-link ' + className
            ),
        ]),
        html.Small(
            className='toc--chapter-content',
            children=Markdown(caption or ''),
            style={
                'display': 'block',
                'marginTop': '-10px' if caption else ''
            }
        ) if caption else None
    ])
