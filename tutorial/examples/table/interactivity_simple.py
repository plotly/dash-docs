import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html

import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


app = dash.Dash(__name__)

app.layout = dash_table.Table(
    id='dash-table-interactivity',
    columns=[
        {"name": i, "id": i, "deletable": True} for i in df.columns
    ],
    data=df.to_dict("rows"),
    editable=True,
    filtering=True,
    sorting=True,
    sorting_type="multi",
    row_selectable="multi",
    row_deletable=True,
    selected_rows=[],
    n_fixed_rows=2,
)


if __name__ == '__main__':
    app.run_server(debug=True)
