import dash_core_components as dcc

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
"""
    ),
]