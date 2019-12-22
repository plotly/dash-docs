# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_auth
from tutorial import styles

layout = html.Div([
    dcc.Markdown('''
    # Authentication

    Authentication for dash apps is provided through a separate
    [`dash-auth`](https://github.com/plotly/dash-auth) package.

    `dash-auth` provides two methods of authentication:
    **HTTP Basic Auth** and **Plotly OAuth**.

    HTTP Basic Auth is one of the simplest forms of authentication on the web.
    As a Dash developer, you hardcode a set of usernames and passwords in your
    code and send those usernames and passwords to your viewers.
    There are a few limitations to HTTP Basic Auth:
    - Users can not log out of applications
    - You are responsible for sending the usernames and passwords
      to your viewers over a secure channel
    - Your viewers can not create their own account and cannot change their
      password
    - You are responsible for safely storing the username and password pairs in
      your code.

    Plotly OAuth provides authentication through your online Plotly account
    or through your company's [Plotly Enterprise server](https://plot.ly/products/on-premise).
    As a Dash developer, this requires a paid Plotly subscription.
    Here's where you can [subscribe to Plotly Cloud](https://plot.ly/products/cloud),
    and here's where you can
    [contact us about Plotly Enterprise](https://plotly.typeform.com/to/seG7Vb).
    The viewers of your app will need a Plotly account but they do not need to
    upgrade to a paid subscription.

    Plotly OAuth allows you to share your apps with other users who have Plotly
    accounts. With Plotly Enterprise, this includes sharing apps through
    the integrated LDAP system. Apps that you have saved will appear in your
    list of files at [https://plot.ly/organize](https://plot.ly/organize)
    and you can manage the permissions of the apps there. Viewers create and
    manage their own accounts.

    '''.replace('    ', '')),

    dcc.Markdown('''
    ## Basic Auth Example

    Logging in through Basic Auth looks like this:
    '''.replace('    ', '')),

    html.Img(
        src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/basic-auth.gif',
        alt='Dash Basic Auth Example',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }),

    dcc.Markdown('''
    Installation:
    '''.replace('    ', '')),

    dcc.Markdown('''
    ```shell
    pip install dash=={}
    pip install dash-auth=={}
    ```
    '''.replace('    ', '').format(
        dash.__version__,
        dash_auth.__version__
    ), style=styles.code_container),

    dcc.Markdown('''
    Example Code:
    '''.replace('    ', '')),

    dcc.Markdown('''
    ```python
    import dash
    import dash_auth
    import dash_core_components as dcc
    import dash_html_components as html
    import plotly

    # Keep this out of source code repository - save in a file or a database
    VALID_USERNAME_PASSWORD_PAIRS = {
        'hello': 'world'
    }

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    auth = dash_auth.BasicAuth(
        app,
        VALID_USERNAME_PASSWORD_PAIRS
    )

    app.layout = html.Div([
        html.H1('Welcome to the app'),
        html.H3('You are successfully authorized'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in ['A', 'B']],
            value='A'
        ),
        dcc.Graph(id='graph')
    ], className='container')

    @app.callback(
        dash.dependencies.Output('graph', 'figure'),
        [dash.dependencies.Input('dropdown', 'value')])
    def update_graph(dropdown_value):
        return {
            'layout': {
                'title': 'Graph of {}'.format(dropdown_value),
                'margin': {
                    'l': 20,
                    'b': 20,
                    'r': 10,
                    't': 60
                }
            },
            'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}]
        }

    if __name__ == '__main__':
        app.run_server(debug=True)
    ```
    ''', style=styles.code_container),

    dcc.Markdown('''
    ## Plotly OAuth Example

    Logging in through Plotly OAuth looks like this:
    '''.replace('   ', '')),

    html.Img(
        src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/plotly-auth.gif',
        alt='Dash Plotly OAuth Example',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }),

    dcc.Markdown('''
    Installation:
    '''.replace('    ', '')),

    dcc.Markdown('''
    ```shell
        pip install dash=={}
        pip install dash-auth=={}
    ```
    '''.replace('    ', '').format(
        dash.__version__,
        dash_auth.__version__
    ), style=styles.code_container),

    dcc.Markdown('''
    Example Code:
    '''.replace('    ', '')),

    dcc.Markdown('''
    ```python
    import dash
    import dash_auth
    import dash_core_components as dcc
    import dash_html_components as html
    import plotly


    # Modify these variables with your own info
    APP_NAME = 'Dash Authentication Sample App'
    APP_URL = 'https://my-dash-app.herokuapps.com'

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    auth = dash_auth.PlotlyAuth(
        app,
        APP_NAME,
        'private',
        APP_URL
    )

    app.layout = html.Div([
        html.H1('Welcome to the app'),
        html.H3('You are successfully authorized'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in ['A', 'B']],
            value='A'
        ),
        dcc.Graph(id='graph')
    ], className='container')

    @app.callback(
        dash.dependencies.Output('graph', 'figure'),
        [dash.dependencies.Input('dropdown', 'value')])
    def update_graph(dropdown_value):
        return {
            'layout': {
                'title': 'Graph of {}'.format(dropdown_value),
                'margin': {
                    'l': 20,
                    'b': 20,
                    'r': 10,
                    't': 60
                }
            },
            'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}]
        }

    if __name__ == '__main__':
        app.run_server(debug=True)
    ```
    ''', style=styles.code_container),

    dcc.Markdown('''
    ## Methods on PlotlyAuth Objects


    With Plotly OAuth, it is possible to create create cookies that store information
    related to a user. In the example below we use the `@auth.is_authorized_hook` and
    `auth.set_user_data` to create a cookie containing an object associated with
    their account and then we determine whether they can view the graph by checking their
    permissions in that cookie using `auth.get_user_data`.

    Finally, we can logout the user by clearing the cookies. To do so, you can create a
    logout button and insert it in the layout or use `auth.logout()` in a callback.

    Plotly Auth uses the environment variables `PLOTLY_USERNAME` and `PLOTLY_API_KEY`.
    You can find your username and API key at [https://plot.ly/settings/api](https://plot.ly/settings/api) or,
    if you are using [Dash Deployment Server](https://plotly/dash/pricing), at https://your-plotly-server.com/settings/api.

    You can set these variables directly in your code with:
    '''.replace('   ', '')),

    dcc.Markdown(
        '''
        ```python
        import os

        os.environ['PLOTLY_USERNAME'] = 'your-username'
        os.environ['PLOTLY_API_KEY'] = 'your-api-key'
        ```
        '''.replace('   ', ''),
        style=styles.code_container),

    dcc.Markdown('''
    or, if you are using [Dash Deployment Server, you can keep your environment variables secret (view the docs)](https://dash.plot.ly/dash-deployment-server/environment-variables).

    '''.replace('   ', '')),

    html.Img(
        src='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/dash-auth-user-data.gif',
        alt='Dash Plotly OAuth User Data and Logout',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }),

    dcc.Markdown('''
    Installation:
    '''.replace('    ', '')),

    dcc.Markdown('''
    ```shell
        pip install dash=={}  # The core dash backend
        pip install dash-auth=={}  # Dash Auth components
    ```
    '''.replace('    ', '').format(
        dash.__version__,
        dash_auth.__version__,
    ), style=styles.code_container),

    dcc.Markdown('''
    Example Code:
    '''.replace('    ', '')),

    dcc.Markdown('''
    ```
    import dash
    import dash_auth
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Output, Input

    import os
    # Modify these variables with your own info
    APP_NAME = 'Dash Authentication Sample App'
    APP_URL = 'http://127.0.0.1:8050/'


    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    auth = dash_auth.PlotlyAuth(
        app,
        APP_NAME,
        'public',
        APP_URL
    )

    app.layout = html.Div([
        html.H1('Welcome to the app', id='title'),
        html.Div(id='authorized'),
        html.Button('View Graph', id='btn'),
        dcc.Graph(id='graph', figure={
            'layout': {
                'title': 'Private Graph',
                'margin': {
                    'l': 20,
                    'b': 20,
                    'r': 10,
                    't': 60
                }
            },
            'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}]
        }, style={'display': 'none'}),
        auth.create_logout_button(
            label='Sign out',
            redirect_to='https://plot.ly')],
         className='container')


    @app.callback(Output('title', 'children'), [Input('title', 'id')])
    def give_name(title):
        username = auth.get_username()
        return 'Welcome to the app, {}'.format(username)


    @auth.is_authorized_hook
    def is_authorized(data):
        active = data.get('is_active')
        if active:
            auth.set_user_data({'graph_1': True})
        return active

    @app.callback(Output('authorized', 'children'), [Input('btn', 'n_clicks')])
    def check_perms(n_clicks):
        if n_clicks:
            perms = auth.get_user_data()
            perm_view_graph = perms.get('graph_1')
            if not perm_view_graph:
                return 'You are not authorized to view this content'
            else:
                return 'You are authorized!'


    @app.callback(Output('graph', 'style'), [Input('btn', 'n_clicks')])
    def check_perms_graph_update(n_clicks):
        if n_clicks:
            perms = auth.get_user_data()
            perm_view_graph = perms.get('graph_1')
            if perm_view_graph:
                return {}
            else:
                return {'display': 'none'}
        else:
            return {'display': 'none'}


    if __name__ == '__main__':
        app.run_server(debug=True)
    ```
    ''', style=styles.code_container)
])
