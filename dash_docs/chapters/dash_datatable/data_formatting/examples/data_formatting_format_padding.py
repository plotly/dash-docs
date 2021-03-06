import dash
from dash_table import DataTable
from dash_table.Format import Format, Padding

app = dash.Dash(__name__)

columns = [
    dict(id='a', name='No padding', type='numeric', format=Format()), # skip-id-check
    dict(id='a', name='Padding 12', type='numeric', format=Format(padding=True, padding_width=12)), # skip-id-check
    dict(id='a', name='Padding 9', type='numeric', format=Format(padding=Padding.yes).padding_width(9)), # skip-id-check
    dict(id='a', name='Padding 6', type='numeric', format=dict(specifier='06')) # skip-id-check
]

values = [123, 123, 1234, 12345, 123456789]

app.layout = DataTable(columns=columns, data=[dict(a=value) for value in values])

if __name__ == '__main__':
    app.run_server(debug=True)
