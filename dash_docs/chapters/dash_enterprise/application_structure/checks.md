## CHECKS

`CHECKS` is an optional text file that allows you to precisely modify Dash 
Enterprise's app health diagnostic checks.

> **`CHECKS` is only available on Dash Enterprise Single Server.** Similar functionality 
> for Dash Enterprise Kubernetes is available via the `app.json` file. 

By default, Dash Enterprise will wait 10 seconds after starting each container 
before assuming it is healthy and continuing with the deployment. Once this happens for 
all of the containers associated with the deployed Dash app, web traffic will then 
be directed to the new containers. Dash Enterprise will then wait an additional 60 
seconds before terminating the processes in the old containers; this gives time
longer running connections some time to finish processing their request.
The checks are compared to the detected `web` process in your  
`Procfile`.

We recommend that you include a `CHECKS` file in your app's root directory if your 
Dash app takes more than the default 10 seconds to boot or load data into memory 
in order to prevent downtime during deployments. It must be place in your app's root
request(s) to your Dash application to determine that it is healthy and ready to 
receive traffic before finishing the deployment.

There are four settings you can modify in your `CHECKS` file:

1. `WAIT` corresponds to the allocated time before Dash Enterprise visits the health check URL
2. `TIMEOUT` corresponds to the time allowed for checks to be carried out
3. `ATTEMPTS` corresponds to the number of allowed check attempts
4. URL corresponds to the target URL of the health check

By default, Dash Enterprise will wait 10 seconds after starting each container 
before assuming it is up and proceeding with the deploy. 

Other instructions must be specified in the form of a relative 
link, followed by content that Dash Enterprise should find in the response. 
The expected content can be omitted if text content is not relevant. 

```
WAIT=15
TIMEOUT=10
ATTEMPTS=3
/<your-dash-app>/_dash-layout analytics
```

In this example, Dash Enterprise will visit the URL `/<your-dash-app>/_dash-layout` and check that the response contains the text "analytics". In practice, replace `<your-dash-app>` with the name of your Dash app on Dash Enterprise. The /_dash-layout path will return the JSON-ified content of your app.layout. Replace "analytics" with text that appears in the /_dash-layout. You can visit this URL directly to inspect its contents at `https://<your-dash-enterprise>/<your-dash-app>/_dash-layout`.

If "analytics" is in the response within 10 seconds (`TIMEOUT`), Dash Enterprise will consider the check to be passed and will begin serving traffic to this new version. If "analytics" isn't in the response after 10 (`TIMEOUT`) seconds, Dash enterprise will try two more times (`ATTEMPTS`). If the next two attempts fail, Dash Enterprise will abort the deployment and keep the previous version of the app running.

The expected content (in the previous example "analytics") can be omitted. If omitted, Dash Enterprise checks that the response has a 200 Status Code.

Another use for a `CHECKS` file allowing your Dash app enough time to fully load. 
In this example, we are simulating an app with a two-minute loading time with
`time.sleep(120)`. 


```python
import dash
import dash_design_kit as ddk
import dash_core_components as dcc
import dash_html_components as html
import time

# simulate long loading time
time.sleep(120)

app = dash.Dash(__name__)
server = app.server
app.layout = ddk.App([
    html.H1('hello world')
])

if __name__ == '__main__':
    app.run_server(debug=False)
```

By including a `CHECKS` file, the new version won't accept traffic until the check passes, and will prevent the end user from encountering downtime while the new version of the app is getting spun up. The check can be configured to wait 120 seconds.

```
WAIT=120
TIMEOUT=10
ATTEMPTS=3
/<your-dash-app>/
```

You can also create your own health check by writing a custom Flask endpoint. In the following example, we include  `@app.server.route('/status')` 
that returns `OK'. In practice, you can place whatever health checks you would like within this 
function. This might include checking the uptime for 3rd party services like databases or APIs.

```python
import dash
import dash_design_kit as ddk
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)
server = app.server
app.layout = ddk.App([
    html.H1('hello world'),
])

# Custom status file for the deployment CHECKS
@app.server.route('/status')
def update_status():
    # Include custom health logic in here
    return 'OK'

    
if __name__ == '__main__':
    app.run_server(debug=False)

```

The example app's `CHECKS` file will then resemble:

```
WAIT=15
TIMEOUT=130
ATTEMPTS=2

/<your-dash-app>/status OK

```

---
