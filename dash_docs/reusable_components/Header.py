import dash_html_components as html


def Header(title):
    return html.Div(
        style={'borderBottom': 'thin lightgrey solid', 'marginRight': 20},
        children=[html.Div(title, style={'fontSize': 30})]
    )
