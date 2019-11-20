import math
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Get data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# Get a list of unique years in the dataframe
years = sorted(list(df.year.unique()))

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(id='graph-left'),
        ], className='six columns'),
        html.Div([
            dcc.Graph(id='graph-right')
        ], className='six columns')
    ], className='row'),
    dcc.Slider(
        id='common-year-slider',
        marks={
            i: str((str(i) if (i-2) % 10 == 0 else ''))
            for i in years
        },
        value=1952, min=years[0], max=years[-1]
    )
])


# Common figure generation function shared by both callbacks
def create_figure(year, selectedData, hoverData, yaxis_column):
    if selectedData is None:
        selectedData = {'points': []}
    if hoverData is None:
        hoverData = {'points': []}
    filtered_countries = set([
        point['customdata']
        for point in selectedData['points'] + hoverData['points']
    ])

    filtered_df = df[df.year == year]
    traces = []
    for i, continent in enumerate(df.continent.unique()):
        continent_df = filtered_df[filtered_df.continent == continent]
        traces.append({
            'x': continent_df.gdpPercap,
            'y': continent_df[yaxis_column],
            'text': continent_df.country,
            'customdata': continent_df.country,
            'marker': {
                'size': 10,
                'opacity': [
                    1.0
                    if (j in filtered_countries or
                        len(filtered_countries) == 0)
                    else 0.3
                    for j in list(continent_df.country)
                ],
                'line': {'width': 0.5, 'color': 'lightgrey'}
            },
            'name': continent,
            'mode': 'markers'
        })
    return {
        'data': traces,
        'layout': {
            'xaxis': {
                'title': 'GDP per Capita', 'type': 'log',
                'range': [math.log10(10), math.log10(120*1000)],
                'autorange': False
            },
            'yaxis': {
                'title': 'Life Expectancy',
                'range': [20, 90], 'autorange': False
            },
            'annotations': [{
                'x': 0, 'xref': 'paper', 'xanchor': 'left',
                'y': 1, 'yref': 'paper', 'yancor': 'bottom',
                'text': year,
                'font': {'size': 16}, 'showarrow': False
            }],
            'legend': {
                'x': 1, 'xanchor': 'right',
                'y': 0, 'yanchor': 'bottom',
                'bgcolor': 'rgba(255, 255, 255, 0.5)'
            },
            'margin': {'l': 40, 'r': 0, 't': 40, 'b': 40},
            'hovermode': 'closest', 'dragmode': 'lasso'
        }
    }


@app.callback(
    Output('graph-left', 'figure'),
    [Input('common-year-slider', 'value'),
     Input('graph-right', 'selectedData'),
     Input('graph-right', 'hoverData')])
def filterLeftPlot(sliderValue, selectedData, hoverData):
    figure = create_figure(sliderValue, selectedData, hoverData, 'lifeExp')
    figure['layout']['yaxis'] = {
        'title': 'Life Expectancy',
        'range': [10, 90], 'autorange': False
    }
    return figure


@app.callback(
    Output('graph-right', 'figure'),
    [Input('common-year-slider', 'value'),
     Input('graph-left', 'selectedData'),
     Input('graph-left', 'hoverData')])
def filterRightPlot(sliderValue, selectedData, hoverData):
    figure = create_figure(sliderValue, selectedData, hoverData, 'pop')
    figure['layout']['yaxis'] = {
        'title': 'Population', 'type': 'log',
        'range': [math.log10(100), math.log10(10*1000*1000*1000)],
        'autorange': False
    }
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
