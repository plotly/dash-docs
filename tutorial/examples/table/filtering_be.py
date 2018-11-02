import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd


app = dash.Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


app.layout = dash_table.DataTable(
    id='table-filtering-be',
    columns=[
        {"name": i, "id": i} for i in sorted(df.columns)
    ],

    filtering='be',
    filtering_settings=''
)


@app.callback(
    Output('table-filtering-be', "data"),
    [Input('table-filtering-be', "filtering_settings")])
def update_graph(filtering_settings):
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

    return dff.to_dict('rows')


if __name__ == '__main__':
    app.run_server(debug=True)
