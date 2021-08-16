import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash_docs.reusable_components import Section, Chapter
from dash_docs import styles
from dash_docs import tools
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)

preamble = html.Div([

    rc.Markdown('''
    # Dash DataTable

    '''),

    html.Iframe(
        src="https://ghbtns.com/github-btn.html?user=plotly&repo=dash-table&type=star&count=true&size=large",
        width="160px",
        height="30px",
        style={'border': 'none'}
    ),

    rc.Markdown('''
    #### Dash DataTable is an interactive table component designed for
    #### viewing, editing, and exploring large datasets.

    This component was written from scratch in React.js specifically
    for the Dash community. Its API was designed to be ergonomic
    and its behavior is completely customizable through its properties.
    DataTable is rendered with standard, semantic HTML `<table/>` markup,
    which makes it accessible, responsive, and easy to style.
    '''),

    rc.Markdown('''
    For production Dash applications, DataTable is intended to be used with
    [Python data pipelines](https://plotly.com/dash/job-queue/) for ingesting
    the table data and [Design Kit](https://plotly.com/dash/design-kit) for
    DataTable styling.
    ''', className='red-links'),

    Section('Quickstart', [
        rc.Markdown(
            '''
            ```shell
            pip install dash=={}
            ```
            '''.format(dash.__version__),
            style=styles.code_container
        ),

        dcc.Tabs([
            dcc.Tab(
                label='Dash open-source',
                children=[
                    rc.Markdown(
                        examples['simple.py'][0],
                        style=styles.code_container
                    ),

                    html.Div(examples['simple.py'][1], className='example-container'),
                ]
            ),
            dcc.Tab(
                label='Dash Enterprise',
                children=[
                    rc.Markdown(
                    '''
                    ```python
                    import dash
                    import dash_table
                    import pandas as pd
                    import dash_design_kit as ddk

                    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

                    app = dash.Dash(__name__)

                    app.layout = ddk.App(show_editor=True, children=[
                        ddk.DataTable(
                           id='table',
                           columns=[{"name": i, "id": i} for i in df.columns],
                           data=df.to_dict('records'),
                           editable=True
                       )
                    ])

                    if __name__ == '__main__':
                        app.run_server(debug=True)
                    ```
                    '''
                    ),

                    html.P('Default Theme'),
                    html.Img(src=tools.relpath('/assets/images/ddk/table-default.png')),
                    html.P('Neptune Theme'),
                    html.Img(src=tools.relpath('/assets/images/ddk/table-neptune.png')),
                    html.P('Miller Theme'),
                    html.Img(src=tools.relpath('/assets/images/ddk/table-miller.png')),
                    html.P('Mercury Theme'),
                    html.Img(src=tools.relpath('/assets/images/ddk/table-mercury.png')),
                    html.P('Design Kit Theme Editor'),
                    html.Img(src=tools.relpath('/assets/images/ddk/theme-editor.png')),

                ]
            ),
        ])

    ]),

    Section('User Guide', []),
])
