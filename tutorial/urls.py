# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from tutorial import styles

layout = [dcc.Markdown('''
    # Multi-Page Apps and URL Support

    Dash renders web applications as a "single-page app". This means that
    the application does not completely reload when the user navigates the
    application, making browsing very fast.

    There are two new components that aid page navigation:
    [`dash_core_components.Location`](/dash-core-components/location) and `dash_core_components.Link`.

    `dash_core_components.Location` represents the location bar in your web browser
    through the `pathname` property. Here's a simple example:

    '''),

    dcc.Markdown('''
    ```python
    import dash
    import dash_core_components as dcc
    import dash_html_components as html

    print(dcc.__version__) # 0.6.0 or above is required

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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


    if __name__ == '__main__':
        app.run_server(debug=True)
    ```
    ''', style=styles.code_container),

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

    ![Example of a multi-page Dash app using the Location and Link components](https://raw.githubusercontent.com/plotly/dash-docs/master/images/url-support.gif)

    ***

    You can modify the example above to display different pages depending on the URL:
    '''),

    dcc.Markdown('''
    ```python
    import dash
    import dash_core_components as dcc
    import dash_html_components as html

    print(dcc.__version__) # 0.6.0 or above is required

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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


    if __name__ == '__main__':
        app.run_server(debug=True)
    ```
    ''', style=styles.code_container),

    dcc.Markdown('''
    ![Dash app with multiple pages](https://raw.githubusercontent.com/plotly/dash-docs/master/images/url-support-pages.gif)

    In this example, we're displaying different layouts through the `display_page`
    function. A few notes:
    - Each page can have interactive elements even though those elements may not
    be in the initial view. Dash handles these "dynamically generated" components
    gracefully: as they are rendered, they will trigger the
    callbacks with their initial values.
    - Since we're adding callbacks to elements that don't exist in the app.layout,
    Dash will raise an exception to warn us that we might be doing something
    wrong.  In this case, we're adding the elements through a callback, so we can
    ignore the exception by setting `app.config.suppress_callback_exceptions = True`.
    It is also possible to do this without suppressing callback exceptions. See the example
    below for details.
    - You can modify this example to import the different page's `layout`s in different files.
    - This Dash Userguide that you're looking at is itself a multi-page Dash app, using
    these same principles.
    '''),

    dcc.Markdown('''
    ***

    ## Dynamically Create a Layout for Multi-Page App Validation

    Dash applies validation to your callbacks, which performs checks such as
    validating the types of callback arguments and checking to see whether the
    specified Input and Output components actually have the specified properties.

    For full validation, all components within your callback must therefore appear
    in the initial layout of your app, and you will see an error if they do not.
    However, in the case of more complex Dash apps that involve dynamic modification
    of the layout (such as multi-page apps), not every component appearing in your
    callbacks will be included in the initial layout.

    Since this validation is done before flask has any request context, you can create
    a layout function that checks `flask.has_request_context()` and returns a complete
    layout to the validator if there is no request context and returns the incomplete
    index layout otherwise.
    '''),
    dcc.Markdown('''
    ```py
    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output, State

    import flask

    app = dash.Dash(
        __name__,
        external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
    )

    url_bar_and_content_div = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

    layout_index = html.Div([
        dcc.Link('Navigate to "/page-1"', href='/page-1'),
        html.Br(),
        dcc.Link('Navigate to "/page-2"', href='/page-2'),
    ])

    layout_page_1 = html.Div([
        html.H2('Page 1'),
        dcc.Input(id='input-1-state', type='text', value='Montreal'),
        dcc.Input(id='input-2-state', type='text', value='Canada'),
        html.Button(id='submit-button', n_clicks=0, children='Submit'),
        html.Div(id='output-state'),
        html.Br(),
        dcc.Link('Navigate to "/"', href='/'),
        html.Br(),
        dcc.Link('Navigate to "/page-2"', href='/page-2'),
    ])

    layout_page_2 = html.Div([
        html.H2('Page 2'),
        dcc.Dropdown(
            id='page-2-dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA'
        ),
        html.Div(id='page-2-display-value'),
        html.Br(),
        dcc.Link('Navigate to "/"', href='/'),
        html.Br(),
        dcc.Link('Navigate to "/page-1"', href='/page-1'),
    ])


    def serve_layout():
        if flask.has_request_context():
            return url_bar_and_content_div
        return html.Div([
            url_bar_and_content_div,
            layout_index,
            layout_page_1,
            layout_page_2,
        ])


    app.layout = serve_layout


    # Index callbacks
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == "/page-1":
            return layout_page_1
        elif pathname == "/page-2":
            return layout_page_2
        else:
            return layout_index


    # Page 1 callbacks
    @app.callback(Output('output-state', 'children'),
                  [Input('submit-button', 'n_clicks')],
                  [State('input-1-state', 'value'),
                   State('input-2-state', 'value')])
    def update_output(n_clicks, input1, input2):
        return ('The Button has been pressed {} times,'
                'Input 1 is "{}",'
                'and Input 2 is "{}"').format(n_clicks, input1, input2)


    # Page 2 callbacks
    @app.callback(Output('page-2-display-value', 'children'),
                  [Input('page-2-dropdown', 'value')])
    def display_value(value):
        print('display_value')
        return 'You have selected "{}"'.format(value)


    if __name__ == '__main__':
        app.run_server(debug=True)
    ```
    ''', style={'borderLeft': 'thin solid lightgrey'}),

    dcc.Markdown('''
    ***

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

    dcc.Markdown('''
    ```py
    import dash

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    server = app.server
    app.config.suppress_callback_exceptions = True
    ```
    ''', style=styles.code_container),

    dcc.Markdown('''
    ***

    `apps/app1.py`
    '''),

    dcc.Markdown('''
    ```py
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output

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
    ```
    ''', style=styles.code_container),

    dcc.Markdown('''
    And similarly for other apps
    ***

    `index.py`

    `index.py` loads different apps on different urls like this:
    '''),

    dcc.Markdown('''
    ```py
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output

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
    ```
    ''', style=styles.code_container),
    dcc.Markdown('''
    ***

    Alternatively, you may prefer a flat project layout with callbacks and layouts
    separated into different files:

    ```
    - app.py
    - index.py
    - callbacks.py
    - layouts.py
    ```

    ***

    `app.py`
    '''),
    dcc.Markdown('''
    ```py
    import dash

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    server = app.server
    app.config.suppress_callback_exceptions = True
    ```
    ''', style=styles.code_container),

    dcc.Markdown('''
    ***

    `callbacks.py`
    '''),
    dcc.Markdown('''
    ```py
    from dash.dependencies import Input, Output

    from app import app

    @app.callback(
        Output('app-1-display-value', 'children'),
        [Input('app-1-dropdown', 'value')])
    def display_value(value):
        return 'You have selected "{}"'.format(value)

    @app.callback(
        Output('app-2-display-value', 'children'),
        [Input('app-2-dropdown', 'value')])
    def display_value(value):
        return 'You have selected "{}"'.format(value)
    ```
    ''', style=styles.code_container),

    dcc.Markdown('''
    ***

    `layouts.py`
    '''),
    dcc.Markdown('''
    ```py
    import dash_core_components as dcc
    import dash_html_components as html

    layout1 = html.Div([
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

    layout2 = html.Div([
        html.H3('App 2'),
        dcc.Dropdown(
            id='app-2-dropdown',
            options=[
                {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                    'NYC', 'MTL', 'LA'
                ]
            ]
        ),
        html.Div(id='app-2-display-value'),
        dcc.Link('Go to App 1', href='/apps/app1')
    ])
    ```
    ''', style=styles.code_container),

    dcc.Markdown('''
    ***

    `index.py`
    '''),
    dcc.Markdown('''
    ```python
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output

    from app import app
    from layouts import layout1, layout2
    import callbacks

    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/apps/app1':
             return layout1
        elif pathname == '/apps/app2':
             return layout2
        else:
            return '404'

    if __name__ == '__main__':
        app.run_server(debug=True)
    ```
    ''', style=styles.code_container),

    dcc.Markdown('''
    ***

    It is worth noting that in both of these project structures, the Dash instance
    is defined in a separate `app.py`, while the entry point for running the app is
    `index.py`. This separation is required to avoid circular imports: the files
    containing the callback definitions require access to the Dash `app` instance
    however if this were imported from `index.py`, the initial loading of `index.py`
    would ultimately require itself to be already imported, which cannot be
    satisfied.
    '''),
]
