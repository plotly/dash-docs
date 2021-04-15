# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

from dash_docs import styles
from dash_docs import tools
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)

layout = html.Div([
    html.H1('Download Component Examples and Reference'),
    rc.Markdown('''
    The Download component allows files to be directly downloaded from your
    app. These files include, but are not limited to, spreadsheets, images and
    text files , etc. The component opens a download dialog when the data
    property changes.

    Note that the following examples make use of the `prevent_initial_call`
    attribute to prevent the callbacks from being triggered when the app inputs
    are initially rendered. See <dccLink href="../advanced-callbacks#prevent-callbacks-from-being-executed-on-initial-load" children="Advanced Callbacks"/>. for more details.
    '''),
    html.H3('Downloading Content as Strings'),
    rc.Syntax(examples['download-text.py'][0], summary=rc.Markdown('''
        Here is an example show how to download content as a string, while showing the raw JSON:
    ''')),
    rc.Example(examples['download-text.py'][1]),

    html.Hr(),

    html.H3('Downloading Images'),
    rc.Syntax(examples['download-image.py'][0], summary=rc.Markdown('''
        To download a file from disk use `dcc.send_file`, taking care to
        specify the file path.
    ''')),
    rc.Example(examples['download-image.py'][1]),

    html.Hr(),

    html.H3('Downloading Dataframes'),
    rc.Syntax(examples['download-dataframe.py'][0], summary=rc.Markdown('''
        For downloading dataframes the many pandas export methods are supported:
    ''')),
    rc.Example(examples['download-dataframe.py'][1]),

    html.Hr(),

    html.H2('dcc.Download Component Properties'),
    rc.ComponentReference('Download'),
])
