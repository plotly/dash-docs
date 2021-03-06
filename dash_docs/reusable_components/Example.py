import dash_html_components as html

def Example(example, style={}):
    return html.Div(example, className='example-container', style=style)
