import sys
import time

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

if sys.version_info < (3, 2, 0):
    from functools32 import lru_cache
else:
    from functools import lru_cache

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    html.Div(id='memoized-children'),
    dcc.RadioItems(
        id='memoized-dropdown',
        options=[
            {'label': 'Option {}'.format(i), 'value': 'Option {}'.format(i)}
            for i in range(1, 4)
        ],
        value='Option 1'
    )
])


# When you click the button, this content gets loaded
@app.callback(
    Output('memoized-children', 'children'),
    [Input('memoized-dropdown', 'value')])
@lru_cache()
def render(value):
    time.sleep(2)
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
