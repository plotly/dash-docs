# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html

from dash_docs import styles
from dash_docs import reusable_components as rc


layout = html.Div([
    rc.Markdown(
    """
    # Integrating Dash with Existing Web Apps

    Our recommend method for securely embedding Dash applications in existing
    Web Apps is to use the [Embedding Middleware](https://plotly.com/dash/embedding/)
    of Dash Enterprise. [Find out if your company is using Dash Enterprise](https://go.plotly.com/company-lookup)

    ## Dash Enterprise Embedding Middleware

    Dash Enterprise provides a first-class capability for embedding Dash apps
    as a microservice in 3rd party websites & Salesforce.

    This capability provides hooks into your existing website's login and
    authentication logic so that only  users who have logged into the
    existing host web application can view the embedded Dash application.

    To get started with Dash Enterprise Embedded Middleware, visit:
    [http://<your-dash-enterprise-hostname>/Docs/embedded-middleware](http://<your-dash-enterprise-hostname>/Docs/embedded-middleware),
    replacing `<your-dash-enterprise-hostname>` with the hostname of your
    licensed Dash Enterprise in your VPC. [Look up the hostname for your company's license](https://go.plotly.com/company-lookup)

    ## Embedding Public Apps in Public Websites with `<iframe>`

    The simplest approach to embedding Dash in an existing web application is to
    include an `<iframe>` element in your HTML.

    Note that this does not work if your
    application is private and does not integrate with your website's existing
    authentication or login system. To provide a single sign on experience,
    use Dash Enterprise Embedding Middleware.


     whose `src` attribute points
    towards the address of a deployed Dash app. This allows you to place your
    Dash app in a specific location within an existing web page with your
    desired dimensions:"""),
    rc.Markdown(
    '''
    ```html
    <iframe src="http://localhost:8050" width=700 height=600>
    ```
    ''')
])
