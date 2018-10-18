import dash_html_components as html

from tutorial.tools import merge

styles = {
    'underline': {
        'border-bottom': 'thin lightgrey solid',
        'margin-top': '50px'
    }
}

def Section(title, links, description=None, headerStyle={}):
    return html.Div(className='toc--section', children=[
        html.H2(title, style=merge(styles['underline'], headerStyle)),
        (
            html.Div(description)
            if description is not None else None
        ),
        html.Ul(links, className='toc--chapters')
    ])
