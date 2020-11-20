# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html

from dash_docs import styles
from dash_docs import reusable_components as rc


layout = html.Div([
    rc.Markdown(
    """
    # Embedding Dash Apps in other Web Platforms

    Our recommend method for securely embedding Dash applications in existing
    Web Apps is to use the [Embedding Middleware](https://plotly.com/dash/embedding/)
    of Dash Enterprise.

    Dash Enterprise can be
    installed on a Linux server at your company or the Kubernetes service
    of every major cloud:

    > - [Install Dash Enterprise on Azure](https://plotly.com/dash/azure/?utm_source=docs&utm_medium=integrating&utm_campaign=nov&utm_content=azure)
    > - [Install Dash Enterprise on AWS](https://plotly.com/dash/aws/?utm_source=docs&utm_medium=integrating&utm_campaign=nov&utm_content=aws)
    > - [Install Dash Enterprise on an on-premises Linux server](https://plotly.com/dash/on-premises-linux/?utm_source=docs&utm_medium=integrating&utm_campaign=nov&utm_content=linux)
    """),
    rc.Markdown(
    """
    > - Or, [find out if your company is using Dash Enterprise](https://go.plotly.com/company-lookup)
    """,
        className="red-links",
    ),
    rc.Markdown(
    """
    ## Dash Enterprise Embedding Middleware

    > If your company has licensed Dash Enterprise, then view the deployment
    > documentation by visiting
    >
    > **`https://<your-dash-enterprise-platform>/Docs/embedded-middleware`**
    >
    > (Replace `<your-dash-enterprise-platform>` with the hostname of your
    > licensed Dash Enterprise in your VPC).
    >
    > [Look up the hostname for your company's license](https://go.plotly.com/company-lookup)

    Dash Enterprise provides a first-class capability for embedding Dash apps
    as a microservice in 3rd party websites & Salesforce.

    This capability provides hooks into your existing website's login and
    authentication logic so that only  users who have logged into the
    existing host web application can view the embedded Dash application.

    To get started with Dash Enterprise Embedded Middleware, **visit:
    `https://<your-dash-enterprise-hostname>/Docs/embedded-middleware`**,
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
