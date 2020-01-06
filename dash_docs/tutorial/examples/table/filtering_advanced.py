import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import json

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

df['id'] = df['country']
df.set_index('id', inplace=True, drop=False)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='filter-query-input', placeholder='Enter filter query',
              style={'width': '100%'}),
    dash_table.DataTable(
        id='datatable-advanced-filtering',
        columns=[
            {'name': i, 'id': i, 'deletable': True} for i in df.columns
            # omit the id column
            if i != 'id'
        ],
        data=df.to_dict('records'),
        editable=True,
        page_action='native',
        page_size=10,
        filter_action="native"
    ),
    html.Div(id='datatable-query-structure', style={'whitespace': 'pre'})
])


@app.callback(
    Output('datatable-advanced-filtering', 'filter_query'),
    [Input('filter-query-input', 'value')]
)
def update_query(query):
    if query is None:
        return ''
    return query


@app.callback(
    Output('datatable-query-structure', 'children'),
    [Input('datatable-advanced-filtering', 'derived_filter_query_structure')]
)
def display_query(query):
    if query is None:
        return ''
    return html.Details([
        html.Summary('Derived filter query structure'),
        html.Div(dcc.Markdown('''```json
{}
```'''.format(json.dumps(query, indent=4))))
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
