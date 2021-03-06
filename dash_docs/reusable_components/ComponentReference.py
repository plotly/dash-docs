# -*- coding: utf-8 -*-
import re
import dash_html_components as html
import dash_core_components as dcc
from textwrap import dedent
from dash_docs import tools
from .Markdown import Markdown


def ComponentReference(component_name, lib=dcc):
    component = getattr(lib, component_name)
    component_doc = component.__doc__

    return_div = [
        Markdown(
            """
            > Access this documentation in your Python terminal with:
            > ```python
            > >>> help({}.{})
            > ```
            """.format(
                lib.__name__, component_name
            )
            + """
            > Our recommended IDE for writing Dash apps is Dash Enterprise's
            > [Data Science Workspaces](https://plotly.com/dash/workspaces),
            > which has typeahead support for Dash Component Properties.
            > [Find out if your company is using
            > Dash Enterprise](https://go.plotly.com/company-lookup).
            """
            if not tools.is_in_dash_enterprise()
            else ""
        )
    ]

    docs = component_doc.split("Keyword arguments:")[-1]

    # This check for the old style docstrings built with dash<=1.18.1
    if docs.count("\n\n-") < 2:
        return format_old_style_docstrings(component_doc, return_div)

    # formats code blocks that includes square brackets
    docs = docs.replace("[", "\[").replace("]", "\]")
    verbatim_regex = r"`((\\\[)((.|\n)*?)(\\\]))`"
    docs = re.sub(re.compile(verbatim_regex), r"`[\3]`", docs)

    # format links
    link_regex = r"\\\[([\w\.\-:\s\/]+)\\\]\(([\w\.\-:#\/]+)\)"
    docs = re.sub(re.compile(link_regex), r"[\1](\2)", docs)

    # formats the prop defaults
    prop_optional_default_regex = r"""default (.*)\)"""
    docs = re.sub(re.compile(prop_optional_default_regex), r"default `\1`)", docs)

    # formats the prop type
    prop_type_regex = r"""(\s*- \w+?\s*\()([^;]*);"""
    docs = re.sub(re.compile(prop_type_regex), r"\1*\2*;", docs)

    # formats the prop name on first level only
    prop_name_regex = r"""(\n- )(\w+?) \("""
    docs = re.sub(re.compile(prop_name_regex), r"\1**`\2`** (", docs)

    # formats keys of nested dicts
    nested_prop_name_regex = r"""(\n\s+- )(\w+?) \("""
    docs = re.sub(re.compile(nested_prop_name_regex), r"\1**`\2`** (", docs)

    # removes a level of nesting
    docs = docs.replace("\n-", "\n")

    return_div.append(Markdown(docs))
    return html.Div(return_div, className="reference")


def format_old_style_docstrings(component_doc, return_div):
    """
    This formats the docstring with components built with dash<=1.18.1
    """

    regex = r"""^([^\(]*)\s*\(([^;]*);\s*(.+?)\):\s*(.*?)\s*$"""

    props = component_doc.split("\n-")[1:]

    # sort alphabetically, but keep id at the top
    id_prop = props.pop(0)
    props.sort(key=lambda x: x.strip()[0])
    props = [id_prop] + props

    for prop in props:

        r = re.match(re.compile(regex), prop.replace("\n", " "))

        if r is None:
            return_div.append(Markdown(dedent(prop.replace("\n", " "))))
            continue

        (prop_name, prop_type, prop_optional_default, prop_desc) = r.groups()
        prop_desc = prop_desc.replace("[", "\[").replace("]", "\]")

        verbatim_regex = r"`((\\\[)(.*?)(\\\]))`"

        prop_desc = re.sub(re.compile(verbatim_regex), r"`[\3]`", prop_desc)

        link_regex = r"\\\[([\w\.\-:\/]+)\\\]\(([\w\.\-:#\/]+)\)"

        prop_desc = re.sub(re.compile(link_regex), r"[\1](\2)", prop_desc)

        if "dict containing keys" in prop_desc or "dicts containing keys" in prop_desc:
            regex_dict = r"""(.*?\.* *[\w]* has the following type: (?:[\w\s|]*)dict[s]* containing keys )([\w\s',]*)(\. Those keys have the following types: )(.*)"""
            parsed_dict_desc = re.match(re.compile(regex_dict), prop_desc)
            try:
                top_level_desc = parsed_dict_desc.groups(0)[0]
                top_level_keys = parsed_dict_desc.groups(0)[1]
                top_level_type_preamble = parsed_dict_desc.groups(0)[2]
                key_defs = parsed_dict_desc.groups(0)[3]

                top_level_keys_list = [
                    key.strip().strip("'") for key in top_level_keys.split(",")
                ]
                for key in top_level_keys_list:
                    key_defs = key_defs.replace(
                        "- {}".format(key), "\n- `{}`".format(key), 1
                    )

                top_level_type_preamble = top_level_type_preamble.replace(
                    "Those keys have the following types: ",
                    "Those keys have the following types: \n",
                )
                prop_desc = (
                    top_level_desc
                    + top_level_keys
                    + top_level_type_preamble
                    + "".join(key_defs)
                )

            except AttributeError:
                pass

        defined_default_val = re.search(r"""default (.*)""", prop_optional_default)

        prop_optional = prop_optional_default
        if defined_default_val is not None:
            default_val = defined_default_val.groups(1)[0]
            prop_optional = "default `{}`".format(default_val)

        if prop_type:
            prop_type = "*{}*; ".format(prop_type)
            prop_type = prop_type.replace("|", "*|*")

        return_div.append(
            Markdown(
                """**`{}`** ({}{}): {}""".format(
                    prop_name, prop_type, prop_optional, prop_desc
                )
            )
        )

    return html.Div(return_div, className="reference")
