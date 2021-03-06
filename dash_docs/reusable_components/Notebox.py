import dash
import dash_html_components as html
import dash_core_components as dcc
from dash_docs import styles
from .Markdown import Markdown

def Notebox(content):
    return html.Div(
        children = [
            Markdown(content)
        ],
        style=styles.notebox
    )
