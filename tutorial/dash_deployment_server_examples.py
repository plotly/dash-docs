# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import styles
from server import app

def s(string_block):
    return string_block.replace('    ', '')

# # # # # # #
# Authenticating to Dash Deployment Server with SSH
# # # # # # #
Ssh = html.Div(children=[
    html.H1('Authenticating to Dash Deployment Server with SSH'),

    dcc.Markdown(s('''

    In Plotly Enterprise 2.4.0 and above, you can deploy your apps using
    either HTTPS or SSH. If you are deploying with HTTPS, then you do not
    need to set up an SSH key. Thus, you can skip this tutorial and go
    straight to
    [Initialize Dash Apps on Dash Deployment Server](/dash-deployment-server/initialize).

    &nbsp;

    If you are deploying with SSH then you need to add a SSH Key to the
    Dash Deployment Server. SSH Keys are used to authenticate your git
    session with the server. Deploying with SSH takes a little bit more
    time to set up but it allows you to deploy without typing in your
    username and password each time. Continue below for instructions on
    how to generate and add a SSH Key.

    ***

    ''')),

    dcc.Markdown(s('''
    #### Why Deploy with SSH?

    We recommend deploying with HTTPS for most of our users.
    However, if your Dash Deployment Server is using a **self-signed
    certificate**, deploying with HTTPS
    [requires some extra, challenging configuration](https://stackoverflow.com/questions/11621768/).
    In these cases, it will be easier to set up deploying with SSH.

    ***

    #### Already Have an SSH Key?

    If you already have an SSH key that you've used in other
    services, you can use that key instead of generating a new one.
    For instructions on how to add an existing SSH Key to the Dash Deployment
    Server, jump to **Copy and Add SSH Key**.

    ***

    ## Generate and Add an SSH Key

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

        dcc.Markdown(s(
        '**1. Open Git Bash**' if platform == 'Windows' else
        '**1. Open Terminal**'
        )),

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
        &nbsp;

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
        &nbsp;

        **2. Open the Dash Deployment Server UI**

        You can find the Dash Deployment Server UI by selecting "Dash App"
        from Plotly's "Create" menu.

        > *The Dash App item in the Create menu takes you to the Dash
        Deployment Server UI*
        ''')),

        html.Img(
            alt='Dash App Create Menu',
            src='/assets/images/dds/open-dds-ui.png',
            style={
                'width': '100%', 'border': 'thin lightgrey solid',
                'border-radius': '4px'
            }
        ),

        dcc.Markdown(s('''
        &nbsp;

        **3. Add SSH Key**

        Select **SSH Keys** in the top navigation menu of the Dash
        Deployment Server UI. Here, select **Add Key** and in the 'Add
        SSH Key' modal, paste in your SSH Key.
        ''')),

        html.Img(
            alt='Add SSH Key',
            src='/assets/images/dds/add-ssh-key.png',
            style={
                'width': '100%', 'border': 'thin lightgrey solid',
                'border-radius': '4px'
            }
        ),

        dcc.Markdown(s('''
        &nbsp;

        **4. Confirm it Has Been Added**

        Once you've added an SSH key, it should be added to your list of SSH
        Keys like the image below.
        ''')),

        html.Img(
            alt='List of SSH Keys',
            src='/assets/images/dds/list-of-ssh-keys.png',
            style={
                'width': '100%', 'border': 'thin lightgrey solid',
                'border-radius': '4px'
            }
        ),

        dcc.Markdown(s('''
        ***

        #### Modify SSH Config

        Next, specify a custom port in your SSH config. By default, this
        should be `3022` but your server administrator may have set it to
        something different.

        This file is located in `~/.ssh/config`. If it's not there, then
        create it. Add the following lines to
        this file, replacing `your-dash-deployment-server` with the domain of
        your Dash Deployment Server (without `http://` or `https://`).
        ''')),

        dcc.SyntaxHighlighter('''Host your-dash-deployment-server
        Port 3022''', customStyle=styles.code_container),

        (dcc.Markdown(s('''
        If you're having trouble opening this file, you can run
        `$ open ~/.ssh/config` which will open the file using your default
        editor. If the file doesn't exist, then you can open that hidden
        folder with just `$ open ~/.ssh`
        ''')) if platform == 'Mac' else ''),

        (dcc.Markdown(s('''
        Please be careful not to save your SSH config as a .txt file as
        it will not be recognized by Git when deploying your applications.
        If you are using Notepad to create your SSH config, you can force the
        removal of the .txt extension by naming the file "config", including
        the quotes, in the Save As dialog box.
        ''')) if platform == 'Windows' else ''),


        dcc.Markdown(s('''
        ***

        If you have successfully added your SSH Key, advance to
        [**Part 1. Initialize Dash Apps on Dash Deployment Server**](/dash-deployment-server/initialize).
        '''))
    ]

# # # # # # #
# Initialize
# # # # # # #
Initialize = html.Div(children=[
    html.H1('Part 1. Initialize Dash Apps on Dash Deployment Server'),

    dcc.Markdown(s('''
        > This is the *1st* deployment chapter of the [Dash Deployment Server Documentation](/dash-deployment-server).
        > The [next chapter](/dash-deployment-server/deployment) covers deploying a Dash App on Dash Deployment Server.

        Before creating or deploying a dash app locally, you need to initialize
        an app on Dash Deployment Server. This can be achieved using the Dash
        Deployment Server UI.
    ''')),

    dcc.Markdown(s('''
        ***

        1. Navigate to the Dash Deployment Server UI by selecting **Dash App**
        from the **+ Create** located in the top right-hand corner.
    ''')),

    html.Img(
        alt='Dash Deployment Server UI',
        src='/assets/images/dds/open-dds-ui.png',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''

        &nbsp;

        2. In the top right-hand corner select **Create App**. The
        'Create Dash App' modal should appear. Here, name your dash app
        (app names must start with a lower case letter and may
        contain only lower case letters, numbers, and -) and then
        hit **Create**. It is important to keep in mind that this name is going
        to be part of the URL for your application.

    ''')),

    html.Img(
        alt='Initialize App',
        src='/assets/images/dds/add-app.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''

        &nbsp;

        3. After you have created the app, it should appear in your list of
        apps.

    ''')),

    html.Img(
        alt='List of Apps',
        src='/assets/images/dds/list-of-apps.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''

        &nbsp;

        4. Now, select the dash app to access the app overview.

    ''')),

    html.Img(
        alt='Dash App Overview',
        src='/assets/images/dds/app-overview.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''

        &nbsp;

        If you have successfully initialized an app, advance to
        [**Part 2. Deploy Dash Apps on Dash Deployment Server**](/dash-deployment-server/deployment).
        If you have encountered any issues see [**Troubleshooting**](/dash-deployment-server)
        for help.

    ''')),

])

# # # # # # #
# Requirements
# # # # # # #
Requirements = html.Div(children=[
    html.H1('Application Structure'),

    dcc.Markdown(s(
    '''
    To deploy dash apps to the Dash Deployment Server, there
    are a few files required for successful deployment. Below is a common
    dash app folder structure and a brief description of each files function.

    ***

    ## Folder Reference

    ```
    Dash_App/
    |-- assets/
       |-- app.css
    |-- app.py
    |-- .gitignore
    |-- Procfile
    |-- requirements.txt
    |-- runtime.txt
    ```

    ***

    ## Files Reference

    `app.py`

    This is the entry point to your application, it contains your Dash app code.
    This file must contain a line that defines the `server` variable:
    ```server = app.server```

    ***

    `.gitignore`

    Determines which files and folders are ignored in git, and therefore
    ignored (i.e. not copied to the server) when you deploy your application.
    An example of its contents would be:

    ```
    venv
    *.pyc
    .DS_Store
    .env
    ```

    ***

    `Procfile`

    Declares what commands are run by app's containers. This is commonly,
    ```web: gunicorn app:server --workers 4``` where app refers to the file
    `app.py` and server refers to the variable named server inside that file.
    gunicorn is the web server that will run your application, make sure to
    add this in your requirements.txt file.

    ***

    `requirements.txt`

    Describes the app's python dependencies. For example,

    ```
    dash==0.21.1
    dash-auth==1.0.1
    dash-renderer==0.11.3
    dash-core-components==0.22.1
    dash-html-components==0.9.0
    ```

    ***

    `runtime.txt`

    This file specifies python runtime. For example, its contents would be
    `python-2.7.15` or `python-3.6.6`.

    ***

    `assets`

    An optional folder that contains CSS stylesheets, images, or
    custom JavaScript files. [Learn more about assets](/external-resources).

    '''))
])


# # # # # # #
# Deploy App
# # # # # # #
Deploy = html.Div(children=[
    html.H1('Part 2. Deploy Dash Apps on Dash Deployment Server'),

    dcc.Markdown(s(
    '''
    > This is the *2nd* deployment chapter of the [Dash Deployment Server Documentation](/dash-deployment-server).
    > The [previous chapter](/dash-deployment-server/initialize) covered initializing a Dash App on Dash Deployment Server.


    To deploy an app to your Dash Deployment Server, you can either choose
    to deploy a cloned sample app, create a new app following the tutorial,
    or an existing app that you created locally and are ready to deploy.

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
        for deployment. Alternatively, you can select **Create New App** to
        run through creating and deploying an app from the beginning.
        Otherwise, if you already have an exisiting app locally that you would
        like to deploy, then select **Deploy Existing App**.

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

                    (dcc.Markdown(s('''
                    &nbsp;

                    First, install [Git for Windows](https://git-scm.com/download/win).
                    Then, in Git Bash:
                    ''')) if platform == 'Windows' else
                    ''),

                    dcc.SyntaxHighlighter(s(
                    '''$ git clone https://github.com/plotly/dash-on-premise-sample-app.git'''),
                    customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    ***

                    #### Modify `config.py`

                    Read through `config.py` and modify the values as necessary.
                    If Dash Deployment Server was set up with "path-based routing"
                    (the default), then you will just need to change the
                    `DASH_APP_NAME` to be equal to the name of the Dash App that you
                    set earlier.
                    ''')),

                    dcc.Markdown(s(
                    '''
                    ***

                    #### Configure your Dash Deployment Server to be your Git remote

                    In the root of your folder, run the following command to create a
                    remote host to your new app on Dash Deployment Server.

                    &nbsp;

                    ##### Which Deployment Method Are You Using?

                    ''')),
                ])
            ]),
            dcc.Tab(label='Create New App', children=[
                html.Div([
                    (dcc.Markdown(s('''
                    &nbsp;

                    First, install [Git for Windows](https://git-scm.com/download/win).
                    Then, in Git Bash:
                    ''')) if platform == 'Windows' else
                    ''),

                    dcc.Markdown(s(
                    '''

                    &nbsp;

                    #### Create a New Folder
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''$ mkdir dash_app_example
$ cd dash_app_example''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''

                    ***

                    #### Initialize the Folder with `git` and a `virtualenv`

                    ''')),

                    dcc.SyntaxHighlighter(
                    ('''$ git init # initializes an empty git repo
$ virtualenv venv # creates a virtualenv called "venv"
$ source venv/bin/activate # uses the virtualenv''') if platform != 'Windows' else (
                    '''$ git init # initializes an empty git repo
$ virtualenv venv # creates a virtualenv called "venv"
$ source venv/Scripts/activate # uses the virtualenv'''), customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    &nbsp;

                    `virtualenv` creates a fresh Python instance. You will need
                    to reinstall your app's dependencies with this virtualenv:
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''$ pip install dash
$ pip install dash-renderer
$ pip install dash-core-components
$ pip install dash-html-components
$ pip install plotly''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    &nbsp;

                    You will also need a new dependency, `gunicorn`, for
                    deploying the app:
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''$ pip install gunicorn''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    ***
                    #### Create Relevant Files For Deployment

                    Create the following files in your project folder:

                    **`app.py`**

                    `app.py` This is the entry point to your application,
                    it contains your Dash app code. This file must contain a
                    line that defines the server variable: `server = app.server`
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
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

@app.callback(Output('display-value', 'children'),
            [Input('dropdown', 'value')])
def display_value(value):
  return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
  app.run_server(debug=True)''',
                    customStyle=styles.code_container, language='python'),

                    dcc.Markdown(s('''
                    ***

                    **`.gitignore`**

                    `.gitignore` Determines which files and folders are
                    ignored in git, and therefore ignored (i.e. not copied
                    to the server) when you deploy your application.
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''venv
*.pyc
.DS_Store
.env''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    ***

                    **`Procfile`**

                    Declares what commands are run by app's containers. This is
                    commonly, `web: gunicorn app:server --workers 4` where app
                    refers to the file `app.py` and server refers to the variable
                    named server inside that file. gunicorn is the web server
                    that will run your application, make sure to add this in
                    your requirements.txt file.

                    ''')),

                    dcc.SyntaxHighlighter(
                    '''web: gunicorn app:server --workers 4''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    ***

                    **`requirements.txt`**

                    `requirements.txt` Describes the app's python dependencies.
                    You can fill this file in automatically with:
                    ''')),

                    dcc.SyntaxHighlighter(
                    '''$ pip freeze > requirements.txt''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    ***

                    **`runtime.txt`**

                    `runtime.txt` This file specifies python runtime.
                    For example, its contents would be `python-2.7.15` or
                    `python-3.6.6`
                    ''')),

                    dcc.Markdown(s(
                    '''
                    ***

                    #### Configure your Dash Deployment Server to be your Git remote

                    In the root of your folder, run the following command to create a
                    remote host to your new app on Dash Deployment Server.

                    &nbsp;

                    ##### Which Deployment Method Are You Using?

                    ''')),
                ])
            ]),
            dcc.Tab(label='Deploy Existing App', children=[
                html.Div([
                    (dcc.Markdown(s('''
                    &nbsp;

                    First, install [Git for Windows](https://git-scm.com/download/win).
                    Then, in Git Bash:
                    ''')) if platform == 'Windows' else
                    ''),

                    dcc.Markdown(s(
                    '''

                    &nbsp;

                    #### Initialize the Folder With Git


                    ''')),

                    dcc.SyntaxHighlighter(
                    '''$ cd <your-folder-name>
$ git init # initializes an empty git repo''', customStyle=styles.code_container),

                    dcc.Markdown(s(
                    '''
                    ***

                    #### Configure your Dash Deployment Server to be your Git remote

                    In the root of your folder, run the following command to create a
                    remote host to your new app on Dash Deployment Server.

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
        dcc.Markdown(s('''
        &nbsp;

        Plotly recommends using HTTPS, but if you would like to use SSH then you
        need to [Configure SSH Authentication](/dash-deployment-server/ssh).

        ''') if method == 'SSH' else ('')),

        dcc.SyntaxHighlighter(s(
        '''$ git remote add plotly dokku@your-dash-deployment-server:your-dash-app-name''' if method == 'SSH' else
        '''$ git remote add plotly https://your-dash-deployment-server/GIT/your-dash-app-name'''),
        customStyle=styles.code_container,
        language='python'
        ),

        dcc.Markdown(s(
        '''
        &nbsp;

        Replace `your-dash-app-name` with the name of your Dash App that you
        supplied in the Dash Deployment Server and `your-dash-deployment-server`
        with the domain of the Dash Deployment Server.

        For example, if your Dash App name was `my-first-dash-app`
        and the domain of your organizations Dash Deployment Server was
        `dash.plotly.acme-corporation.com`, then this command would be
        `git remote add plotly dokku@dash.plotly.acme-corporation.com:my-first-dash-app`.
            ''' if method == 'SSH' else '''
        &nbsp;

        Replace `your-dash-app-name` with the name of your Dash App that
        you supplied in the Dash Deployment Server and `your-dash-deployment-server`
        with the domain of the Dash Deployment Server.

        For example, if your Dash App name was `my-first-dash-app`
        and the domain of your organizations Dash Deployment Server was
        `dash.plotly.acme-corporation.com`, then this command would be
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
        '''$ git status # view the changed files
$ git diff # view the actual changed lines of code
$ git add .  # add all the changes
$ git commit -m 'a description of the changes'
$ git push plotly master'''), customStyle=styles.code_container, language='python'),

        dcc.Markdown(s(
        '''

        &nbsp;

        This commands will push the code in this folder to the
        Dash Deployment Server and while doing so, will install the
        necessary python packages and run your application
        automatically.

        Whenever you make changes to your Dash code,
        you will need to run those `git` commands above.

        If you install any other Python packages, add those packages to
        the `requirements.txt` file. Packages that are included in this
        file will be installed automatically by the Dash Deployment Server.
        ''')),

        dcc.Markdown(s(
        '''

        ***

        #### Deploy Failed?

        If your depoly has been unsuccesful, you can check that you have the
        [necessary files required for deployment](/dash-deployment-server/application-structure),
        or if you have a specific error, take a look at
        [Common Errors](/dash-deployment-server/troubleshooting).

        '''))
    ]

# # # # # # #
# Dash App Authentication
# # # # # # #
Authentication = html.Div(children=[
    html.H1('Dash App Authentication'),
    dcc.Markdown(s('''
    The `dash-auth` package provides login through your Plotly
    Enterprise accounts. For example, the discussion below describes how
    `dash-auth` works in the
    [On-Premise Sample App](https://github.com/plotly/dash-on-premise-sample-app/).

    ***

    #### Modify the `config.py` File

    This file contains several settings that are used in your app.
    It's kept in a separate file so that it's easy for you to
    transfer from app to app.
    *Read through this file and modify the variables as appropriate.*

    ''')),

    dcc.Markdown(s('''
    ***

    #### Redeploy Your App

    Your app should now have a Dash Deployment Server login screen.
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
    Dash Deployment Server supports these actions through an
    `apt-packages` file and a `predeploy` script.

    &nbsp;

    We have a collection of sample apps taht install common system
    level dependencies. These applications are _ready to deploy_:

    - [Oracle cx_Oracle Database](https://github.com/plotly/dash-on-premise-sample-app/pull/2#issue-144246327)
    - [Pyodbc Database Driver](https://github.com/plotly/dash-on-premise-sample-app/pull/3#issue-144272510)

    &nbsp;

    If you need help configuring complex system level dependencies, please
    reach out to our [support](/dash-deployment-server/support) team.

    ***

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

    ***

    #### Configure System Dependencies

    You may include a pre-deploy script that executes in
    your Dash App's environment. For the case of adding an
    ODBC driver we need to add ODBC initialization files into
    the correct systems paths. To do so we include the ODBC
    initialization files in the application folder and then
    copy them into system paths in the pre-deploy script.

    &nbsp;

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
    &nbsp;

    ##### Run Pre-Deploy Script Using `app.json`

    Next we must instruct Dash Deployment Server to run our `setup_pyodbc`
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
    Redis is a powerful in memory database that is well suited for many Dash
    applications. In particular, you can use Redis to:

    - Save application data
    - Enable queued and background processes with Celery.
    [Redis and Celery Demo App](https://github.com/plotly/dash-redis-demo)
    - Cache data from your callbacks across processes.
    [Caching in Dash with Redis](/performance)

    &nbsp;

    While Redis is an _in memory database_, Dash Deployment Server regularly
    backs up its data to the underlying server. So, it's safe for production
    usage. Dash Deployment Server can dynamically spin up and manage secure
    instances of Redis for your application.
    ''')),

    dcc.Markdown(s('''
    ***

    #### Enable Redis Databases

    In Plotly Enterprise 2.5.0, Redis Databases are always enabled.

    For previous versions, navigate to Plotly On-Premise Server Settings
    (`https://<your.plotly.domain>:8800/settings`), then under **Special Options
    & Customizations** select **Enable Dash Customizations** and **Enable Redis
    Databases** for Dash Apps.
    ''')),

    html.Img(
        alt='Enable Redis Databases',
        src='/assets/images/dds/enable-redis.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    ***

    #### Create and Link (via UI)

    You can create one redis instance that is used by multiple apps or you
    can create a unique Redis Database for each individual app.
    To start, we recommending creating a unique Redis Database for each
    Dash App. It will be easier for you to ensure that one application doesn't
    override the data from a separate application.

    &nbsp;

    In Plotly Enterprise 2.5.0 it is possible to create and link a Redis
    Database to your Dash App using the Dash Deployment Server UI.
    Here, you have two options:

    &nbsp;

    **1.** Create a database before initializing an app.

    **2.** Create and link a database after an app has been initialized.

    &nbsp;

    ##### Create a Database Before Initializing an App

    If you haven't initialized an app yet, select **Databases** situated in the
    top navigation menu. Next, select **Create Database**, then in the
    'Create Database' modal, add the name of your database. We recommend using
    a convention like using the name of your application and adding `-redis`
    to the end, e.g. `my-dash-app-redis`.

    Once your Redis Database has been created, you'll notice that it is
    added to your list of databases.
    ''')),

    html.Img(
        alt='Create Database',
        src='/assets/images/dds/create-redis-db.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    &nbsp;

    Next, navigate to **Apps** and create a new app (for more info see
    ['Part 1. Initialize Dash Apps on Dash Deployment Server'](/dash-deployment-server/initialize)),
    in the 'Create App' modal you have the option of linking a database.
    Here, use the dropdown to select the database that you created previously
    (see image below).
    ''')),

    html.Img(
        alt='Link Database',
        src='/assets/images/dds/link-redis-db.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    &nbsp;

    ##### Create and Link a Database After an App Has Been Initialized.

    In the Dash Deployment Server UI, select the app then navigate
    to the settings page. In Databases, use the dropdown to select
    **create and link database** then **Add**.

    ''')),

    html.Img(
        alt='Create and Link Database in App',
        src='/assets/images/dds/create-and-link-redis-db.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    ***

    #### Create and Link (via Command Line)

    While it is now possible to create and link Redis Databases via the
    Dash Deployment Server UI, it is still possible to create and link a Redis
    database via the command line (using ssh):

    ''')),

    dcc.SyntaxHighlighter(s(
    """$ ssh dokku@YOUR_DASH_SERVER redis:create SERVICE-NAME
    $ ssh dokku@YOUR_DASH_SERVER redis:link SERVICE-NAME APP-NAME"""),
    customStyle=styles.code_container,
    language='python'
    ),

    dcc.Markdown(s('''

    &nbsp;

    In the commands above, replace:
    * `YOUR_DASH_SERVER` with the name of your Dash server
    (same as when you run `git remote add`)
    * `SERVICE-NAME` with the name you want for your Redis service
    * `APP-NAME` with the name of your app (as specified in the
    Dash App Manager).

    ''')),

    dcc.Markdown(s('''
    ***

    #### Referencing Redis in Your Code

    You can reference your Redis Database with the `os.environ` module:

    ''')),

    dcc.SyntaxHighlighter(s(
    """redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])"""),
    customStyle=styles.code_container,
    language='python'
    ),

    dcc.Markdown(s('''
    ***

    #### Running Redis on Your Local Machine

    To get started, see the [Redis documentation](https://redis.io/documentation)
    to download Redis and set up a local instance.

    &nbsp;

    By referencing Redis in our code, we'll need to add the variable to our
    local environment as well. One easy way to do this is to define the
    variable on-the-fly when you run `python app.py`.
    ''')),

    dcc.SyntaxHighlighter(s("$ REDIS_URL=redis://<your-redis-instance-ip>:6379 python app.py"),
    customStyle=styles.code_container,
    language='python'),

    dcc.Markdown(s('''
    &nbsp;

    ##### Windows Users

    Installing Redis from source on windows can be tricky. If you have the
    "Windows Subsystem for Linux", we recommend using that and installing
    the Redis in that linux environment. Otherwise, we recommend installing
    these [64-bit binary releases of Redis](https://github.com/ServiceStack/redis-windows#option-3-running-microsofts-native-port-of-redis).

    '''))
])


# # # # # # #
# Linking a Celery Process
# # # # # # #
Celery = html.Div(children=[
    html.H1('Linking a Celery Process'),

    dcc.Markdown(s(
    '''
    Celery is a reliable asynchronous task queue/job queue that supports both
    real-time processing and task scheduling in production systems. This makes
    Celery well suited for Dash Applications. For example:

    - Enable queued and background processes with Celery.
    [Redis and Celery Demo App](https://github.com/dash-redis-demo)
    - Periodically update an App's data.
    [Redis and Celery Periodic Updates Demo App](https://github.com/plotly/dash-redis-celery-periodic-updates)

    &nbsp;

    For more information about Celery, visit
    [Celery's documentation](http://docs.celeryproject.org/en/latest/).

    ''')),

])

# # # # # # #
# Env Vars
# # # # # # #
EnvVars = html.Div(children=[
    html.H1('Setting Environment Variables'),

    dcc.Markdown(s('''
    In Plotly Enterprise 2.5.0, you can store secrets as environment variables
    instead of in your application. It's good practice to keep application
    secrets like database passwords outside of your code so that they aren't
    mistakenly exposed or shared. Instead of storing these secrets in code,
    you can store them as environment variables and your Dash Application code
    can reference them dynamically.

    ''')),

    dcc.Markdown(s('''

    ***

    #### Add Environment Variables

    To add environment variables via the Dash Deployment Server UI,
    navigate to the application settings. Here, use the text boxes to
    add the environmental variable name and value. For example, `"DATABASE_USER"`
    and `"DATABASE_PASSWORD"`.

    ''')),

    html.Img(
        alt='Add Environment Variables',
        src='/assets/images/dds/add-env-variable.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''

    ***

    #### Referencing Environment Variables in Your Code

    You can reference these variables with the `os.environ` module:

    ''')),

    dcc.SyntaxHighlighter(s(
    """database_password = os.environ['DATABASE_PASSWORD']"""),
    customStyle=styles.code_container,
    language='python'
    ),

    dcc.Markdown(s('''
    &nbsp;

    Alternatively, if the variable isn't in your environment and you want
    to fallback to some other value, use:

    ''')),

    dcc.SyntaxHighlighter(s(
    """database_password = os.environ.get('DATABASE_PASSWORD', 'my-default-database-password')"""),
    customStyle=styles.code_container,
    language='python'
    ),



    dcc.Markdown(s('''
    ***

    #### Defining Environment Variables In Your Local Environment

    By referencing these environment variables in our code, we'll need to add
    these variables to our local environment as well. One easy way to do
    this is to define the variables on-the-fly when you run `python app.py`.
    That is, instead of running `python app.py`, run:

    ```
    $ DATABASE_USER=chris DATABASE_PASSWORD=my-password python app.py
    ```

    &nbsp;

    Alternatively, you can define them for your session by "exporting" them:
    ''')),

    dcc.SyntaxHighlighter(s("""$ export DATABASE_USER=chris
    $ export DATABASE_PASSWORD=my-password
    $ python app.py"""),
    customStyle=styles.code_container,
    language='python'
    ),


    dcc.Markdown(s('''
    ***

    #### Delete Environment Variables

    To remove an environment variable via the Dash Deployment Server UI,
    navigate to the application settings. Here, simply click the red
    cross situated to the right-hand side of the environment variable.

    ''')),

    html.Img(
        alt='Delete Environment Variables',
        src='/assets/images/dds/remove-env-variable.PNG',
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

    dcc.Markdown(s('''
    In Dash Deployment Server, Dash Apps are run in isolated containers.
    Dash Deployment Server builds the entire system for each individual app
    from scratch, including installing a fresh instance of Python, installing
    dependencies, and more. This isolation and containerization is great: it
    allows for one app's dependencies to not impact the next app's and,
    from a security perspective, ensures that applications can't modify or
    access the underlying server. One part of this isolation is that each app
    has it's own "ephemeral" filesystem. This means that:

    - By default, files that are saved in the app's environment aren't
    persisted across deploys.
    - By default, files (even networked file systems) that are on the actual
    physical server aren't actually accessible to the application.

    &nbsp;

    Starting in Plotly Enterprise 2.5.0, you can map filesystems from the
    underlying server into the application. This allows you to save files
    persistently as well as read files from the underlying server, including
    networked file systems.

    Since this feature has security implications, only users with
    admin/superuser privileges are allowed to map directories onto apps.
    Before you get started, ask your current administrator to grant you
    admin/superuser privileges as shown below.

    ***

    #### Add Admin/Superuser Privileges

    As administrator, navigate to the admin panel
    `https://<your.plotly.domain>/admin/` and select **Users**. From the list
    of users, select the user you wish to edit. Next, check both the
    **Staff status** and **Superuser status** box to give the user
    admin/superuser privileges, which will allow the user to map
    directories onto apps.

    ''')),

    html.Img(
        alt='Add Admin/Superuser Status',
        src='/assets/images/dds/add-superuser.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''

    ***

    #### Add Directory Mapping

    To add a directory mapping via the Dash Deployment Server UI,
    navigate to the application **Settings** and scroll down to
    **Directory Mappings**. Here, use the text boxes to
    add the **Host Path** and **App Path**. For example, `/srv/app-data`
    and `/data`.

    ''')),

    html.Img(
        alt='Add Directory Mapping',
        src='/assets/images/dds/add-dir-map.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''

    ***

    #### Referencing the File System in Your Code

    If you have mapped the directory from `/srv` to `/srv/app-data`, then you
    can read files from this folder in you application with the following code:

    ''')),

    dcc.SyntaxHighlighter(s("""import os
    file_pathname = os.path.join('data', 'some-file.csv')"""),
    customStyle=styles.code_container,
    language='python'
    ),

    dcc.Markdown(s('''
    &nbsp;

    In some cases, the filesystems that you reference in your deployed
    application may be different from those that you reference locally.
    In your application code, you can check which environment you are in
    with the following code:

    ''')),

    dcc.SyntaxHighlighter(
"""if 'DASH_APP' in os.environ:
    # this is a deployed app
    filepath = os.path.join('data', 'my-dataset.csv')
else:
    # local file path
    filepath = os.path.join('Users', 'chris', 'data', 'my-dataset.csv')""",
    customStyle=styles.code_container,
    language='python'
    ),

    dcc.Markdown(s('''
    ***

    #### Recommendations

    If you are mounting a filesystem, we have the following recommendations:

    - Try to isolate the data that you need into it's own, app-specific folder
    - Do not mount the entire filesystem
    - Do not mount system directories, like those under `/usr`.
    - As per the
    ["Filesystem Hierarchy Standard (FHS)"](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard),
    folders inside the `/srv` folder would be a good, conventional place
    to host app level data.
    - This feature also works with networked filesystems. Note that this
    requires some extra configuration in the underlying server by your
    server administrator. In particular, the network filesystem should be
    added to the `/etc/fstab` file on the underlying server. For more
    information, see this
    [RHEL7 and CentOS documentation on CIFS and NFS](https://www.certdepot.net/rhel7-mount-unmount-cifs-nfs-network-file-systems/)
    , the official [Ubuntu NFS documentation](https://help.ubuntu.com/lts/serverguide/network-file-system.html.en),
    the official [Ubuntu CIFS documentation](https://wiki.ubuntu.com/MountWindowsSharesPermanently)
    or [contact our support team](/dash-deployment-server/support).

    ***

    #### Remove Directory Mapping

    To remove directory mappings via the Dash Deployment Server UI,
    navigate to the application **Settings** and scroll down to
    **Directory Mappings**. Next, use the red cross situated to the
    right-hand side of the environment variable.

    ''')),

    html.Img(
        alt='Remove Directory Mapping',
        src='/assets/images/dds/remove-dir-map.PNG',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),
])

# # # # # # #
# Staging App
# # # # # # #
StagingApp = html.Div(children=[
    html.H1('Create a Staging Dash App'),

    dcc.Markdown(s(
    '''
    Once you have deployed your application, your end-users will expect that
    it is stable and ready for consumption. So, what do you do if you want to
    test out or share some changes on the server? We recommend creating
    separate applications: one for "production" consumption and another one
    for testing. You will share the URL of the "production" app to your end
    users and you will use your "testing" app to try out different changes
    before you send them to your production app. With Dash Deployment
    Server, creating a separate testing app is easy:

    ***

    ### Initialize a New Dash App

    [Initialize a new app](/dash-deployment-server/initialize) in the Dash
    Deployment Server UI. We recommend giving it the same name as your
    other app but appending `-stage` to it (e.g. `analytics-stage`).

    ***

    ### Configure a New Git Remote

    Add a new remote that points to this URL. In this example,
    we'll name the remote "stage":

    ''')),

    dcc.SyntaxHighlighter(s(
    '''$ git add remote stage https://your-dash-deployment-server/GIT/your-dash-app-name-stage'''),
    customStyle=styles.code_container, language='python'),

    dcc.Markdown(s(
    '''
    ***

    ### Deploy Changes to Your Staging App

    Now, you can deploy your changes to this app just like you would
    with your other app. Instead of `$ git push plotly master`, you'll deploy
    to your staging app with:

    ''')),

    dcc.SyntaxHighlighter(s(
    '''$ git push stage master'''),
    customStyle=styles.code_container, language='python'),

])

# # # # # # #
# Common Errors
# # # # # # #
Troubleshooting = html.Div(children=[
    html.H1('Common Errors'),
    dcc.Markdown(s(
    '''
    This section describes some of the common errors you may encounter when
    trying to deploy to the Dash Deployment Server, and provides information
    about how to resolve these errors. If you can't find the information
    you're looking for, or need help, [contact our support team](/dash-deployment-server/support).

    ***

    ''')),

    dcc.Markdown(s(
    '''
    #### Deploying with Self-Signed Certificates?

    ''')),

    dcc.SyntaxHighlighter(s(
    '''fatal: unable to access 'https://<your-dash-deployment-server>/GIT/your-dash-app-name/': SSL certificate problem: self signed certificate'''),
    customStyle=styles.code_container, language='python'),

    dcc.Markdown(s(
    '''
    &nbsp;

    We recommend deploying with HTTPS for most of our users.
    However, if your Dash Deployment Server is using a **self-signed
    certificate**, deploying with HTTPS
    [requires some extra, challenging configuration](https://stackoverflow.com/questions/11621768/).
    In these cases, it will be easier to set up deploying with SSH.

    ***

    #### Deployment Failing?

    ''')),

    html.Details([
        html.Summary("Could not find a version that satisfies the requirement"),

        dcc.SyntaxHighlighter(
        '''...
    remote: -----> Cleaning up...
    remote: -----> Building my-dash-app from herokuish...
    remote: -----> Injecting apt repositories and packages ...
    remote: -----> Adding BUILD_ENV to build environment...
    remote:        -----> Python app detected
    remote:        !     The latest version of Python 2 is python-2.7.15 (you are using python-2.7.13, which is unsupported).
    remote:        !     We recommend upgrading by specifying the latest version (python-2.7.15).
    remote:        Learn More: https://devcenter.heroku.com/articles/python-runtimes
    remote: -----> Installing python-2.7.13
    remote: -----> Installing pip
    remote: -----> Installing requirements with pip
    remote:        Collecting dash==0.29.1 (from -r /tmp/build/requirements.txt (line 1))
    remote:        Could not find a version that satisfies the requirement dash==0.29.1 (from -r /tmp/build/requirements.txt (line 1)) (from versions: 0.17.4, 0.17.5, 0.17.7, 0.17.8rc1, 0.17.8rc2, 0.17.8rc3, 0.18.0, 0.18.1, 0.18.2, 0.18.3rc1, 0.18.3, 0.19.0, 0.20.0, 0.21.0, 0.21.1, 0.22.0rc1, 0.22.0rc2, 0.22.0, 0.23.1, 0.24.0, 0.24.1rc1, 0.24.1, 0.24.2, 0.25.0)
    remote:        No matching distribution found for dash==0.29.1 (from -r /tmp/build/requirements.txt (line 1))''',
        customStyle=styles.code_container, language='python'),

        dcc.Markdown(s(
        '''
        &nbsp;

        If you're seeing the error above, it is likely that there is an error in
        your `requirements.txt` file. To resolve, check the versioning in your
        `requirements.txt` file. For example, the above failed because
        `dash==29.1` isn't a version of dash. If you're working in a virtualenv then
        you can check your versioning with the command:
        ''')),

        dcc.SyntaxHighlighter('$ pip list', customStyle=styles.code_container, language='python'),

        dcc.Markdown(s(
        '''
        &nbsp;

        if it is differs to your `requirements.txt`, you can update it with the command:
        ''')),

        dcc.SyntaxHighlighter('$ pip freeze > requirements.txt', customStyle=styles.code_container, language='python'),

        dcc.Markdown(s(
        '''
        &nbsp;

        For more information see [Application Structure](/dash-deployment-server/application-structure).

        &nbsp;
        '''))
    ]),

    html.Details([
        html.Summary("Failed to find application object 'server' in 'app"),

        dcc.SyntaxHighlighter(
        '''...
    remote:        Failed to find application object 'server' in 'app'
    remote:        [2018-08-16 16:00:49 +0000] [181] [INFO] Worker exiting (pid: 181)
    remote:        [2018-08-16 16:00:49 +0000] [12] [INFO] Shutting down: Master
    remote:        [2018-08-16 16:00:49 +0000] [12] [INFO] Reason: App failed to load.
    remote:        [2018-08-16 16:00:51 +0000] [12] [INFO] Starting gunicorn 19.9.0
    remote:        [2018-08-16 16:00:51 +0000] [12] [INFO] Listening at: http://0.0.0.0:5000 (12)
    remote:        [2018-08-16 16:00:51 +0000] [12] [INFO] Using worker: sync
    remote:        [2018-08-16 16:00:51 +0000] [179] [INFO] Booting worker with pid: 179
    remote:        [2018-08-16 16:00:51 +0000] [180] [INFO] Booting worker with pid: 180''',
        customStyle=styles.code_container, language='python'),

        dcc.Markdown(s(
        '''
        &nbsp;

        Deployment fails with the above message when you have failed to declare
        `server` in your `app.py` file. Check your `app.py` file and confirm that
        you have `server = app.server`.

        &nbsp;

        For more information see
        [Application Structure](/dash-deployment-server/application-structure).

        &nbsp;
        '''))
    ]),

    html.Details([
        html.Summary("Got permission denied while trying to connect to the Docker daemon socket"),

        dcc.SyntaxHighlighter(s(
        '''$ Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.38/containers/json?all=1&filters=%7B%22label%22%3A%7B%22dokku%22%3Atrue%7D%2C%22status%22%3A%7B%22exited%22%3Atrue%7D%7D: dial unix /var/run/docker.sock: connect: permission denied'''),
        customStyle=styles.code_container, language='python'),

        dcc.Markdown(s(
        '''
        &nbsp;

        If you're receiving the above user permission error, please
        [contact support](/dash-deployment-server/support)
        '''))
    ]),

])

# # # # # # #
# Analytics
# # # # # # #
Analytics = html.Div(children=[
    html.H1('Dash App Analytics'),
    dcc.Markdown(s('''
    #### Dash App Analytics

    After you have successfully deployed a Dash App to the Dash Deployment
    Server, you can monitor app performance via the app analytics and logs.
    Here, navigate to the Dash Deployment Server UI and select the app to
    display analytics.

    ''')),

    html.Img(
        alt='App Analytics',
        src='/assets/images/dds/analytics.png',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),
])

# # # # # # #
# Logs
# # # # # # #
Logs = html.Div(children=[
    html.H1('Dash App Logs'),
    dcc.Markdown(s('''
    ***

    #### Dash App Logs (via UI)

    If you have successfully deployed a Dash App to the Dash Deployment
    Server, you can view the app's logs via the Dash Deployment Server UI.
    From your list of apps, open the app and then select **Logs**.
    ''')),

    html.Img(
        alt='App Logs',
        src='/assets/images/dds/logs.png',
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    dcc.Markdown(s('''
    ***

    #### Dash App Logs (via Command Line)

    Alternatively, the above can be accomplished via the command line.
    To view the logs for a specific Dash App run the following command
    in your terminal:

    ''')),

    dcc.SyntaxHighlighter(s(
    '''$ ssh dokku@<your-dash-domain> logs <your-app-name> --num -1'''),
    customStyle=styles.code_container, language='python'),

    dcc.Markdown(s('''

    &nbsp;

    This will work for any application that you own. This command
    authenticates with the server with ssh.
    [Configure SSH Authentication](/dash-deployment-server/ssh).

    &nbsp;

    **Options**
    - `--num`, `-n`: The number of lines to display. By default, 100
    lines are displayed.
       Set to -1 to display _all_ of the logs. Note that we only store logs
       from the latest app deploy.
    - `--tail`, `-t`: Continuously stream the logs.
    - `--quiet`, `-q`: Display the raw logs without colors, times, and names.
    ''')),
])

# # # # # # #
# Support
# # # # # # #
Support = html.Div(children=[
    html.H1('Plotly Enterprise Support'),
    dcc.Markdown(s('''
    ***

    #### Need to Contact Support?

    If you encounter any issues deploying your app you can email
    `onpremise.support@plot.ly`. It is helpful to include any error
    messages you encounter as well as available logs. See [App Logs](/dash-deployment-server/logs) on how
    to obtain Dash App logs. Additionally, see below for the Plotly Enterprise support
    bundle.
    ''')),

    dcc.Markdown(s('''
    ***

    #### Enterprise Support Bundle

    If you're requested to send the full support bundle you can
    download this from your Plotly Enterprise Server Manager
    (e.g. `https://<your.plotly.domain>:8800`). Please note you
    will need admin permissions to access the Server Manager.
    Navigate to the Server Manager and then select the Support tab.
    There you will see the option to download the support bundle.
    '''))
])
