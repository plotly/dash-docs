import dash
from dash.dependencies import Output, Input
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(prevent_initial_callbacks=True)
app.layout = html.Div([
    html.Button("Download CSV", id="btn_csv"),
    dcc.Download(id="download-dataframe-csv")
])

import pandas as pd

df = pd.DataFrame({
    "a": [1, 2, 3, 4],
    "b": [2, 1, 5, 6],
    "c": ["x", "x", "y", "y"]
})

@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"), prevent_initial_call=True
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, "mydf.csv")

if __name__ == '__main__':
    app.run_server(debug=True)
