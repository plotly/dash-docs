import dash
import dash_table
import pandas as pd
from collections import OrderedDict


app = dash.Dash(__name__)

df = pd.DataFrame(OrderedDict([
    ('climate', ['Sunny', 'Snowy', 'Sunny', 'Rainy']),
    ('temperature', [13, 43, 50, 30]),
    ('city', ['NYC', 'Montreal', 'Miami', 'NYC'])
]))


app.layout = dash_table.Table(
    id='table-dropdowns',
    dataframe=df.to_dict('rows'),
    columns=[
        {'id': 'climate', 'name': 'climate'},
        {'id': 'temperature', 'name': 'temperature'},
        {'id': 'city', 'name': 'city'},
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
)

if __name__ == '__main__':
    app.run_server(debug=True)
