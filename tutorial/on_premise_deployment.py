from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import styles
from server import app


def s(string_block):
    return string_block.replace('    ', '')


STEPS = [
    {'label': 'Part 1 - Authenticating to Plotly On-Premise with SSH',
     'value': 'ssh'},

    {'label': 'Part 2 - Initializing App on Plotly On-Premise',
     'value': 'create-app'},

    {'label': 'Part 3 - Deploying App to Plotly On-Premise',
     'value': 'deployment'},

    {'label': 'Part 4 - Adding Authentication to your Dash App (Optional)',
     'value': 'auth'},

    {'label': 'Part 5 - Troubleshooting App Deployment',
     'value': 'troubleshooting'},

]


def generate_instructions(chapter, platform):
    if chapter == 'ssh':
        return [
            dcc.Markdown(s('''
                You will deploy your Dash code to Plotly On-Premise using Git
                with SSH.
            ''')),

            (dcc.Markdown(s('''
                These instructions assume that you are using
                **Git Bash** on Windows, which is included in the
                official [Git for Windows release](https://git-scm.com/download/win).
            ''')) if platform == 'Windows' else
            ''),

            dcc.Markdown(s('''

                ***

                ### Generate a new SSH key

                If you already have an SSH key that you've used in other
                services, you can use that key instead of generating a new one.

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

                ### Add your SSH key to the ssh-agent

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
                 '$ ssh-add -K ~/.ssh/id_rsa'),
                customStyle=styles.code_container,
                language='python'
            ),

            dcc.Markdown(s('''
                ***

                ### Add your SSH public key your Dash App Manager
            ''')),

            dcc.Markdown(s('''
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
                **2. Open the Dash App Manager**

                You can find the Dash App Manager by clicking on "Dash App" in your
                Plotly On-Premise's "Create" menu.

                > *The Dash App item in the Create menu takes you to the Dash App Manager*
            ''')),

            html.Img(
                alt='Dash App Create Menu',
                src='https://github.com/plotly/dash-docs/raw/master/images/dash-create-menu.png',
                style={
                    'width': '100%', 'border': 'thin lightgrey solid',
                    'border-radius': '4px'
                }
            ),

            dcc.Markdown(s('''
                **3. Paste your key into the Dash App Manager's SSH key field.**
            ''')),

            dcc.Markdown(s('''
                > *The Dash App Manager's SSH Key Interface. Copy and paste
                > your public key in this interface and click "Update".*
            ''')),

            html.Img(
                alt='Dash App Manager Public Key Interface',
                src='https://github.com/plotly/dash-docs/raw/master/images/dash-app-manager-ssh-key.png',
                style={
                    'width': '100%', 'border': 'thin lightgrey solid',
                    'border-radius': '4px'
                }
            ),

            dcc.Markdown(s('''
                ***

                ### Modify SSH Config
                Next, specify a custom port in your SSH config. By default, this should be
                `3022` but your server administrator may have set it to something different.

                This file is located in `~/.ssh/config`. If it's not there, then create it.
                Add the following lines to
                this file, replacing `your-dash-app-manager` with the domain of
                your Dash App Manager (without `http://` or `https://`).
            ''')),

            dcc.SyntaxHighlighter('''Host your-dash-app-manager
    Port 3022''', customStyle=styles.code_container),

            (dcc.Markdown('''If you're having trouble opening this file, you can run `$ open ~/.ssh/config`
            which will open the file using your default editor. If the file doesn't exist,
            then you can open that hidden folder with just `$ open ~/.ssh`''')
            if platform == 'Mac' else ''),

            dcc.Markdown(s('''
                ***

                Next, proceed to Part 2 to intialize your app on Plotly On-Premise.

            '''))
        ]
    elif chapter == 'create-app':
        return [
            dcc.Markdown(s('''

                **1. Visit the Dash App Manager**

                **2. Add an app**

                Click on `Add an app` and enter a name for your app.
                The app's name will be part of the URL of your app.
            ''')),

            html.Img(
                alt='Dash App Manager Add App Interface',
                src='https://github.com/plotly/dash-docs/raw/master/images/dash-app-manager-empty.png',
                style={
                    'width': '100%', 'border': 'thin lightgrey solid',
                    'border-radius': '4px'
                }
            ),

            dcc.Markdown(s('''
                ***

                Next, proceed to Part 3 to deploy your app

            '''))

        ]

    elif chapter == 'deployment':
        return [
            dcc.Markdown(s('''

                #### Download the Sample App from GitHub

                Clone the [Dash On Premise Sample App](https://github.com/plotly/dash-on-premise-sample-app) from GitHub.

            ''')),

            ('In Git Bash, run: ' if platform == 'Windows' else ''),

            dcc.SyntaxHighlighter(s('''
                $ git clone https://github.com/plotly/dash-on-premise-sample-app.git
                '''),
                customStyle=styles.code_container
            ),

            dcc.Markdown(s('''

                ***

                #### Configure your Plotly On-Premise server to be your Git remote

                The following command will create a remote host to your new app on
                Plotly On-Premise.
            ''')),

            dcc.SyntaxHighlighter(s('''$ cd dash-on-premise-sample-app
                $ git remote add plotly dokku@your-dash-app-manager:your-dash-app-name'''),
                customStyle=styles.code_container,
                language='python'
            ),

            dcc.Markdown(s('''
                Replace `your-dash-app-name` with the name of your Dash app that you supplied
                in the Dash app manager and `your-dash-app-manager` with the domain of the
                Dash App Manager.

                For example, if your Dash app name was `my-first-dash-app`
                and the domain of your organizations Dash App Manager was `dash.plotly.acme-corporation.com`,
                then this command would be
                `git remote add plotly dokku@dash.plotly.acme-corporation.com:my-first-dash-app`.

            ''')),

            dcc.Markdown(s('''***

                #### Modify `config.py`

                Read through `config.py` and modify the values as necessary.
                If Dash On-Premise was set up with "path-based routing"
                (the default), then you will just need to change the
                `DASH_APP_NAME` to be equal to the name of the Dash app that you
                set earlier.
            ''')),

            dcc.Markdown(s('''
                ***

                #### Deploying Changes

                After you have modified `config.py`, you are ready to upload
                this folder to your Dash On-Premise server.
                Files are transferred to the server using `git`:
            ''')),

            dcc.SyntaxHighlighter(s('''$ git status # view the changed files
                $ git diff # view the actual changed lines of code
                $ git add .  # add all the changes
                $ git commit -m 'a description of the changes'
                $ git push plotly master
                '''), customStyle=styles.code_container, language='python'),

            dcc.Markdown(s('''
                This commands will push the code in this folder to the
                Dash On-Premise server and while doing so, will install the
                necessary python packages and run your application
                automatically.

                Whenever you make changes to your Dash code,
                you will need to run those `git` commands above.

                If you install any other Python packages, add those packages to
                the `requirements.txt` file. Packages that are included in this
                file will be installed automatically by the Plotly On-Premise
                server.

                You can now modify `app.py` with your own custom Dash
                application code.
            '''))
        ]
    elif chapter == 'auth':
        return [
            dcc.Markdown(s('''
            The `dash-auth` package provides login through your Plotly
            On-Premise accounts.

            #### Modify the `config.py` file

            This file contains several settings that are used in your app.
            It's kept in a separate file so that it's easy for you to
            transfer from app to app.
            *Read through this file and modify the variables as appropriate.*

            ''')),

            dcc.Markdown(s('''
            #### Redeploy your app

            Your app should now have a Plotly On-Premise login screen.
            You can manage the permissions of the app in your list of files
            at `https://<your-plotly-domain>/organize`.
            '''))
        ]
    elif chapter == 'troubleshooting':
        return [
            dcc.Markdown(s('''
            If you encounter any issues deploying your app you can email
            `onpremise.support@plot.ly`. It is helpful to include any error
            messages you encounter as well as available logs. See below on how
            to obtain Dash app logs as well as the Plotly On-Premise support
            bundle.

            #### Dash App Logs

            To view the logs for a specific Dash app run the following command
            in your terminal:

            `ssh dokku@<your-dash-domain> logs <your-app-name>`

            This will work for any app you have permission on, and uses the
            same mechanism as pushing the app via ssh.
            Please note, to continually stream the logs you can add the `-t`
            flag:

            `ssh dokku@<your-dash-domain> logs <your-app-name> -t`

            ''')),

            dcc.Markdown(s('''
            #### Onpremise Support Bundle

            If you're requested to send the full support bundle you can
            download this from your Plotly On-Premise Server Manager
            (e.g. `https://<your.plotly.domain>:8800`). Please note you
            will need admin permissions to access the Server Manager.
            Navigate to the Server Manager and then select the Support tab.
            There you will see the option to download the support bundle.
            '''))
        ]

layout = html.Div([
    dcc.Markdown(s('''
        # Deploying Dash Apps on Plotly On-Premise

        By default, Dash apps run on `localhost` - you can only access them on your
        own machine. With Plotly On-Premise, you can easily deploy your Dash code
        to your organization's behind-the-firewall server.
        If you would like to learn more about Plotly On-Premise or start a trial,
        [please reach out](https://plotly.typeform.com/to/seG7Vb).
    ''')),

    html.Hr(),

    dcc.RadioItems(
        id='step',
        options=STEPS,
        value='ssh'
    ),

    html.Hr(),

    html.H2(id='header'),

    dcc.RadioItems(
        id='platform',
        options=[
            {'label': i, 'value': i} for i in
            ['Windows', 'Mac', 'Linux']],
        value='Windows',
        labelStyle={'display': 'inline-block'}
    ),

    html.Hr(),

    html.Div(id='deployment-instructions')
])


@app.callback(Output('header', 'children'),
              [Input('step', 'value')])
def display_header(value):
    return [i['label'] for i in STEPS if i['value'] == value][0]


@app.callback(Output('deployment-instructions', 'children'),
              [Input('step', 'value'),
               Input('platform', 'value')])
def display_instructions(chapter, platform):
    return generate_instructions(chapter, platform)
