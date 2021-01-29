import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Slider(
            id="slider-circular", min=0, max=20, 
            marks={i: str(i) for i in range(21)}, 
            value=3
        ),
        dcc.Input(
            id="input-circular", type="number", min=0, max=20, value=3
        ),
    ]
)
@app.callback(
    Output("input-circular", "value"),
    Output("slider-circular", "value"),
    Input("input-circular", "value"),
    Input("slider-circular", "value"),
)
def callback(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input" else slider_value
    return value, value
    
if __name__ == '__main__':
    app.run_server(debug=True)