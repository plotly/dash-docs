import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://codepen.io/chriddyp/pen/LLYbXR.css'
]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Hours per Day'),
    dcc.Slider(id='hours', value=5, min=0, max=24, step=1),

    html.Label('Rate'),
    dcc.Input(id='rate', value=2, type='number'),

    html.Label('Amount per Day'),
    html.Div(id='amount'),

    html.Label('Amount per Week'),
    html.Div(id='amount-per-week')
], style={
    'padding': 60,
    'width': 180,
    'border': 'thin lightgrey solid',
    'backgroundColor': 'white',
    'marginRight': 'auto',
    'marginLeft': 'auto',
    'borderRadius': 5,
    'marginTop': 40
})


@app.callback(Output('amount', 'children'),
              [Input('hours', 'value'), Input('rate', 'value')])
def compute_amount(hours, rate):
    return float(hours) * float(rate)


@app.callback(Output('amount-per-week', 'children'),
              [Input('amount', 'children')])
def compute_amount(amount):
    return float(amount) * 7



if __name__ == '__main__':
    app.run_server(debug=True)
