import dash_core_components as dcc
import dash_html_components as html

from tutorial import styles
from textwrap import dedent as s

from tutorial.utils.component_block import ComponentBlock


def generate_code_container(
        component_name,
        library_name, library_short,
        default_id=True,
        description='',
        props=None,
        style=None
):
    '''
    Generates a section for the component specified, including pretty-printed 
    code containing top-level props (not dicts) and style dictionaries.

    :param (str) component_name: The component name in camelcase with the first 
                                 letter also capitalized. 
    :param (str) library_name: Name of the library the component belongs to,
                               with words separated by dashes ('-'). 
    :param (str) library_short: A short name for the library (e.g., "dcc"). 
    :param (bool) default_id: Whether or not to generate an id for the
                              component. Can be useful for custom styling. 
    :param (dict) props: A dictionary of the component's keys and the values 
                         corresponding to those keys. 
    :param (dict) style: A dictionary that determines the styling of the 
                         component, if 'style' is a property of that component.
                         (Will fail if this is not true.) 
    '''
    propString = '\n  '
    if(default_id):
        propString += 'id=\'my-{}-{}\', '.format(
            library_short,
            component_name.lower())

    if props is not None:
        for key in props.keys():
            propString += '{}={}, '.format(key, props[key])

    if style is not None:
        styleString = 'style={\n  '
        for key in style.keys():
            styleString += '  \'{}\': \'{}\', '.format(
                key,
                str(style[key])
            )
        styleString = styleString[:-2]
        styleString += '\n  }, '
        propString += styleString
 
    propString = propString.replace(', ', ',\n  ')

    if(len(propString) > 4): 
        propString = propString[:-4] + '\n'
    else:
        propString = ''

    example_string = '''import {} as {}

{}.{}({})'''.format(library_name.replace('-', '_'),
                    library_short,
                    library_short, 
                    component_name,
                    propString)
    return [

        html.Hr(),

        html.H3(dcc.Link(component_name,
                         href='/{}/{}'.format(
                             library_name,
                             component_name.lower())),
                id=component_name.replace(' ', '-').lower()),
        
        dcc.Markdown(s(description)),
        
        ComponentBlock(
            example_string
        ),

        html.Br(), 
        
        dcc.Link('More {} Examples and Reference'.format(component_name),
                 href='/{}/{}'.format(
                     library_name,
                     component_name.lower()))
    ]


def generate_docs(
        library_name,
        library_short, 
        library_heading,
        component_dict
):
    ''' 
    A function that generates documentation. 
    
    :param (str) library_name: The name of the library, with first letter
                               capitalized.
    :param (str) library_short: A short name for the library, with words
                                separated by dashes ('-'). 
    :param (object) library_heading: An object that contains a description of
                                     the library and its components. Usually
                                     a dcc.Markdown() object.
    ''' 

    layout_children = [library_heading]
    components = list(component_dict.keys())
    components.sort()
    # ensure alphabetical order
    for component in components:
        layout_children += generate_code_container(
            component,
            library_name,
            library_short,
            **component_dict[component]
        )

    return layout_children 

    
