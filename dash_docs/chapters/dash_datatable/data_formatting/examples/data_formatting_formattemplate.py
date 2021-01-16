import dash
from dash_table import DataTable, FormatTemplate

app = dash.Dash(__name__)

money = FormatTemplate.money(2)
percentage = FormatTemplate.percentage(2)

columns = [
    dict(id='account', name='Account'),
    dict(id='balance', name='Balance', type='numeric', format=money),
    dict(id='rate', name='Rate', type='numeric', format=percentage)
]

data = [
    dict(account='A', balance=522.31, rate=0.139),
    dict(account='B', balance=1607.9, rate=0.1044),
    dict(account='C', balance=-228.41, rate=0.199),
]

app.layout = DataTable(
    columns=columns,
    data=data
)

if __name__ == '__main__':
    app.run_server(debug=True)
