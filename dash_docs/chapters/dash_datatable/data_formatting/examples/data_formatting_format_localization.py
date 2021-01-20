import dash
from dash_html_components import Br, Div
from dash_table import DataTable
from dash_table.Format import Format, Group, Prefix, Scheme, Symbol

app = dash.Dash(__name__)

columns_1 = [
    dict(id='a', name='Symbol', type='numeric', format=Format(symbol=Symbol.yes)), # skip-id-check
    dict(id='a', name='Symbol prefix', type='numeric', format=Format(symbol=Symbol.yes, symbol_prefix='CAD$ ')), # skip-id-check
    dict(id='a', name='Symbol suffix', type='numeric', format=Format(symbol=Symbol.yes, symbol_suffix=' $CAD')), # skip-id-check
    dict(id='a', name='Symbol custom', type='numeric', format=dict(specifier='$', locale=dict(symbol=['@', '*']))) # skip-id-check
]

columns_2 = [
    dict(id='a', name='Decimal', type='numeric', format=Format(decimal_delimiter=':').scheme('f').precision(2)), # skip-id-check
    dict(id='a', name='Custom decimal', type='numeric', format=dict(specifier='.2f', locale=dict(decimal=':'))), # skip-id-check
    dict(id='a', name='Group', type='numeric', format=Format(group_delimiter=':', group=Group.yes, groups=[2])), # skip-id-check
    dict(id='a', name='Custom group', type='numeric', format=dict(specifier=',', locale=dict(group=':', grouping=[2]))) # skip-id-check
]

columns_3 = [
    dict(id='a', name='Custom numerals', type='numeric', format=dict(locale=dict(numerals=['0', 'AA', 'b', 'CC', '', '', '', '77', '88', '99']))), # skip-id-check
    dict(id='a', name='Percent symbol', type='numeric', format=dict(specifier='.2%', locale=dict(percent='@'))), # skip-id-check
    dict(id='a', name='Group 4 digits', type='numeric', format=dict(specifier=',.0f', locale=dict(separate_4digits=False))), # skip-id-check
    dict(id='a', name='SI', type='numeric', format=Format(si_prefix=Prefix.milli).precision(0)), # skip-id-check
    dict(id='a', name='SI+space', type='numeric', format=Format(si_prefix=Prefix.milli, symbol=Symbol.yes, symbol_suffix=' ').precision(0)), # skip-id-check
    dict(id='a', name='Explicit SI', type='numeric', format=Format(si_prefix=10 ** -3).precision(0)) # skip-id-check
]

values = [123, 123, 1234, 12345, 123456789]
data = [dict(a=value) for value in values]

app.layout = Div([
    DataTable(columns=columns_1, data=data),
    Br(),
    DataTable(columns=columns_2, data=data),
    Br(),
    DataTable(columns=columns_3, data=data)
])

if __name__ == '__main__':
    app.run_server(debug=True)
