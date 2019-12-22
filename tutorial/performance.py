import dash_core_components as dcc

from tutorial.components import Syntax
from tutorial import tools

examples = {
    'memoization': tools.load_example(
        'tutorial/examples/performance_memoization.py'),
    'performance_flask_caching': tools.load_example(
        'tutorial/examples/performance_flask_caching.py'),
    'performance_flask_caching_dataset': open(
        'tutorial/examples/performance_flask_caching_dataset.py').read()
}

layout = [
    dcc.Markdown('''# Performance

This chapter contains several recommendations for improving the performance
of your dash apps.

The main performance limitation of dash apps is likely the callbacks in
the application code itself. If you can speed up your callbacks, your app
will feel snappier.

### Memoization

Since Dash's callbacks are functional in nature (they don't contain any state),
it's easy to add memoization caching. Memoization stores the results of a
function after it is called and re-uses the result if the function is called
with the same arguments.

To better understand how memoization works, let's start with a simple example.

'''),

    Syntax('''
import time
import functools32

@functools32.lru_cache(maxsize=32)
def slow_function(input):
    time.sleep(10)
    return 'Input was {}'.format(input)
    '''),

    dcc.Markdown('''

Calling `slow_function('test')` the first time will take 10 seconds.
Calling it a second time with the same argument will take almost no time
since the previously computed result was saved in memory and reused.

***

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

    Syntax(examples['performance_flask_caching'][0]),

    dcc.Markdown('''

***

Here is an example that **caches a dataset** instead of a callback.
It uses the FileSystem cache, saving the cached results to the filesystem.

This approach works well if there is one dataset that is used to update
several callbacks.

'''),

    Syntax(examples['performance_flask_caching_dataset']),

    dcc.Markdown('''

***

### Graphs

[Plotly.js](https://github.com/plotly/plotly.js) is pretty fast out of the box.

Most plotly charts are rendered with SVG. This provides crisp rendering,
publication-quality image export, and wide browser support.
Unfortunately, rendering graphics in SVG can be slow for large datasets
(like those with more than 15k points).
To overcome this limitation, plotly.js has WebGL alternatives to
some chart types. WebGL uses the GPU to render graphics.

The high performance, WebGL alternatives include:
- `scattergl`: A webgl implementation of the `scatter` chart type. [Examples](https://plot.ly/python/webgl-vs-svg/), [reference](https://plot.ly/python/reference/#scattergl)
- `pointcloud`: A lightweight version of `scattergl` with limited customizability but even faster rendering. [Reference](https://plot.ly/python/reference/#pointcloud)
- `heatmapgl`: A webgl implementation of the `heatmap` chart type. [Reference](https://plot.ly/python/reference/#heatmapgl)


Currently, dash redraws the entire graph on update using the `plotly.js`
`newPlot` call. The performance of updating a chart could be improved
considerably by introducing `restyle` calls into this logic. If you or
your company would like to sponsor this work,
[get in touch](https://plot.ly/products/consulting-and-oem/).

***

### Sponsoring Performance Enhancements

There are many other ways that we can improve the performance of dash apps,
like caching front-end requests, pre-filling the cache, improving plotly.js's
webgl capabilities, reducing JavaScript bundle sizes, and more.

Historically, many of these performance related features have been funded
through company sponsorship. If you or your company would like to sponsor
these types of enhancements, [please get in touch](https://plot.ly/products/consulting-and-oem/),
we'd love to help.

''')
]
