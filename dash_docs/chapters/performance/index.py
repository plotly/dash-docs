import dash_core_components as dcc
import dash_html_components as html
from dash_docs import tools
from dash_docs import reusable_components as rc


layout = html.Div(children=[
    rc.Markdown('''# Performance

This chapter contains several recommendations for improving the performance
of your dash apps.

The main performance limitation of dash apps is likely the callbacks in
the application code itself. If you can speed up your callbacks, your app
will feel snappier.

***

## Memoization



Since Dash's callbacks are functional in nature (they don't contain any state),
it's easy to add memoization caching. Memoization stores the results of a
function after it is called and re-uses the result if the function is called
with the same arguments.

<blockquote>
For a simple example of using memoization in a Dash app to improve
performance, see the "Improving performance with memoization" section
in the <dccLink href="/advanced-callbacks" children="advanced callbacks"/>
chapter.
</blockquote>

Dash apps are frequently deployed across multiple processes or threads.
In these cases, each process or thread contains its own memory, it doesn't
share memory across instances. This means that if we were to use `lru_cache`,
our cached results might not be shared across sessions.

Instead, we can use the
[Flask-Caching](https://pythonhosted.org/Flask-Caching/)
library which saves the results in a shared memory database like Redis or as
a file on your filesystem. Flask-Caching also has other nice features like
time-based expiry. Time-based expiry is helpful if you want to update your
data (clear your cache) every hour or every day.

Here is an example of `Flask-Caching` with Redis:
'''),

    rc.Markdown("""
    ```python

    import datetime
    import os

    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output
    from flask_caching import Cache

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    cache = Cache(app.server, config={
        # try 'filesystem' if you don't want to setup redis
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_URL': os.environ.get('REDIS_URL', '')
    })
    app.config.suppress_callback_exceptions = True

    timeout = 20
    app.layout = html.Div([
        html.Div(id='flask-cache-memoized-children'),
        dcc.RadioItems(
            id='flask-cache-memoized-dropdown',
            options=[
                {'label': 'Option {}'.format(i), 'value': 'Option {}'.format(i)}
                for i in range(1, 4)
            ],
            value='Option 1'
        ),
        html.Div('Results are cached for {} seconds'.format(timeout))
    ])


    @app.callback(
        Output('flask-cache-memoized-children', 'children'),
        Input('flask-cache-memoized-dropdown', 'value'))
    @cache.memoize(timeout=timeout)  # in seconds
    def render(value):
        return 'Selected "{}" at "{}"'.format(
            value, datetime.datetime.now().strftime('%H:%M:%S')
        )


    if __name__ == '__main__':
        app.run_server(debug=True)
    ```


    """    ),

    rc.Markdown('''

***

Here is an example that **caches a dataset** instead of a callback.
It uses the FileSystem cache, saving the cached results to the filesystem.

This approach works well if there is one dataset that is used to update
several callbacks.

'''),

    rc.Markdown("""
    ```python

    import datetime as dt

    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    import numpy as np
    import pandas as pd
    from dash.dependencies import Input, Output
    from flask_caching import Cache

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    cache = Cache(app.server, config={
        'CACHE_TYPE': 'filesystem',
        'CACHE_DIR': 'cache-directory'
    })

    TIMEOUT = 60

    @cache.memoize(timeout=TIMEOUT)
    def query_data():
        # This could be an expensive data querying step
        np.random.seed(0)  # no-display
        df = pd.DataFrame(
            np.random.randint(0, 100, size=(100, 4)),
            columns=list('ABCD')
        )
        now = dt.datetime.now()
        df['time'] = [now - dt.timedelta(seconds=5*i) for i in range(100)]
        return df.to_json(date_format='iso', orient='split')


    def dataframe():
        return pd.read_json(query_data(), orient='split')

    app.layout = html.Div([
        html.Div('Data was updated within the last {} seconds'.format(TIMEOUT)),
        dcc.Dropdown(
            id='live-dropdown',
            value='A',
            options=[{'label': i, 'value': i} for i in dataframe().columns]
        ),
        dcc.Graph(id='live-graph')
    ])


    @app.callback(Output('live-graph', 'figure'),
                Input('live-dropdown', 'value'))
    def update_live_graph(value):
        df = dataframe()
        now = dt.datetime.now()
        return {
            'data': [{
                'x': df['time'],
                'y': df[value],
                'line': {
                    'width': 1,
                    'color': '#0074D9',
                    'shape': 'spline'
                }
            }],
            'layout': {
                # display the current position of now
                # this line will be between 0 and 60 seconds
                # away from the last datapoint
                'shapes': [{
                    'type': 'line',
                    'xref': 'x', 'x0': now, 'x1': now,
                    'yref': 'paper', 'y0': 0, 'y1': 1,
                    'line': {'color': 'darkgrey', 'width': 1}
                }],
                'annotations': [{
                    'showarrow': False,
                    'xref': 'x', 'x': now, 'xanchor': 'right',
                    'yref': 'paper', 'y': 0.95, 'yanchor': 'top',
                    'text': 'Current time ({}:{}:{})'.format(
                        now.hour, now.minute, now.second),
                    'bgcolor': 'rgba(255, 255, 255, 0.8)'
                }],
                # aesthetic options
                'margin': {'l': 40, 'b': 40, 'r': 20, 't': 10},
                'xaxis': {'showgrid': False, 'zeroline': False},
                'yaxis': {'showgrid': False, 'zeroline': False}
            }
        }


    if __name__ == '__main__':
        app.run_server(debug=True)



    ```







    """),

    rc.Markdown('''

***

## Graphs



[Plotly.js](https://github.com/plotly/plotly.js) is pretty fast out of the box.

Most plotly charts are rendered with SVG. This provides crisp rendering,
publication-quality image export, and wide browser support.
Unfortunately, rendering graphics in SVG can be slow for large datasets
(like those with more than 15k points).
To overcome this limitation, plotly.js has WebGL alternatives to
some chart types. WebGL uses the GPU to render graphics.

The high performance, WebGL alternatives include:
- `scattergl`: A webgl implementation of the `scatter` chart type. [Examples](https://plotly.com/python/webgl-vs-svg/), [reference](https://plotly.com/python/reference/#scattergl)
- `pointcloud`: A lightweight version of `scattergl` with limited customizability but even faster rendering. [Reference](https://plotly.com/python/reference/#pointcloud)
- `heatmapgl`: A webgl implementation of the `heatmap` chart type. [Reference](https://plotly.com/python/reference/#heatmapgl)


Currently, dash redraws the entire graph on update using the `plotly.js`
`newPlot` call. The performance of updating a chart could be improved
considerably by introducing `restyle` calls into this logic. If you or
your company would like to sponsor this work,
[get in touch](https://plotly.com/products/consulting-and-oem/).

***

## Clientside Callbacks

Clientside callbacks execute your code in the client in JavaScript rather than
on the server in Python.

Read more about clientside callbacks in the
<dccLink href="/clientside-callbacks" children="clientside callbacks"/>
chapter.

## Sponsoring Performance Enhancements

There are many other ways that we can improve the performance of dash apps,
like caching front-end requests, pre-filling the cache, improving plotly.js's
webgl capabilities, reducing JavaScript bundle sizes, and more.

Historically, many of these performance related features have been funded
through company sponsorship. If you or your company would like to sponsor
these types of enhancements, [please get in touch](https://plotly.com/products/consulting-and-oem/),
we'd love to help.

''')
])
