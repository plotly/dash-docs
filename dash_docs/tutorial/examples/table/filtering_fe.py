import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html

import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    columns=[
        {"name": i, "id": i} for i in df.columns
    ],
    data=df.to_dict('records'),
    filter_action="native",
)


if __name__ == '__main__':
    app.run_server(debug=True)
