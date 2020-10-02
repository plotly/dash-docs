from datetime import datetime as dt
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import re

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=dt(1995, 8, 5).date(),
        max_date_allowed=dt(2017, 9, 19).date(),
        initial_visible_month=dt(2017, 8, 5).date(),
        date=dt(2017, 8, 25, 23, 59, 59).date()
    ),
    html.Div(id='output-container-date-picker-single')
])


@app.callback(
    Output('output-container-date-picker-single', 'children'),
    [Input('my-date-picker-single', 'date')])
def update_output(date):
    string_prefix = 'You have selected: '
    if date is not None:
        date_object = dt.strptime(date, '%Y-%m-%d')
        date_string = date_object.strftime('%B %d, %Y')
        return string_prefix + date_string


if __name__ == '__main__':
    app.run_server(debug=True)
