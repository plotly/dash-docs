import dash_core_components as dcc
from dash_docs import tools
import re

def replace_relative_links(children):
    children = re.sub(
        ']\((\/\S*)\)',
        lambda match: ']({})'.format(tools.relpath(match.groups()[0])),
        children
    )
    children = re.sub(
        'href="(/\S*)"',
        lambda match: 'href="{}"'.format(tools.relpath(match.groups()[0])),
        children
    )
    return children

# Use our own Markdown function so that we can
# use `relpath` for the embedded URLs
def Markdown(children='', **kwargs):
    children = replace_relative_links(children)
    if kwargs.pop('escape_tags', False) and 'dccLink' in children:
        # escape the HTML tags presented in the html component docstrings
        # note that if these tags are within `backticks`, then we don't need
        # to escape. so, let the caller determine whether or not to escape a
        # section.
        children = re.sub(
            '\<(\w+)\>',
            # for some reason, if we do `\<{}\>`, the first slash is shown in the
            # rendered text.
            lambda match: '<{}\> '.format(match.groups()[0]),
            children
        )
    return dcc.Markdown(
        children=children,
        dangerously_allow_html=('dccLink' in children),
        **kwargs
    )
