import dash_core_components as dcc
import dash_html_components as html

from tutorial import styles


def Syntax(children, style=styles.code_container, summary=''):
    code = children
    if not code.startswith('```'):
        code = '```py\n' + code + '\n```'

    if summary:
        return html.Details([
            html.Summary(summary),
            dcc.Markdown(code, style=style)
        ], open=True)
    else:
        return dcc.Markdown(code, style=style)


def Example(example):
    return html.Div(example, className='example-container')
