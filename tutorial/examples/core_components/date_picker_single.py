import dash
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt

app = dash.Dash()
app.layout = html.Div([
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2017, 9, 19),
        initial_visible_month=dt(2017, 8, 5),
        date=dt(2017, 8, 25)
    ),
    html.Div(id='output-container-date-picker-single')
])


@app.callback(
    dash.dependencies.Output('output-container-date-picker-single', 'children'),
    [dash.dependencies.Input('my-date-picker-single', 'date')])
def update_output(date):
    string_prefix = "You have selected: "
    if date is not None:
        date = dt.strptime(date, '%Y-%m-%d')
        date_string = date.strftime('%B %d, %Y')
        return string_prefix + date_string

if __name__ == '__main__':
    app.run_server(debug=True)
