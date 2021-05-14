import dash
from dash_table import DataTable
from dash_table.Format import Format, Align

app = dash.Dash(__name__)

columns = [
    dict(id='a', name='No fill', type='numeric', format=Format()), # skip-id-check
    dict(id='a', name='Align left (10)', type='numeric', format=Format().align(Align.left).fill('-').padding_width(10)), # skip-id-check
    dict(id='a', name='Align right (8)', type='numeric', format=Format(align=Align.right, fill='-', padding_width=8)), # skip-id-check
    dict(id='a', name='Align center (6)', type='numeric', format=dict(specifier='-^6')) # skip-id-check
]

values = [123, 123, 1234, 12345, 123456789]

app.layout = DataTable(
    columns=columns,
    data=[dict(a=value) for value in values]
)

if __name__ == '__main__':
    app.run_server(debug=True)
