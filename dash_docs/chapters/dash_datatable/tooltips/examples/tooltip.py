import dash
import pandas as pd
from dash.dependencies import Input, Output
import dash_table

app = dash.Dash(__name__)


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app.layout = dash_table.DataTable(
    columns=[dict(name=i, id=i) for i in sorted(df.columns)],
    data=df.to_dict('records'),
    fixed_columns=dict(headers=True),
    fixed_rows=dict(headers=True),
    tooltip=dict(
        continent='Continent',
        country=dict(
            value='Country',
            use_with='both'
        ),
        gdpPercap=dict(
            value='*GDP per capita*',
            type='markdown',
            use_with='header'
        ),
        lifeExp=dict(
            value='Life Expectancy',
            delay=0,
            duration=None
        ),
        pop=dict(
            value='Population',
            delay=2000,
            duration=500
        )
    ),
    tooltip_delay=350,
    tooltip_duration=2000
)

if __name__ == '__main__':
    app.run_server(debug=True)
