# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig.update_traces(
    hovertemplate=None,
    hoverinfo="none"
)

# This does not work because I'm not a PRO CodePen user.
external_stylesheets = ['https://codepen.io/rsreusser/pen/RwoBXpK.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.Div( id='my-hovers' ),

    html.Div( id='my-hovers-loader', className='hover hover-loader', children=[
        html.Div( className='hover-content', children='Loading…' )
    ]),

    dcc.Graph( id='my-graph', figure=fig, clear_on_unhover=True )
])

app.clientside_callback(
    """
    function(hoverData) {
        if (!hoverData || !hoverData.points || !hoverData.points.length) {
            return { display: 'none' };
        }
        var pt = hoverData.points[0];
        return {
            top: Math.round((pt.offsetY0 + pt.offsetY1) / 2),
            left: Math.round(pt.offsetX1)
        };
    }
    """,
    Output('my-hovers-loader', 'style'),
    Input('graph', 'hoverData')
)

@app.callback(
    Output('my-hovers', 'children'),
    Input('my-graph', 'hoverData')
)
def display_hover(hoverData):
    if not hoverData:
        return []

    hovers = []
    for pt in hoverData['points']:
        left = pt['offsetX1'] + 2
        top = (pt['offsetY0'] + pt['offsetY1']) / 2

        hovers.append(html.Div(
            className='hover hover-right',
            style={
                'top': round((pt['offsetY0'] + pt['offsetY1']) / 2),
                'left': pt['offsetX1']
            },
            children=[
                html.Div(
                    className='hover-content',
                    children=[html.Div('{} {}'.format(pt['y'], pt['x']))],
                ),
            ],
        ))
    return hovers

if __name__ == '__main__':
    app.run_server(debug=True)
