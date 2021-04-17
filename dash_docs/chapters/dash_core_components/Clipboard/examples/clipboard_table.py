
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

app.layout = html.Div(
    [
        dcc.Clipboard(
            id="DataTable_copy",
            style={"fontSize": 30, "color": "white", "backgroundColor": "grey", "height":38},
            className="button",
        ),
        dcc.RadioItems(
            id="copy_selected",
            options=[
                {"label": "Copy All", "value": "all"},
                {"label": "Copy Selected", "value": "some"},
            ],
            value="all",
            style={"display": "inline-block"},
        ),
        dash_table.DataTable(
            id="DataTable",
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
            sort_action="native",
            page_size=10,
        ),
    ]
)


@app.callback(
    Output("DataTable_copy", "text"),
    Input("DataTable_copy", "n_clicks"),
    State("DataTable", "start_cell"),
    State("DataTable", "end_cell"),
    State("DataTable", "derived_virtual_data"),
    State("copy_selected", "value")
)
def custom_copy(_, start, end, data, copy_selected):
    dff = pd.DataFrame(data)
    if start and (copy_selected == 'some'):
        copy_cells = dff.loc[
            start["row"]: end["row"], start["column_id"]: end["column_id"]
        ]
        return copy_cells.to_string(header=False)
    else:
        return dff.to_string()  # includes headers


if __name__ == "__main__":
    app.run_server(debug=True)