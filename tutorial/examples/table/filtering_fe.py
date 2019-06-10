import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html

import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-filtering-fe',
        columns=[
            {"name": i, "id": i, "deletable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        filtering=True,
    ),
    html.Div(id='datatable-filter-container')
])


@app.callback(
    Output('datatable-filter-container', "children"),
    [Input('datatable-filtering-fe', "data")])
def update_graph(rows):
    if rows is None:
        dff = df
    else:
        dff = pd.DataFrame(rows)

    return html.Div()


if __name__ == '__main__':
    app.run_server(debug=True)
