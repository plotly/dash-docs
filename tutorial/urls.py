# -*- coding: utf-8 -*-
import dash_core_components as dcc
import styles

layout = [dcc.Markdown('''
# Multi-Page Apps and URL Support

Dash renders web applications as a "single-page app". This means that
the application does not completely reload when the user navigates the
application, making browsing very fast.

There are two new components that aid page navigation:
`dash_core_components.Location` and `dash_core_components.Link`.

`dash_core_components.Location` represents the location bar in your web browser
through the `pathname` property. Here's a simple example:

'''),

          dcc.SyntaxHighlighter('''import dash
import dash_core_components as dcc
import dash_html_components as html

print(dcc.__version__) # 0.6.0 or above is required

app = dash.Dash()

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),

    # content will be rendered in this element
    html.Div(id='page-content')
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return html.Div([
        html.H3('You are on page {}'.format(pathname))
    ])


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


if __name__ == '__main__':
    app.run_server(debug=True)
''', language='python', customStyle=styles.code_container),

          dcc.Markdown('''
In this example, the callback `display_page` receives the current pathname
(the last part of the URL) of the page. The callback simply displays the
`pathname` on page but it could use the `pathname` to display different
content.

The `Link` element updates the `pathname` of the browser _without refreshing the
page_. If you used a `html.A` element instead, the `pathname` would update but
the page would refresh.

Here is a GIF of what this example looks like. Note how clicking on the `Link`
doesn't refresh the page even though it updates the URL!

![Example of a multi-page Dash app using the Location and Link components](https://github.com/plotly/dash-docs/raw/master/images/url-support.gif)

***

You can modify the example above to display different pages depending on the URL:
'''),

          dcc.SyntaxHighlighter('''import dash
import dash_core_components as dcc
import dash_html_components as html

print(dcc.__version__) # 0.6.0 or above is required

app = dash.Dash()

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
])

page_1_layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(
        id='page-1-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),

])

@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)


page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(
        id='page-2-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])

@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


if __name__ == '__main__':
    app.run_server(debug=True)
''', language='python', customStyle=styles.code_container),

          dcc.Markdown('''![Dash app with multiple pages](https://github.com/plotly/dash-docs/raw/master/images/url-support-pages.gif)

In this example, we're displaying different layouts through the `display_page`
function. A few notes:
- Each page can have interactive elements even though those elements may not
be in the initial view. Dash handles these "dynamically generated" components
gracefully: as they are rendered, they will trigger the
callbacks with their initial values.
- Since we're adding callbacks to elements that don't exist in the app.layout,
Dash will raise an exception to warn us that we might be doing something
wrong.  In this case, we're adding the elements through a callback, so we can
ignore the exception by setting `app.config.suppress_callback_exceptions = True`
- You can modify this example to import the different page's `layout`s in different files.
- This Dash Userguide that you're looking at is itself a multi-page Dash app, using
rendered with these same principles.
'''),

          dcc.Markdown('''***

# Structuring a Multi-Page App

Here's how to structure a multi-page app, where each app is contained in a
separate file.


File structure:
```
- app.py
- index.py
- apps
   |-- __init__.py
   |-- app1.py
   |-- app2.py
```

***

`app.py`
'''),

          dcc.SyntaxHighlighter('''import dash

app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True
''', language='python', customStyle=styles.code_container),

          dcc.Markdown('''
***

`apps/app1.py`
'''),

          dcc.SyntaxHighlighter('''from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

layout = html.Div([
    html.H3('App 1'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-1-display-value'),
    dcc.Link('Go to App 2', href='/apps/app2')
])


@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
''', language='python', customStyle=styles.code_container),

          dcc.Markdown('''
And similarly for other apps
***

`index.py`

`index.py` loads different apps on different urls like this:
'''),

          dcc.SyntaxHighlighter('''
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
from apps import app1, app2


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
         return app1.layout
    elif pathname == '/apps/app2':
         return app2.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
''', language='python', customStyle=styles.code_container)
]
