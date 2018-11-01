import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

df[' index'] = range(1, len(df) + 1)

app = dash.Dash(__name__)

PAGE_SIZE = 5

app.layout = dash_table.DataTable(
    id='table-paging-and-sorting',
    columns=[
        {'name': i, 'id': i, 'deletable': True} for i in sorted(df.columns)
    ],
    pagination_settings={
        'current_page': 0,
        'page_size': PAGE_SIZE
    },
    pagination_mode='be',

    sorting='be',
    sorting_type='single',
    sorting_settings=[]
)


@app.callback(
    Output('table-paging-and-sorting', 'data'),
    [Input('table-paging-and-sorting', 'pagination_settings'),
     Input('table-paging-and-sorting', 'sorting_settings')])
def update_graph(pagination_settings, sorting_settings):
    if len(sorting_settings):
        dff = df.sort_values(
            sorting_settings[0]['column_id'],
            ascending=sorting_settings[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = df

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')


if __name__ == '__main__':
    app.run_server(debug=True)
