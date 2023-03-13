import math
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly import express as px
import pandas as pd


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig = px.scatter(df, x="Fruit", y="Amount", color="City")
fig.update_traces(hoverinfo="none", hovertemplate=None)

# This does not work because I'm not a PRO CodePen user.
external_stylesheets = ['https://codepen.io/rsreusser/pen/RwoBXpK.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.Div( id='my-hovers'),
    dcc.Graph( id='graph', figure=fig, clear_on_unhover=True )
])

@app.callback(
    Output('my-hovers', 'children'),
    Input('graph', 'hoverData')
)
def display_hover(hoverData):
    hovers = []
    if not hoverData:
        return []

    for pt in hoverData['points']:
        # TODO: Decide based on page size
        hoverLeft = pt['offsetX1'] > 200

        hovers.append(html.Div(
            className='hover {}'.format('hover-left' if hoverLeft else ''),
            style={
                # Be sure to round these to avoid fractional pixel offsets
                # Align veritcally with the middle of the bounding box
                'top': round(0.5 * (pt['offsetY0'] + pt['offsetY1'])),

                # Align to the left or right edge, depending on the hover direction
                'left': round(pt['offsetX0'] if hoverLeft else pt['offsetX1'])
            },
            children=[
                html.Div(
                    className='hover-content',
                    children=[html.Div('{} {}'.format(pt['y'], pt['x']))],
                ),
            ]
        ))
    return hovers

if __name__ == '__main__':
    app.run_server(debug=True)
