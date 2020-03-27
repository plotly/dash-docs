# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_core_components as dcc
import re
from dash_docs import reusable_components

def generate_prop_info(component_name, lib=dcc):
    component = getattr(lib, component_name)
    component_doc = component.__doc__

    regex = r'''^([^\(]*)\s*\(([^;]*);\s*(.+?)\):\s*(.*?)\s*$'''

    return_div = [
        reusable_components.Markdown(
            '''
            > Access this documentation in your Python terminal with:
            > ```shell
            > >>> help({}.{})
            > ```
            '''.format(lib.__name__, component_name)
        )
    ]

    props = component_doc.split('\n-')[1:]

    # sort alphabetically, but keep id at the top
    id_prop = props.pop(0)
    props.sort(key=lambda x: x.strip()[0])
    props = [id_prop] + props

    for prop in props:

        r = re.match(
            re.compile(regex),
            prop.replace('\n', ' ')
        )

        if r is None:
            return_div.append(reusable_components.Markdown(prop.replace('\n', ' ')))
            continue

        (prop_name, prop_type, prop_optional_default, prop_desc) = r.groups()
        prop_desc = prop_desc.replace(
            '[', '\[').replace(
                ']', '\]')

        verbatim_regex = r'`((\\\[)(.*?)(\\\]))`'

        prop_desc = re.sub(re.compile(verbatim_regex),
                           r'`[\3]`',
                           prop_desc)

        link_regex = r'\\\[([\w\.\-:\/]+)\\\]\(([\w\.\-:#\/]+)\)'

        prop_desc = re.sub(re.compile(link_regex),
                           r'[\1](\2)',
                           prop_desc)

        if 'dict containing keys' in prop_desc or 'dicts containing keys' in prop_desc:
            regex_dict = r'''(.*?\.* *[\w]* has the following type: (?:[\w\s|]*)dict[s]* containing keys )([\w\s',]*)(\. Those keys have the following types: )(.*)'''
            parsed_dict_desc = re.match(
                re.compile(regex_dict),
                prop_desc
            )
            try:
                top_level_desc = parsed_dict_desc.groups(0)[0]
                top_level_keys = parsed_dict_desc.groups(0)[1]
                top_level_type_preamble = parsed_dict_desc.groups(0)[2]
                key_defs = parsed_dict_desc.groups(0)[3]

                top_level_keys_list = [key.strip().strip('\'')
                                       for key in top_level_keys.split(',')]
                for key in top_level_keys_list:
                    key_defs = key_defs.replace(
                        '- {}'.format(key),
                        '\n- `{}`'.format(key),
                        1
                    )

                top_level_type_preamble = top_level_type_preamble.replace(
                    'Those keys have the following types: ',
                    'Those keys have the following types: \n'
                )
                prop_desc = top_level_desc + \
                    top_level_keys + \
                    top_level_type_preamble + \
                    ''.join(key_defs)

            except AttributeError:
                pass

        defined_default_val = re.search(
            r'''default (.*)''',
            prop_optional_default
        )

        prop_optional = prop_optional_default
        if defined_default_val is not None:
            default_val = defined_default_val.groups(1)[0]
            prop_optional = 'default `{}`'.format(default_val)

        if prop_type:
            prop_type = '*{}*; '.format(prop_type)
            prop_type = prop_type.replace('|', '*|*')

        return_div.append(reusable_components.Markdown(
            '''**`{}`** ({}{}): {}'''.format(
                prop_name,
                prop_type,
                prop_optional,
                prop_desc
            )
        ))

    return html.Div(return_div, className='reference')
