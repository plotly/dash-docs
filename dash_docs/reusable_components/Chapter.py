import dash_html_components as html
import dash_core_components as dcc
from .Markdown import Markdown

def s(string_block):
    return string_block.replace('    ', '')

def Chapter(name, href=None, caption=None):
    linkComponent = html.A if href.startswith('http') else dcc.Link
    return html.Div(className='toc--chapter', children=[
        html.Li(
            linkComponent(
                name,
                href=href,
                id=href,
                className='toc--chapter-link'
            ),
        ),
        html.Small(
            className='toc--chapter-content',
            children=Markdown(s(caption or '')),
            style={
                'display': 'block',
                'marginTop': '-10px' if caption else ''
            }
        ) if caption else None
    ])
