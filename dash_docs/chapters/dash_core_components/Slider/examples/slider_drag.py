import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Slider(id='slider-drag'),
    html.Div(id='slider-drag-output', style={'margin-top': 20})
])


@app.callback(Output('slider-drag-output', 'children'),
              [Input('slider-drag', 'drag_value'), Input('slider-drag', 'value')])
def display_value(drag_value, value):
    return 'drag_value: {} | value: {}'.format(drag_value, value)


if __name__ == '__main__':
    app.run_server(debug=True)
