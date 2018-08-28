import dash_core_components as dcc
import dash_html_components as html

import styles


def Syntax(children,
           language='python',
           style=styles.code_container,
           summary=''):
    if summary:
        return html.Details([
            html.Summary(summary),
            dcc.SyntaxHighlighter(
                children,
                language=language,
                customStyle=style
            )
        ], open=True)
    else:
        return dcc.SyntaxHighlighter(
            children,
            language=language,
            customStyle=style
        )


def Example(example):
    return html.Div(example, className='example-container')
