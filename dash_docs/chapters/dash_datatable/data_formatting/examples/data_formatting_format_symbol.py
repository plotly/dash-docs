import dash
from dash_html_components import Br, Div
from dash_table import DataTable
from dash_table.Format import Format, Symbol

app = dash.Dash(__name__)

columns_1 = [
    dict(id='a', name='Default', type='numeric', format=Format()), # skip-id-check
    dict(id='a', name='No Symbol', type='numeric', format=Format(symbol=Symbol.no)), # skip-id-check
    dict(id='a', name='$ Symbol', type='numeric', format=Format(symbol=Symbol.yes)), # skip-id-check
    dict(id='a', name='$ Symbol / Locale prefix', type='numeric', format=Format().symbol(Symbol.yes).symbol_prefix('@')), # skip-id-check
    dict(id='a', name='$ Symbol / Locale prefix+suffix', type='numeric', format=Format().symbol(Symbol.yes).symbol_prefix('@').symbol_suffix('*')) # skip-id-check
]

columns_2 = [
    dict(id='a', name='Binary', type='numeric', format=Format(symbol=Symbol.binary)), # skip-id-check
    dict(id='a', name='Octal', type='numeric', format=Format(symbol=Symbol.octal)), # skip-id-check
    dict(id='a', name='Hex', type='numeric', format=Format(symbol=Symbol.hex)), # skip-id-check
    dict(id='a', name='Custom', type='numeric', format=dict(locale=dict(symbol=['@', '*']), specifier='$')) # skip-id-check
]

values = [123.1, 123.12, 1234.123, 12345.12]
data = [dict(a=value) for value in values]

app.layout = Div([
    DataTable(columns=columns_1, data=data),
    Br(),
    DataTable(columns=columns_2, data=data)
])

if __name__ == '__main__':
    app.run_server(debug=True)
