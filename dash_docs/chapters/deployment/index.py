import dash_core_components as dcc
import dash_html_components as html
from dash_docs import styles
from dash_docs import reusable_components as rc

layout = html.Div(children=[
    rc.Markdown('''
    # Deploying Dash Apps

    By default, Dash apps run on `localhost` - you can only access them on your
    own machine. To share a Dash app, you need to "deploy" it to a server.

    Our recommend method for securely deploying Dash applications is
    [Dash Enterprise](https://plotly.com/dash). Dash Enterprise can be
    installed on a Linux server at your company or the Kubernetes service
    of every major cloud:

    > - [Install Dash Enterprise on Azure](https://plotly.com/dash/azure/?utm_source=docs&utm_medium=deployment&utm_campaign=nov&utm_content=azure)
    > - [Install Dash Enterprise on AWS](https://plotly.com/dash/aws/?utm_source=docs&utm_medium=deployment&utm_campaign=nov&utm_content=aws)
    > - [Install Dash Enterprise on an on-premises Linux server](https://plotly.com/dash/on-premises-linux/?utm_source=docs&utm_medium=deployment&utm_campaign=nov&utm_content=linux)
    > - Or, [find out if your company is using Dash Enterprise](https://go.plotly.com/company-lookup)

    ## Dash Enterprise Deployment

    > If your company has licensed Dash Enterprise, then view the deployment
    > documentation by visiting
    >
    > **`https://<your-dash-enterprise-platform>/Docs/dash-enterprise`**
    >
    > (Replace `<your-dash-enterprise-platform>` with the hostname of your
    > licensed Dash Enterprise in your VPC).
    >
    '''),

    rc.Markdown('''
    > [Look up the hostname for your company's license](https://go.plotly.com/company-lookup)
    ''',
        className='red-links'
    ),

    rc.Markdown('''
    [Dash Enterprise](https://plotly.com/dash/)
    is Plotly's commercial product for developing & deploying
    Dash Apps on your company's on-premises Linux servers or VPC
    ([AWS](https://plotly.com/dash/aws), [Google Cloud](https://plotly.com/dash), or [Azure](https://plotly.com/dash/azure)).

    In addition to [easy, git-based deployment](https://plotly.com/dash/app-manager), the Dash Enterprise platform provides a complete Analytical App Stack.
    This includes:
    - [LDAP & SAML Authentication Middleware](https://plotly.com/dash/authentication)
    - [Data Science Workspaces](https://plotly.com/dash/workspaces)
    - [High Availability & Horizontal Scaling](https://plotly.com/dash/kubernetes)
    - [Job Queue Support](https://plotly.com/dash/job-queue)
    - [Enterprise-Wide Dash App Portal](https://plotly.com/dash/app-manager)
    - [Design Kit](https://plotly.com/dash/design-kit)
    - [Reporting, Alerting, Saved Views, and PDF Reports](https://plotly.com/dash/snapshot-engine)
    - [Dashboard Toolkit](https://plotly.com/dash/toolkit)
    - [Embedding Dash apps in Existing websites or Salesforce](https://plotly.com/dash/embedding)
    - [AI App Catalog](https://plotly.com/dash/ai-and-ml-templates)
    - [Big Data Best Practices](https://plotly.com/dash/big-data-for-python)
    - [GPU support](https://plotly.com/dash/gpu-dask-acceleration)

    ![The Analytical App Stack](/assets/images/dds/stack.png)

    ## Heroku for Sharing Public Dash apps for Free

    Heroku is one of the easiest platforms for deploying and managing public Flask
    applications. The git & buildpack-based deployment of UIs of Heroku and Dash Enterprise
    are nearly identical, enabling an easy transition to Dash Enterprise if you
    are already using Heroku.

    [View the official Heroku guide to Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction).

    Here is a simple example. This example requires a Heroku account,
    `git`, and `virtualenv`.

    ***

    **Step 1. Create a new folder for your project:**
    '''),

    rc.Markdown('''
    ```shell
    $ mkdir dash_app_example
    $ cd dash_app_example
    ```
    ''', style=styles.code_container),

    rc.Markdown('''

    ***

    **Step 2. Initialize the folder with `git` and a `virtualenv`**

    '''),

          rc.Markdown('''
          ```shell
          $ git init        # initializes an empty git repo
          $ virtualenv venv # creates a virtualenv called "venv"
          $ source venv/bin/activate # uses the virtualenv
          ```
          ''',style=styles.code_container),

          rc.Markdown('''
`virtualenv` creates a fresh Python instance. You will need to reinstall your
app's dependencies with this virtualenv:
'''),

          rc.Markdown('''
          ```shell
          $ pip install dash
          $ pip install plotly
          ```
          ''', style=styles.code_container),

          rc.Markdown('''
You will also need a new dependency, `gunicorn`, for deploying the app:
'''),

          rc.Markdown('''
          ```shell
          $ pip install gunicorn
          ```
          ''', style=styles.code_container),

          rc.Markdown('''***
**Step 3. Initialize the folder with a sample app (`app.py`), a `.gitignore` file, `requirements.txt`, and a `Procfile` for deployment**

Create the following files in your project folder:

**`app.py`**
'''),

    rc.Markdown('''
    ```python
    import os

    import dash
    import dash_core_components as dcc
    import dash_html_components as html

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    server = app.server

    app.layout = html.Div([
        html.H2('Hello World'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA'
        ),
        html.Div(id='display-value')
    ])

    @app.callback(dash.dependencies.Output('display-value', 'children'),
                  [dash.dependencies.Input('dropdown', 'value')])
    def display_value(value):
        return 'You have selected "{}"'.format(value)

    if __name__ == '__main__':
        app.run_server(debug=True)
    ```
    ''', style=styles.code_container),

          rc.Markdown('''
***

**`.gitignore`**
'''),

          rc.Markdown('''
          ```shell
          venv
          *.pyc
          .DS_Store
          .env
          ```
          ''', style=styles.code_container),

          rc.Markdown('''
          ***

          **`Procfile`**
          '''),

          rc.Markdown('''
          ```shell
          web: gunicorn app:server
          ```
          ''', style=styles.code_container),

          rc.Markdown('''
(Note that `app` refers to the filename `app.py`.
`server` refers to the variable `server` inside that file).

***

**`requirements.txt`**

`requirements.txt` describes your Python dependencies.
You can fill this file in automatically with:
'''),

          rc.Markdown('''
          ```shell
          $ pip freeze > requirements.txt
          ```
          ''', style=styles.code_container),

          rc.Markdown('''
***

**4. Initialize Heroku, add files to Git, and deploy**
'''),

    rc.Markdown('''
    ```shell
    $ heroku create my-dash-app # change my-dash-app to a unique name
    $ git add . # add all files to git
    $ git commit -m 'Initial app boilerplate'
    $ git push heroku master # deploy code to heroku
    $ heroku ps:scale web=1  # run the app with a 1 heroku "dyno"
    ```
    ''', style=styles.code_container),

          rc.Markdown('''
You should be able to view your app at `https://my-dash-app.herokuapp.com`
(changing `my-dash-app` to the name of your app).

**5. Update the code and redeploy**

When you modify `app.py` with your own code, you will need to add the changes
to git and push those changes to heroku.

'''),

    rc.Markdown('''
    ```shell
    $ git status # view the changes
    $ git add .  # add all the changes
    $ git commit -m 'a description of the changes'
    $ git push heroku master
    ```
''', style=styles.code_container),

          rc.Markdown('''

***

This workflow for deploying apps on Heroku is very similar to how deployment
works with the Plotly Enterprise's Dash Enterprise.
[Learn more](https://plotly.com/dash/) or [get in touch](https://plotly.com/get-demo/).
''')
])
