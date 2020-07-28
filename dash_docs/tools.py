import os
import re

if os.environ.get('DASH_APP_LOCATION', '') != 'ABSOLUTE':
    from .server import app
else:
    from server import app


def relpath(path):
    if path.startswith('/') and 'DASH_DOCS_URL_PREFIX' in os.environ and not path.startswith('/{}'.format(os.environ['DASH_DOCS_URL_PREFIX'].strip('/'))):
        # In enterprise docs, all assets are under `/Docs`
        return '{}{}'.format(
            os.environ['DASH_DOCS_URL_PREFIX'].rstrip('/'),
            path
        )

    return path


def exception_handler(func):
    def wrapper(path, **kwargs):
        try:
            return func(path, **kwargs)
        except Exception as e:
            print('\nError running {}\n{}'.format(path, '=' * 76))
            raise e
    return wrapper


def load_examples(index_filename, omit=[]):
    dir = os.path.dirname(os.path.relpath(index_filename))
    example_dir = os.path.join(dir, 'examples')
    try:
        example_filenames = os.listdir(example_dir)
    except:
        # e.g. no examples folder
        return {}

    examples = {}
    for filename in example_filenames:
        full_filename = os.path.join(example_dir, filename)
        if filename not in omit and os.path.isfile(full_filename) and filename.endswith('.py'):
            examples[filename] = load_example(full_filename)
    return examples



@exception_handler
def load_example(path, relative_path=False):
    if relative_path:
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
    with open(path, 'r') as _f:
        _source = _f.read()
        _example = _source

        # Use the global app assignment
        if 'app = dash.Dash' not in _example and 'app = CustomDash()' not in _example:
            raise Exception("Didn't declare app")
        _example = _example.replace('app = dash.Dash', '# app = dash.Dash')

        commented_configs = [
            'app.scripts.config.serve_locally',
            'app.css.config.serve_locally'
        ]
        for config in commented_configs:
            _example = _example.replace(
                config,
                '# {}'.format(config)
            )

        if 'import dash\n' not in _example:
            raise Exception("Didn't import dash")

        # return the layout instead of assigning it to the global app
        if 'app.layout = ' not in _example:
            raise Exception('app.layout not assigned')
        _example = _example.replace('app.layout = ', 'layout = ')

        # Remove the "# Run the server" commands
        if 'app.run_server' not in _example:
            raise Exception('app.run_server missing')
        _example = _example.replace(
            '\n    app.run_server',
            'print("Running")\n    # app.run_server'
        )

        # if there are lines that should be included in the syntax but
        # not executed, simply put a comment on that line starting "# no-exec"
        # similarly, if there are lines that should be evalued but
        # not executed, simply put a comment on that line starting "# no-display"
        no_exec = '# no-exec'
        no_display = '# no-display'
        if no_exec in _example:
            _example = '\n'.join(
                line for line in _example.splitlines() if no_exec not in line
            )

            find_no_exec = re.compile(r'\s+' + no_exec + '.*')
            _source = '\n'.join(
                find_no_exec.sub('', line) if no_exec in line else line
                for line in _source.splitlines()
            )

        if no_display in _example:
            _source = '\n'.join(
                line for line in _source.splitlines() if no_display not in line
            )

            find_no_display = re.compile(r'\s+' + no_display + '.*')
            _example = '\n'.join(
                find_no_display.sub('', line) if no_display in line else line
                for line in _example.splitlines()
            )

        if '$tools' in _example:
            _example = _example.replace('$tools', os.path.dirname(os.path.realpath(__file__)))

        # replace remote datasets with local ones
        # so that the app can run in internet-less environments
        find_and_replace = {
            'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv':
            'datasets/gapminderDataFiveYear.csv',

            'https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv':
            'datasets/gapminder2007.csv',

            'https://raw.githubusercontent.com/plotly/datasets/master/solar.csv':
            'datasets/solar.csv',

            'https://raw.githubusercontent.com/plotly/datasets/master/Emissions%20Data.csv':
            'datasets/Emissions%20Data.csv',

            'https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv':
            'datasets/1962_2006_walmart_store_openings.csv',

            'https://upload.wikimedia.org/wikipedia/commons/e/e4/Mitochondria%2C_mammalian_lung_-_TEM_%282%29.jpg':
            'datasets/mitochondria.jpg',

            'https://gist.githubusercontent.com/chriddyp/cb5392c35661370d95f300086accea51/raw/8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/indicators.csv':
            'datasets/indicators.csv',

            'https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv':
            'datasets/usa-agricultural-exports-2011.csv',

            'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv':
            'datasets/gdp-life-exp-2007.csv',

            'https://plotly.github.io/datasets/country_indicators.csv':
            'datasets/country_indicators.csv',

            'https://github.com/plotly/datasets/raw/master/26k-consumer-complaints.csv':
            'datasets/26k-consumer-complaints.csv',

            'https://js.cytoscape.org/demos/colajs-graph/data.json':
            'datasets/colajs-graph-data.json',

            'https://js.cytoscape.org/demos/colajs-graph/cy-style.json':
            'datasets/colajs-graph-cy-style.json',

            'https://www.publicdomainpictures.net/pictures/60000/nahled/flower-outline-coloring-page.jpg':
            relpath('/assets/images/gallery/flower-outline-coloring-page.jpg'),

            'https://raw.githubusercontent.com/plotly/datasets/master/mitochondria.jpg':
            relpath('/assets/images/gallery/mitochondria.jpg'),

        }
        for key in find_and_replace:
            if key in _example:
                _example = _example.replace(key, find_and_replace[key])

        scope = {'app': app}
        try:
            exec(_example, scope)
        except Exception as e:
            print(_example)
            raise e

    return (
        '```python \n' + _source + '```',
        scope['layout']  # layout is a global created from the app
    )


def merge(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def read_file(path):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path), 'r') as f:
        return f.read()
