import dash
from dash_table import DataTable
from dash_table.Format import Format, Group

app = dash.Dash(__name__)

columns = [
    dict(id='a', name='No groups', type='numeric', format=Format()), # skip-id-check
    dict(id='a', name='Groups of 3', type='numeric', format=Format().group(True)), # skip-id-check
    dict(id='a', name='Groups of 4', type='numeric', format=Format(group=True, groups=[4])), # skip-id-check
    dict(id='a', name='Groups of 2,3,2', type='numeric', format=Format(group=Group.yes).groups([2, 3, 2])) # skip-id-check
]

values = [123, 123, 1234, 12345, 123456789]

app.layout = DataTable(
    columns=columns,
    data=[dict(a=value) for value in values]
)

if __name__ == '__main__':
    app.run_server(debug=True)
