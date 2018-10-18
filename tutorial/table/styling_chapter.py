from collections import OrderedDict
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

import dash_table
from .utils import html_table, section_title


data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10"] * 2),
        ("Region", ["Montreal", "Vermont", "New York City"] * 2),
        ("Temperature", [1, -20, 3.512] * 2),
        ("Humidity", [10, 20, 30] * 2),
        ("Pressure", [2, 10924, 3912] * 2),
    ]
)

df = pd.DataFrame(data)

layout = html.Div('Styling')

