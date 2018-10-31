import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


app = dash.Dash(__name__)

app.layout = html.Div([
    # embed `dcc` input in initial layout (https://github.com/plotly/dash-renderer/issues/46)
    html.Div(dcc.Input(), style={'display': 'none'}),
    dash_table.DataTable(
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
    ),
    html.Div(id='dash-table-interactivity-container')
])


@app.callback(
    Output('dash-table-interactivity-container', "children"),
    [Input('dash-table-interactivity', "derived_virtual_dataframe"),
     Input('dash-table-interactivity', "selected_rows")])
def update_graph(rows, selected_rows):
    # When the table is first rendered, `derived_virtual_dataframe`
    # will be `None`. This is due to an idiosyncracy in Dash
    # (unsupplied properties are always None and Dash calls the dependent
    # callbacks when the component is first rendered).
    # So, if `selected_rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_dataframe=df.to_rows('dict')` when you initialize
    # the component.
    if rows is None:
        dff = df
    else:
        dff = pd.DataFrame(rows)

    colors = []
    for i in range(len(dff)):
        if i in selected_rows:
            colors.append("#7FDBFF")
        else:
            colors.append("#0074D9")

    return html.Div(
        [
            dcc.Graph(
                id=column,
                figure={
                    "data": [
                        {
                            "x": dff["country"],
                            # check if column exists - user may have deleted it
                            # If `column.deletable=False`, then you don't
                            # need to do this check.
                            "y": dff[column] if column in dff else [],
                            "type": "bar",
                            "marker": {"color": colors},
                        }
                    ],
                    "layout": {
                        "xaxis": {"automargin": True},
                        "yaxis": {"automargin": True},
                        "height": 250,
                        "margin": {"t": 10, "l": 10, "r": 10},
                    },
                },
            )
            for column in ["pop", "lifeExp", "gdpPercap"]
        ]
    )



if __name__ == '__main__':
    app.run_server(debug=True)
