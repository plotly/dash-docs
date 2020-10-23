import dash
import pandas as pd
from dash.dependencies import Input, Output
import dash_table

app = dash.Dash(__name__)


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app.layout = dash_table.DataTable(
    columns=[dict(name=[i,i], id=i) for i in sorted(df.columns)],
    data=df.to_dict('records'),
    fixed_columns=dict(headers=True),
    fixed_rows=dict(headers=True),
    tooltip=dict(
        continent='Continent',
        country='Country',
        gdpPercap='GDP per capita',
        lifeExp='Life Expectancy'
    ),
    tooltip_header=dict(
        continent=dict(value='*Continent*', type='markdown'),
        country='**Country**',
        gdpPercap=None,
        lifeExp=[None, dict(value='*LIFE EXPECTANCY*', type='markdown')],
        pop=['Population', dict(value='# Population', type='text')]
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)
