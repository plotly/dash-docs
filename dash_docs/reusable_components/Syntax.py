import dash_html_components as html

from dash_docs import styles
from . import Markdown

from textwrap import dedent

def Syntax(children, style=styles.code_container, summary=''):
    code = dedent(children).strip()
    if not code.startswith('```'):
        code = '```py\n' + code.strip() + '\n```'

    if summary:
        return html.Details([
            html.Summary(summary),
            Markdown(code, style=style)
        ], open=True)
    else:
        return Markdown(code, style=style)
