import dash
import dash_html_components as html
from dash_canvas import DashCanvas
import numpy as np

app = dash.Dash(__name__)

filename = 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Mitochondria%2C_mammalian_lung_-_TEM_%282%29.jpg'
canvas_width = 500


app.layout = html.Div([
    DashCanvas(id='canvas_image',
               tool='line',
               lineWidth=5,
               lineColor='red',
               filename=filename,
               width=canvas_width)
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
