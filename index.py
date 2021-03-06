#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash_docs.run import app, server

if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
