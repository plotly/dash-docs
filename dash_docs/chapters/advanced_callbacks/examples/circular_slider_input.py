import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    dcc.Slider(
        id='slider-circular',
        min=0, max=20,
    ),
    dcc.Input(
        id='input-circular',
        type='number',
        debounce=False,
        value=3
    ),
])


@app.callback(
    Output('input-circular', 'value'),
    Output('slider-circular', 'value'),
    Input('input-circular', 'value'),
    Input('slider-circular', 'value'),
)
def callback(iv, sv):
    ctx = dash.callback_context
    if not ctx.triggered:
        # default to input value during initialization
        if iv is not None:
            value = iv
        else:
            value = sv
    else:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if trigger_id == 'input':
            value = iv
        else:
            value = sv
    return value, value


if __name__ == '__main__':
    app.run_server(debug=True)