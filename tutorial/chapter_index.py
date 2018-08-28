import auth
import core_component_examples as examples
import core_components
import dash_deployment_server
import dash_deployment_server_examples as dds_examples
import deployment
import external_css_and_js
import gallery
import getting_started_part_1
import getting_started_part_2
import graphing
import html_components
import installation
import introduction
import live_updates
import on_premise_deployment
import performance
import plugins
import search
import sharing_state
import state
import support
import urls

## The chapters dict is used to generate the dash-docs search index
## If edited, update the search index by running `python dash_search_index.py`
## in the root of this repo.

chapters = {
    ### home.py ###
    'introduction': {
        'url': '/introduction',
        'content': introduction.layout,
        'name':'Introduction',
        'description': 'Dash is a productive Python framework for ' \
                       'building web applications written on top of ' \
                       'Flask, Plotly.js, and React.js.'
    },

    'gallery': {
        'url': '/gallery',
        'content': gallery.layout,
        'name': 'Dash App Gallery',
        'description': 'Examples of Dash apps including ' \
                       'drill down, stock tickers, streaming, ' \
                       'and PDF generation.'
    },

    'installation': {
        'url': '/installation',
        'content': installation.layout,
        'name': 'Part 1. Installation',
        'description': 'How to install and upgrade dash libraries with pip.'
    },

    'getting-started': {
        'url': '/getting-started',
        'content': getting_started_part_1.layout,
        'name': 'Part 2. The Dash Layout',
        'description': 'The Dash `layout` describes what your app will ' \
                       'look like and is composed of a set of declarative ' \
                       'Dash components.'
    },

    'getting-started-part-2': {
        'url': '/getting-started-part-2',
        'content': getting_started_part_2.layout,
        'name': 'Part 3. Basic Callbacks',
        'description': "Dash apps are made interactive through Dash " \
                       "Callbacks: Python functions that are " \
                       "automatically called whenever an input " \
                       "component's property changes. Callbacks " \
                       "can be chained, allowing one update in the " \
                       "UI to trigger several updates across the app."
    },

    'state': {
        'url': '/state',
        'content': state.layout,
        'name': 'Part 4. Callbacks With State',
        'description': 'Basic callbacks are fired whenever the values ' \
                       'change. Use Dash `State` with Dash `Inputs` to ' \
                       'pass in extra values whenever the `Inputs` ' \
                       'change. `State` is useful for UIs that contain ' \
                       'forms or buttons.'
    },

    'graphing': {
        'url': '/interactive-graphing',
        'content': graphing.layout,
        'name': 'Part 5. Interactive Graphing and Crossfiltering',
        'description': 'Bind interactivity to the Dash `Graph` ' \
                       'component whenever you hover, click, or ' \
                       'select points on your chart.'
    },

    'shared-state': {
        'url': '/sharing-data-between-callbacks',
        'content': sharing_state.layout,
        'name': 'Part 6. Sharing Data Between Callbacks',
        'description': '`global` variables will break your Dash apps. ' \
                       'However, there are other ways to share data ' \
                       'between callbacks. This chapter is useful for ' \
                       'callbacks that run expensive data processing ' \
                       'tasks or process large data.'
    },

    'dash-core-components': {
        'url': '/dash-core-components',
        'content': core_components.layout,
        'name': 'Dash Core Components',
        'description': 'The Dash Core Component library contains a set ' \
                       'of higher-level components like sliders, graphs, ' \
                       'dropdowns, tables, and more.'
    },

    'dash-html-components': {
        'url': '/dash-html-components',
        'content': [
            html_components.layout,
            # html_component_appendix.layout,
        ],
        'name': 'Dash HTML Components',
        'description': 'Dash provides all of the available HTML tags ' \
                       'as user-friendly Python classes. This chapter ' \
                       'explains how this works and the few important ' \
                       'key differences between Dash HTML components ' \
                       'and standard html.'
    },

    'plugins': {
        'url': '/plugins',
        'content': plugins.layout,
        'name': 'Build Your Own Components',
        'description': 'Dash components are built with ' \
                       '[React.js](https://reactjs.org/). Dash provides ' \
                       'a React &rarr; Dash toolchain that generates a Dash-' \
                       'compatible interface to these components in Python.'
    },

    'performance': {
        'url': '/performance',
        'content': performance.layout,
        'name': 'Performance',
        'description': 'There are two main ways to speed up dash apps: '\
                       'caching and using WebGL chart types.'
    },

    'live-updates': {
        'url': '/live-updates',
        'content': live_updates.layout,
        'name': 'Live Updates',
        'description': 'Update your apps on page load or on a predefined ' \
                       'interval (e.g. every 30 seconds).'
    },

    'external': {
        'url': '/external-resources',
        'content': external_css_and_js.layout,
        'name': 'Adding CSS & JS and Overriding the Page-Load Template',
        'description': '''
            New in dash v0.22.0! Learn how to add custom CSS and JS to your
            application with the `assets` directory. Also, learn how to
            customize the HTML template that Dash serves on page load in order
            to add custom meta tags, customize the page's title, and more.
        '''
    },

    'urls': {
        'url': '/urls',
        'content': urls.layout,
        'name': 'URL Routing and Multiple Apps',
        'description': 'Dash provides two components (`dcc.Link` and ' \
                       '`dcc.Location`) that allow you to easily make ' \
                       'fast multipage apps using its own "Single Page ' \
                       'App (SPA)" design pattern.'
    },

    'auth': {
        'url': '/authentication',
        'content': auth.layout,
        'name': 'Authentication',
        'description': 'Authentication for dash apps is provided through a ' \
                       'separate dash-auth package. `dash-auth` provides ' \
                       'two methods of authentication: HTTP Basic Auth and ' \
                       'Plotly OAuth.'
    },

    'deployment': {
        'url': '/deployment',
        'content': deployment.layout,
        'name': 'Deployment',
        'description': 'To share a Dash app, you need to "deploy" your Dash ' \
                       'app to a server'
    },

    # 'deployment-onpremise': {
    #     'url': '/deployment/on-premise',
    #     'content': on_premise_deployment.layout,
    #     'name': 'Deploying Dash Apps on Plotly Enterprise',
    #     'description': "Plotly Enterprise is Plotly's commercial " \
    #                    "offering for hosting and sharing Dash apps."
    # },

    'dash-deployment-server': {
        'url': '/dash-deployment-server',
        'content': dash_deployment_server.layout,
        'name': 'Dash Deployment Server Documentation',
        'description': "Dash Deployment Server is Plotly's commercial " \
                       "offering for hosting and sharing Dash Apps with " \
                       "Plotly Enterprise."
    },

    'support': {
        'url': '/support',
        'content': support.layout,
        'name': 'Support and Contact',
        'description': 'More information for Dash demos, Enterprise trials, ' \
                       'Dash workshops, sponsored feature requests and ' \
                       'customizations.'
    },
### End of home.py ###

### Start Components ###
    'dropdown-examples': {
        'url': '/dash-core-components/dropdown',
        'content': examples.Dropdown,
        'name': 'Dropdowns',
        'description': 'Dropdown examples, properties, and reference.'
    },

    'slider-examples': {
        'url': '/dash-core-components/slider',
        'content': examples.Slider,
        'name': 'Sliders Component',
        'description': 'Slider examples, properties, and reference.'
    },

    'range-slider-examples': {
        'url': '/dash-core-components/rangeslider',
        'content': examples.RangeSlider,
        'name': 'Range Slider Component',
        'description': 'Range slider examples, properties, and reference.'
    },

    'checklist-examples': {
        'url': '/dash-core-components/checklist',
        'content': examples.Checklist,
        'name': 'Checklist Component',
        'description': 'Checklist examples, properties, and reference.'
    },

    'input-examples': {
        'url': '/dash-core-components/input',
        'content': examples.Input,
        'name': 'Input Component',
        'description': 'Input properties and reference.'
    },

    'radio-item-examples': {
        'url': '/dash-core-components/radioitems',
        'content': examples.RadioItems,
        'name': 'Radio Item Component',
        'description': 'Radio item examples, properties, and reference.'
    },

    'datepickersingle-examples': {
        'url': '/dash-core-components/datepickersingle',
        'content': examples.DatePickerSingle,
        'name': 'Date Picker: Single Component',
        'description': 'Single date picker examples, properties, and reference.'
    },

    'datepickerrange-examples': {
        'url': '/dash-core-components/datepickerrange',
        'content': examples.DatePickerRange,
        'name': 'Date Picker: Range Component',
        'description': 'Date range picker examples, properties, and reference.'
    },

    'markdown-examples': {
        'url': '/dash-core-components/markdown',
        'content': examples.Markdown,
        'name': 'Markdown Component',
        'description': 'Markdown examples, properties, and reference.'
    },

    'link-examples': {
        'url': '/dash-core-components/link',
        'content': examples.Link,
        'name': 'Link Component',
        'description': 'Link examples, properties, and reference.'
    },

    'tabs-example': {
        'url': '/dash-core-components/tabs',
        'content': examples.Tabs,
        'name': 'Tabs & Tab Component',
        'description': 'Tabs examples, properties, and reference.'
    },

    'textarea-examples': {
        'url': '/dash-core-components/textarea',
        'content': examples.Textarea,
        'name': 'Text Area Component',
        'description': 'Text area properties and reference.'
    },

    'upload-examples': {
        'url': '/dash-core-components/upload',
        'content': examples.Upload,
        'name': 'Upload Component',
        'description': 'Upload examples, properties, and reference.'
    },
### End Components ###

### Start Dash Deployment Server ###
    'ssh-examples': {
        'url': '/dash-deployment-server/ssh',
        'content': dds_examples.Ssh,
        'name': 'Authenticating to Dash Deployment Server with SSH',
        'description': "There are two methods to deploy Dash Apps: HTTPS and SSH "
        "and we recommend getting started with the HTTPS method."
    },

    'initialize-examples': {
        'url': '/dash-deployment-server/initialize',
        'content': dds_examples.Initialize,
        'name': 'Part 1. Initialize Dash Apps on Dash Deployment Server',
        'description': 'Initialize Dash Apps on Plotly Enterprise'
    },

    'requirements-examples': {
        'url': '/dash-deployment-server/application-structure',
        'content': dds_examples.Requirements,
        'name': 'Application Structure',
        'description': 'Ensure that your app meets all the requirements for deployment.'
    },

    'create-deploy-examples': {
        'url': '/dash-deployment-server/deployment',
        'content': dds_examples.Deploy,
        'name': 'Part 2. Deploy Dash Apps on Dash Deployment Server',
        'description': 'Deploy Dash Apps on Dash Deployment Server'
    },

    'app-auth-examples': {
        'url': '/dash-deployment-server/app-authentication',
        'content': dds_examples.Authentication,
        'name': 'Dash App Authentication',
        'description': 'Adding Authentication to your Dash App'
    },

    'config-sys-examples': {
        'url': '/dash-deployment-server/configure-system-dependencies',
        'content': dds_examples.ConfigSys,
        'name': 'Configuring System Dependencie',
        'description': 'Install and configure system dependencies such '
        'as database drivers or the Java JRE environment.'
    },

    'redis-examples': {
        'url': '/dash-deployment-server/redis-database',
        'content': dds_examples.Redis,
        'name': 'Linking a Redis Database',
        'description': 'Create and link an in-memory database to your Dash Apps.'
    },

    'celery-examples': {
        'url': '/dash-deployment-server/celery-process',
        'content': dds_examples.Celery,
        'name': 'Linking a Celery Process',
        'description': 'Add a task queue to your Dash Apps.'
    },

    'env-var-examples': {
        'url': '/dash-deployment-server/enviornment-variables',
        'content': dds_examples.EnvVars,
        'name': 'Setting Enviornment Variables',
        'description': 'Environment variables are commonly used to store '
        'secret variables like database passwords.'
    },

    'local-dir-examples': {
        'url': '/dash-deployment-server/map-local-directories',
        'content': dds_examples.LocalDir,
        'name': 'Mapping Local Directories',
        'description': 'Directory mappings allow you to make directories '
        'on the Dash Deployment Server available to your app.'
    },

    'stage-examples': {
        'url': '/dash-deployment-server/staging-app',
        'content': dds_examples.StagingApp,
        'name': 'Create a Staging Dash App ',
        'description': 'Use a staged Dash App to test changes before updating '
        'your prodcution Dash App.'
    },

    'troubleshooting-examples': {
        'url': '/dash-deployment-server/troubleshooting',
        'content': dds_examples.Troubleshooting,
        'name': 'Common Errors',
        'description': 'Common errors when deploying Dash Apps.'
    },

    'analytics-examples': {
        'url': '/dash-deployment-server/analytics',
        'content': dds_examples.Analytics,
        'name': 'App Analytics',
        'description': 'View app analytics such as last updated, '
        'CPU usage, Memory Usage, and more.'
    },

    'logs-examples': {
        'url': '/dash-deployment-server/logs',
        'content': dds_examples.Logs,
        'name': 'App Logs',
        'description': """Check your Dash App's logs via the Dash
        Deployment Server UI or via the command line."""
    },

    'support-examples': {
        'url': '/dash-deployment-server/support',
        'content': dds_examples.Support,
        'name': 'Support',
        'description': 'Having trouble deploying your app? Our dedicated '
        'support team is available to help you out.'
    },
### End Dash Deployment Server ###

    'search': {
        'url': '/search',
        'content': search.layout,
        'name': '',
        'description': 'Search the Dash Docs'
    },

    'confirm-examples': {
        'url': '/dash-core-components/confirm',
        'content': examples.ConfirmDialog,
        'name': 'ConfirmDialog Component',
        'description': 'ConfirmDialog examples, properties, and reference'
    },

    'confirm-provider-examples': {
        'url': '/dash-core-components/confirm-provider',
        'content': examples.ConfirmDialogProvider,
        'name': 'ConfirmDialogProvider Component',
        'description': 'ConfirmDialogProvider examples, properties and reference'
    }
}
