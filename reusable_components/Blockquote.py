import dash_html_components as html
import dash_core_components as dcc

def s(string_block):
    return string_block.replace('    ', '')

def Blockquote():
    return dcc.Markdown(s(
    '''
    > This documentation is for the
    [Dash Deployment Server](https://plot.ly/dash/pricing),
    Plotly's commercial platform for deploying and managing Dash applications.
    [View the docs](https://dash.plot.ly/dash-deployment-server/) or
    [request a trial](https://go.plot.ly/dash-doc).
    '''
    ))
