# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import styles
from server import app

def s(string_block):
    return string_block.replace('    ', '')

# # # # # # #
# Authenticating to Plotly Enterprise with SSH
# # # # # # #
Ssh = html.Div(children=[
    html.H1('Authenticating to Plotly Enterprise with SSH'),

    dcc.Markdown(s('''

    From Plotly Enterprise 2.4.0, you can deploy your apps using
    either HTTPS or SSH. If you are deploying with HTTPS, then you do not
    need to set up an SSH key. Thus, you can skip this tutorial and go
    straight to
    [Deploy Dash Apps on Plotly Enterprise](https://dash.plot.ly/dash-deployment-server/deployment).

    &nbsp;

    If you are deploying with SSH then you need to add a SSH Key to the
    Dash Deployment Server. SSH Keys are used to authenticate your git
    session with this server. Deploying with SSH takes a little bit more
    time to set up but it allows you to deploy without typing in your
    username and password each time. Continue below for instructions on
    how to generate and add a SSH Key.

    ***

    ''')),

    dcc.Markdown(s('''
    #### Already Have an SSH Key?

    If you already have an SSH key that you've used in other
    services, you can use that key instead of generating a new one.
    For instructions on how to add an existing SSH Key to the Dash Deployment
    Server, jump to **Copy and Add SSH Key**.

    ***
    ''')),

    dcc.Markdown(s('''
    #### Which OS Are You Using?

    ''')),

    dcc.RadioItems(
        id='platform',
        options=[
            {'label': i, 'value': i} for i in
            ['Windows', 'Mac', 'Linux']],
        value='Windows',
        labelStyle={'display': 'inline-block'}
    ),
    html.Div(id='instructions')
])

@app.callback(Output('instructions', 'children'),
              [Input('platform', 'value')])
def display_instructions(platform):
    return [

        (dcc.Markdown(s('''
        These instructions assume that you are using
        **Git Bash** on Windows, which is included in the
        official [Git for Windows release](https://git-scm.com/download/win).
        ''')) if platform == 'Windows' else
        ''),

        dcc.Markdown(s('''
        ***

        #### Generate a New SSH Key

        ''')),

        dcc.Markdown(
        '**1. Open Git Bash**' if platform == 'Windows' else
        '**1. Open Terminal**'
        ),

        dcc.Markdown(s('''
        **2. Generate Key**

        This command will walk you
        through a few instructions.
        ''')),

        dcc.SyntaxHighlighter(
            ('$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"'),
            customStyle=styles.code_container,
            language='python'
        ),

        dcc.Markdown(s('''
        ***

        #### Check the SSH-Agent

        **1. Ensure the ssh-agent is running:**
        ''')),

        dcc.SyntaxHighlighter(
            ('$ eval $(ssh-agent -s)' if platform == 'Windows' else
             '$ eval "$(ssh-agent -s)"'),
            customStyle=styles.code_container,
            language='python'
        ),

        dcc.Markdown(s('''
        **2. Run `ssh-add`**

        Replace `id_rsa` with the name of the key that you
        created above if it is different.
        ''')),

        dcc.SyntaxHighlighter(
            ('$ ssh-add ~/.ssh/id_rsa' if platform == 'Windows' else
             '$ ssh-add -k ~/.ssh/id_rsa'),
            customStyle=styles.code_container,
            language='python'
        ),

        dcc.Markdown(s('''
        ***

        #### Copy and Add SSH Key

        **1. Copy the SSH key to your clipboard.**

        Replace `id_rsa.pub` with the name of the key that you
        created above if it is different.

        ''')),

        dcc.SyntaxHighlighter(
            ('$ clip < ~/.ssh/id_rsa.pub' if platform == 'Windows' else
             '$ pbcopy < ~/.ssh/id_rsa.pub' if platform == 'Mac' else
             '$ sudo apt-get install xclip\n$ xclip -sel clip < ~/.ssh/id_rsa.pub'),
            customStyle=styles.code_container,
            language='python'
        ),

        dcc.Markdown(s('''
        **2. Open the Dash Deployment Server UI**

        You can find the Dash Deployment Server UI by clicking on "Dash App" in your
        Plotly Enterprise's "Create" menu.

        > *The Dash App item in the Create menu takes you to the Dash Deployment Server UI*
        ''')),

        html.Img(
            alt='Dash App Create Menu',
            src='https://github.com/plotly/dash-docs/raw/master/images/dds/open-dds-ui.png',
            style={
                'width': '100%', 'border': 'thin lightgrey solid',
                'border-radius': '4px'
            }
        ),

        dcc.Markdown(s('''
        **3. Add SSH Key**

        Click **SSH Keys** in the top navigation menu of the Dash
        Deployment Server interface. Here, select **Add Key** and in the 'Add
        SSH Key' modal, paste in your SSH Key.
        ''')),

        html.Img(
            alt='Add SSH Key',
            src='https://github.com/plotly/dash-docs/raw/master/images/dds/add-ssh-key.png',
            style={
                'width': '100%', 'border': 'thin lightgrey solid',
                'border-radius': '4px'
            }
        ),

        dcc.Markdown(s('''
        **4. Confirm it Has Been Added**

        Once you've added an SSH key, it should be added to you list of SSH
        Keys like the image below.
        ''')),

        html.Img(
            alt='List of SSH Keys',
            src='https://github.com/plotly/dash-docs/raw/master/images/dds/list-of-ssh-keys.png',
            style={
                'width': '100%', 'border': 'thin lightgrey solid',
                'border-radius': '4px'
            }
        ),

        dcc.Markdown(s('''
        ***

        #### Modify SSH Config

        Next, specify a custom port in your SSH config. By default, this should be
        `3022` but your server administrator may have set it to something different.

        This file is located in `~/.ssh/config`. If it's not there, then create it.
        Add the following lines to
        this file, replacing `your-dash-app-manager` with the domain of
        your Dash Deployment Server (without `http://` or `https://`).
        ''')),

        dcc.SyntaxHighlighter('''Host your-dash-app-manager
        Port 3022''', customStyle=styles.code_container),

        (dcc.Markdown('''
        If you're having trouble opening this file, you can run `$ open ~/.ssh/config`
        which will open the file using your default editor. If the file doesn't exist,
        then you can open that hidden folder with just `$ open ~/.ssh`
        ''') if platform == 'Mac' else ''),

        (dcc.Markdown('''
        Please be careful not to save your SSH config as a .txt file as
        it will not be recognized by Git when deploying your applications. If you are using
        Notepad to create your SSH config, you can force the removal of the .txt extension
        by naming the file "config", including the quotes, in the Save As dialog box.
        ''') if platform == 'Windows' else ''),


        dcc.Markdown(s('''
        ***

        Continue on to **Initialize Dash Apps on Plotly Enterprise**.
        '''))
    ]

# # # # # # #
# Initialize
# # # # # # #
Initialize = html.Div(children=[
    html.H1('Initialize App on Plotly Enterprise'),

    dcc.Markdown(s('''
        ***

        1. Navigate to the Dash Deployment Server UI
    ''')),

    html.Img(
        alt='Dash Deployment Server UI Add App Interface',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/open-dds-ui.png',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
        2. In the top right-hand corner select 'Create App'
        3. The 'Create Dash App' modal should appear. Let’s name your Dash App and hit 'Create'.
        App names must start with a lower case letter and may contain only lower case letters, numbers, and -.
        It is important to keep in mind that this name is going to be part of the URL of your application.

    ''')),

    html.Img(
        alt='Dash Deployment Server UI Add App Interface',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/add-app.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''

        4. The dash app should appear in your list of 'Apps'. Simply click on the dash app name.

    ''')),

    html.Img(
        alt='Dash Deployment Server UI Add App Interface',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/list-of-apps.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''

        5. Now that you’ve created this app, advance to the next chapter:
        **Deploy Requirements**

    ''')),
])

# # # # # # #
# Requirements
# # # # # # #
Requirements = html.Div(children=[
    html.H1('Deploy Requirements'),

    dcc.Markdown(s(
    '''
    ***

    When it comes time to deploy dash apps to the Dash Deployment Server, there
    are a few files required for successful deployment. Below, is a common
    dash app folder structure and a brief description of each files function.

    ## Files

    ```
    dash_app/
    |-- assets/
       |-- typography.css
       |-- header.css
       |-- custom-script.js
    |-- app.py
    |-- config.py
    |-- .gitignore
    |-- Procfile
    |-- requirements.txt
    |-- runtime.txt
    ```

    &nbsp;

    `app.py` - defines the dash application.

    `config.py` - an optional file for configurations.

    `.gitignore` - determine which files and folders are ignored.

    `Procfile` - declares what commnads are run by app's containers.

    `requirements.txt` - describes your python dependencies.

    `runtime.txt` - specifies python runtime.

    &nbsp;

    To learn more about local assests (stylesheets and scripts) see [here](https://dash.plot.ly/external-resources).

    '''))
])


# # # # # # #
# Deploy App
# # # # # # #
Deploy = html.Div(children=[
    html.H1('Deploy Dash App on Plotly Enterprise'),

    dcc.Markdown(s(
    '''
    ***

    This tutorial will instruct you on how to deploy an app to your Dash
    Deployment Server. Below, you can either choose to deploy a cloned sample
    app, create a new app following the tutorial, or an existing app that you
    created locally and are ready to deploy. However, first ensure that you have
    [initialized the app](https://dash.plot.ly/dash-deployment-server/initialize).
    Additionally, check the app you are deploying has the
    [required files](https://dash.plot.ly/dash-deployment-server/deploy-requirements).

    ''')),

    dcc.Markdown(s(
    '''
    ***

    #### Which OS Are You Using?

    ''')),

    dcc.RadioItems(
        id='platform-2',
        options=[
            {'label': i, 'value': i} for i in
            ['Windows', 'Mac', 'Linux']],
        value='Windows',
        labelStyle={'display': 'inline-block'}
    ),
    html.Div(id='instructions-2'),
    dcc.RadioItems(
        id='deploy-method',
        options=[
            {'label': i, 'value': i} for i in
            ['HTTPS', 'SSH']],
        value='HTTPS',
        labelStyle={'display': 'inline-block'}
    ),
    html.Div(id='remote-and-deploy-instructions'),

])


@app.callback(Output('instructions-2', 'children'),
              [Input('platform-2', 'value')])
def display_instructions2(platform):
    return [
        dcc.Markdown(s(
        '''

        ***

        #### What Would You Like To Do?

        If you haven't deployed an app you can get started by selecting
        **Clone Sample App** to clone our sample app, which is already setup
        for for deployment. Alternatively, you can select **Create New App** to
        run through creating and deploying an app. Otherwise, if you already
        have an exisiting app locally that you would like to deploy,
        then select **Deploy Existing App**.

        &nbsp;

        ''')),

        dcc.Tabs(id="tabs", children=[
            dcc.Tab(label='Clone Sample App', children=[
                html.Div([
                    dcc.Markdown(s(
                    '''

                    &nbsp;

                    #### Clone the [Dash On Premise Sample App](https://github.com/plotly/dash-on-premise-sample-app) from GitHub.

                    ''')),

                    ('In Git Bash, run: ' if platform == 'Windows' else ''),

                    dcc.SyntaxHighlighter(s(
                    '''
$ git clone https://github.com/plotly/dash-on-premise-sample-app.git
                    '''),customStyle=styles.code_container
                    ),

                    dcc.Markdown(s(
                    '''
                    ***

                    #### Modify `config.py`

                    Read through `config.py` and modify the values as necessary.
                    If Dash Deployment Server was set up with "path-based routing"
                    (the default), then you will just need to change the
                    `DASH_APP_NAME` to be equal to the name of the Dash app that you
                    set earlier.
                    ''')),

                    dcc.Markdown(s(
                    '''
                    ***

                    #### Configure your Plotly Enterprise server to be your Git remote

                    In the root of your folder, run the following command to create a
                    remote host to your new app on Plotly Enterprise.

                    &nbsp;

                    ##### Which Deployment Method Are You Using?

                    ''')),
                ])
            ]),
            dcc.Tab(label='Create New App', children=[
                html.Div([
                    dcc.Markdown(s(
                    '''

                    &nbsp;

                    #### Create a New Folder
                    ''')),

                    dcc.SyntaxHighlighter('''
$ mkdir dash_app_example
$ cd dash_app_example
                    ''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''

                    ***

                    #### Initialize the Folder with `git` and a `virtualenv`

                    ''')),

                    dcc.SyntaxHighlighter(
                    '''
$ git init # initializes an empty git repo
$ virtualenv venv # creates a virtualenv called "venv"
$ source venv/bin/activate # uses the virtualenv
                    ''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    `virtualenv` creates a fresh Python instance. You will need
                    to reinstall your app's dependencies with this virtualenv:
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''
$ pip install dash
$ pip install dash-renderer
$ pip install dash-core-components
$ pip install dash-html-components
$ pip install plotly
                    ''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
You will also need a new dependency, `gunicorn`, for deploying the app:
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''
$ pip install gunicorn
                    ''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
***
#### Create Relevant Files For Deployment

Create the following files in your project folder:

**`app.py`**
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''
import os

import dash
import dash_core_components as dcc
import dash_html_components as html


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

                    dcc.Markdown(s('''
***

**`.gitignore`**
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''
venv
*.pyc
.DS_Store
.env
                    ''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
***

**`Procfile`**

                    ''')),

                    dcc.SyntaxHighlighter(
                    '''
web: gunicorn app:server
                    ''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
(Note that `app` refers to the filename `app.py`.
`server` refers to the variable `server` inside that file).

***

**`requirements.txt`**

`requirements.txt` describes your Python dependencies.
You can fill this file in automatically with:
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''
$ pip freeze > requirements.txt
                    ''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    ***

                    #### Configure your Plotly Enterprise server to be your Git remote

                    In the root of your folder, run the following command to create a
                    remote host to your new app on Plotly Enterprise.

                    &nbsp;

                    ##### Which Deployment Method Are You Using?

                    ''')),
                ])
            ]),
            dcc.Tab(label='Deploy Existing App', children=[
                html.Div([
                    dcc.Markdown(s(
                    '''

                    &nbsp;

                    #### Initialize the Folder With Git


                    ''')),

                    dcc.SyntaxHighlighter(
                    '''
$ cd <your-folder-name>
$ git init # initializes an empty git repo
                    ''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    ***

                    #### Check Deploy Requirements

                    Ensure that you have met all deploy requirements. See,
                    [**Deploy Requirements**](https://dash.plot.ly/dash-deployment-server/deploy-requirements).
                    If you're satisfied, advance to
                    **Configure your Plotly Enterprise server to be your Git remotes**.

                    ***

                    #### Configure your Plotly Enterprise server to be your Git remote

                    In the root of your folder, run the following command to create a
                    remote host to your new app on Plotly Enterprise.

                    &nbsp;

                    ##### Which Deployment Method Are You Using?

                    ''')),
                ])
            ]),
        ]),

]

@app.callback(Output('remote-and-deploy-instructions', 'children'),
              [Input('deploy-method', 'value')])
def display_instructions2(method):
    return [
        dcc.SyntaxHighlighter(s(
        '''
    $ git remote add plotly dokku@your-dash-app-manager:your-dash-app-name
        ''' if method == 'SSH' else '''
    $ git remote add plotly https://your-dash-app-manager/GIT/your-dash-app-name
        '''),
        customStyle=styles.code_container,
        language='python'
        ),

        dcc.Markdown(s(
        '''
    &nbsp;

    Replace `your-dash-app-name` with the name of your Dash app that you supplied
    in the Dash Deployment Server and `your-dash-app-manager` with the domain of the
    Dash Deployment Server.

    For example, if your Dash app name was `my-first-dash-app`
    and the domain of your organizations Dash Deployment Server was `dash.plotly.acme-corporation.com`,
    then this command would be
    `git remote add plotly dokku@dash.plotly.acme-corporation.com:my-first-dash-app`.
        ''' if method == 'SSH' else '''
    &nbsp;

    Replace `your-dash-app-name` with the name of your Dash app that you supplied
    in the Dash Deployment Server and `your-dash-app-manager` with the domain of the
    Dash Deployment Server.

    For example, if your Dash app name was `my-first-dash-app`
    and the domain of your organizations Dash Deployment Server was `dash.plotly.acme-corporation.com`,
    then this command would be
    `git remote add plotly https://dash.plotly.acme-corporation.com/GIT/my-first-dash-app`.
        ''')),

        dcc.Markdown(s(
        '''
        ***

        #### Deploying Changes

        Now, you are ready to upload this folder to your Dash Deployment Server.
        Files are transferred to the server using `git`:
        ''')),

        dcc.SyntaxHighlighter(s(
        '''
    $ git status # view the changed files
    $ git diff # view the actual changed lines of code
    $ git add .  # add all the changes
    $ git commit -m 'a description of the changes'
    $ git push plotly master
        '''), customStyle=styles.code_container, language='python'),

        dcc.Markdown(s(
        '''
        This commands will push the code in this folder to the
        Dash Deployment Server and while doing so, will install the
        necessary python packages and run your application
        automatically.

        Whenever you make changes to your Dash code,
        you will need to run those `git` commands above.

        If you install any other Python packages, add those packages to
        the `requirements.txt` file. Packages that are included in this
        file will be installed automatically by the Plotly Enterprise
        server.
        '''))
    ]

# # # # # # #
# Dash App Authentication
# # # # # # #
Authentication = html.Div(children=[
    html.H1('Dash App Authentication'),
    dcc.Markdown(s('''
    The `dash-auth` package provides login through your Plotly
    Enterprise accounts.

    #### Modify the `config.py` file

    This file contains several settings that are used in your app.
    It's kept in a separate file so that it's easy for you to
    transfer from app to app.
    *Read through this file and modify the variables as appropriate.*

    ''')),

    dcc.Markdown(s('''
    #### Redeploy your app

    Your app should now have a Plotly Enterprise login screen.
    You can manage the permissions of the app in your list of files
    at `https://<your-plotly-domain>/organize`.
    '''))
])

# # # # # # #
# Configuring System Dependencies
# # # # # # #
ConfigSys = html.Div(children=[
    html.H1('Configuring System Dependencies'),
    dcc.Markdown(s('''
    In some cases you may need to install and configure system
    dependencies. Examples include installing and configuring
    database drivers or the Java JRE environment.
    Plotly Enterprise supports these actions through an
    `apt-packages` file and a `predeploy` script.

    #### Install Apt Packages

    In the root of your application folder create a file called
    `apt-packages`. Here you may specify apt packages to be
    installed with one package per line. For example to install
    the ODBC driver we could include an `apt-packages` file that
    looks like:

    ''')),

    dcc.SyntaxHighlighter(s('''unixodbc
    unixodbc-dev
    '''), customStyle=styles.code_container, language="text"),

    dcc.Markdown(s('''

    #### Configure System Dependencies

    You may include a pre-deploy script that executes in
    your Dash App's environment. For the case of adding an
    ODBC driver we need to add ODBC initialization files into
    the correct systems paths. To do so we include the ODBC
    initialization files in the application folder and then
    copy them into system paths in the pre-deploy script.

    ##### Add A Pre-Deploy Script
    Let's generate a file to do this. Note that the file can
    have any name as we must specify the name in an application
    configuration file `app.json`.
    For the purposes of this example we assume we have
    named it `setup_pyodbc` and installed it in the root of our
    application folder.

    ''')),

    dcc.SyntaxHighlighter(s('''cp /app/odbc.ini /etc/odbc.ini
    cp /app/odbcinst.ini /etc/odbcinst.ini
    '''), customStyle=styles.code_container, language="text"),

    dcc.Markdown(s('''

    ##### Run Pre-Deploy Script Using `app.json`

    Next we must instruct Plotly Enterprise to run our `setup_pyodbc`
    file by adding a JSON configuration file named `app.json`
    into the root of our application folder.

    ''')),

    dcc.SyntaxHighlighter(s('''{
    \t"scripts": {
    \t\t"dokku": {
    \t\t\t"predeploy": "/app/setup_pyodbc"
    \t\t}
    \t}
    }
    '''), customStyle=styles.code_container, language='json'),

    dcc.Markdown(s('''
    ***

    Now when the application is deployed it will install the apt
    packages specified in `apt-packages` and run the setup file
    specified in `app.json`. In this case it allows us to install
    and then configure the ODBC driver.

    To see this example code in action
    [check out our ODBC example](https://github.com/plotly/dash-on-premise-sample-app/pull/3#issue-144272510)
     On-Premise application.
    '''))
])

# # # # # # #
# Redis
# # # # # # #
Redis = html.Div(children=[
    html.H1('Create and Link Redis Database'),

    dcc.Markdown(s('''
    Redis now works out of the box with the Dash Deployment Server.
    To see an example, check out our sample
    [Redis App](https://github.com/plotly/dash-redis-demo). For instruction
    on how to create and link a Redis Database, see below.
    ''')),

    dcc.Markdown(s('''
    #### Enable Redis Databases

    First navigate to the `8800/settings`, under **Special Options &
    Customizations** select **Enable Dash Customizations** and **Enable Redis
    Databases** for Dash Apps.
    ''')),

    html.Img(
        alt='Enable Redis Databases',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/enable-redis.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    #### Create and Link (via Interface)

    In Plotly Enterprise 2.5.0 it is possible to create and link a Redis
    Database to your dash app using the Dash Deployment Server UI.
    Here, you have two options:

    1. Create a database before initializing an app.
    2. Create and link a database after an app has been initialized.

    ##### Create a Database Before Initializing an App

    If you haven't initialized an app yet, select **Databases** situated in the
    top navigation menu. Next, click **Create Database**, then in the
    'Create Database' modal, add the name of your database
    (for example, `redis-one`). Once it has been created, you'll notice that
    it is added to your list of databases.
    ''')),

    html.Img(
        alt='Create Database',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/create-redis-db.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    Now, navigate to Apps and create a new app (for more info see ['Create and
    Deploy an App'](https://www.dash.plot.ly/dash-deployment-server/deployment)),
    in the 'Create App' modal you have the option of linking a databases.
    Here, use the dropdown to select the database that you just created
    (see image below).
    ''')),

    html.Img(
        alt='Link Database',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/link-redis-db.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    ##### Create and Link a Database After an App Has Been Initialized.

    In the Dash App Manager (`MANAGER/apps`), click on the app then navigate
    to the settings (`MANAGER/apps/<user>:<app-name>/settings`) page.
    In Databases, use the dropdown to select **create and link database**
    then click **Add**.

    ''')),

    html.Img(
        alt='Create and Link Database in App',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/create-and-link-redis-db.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    #### Create and Link (via Command Line)

    Whilst it is now possible to create and link Redis Databases via the
    interface, it is still possible to create and link a Redis database via
    the command line (using ssh):

    ```
    ssh dokku@YOUR_DASH_SERVER redis:create SERVICE-NAME
    ssh dokku@YOUR_DASH_SERVER redis:link SERVICE-NAME APP-NAME
    ```

    In the commands above, replace:
    * `YOUR_DASH_SERVER` with the name of your Dash server (same as when you run `git remote add`)
    * `SERVICE-NAME` with the name you want for your Redis service
    * `APP-NAME` with the name of your app (as specified in the Dash App Manager).

    '''))
])

# # # # # # #
# Env Vars
# # # # # # #
EnvVars = html.Div(children=[
    html.H1('Setting Environment Variables'),

    dcc.Markdown(s('''
    Environment variables are config values that can affect the way your app
    behaves. In Plotly Enterprise >2.5.0, you can add and remove
    sensitive data (e.g. API keys) via the Dash Deployment Server UI,
    rather than placing them in the repository.

    ''')),

    dcc.Markdown(s('''
    #### Add Environment Variables

    To add environment variables via the Dash Deployment Server UI,
    navigate to the application settings
    (`MANAGER/apps/<user>:<app-name>/settings`). Here, use the text boxes to
    add the environmental variable name and value. For example, `DASH_APP_FID`
    and `admin:0`.

    ''')),

    html.Img(
        alt='Add Environment Variables',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/add-env-variable.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    #### Delete Environment Variables

    To remove an environment variable via the Dash Deployment Server UI,
    navigate to the application settings
    (`MANAGER/apps/<user>:<app-name>/settings`). Here, simply click the red
    cross situated to the right-hand side of the environment variable.

    ''')),

    html.Img(
        alt='Delete Environment Variables',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/remove-env-variable.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),
])

# # # # # # #
# Local Directories
# # # # # # #
LocalDir = html.Div(children=[
    html.H1('Mapping Local Directories Examples and Reference'),
    html.Img(
        alt='Coming Soon',
        src='https://github.com/plotly/dash-docs/raw/master/images/building.png',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),
])

# # # # # # #
# Troubleshooting App Deployment
# # # # # # #
Troubleshooting = html.Div(children=[
    html.H1('Troubleshooting App Deployment'),

    dcc.Markdown(s('''
    #### Common Errors

    [insert section about commom mistakes and pitfalls ... and the workarounds.]

    ''')),

    # dcc.Markdown(s('''
    # #### Dash App Analytics
    #
    # After you have successfully deployed a dash app to the Dash Deployment
    # Server, you can monitor app performance via the app analytics and logs.
    # Here, navigate to the Dash Deployment Server UI, select the app
    # (`MANAGER/apps/<user>:<app-name>/overview`) to display the applications
    # analytics.
    # ''')),
    #
    # html.Img(
    #     alt='App Analytics',
    #     src='',
    #     style={
    #         'width': '100%', 'border': 'thin lightgrey solid',
    #         'border-radius': '4px'
    #     }
    # ),
    #
    # dcc.Markdown(s('''
    # #### Dash App Logs
    #
    # To view the logs, navigate to logs (`MANAGER/apps/<user>:<app-name>/logs`).
    # ''')),
    #
    # html.Img(
    #     alt='App Analytics',
    #     src='',
    #     style={
    #         'width': '100%', 'border': 'thin lightgrey solid',
    #         'border-radius': '4px'
    #     }
    # ),
    #
    # dcc.Markdown(s('''
    # #### Dash App Logs (via Command Line)
    #
    # Alternatively, the above can be accomplished via the command line.
    # To view the logs for a specific Dash app run the following command
    # in your terminal:
    #
    # ```
    # ssh dokku@<your-dash-domain> logs <your-app-name> --num -1
    # ```
    #
    # This will work for any app you have permission on, and uses the
    # same mechanism as pushing the app via ssh.
    #
    # **Options**
    # - `--num`, `-n`: The number of lines to display. By default, 100 lines are displayed.
    #    Set to -1 to display _all_ of the logs. Note that we only store logs from the latest app deploy.
    # - `--tail`, `-t`: Continuously stream the logs.
    # - `--quiet`, `-q`: Display the raw logs without colors, times, and names.
    # ''')),
    #
    # dcc.Markdown(s('''
    # #### Support
    #
    # If you encounter any issues deploying your app you can email
    # `onpremise.support@plot.ly`. It is helpful to include any error
    # messages you encounter as well as available logs. See below on how
    # to obtain Dash app logs as well as the Plotly Enterprise support
    # bundle.
    # ''')),
    #
    # dcc.Markdown(s('''
    # #### Enterprise Support Bundle
    #
    # If you're requested to send the full support bundle you can
    # download this from your Plotly Enterprise Server Manager
    # (e.g. `https://<your.plotly.domain>:8800`). Please note you
    # will need admin permissions to access the Server Manager.
    # Navigate to the Server Manager and then select the Support tab.
    # There you will see the option to download the support bundle.
    # '''))
])


Analytics = html.Div(children=[
    dcc.Markdown(s('''
    #### Dash App Analytics

    After you have successfully deployed a dash app to the Dash Deployment
    Server, you can monitor app performance via the app analytics and logs.
    Here, navigate to the Dash Deployment Server UI, select the app
    (`MANAGER/apps/<user>:<app-name>/overview`) to display the applications
    analytics.
    ''')),

    html.Img(
        alt='App Analytics',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/analytics.png',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),
])

Logs = html.Div(children=[
    dcc.Markdown(s('''
    #### Dash App Logs

    To view the logs, navigate to logs (`MANAGER/apps/<user>:<app-name>/logs`).
    ''')),

    html.Img(
        alt='App Logs',
        src='https://github.com/plotly/dash-docs/raw/master/images/dds/logs.png',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    #### Dash App Logs (via Command Line)

    Alternatively, the above can be accomplished via the command line.
    To view the logs for a specific Dash app run the following command
    in your terminal:

    ```
    ssh dokku@<your-dash-domain> logs <your-app-name> --num -1
    ```

    This will work for any app you have permission on, and uses the
    same mechanism as pushing the app via ssh.

    **Options**
    - `--num`, `-n`: The number of lines to display. By default, 100 lines are displayed.
       Set to -1 to display _all_ of the logs. Note that we only store logs from the latest app deploy.
    - `--tail`, `-t`: Continuously stream the logs.
    - `--quiet`, `-q`: Display the raw logs without colors, times, and names.
    ''')),
])

Support = html.Div(children=[
    dcc.Markdown(s('''
    #### Support

    If you encounter any issues deploying your app you can email
    `onpremise.support@plot.ly`. It is helpful to include any error
    messages you encounter as well as available logs. See below on how
    to obtain Dash app logs as well as the Plotly Enterprise support
    bundle.
    ''')),

    dcc.Markdown(s('''
    #### Enterprise Support Bundle

    If you're requested to send the full support bundle you can
    download this from your Plotly Enterprise Server Manager
    (e.g. `https://<your.plotly.domain>:8800`). Please note you
    will need admin permissions to access the Server Manager.
    Navigate to the Server Manager and then select the Support tab.
    There you will see the option to download the support bundle.
    '''))
])
