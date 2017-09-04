import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.layout = html.Div([
    html.Div(dcc.Input(id='input-box', type="text")),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button',
             children="Enter a value and press submit")
])

@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(n_clicks, value):
    return "The input value was \"{}\" and the button has been clicked {} times".format(
        value,
        n_clicks
    )

if __name__ == '__main__':
    app.run_server(debug=True)
