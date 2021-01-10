# -*- coding: utf-8 -*-
import re
import dash_html_components as html
import dash_core_components as dcc

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

    # formats code blocks that includes square brackets
    docs = docs.replace("[", "\[").replace("]", "\]")
    verbatim_regex = r"`((\\\[)((.|\n)*?)(\\\]))`"
    docs = re.sub(re.compile(verbatim_regex), r"`[\3]`", docs)

    # format links
    link_regex = r"\\\[([\w\.\-:\/]+)\\\]\(([\w\.\-:#\/]+)\)"
    docs = re.sub(re.compile(link_regex), r"[\1](\2)", docs)

    # formats the prop defaults
    prop_optional_default_regex = r"""default (.*)\)"""
    docs = re.sub(re.compile(prop_optional_default_regex), r"default `\1`)", docs)

    # formats the prop type
    prop_type_regex = r"""(\s*- \w+?\s*\()([^;]*);"""
    docs = re.sub(re.compile(prop_type_regex), r"\1*\2*;", docs)

    # formats the prop name
    prop_name_regex = r"""(\n- )(\w+?) \("""
    docs = re.sub(re.compile(prop_name_regex), r"\1**`\2`** (", docs)

    # formats keys of nested dicts
    nested_prop_name_regex = r"""(\n\s+- )(\w+?) \("""
    docs = re.sub(re.compile(nested_prop_name_regex), r"\1`\2` (", docs)

    # formats the prop name in the intro to the nested dict
    intro_prop_regex = r"""(\s*)(\w+?)( has the following type:)"""
    docs = re.sub(re.compile(intro_prop_regex), r"\1`\2`\3", docs)

    # removes a level of nesting
    docs = docs.replace("\n-", "\n")

    return_div.append(Markdown(docs))
    return html.Div(return_div, className="reference")
