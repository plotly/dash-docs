import dash_core_components as dcc

from tutorial import styles

layout = [
    dcc.Markdown(
"""
# Project structure
As your Dash app grows, keeping everything in a single app.py quickly becomes a hassle. At some point, it is natural to
break things out into separate files. In a typical Dash app, there are a few 'natural' boundaries along which to divide 
our code, namely:

- app - the Dash app initialization
- data - functions for fetching and preparing data
- layouts - structure of the app
- callbacks - the reactive event handler functions
- routes - optional routing logic for multi-page Dash apps
- utils - other functions, which may be shared between callbacks

This chapter will briefly describe how to separate out your app code into multiple files, for improved maintainability.

## Package initialization
A package architecture is key to allowing Python projects to be spread across files. To tell Python that the Dash app
folder is a package, simply add an empty `__init__.py` file to the project directory.

## Main entrypoint
Each Dash app needs a main entrypoint, which is basically the file you run with `python app.py` in a monolithic Dash app.

In our case, we will fall back to a long-standing convention in web development, and call our entry point `index.py`.
The `index.py` file will be fairly minimal, containing only logic to run the app, e.g.
"""),

    dcc.SyntaxHighlighter("""
# Import the app and server instances
from server import app

# Run the app if this file is called directly
if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8050)

""", customStyle=styles.code_container),

    dcc.Markdown("""
## Server
`server.py` is where we actually define the Dash app instance and attach the app layout. 

    """),

    dcc.SyntaxHighlighter("""
# Required import
from dash import Dash

# Import main layout (e.g. placeholder elements)
from layouts import main_layout

# Create Dash instance
# optionally attach external scripts and stylesheets
app = Dash()

# Attach the main layout
app.layout = main_layout
    """, customStyle=styles.code_container),


    dcc.Markdown("""
## Layouts
Layouts are structural in nature, defining the tree of components to render on the page. For our project structure,
we will define layouts in `layouts.py`.
    """),

    dcc.SyntaxHighlighter("""
# Import Dash Core Components and HTML as needed
import dash_core_components as dcc
import dash_html_components as html

# Define a main layout
main_layout = html.Div(
    children=[
        # Additional HTML or DCC children
    ]
)
""", customStyle=styles.code_container),

dcc.Markdown("""
## Callbacks
Callbacks are functional, responding to user input or other events. We will define callbacks in `callbacks.py`.
    """),

    dcc.SyntaxHighlighter("""
# Import Dash Input and Output
from dash.dependencies import Input, Output

# Import app instance
from server import app

# Create one or more callbacks
@app.callback(Output(...),
               [Input(...)])
def do something(n_intervals):
    pass
)
""", customStyle=styles.code_container),

    dcc.Markdown("""
## Related resources
This chapter is informed and inspired by the following resource(s) and discussion(s):

- [Splitting callback definitions in multiple files](https://community.plot.ly/t/splitting-callback-definitions-in-multiple-files/10583/2)
- [Slapdash](https://github.com/ned2/slapdash) - boilerplate for bootstrapping scalable multi-page Dash applications
    """),
]