import dash_core_components as dcc
import dash_html_components as html

from dash_docs import styles
from dash_docs import reusable_components

def Syntax(children, style=styles.code_container, summary=''):
    code = children
    if not code.startswith('```'):
        code = '```py\n' + code + '\n```'

    if summary:
        return html.Details([
            html.Summary(summary),
            reusable_components.Markdown(code, style=style)
        ], open=True)
    else:
        return reusable_components.Markdown(code, style=style)


def Example(example):
    return html.Div(example, className='example-container')
