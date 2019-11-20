import math
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
years = sorted(list(df.year.unique()))

app.layout = html.Div([
    dcc.Graph(id='graph-with-history'),
    dcc.Slider(
        id='year-slider-id',
        marks={
            i: str((str(i) if (i-2) % 10 == 0 else ''))
            for i in years
        },
        value=1952, min=years[0], max=years[-1]
    )
])


@app.callback(
    Output('graph-with-history', 'figure'),
    [Input('graph-with-history', 'hoverData'),
     Input('graph-with-history', 'selectedData'),
     Input('year-slider-id', 'value')])
def filterTimeSeries(hoverData, selectedData, year):
    if hoverData is None:
        hoverData = {'points': []}
    if selectedData is None:
        selectedData = {'points': []}
    filtered_countries = set([
        point['customdata']
        for point in hoverData['points'] + selectedData['points']
    ])

    filtered_df = df[df.year == year]
    traces = []
    for i, continent in enumerate(df.continent.unique()):
        continent_df = filtered_df[filtered_df.continent == continent]
        traces.append({
            'x': continent_df.gdpPercap,
            'y': continent_df.lifeExp,
            'text': continent_df.country,
            'customdata': continent_df.country,
            'marker': {
                'size': 10,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'lightgrey'}
            },
            'name': continent,
            'mode': 'markers'
        })
    for country in filtered_countries:
        country_df = df[df.country == country]
        traces.append({
            'x': country_df.gdpPercap,
            'y': country_df.lifeExp,
            'hoverinfo': 'skip',
            'mode': 'lines',
            'line': {'width': 1, 'color': 'grey'},
            'name': country
        })
    return {
        'data': traces,
        'layout': {
            'xaxis': {
                'title': 'GDP per Capita', 'type': 'log',
                'range': [math.log10(10), math.log10(100*1000)],
                'autorange': False
            },
            'yaxis': {
                'title': 'Life Expectancy',
                'range': [20, 90], 'autorange': False
            },
            'legend': {
                'x': 0, 'xanchor': 'left',
                'y': 1, 'yanchor': 'top',
                'bgcolor': 'rgba(255, 255, 255, 0.5)'
            },
            'margin': {'l': 40, 'r': 0, 't': 40, 'b': 40},
            'hovermode': 'closest', 'dragmode': 'select'
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True)
