import dash_html_components as html
import dash_core_components as dcc

import reusable_components

def s(string_block):
    return string_block.replace('    ', '')

layout = html.Div(className='toc', children=[
    html.H1('Dash Deployment Server Documentation'),

    reusable_components.Section("What's Dash Deployment Server?", [
        reusable_components.Chapter('Learn More About Dash Deployment Server',
                'https://plot.ly/dash/pricing/',
                """Dash Deployment Server is Plotly's commercial offering
                   for hosting and sharing Dash Apps on-premises or in the
                   cloud. [Learn more](https://plot.ly/dash/pricing) or
                   [request a trial](https://plotly.typeform.com/to/rkO85m).""")
    ]),

    reusable_components.Section("Deployment", [
        reusable_components.Chapter('Part 1. Initialize Dash Apps on Dash Deployment Server',
                '/dash-deployment-server/initialize',
                'Initialize an app via Dash Deployment Server UI.'),
        reusable_components.Chapter('Part 2. Deploy Dash Apps on Dash Deployment Server',
                '/dash-deployment-server/deployment',
                'Deploy Dash Apps to the Dash Deployment Server using '
                'HTTPS or SSH. Start with a sample app or deploy your existing app.')
    ]),

    reusable_components.Section("Configuration", [
        reusable_components.Chapter('Application Structure',
                '/dash-deployment-server/application-structure',
                'Ensure that your app meets all the requirements for deployment.'),
        reusable_components.Chapter('Configuring System Dependencies',
                '/dash-deployment-server/configure-system-dependencies',
                'Install and configure system dependencies such as database drivers or the Java JRE environment.'),
        reusable_components.Chapter('Setting Enviornment Variables',
                '/dash-deployment-server/enviornment-variables',
                'Environment variables are commonly used to store secret '
                'variables like database passwords.'),
        reusable_components.Chapter('Mapping Local Directories',
                '/dash-deployment-server/map-local-directories',
                'Directory mappings allow you to make directories on the '
                'Dash Deployment Server available to your app.')
    ]),

    reusable_components.Section("Advanced", [
        reusable_components.Chapter('Authenticating to Dash Deployment Server with SSH',
                '/dash-deployment-server/ssh',
                "There are two methods to deploy Dash Apps: HTTPS and SSH "
                "and we recommend getting started with the HTTPS method. "
                "In this section, you'll learn more about deploying with SSH."),
        reusable_components.Chapter('Dash App Authentication',
                '/dash-deployment-server/app-authentication',
                'Using `dash-auth` package to provide login through '
                'Plotly Enterprise.'),
        reusable_components.Chapter('Linking a Redis Database',
                '/dash-deployment-server/redis-database',
                'Create and link an in-memory database to your Dash Apps.'),
        reusable_components.Chapter('Linking a Celery Process',
                '/dash-deployment-server/celery-process',
                'Add a task queue to your Dash Apps.'),
        reusable_components.Chapter('Create a Staging Dash App',
                '/dash-deployment-server/staging-app',
                'Use a staged Dash App to test changes before updating your '
                'prodcution Dash App.')
    ]),

    reusable_components.Section("Troubleshooting", [
        reusable_components.Chapter('App Analytics',
                '/dash-deployment-server/analytics',
                """View app analytics such as last updated, CPU usage, Memory Usage, and more."""),
        reusable_components.Chapter('App Logs',
                '/dash-deployment-server/logs',
                """Check your Dash App's logs via the Dash Deployment Server
                UI or via the command line."""),
        reusable_components.Chapter('Common Errors',
                '/dash-deployment-server/troubleshooting',
                """Common errors when deploying Dash Apps."""),
        reusable_components.Chapter('Support',
                '/dash-deployment-server/support',
                """Having trouble deploying your app? Our dedicated support team is available to help you out.""")
    ])
])
