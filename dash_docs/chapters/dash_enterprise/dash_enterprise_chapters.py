# -*- coding: utf-8 -*-
import dash
import dash_auth
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output
import os
import plotly
from dash_docs import styles
from dash_docs import reusable_components as rc
from dash_docs import tools

if os.environ.get('DASH_APP_LOCATION', '') != 'ABSOLUTE':
    from dash_docs.server import app
else:
    from server import app


def Blockquote():
    if 'DASH_DOCS_URL_PREFIX' in os.environ:
        return None
    return rc.Markdown('''
        > This documentation is for [Dash Enterprise](https://plotly.com/dash).
        > Dash Enterprise is the fastest way to write & deploy Dash apps and
        > Jupyter notebooks.
        > 10% of the Fortune 500 uses Dash Enterprise to productionize AI and
        > data science apps. [Find out if your company is using Dash Enterprise](https://go.plotly.com/company-lookup)
    ''')


# # # # # # #
# Initialize
# # # # # # #
Initialize = html.Div(children=[
    html.H1('Part 1. Initialize Dash Apps on Dash Enterprise'),

    Blockquote(),

    rc.Markdown('''
        > This is the *1st* deployment chapter of the <dccLink href="/dash-enterprise" children="Dash Enterprise Documentation"/>.
        > The <dccLink href="/dash-enterprise/deployment" children="next chapter"/> covers deploying a Dash App on Dash Enterprise.

        Before creating or deploying a dash app locally, you need to initialize
        an app on Dash Enterprise.

        This can be achieved by visiting the Dash App Manager at
        `https://your-dash-server/Manager`
    '''),

    rc.Markdown('''
        ***

        1. Navigate to the Dash Enterprise App Manager at
        https://your-dash-server/Manager
    '''),

    rc.Markdown('''

        &nbsp;

        2. In the top right-hand corner, select **Create App**. The
        'Create Dash App' modal should appear. Here, name your dash app
        (app names must start with a lowercase letter and may
        contain only lowercase letters, numbers, and -) and then
        hit **Create**. It is important to keep in mind that this name is going
        to be part of the URL for your application.

    '''),

    html.Img(
        alt='Initialize App',
        src=tools.relpath('/assets/images/dds/add-app.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''

        &nbsp;

        3. After you have created the app, the app overview page will open with
        deployment instructions.

    '''),

    html.Img(
        alt='List of Apps',
        src=tools.relpath('/assets/images/dds/list-of-apps.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''

        &nbsp;

        4. Now, select the dash app to access the app overview.

    '''),

    html.Img(
        alt='Dash App Overview',
        src=tools.relpath('/assets/images/dds/app-overview.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''

        &nbsp;

        If you have successfully initialized an app, advance to
        <b><dccLink
            children="Part 2. Deploy Dash Apps on Dash Enterprise"
            href="/dash-enterprise/deployment"/>
        </b>.
        If you have encountered any issues, see
        <b><dccLink
            children="Troubleshooting"
            href="/dash-enterprise"
            />
        </b>
        for help.

    '''),

])


# # # # # # #
# Deploy App
# # # # # # #
Deploy = html.Div(children=[
    html.H1('Part 2. Deploy Dash Apps on Dash Enterprise'),

    Blockquote(),

    rc.Markdown(
    '''
    > This is the *2nd* deployment chapter of the <dccLink href="/dash-enterprise" children="Dash Enterprise Documentation"/>.
    > The <dccLink href="/dash-enterprise/initialize" children="previous chapter"/> covered initializing a Dash App on Dash Enterprise.


    To deploy an app to your Dash Enterprise, you can either choose
    to deploy a cloned sample app, create a new app following the tutorial,
    or deploy an existing app that you created locally.

    '''),

    rc.Markdown(
    '''
    ***

    #### Which OS Are You Using?

    '''),

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
              Input('platform-2', 'value'))
def display_instructions2(platform):
    return [
        rc.Markdown(
        '''

        ***

        #### What Would You Like To Do?

        If you haven't deployed an app, you can get started by
        **Downloading a Sample App**, which is already setup
        for deployment. Alternatively, you can select **Create New App** to
        run through creating and deploying an app from the beginning.
        Otherwise, if you already have an existing app locally that you would
        like to deploy, then select **Deploy Existing App**.

        &nbsp;

        '''),

        dcc.Tabs([
            dcc.Tab(label='Download a Sample App', children=[
                html.Div([
                    rc.Markdown(
                    '''

                    &nbsp;

                    #### [Visit the sample app page](https://dash-gallery.plotly.host/Portal/)

                    And download & unzip the files.

                    '''),

                    (rc.Markdown('''
                    &nbsp;

                    Then, install [Git for Windows](https://git-scm.com/download/win).

                    ''') if platform == 'Windows' else
                    ''),

                    rc.Markdown(
                    '''
                    In Git Bash, navigate into the sample app folder and
                    initialize the repository.

                    ```shell
                    $ cd sample-app
                    $ git init
                    ```
                    ''',
                    style=styles.code_container),


                    rc.Markdown(
                    '''
                    ***

                    #### Configure your Dash Enterprise to be your Git remote

                    In the root of your folder, run the following command to create a
                    remote host to your new app on Dash Enterprise.

                    &nbsp;

                    ##### Which Deployment Method Are You Using?

                    For most use cases, Plotly recommends using HTTPS as it
                    doesn't require any extra configuration. However, if
                    you are using self-signed certificates or if your server
                    has SAML enabled, then you should deploy with SSH.
                    <dccLink href="/dash-enterprise/ssh" children="Configure SSH Authentication"/>.

                    &nbsp;

                    '''),
                ])
            ]),
            dcc.Tab(label='Create New App', children=[
                html.Div([
                    (rc.Markdown('''
                    &nbsp;

                    First, install [Git for Windows](https://git-scm.com/download/win).
                    Then, in Git Bash:
                    ''') if platform == 'Windows' else
                    ''),

                    rc.Markdown(
                    '''

                    &nbsp;

                    #### Create a New Folder
                    '''),

                    rc.Markdown(
                    '''
                    ```shell
                    $ mkdir dash_app_example
                    $ cd dash_app_example
                    ```
                    ''', style=styles.code_container),

                    rc.Markdown(
                    '''

                    ***

                    #### Initialize the Folder with `git` and a `virtualenv`

                    '''),

                    rc.Markdown(
                    ('''
                    ```shell
                    $ git init # initializes an empty git repo
                    $ virtualenv venv # creates a virtualenv called "venv"
                    $ source venv/bin/activate # uses the virtualenv
                    ```
                    ''') if platform != 'Windows' else (
                    '''
                    ```shell
                    $ git init # initializes an empty git repo
                    $ virtualenv venv # creates a virtualenv called "venv"
                    $ source venv/Scripts/activate # uses the virtualenv
                    ```
                    '''), style=styles.code_container),

                    rc.Markdown(
                    '''
                    &nbsp;

                    `virtualenv` creates a fresh Python instance. You will need
                    to reinstall your app's dependencies with this virtualenv:
                    '''),

                    rc.Markdown(
                    '''
                    ```shell
                    $ pip install dash
                    $ pip install plotly
                    ```
                    ''', style=styles.code_container),

                    rc.Markdown(
                    '''
                    &nbsp;

                    You will also need a new dependency, `gunicorn`, for
                    deploying the app:
                    '''),

                    rc.Markdown(
                    '''
                    ```shell
                    $ pip install gunicorn
                    ```
                    ''', style=styles.code_container),

                    rc.Markdown(
                    '''
                    ***
                    #### Create Relevant Files For Deployment

                    Create the following files in your project folder:

                    **`app.py`**

                    `app.py` This is the entry point to your application,
                    it contains your Dash app code. This file must contain a
                    line that defines the server variable: `server = app.server`
                    '''),

                    rc.Markdown(
                    '''
                    ```python
                    import os

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
                                Input('dropdown', 'value'))
                    def display_value(value):
                      return 'You have selected "{}"'.format(value)

                    if __name__ == '__main__':
                      app.run_server(debug=True)
                    ```
                    ''',
                    style=styles.code_container),

                    rc.Markdown('''
                    ***

                    **`.gitignore`**

                    `.gitignore` Determines which files and folders are
                    ignored in git, and therefore ignored (i.e. not copied
                    to the server) when you deploy your application.
                    '''),

                    rc.Markdown(
                    '''
                    ```shell
                    venv
                    *.pyc
                    .DS_Store
                    .env
                    ```
                    ''', style=styles.code_container),

                    rc.Markdown(
                    '''
                    ***

                    **`Procfile`**

                    Declares what commands are run by app's containers. This is
                    commonly, `web: gunicorn app:server --workers 4` where app
                    refers to the file `app.py` and server refers to the variable
                    named `server` inside that file. gunicorn is the web server
                    that will run your application, make sure to add this in
                    your requirements.txt file.

                    '''),

                    rc.Markdown(
                    '''
                    ```shell
                    web: gunicorn app:server --workers 4
                    ```
                    ''', style=styles.code_container),

                    rc.Markdown(
                    '''
                    For some applications, you may require using the `worker`
                    process. For example, the
                    [Snapshot Engine](https://plotly.com/dash/snapshot-engine/) examples
                    use Celery - an asynchronous task/job queue & scheduler.

                    In this case, your `Procfile` might look something like this:
                    ```shell
                    web: gunicorn app:server --workers 4
                    worker: celery -A app:celery_instance worker
                    ```
                    When using a `worker` process in your `Procfile`
                    you will need to include a `DOKKU_SCALE` file (see below).

                    '''),

                    rc.Markdown(
                    '''
                    ***

                    **`requirements.txt`**

                    `requirements.txt` Describes the app's python dependencies.
                    You can fill this file in automatically with:
                    '''),

                    rc.Markdown(
                    '''
                    ```shell
                    $ pip freeze > requirements.txt
                    ```
                    ''', style=styles.code_container),

                    rc.Markdown(
                    '''
                    If you are using one of the enterprise packages, like
                    `dash-design-kit` or `dash-snapshots`, then you'll also
                    need to prefix this file with a "`--extra-index-url`" flag.
                    `--extra-index-url` will specify the download location
                    of these packages. For example, this file might look like:
                    ```
                    --extra-index-url=https://your-dash-server.com/Docs/packages
                    dash-design-kit
                    dash
                    gunicorn
                    ```

                    ***

                    **`DOKKU_SCALE`**

                    Optional. This should only be used when your `Procfile`
                    contains a `worker: ` command. This file will specify
                    the number of containers that should be used to run the
                    web & worker processes.

                    '''),

                    rc.Markdown(
                    '''
                    ```shell
                    web=1
                    worker=1
                    ```
                    ''', style=styles.code_container),

                    rc.Markdown(
                    '''
                    ***

                    #### Configure your Dash Enterprise to be your Git remote

                    In the root of your folder, run the following command to create a
                    remote host to your new app on Dash Enterprise.

                    &nbsp;

                    ##### Which Deployment Method Are You Using?

                    For most use cases, Plotly recommends using HTTPS as it
                    doesn't require any extra configuration. However, if
                    you are using self-signed certificates or if your server
                    has SAML enabled, then you should deploy with SSH.
                    <dccLink href="/dash-enterprise/ssh" children="Configure SSH Authentication"/>.

                    &nbsp;

                    '''),
                ])
            ]),
            dcc.Tab(label='Deploy Existing App', children=[
                html.Div([
                    (rc.Markdown('''
                    &nbsp;

                    First, install [Git for Windows](https://git-scm.com/download/win).
                    Then, in Git Bash:
                    ''') if platform == 'Windows' else
                    ''),

                    rc.Markdown(
                    '''

                    &nbsp;

                    #### Initialize the Folder With Git


                    '''),

                    rc.Markdown(
                    '''
                    ```shell
                    $ cd <your-folder-name>
                    $ git init # initializes an empty git repo
                    ```
                    ''', style=styles.code_container),

                    rc.Markdown(
                    '''
                    ***

                    #### Configure your Dash Enterprise to be your Git remote

                    In the root of your folder, run the following command to create a
                    remote host to your new app on Dash Enterprise.

                    &nbsp;

                    ##### Which Deployment Method Are You Using?

                    For most use cases, Plotly recommends using HTTPS as it
                    doesn't require any extra configuration. However, if
                    you are using self-signed certificates or if your server
                    has SAML enabled, then you should deploy with SSH.
                    <dccLink href="/dash-enterprise/ssh" children="Configure SSH Authentication"/>.

                    &nbsp;

                    '''),
                ])
            ]),
        ]),

]

@app.callback(Output('remote-and-deploy-instructions', 'children'),
              Input('deploy-method', 'value'))
def display_instructions_deploy(method):
    return [
        rc.Markdown('''

        &nbsp;

        '''),

        rc.Markdown(
        '''
        ```shell
        $ git remote add plotly dokku@your-dash-enterprise:your-dash-app-name
        ```
        ''' if method == 'SSH' else
        '''
        ```shell
        $ git remote add plotly https://your-dash-enterprise-server/GIT/your-dash-app-name
        ```
        ''',
        style=styles.code_container,
        ),

        rc.Markdown(
        '''
        &nbsp;

        Replace `your-dash-app-name` with the name of your Dash App that you
        supplied in Dash Enterprise and `your-dash-enterprise`
        with the domain of your Dash Enterprise platform.

        For example, if your Dash App name was `my-first-dash-app`
        and the domain of your organizations Dash Enterprise was
        `dash.plotly.acme-corporation.com`, then this command would be
        `git remote add plotly dokku@dash.plotly.acme-corporation.com:my-first-dash-app`.
            ''' if method == 'SSH' else '''
        &nbsp;

        Replace `your-dash-app-name` with the name of your Dash App that
        you supplied in the Dash Enterprise platform and `your-dash-enterprise`
        with the domain of your Dash Enterprise platform.

        For example, if your Dash App name was `my-first-dash-app`
        and the domain of your organizations Dash Enterprise was
        `dash.plotly.acme-corporation.com`, then this command would be
        `git remote add plotly https://dash.plotly.acme-corporation.com/GIT/my-first-dash-app`.
        '''),

        rc.Markdown(
        '''
        ***

        #### Deploying Changes

        Now, you are ready to upload this folder to your Dash Enterprise.
        Files are transferred to the server using `git`:
        '''),

        rc.Markdown(
        '''
        ```shell
        $ git status # view the changed files
        $ git diff # view the actual changed lines of code
        $ git add .  # add all the changes
        $ git commit -m 'a description of the changes'
        $ git push plotly master
        ```
        ''', style=styles.code_container),

        rc.Markdown(
        '''

        &nbsp;

        This command will push the code in this folder to the
        Dash Enterprise and while doing so, will install the
        necessary python packages and run your application
        automatically.

        Whenever you make changes to your Dash code,
        you will need to run those `git` commands above.

        If you install any other Python packages, add those packages to
        the `requirements.txt` file. Packages that are included in this
        file will be installed automatically by Dash Enterprise.
        '''),

        rc.Markdown(
        '''

        ***

        #### Deploy Failed?

        If your deploy has been unsuccessful, you can check that you have the
        <dccLink href="/dash-enterprise/application-structure" children="necessary files required for deployment"/>,
        or if you have a specific error, take a look at
        <dccLink href="/dash-enterprise/troubleshooting" children="Common Deployment Errors"/>.

        ''')
    ]

# # # # # # #
# Adding Static Assets
# # # # # # #
staticAssets = html.Div(children=[
    html.H1('Adding Static Assets'),

    Blockquote(),

    rc.Markdown(
    '''
    ***

    #### Adding Your Own CSS and JavaScript to Dash Apps

    Including custom CSS or JavaScript in your Dash apps is simple. Just
    create a folder named `assets` in the root of your app directory and include
    your CSS and JavaScript files in that folder. Dash will automatically
    serve all of the files that are included in this folder.

    For more information about custom CSS, JavaScripts, HTML index template,
    meta tags, or serving Dash's component libraries locally, see
    <dccLink href="/external-resources" children="Dash Docs"/>.

    ***

    #### Embedding Images in Your Dash Apps

    Apps deployed on Dash Enterprise are deployed under an app name
    prefix. As a consequence, images that are added to the `assets` folder will
    require the app name prefix in the relative path. For example, with the
    below folder structure:


    ```shell
    -- app.py
    -- assets/
       |-- my-image.png
    ```

    &nbsp;

    your `app.py` file you would include:

    '''),

    rc.Markdown(
    '''
    ```python
    html.Img(src=app.get_asset_url('my-image.png'))
    ```
    ''', style=styles.code_container)
])

# # # # # # #
# Configuring System Dependencies
# # # # # # #
ConfigSys = html.Div(children=[
    html.H1('Configuring System Dependencies'),

    Blockquote(),

    rc.Markdown('''
    In some cases you may need to install and configure system
    dependencies. Examples include installing and configuring
    database drivers or the Java JRE environment.
    Dash Enterprise supports these actions through an
    `apt-packages` file and a `predeploy` script.

    &nbsp;

    We have a collection of sample apps that install common system-level
    dependencies. These applications are _ready to deploy_:

    - [Oracle cx_Oracle Database](https://github.com/plotly/dash-on-premise-sample-app/pull/2)
    - [Pyodbc Database Driver](https://github.com/plotly/dash-on-premise-sample-app/pull/3)

    &nbsp;

    If you need help configuring complex system level dependencies, please
    reach out to our <dccLink href="/dash-enterprise/support" children="support"/> team.

    ***

    #### Install Apt Packages

    In the root of your application folder, create a file called
    `apt-packages`. Here you may specify apt packages to be
    installed with one package per line. For example, to install
    the ODBC driver we could include an `apt-packages` file that
    looks like:

    '''),

    rc.Markdown('''
    ```shell
    unixodbc
    unixodbc-dev
    ```
    ''', style=styles.code_container),

    rc.Markdown('''

    ***

    #### Configure System Dependencies

    You may include a pre-deploy script that executes in
    your Dash App's environment. For the case of adding an
    ODBC driver, we need to add ODBC initialization files into
    the correct systems paths. To do so, we include the ODBC
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

    '''),

    rc.Markdown('''
    ```shell
    cp /app/odbc.ini /etc/odbc.ini
    cp /app/odbcinst.ini /etc/odbcinst.ini
    ```
    ''', style=styles.code_container),

    rc.Markdown('''
    &nbsp;

    ##### Run Pre-Deploy Script Using `app.json`

    Next we must instruct Dash Enterprise to run our `setup_pyodbc`
    file by adding a JSON configuration file named `app.json`
    into the root of our application folder.

    '''),

    rc.Markdown('''
    ```json
    {
        "scripts": {
            "dokku": {
                "predeploy": "/app/setup_pyodbc"
            }
        }
    }
    ```
    ''', style=styles.code_container),

    rc.Markdown('''
    ***

    Now when the application is deployed, it will install the apt
    packages specified in `apt-packages` and run the setup file
    specified in `app.json`. In this case it allows us to install
    and then configure the ODBC driver.

    To see this example code in action
    [check out our ODBC example](https://github.com/plotly/dash-on-premise-sample-app/pull/3#issue-144272510)
     On-Premises application.
    ''')
])


# # # # # # #
# Env Vars
# # # # # # #
EnvVars = html.Div(children=[
    html.H1('Setting Environment Variables'),

    Blockquote(),

    rc.Markdown('''
    In Plotly Enterprise 2.5.0 and up, you can store secrets as environment variables
    instead of hardcoded in your application code.
    It's good practice to keep application
    secrets like database passwords outside of your code so that they aren't
    mistakenly exposed or shared. Instead of storing these secrets in code,
    you can store them as environment variables and your Dash Application code
    can reference them dynamically.

    '''),

    rc.Markdown('''

    ***

    #### Add Environment Variables

    To add environment variables via the Dash Enterprise UI,
    navigate to the application settings. Here, use the text boxes to
    add the environmental variable name and value. For example, `"DATABASE_USER"`
    and `"DATABASE_PASSWORD"`.

    '''),

    html.Img(
        alt='Add Environment Variables',
        src=tools.relpath('/assets/images/dds/add-env-variable.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''

    ***

    #### Referencing Environment Variables in Your Code

    You can reference these variables with the `os.environ` module:

    '''),

    rc.Markdown(
    '''
    ```python
    database_password = os.environ['DATABASE_PASSWORD']
    ```
    ''',
    style=styles.code_container,
    ),

    rc.Markdown('''
    &nbsp;

    Alternatively, if the variable isn't in your environment and you want
    to fall back to some other value, use:

    '''),

    rc.Markdown(
    '''
    ```py
    database_password = os.environ.get('DATABASE_PASSWORD', 'my-default-database-password')
    ```
    ''',
    style=styles.code_container,
    ),



    rc.Markdown('''
    ***

    #### Defining Environment Variables In Your Local Environment

    By referencing these environment variables in our code, we'll need to add
    these variables to our local environment as well. One easy way to do
    this is to define the variables on-the-fly when you run `python app.py`.
    That is, instead of running `python app.py`, run:

    ```shell
    $ DATABASE_USER=chris DATABASE_PASSWORD=my-password python app.py
    ```

    &nbsp;

    Alternatively, you can define them for your session by "exporting" them:
    '''),

    rc.Markdown(
    '''
    ```shell
    $ export DATABASE_USER=chris
    $ export DATABASE_PASSWORD=my-password
    $ python app.py
    ```
    ''',
    style=styles.code_container,
    ),


    rc.Markdown('''
    ***

    #### Delete Environment Variables

    To remove an environment variable via the Dash Enterprise UI,
    navigate to the application settings. Here, simply click the red
    cross situated to the right-hand side of the environment variable.

    '''),

    html.Img(
        alt='Delete Environment Variables',
        src=tools.relpath('/assets/images/dds/remove-env-variable.png'),
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

    Blockquote(),

    rc.Markdown('''
    In Dash Enterprise, Dash Apps are run in isolated containers.
    Dash Enterprise builds the entire system for each individual app
    from scratch, including installing a fresh instance of Python, installing
    dependencies, and more. This isolation and containerization is great: it
    allows for one app's dependencies to not impact the next app's and,
    from a security perspective, ensures that applications can't modify or
    access the underlying server. One part of this isolation is that each app
    has its own "ephemeral" filesystem. This means that:

    - By default, files that are saved in the app's environment aren't
    persisted across deploys.
    - By default, files (even networked file systems) that are on the actual
    physical server aren't actually accessible to the application.

    &nbsp;

    Starting in Plotly Enterprise 2.5.0, you can map filesystems from the
    underlying server into the application. This allows you to save files
    persistently as well as read files from the underlying server, including
    networked file systems.

    Since this feature has security implications, only directories specified
    in the Plotly-On-Premise Server Manager can be mapped to Dash Apps.
    > Note that in Plotly Enterprise versions before 3.1.0 only users with admin privileges
    > could map local directories into their apps. Please contact `onpremise.support@plotly.com` if
    > you have any questions.

    ***

    #### Approve Directories for Mapping

    A server administrator with access to `https://<your.plotly.domain>:8800/settings`
    can allow certain directories on the host server to be mapped to dash apps. Go to
    the *Allowed Directories for Mapping* section of the settings page and add the path(s)
    of approved directories.

    '''),

    html.Img(
        alt='Add Admin/Superuser Status',
        src=tools.relpath('/assets/images/dds/specify-directories-for-mapping.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''

    ***

    #### Add Directory Mapping

    To add a directory mapping via the Dash Enterprise UI,
    navigate to the application **Settings** and scroll down to
    **Directory Mappings**. Here, use the text boxes to
    add the **Host Path** and **App Path**. For example, `/srv/app-data`
    and `/data`.

    '''),

    html.Img(
        alt='Add Directory Mapping',
        src=tools.relpath('/assets/images/dds/add-dir-map.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

rc.Markdown('''

    &nbsp;

    If the directory you're trying to map from isn't admin-approved, you will see an error
    message.

    &nbsp;

    '''),

    html.Img(
        alt='Add Directory Mapping',
        src=tools.relpath('/assets/images/dds/map-directory-not-approved.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''

    ***

    #### Referencing the File System in Your Code

    If you have mapped the directory from `/srv/app-data` to `/data`, then you
    can read files from this folder in your application with the following code:

    '''),

    rc.Markdown('''
    ```python
    import os
    file_pathname = os.path.join(os.sep, 'data', 'my-dataset.csv')
    ```
    ''',
    style=styles.code_container,
    ),

    rc.Markdown('''
    &nbsp;

    In some cases, the filesystems that you reference in your deployed
    application may be different from those that you reference locally.
    In your application code, you can check which environment you are in
    with the following code:

    '''),

    rc.Markdown(
    '''
    ```python
    if 'DASH_APP_NAME' in os.environ:
        # this is a deployed app
        filepath = os.path.join(os.sep, 'data', 'my-dataset.csv')
    else:
        # local file path
        filepath = os.path.join(os.sep, 'Users', 'chris', 'data', 'my-dataset.csv')
    ```
    ''',
    style=styles.code_container,
    ),

    rc.Markdown('''
    ***

    #### Recommendations

    If you are mounting a filesystem, we have the following recommendations:

    - Try to isolate the data that you need into its own, app-specific folder
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
    or <dccLink href="/dash-enterprise/support" children="contact our support team"/>.

    ***

    #### Remove Directory Mapping

    To remove directory mappings via the Dash Enterprise UI,
    navigate to the application **Settings** and scroll down to
    **Directory Mappings**. Next, use the red cross situated to the
    right-hand side of the environment variable.

    '''),

    html.Img(
        alt='Remove Directory Mapping',
        src=tools.relpath('/assets/images/dds/remove-dir-map.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),
])


# # # # # # #
# Authenticating to Dash Enterprise with SSH
# # # # # # #
Ssh = html.Div(children=[
    html.H1('Authenticating to Dash Enterprise with SSH'),

    Blockquote(),

    rc.Markdown('''

    In Plotly Enterprise 2.4.0 and above, you can deploy your apps using
    either HTTPS or SSH. If you are deploying with HTTPS, then you do not
    need to set up an SSH key. Thus, you can skip this tutorial and go
    straight to
    <dccLink href="/dash-enterprise/initialize" children="Initialize Dash Apps on Dash Enterprise"/>.

    &nbsp;

    If you are deploying with SSH then you need to add a SSH Key to the
    Dash Enterprise. SSH Keys are used to authenticate your git
    session with the server. Deploying with SSH takes a little bit more
    time to set up but it allows you to deploy without typing in your
    username and password each time. Continue below for instructions on
    how to generate and add a SSH Key.

    ***

    '''),

    rc.Markdown('''
    #### Why Deploy with SSH?

    We recommend deploying with HTTPS for most of our users. However, there
    are a few cases where deploying with SSH is advantageous:

    - If your Dash Enterprise is using a **self-signed certificate**,
    deploying with HTTPS
    [requires some extra, challenging configuration](https://stackoverflow.com/questions/11621768/).
    In these cases, it will be easier to configure deployment using SSH.
    - If your Dash Enterprise is configured with **SAML**, then the
    HTTPS method will not work.
    - If you are experiencing connectivity issues due to network latency, consider deploying with SSH instead; this method is often less susceptible to timeouts than HTTP, and so may provide a more reliable means of deploying your app.
    deploying with HTTP

    ***

    #### Already Have an SSH Key?

    If you already have an SSH key that you've used in other
    services, you can use that key instead of generating a new one.
    For instructions on how to add an existing SSH Key to Dash Enterprise,
    scroll down to **Copy and Add SSH Key**.

    ***

    ## Generate and Add an SSH Key

    '''),

    rc.Markdown('''
    #### Which OS Are You Using?

    '''),

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
              Input('platform', 'value'))
def display_instructions(platform):
    return [

        (rc.Markdown('''
        These instructions assume that you are using
        **Git Bash** on Windows, which is included in the
        official [Git for Windows release](https://git-scm.com/download/win).
        ''') if platform == 'Windows' else
        ''),

        rc.Markdown('''
        ***

        #### Generate a New SSH Key

        '''),

        rc.Markdown(
        '**1. Open Git Bash**' if platform == 'Windows' else
        '**1. Open Terminal**'
        ),

        rc.Markdown('''
        **2. Generate Key**

        This command will walk you
        through a few instructions.
        '''),

        rc.Markdown(
        '''
        ```shell
        $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
        ```
        ''',
        style=styles.code_container,
        ),

        rc.Markdown('''
        ***

        #### Check the SSH-Agent

        **1. Ensure the ssh-agent is running:**
        '''),

        rc.Markdown(
            (
            '''
            ```shell
            $ eval $(ssh-agent -s)
            ```
            ''' if platform == 'Windows' else
            '''
            ```shell
            $ eval "$(ssh-agent -s)"
            ```
            '''),
            style=styles.code_container,
        ),

        rc.Markdown('''
        &nbsp;

        **2. Run `ssh-add`**

        Replace `id_rsa` with the name of the key that you
        created above if it is different.
        '''),

        rc.Markdown(
            (
            '''
            ```shell
            $ ssh-add ~/.ssh/id_rsa
            ```
            ''' if platform == 'Windows' else
            '''
            ```shell
            $ ssh-add -k ~/.ssh/id_rsa
            ```
            '''),
            style=styles.code_container,
        ),

        rc.Markdown('''
        ***

        #### Copy and Add SSH Key

        **1. Copy the SSH key to your clipboard.**

        Replace `id_rsa.pub` with the name of the key that you
        created above if it is different.

        '''),

        rc.Markdown(
            (
            '''
            ```shell
            $ clip < ~/.ssh/id_rsa.pub
            ```
            '''
            if platform == 'Windows' else
            '''
            ```shell
            $ pbcopy < ~/.ssh/id_rsa.pub
            ```
            '''
            if platform == 'Mac' else
            '''
            ```shell
            $ sudo apt-get install xclip\n$ xclip -sel clip < ~/.ssh/id_rsa.pub
            ```
            '''),
            style=styles.code_container,
        ),

        rc.Markdown('''
        &nbsp;

        **2. Add SSH Key**

        Select **SSH Keys** in the top navigation menu of the Dash
        Enterprise UI. Here, select **Add Key** and in the 'Add
        SSH Key' modal, paste in your SSH Key.
        '''),

        html.Img(
            alt='Add SSH Key',
            src=tools.relpath('/assets/images/dds/add-ssh-key.png'),
            style={
                'width': '100%', 'border': 'thin lightgrey solid',
                'border-radius': '4px'
            }
        ),

        rc.Markdown('''
        &nbsp;

        **3. Confirm it Has Been Added**

        Once you've added an SSH key, it should be added to your list of SSH
        Keys like the image below.
        '''),

        html.Img(
            alt='List of SSH Keys',
            src=tools.relpath('/assets/images/dds/list-of-ssh-keys.png'),
            style={
                'width': '100%', 'border': 'thin lightgrey solid',
                'border-radius': '4px'
            }
        ),

        rc.Markdown('''
        ***

        #### Modify SSH Config

        Next, specify a custom port in your SSH config. By default, this
        should be `3022` but your server administrator may have set it to
        something different.

        This file is located in `~/.ssh/config`. If it's not there, then
        create it. Add the following lines to
        this file, replacing `your-dash-enterprise-server` with the domain of
        your Dash Enterprise server (without `http://` or `https://`).
        '''),

        rc.Markdown('''
        ```
        Host your-dash-enterprise-server
            Port 3022
        ```''', style=styles.code_container),

        (rc.Markdown('''
        If you're having trouble opening this file, you can run
        `$ open ~/.ssh/config` which will open the file using your default
        editor. If the file doesn't exist, then you can open that hidden
        folder with just `$ open ~/.ssh`
        ''') if platform == 'Mac' else ''),

        (rc.Markdown('''
        Please be careful not to save your SSH config as a .txt file as
        it will not be recognized by Git when deploying your applications.
        If you are using Notepad to create your SSH config, you can force the
        removal of the .txt extension by naming the file "config", including
        the quotes, in the Save As dialog box.
        ''') if platform == 'Windows' else ''),


        rc.Markdown('''
        ***

        If you have successfully added your SSH Key, advance to
        <b>
            <dccLink
                children="Part 1. Initialize Dash Apps on Dash Enterprise"
                href="/dash-enterprise/initialize"
            />
        </b>.
        ''')
    ]

# # # # # # #
# Managing Dash Apps from the Command Line
# # # # # # #
Cli = html.Div(children=[
    html.H1('Managing Dash Apps via Dokku instead of Official API'),

    Blockquote(),

    rc.Markdown('''
    Certain management actions are not yet exposed in the official 
    <dccLink href="/dash-enterprise/api" children="Dash Enterprise GraphQL API"/>.
    
    Until these commands are exposed in the API,
    you can run SSH commands against a core part of the Dash Enterprise
    technology stack, `dokku`.
    
    These commands should be treated as **temporary workarounds** until they are officially 
    supported in the GraphQL API. **Support for these commands may be dropped in 
    the future.**
    
    ***
    
    After setting up SSH authentication (see our <dccLink href="/dash-enterprise/ssh" children="ssh doc"/>), you will
    be able to use the commands below to help manage your apps from the command line.

    All commands are performed using `ssh dokku@your-dash-enterprise -p PORT command flags appname` where
    `PORT` is the ssh port for Dash Enterprise (usually 3022). Dash Enterprise will compare the private key supplied to the ssh command
    and the public key uploaded to Dash Enterprise in order to authenticate the user initiating the request.

    > Note that using the same public key for multiple users on Dash Enterprise isn't supported and will likely prevent it
    > from authenticating to the correct user.

    ***

    '''),

    rc.Markdown('''

    ### List of exposed Dash Enterprise commands:


    #### App-related Commands:

    > These commands can only be run by the app-owner or an admin account.'''),

    html.Details([
        html.Summary('Lock app'),
        rc.Markdown('''
        &nbsp;

        If you wish to disable deploying for a period of time, this can be
        done via deploy locks. Normally, deploy locks exist only for the duration
        of a deploy to prevent deploys from colliding, but a deploy lock can
        be created at any time by running the apps:lock command.

        **Example:**


        `ssh dokku@your-dash-enterprise -p PORT apps:lock my-dash-app`


        &nbsp;
        ''')]),

    html.Details([
        html.Summary('Unlock app'),
        rc.Markdown('''
        &nbsp;

        In some cases, it may be necessary to remove an existing deploy lock.
        This can be performed via the apps:unlock command.

        > **Warning**: Removing the deploy lock will not stop in-progress deploys.
        At this time, in-progress deploys will need to be manually terminated by
        someone with access to the Dash Enterprise server console.

        **Example:**
        `ssh dokku@your-dash-enterprise -p PORT apps:unlock my-dash-app`

        &nbsp;
        # ''')]),

    html.Details([
        html.Summary('Get app logs'),
        rc.Markdown('''
        &nbsp;

        You can get logs of an app using the logs command:

        **Example:**
        `ssh dokku@your-dash-enterprise -p PORT logs my-dash-app`

        `logs` also support following flags:

        ```
        -n, --num NUM          # the number of lines to display
        -p, --ps PS            # only display logs from the given process
        -t, --tail             # continually stream logs
        -q, --quiet            # display raw logs without colors, time and names
        ```

        You can use these flags as follows:

        `ssh dokku@your-dash-enterprise -p PORT logs my-dash-app -t -p web`

        &nbsp;
        ''')]),

    html.Details([
        html.Summary('Get logs from failed deploy'),
        rc.Markdown('''
        &nbsp;

        In some cases, it may be useful to retrieve the logs from a previously failed deploy.
        You can retrieve these logs with the logs:failed command.

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT logs:failed my-dash-app`

        &nbsp;
        ''')]),

    html.Details([
        html.Summary("Rebuild an app's environment"),
        rc.Markdown('''
        &nbsp;

        You can trigger an application to rebuild its environment using `ps:rebuild`.

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT ps:rebuild my-dash-app`

        &nbsp;
        ''')]),

    html.Details([
        html.Summary("Get a report of your app's status"),
        rc.Markdown('''
        &nbsp;

        This command displays a process report for one or more apps.

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT ps:report my-dash-app`

        You can also retrieve a specific piece of service info via flags:
        ```
        --processes         # Display only the number of running processes
        --deployed          # Display only the deploy status i.e. true or false
        --running           # Display the running status i.e. true or false
        --restore           # Display the running status i.e. true or false
        --restart-policy    # Display the restart policy for the app
        ```

        `ssh dokku@your-dash-enterprise -p PORT ps:report my-dash-app --processes`

        &nbsp;
        ''')]),

    html.Details([
        html.Summary("Restart an app"),
        rc.Markdown('''
            &nbsp;

            Applications can be restarted, which is functionally identical to releasing and deploying an application.

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT ps:restart my-dash-app`

            &nbsp;
            ''')
    ]),

    html.Details([
        html.Summary("Stop an app"),
        rc.Markdown('''
            &nbsp;

            Deployed applications can be stopped using the ps:stop command.
            This turns off all running containers for an application, and will result in a 502 Bad Gateway response.

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT ps:stop my-dash-app`

            &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Start an app"),
        rc.Markdown('''
            &nbsp;

            All stopped containers can be started using the ps:start command.

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT ps:start my-dash-app`

            &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Scale app processes"),
        rc.Markdown('''
        &nbsp;

        Dash Enterprise can also manage scaling applications (increase the number of containers for processes defined
        in the Procfile) via the `ps:scale` command. Dash Enterprise only scales the web process by default so if you
        define others you will need to scale them.

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT ps:scale my-dash-app web=1`

        This command can be used to scale multiple process types at the same time.

        `ssh dokku@your-dash-enterprise -p PORT ps:scale my-dash-app web=1 worker=1`

        The ps:scale command with no process type argument will output
        the current scaling settings for an application:

        ```
        ssh dokku@your-dash-enterprise -p PORT ps:scale my-dash-app
        -----> Scaling for my-dash-app
        -----> proctype           qty
        -----> --------           ---
        -----> web                1
        -----> worker             1
        ```

        &nbsp;
    ''')
    ]),

    html.Details([
        html.Summary("List persistent storage directories"),
        rc.Markdown('''
            &nbsp;

            List bind mounts for an app's container(s) (host:container).
            See our doc on <dccLink href="/dash-enterprise/map-local-directories" children="mapping local directories"/> for more info on
            how to set these up.

            **Example:**
            `ssh dokku@your-dash-enterprise -p PORT storage:list my-dash-app`

            &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Clear app cache"),
        rc.Markdown('''
            &nbsp;

            Building containers with buildpacks results in a persistent `cache` directory between deploys of the same application. To clear this cache directory, run the following shell command:

            **Example:**
            `ssh dokku@your-dash-enterprise -p PORT repo:purge-cache my-dash-app`

            &nbsp;
        ''')
    ]),

    rc.Markdown('''

    #### Service-related Commands:

    > These commands can only be run by the service-owner.'''),

    html.H5("Redis"),

    html.Details([
        html.Summary("Export the contents of a Redis database"),
        rc.Markdown('''
            &nbsp;

            Export a dump of the Redis service database. By default, datastore output is exported to stdout:

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT redis:export redis-db`

            You can redirect this output to a file:

           `ssh dokku@your-dash-enterprise -p PORT redis:export redis-db > db.dump`

           &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Upload an existing redis dump to Redis database"),
        rc.Markdown('''
            &nbsp;

            Import a datastore dump:

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT redis:import redis-db < db.dump`

            &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Get connection info for a Redis service"),
        rc.Markdown('''
            &nbsp;

            Print the connection information. Get connection information as follows:

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT redis:info redis-db`

            You can also retrieve a specific piece of service info via flags:

            ```shell
            ssh dokku@your-dash-enterprise -p PORT redis:info redis-db --config-dir
            ssh dokku@your-dash-enterprise -p PORT redis:info redis-db --data-dir
            ssh dokku@your-dash-enterprise -p PORT redis:info redis-db --dsn
            ssh dokku@your-dash-enterprise -p PORT redis:info redis-db --exposed-ports
            ssh dokku@your-dash-enterprise -p PORT redis:info redis-db --id
            ssh dokku@your-dash-enterprise -p PORT redis:info redis-db --internal-ip
            ssh dokku@your-dash-enterprise -p PORT redis:info redis-db --links
            ssh dokku@your-dash-enterprise -p PORT redis:info redis-db --service-root
            ssh dokku@your-dash-enterprise -p PORT redis:info redis-db --status
            ssh dokku@your-dash-enterprise -p PORT redis:info redis-db --version
            ```

            &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Get Redis logs"),
        rc.Markdown('''
            &nbsp;

            Print the most recent log(s) for this service.

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT redis:logs redis-db`

            By default, logs will not be tailed, but you can do this with the --tail flag:

            `ssh dokku@your-dash-enterprise -p PORT redis:logs redis-db --tail`

            &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Restart a Redis service"),
        rc.Markdown('''
        &nbsp;

        Restart the service:

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT redis:restart redis-db`

        &nbsp;
    ''')
    ]),

    html.Details([
        html.Summary("Stop a Redis service"),
        rc.Markdown('''
        &nbsp;

        Stop the service:

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT redis:stop redis-db`

        &nbsp;
    ''')
    ]),

    html.Details([
        html.Summary("Start a stopped Redis service"),
        rc.Markdown('''
        &nbsp;

        Start the service:

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT redis:start redis-db`

        &nbsp;
    ''')
    ]),

    html.H5("Postgres"),

    html.Details([
        html.Summary("Export the contents of a Postgres database"),
        rc.Markdown('''
            &nbsp;

            Export a dump of the Postgres service database. By default, datastore output is exported to stdout:

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT postgres:export postgres-db`

            You can redirect this output to a file:

           `ssh dokku@your-dash-enterprise -p PORT postgres:export postgres-db > db.dump`

           &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Upload an existing postgres dump to Postgres database"),
        rc.Markdown('''
            &nbsp;

            Import a datastore dump:

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT postgres:import postgres-db < db.dump`

            &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Get connection info for a Postgres service"),
        rc.Markdown('''
            &nbsp;

            Print the connection information. Get connection information as follows:

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db`

            You can also retrieve a specific piece of service info via flags:

            ```shell
            ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db --config-dir
            ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db --data-dir
            ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db --dsn
            ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db --exposed-ports
            ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db --id
            ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db --internal-ip
            ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db --links
            ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db --service-root
            ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db --status
            ssh dokku@your-dash-enterprise -p PORT postgres:info postgres-db --version
            ```

            &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Get Postgres logs"),
        rc.Markdown('''
            &nbsp;

            Print the most recent log(s) for this service.

            **Example:**

            `ssh dokku@your-dash-enterprise -p PORT postgres:logs postgres-db`

            By default, logs will not be tailed, but you can do this with the --tail flag:

            `ssh dokku@your-dash-enterprise -p PORT postgres:logs postgres-db --tail`

            &nbsp;
        ''')
    ]),

    html.Details([
        html.Summary("Restart a Postgres service"),
        rc.Markdown('''
        &nbsp;

        Restart the service:

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT postgres:restart postgres-db`

        &nbsp;
    ''')
    ]),

    html.Details([
        html.Summary("Stop a Postgres service"),
        rc.Markdown('''
        &nbsp;

        Stop the service:

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT postgres:stop postgres-db`

        &nbsp;
    ''')
    ]),

    html.Details([
        html.Summary("Start a stopped Postgres service"),
        rc.Markdown('''
        &nbsp;

        Start the service:

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT postgres:start postgres-db`

        &nbsp;
    ''')
    ]),



    rc.Markdown('''

    #### Service Linking Commands:

    > These commands can only be run by the user who owns both the service as well as the application.
    '''),

    html.Details([
        html.Summary("Link Redis to an app"),
        rc.Markdown('''
        &nbsp;

        Link the Redis service to the app. This will also restart your app:

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT redis:link redis-db my-dash-app`

        &nbsp;
    ''')
    ]),

    html.Details([
        html.Summary("Unlink Redis from an app"),
        rc.Markdown('''
        &nbsp;

        Unlink the Redis service from the app. This will also restart your app and unset related environment variables:

        **Example:**

        `ssh dokku@your-dash-enterprise -p PORT redis:unlink redis-db my-dash-app`

        &nbsp;
    ''')
    ])

    ])

# # # # # # #
# Dash App Authentication
# # # # # # #
Authentication = html.Div(children=[
    html.H1('Dash App Authentication'),

    Blockquote(),

    rc.Markdown('''
    Dash Enterprise will automatically implement user authentication if your
    <dccLink children="Dash app's privacy" href="/dash-enterprise/privacy"/>
    is set to *Restricted* (the default setting)
    or *Authorized* but not if is set to *Unauthorized*. You can access the authentication data within your app
    using the [`dash-enterprise-auth`](https://github.com/plotly/dash-enterprise-auth/) package.

    ***

    '''),

    rc.Markdown('''

    ## Using `dash-enterprise-auth` in an Existing Dash App

    If you have previously deployed your Dash app to your Dash Enterprise,
    simply add `dash-enterprise-auth` to your `requirements.txt` file.

    `dash-enterprise-auth` includes the method `create_logout_button` which allows you to
    add a logout button to your app's layout and it also includes three other methods,
    `get_username`, `get_user_data` and `get_kerberos_ticket_cache` (only applicable for
    certain server configurations), which provide information about the app's viewer and so
    must be called from within callbacks.

    The example below demonstrates how to use these callbacks. Note that in order to use
    `create_logout_button` locally you will have to set an environment variable called
    `DASH_LOGOUT_URL`. You can do this by running your code with `DASH_LOGOUT_URL=plotly.com python app.py`.

    '''),


    rc.Markdown('''
    ```python
    import dash
    from dash.dependencies import Input, Output
    import dash_core_components as dcc
    import dash_html_components as html
    import dash_enterprise_auth as auth


    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    server = app.server  # Expose the server variable for deployments


    # Standard Dash app code below
    app.layout = html.Div(className='container', children=[

        html.Div([
            html.H2('Sample App', id='header-title', className='ten columns'),
            html.Div(auth.create_logout_button(), className='two columns', style={'marginTop': 30})
        ]),
        html.Div(id='dummy-input', style={'display': 'none'}),

        html.Div([
            html.Div(
                className='four columns',
                children=[
                    dcc.Dropdown(
                        id='dropdown',
                        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
                        value='LA'
                    )
            ]),
            html.Div(
                className='eight columns',
                children=[
                    dcc.Graph(id='graph')
                ])
        ])
    ])


    @app.callback(Output('header-title','children'),
                  Input('dummy-input', 'children'))
    def update_title(_):

        # print user data to the logs
        print(auth.get_user_data())

        # update header with username
        return 'Hello {}'.format(auth.get_username())


    @app.callback(Output('graph', 'figure'),
                  Input('dropdown', 'value'))
    def update_graph(value):
        return {
            'data': [{
                'x': [1, 2, 3, 4, 5, 6],
                'y': [3, 1, 2, 3, 5, 6]
            }],
            'layout': {
                'title': value,
                'margin': {
                    'l': 60,
                    'r': 10,
                    't': 40,
                    'b': 60
                }
            }
        }

    if __name__ == '__main__':
        app.run_server(debug=True)
    ```
    ''',
    style=styles.code_container,
    )
])

# # # # # # #
# Dash App Privacy
# # # # # # #
AppPrivacy = html.Div(children=[
    html.H1('Dash App Privacy'),

    Blockquote(),

    rc.Markdown('''
    &nbsp;

    Starting in Version 3.0.0 of Dash Enterprise, you can restrict
    who is able to view your app from the app's management page.
     This will also restrict who will be able to see it in the
    <dccLink href="/dash-enterprise/portal" children="Dash App Portal"/>.

    Find a list of links to these pages for your apps at
    `https://<your-dash-enterprise>.com/Manager/apps`. Contact support
    if you have any questions about privacy in previous versions of Dash Enterprise.

    &nbsp;
    '''),

    html.Img(
        alt='Dash Enterprise Apps List',
        src=tools.relpath('/assets/images/dds/manager-apps-list.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''
    &nbsp;

    From the settings tab of your app's management page, scroll down
    to *App Privacy* to change the privacy settings of your app. If you choose
    the *Restricted* setting, an input will appear where you need to
    add a list of usernames of users that you would like to be able to view
    the app. Additionally, if LDAP is enabled, you can also add entire LDAP groups.

    &nbsp;
    '''),

    html.Img(
        alt='Dash App Privacy Settings',
        src=tools.relpath('/assets/images/dds/app-settings-privacy.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    )
])

# # # # # # #
# Adding Private Python Packages
# # # # # # #
PrivatePackages = html.Div(children=[
    html.H1('Adding Private Python Packages'),

    Blockquote(),

    rc.Markdown('''

    When a Dash App is deployed on the Dash Enterprise, the
    `requirements.txt` will install the relevant python dependencies. If you
    want to add private python packages you will need amend the
    `requirements.txt` file. This can be done via two methods: (1) using
    tarballs or (2) using environment variables.

    ***

    #### Using Tarballs

    To add private python packages to a Dash App using tarballs, you need to
    include the `tar.gz` file in your App's root folder. For example,

    ```python
    -- .gitignore
    -- app.py
    -- Procfile
    -- requirements.txt
    -- myPackage.tar.gz
    ```

    &nbsp;

    Then in the `requirements.txt` include:

    ```shell
    myPackage.tar.gz
    ```


    ***

    #### Using Environment Variables

    As of `pip==10.0.0`, it is possible to use environment variables within
    the `requirements.txt` file. Thus, private python packages can be added by
    using the `${VARIABLE}` syntax. For example,

    '''),

    rc.Markdown(
    '''
    ```shell
    git+http://${AUTH_USER}:${AUTH_PASSWORD}@git.example.com/MyProject#egg=MyProject
    ```
    ''',
    style=styles.code_container,
    ),

    rc.Markdown('''
    &nbsp;

    `AUTH_USER` and `AUTH_PASSWORD` variables can be added to your Dash App via
    the Dash Enterprise UI. For more information about adding
    environment variables to your Dash Apps, see
    <dccLink href="/dash-enterprise/environment-variables" children="Setting Environment Variables"/>

    ''')
])


# # # # # # #
# Redis
# # # # # # #
Redis = html.Div(children=[
    html.H1('Create and Link Redis Database'),

    Blockquote(),

    rc.Markdown('''
    Redis is a powerful in-memory database that is well-suited for many Dash
    applications. In particular, you can use Redis to:

    - Save application data
    - Enable queued and background processes with Celery.
    [Redis and Celery Demo App](https://github.com/plotly/dash-redis-demo)
    - Cache data from your callbacks across processes.
    <dccLink href="/performance" children="Caching in Dash with Redis"/>

    &nbsp;

    While Redis is an _in-memory database_, Dash Enterprise regularly
    backs up its data to the underlying server. So, it's safe for production
    usage. Dash Enterprise can dynamically spin up and manage secure
    instances of Redis for your application.
    '''),

    rc.Markdown('''
    ***

    #### Enable Redis Databases

    In Plotly Enterprise 2.5.0, Redis Databases are always enabled.

    For previous versions, navigate to Plotly On-Premises Server Settings
    (`https://<your.plotly.domain>:8800/settings`), then under **Special Options
    & Customizations** select **Enable Dash Customizations** and **Enable Redis
    Databases** for Dash Apps.
    '''),

    html.Img(
        alt='Enable Redis Databases',
        src=tools.relpath('/assets/images/dds/enable-redis.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''
    ***

    #### Create and Link (via UI)

    You can create one Redis instance that is used by multiple apps or you
    can create a unique Redis Database for each individual app.
    To start, we recommend creating a unique Redis Database for each
    Dash App. It will be easier for you to ensure that one application doesn't
    override the data from a separate application.

    &nbsp;

    In Plotly Enterprise 2.5.0 it is possible to create and link a Redis
    Database to your Dash App using the Dash Enterprise UI.
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
    '''),

    html.Img(
        alt='Create Database',
        src=tools.relpath('/assets/images/dds/create-redis-db.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''
    &nbsp;

    Next, navigate to **Apps** and create a new app (for more info see
    <dccLink
        children="Part 1. Initialize Dash Apps on Dash Enterprise"
        href="/dash-enterprise/initialize"
    />,
    in the 'Create App' modal you have the option of linking a database.
    Here, use the dropdown to select the database that you created previously
    (see image below).
    '''),

    html.Img(
        alt='Link Database',
        src=tools.relpath('/assets/images/dds/link-redis-db.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''
    &nbsp;

    ##### Create and Link a Database After an App Has Been Initialized.

    In the Dash Enterprise UI, select the app then navigate
    to the settings page. In Databases, use the dropdown to select
    **create and link database** then **Add**.

    '''),

    html.Img(
        alt='Create and Link Database in App',
        src=tools.relpath('/assets/images/dds/create-and-link-redis-db.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''
    ***

    #### Create and Link (via Command Line)

    While it is now possible to create and link Redis Databases via the
    Dash Enterprise UI, it is still possible to create and link a Redis
    database via the command line (using ssh):

    '''),

    rc.Markdown(
    '''
    ```shell
    $ ssh dokku@YOUR_DASH_SERVER redis:create SERVICE-NAME
    $ ssh dokku@YOUR_DASH_SERVER redis:link SERVICE-NAME APP-NAME
    ```
    ''',
    style=styles.code_container,
    ),

    rc.Markdown('''

    &nbsp;

    In the commands above, replace:
    * `YOUR_DASH_SERVER` with the name of your Dash server
    (same as when you run `git remote add`)
    * `SERVICE-NAME` with the name you want for your Redis service
    * `APP-NAME` with the name of your app (as specified in the
    Dash App Manager).

    '''),

    rc.Markdown('''
    ***

    #### Referencing Redis in Your Code

    You can reference your Redis Database with the `os.environ` module:

    '''),

    rc.Markdown(
    '''
    ```shell
    redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])
    ```
    ''',
    style=styles.code_container,
    ),

    rc.Markdown('''
    ***

    #### Using Redis inside Workspaces

    Dash Enterprise Workspaces share the same Redis instance as the deployed
    application.
    This enables you to inspect data of your Redis instances from within
    workspaces. However, it is important that you structure your code to
    not override Redis data.

    Each Redis instance has 16 available databases.

    `dash-snapshots` implicitly uses an alternative Redis database on the
    same instance.

    The Sample Applications & Templates demonstrate how to use an alternative
    Redis database if within the Workspace environment:

    ```
    if os.environ.get("DASH_ENTERPRISE_ENV") == "WORKSPACE":
        next_database_number = str((int(os.environ.get("REDIS_URL")[-1]) + 1) % 16)
        REDIS_URL = os.environ["REDIS_URL"][:-1] + next_database_number
        parsed_url = urlparse(os.environ.get("REDIS_URL"))
        if parsed_url.path == "" or parsed_url.path == "/":
            i = 0
        else:
            try:
                i = int(parsed_url.path[1:])
            except:
                raise Exception("Redis database should be a number")
        parsed_url = parsed_url._replace(path="/{}".format((i + 1) % 16))

        updated_url = parsed_url.geturl()
        REDIS_URL = "redis://%s" % (updated_url.split("://")[1])
    else:
        REDIS_URL = os.environ.get("REDIS_URL", "redis://127.0.0.1:6379")
    ```

    ***

    #### Running Redis on Your Local Machine

    To get started, see the [Redis documentation](https://redis.io/documentation)
    to download Redis and set up a local instance.

    &nbsp;

    By referencing Redis in our code, we'll need to add the variable to our
    local environment as well. One easy way to do this is to define the
    variable on-the-fly when you run `python app.py`.
    '''),

    rc.Markdown(
    '''
    ```shell
    $ REDIS_URL=redis://<your-redis-instance-ip>:6379 python app.py
    ```
    ''',
    style=styles.code_container,
    ),

    rc.Markdown('''
    &nbsp;

    ##### Windows Users

    Installing Redis from source on windows can be tricky. If you have the
    "Windows Subsystem for Linux", we recommend using that and installing
    the Redis in that linux environment. Otherwise, we recommend installing
    these [64-bit binary releases of Redis](https://github.com/ServiceStack/redis-windows#option-3-running-microsofts-native-port-of-redis).

    ''')
])


# # # # # # #
# Linking a Celery Process
# # # # # # #
Celery = html.Div(children=[
    html.H1('Linking a Celery Process'),

    Blockquote(),

    rc.Markdown(
    '''
    Celery is a reliable asynchronous task queue/job queue that supports both
    real-time processing and task scheduling in production systems. This makes
    Celery well suited for Dash Applications.

    For more detail on how to use Celery within Dash Enterprise, see the
    chapters in Dash Enterprise on the Dash Snapshot Engine or the
    Sample Applications and Templates.

    For more information about Celery, visit
    [Celery's documentation](http://docs.celeryproject.org/en/latest/).
    '''),

])

# # # # # # #
# Staging App
# # # # # # #
StagingApp = html.Div(children=[
    html.H1('Create a Staging Dash App'),

    Blockquote(),

    rc.Markdown(
    '''
    Once you have deployed your application, your end-users will expect that
    it is stable and ready for consumption. So, what do you do if you want to
    test out or share some changes on the server? We recommend creating
    separate applications: one for "production" consumption and another one
    for testing. You will share the URL of the "production" app to your
    end-users and you will use your "testing" app to try out different changes
    before you send them to your production app. With Dash Enterprise,
    creating a separate testing app is easy:

    ***

    ### Initialize a New Dash App

    <dccLink href="/dash-enterprise/initialize" children="Initialize a new app"/> in the
    Dash Enterprise UI. We recommend giving it the same name as your
    other app but appending `-stage` to it (e.g. `analytics-stage`).

    ***

    ### Configure a New Git Remote

    Add a new remote that points to this URL. In this example,
    we'll name the remote "stage":

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git add remote stage https://your-dash-enterprise/GIT/your-dash-app-name-stage
    ```
    ''',
    style=styles.code_container),

    rc.Markdown(
    '''
    ***

    ### Deploy Changes to Your Staging App

    Now, you can deploy your changes to this app just like you would
    with your other app. Instead of `$ git push plotly master`, you'll deploy
    to your staging app with:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git push stage master
    ```''',
    style=styles.code_container),

])

# # # # # # #
# Dash Enterprise PDF Service
# # # # # # #
pdfService = html.Div(children=[
    html.H1('Dash Enterprise PDF Service'),

        Blockquote(),

        rc.Markdown(
        '''

        The Dash Enterprise platform has an API endpoint for creating PDF exports
        of your Dash applications. The API is simple: pass in the URL of your
        Dash app and the sizing parameters and get back a PDF print out. You can
        automate PDF generation with
        <dccLink
            children="Dash Enterprise's Celery task queues"
            href="/dash-enterprise/celery-process"
        />
        or you can generate these PDFs on-the-fly.

        This API endpoint is used by the Dash Enterprise Snapshot Engine library.
        Refer to the
        [Snapshot Engine documentation](https://plotly.com/dash/snapshot-engine/)
        for more examples.

        ***

        #### API Parameters

        '''),

        rc.Markdown('''
        ```bash
        POST https://<your-dash-enterprise>/Manager/api/generate_report
        content-type: application/json
        plotly-client-platform: dash
        Authorization: Basic ...

        {
            "url": "...",
            "appname": os.environ.get('DASH_APP_NAME'),
            "secret_key": os.environ.get('DASH_SECRET_KEY'),
            "pdf_options": {
                "pageSize": "Letter",
                "marginsType": 1
            },
            "wait_selector": "body"
        }
        ```
        ''',
        style=styles.code_container),

        rc.Markdown(
        '''

        - `url` - The URL to download
        - `appname` - Your app's name.
        - `secret_key` - Your app's secret key. This is needed for authorizing the pdf generation.
        - `wait_selector` - A string that specifies a
        [CSS selector](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Simple_selectors).
        The API will wait until an element that matches this CSS selector
        appears on the screen before taking a screenshot. This ensures that
        the page has finished loading before taking a screenshot.
        In general, we recommend:
          - If there are no graphs on the page, then embed an
          `html.Div(id='waitfor')` in your `app.layout` or return it from
          the callback that gets executed last. With the id `waitfor`, the
          `wait_selector` would be `"#waitfor"`.
          - If the page has `dcc.Graph` elements on it, then you'll want
          to wait until these graphs have finished renderering. To do this,
          set the `wait_selector` to be `#graph_id .svg-container` where
          `"graph_id"` corresponds to the ID of the `dcc.Graph` component.
          `.svg-container` refers to a CSS class of an element that plotly
          inserts in the graph when it has finished rendering.
        - `pdf_options` - PDF sizing options. These options are similar to the
        options that you see when you print a web page using your web browser.
        They include:
          - `pageSize`: Predefined page size of the generated PDF. Available options:
            `A3`, `A4`, `A5`, `Legal`, `Tabloid`. Custom page sizes can be
            provided with the top level `page_size` property (see below).

          - `marginsType`: Specifies the type of margins to use. `0` for
            default margin, `1` for no margin, and `2` for minimum margin. We
            recommend using `1` and controlling the margins yourself through
            your app's CSS.
          - `landscape` (optional): `True` for landscape, `False` for portrait.
          - 'page_size' (optional): A dict specifying `width` & `height`
          in microns, e.g. {'width': 296700, 'height': 209900}.

        ***

        #### Basic Example

        This example provides a simple UI around the PDF API. You can run this
        example locally or you can deploy this example to Dash Enterprise.
        A few things to note:

         - If you're testing locally, you will have to specify default values for your
        DASH_DOMAIN_BASE, DASH_APP_NAME and DASH_SECRET_KEY. You can find them in the list of your app's
        environment variables. See <dccLink href="/dash-enterprise/environment-variables" children="our doc on environment variables"/>
        for more details.
        '''),

        rc.Markdown(
        '''
        ```python

        import dash
        from dash.dependencies import Input, Output, State
        import dash_core_components as dcc
        import dash_html_components as html

        import base64
        import os
        import requests

        app = dash.Dash(__name__)
        server = app.server


        app.layout = html.Div([
            html.Label('Website URL'),
            dcc.Input(
                id='website',
                value='https://dash.plotly.com'
            ),

            html.Div(html.B('CSS Selector')),
            html.Div(
                'Wait until an element targeted by this selector appears '
                'before taking a snapshot. These are standard CSS query selectors'.
            ),
            dcc.Input(
                id='wait_selector',
                value='#wait-for-layout'
            ),

            html.Button(id='run', children='Snapshot', n_clicks=0),

            html.Div(id='output'),

        ])


        @app.callback(Output('output', 'children'),
                      Input('run', 'n_clicks'),
                      State('website', 'value'),
                      State('wait_selector', 'value'))
        def snapshot_page(n_clicks, url, wait_selector):
            if n_clicks == 0:
                return ''
            payload = {
                'url': url,
                "appname": os.environ.get('DASH_APP_NAME', 'your-dash-app-name'),
                "secret_key": os.environ.get('DASH_SECRET_KEY', 'your-dash-app-secret-key'),
                'pdf_options': {
                    'pageSize': 'Letter',
                    'marginsType': 1
                },
                'wait_selector': wait_selector
            }

            res = requests.post(
                'https://{}/Manager/api/generate_report'.format(
                    os.environ.get('DASH_DOMAIN_BASE', 'your-dash-domain-base')
                ),
                json=payload
            )
            if res.status_code == 200:
                return html.A(
                    'Download',
                    href='data:application/pdf;base64,{}'.format(
                        base64.b64encode(res.content).decode('utf-8')
                    ),
                    download='dash.pdf',
                    target='_blank'
                )

            return html.Pre('Status: {}, Response: {}'.format(
                res.status_code, res.content
            ))


        if __name__ == '__main__':
            app.run_server(debug=True)
        ```
        ''',
        style=styles.code_container),

        rc.Markdown('''

        ***

        #### Custom Reporting Solutions

        Plotly helps companies modernize their reporting infrastructure with
        Dash. In particular, we help organizations with:
        - Our modules for saving and loading reports in Dash Enterprise
        - Converting existing PDF reports into Dash application code
        - Creating high-quality, branded PDF templates

        Get in touch with your sales rep or
        [reach out to us directly](https://plotly.com/get-demo/)
        to learn more.

        '''),

])

# # # # # # #
# Dash App SQL Database Connections
# # # # # # #
DataConnections = html.Div(children=[
    html.H1('Connect a Dash App to an SQL Database'),

    rc.Markdown(
    '''

    ## Managing Connection Drivers and Libraries

    Dash Apps can use open source libraries to query external databases and datastores in callbacks or job queues.

    The Python DB-API standardizes the interface for most Python database access modules. This allows us to write Dash
    apps with code that can be modified with little effort to connect to different types of databases with different dialects
    by following the standardized API. For more information on the Python DB-API, see [PEP-0249](https://www.python.org/dev/peps/pep-0249/).

    To query databases, you'll need to install the Python database packages and in many cases system level dependencies.
    For complete examples, see the relevant "Database Connections" section in Sample Apps & Templates:

    * Connecting to PostgreSQL
    * Connecting to MSSQL with pyodbc
    * Connecting to MySQL
    * Connecting to Oracle Express
    * Connecting to Databricks Cluster
    * Connecting to Dask Cluster

    ## Working with Connection Objects in a Dash App

    Many of the database apps follow a similar pattern:

    1. Install the database driver & system level dependencies. This will vary by database type and we recommend viewing
    the examples that we've provided first. Many of the database drivers more easily installed on Linux environments,
    and so we recommend developing these apps in a [Dash Enterprise Workspace](https://plotly.com/dash/workspaces/).

    2. Create a connection. We recommend using [SQLAlchemy](https://www.sqlalchemy.org) if available for your database.

    3. Store your connection's database password as an environment variable in your App Settings in the Dash Enterprise
    App Manager instead of storing it within code.

    4. Test that the database server has started successfully, verify that it is accepting connections, and validate the credentials and connection string; we can create a simple
    `try_connection` function which sends a basic query to the database and checks to see if it is successful. If it fails,
    the connection is retried after an exponentially increasing delay. This allows us to distinguish between errors
    arising from issues with the callback logic, and errors caused by database configuration or connectivity problems. Eg:
    ```
    @retry(wait=wait_exponential(multiplier=2, min=1, max=10), stop=stop_after_attempt(5))
    def try_connection():
        try:
            with postgres_engine.connect() as connection:
                stmt = text("SELECT 1")
                connection.execute(stmt)
            print("Connection to database successful.")

        except Exception as e:
            print("Connection to database failed, retrying.")
            raise Exception
    ```

    5. Consider [connection pooling](https://docs.sqlalchemy.org/en/14/core/pooling.html#using-connection-pools-with-multiprocessing-or-os-fork).
    In these examples above, we don't use database connection pools. Connection pools have tricky implications when using
    alongside `celery` or gunicorn's `--preload` option. If you aren't using `--preload` nor `celery`, then you can improve
    your query performance by using a node pool. With a node pool, connections are shared instead of recreated and discarded.
    It is possible to use --preload and celery with a node pool but it requires extra caution. For more details, see:
    > - [SQLAlchemy: Using Connection Pools with Multiprocessing or os.fork()](https://docs.sqlalchemy.org/en/14/core/pooling.html#using-connection-pools-with-multiprocessing-or-os-fork)
    > - [Not The Same Pre-fork Worker Model](https://www.yangster.ca/post/not-the-same-pre-fork-worker-model/)
    > - [SQLAlchemy connection pool within multiple threads and processes](https://davidcaron.dev/sqlalchemy-multiple-threads-and-processes/)

    To disable connection pooling, you will use the `NullPool`:
    ```
    from sqlalchemy.pool import NullPool
    engine = create_engine(
        'postgresql+psycopg2://username:password@localhost/test',
        pool=NullPool)
    ```

    6. Construct your SQL query. You have several options here:
        * Use raw SQL commands. This is the low-level option and great if you want full control & transparency and are
        comfortable with SQL. We recommend using the [`text`](https://docs.sqlalchemy.org/en/13/core/sqlelement.html#sqlalchemy.sql.expression.text)
        function in `sqlalchemy` and parameterized queries. This will avoid SQL Injection issues:
        ```python
        import pandas as pd
        from sqlalchemy import text

        t = text("SELECT * FROM users WHERE id=:user_id")
        result = pd.read_sql(t, params={'user_id': 12})
        ```
        * Use the Pythonic classes available with `sqlalchemy`. For  examples, see [SQLAlchemy — Python Tutorial
        ](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91).

        *; Use [ibis](https://ibis-project.org), a library that uses SQLAlchemy under the hood but has a more Pandas-like interface.

    7. Open a connection when you need to perform an operation and close it after. In `sqlalchemy`, this can be done with the `with engine.connect()` clause.
    While a NullPool can do this for us by default as well, we can also use the Engine object to implicitly open and close connections
    on an ad hoc basis for both this and other pooling implementations. Enclosed in the `with`context statement, the
    connection object generated by the `Engine.connect()` method is automatically closed by `Connection.close()` at the
    end of the codeblock e.g.
    ```python
    with mssql_engine.connect() as connection:
         countries = pd.read_sql('SELECT DISTINCT location from data', connection)
    ```

    ## Database URLs

    As we saw earlier when creating our SQLAlchemy engine object, a database URL is required to be passed to specify the
    dialect and driver we will use to connect to our database. This can be passed to the pool or directly to the Engine
    object to use a default pool.
    ```
    dialect+driver://username:password@host:port/database

    # For PostgreSQL
    postgres+psycopg2://username:password@localhost:8050/test-database
    ```
    For more information on dialects and drivers, see [here](https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls).

    '''),
])

# # # # # # # # #
# Common Deployment Errors
# # # # # # # # #
Troubleshooting = html.Div(children=[
     html.H1('Common Deployment Errors'),

    Blockquote(),

    rc.Markdown(
        '''
        This chapter describes errors that you may encountering when deploying with `git push plotly master`.

        Troubleshooting Checklist

        1. Search for your error message on this page.
        2. Verify that you can deploy a sample application or template.
        3. Verify the Dash Enterprise-specific files required for deployment like requirements.txt & Procfile. <dccLink href="/dash-enterprise/application-structure" children="View a full list of these files"/>.
        4. Verify that the requirements & versions listed in the App Manager for your application match your expectations and what you have specified in your requirements.txt file. The requirements listed in the App Manager represent the exact versions being used in the application that is currently deployed.
        5. Try running your application in a Workspace.
        6. Try deploying your application from a Workspace. In Workspaces, git & ssh are preconfigured so running `git push plotly master` should "just work".
        7. Reach out to our <dccLink href="/dash-enterprise/support" children="support team"/> with the error that you encountered when doing a `git push plotly master`.

        The following is a collection of common error messages when running `git push`.
        
        
        ---
        '''
    ),

    rc.Markdown(
        '''
        ### error: failed to push some refs to dokku@<dash-enterprise>:<app-name>

        ```shell
        $ git push plotly master
        [...]
        To <your-dash-enterprise-host>:<your-dash-app>
        ! [remote rejected] master -> master (pre-receive hook declined)
        error: failed to push some refs to '<your-dash-enterprise-host>:<your-dash-app>'
        ```


        This is a generic error message that indicates that the git push deployment failed. The root cause of the error will be further up in the logs.

        In some cases, the error message may not exist or may be misleading. This page covers many of the common errors that may be reported further up in your deploy logs.
        
        
        ---
        '''
    ),

    rc.Markdown(
        '''
        ### cat /app/Procfile: No such file or directory

        ```shell
        $ git push plotly master
        [...]
        remote: App container failed to start!!
        =====> demo-app web container output:
            cat: /app/Procfile: No such file or directory
            cat: /app/Procfile: No such file or directory
        =====> end demo-app web container output
        To <your-dash-enterprise-host>:<your-dash-app>
        ! [remote rejected] master -> master (pre-receive hook declined)
        error: failed to push some refs to '<your-dash-enterprise-host>:<your-dash-app>'
        ```


        This error occurs when the project folder doesn’t contain a file named `Procfile`.

        See <dccLink href="/dash-enterprise/application-structure" children="Application Structure"/>
        page for more details on `Procfile`.
        
        
        ---
        '''
    ),


    rc.Markdown(
        '''
        ### Failed to find application object 'server' in 'index'

        ```shell
        remote: App container failed to start!!
        =====> <your-dash-app> web container output:
        [...]
        Failed to find application object 'server' in 'index'
        [...]
            raise HaltServer(reason, self.APP_LOAD_ERROR)
            gunicorn.errors.HaltServer: <HaltServer 'App failed to load.' 4>
        [...]
                raise HaltServer(reason, self.APP_LOAD_ERROR)
            gunicorn.errors.HaltServer: <HaltServer 'App failed to load.' 4>
            Failed to find application object 'server' in 'index'
            [2020-11-02 18:17:22 +0000] [191] [INFO] Worker exiting (pid: 191)
        =====> end aa-qa web container output
        To <your-dash-enterprise-host>:<your-dash-app>
        ! [remote rejected] master -> master (pre-receive hook declined)
        error: failed to push some refs to 'dokku@<your-dash-enterprise-host>:<your-dash-app>'
        ```


        This happens when `server = app.server` is missing from your code .

        See  <dccLink href="/dash-enterprise/application-structure" children="Application Structure"/>
        page for more details.
        
        
        ---
        '''
    ),


    rc.Markdown(
        '''
        ### Unable to select a buildpack

        ```shell
        $ git push plotly master
        [...]
        -----> Adding BUILD_ENV to build environment...
        -----> Unable to select a buildpack
        To <your-dash-enterprise-host>:<your-dash-app>
        ! [remote rejected] master -> master (pre-receive hook declined)
        error: failed to push some refs to '<your-dash-enterprise-host>:<your-dash-app>'
        ```


        This error may happen if you are trying to push from a branch
        that is not your `master` branch.

        To resolve get the name of your current
        branch by running `git branch`. Then, to push from this branch
        to the remote server, run `git push plotly your-branch-name:master`.

        This may also occur if you don’t have a `requirements.txt` file.

        The buildpack is the technology Dash Enterprise uses to create a Docker container.

        Dash Enterprise supports three different buildpacks: The standard Python & pip buildpack, a Python & conda buildpack, and a Dash for R buildpack. Dash Enterprise automatically selects the buildpack based off of which files are contained in the project:\

        - `requirements.txt` - If this file exists, then Dash Enterprise uses the Python & pip buildpack.
        - `conda-requirements.txt` - If this file exists, then Dash Enterprises uses the Python & conda buildpack.
        - `.buildpacks` - If this file exists and is equal to `https://github.com/plotly/heroku-buildpack-r#heroku-18`, then Dash Enterprise uses the R buildpack.

        See  <dccLink href="/dash-enterprise/application-structure" children="Application Structure"/>
        page for more details on buildpacks.
        
        
        ---
        '''
    ),

   rc.Markdown(
        '''
        ### remote: unknown shorthand flag: 'e' in -e

        ```
        $ git push plotly master
        [...]
        remote: unknown shorthand flag: 'e' in -e
        remote: See 'docker image build --help'
        ```

        This error can happen if your project contains a `Dockerfile`.
        Dash Enterprise does not support projects that contain a `Dockerfile`.
        To resolve, remove the `Dockerfile` from your project and redeploy.

        > Background

        > Dash Enterprise uses buildpack technology in order to automatically
        > build Docker containers. These buildpacks are detected automatically
        > depending on the files within the project file.

        > Dash Enterprise supports three different buildpacks: The standard Python & pip buildpack, a Python & conda buildpack, and a Dash for R buildpack. Dash Enterprise automatically selects the buildpack based off of which files are contained in the project:\

        > - `requirements.txt` - If this file exists, then Dash Enterprise uses the Python & pip buildpack.
        > - `conda-requirements.txt` - If this file exists, then Dash Enterprises uses the Python & conda buildpack.
        > - `.buildpacks` - If this file exists and is equal to `https://github.com/plotly/heroku-buildpack-r#heroku-18`, then Dash Enterprise uses the R buildpack.

        > If a `Dockerfile` is included, then Dash Enterprise attempts to use
        > an unsupported Docker buildpack.



        ---
        '''
    ),

    rc.Markdown(
        '''
        ### fatal: unable to run gunicorn: file does not exist

        ```shell
        $ git push plotly master
        [...]
        remote: App container failed to start!!
        =====> demo-app web container output:
            setuidgid: fatal: unable to run gunicorn: file does not exist
            setuidgid: fatal: unable to run gunicorn: file does not exist
            setuidgid: fatal: unable to run gunicorn: file does not exist
            setuidgid: fatal: unable to run gunicorn: file does not exist
            setuidgid: fatal: unable to run gunicorn: file does not exist
            setuidgid: fatal: unable to run gunicorn: file does not exist
        =====> end demo-app web container output
        To <your-dash-enterprise-host>:<your-dash-app>
        ! [remote rejected] master -> master (pre-receive hook declined)
        error: failed to push some refs to '<your-dash-enterprise-host>:<your-dash-app>'
        ```


        This happens when `gunicorn` is missing from your app's `requirement.txt` file.

        See  <dccLink href="/dash-enterprise/application-structure" children="Application Structure"/>
        page for more details on `gunicorn` and `requirement.txt`.
       
       
        ---
        '''
    ),

    rc.Markdown(
        '''
        ### syntax error in expression (error token is " ")

        ```shell
        $ git push plotly master
        [...]
        remote: /var/lib/dokku/plugins/enabled/scheduler-docker-local/scheduler-deploy: line 67: [[: web: gunicorn: syntax error in expression (error token is ": gunicorn")
        remote: /var/lib/dokku/plugins/enabled/scheduler-docker-local/scheduler-deploy: line 156: web: gunicorn: syntax error in expression (error token is ": gunicorn")
        To <your-dash-enterprise-host>:<your-dash-app>
        ! [remote rejected] master -> master (pre-receive hook declined)
        error: failed to push some refs to 'dokku@<your-dash-enterprise-host>:<your-dash-app>'
        ```


        This can happen when the entries in your `DOKKU_SCALE` file don't match your `Procfile`.

        See <dccLink href="/dash-enterprise/application-structure" children="Application Structure"/>
        page for more details on `Procfile`.
        
        
        ---
        '''
    ),

    rc.Markdown(
        '''
        ### fatal: unable to access 'https://<your-dash-enterprise-host>/GIT/your-dash-app-name/': SSL certificate problem: self signed certificate

        ```shell
        $ git push plotly master
        [...]
        fatal: unable to access 'https://<your-dash-enterprise-host>/GIT/your-dash-app-name/': SSL certificate problem: self signed certificate
        ```


        This can happen if you are deploying to Dash Enterprise using an https remote while Dash Enterprise is using a self-signed certificate.
        Resolve this by <dccLink href="/dash-enterprise/ssh" children="deploying with SSH"/>.
        Alternatively, you can attempt to follow
        [these 3rd party instructions to make git accept a self-signed certificate](https://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate).\


        ---
        '''
    ),

    rc.Markdown(
        '''
        ### Could not find a version that satisfies the requirement

        ```shell
        $ git push plotly master
        [...]
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
        remote:        No matching distribution found for dash==0.29.1 (from -r /tmp/build/requirements.txt (line 1))```
        ```


        This can happen if there is an error in
        your `requirements.txt` file. To resolve, check the versioning in your
        `requirements.txt` file. For example, the above failed because
        `dash==29.1` isn't a version of dash. If you're working in a virtualenv then
        you can check your version with the command:

        ```
        $ pip list
        ```

        if it differs from your `requirements.txt`, you can update it with the command:

        ```
        pip freeze > requirements.txt
        ```

        See <dccLink href="/dash-enterprise/application-structure" children="Application Structure"/> page for more details on `requirements.txt`.


        ---
        '''
    ),

    rc.Markdown(
        '''
        ### SSH deploy: git push is asking for password

        ```shell
        $ git push plotly master
        dokku@your-dash-server password:
        ```


        This means that the ssh authentication has failed.

        This can be for a variety of
        reasons so it is useful to run git push again with ssh debugging enabled by
        adding `GIT_SSH_COMMAND='ssh -v'` before your `git push` command.

        ```python
        $ GIT_SSH_COMMAND='ssh -v' git push plotly master

        # OpenSSH_7.6p1 Ubuntu-4ubuntu0.1, OpenSSL 1.0.2n  7 Dec 2017
        # debug1: Reading configuration data /home/michael/.ssh/config
        # debug1: /home/michael/.ssh/config line 1: Applying options for dash.local
        # debug1: Reading configuration data /etc/ssh/ssh_config
        # debug1: /etc/ssh/ssh_config line 19: Applying options for *
        debug1: Connecting to dash.local [192.168.233.240] port 3022.
        # debug1: Connection established.
        # [...]
        # [...]
        # debug1: Authentications that can continue: publickey,password
        # debug1: Next authentication method: publickey
        debug1: Offering public key: RSA SHA256:NWVDKQ /home/michael/.ssh/test
        # debug1: Authentications that can continue: publickey,password
        debug1: Offering public key: RSA SHA256:zessB4 /home/michael/.ssh/google_compute_engine
        # debug1: Authentications that can continue: publickey,password
        # debug1: Trying private key: /home/michael/.ssh/id_rsa
        # debug1: Trying private key: /home/michael/.ssh/id_dsa
        # debug1: Trying private key: /home/michael/.ssh/id_ecdsa
        # debug1: Trying private key: /home/michael/.ssh/id_ed25519
        # debug1: Next authentication method: password
        dokku@dash.local's password:
        ```

        Above, you can see the output of the debugging logs where unimportant lines
        have been commented out or omitted. Check the first uncommented out line in the sample
        output above to ensure that the domain is your Dash server's domain and that port is 3022.
        If it isn't, you will need to update your `~/.ssh/config` file to set the
        correct port.

        The next two emphasized lines show the public keys that were offered (and
        in this case rejected) by the server. If the RSA key that you added to
        Dash Enterprise is not among those offered you will need to add it to your `ssh-agent`
        with `ssh-add ~/path/to/your/key`.

        See <dccLink href="/dash-enterprise/ssh" children="SSH"/> page for more details on `ssh-agent`
        and modifying your `~/.ssh/config` file.


        ---
        '''
    ),

    rc.Markdown(
        '''
        ### Got permission denied while trying to connect to the Docker daemon socket

        ```shell
        $ git push plotly master
        [...]
        Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.38/containers/json?all=1&filters=%7B%22label%22%3A%7B%22dokku%22%3Atrue%7D%2C%22status%22%3A%7B%22exited%22%3Atrue%7D%7D: dial unix /var/run/docker.sock: connect: permission denied
        ```


        If you're receiving the above user permission error, please
        <dccLink href="/dash-enterprise/support" children="contact support"/>.
        
        
        ---
        '''
    ),

    rc.Markdown(
        '''
        ### fatal: Authentication failed for 'https://<your-dash-enterprise-host>/GIT/<your-dash-app>/'

        ```shell
        $ git push plotly master
        [...]
        fatal: Authentication failed for 'https://<your-dash-enterprise-host>/GIT/<your-dash-app>/'
        ```


        This can happen when using git to push changes
        to a SAML enabled Dash Enterprise Server with `https`.
        If your Dash Enterprise server is configured to use SAML-based authentication,
        then pushing code with the `https` git remote is not supported.
        Resolve this by <dccLink href="/dash-enterprise/ssh" children="deploying with SSH"/>.
        
        
        ---
        '''
    ),


    rc.Markdown(
        '''
        ### Access denied

        ```shell
        $ git push plotly master
        [...]
        User does not have permissions to run git-receive-pack on <repository>, or <repository> does not exist
        Access denied
        fatal: Could not read from remote repository.

        Please make sure you have the correct access rights
        and the repository exists.
        ```


        This happens when multiple user push changes to the same app.
        Dash Enterprise does not support collaborative deploys or changes being pushed to an app by multiple users.
        You have three options to work deploy apps collaboratively:

        1. Only the app owner and admin users can deploy to the application. If you are given admin rights you will be able to deploy changes to the app as well.
        2. Pushing via [ssh deploy method](https://dash.plotly.com/dash-enterprise/ssh) after adding your ssh key to the app owner's account.For this method to work, you must create a separate ssh key specifically for the other users account. If you upload the same key to two different users, then Dash Enterprise will not know which user is deploying and will complain and say you don't have permission.
        3. Pushing the master branch from the repository with the app owner's credentials after setting up a CI pipeline working in a repository.
        
        
        ---
        '''
    ),

    rc.Markdown(
        '''
        ### remote: Access denied

        ```shell
        $ git push plotly master
        [...]
        Counting objects: 3, done.
        Delta compression using up to 8 threads.
        Compressing objects: 100% (3/3), done.
        Writing objects: 100% (3/3), 5.18 KiB | 2.59 MiB/s, done.
        Total 3 (delta 0), reused 0 (delta 0)

        remote: User <your-user-name> does not have permissions to run git-hook on <your-dash-app>, or <your-dash-app> does not exist
        remote: Access denied
        To <your-dash-enterprise-host>/GIT/<your-dash-app>
        ! [remote rejected] master -> master (pre-receive hook declined)

        error: failed to push some refs to '<your-dash-enterprise-host>:<your-dash-app>'
        ```

        ```shell
        $ git push plotly master
        [...]
        ssh: connect to host <your-dash-enterprise-host> port 22: Connection timed out

        fatal: Could not read from remote repository.

        Please make sure you have the correct access rights

        and the repository exists.
        ```


        If deploying with SSH, then this can happen when your `~/.ssh/config` is improperly configured. See  <dccLink href="/dash-enterprise/ssh" children="SSH"/> page for more details.

        If deploying with HTTPS, then this can happen if your username or password is incorrect. Note that usernames and passwords in Dash Enterprise are case sensitive; e.g. the username `Chris.Parmer` is different than the username `chris.parmer`.

        Git can sometimes cache these usernames after you've typed them. Run `$ git config credential.helper` to verify and correct the username.

        Also, some operating system's password managers can cache usernames as well. Open your operating system's password manager and verify the username & password if you are deploying with `https`, running into access denied errors, and `git` isn't asking you for your username and password.
        
        
        ---
        '''
    ),

    rc.Markdown(
        '''
        ### Please make sure you have the correct access rights and the repository exists

        ```shell
        $ git push plotly master
        [...]
        dokku@<dash-enterprise-server>: Permission denied (publickey).

        fatal: Could not read from remote repository.

        Please make sure you have the correct access rights

        and the repository exists.
        ```


        This can happen when your `~/.ssh/config` is improperly configured.

        See the **Modify SSH Config** section on <dccLink href="/dash-enterprise/ssh" children="SSH"/> page
        for more details. Watch out for trailing slashes in your Dash Enterprise Server domain!
        
        
        ---
        '''
    ),

    rc.Markdown(
        '''
        ### fatal: invalid server response; got 'ed20603d685403ed53ba0017dd8dda3f11407ce6 HEAD'

        ```
        $ git clone https://<dash-enterprise-server/GIT/<dash-app-name>
        Cloning into <dash-app-name>...
        Username for 'https://dash.local':
        Password for 'https://admin@dash.local':

        fatal: invalid server response; got 'ed20603d685403ed53ba0017dd8dda3f11407ce6 HEAD'
        ```


        This error can happen if you are using a version of `git` that
        is incompatible with Dash Enterprise's `git` server.
        In `git` `v2.26`, `git` switched the default transport protocol
        to Version 2. Dash Enterprise's git server runs on `git` 2.17.1
        and it only supports version `0`.

        According to the git documentation,
        the server and client are supposed to be able to negotiate the
        protocol but, for some as of yet unknown reason, this does not work
        when deploying with `https`.

        To fix, manually configure `git` to use the old protocol,
        either in the operation itself:

        ```
        $ git -c protocol.version=0 git clone https://<dash-enterprise-server/GIT/<dash-app-name>
        ```

        or globally:

        ```
        git config --global protocol.version 0
        ```

        **This error can also happen if you forgot to add the ~/.ssh/config entry.** 
        It should resemble:

        ```
        Host <dash-enterprise-server>
            Port 3022
        ```
        
        See the Modify SSH Config section in [SSH Instructions chapter](https://dash.plotly.com/dash-enterprise/ssh)
        for more details.


        ---
        '''
    ),

    rc.Markdown(
        '''
        ### Proc entrypoint worker does not exist. Please check your Procfile

        ```
        $ git push plotly master
        [...]
        =======> <dash-app> worker container output:
        Proc entrypoint worker does not exist. Please check your Procfile
        ```


        This can happen if the directives listed in `DOKKU_SCALE` don't match
        the directives listed in `Procfile`.

        For example:


        `Procfile`
        ```
        web: gunicorn app:server --workers 4
        ```
        `DOKKU_SCALE`
        ```
        web=1
        worker=1
        ```

        In this case, `DOKKU_SCALE` is asking Dash Enterprise to run the "web"
        process and the "worker" process in their own container.
        However, there is no associated command for the "worker" process in the
        `Procfile`.

        To resolve, make sure that the directives (e.g. `web`, `worker`) in the `Procfile` & `DOKKU_SCALE`
        match.

        See <dccLink href="/dash-enterprise/application-structure" children="application structure"/>
        for more details on `Procfile` & `DOKKU_SCALE`.


        ---
        '''
    ),

    rc.Markdown(
        '''
        ## App container failed to start!!

        ```
        $ git push plotly master
        [...]
        remote: -----> Attempting pre-flight checks (web.1)
        remote: App container failed to start!!
        remote: =====> <dash-app-name> web container output:
        remote:        [2020-10-20 12:04:12] [9] [INFO] Starting gunicorn 19.9.0
        [...]
        ```


        This can happen if there is an error when Dash Enterprise attempts to
        run the command listed in the `web` directive in `Procfile`
        (e.g. `gunicorn app:server`). This is usually an error within your
        application code.

        To diagnose, try running the `web` command listed
        in the `Procfile` either locally or within a Dash Enterprise Workspace.

        Also, verify that your development environment matches the production
        environment. Using a Dash Enterprise Workspace is a great way to
        ensure that your environment will match since it has the same build
        process (it will build the packages listed in `requirements.txt`),
        the same network, and the same operating system.


        ---
        '''
    ),

    rc.Markdown(
        '''
        ## gunicorn: error: unrecognized arguments

        ```sh
        $ git push plotly master
        [...]
        remote: App container failed to start!!
        =====> <your-dash-app> web container output:
               usage: gunicorn [OPTIONS] [APP_MODULE]
               gunicorn: error: unrecognized arguments: --timout 2
        [...]
         ! [remote rejected] master -> master (pre-receive hook declined)
        error: failed to push some refs to 'dokku@<your-dash-enterprise-host>:<your-dash-app>'
        ```


        This can happen when you add an invalid `gunicorn` argument to the `web`process in your `Procfile`.

        To resolve, verify the format and spelling of those arguments. See [Gunicorn Docs on Settings](https://docs.gunicorn.org/en/stable/settings.html) for more details.


        ---
        '''
    ),

        rc.Markdown(
        '''
        ## \[CRITICAL\] WORKER TIMEOUT

        ```sh
        [...]
        2020-12-01T07:45:15.008398034Z app[web.1]: [2020-12-01 07:45:15 +0000] [15] [CRITICAL] WORKER TIMEOUT (pid:1040)
        [...]

        ```

        This can happen in the following scenarios:


        * Your app takes longer than 30 seconds to start — 

        In this scenario, the `gunicorn` `web` process does not have enough 
        time to complete its task during the booting process. By default, 
        `gunicorn` has a 30 second timeout. Workers silent for more than this 
        many seconds are killed and restarted. 


        To resolves, we recommend that you first use the `--preload` flag to reduce your 
        application's memory consumption and speed up boot time. Avoid the `--preload` 
        flag if you are using shared database connection pools. See 
        [Gunicorn Docs on Preloading](https://docs.gunicorn.org/en/latest/settings.html#preload-app) 
        for more details. 


        ```
        web: gunicorn app:server --workers 4 --preload
        
        ```
    

        Use the `--timeout` flag only if you cannot use the `--preload` flag. 
        `--timeout` allows you to modify the default amount of time available 
        for your workers to complete  a task. See 
        [Gunicorn Docs on Timeout](https://docs.gunicorn.org/en/stable/settings.html#timeout)
        for details.


        ```
        web: gunicorn app:server --workers 4 --timeout 90

        ```
  

        * Your app's callbacks take more than 30 seconds to finish — 

        To resolve, consider using a background job queue with the Dash 
        Enterprise Snapshot Engine. 

        Alternatively, increase this timeout and ask 
        your server admin to increase the timeout setting in the Dash Enterprise 
        Server Manager. We recommend using a job queue instead of increasing 
        the timeouts because it will make your application more scalable.


        ---
        '''
    ),

    rc.Markdown(
        '''
        ## error processing package ca-certificates

        ```
        rm: cannot remove ‘ca-certicates.crt’: Device or resource busy
        dpkg: error processing package ca-certificates

        ```

        This may occur because Dash Enterprise maps `/etc/ssl/certs` from the host server to 
        Dash apps to make it possible to install APT packages from non-standard APT repositories
        by default. This interfere with installing certain packages. A server configuration 
        option to turn this feature off is available. See APT files section in 
        [Application Structure chapter](/dash-enterprise/application-structure) 
        for more details.

        To resolve, an admin user can login to your-dash-instance:8800/settings, check 
        "Enable Dash Customizations" at the bottom of the page and then check 
        "Indirect Certificate Mapping". They would then save and restart the 
        server to enable the change. That would prevent you from seeing this 
        current error.
    

        ---
        '''
    )



])

# # # # # #
# Portal
# # # # # # #
Portal = html.Div(children=[
    html.H1('Dash App Portal'),

    Blockquote(),

    rc.Markdown('''
    Located at `https://your-dash-enterprise-server/Portal`,
    the Dash App Portal is the front page for your Dash Enterprise platform.
    It allows multiple users to prominently display their selected apps in
    one central location.

    The portal and apps have a default style which can
    be customized.

    &nbsp;
    '''),

    html.Img(
        alt='Default Dash App Portal',
        src=tools.relpath('/assets/images/dds/default-portal.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''

    ### Dash Apps on the Portal

    In order for your app to appear on the Dash App Portal, you need
    enable the *Show in Portal* Toggle in your app's settings from
    within the Dash Enterprise app manager and then edit your app's metadata to
    make it easier to find/customize its appearance.

    > Note that only users with access to your app will be able
    to see it in the portal. For more information about setting app privacy
    see <dccLink href="/dash-enterprise/privacy" children="Dash App Privacy"/>.

    &nbsp;

    '''),

    html.Img(
        alt='Dash App Portal Settings',
        src=tools.relpath('/assets/images/dds/manager-app-settings-portal.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''
    &nbsp;

    ### Customize the Portal

    From the Dash Enterprise app Manager, access the *Portal* tab
    to see its settings (or go to `/Manager/settings/portal/general`).

    &nbsp;
    '''),

    html.Img(
        alt='Customized Portal',
        src=tools.relpath('/assets/images/dds/manager-settings-portal.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''
    &nbsp;

    Here, you can decide who can view the portal and customize
    its appearance.

    &nbsp;
    '''),

    html.Img(
        alt='Customized Portal',
        src=tools.relpath('/assets/images/dds/custom-portal.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),


])


# # # # # #
# Admin Panel
# # # # # # #
AdminPanel = html.Div(children=[
    html.H1('Admin Panel'),

    Blockquote(),

    rc.Markdown('''
    The Admin panel allows Admin users, users with Staff and Superuser Status, to manage all users of the Dash Enterprise platform.
    From here they can add, view, modify, and delete user accounts. The panel can be accessed from the navbar
    dropdown in the /Manager or /Portal pages as shown below.

    &nbsp;
    '''),

    html.Img(
        alt='Dash Enterprise admin panel link',
        src=tools.relpath('/assets/images/dds/dash-enterprise-admin-panel-link.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''

    Only Admin users have access to the admin panel and other users will
    not be able to see the above link.

    ### Users Section

    The users section displays a summary of all the users which includes the number of Dash apps created.

    &nbsp;

    '''),

    html.Img(
        alt='Users summary section',
        src=tools.relpath('/assets/images/dds/admin-users-screen-table.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''
    &nbsp;

    A specific user account can be accessed and modified by clicking on a username. This view
    allows you modify the user's account (e.g. make them an admin, change the email associated
    with the account) or delete it altogether.

    &nbsp;
    '''),

    html.Img(
        alt='Modify user section',
        src=tools.relpath('/assets/images/dds/admin-change-user-section.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''
    &nbsp;

    For more information contact `onpremise.support@plotly.com`.

    &nbsp;
    ''')


])


# # # # # # #
# Analytics
# # # # # # #
Analytics = html.Div(children=[
    html.H1('Dash App Analytics'),

    Blockquote(),

    rc.Markdown('''
    #### Dash App Analytics

    After you have successfully deployed a Dash App to Dash Enterprise,
    you can monitor app performance via the app analytics and logs.
    Here, navigate to the Dash Enterprise UI and select the app to
    display analytics.

    '''),

    html.Img(
        alt='App Analytics',
        src=tools.relpath('/assets/images/dds/analytics.png'),
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

    Blockquote(),

    rc.Markdown('''
    ***

    Dash apps create a log of usage data as well as any `print` statements
    called from your app. These logs can be accessed via the Dash Enterprise UI or from the
    command line. Note that they will be cleared each time you re-deploy
    your app.

    ***

    #### Dash App Logs (via UI)

    If you have successfully deployed a Dash App to the Dash Enterprise,
    you can view the app's logs via the Dash Enterprise UI.
    From your list of apps, open the app and then select **Logs**. This will
    display the most recent 500 log entries for your app. For the complete list,
    use the command line method outlined below.
    '''),

    html.Img(
        alt='App Logs',
        src=tools.relpath('/assets/images/dds/logs.png'),
        style={
            'width': '100%', 'border': 'thin lightgrey solid',
            'border-radius': '4px'
        }
    ),

    rc.Markdown('''
    ***

    #### Dash App Logs (via Command Line)

    Alternatively, the above can be accomplished via the command line.
    To view the logs for a specific Dash App run the following command
    in your terminal:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ ssh dokku@<your-dash-domain> logs <your-app-name> --num -1
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''

    &nbsp;

    This will work for any application that you own. This command
    authenticates with the server with ssh.
    <dccLink href="/dash-enterprise/ssh" children="Configure SSH Authentication"/>.

    &nbsp;

    **Options**
    - `--num`, `-n`: The number of lines to display. By default, 100
    lines are displayed.
       Set to -1 to display _all_ of the logs. Note that we only store logs
       from the latest app deploy.
    - `--tail`, `-t`: Continuously stream the logs.
    - `--quiet`, `-q`: Display the raw logs without colors, times, and names.
    '''),
])


# # # # # # #
# Support
# # # # # # #
Support = html.Div(children=[
    html.H1('Plotly Enterprise Support'),

    Blockquote(),

    rc.Markdown('''
    ***

    #### Need to Contact Support?

    If you encounter any issues deploying your app, you can email
    `onpremise.support@plotly.com`. It is helpful to include any error
    messages you encounter, as well as available logs. See <dccLink href="/dash-enterprise/logs" children="App Logs"/> on how
    to obtain Dash App logs. Additionally, see below for the Plotly Enterprise support
    bundle.
    '''),

    rc.Markdown('''
    ***

    #### Enterprise Support Bundle

    If you're requested to send the full support bundle, you can
    download this from your Plotly Enterprise Server Manager
    (e.g. `https://<your.plotly.domain>:8800`). Please note you
    will need admin permissions to access the Server Manager.
    Navigate to the Server Manager and then select the Support tab.
    There you will see the option to download the support bundle.
    ''')
])

# # # # # # #
# Advanced Git
# # # # # # #
Git = html.Div(children=[
    html.H1('Advanced Git'),

    Blockquote(),

    rc.Markdown('''

    ***

    Plotly uses [Git](https://git-scm.com/) to manage Dash App deployments.
    This section serves as a reference for what git commands are utilized,
    when to use them, and why.

    &nbsp;

    - Initialize a Repository
    - Cloning a Repository
    - Remote Repositories
    - Deploying Changes
    - Using Branches

    ***

    '''),

    rc.Markdown('''

    #### Initialize a Repository

    If you have created a new folder for your Dash App, or have an existing
    folder on your local machine, you need to initialize a local Git
    repository before you can deploy your Dash App to the Dash Enterprise.
    You need to initialize the local Git repository from your app's
    root folder, thus:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ cd myDashApp
    $ git init
    Initialized empty Git repository in .git/
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''
    ***

    #### Cloning a Repository

    If you have an existing repository hosted on Github, or would like to
    utilize one the demo Dash Apps from [Plotly's Gallery](https://dash-gallery.plotly.host/Portal/), then you
    you'll need to clone the repository. You can achieve this by using the
    `git clone` command:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git clone <repository-name>
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''&nbsp;'''),

    rc.Notebox('''

    **Note:** the above command will generate a local Git repository on your
    machine, which by default will include the remote Github repository
    `origin`. If you're concerned that you may accidentally push to this
    repository, you can remove it. See the next section **Remote Repositories**
    for how to view and remove remote repositories.

    '''),

    rc.Markdown('''

    ***

    #### Remote Repositories

    Once you have initialized your local Git repository or cloned an existing
    repository from Github, you need to create a remote repository on the
    Dash Enterprise, which you will deploy your changes to.
    Note that this remote repository will be your live / production Dash App.

    &nbsp;

    To create a remote repository

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git remote add <remote-name> <remote-URL>
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''

    &nbsp;

    To view all remotes:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git remote -v
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''

    &nbsp;

    To rename a remote repository:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git remote rename <existing-name> <new-name>
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''

    &nbsp;

    To remove a remote repository:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git remote rm <remote-name>
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''

    ***

    #### Deploying Changes

    By default, Dash apps run on `localhost` - you can only access them on
    your local machine. To share a Dash app, you need to "deploy" your Dash app
    to the Dash Enterprise platform. This can be achieved via a series of
    commands. Namely,

    - `git status` allows you to view which files have been changed.
    - `git diff` prints out changes within the files.
    - `git add .` will add all your changes.
    - `git commit -m "a description of the changes"` will commit you changes.
    - `git push <repository-name> master` will deploy your code to
    Dash Enterprise.

    &nbsp;

    '''),

    rc.Notebox('''
    `git status` and `git diff` are optional and are only required if you
    wish to inspect before adding changes.
    '''),

    rc.Markdown('''

    &nbsp;

    The demonstration below is a common way to deploy your changes:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git add .
    $ git commit -m "a description of the changes"
    $ git push <repository-name> master
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''

    ***

    #### Using Branches

    If you want to try out a new feature or test something different with your
    Dash App but don't want to alter your `master` code, you can create a
    branch to encapsulate these changes.

    &nbsp;

    To view all branches:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git branch
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''

    &nbsp;

    To create a new branch:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git branch <branchname>
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''

    &nbsp;

    Once you've created a new branch, you need to check it out (i.e. navigate
    to it).

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git checkout <branchname>
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''

    &nbsp;

    If you have created a new branch and are happy with the changes, you can
    add and commit these changes using the common `git add . ` and
    `git commit -m "description"` commands. To deploy these to Dash Enterprise,
    you will need to deploy the branch into master:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git add .
    $ git commit -m "a description of changes"
    $ git push <remote-name> <branchname>:master
    ''',
    style=styles.code_container),

    rc.Markdown('''

    &nbsp;

    To rename a branch:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git branch -m <existing-name> <new-name>
    ```
    ''',
    style=styles.code_container),


    rc.Markdown('''

    &nbsp;

    If you no longer require the branch, you can remove a branch:

    '''),

    rc.Markdown(
    '''
    ```shell
    $ git branch -D <branch-name>
    ```
    ''',
    style=styles.code_container),

    rc.Markdown('''&nbsp;'''),

    rc.Notebox('''

    **Note:** using `-D` will delete the branch and all unmerged changes.

    '''),

    rc.Markdown('''

    ***

    #### Additional Resources

    For more information regarding version control and Git commands, see Git's
    [documentation](https://git-scm.com/).



    ''')
])
