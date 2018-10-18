import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd


app = dash.Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


PAGE_SIZE = 5


app.layout = dash_table.Table(
    id='table-filtering',
    columns=[
        {"name": i, "id": i, "deletable": True} for i in sorted(df.columns)
    ],
    pagination_settings={
        'displayed_pages': 1,
        'current_page': 0,
        'page_size': PAGE_SIZE
    },
    pagination_mode='be',

    filtering='be',
    filtering_settings=''
)


@app.callback(
    Output('table-filtering', "dataframe"),
    [Input('table-filtering', "pagination_settings"),
     Input('table-filtering', "filtering_settings")])
def update_graph(pagination_settings, filtering_settings):
    print(filtering_settings)
    filtering_expressions = filtering_settings.split(' && ')
    dff = df
    for filter in filtering_expressions:
        if ' eq ' in filter:
            col_name = filter.split(' eq ')[0]
            filter_value = filter.split(' eq ')[1]
            dff = dff.loc[dff[col_name] == filter_value]
        if ' > ' in filter:
            col_name = filter.split(' > ')[0]
            filter_value = float(filter.split(' > ')[1])
            dff = dff.loc[dff[col_name] > filter_value]
        if ' < ' in filter:
            col_name = filter.split(' < ')[0]
            filter_value = float(filter.split(' < ')[1])
            dff = dff.loc[dff[col_name] < filter_value]

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')


if __name__ == '__main__':
    app.run_server(debug=True)
