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

## Main entrypoint
Each Dash app needs a main entrypoint, which is basically the file you run with `python app.py` in a monolithic Dash app.

In our case, we will fall back to a long-standing convention in web development, and call our entry point `index.py`.
The `index.py` file will be fairly minimal, containing only logic to run the app, e.g.

```py
# Import the app and server instances
from server import app, server

# Optionally set the app title
app.title = 'My Dash app'

# Optionally override the app basic HTML structure
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta
            name="description"
            content="My Dash app is great!"
        >
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
        </footer>
    </body>
</html>
'''

# Run the app if this file is called directly
if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8050)

```

## Related resources
This chapter is informed and inspired by the following resource(s) and discussion(s):

- [Splitting callback definitions in multiple files](https://community.plot.ly/t/splitting-callback-definitions-in-multiple-files/10583/2)
- [Slapdash](https://github.com/ned2/slapdash) - boilerplate for bootstrapping scalable multi-page Dash applications
"""
    ),
]