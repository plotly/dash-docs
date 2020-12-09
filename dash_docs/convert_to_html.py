"""
HTML regex, from Regex Cookbook 2nd edition
https://learning.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch09s02.html
"""
import re
import textwrap
import sys

import dash_core_components as dcc
import dash_html_components as html
from dash.development.base_component import Component

html_tags = [tag for tag in dir(html) if tag[0].isupper()] + ['menu']

tag_string = '|'.join(sorted(html_tags, key=len, reverse=True))

html_tag_regex = re.compile(
                 """(?i)
                 <
                 /?                  # Permit closing tags
                 ([A-Za-z][^\s>/]*)  # Capture the tag name to backreference 1
                 (?:                 # Attribute value branch:
                    = \s*            #   Signals the start of an attribute value
                    (?: "[^"]*"      #   Double-quoted attribute value
                    | '[^']*'        #   Single-quoted attribute value
                    | [^\s>]+        #   Unquoted attribute value
                    )
                 |                   # Non-attribute-value branch:
                   [^>]              #   Character outside of an attribute value
                   )*
                   (?:>|$)           # End of the tag or string
                 """, re.VERBOSE)


empty_tags = ['area', 'base', 'basefont', 'br', 'col', 'embed', 'frame',
              'hr', 'img', 'input', 'isindex', 'keygen', 'link',
              'meta', 'param', 'source', 'track', 'wbr']

# boolean attributes that don't take a value (their presence is enough)
bool_html_attrs = ['async', 'autofocus', 'autoplay', 'checked',
                   'controls', 'default', 'defer', 'disabled',
                   'formNoValidate', 'frameborder', 'hidden', 'ismap',
                   'itemscope', 'loop', 'multiple', 'muted', 'nomodule',
                   'novalidate', 'open', 'readonly', 'required', 'reversed',
                   'scoped', 'selected', 'typemustmatch']

list_tags = ['ul', 'ol', 'dl']

md_extensions = ('abbr', 'admonition', 'attr_list', 'def_list', 'fenced_code',
                 'footnotes', 'meta', 'md_in_html', 'nl2br', 'sane_lists',
                 'smarty', 'toc', 'tables')


def _translate_attrib(attrib):
    attrib_map = {
        'className': 'class',
        'classname': 'class',
        True: 'true',
        'True': 'true',
        False: 'false',
        'False': 'false',
    }
    if isinstance(attrib, (str, bool, int)) and attrib in attrib_map:
        return attrib_map[attrib]
    return attrib


def _style_to_attrib(style_dict):
    attrib_str = [':'.join([k, str(v)]) for k, v in style_dict.items()]
    attrib_str = '; '.join(attrib_str)
    return '"' + attrib_str + '"'


def dcc_to_html(component):
    component_dict = component.to_plotly_json()

    div = html.Div()
    dcc_type = component_dict['type']
    # e.g: ssr-dash-core-components-graph
    dcc_type = '-'.join(['ssr'] + component_dict['namespace'].split('_') + [dcc_type]).lower()
    div.className = dcc_type

    for key, val in component_dict['props'].items():
        if key == 'className':
            join = [val, 'ssr', ]
            div.className = val + '-' + dcc_type
        if key == 'id':
            div.id = val
        if key == 'style':
            div.style = val
    if component_dict['type'] == 'Markdown':
        div.children = markdown_to_html(component_dict['props']['children'])
    if component_dict['type'] != 'Markdown':
        if 'style' in div.to_plotly_json()['props']:
            if 'height' not in div.style:
                div.style['height'] = '50px' if component_dict['type'] \
                                                not in ['Graph', 'DataTable'] else '300px'
        else:
            div.style = {'height': '50px' if component_dict['type'] not in ['Graph', 'DataTable'] else '300px'}
    return div


def convert_to_html(component):
    if component is None:
        return ''
    if not isinstance(component, Component):
        # likely a str, int, float
        return str(component)
    component_dict = component.to_plotly_json()
    if component_dict['type'] == 'Link':
        component_dict['namespace'] = 'dash_html_components'
        component_dict['type'] = 'A'

    if component_dict['namespace'] != 'dash_html_components':
        component = dcc_to_html(component)
        component_dict = component.to_plotly_json()
    tag = component_dict['type'].lower()
    attrib_str = ['='.join([_translate_attrib(k).lower(),
                            '"{}"'.format(_translate_attrib(v))])
                  for k, v in component_dict['props'].items()
                  if _translate_attrib(k).lower()
                  not in ['style', 'children'] + bool_html_attrs]
    attrib_str = ' '.join(attrib_str)
    bool_str, style_str = '', ''
    bool_attrs = []
    for bool_attr in component_dict['props']:
        if _translate_attrib(bool_attr).lower() in bool_html_attrs:
            if bool(component_dict['props'][bool_attr]):
                bool_attrs.append(_translate_attrib(bool_attr).lower())
        bool_str = ' '.join(bool_attrs)
    if 'style' in component_dict['props']:
        style_str = 'style=' + _style_to_attrib(component_dict['props']['style'])
    attrib_str = ' '.join([attrib_str, style_str, bool_str]).strip()
    initial_indent = 0

    comp_children = component_dict['props'].get('children', None)
    if comp_children:
        if isinstance(comp_children, (tuple, list)):
            children = '\n' + '\n'.join([re.sub('^', '\g<0>' + (' ' * i if tag not in list_tags else ' ' * 2),
                                            convert_to_html(child))
                                            for i, child in enumerate(comp_children)])
        else:
            children = convert_to_html(comp_children)
    else:
        # e.g. html.Img doesn't have any children
        children = ''

    initial_indent += 2
    closing_tag = '\n</{}>'.format(tag) if tag not in empty_tags else ''
    attrib_str = ' ' + attrib_str if attrib_str else ''
    return '<{}{}>{}{}'.format(tag, attrib_str, children, closing_tag)


def _dccLink_to_a_href(text):
    dcclink_regex = re.compile('(?ms)<dccLink .*?/>')
    href_regex = re.compile('(?ms)<dccLink .*?href="(.*?)".*?/>')
    children_regex = re.compile('(?ms)<dccLink .*?children="(.*?)".*?/>')

    replacements = []
    hrefs = re.findall(href_regex, text)
    children = re.findall(children_regex, text)
    for child, href in zip(children, hrefs):
        replacements.append('[{}]({})'.format(child, href))
    # split by <dccLink .* /> then stitch with `replacements`
    converted = ''.join([''.join(x)
                         for x in zip(re.split(dcclink_regex, text),
                                      replacements + [''])])
    return converted


def _convert_blockquotes(text):
    """Convert <blockquote>.*?</blockquote> to `> `."""
    return re.sub('(?ms).*<blockquote>\n\s{,4}(.*?)</blockquote>.*',
                  '> \g<1>', str(text))


def markdown_to_html(md_text, extensions=md_extensions):
    """Convert ``md_text`` to HTML string.
    To enable/disable ``extensions`` simply add/remove from the list.
    Please see the documentation for details:
    https://python-markdown.github.io/extensions/
    """
    # markdown isn't supported in Python 2, so protect the import
    # we don't actually deploy the docs on Python 2, we're
    # just running some tests, so the SSR functionality doesn't
    # need to work
    if sys.version_info < (3, 5):
        return md_text
    import markdown
    convert_blockquotes = _convert_blockquotes(md_text)
    convert_dccLinks = _dccLink_to_a_href(convert_blockquotes)
    escape_html = html_tag_regex.sub('&lt;\g<1>&gt;', convert_dccLinks)
    # convert http://example.com to <a href="http://example.com">http://example.com</a>
    link_standalone_urls = re.sub('(\s|\n|^)(https?://.*?)($|\s)',
                                  '\g<1><a href="\g<2>">\g<2></a>\g<3>',
                                  escape_html)
    return markdown.markdown(textwrap.dedent(link_standalone_urls),
                             extensions=extensions)
