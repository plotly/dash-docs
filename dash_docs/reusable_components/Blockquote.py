import dash_html_components as html
import dash_core_components as dcc

def s(string_block):
    return string_block.replace('    ', '')

def Blockquote():
    return dcc.Markdown(s(
    '''
    > This documentation is for the
    [Dash Enterprise](https://plot.ly/dash),
    Plotly's commercial platform for managing and improving
    Dash applications in your organization.
    [View the docs](/dash-enterprise/) or
    [request a trial](https://go.plot.ly/dash-doc).
    '''
    ))
