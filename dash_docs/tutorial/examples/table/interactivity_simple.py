import dash
import dash_table

import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    columns=[
        {"name": i, "id": i, "deletable": True} for i in df.columns
    ],
    data=df.to_dict('records'),
    editable=True,
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    row_selectable="multi",
    row_deletable=True,
    selected_rows=[],
    fixed_rows={ 'headers': True, 'data': 0 },
)


if __name__ == '__main__':
    app.run_server(debug=True)
