# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

from dash_docs import styles
from dash_docs import tools
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)

layout = html.Div(children=[
    html.H1('Clipboard Examples and Reference'),

    rc.Markdown("""
        The Clipboard component copies text to the 
        browser's clipboard by clicking on a copy icon.    
    """),
    html.H3('Simple Clipboard Example'),
    rc.Markdown("""
        The easiest way to trigger the copy is by using the the `target_id` 
        prop. No callback is required!

        Place dcc.Clipboard() in the layout where you would like the copy
         icon located. Specify the `target_id` of the component with text to copy.
         In this example, the content of the `value` prop of the dcc.Textarea() is copied to the clipboard.    
    """),
    rc.Markdown(
        examples['clipboard_textarea.py'][0],
        style=styles.code_container,
    ),
    html.Div(examples['clipboard_textarea.py'][1], className='example-container'),


    html.H3('Clipboard icon inside a scrollable div'),
    rc.Markdown("""The `style` and `className` can be used to change the design or the position 
    of the copy icon.  This example shows the icon placed in the top right corner of a scrollable div. 
     The next example shows the icon styled like a button.  
   """),

    html.Div(
        examples['clipboard_markdown.py'][1],
        className='example-container',
        style={'overflow': 'hidden', 'padding': '20px'}
    ),

    html.H3('Updating Text in a callback'),
    rc.Markdown("""When `target_id` is not specified, the content of the `text` prop
    is copied to the clipboard.  This works well with components like the DataTable where
    you may want to customized the text in a callback.  In this example, 
    the dataframe is converted to text with pandas `to_string()`.  See the pandas documentation 
        for other formatting options such as including or excluding headers.  
    """
    ),
    rc.Markdown(
        examples['clipboard_table.py'][0],
        style=styles.code_container,
    ),
    html.Div(
        examples['clipboard_table.py'][1],
        className='example-container',
        style={'overflow': 'hidden', 'padding': '20px'}
    ),

    html.H3("Clipboard Properties"),
    rc.ComponentReference('Clipboard')
])
