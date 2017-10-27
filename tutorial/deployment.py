import dash_core_components as dcc
import styles

layout = [dcc.Markdown('''
# Deploying Dash Apps

By default, Dash apps run on `localhost` - you can only access them on your
own machine. To share a Dash app, you need to "deploy" your Dash app to a
server and open up the server's firewall to the public or to a restricted
set of IP addresses.

### Public Dash App Hosting

Dash apps can be hosted on a variety of third-party services: Digital Ocean,
Python Anywhere, Heroku, Google Cloud, Amazon Web Services, Azure, and more.
You can also deploy Dash apps directly on your own infrastructure.

Dash uses Flask under the hood. This makes deployment easy: you can deploy
a Dash app just like you would deploy a Flask app.
Almost every cloud server provider has a guide for deploying
Flask apps. For more, see the official [Flask Guide to Deployment](http://flask.pocoo.org/docs/0.12/deploying/)
or view the tutorial on deploying to Heroku below.

### Private Dash Apps

You can restrict access to Dash apps through the `dash-auth`
package, which provides authentication through HTTP Basic Auth and through
your [Plotly Cloud account](https://plot.ly/).
[Tutorial on Dash Authentication](/dash/authentication).

### On-Premise Dash Apps

You can use [Plotly On-Premise](https://plot.ly/products/on-premise).
It offers an enterprise-wide
Dash App Portal, easy git-based deployment, automatic URL
namespacing, built-in SSL support, LDAP authentication, and more.
[Request a Dash On-Premises demo](https://plot.ly/products/on-premise).

For existing customers, view the
[tutorial on deploying Dash Apps on Plotly On-Premise](/dash/deployment/on-premise).

### Dash and Flask

Dash apps are web applications. Dash uses [Flask]() as the web framework.
The underlying Flask app is available at `app.server`, that is:
'''),

dcc.SyntaxHighlighter('''import dash

app = dash.Dash(__name__)

server = app.server # the Flask app
''', language='python', customStyle=styles.code_container),

dcc.Markdown('''
You can also pass your own flask app instance into Dash:
'''),

dcc.SyntaxHighlighter('''import flask

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
''', language='python', customStyle=styles.code_container),

dcc.Markdown('''
By exposing this `server` variable, you can deploy Dash apps like you would
any Flask app. For more, see the official [Flask Guide to Deployment](http://flask.pocoo.org/docs/0.12/deploying/).
Note that

> While lightweight and easy to use, *Flask's built-in server is not suitable
> for production* as it doesn't scale well and by default serves only one
> request at a time

### Heroku Example

Heroku is one of the easiest platforms for deploying and managing public Flask
applications.

[View the official Heroku guide to Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction).

Here is a simple example. This example requires a Heroku account,
`git`, and `virtualenv`.

***

**Step 1. Create a new folder for your project:**
'''),

dcc.SyntaxHighlighter('''$ mkdir dash_app_example
$ cd dash_app_example
''', customStyle=styles.code_container),

dcc.Markdown('''

***

**Step 2. Initialize the folder with `git` and a `virtualenv`**

'''),

dcc.SyntaxHighlighter('''$ git init        # initializes an empty git repo
$ virtualenv venv # creates a virtualenv called "venv"
$ source venv/bin/activate # uses the virtualenv
''', customStyle=styles.code_container),

dcc.Markdown('''
`virtualenv` creates a fresh Python instance. You will need to reinstall your
app's dependencies with this virtualenv:
'''),

dcc.SyntaxHighlighter('''$ pip install dash
$ pip install dash-renderer
$ pip install dash-core-components
$ pip install dash-html-components
$ pip install plotly
''', customStyle=styles.code_container),

dcc.Markdown('''
You will also need a new dependency, `gunicorn`, for deploying the app:
'''),

dcc.SyntaxHighlighter('''$ pip install gunicorn''', customStyle=styles.code_container),

dcc.Markdown('''***
**Step 3. Initialze the folder with a sample app (`app.py`), a `.gitignore` file, `requirements.txt`, and a `Procfile` for deployment**

Create the following files in your project folder:

**`app.py`**
'''),

dcc.SyntaxHighlighter('''import dash
import dash_core_components as dcc
import dash_html_components as html
import os

app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

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
''', customStyle=styles.code_container, language='python'),

dcc.Markdown('''
***

**`.gitignore`**
'''),

dcc.SyntaxHighlighter('''venv
*.pyc
.DS_Store
.env
''', customStyle=styles.code_container),

dcc.Markdown('''
***

**`Procfile`**

'''),

dcc.SyntaxHighlighter('''web: gunicorn app:server
''', customStyle=styles.code_container),

dcc.Markdown('''
(Note that `app` refers to the filename `app.py`.
`server` refers to the variable `server` inside that file).

***

**`requirements.txt`**

`requirements.txt` describes your Python dependencies.
You can fill this file in automatically with:
'''),

dcc.SyntaxHighlighter('''$ pip freeze > requirements.txt
''', customStyle=styles.code_container),

dcc.Markdown('''
***

**4. Initialize Heroku, add files to Git, and deploy**
'''),

dcc.SyntaxHighlighter('''$ heroku create my-dash-app # change my-dash-app to a unique name
$ git add . # add all files to git
$ git commit -m 'Initial app boilerplate'
$ git push heroku master # deploy code to heroku
$ heroku ps:scale web=1  # run the app with a 1 heroku "dyno"
''', customStyle=styles.code_container, language='python'),

dcc.Markdown('''
You should be able to view your app at `https://my-dash-app.herokuapp.com`
(changing `my-dash-app` to the name of your app).

**5. Update the code and redeploy**

When you modify `app.py` with your own code, you will need to add the changes
to git and push those changes to heroku.

'''),

dcc.SyntaxHighlighter('''$ git status # view the changes
$ git add .  # add all the changes
$ git commit -m 'a description of the changes'
$ git push heroku master
''', customStyle=styles.code_container, language='python'),

dcc.Markdown('''

***

This workflow for deploying apps on heroku is very similar to how deployment
works with the Plotly On-Premise's Dash Deployment Server.
If you'd like to learn more, [please reach out](https://plot.ly/products/on-premise).
''')
]
