# -*- coding: utf-8 -*-
from textwrap import dedent

import dash_core_components as dcc
import dash_html_components as html

from tutorial import styles


def Syntax(content):
    return dcc.Markdown(
        '```python  \n' + content.strip() + '  \n```',
        style=styles.code_container
    )


layout = html.Div([
    dcc.Markdown(dedent(
    """
    # Integrating Dash with Existing Web Apps

    This section describes three different approaches to embedding a Dash app
    within an existing web application.

    ## Using an `<iframe>`

    The simplest approach to embedding Dash in an existing web application is to
    include an `<iframe>` element in your HTML whose `src` attribute points
    towards the address of a deployed Dash app. This allows you to place your
    Dash app in a specific location within an existing web page with your
    desired dimensions:""")),
    dcc.Markdown(
    '''
    ```html
    <iframe src="http://localhost:8050" width=700 height=600>
    ```
    '''),
    dcc.Markdown(dedent(
    """
    ## Embedding a Dash app within an Existing Flask App

    As discussed in the [Deployment Chapter](/deployment), Dash uses the Flask
    web framework under the hood. This makes it fairly straightforward to
    embed a Dash app at a specific route of an existing Flask app.

    In the following example, a Dash app is mounted at the `/dash` route (eg
    `http://localhost:8050/dash`) of a Flask app:
    """
    )),
    Syntax(dedent(
    '''
    import flask
    import dash
    import dash_html_components as html

    server = flask.Flask(__name__)

    @server.route('/')
    def index():
        return 'Hello Flask app'

    app = dash.Dash(
        __name__,
        server=server,
        routes_pathname_prefix='/dash/'
    )

    app.layout = html.Div("My Dash app")

    if __name__ == '__main__':
        app.run_server(debug=True)
    '''
    )),
    dcc.Markdown(dedent(
    """
    > **Note**: it is important to set the `name` parameter of the Dash instance
    to the value `__name__`, so that Dash can correctly detect the location of
    any static assets inside an `assets` directory for this Dash app.
    """
    )),
    html.Hr(),
    dcc.Markdown(dedent(
    """
    ## Combining One or More Dash Apps with Existing WSGI Apps

    This approach uses Werkzeug's
    [`DispatcherMiddleware`](http://werkzeug.pocoo.org/docs/latest/middlewares/)
    to combine one or more Dash apps with existing WSGI apps (including
    Flask). It is useful when you want to combine multiple Dash apps or when
    your existing app is a non-Flask WSGI app.

    The following example illustrates this approach by combining two Dash apps
    with a Flask app.
    """
    )),
    dcc.Markdown("`flask_app.py`"),
    Syntax(dedent(
    """
    from flask import Flask

    flask_app = Flask(__name__)

    @flask_app.route('/')
    def index():
        return 'Hello Flask app'
    """
    )),
    html.Hr(),
    dcc.Markdown("`app1.py`"),
    Syntax(dedent(
    """
    import dash
    import dash_html_components as html

    app = dash.Dash(
        __name__,
        requests_pathname_prefix='/app1/'
    )

    app.layout = html.Div("Dash app 1")
    """
    )),
    html.Hr(),
    dcc.Markdown("`app2.py`"),
    Syntax(dedent(
    """
    import dash
    import dash_html_components as html

    app = dash.Dash(
        __name__,
        requests_pathname_prefix='/app2/'
    )

    app.layout = html.Div("Dash app 2")
    """
    )),
    html.Hr(),
    dcc.Markdown("`wsgi.py`"),
    Syntax(dedent(
    """
    from werkzeug.wsgi import DispatcherMiddleware

    from app1 import app as app1
    from app2 import app as app2

    application = DispatcherMiddleware(flask_app, {
        '/app1': app1.server,
        '/app2': app2.server,
    })
    """
    )),
    dcc.Markdown(dedent(
    """
    In this example, the Flask app has been mounted at `/` and the two Dash apps
    have been mounted at `/app1` and `/app2`. In this approach, we do not pass
    in a Flask server to the Dash apps, but let them create their own, which the
    `DispatcherMiddleware` routes requests to based on the prefix of the
    incoming requests. Within each Dash app, `requests_pathname_prefix` must be
    specified as the app's mount point, in order to match the route prefix
    set by the `DispatcherMiddleware`.

    Note that the `application` object in `wsgi.py` is of type
    `werkzeug.wsgi.DispatcherMiddleware`, which does not have a `run`
    method. This can be run as a WSGI app like so:
    """
    )),
    Syntax("$ gunicorn wsgi:application"),
    dcc.Markdown(dedent(
    """
    Alternatively, you can use the Werkzeug development server (which is not
    suitable for production) to run the app:

    `run.py`
    """
    )),
    Syntax(dedent(
    """
    from werkzeug.wsgi import DispatcherMiddleware
    from werkzeug.serving import run_simple

    from app1 import app as app1
    from app2 import app as app2

    application = DispatcherMiddleware(flask_app, {
        '/app1': app1.server,
        '/app2': app2.server,
    })

    if __name__ == '__main__':
        run_simple('localhost', 8050, application)
    """
    )),
    dcc.Markdown(dedent(
    """
    If you need access to the Dash development tools when using this approach
    (whether running with a WSGI server, or using the Werkzeug development
    server) you must invoke them manually for each Dash app. The following lines
    can be added before the initialisation of the `DispatcherMiddleware` to do this:
    """
    )),
    Syntax(dedent(
    """
    app1.enable_dev_tools(debug=True)
    app2.enable_dev_tools(debug=True)
    """
    )),
    dcc.Markdown(dedent(
    """
    > **Note:** debug mode should not be enabled in production. When using debug
        mode with Gunicorn, the `--reload` command line flag is required for hot
        reloading to work.

    In this example, the existing app being combined with two Dash apps is a
    Flask app, however this approach enables the combination of any web
    application implementing the [WSGI
    specification](https://wsgi.readthedocs.io). A list of WSGI web frameworks
    can be found in the [WSGI
    documentation](https://wsgi.readthedocs.io/en/latest/frameworks.html) with
    one or more Dash apps.
    """
    )),
    ])
