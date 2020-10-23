import dash
import pandas as pd
from dash.dependencies import Input, Output
import dash_table

app = dash.Dash(__name__)


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app.layout = dash_table.DataTable(
    id='tooltip',
    columns=[dict(name=i, id=i) for i in sorted(df.columns)],
    data=df.to_dict('records'),
    fixed_columns=dict(headers=True),
    fixed_rows=dict(headers=True),
    tooltip=dict(pop='Population'),
    tooltip_conditional=[
        {
            'if': {
                'column_id': 'pop',
                'filter_query': '{pop} lt 5000000',
            },
            'type': 'markdown',
            'value': '*Small Population*'
        },
        {
            'if': {
                'column_id': 'pop',
                'filter_query': '{pop} gt 40000000',
            },
            'type': 'markdown',
            'value': '*Medium Population*'
        },
        {
            'if': {
                'column_id': 'pop',
                'filter_query': '{pop} gt 100000000',
            },
            'type': 'markdown',
            'value': '*Large Population*'
        }
    ],
    tooltip_data=[
        dict(pop=str(record['pop'])) for record in df.to_dict('records')[0:10]
    ],
    style_data_conditional=[
        {
            'if': {
                'column_id': 'pop',
                'filter_query': '{pop} lt 5000000',
            },
            'backgroundColor': 'yellow'
        },
        {
            'if': {
                'column_id': 'pop',
                'filter_query': '{pop} gt 40000000',
            },
            'backgroundColor': 'orange'
        },
        {
            'if': {
                'column_id': 'pop',
                'filter_query': '{pop} gt 100000000',
            },
            'backgroundColor': 'red'
        }
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
