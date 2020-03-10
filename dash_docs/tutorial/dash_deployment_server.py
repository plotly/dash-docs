import dash_html_components as html
import os

from dash_docs import reusable_components


def s(string_block):
    return string_block.replace('    ', '')


layout = html.Div(className='toc', children=[
    html.H1('Dash Enterprise Documentation'),

    reusable_components.Section("What's Dash Enterprise?", [
        reusable_components.Chapter('Learn More About Dash Enterprise',
                'https://plot.ly/get-pricing/',
                """Dash Enterprise is Plotly's commercial offering
                   for managing and improving your Dash apps in your
                   organization. [Learn more](https://plot.ly/dash) or
                   [request a trial](https://plot.ly/get-demo).""")
    ]) if 'DASH_DOCS_URL_PREFIX' not in os.environ else '',

    reusable_components.Section("Deployment", [
        reusable_components.Chapter('Part 1. Initialize Dash Apps on Dash Enterprise',
                '/dash-enterprise/initialize',
                'Initialize an app via Dash Enterprise UI.'),
        reusable_components.Chapter('Part 2. Deploy Dash Apps on Dash Enterprise',
                '/dash-enterprise/deployment',
                'Deploy Dash Apps to the Dash Enterprise using '
                'HTTPS or SSH. Start with a sample app or deploy your existing app.')
    ]),

    reusable_components.Section("Configuration", [
        reusable_components.Chapter('Application Structure',
                '/dash-enterprise/application-structure',
                'Ensure that your app meets all the requirements for deployment.'),
        reusable_components.Chapter('Adding Static Assets',
                '/dash-enterprise/static-assets',
                'Learn how to include custom CSS, JS, and images with the `assets` directory.'),
        reusable_components.Chapter('Configuring System Dependencies',
                '/dash-enterprise/configure-system-dependencies',
                'Install and configure system dependencies such as database drivers or the Java JRE environment.'),
    ]),

reusable_components.Section("User Interface", [
        reusable_components.Chapter('Dash App Portal',
                '/dash-enterprise/portal',
                'Learn about the Dash App Portal.'),
        reusable_components.Chapter('Admin Panel',
                '/dash-enterprise/admin-panel',
                'Manage users in the Admin Panel.'),
        reusable_components.Chapter('Dash App Privacy',
                '/dash-enterprise/privacy',
                'Learn about Dash App privacy and how to manage collaborators.'),
        reusable_components.Chapter('Linking a Redis Database',
                '/dash-enterprise/redis-database',
                'Create and link an in-memory database to your Dash Apps.'),
        reusable_components.Chapter('Setting Environment Variables',
                '/dash-enterprise/environment-variables',
                'Environment variables are commonly used to store secret '
                'variables like database passwords.'),
        reusable_components.Chapter('Mapping Local Directories',
                '/dash-enterprise/map-local-directories',
                'Directory mappings allow you to make directories on the '
                'Dash Enterprise available to your app.')
    ]),

    reusable_components.Section("Advanced", [
        reusable_components.Chapter('Authenticating to Dash Enterprise with SSH',
                '/dash-enterprise/ssh',
                "There are two methods to deploy Dash Apps: HTTPS and SSH. "
                "We recommend getting started with the HTTPS method. "
                "In this section, you'll learn more about deploying with SSH."),
        reusable_components.Chapter('Managing Dash Apps from the Command Line',
                '/dash-enterprise/cli',
                "A list of commands to manage Dash apps and services using"
                " the command line."),
        reusable_components.Chapter('Dash Enterprise Auth Features',
                '/dash-enterprise/app-authentication',
                'Using `dash-enterprise-auth` to manage user authentication data.'),
        reusable_components.Chapter('App Deployment Health Checks',
                '/dash-enterprise/checks',
                'Create custom checks to ensure that a newly deployed app can serve traffic.'),
        reusable_components.Chapter('Adding Private Python Packages',
                '/dash-enterprise/private-packages',
                'Install private python packages in your Dash Apps.'),
        reusable_components.Chapter('Linking a Celery Process',
                '/dash-enterprise/celery-process',
                'Add a task queue to your Dash Apps.'),
        reusable_components.Chapter('Create a Staging Dash App',
                '/dash-enterprise/staging-app',
                'Use a staged Dash App to test changes before updating your '
                'production Dash App.'),
        reusable_components.Chapter('Dash Enterprise PDF Service',
                '/dash-enterprise/pdf-service',
                'Utilize the Dash Enterprise API endpoint for creating '
                'PDF exports of your Dash applications')
    ]),

    reusable_components.Section("Troubleshooting", [
        reusable_components.Chapter('App Analytics',
                '/dash-enterprise/analytics',
                """View app analytics such as last updated, CPU usage, Memory Usage, and more."""),
        reusable_components.Chapter('App Logs',
                '/dash-enterprise/logs',
                """Check your Dash App's logs via the Dash Enterprise
                UI or via the command line."""),
        reusable_components.Chapter('Common Errors',
                '/dash-enterprise/troubleshooting',
                """Common errors when deploying Dash Apps."""),
        reusable_components.Chapter('Support',
                '/dash-enterprise/support',
                """Having trouble deploying your app? Our dedicated support team is available to help you out.""")
    ]),

    reusable_components.Section("Reference", [
        reusable_components.Chapter('Advanced Git',
                '/dash-enterprise/git',
                'A reference for git commands and how they are used '
                'with Dash Enterprise.'),
        reusable_components.Chapter('Dash Enterprise API',
                'https://github.com/plotly/dds-api-docs',
                'Reference documentation for Dash Enterprise\'s GraphQL API. '
                'Use this to programmatically add collaborators, '
                'initialize dash apps and more.')
    ])
])
