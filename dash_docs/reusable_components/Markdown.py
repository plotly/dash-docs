import dash_core_components as dcc
from dash_docs import tools
import re

# Use our own Markdown function so that we can
# use `relpath` for the embedded URLs
def Markdown(children='', **kwargs):
    children = re.sub(
        ']\((\/\S*)\)',
        lambda match: ']({})'.format(tools.relpath(match.groups()[0])),
        children
    )
    # escape the HTML tags presented in the html component docstrings
    children = re.sub(
        '\<(\w+)\>',
        # for some reason, if we do `\<{}\>`, the first slash is shown in the
        # rendered text.
        lambda match: '<{}\> '.format(match.groups()[0]),
        children
    )
    # except when we talk about <template> in the context of dash-table
    # (and likely other workarounds in the future, too!)
    children = children.replace(
        'FormatTemplate.<template\>',
        'FormatTemplate.<template>'
    )
    return dcc.Markdown(
        children=children,
        dangerously_allow_html=True,
        **kwargs
    )
