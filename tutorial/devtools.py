from textwrap import dedent as d

import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([
    dcc.Markdown(d('''
    # Dash Dev Tools

    Dash Dev Tools is an initiative to make debugging and developing Dash apps more pleasant. This initiative was [sponsored by an organization](http://plot.ly/products/consulting-and-oem/) and you can see our work in our [GitHub project](https://github.com/orgs/plotly/projects/3).

    *dev_tools features are activated by default when you run the app with `app.run_server(debug=True)`*

    ## Hot Reloading

    **New in dash 0.30.0 and dash-renderer 0.15.0**

    By default, Dash includes "hot-reloading". This means that Dash will automatically refresh your browser when you make a change in your Python or CSS code.

    Hot reloading works by running a "file watcher" that examines your working directory to check for changes. When a change is detected, Dash reloads your application in an efficient way automatically. A few notes:
    - Hot reloading is triggered when you _save_ a file.
    - Dash examines the files in your working directory.
    - CSS files are automatically "watched" by examining the `assets/` folder. [Learn more about css](/external-resources)
    - If only CSS changed, then Dash will only refresh that CSS file.
    - When your Python code has changed, Dash will re-run the entire file and then refresh the application in the browser.
    - If your application initialization is slow, then you might want to consider how to save certain initialization steps to file. For example, if your app initialization downloads a static file from a remote service, perhaps you could include it locally.
    - Hot reloading will not save the application's _state_. For example, if you've selected some items in a dropdown, then that item will be cleared on hot-reload.
    - Hot reloading is configurable through a set of parameters. See the Reference section at the end of this page.

    ## Serving the dev bundles

    Component library bundles are minified by default, if you encounter a front-end error in your code, the variables names will be mangled.
    By serving the dev bundles, you will get the full names.

    ## Dev Tools UI

    **New in dash 0.42.0 and dash-renderer 0.23.0**

    The new Dev Tools UI provides a simple interface, which consolidates both frontend and backend errors into an "error popup" at the top-right corner.
    This could reduce your context switch among *terminal*, *code editor*, *browser* and *browser debug console* while developping a dash app.

    To better understand the interaction of callbacks, we visualize the callback function definitions into
    a DAG (Directed Acyclic Graph). A **Callback Graph** icon is available after clicking the debug icon at the bottom-right corner.

    As upgrading to React 16 since dash-renderer *0.22.0*, we also leverage the new
    [Error Handling](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html) feature so that all
    Dash React Components get free [Component Props check](https://reactjs.org/docs/typechecking-with-proptypes.html)
    from *dash-renderer*.

    Note: You can disable the check by setting `dev_tools_props_check=False`. But we strongly recommended to fix the props errors:

    > As of React 16, errors that were not caught by any error boundary will result in
    > unmounting of the whole React component tree.

    ## Reference

    The full set of dev tools parameters are included in `app.run_server` or `app.enable_dev_tools`:

    - `debug`, bool, activate all the dev tools.
    - `dev_tools_ui`, bool, set to `False` to explicitly disable dev tools UI in debugger mode (defualt=True)
    - `dev_tools_props_check`, bool, set to `False` to explicitly disable component props validation (default=True)
    - `dev_tools_hot_reload`, bool, set to `True` to enable hot reload (default=False).
    - `dev_tools_hot_reload_interval`, int, interval in millisecond at which the renderer will request the reload hash (default=3000).
    - `dev_tools_hot_reload_watch_interval`, float, delay in seconds between each walk of the assets folder to detect file changes. (default=0.5 seconds)
    - `dev_tools_hot_reload_max_retry`, int, number of times the reloader is allowed to fail before stopping and sending an alert. (default=8)
    - `dev_tools_silence_routes_logging`, bool, remove the routes access logging from the console.
    - `dev_tools_serve_dev_bundles`, bool, serve the dev bundles.

    ### Settings with environment variables

    All the `dev_tools` variables can be set with environment variables, just replace the `dev_tools_` with `dash_` and convert to uppercase.
    This allows you to have different run configs without changing the code.

    Linux/macOS:

    `export DASH_HOT_RELOAD=false`

    Windows:

    `set DASH_DEBUG=true`
    '''))
])
