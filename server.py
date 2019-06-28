# -*- coding: utf-8 -*-
from dash import Dash

from flask import Flask, redirect

import os


app = Dash(
    __name__,
    external_stylesheets=[
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
    ]
)
server = app.server

app.config.suppress_callback_exceptions = True


@server.route('/deployment/on-premise')
def redirectDDS():
    return redirect("/dash-deployment-server", code=302)

@server.route('/dash-deployment-server/enviornment-variables')
def redirectEnvVar():
    return redirect("/dash-deployment-server/environment-variables", code=302)


@server.route('/dash-1-0-migration.')
def redirectMigration():
    return redirect("/dash-1-0-migration", code=302)


@server.route('/gallery')
def redirectGallery():
    return redirect("https://dash-gallery.plotly.host/Portal/", code=302)
