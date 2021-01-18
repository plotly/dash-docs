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

    > Dash Enterprise can be installed on the Kubernetes
    > services of
    > [AWS](https://go.plotly.com/dash-aws),
    > [Azure](https://go.plotly.com/dash-azure),
    > GCP,
    > or an
    > [on-premise Linux Server](https://plotly.com/dash/on-premises-linux/?utm_source=docs&utm_medium=workspace&utm_campaign=nov&utm_content=linux).
    > [Find out if your company is using Dash Enterprise](https://go.plotly.com/company-lookup)

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
    
    #### Sharing State between a Javascript Host app and an embedded Dash App

    You can find here a simple example illustrating multidirectional shared state, enabling the communication between your JavaScript host app and your Dash app.

    ![GIF showing how to use dash embedded](https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-embedded-js-host.gif)

    Inside your JavaScript host app, you simply provide the array or object that you want to share to your Dash app as a positional argument in Dash Embedded Components `renderDash()` function:
    ```js
    ...
    var setter = window.dash_embedded_component.renderDash(
        { url_base_pathname: "http://dash.tests:8050" }, 
        'dash-app', 
        sharedData
    );
    ```

    If you are using a React app, you can import the component and use it inside JSX:
    ```js
    import { DashApp } from "dash-embedded-component";

    window.React = React;
    window.ReactDOM = ReactDOM;
    window.PropTypes = PropTypes;

    class App extends React.Component {
        constructor(props) {
            super(props);
            this.state = {
                sharedData: {
                    myObject: {
                        clicks: 0,
                        aString: randomString(5),
                        data: myData,
                        multiplyFunc: (x, y) => { ... },
                        sumFunc: (x, y) => { ... },
                        storeDataFromDash: obj => { ... },
                        dashAppData: {}
                    },
                },
            };
            this.clickIncrement = this.clickIncrement.bind(this);
            ...
        }

        render() {
            return (
            <div className="App-Background">
                ...
                <div className="App-Content">
                <h1>Embedded Dash Application</h1>
                <DashApp config={{url_base_pathname: "http://dash.tests:8050"}} value={this.state.sharedData} />
                </div>
            </div>
            );
        }
    }
    ```

    Then inside your Dash app, simply use the `dash_embedded.ConsumerContext` and `dash_embedded.ConsumerFunction` components consume and use the shared data:

    ```python
    ...
    app.layout = ddk.App(
        [
            ...
            ddk.Card(
                [
                    ddk.CardHeader(title="Triggering Callbacks from Dash App & Host App"),
                    ConsumerContext(id="clicks", path=["myObject", "clicks"]),
                    ConsumerContext(id="data-one", path=["myObject", "data", "dataOne"]),
                    ConsumerContext(id="data-two", path=["myObject", "data", "dataTwo"]),
                    ...
                ],
                width=50,
            ),
            ddk.ControlCard(
                [
                    ddk.CardHeader(title="Triggering Host App Functions from Dash App"),
                    ConsumerFunction(
                        id="host-app-multiply", path=["myObject", "multiplyFunc"]
                    ),
                    ConsumerFunction(id="host-app-sum", path=["myObject", "sumFunc"]),
                    ddk.ControlItem(...),
                    ...
                ],
                width=50,
            ),
            ...
        ]
    )
    ...
    ```
    

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
