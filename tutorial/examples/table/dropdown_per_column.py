import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_table
import pandas as pd
from collections import OrderedDict


app = dash.Dash(__name__)

df = pd.DataFrame(OrderedDict([
    ('climate', ['Sunny', 'Snowy', 'Sunny', 'Rainy']),
    ('temperature', [13, 43, 50, 30]),
    ('city', ['NYC', 'Montreal', 'Miami', 'NYC'])
]))


app.layout = html.Div([
    dash_table.DataTable(
        id='table-dropdown',
        data=df.to_dict('rows'),
        columns=[
            {'id': 'climate', 'name': 'climate', 'presentation': 'dropdown'},
            {'id': 'temperature', 'name': 'temperature'},
            {'id': 'city', 'name': 'city', 'presentation': 'dropdown'},
        ],

        editable=True,
        column_static_dropdown=[
            {
                'id': 'climate',
                'dropdown': [
                    {'label': i, 'value': i}
                    for i in df['climate'].unique()
                ]
            },
            {
                'id': 'city',
                'dropdown': [
                    {'label': i, 'value': i}
                    for i in df['city'].unique()
                ]
            },
        ]
    ),
    html.Div(id='table-dropdown-container')
])


# In order for the changes in the dropdown to persist,
# the dropdown needs to be "connected" to the table via
# a callback
@app.callback(Output('table-dropdown-container', 'children'),
              [Input('table-dropdown', 'data_timestamp')])
def update_output(timestamp):
    return timestamp


if __name__ == '__main__':
    app.run_server(debug=True)
