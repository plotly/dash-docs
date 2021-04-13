import dash_html_components as html
import dash_core_components as dcc

from dash_docs import reusable_components as rc

layout = html.Div([
    rc.Markdown('''
        ## Introduction to Dash

        Downloaded 500,000 times per month, Dash is the original low-code framework 
        for rapidly building data apps in Python, R, Julia, and .NET.

        Written on top of Plotly.js and React.js,
        Dash is ideal for building and deploying data apps
        with customized user interfaces in pure Python.
        It's particularly suited for anyone who works with data in Python.

        Through a couple of simple patterns, Dash abstracts away all of the
        technologies and protocols that are required to build a full-stack
        Web app with interactive data visualization.
        
        Dash is simple enough that you can bind a user interface
        to your Python code in less than 10 minutes.

        Dash apps are rendered in the web browser. You can deploy your apps
        to VMs or [Kubernetes clusters](https://plotly.com/dash/kubernetes/) and then share them through URLs.
        Since Dash apps are viewed in the web browser, Dash is inherently
        cross-platform and mobile ready.

        There is a lot behind the framework. To learn more about how it is built
        and what motivated Dash, read our post 
        [Dash is React for Python](https://medium.com/plotly/dash-is-react-for-python-r-and-julia-c75822d1cc24).

        Dash is an open source library, released under the permissive MIT license.
        [Plotly](https://plotly.com) also develops Dash and offers a [platform for writing and deploying Dash
        apps in an enterprise environment](https://plotly.com/dash).
        If you're interested, [please get in touch](https://plotly.com/get-demo/).

    '''.replace('  ', '')),
])
