# -*- coding: utf-8 -*-
import dash
from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from flask import Flask, request, redirect
import json
import plotly.graph_objs as go
import os
from flask_cors import CORS

server = Flask(__name__, static_url_path='/static', static_folder='./static')
server.secret_key = os.environ.get('secret_key', 'secret')

app = Dash(
    __name__,
    server=server
)

app.css.config.serve_locally = False
app.scripts.config.serve_locally = False
app.config.suppress_callback_exceptions = True

@app.server.route('/deployment/on-premise')
def redirectDDS():
    return redirect("/dash-deployment-server", code=302)
