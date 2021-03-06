# -*- coding: utf-8 -*-
import os
from .import chapters
import json
import plotly
import six
import textwrap
import traceback
import os

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import dash_daq
import dash_cytoscape
import dash_bio

from dash_docs import reusable_components as rc, tools
from .reusable_components import TOC, TOCChapters
from .convert_to_html import convert_to_html

## The chapters dict is used to generate the dash-docs search index
## If edited, update the search index by running `python dash_search_index.py`
## in the root of this repo.


def component_list(
        package, content_module, base_url, import_alias,
        component_library, escape_tags=False,
        ad='dash-club.png',
        adhref='https://go.plotly.com/dash-club/?utm_source=docs&utm_medium=sidebar&utm_campaign=nov&utm_content=dash-club'):
    return [
        {
            'url': tools.relpath('/{}/{}'.format(base_url, component.lower())),
            'name': '{}.{}'.format(import_alias, component),
            'description': ' '.join([
                'Official examples and reference documentation for {name}.',
                '{which_library}'
            ]).format(
                name='{}.{}'.format(import_alias, component),
                component_library=component_library,
                which_library=(
                    '{name} is a {component_library} component.'.format(
                        name='{}.{}'.format(import_alias, component),
                        component_library=component_library,
                    ) if component_library != import_alias else ''
                )
            ).strip(),
            'content': (
                getattr(content_module, component)
                if (content_module is not None and
                    hasattr(content_module, component))
                else html.Div([
                    html.H1(html.Code('{}.{}'.format(
                        import_alias,
                        component
                    ))),
                    html.H2('Reference & Documentation'),
                    rc.Markdown(
                        getattr(package, component).__doc__,
                        escape_tags=escape_tags
                    ),
                ])
            ),
            'ad': ad,
            'adhref': adhref
        } for component in sorted(dir(package))
        if not component.startswith('_') and
        component[0].upper() == component[0]
    ]

APP_MANAGER_URLS = [
    {
        'name': 'App Manager Overview',
        'breadcrumb': 'Dash Enterprise',
        'url': '/dash-enterprise',
        'content': chapters.dash_enterprise.index.layout
    },
    {
        'url': '/dash-enterprise/initialize',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Initialize,
        'name': 'Part 1. Initialize Dash Apps on Dash Enterprise',
        'description': 'Initialize Dash Apps on Plotly Enterprise'
    },
    {
        'url': '/dash-enterprise/deployment',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Deploy,
        'name': 'Part 2. Deploy Dash Apps on Dash Enterprise',
        'description': 'Deploy Dash Apps on Dash Enterprise'
    },
    {
        'url': '/dash-enterprise/application-structure',
        'content': chapters.dash_enterprise.application_structure.index.layout,
        'name': 'Application Structure, Buildpacks, and Deployment Lifecycle',
        'description': 'Ensure that your app meets all the requirements for deployment.'
    },
    {
        'url': '/dash-enterprise/static-assets',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.staticAssets,
        'name': 'Adding Static Assets',
        'description': 'Learn how to include custom CSS, JS, and images with the `assets` directory.'
    },
    {
        'url': '/dash-enterprise/configure-system-dependencies',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.ConfigSys,
        'name': 'Configuring System Dependencies',
        'description': 'Install and configure system dependencies such '
        'as database drivers or the Java JRE environment.'
    },
    {
        'url': '/dash-enterprise/portal',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Portal,
        'name': 'Dash App Portal',
        'description': 'Learn about the Dash App Portal '
    },
    {
        'url': '/dash-enterprise/admin-panel',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.AdminPanel,
        'name': 'Admin Panel',
        'description': 'Manage users in the Admin Panel '
    },
    {
        'url': '/dash-enterprise/redis-database',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Redis,
        'name': 'Linking a Redis Database',
        'description': 'Create and link an in-memory database to your Dash Apps.'
    },
    {
        'url': '/dash-enterprise/environment-variables',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.EnvVars,
        'name': 'Setting Environment Variables',
        'description': 'Environment variables are commonly used to store '
        'secret variables like database passwords.'
    },
    {
        'url': '/dash-enterprise/map-local-directories',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.LocalDir,
        'name': 'Mapping Local Directories',
        'description': 'Directory mappings allow you to make directories '
        'on the Dash Enterprise available to your app.'
    },
    {
        'url': '/dash-enterprise/ssh',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Ssh,
        'name': 'Authenticating to Dash Enterprise with SSH',
        'description': "There are two methods to deploy Dash Apps: HTTPS and SSH "
        "and we recommend getting started with the HTTPS method."
    },
    {
        'url': '/dash-enterprise/cli',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Cli,
        'name': 'Managing Dash Apps via the Command Line',
        'description': "A list of commands to manage Dash apps available  "
        "to app owners from the command line via ssh."
    },
    {
        'url': '/dash-enterprise/private-packages',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.PrivatePackages,
        'name': 'Adding Private Python Packages',
        'description': 'Install private python packages in your Dash Apps.'
    },
    {
        'url': '/dash-enterprise/celery-process',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Celery,
        'name': 'Linking a Celery Process',
        'description': 'Add a task queue to your Dash Apps.'
    },
    {
        'url': '/dash-enterprise/staging-app',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.StagingApp,
        'name': 'Create a Staging Dash App ',
        'description': 'Use a staged Dash App to test changes before updating '
        'your production Dash App.'
    },
    {
        'url': '/dash-enterprise/database-connections',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.DataConnections,
        'name': 'Connect a Dash App to an SQL Database',
        'description': 'Learn how to manage external database connections, perform '
        'queries with Dash callbacks, and maintain SQL best practices.'
    },
    {
        'url': '/dash-enterprise/analytics',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Analytics,
        'name': 'App Analytics',
        'description': 'View app analytics such as last updated, '
        'CPU usage, Memory Usage, and more.'
    },
    {
        'url': '/dash-enterprise/logs',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Logs,
        'name': 'App Logs',
        'description': '''Check your Dash App's logs via the Dash
        Enterprise UI or via the command line.'''
    },
    {
        'url': '/dash-enterprise/troubleshooting',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Troubleshooting,
        'name': 'Common Errors',
        'description': 'Common errors when deploying Dash Apps.'
    },
    {
        'url': '/dash-enterprise/support',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Support,
        'name': 'Support',
        'description': 'Having trouble deploying your app? Our dedicated '
        'support team is available to help you out.'
    },
    {
        'url': '/dash-enterprise/git',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Git,
        'name': 'Advanced Git',
        'description': 'A reference for git commands and how they are used '
        'with Dash Enterprise.'
    },
    {
        'url': '/dash-enterprise/privacy',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.AppPrivacy,
        'name': 'Dash App Privacy',
        'description': 'Dash App Privacy and Managing Collaborators'
    },
    {
        'url': '/dash-enterprise/app-authentication',
        'content': chapters.dash_enterprise.dash_enterprise_chapters.Authentication,
        'name': 'Dash Enterprise Auth Features',
        'description': 'Accessing User Authentication Data in your Dash App'
    },
    {
        'url': '/dash-enterprise/continuous-integration',
        'content': chapters.dash_enterprise.continuous_integration.index.layout,
        'name': 'Dash Enterprise Continuous Integration',
        'description': 'Learn how to setup CI pipelines for Dash Enterprise'
    },
    {
        'url': '/dash-enterprise/review-apps',
        'content': chapters.dash_enterprise.review_apps.index.layout,
        'name': 'Dash Enterprise Review Apps',
        'description': 'Enhance your CI pipeline with automated Review App deployment'
    },
    {
        'url': '/dash-enterprise/api',
        'content': chapters.dash_enterprise.api.index.layout,
        'name': 'GraphQL API',
        'description': 'Learn how to integrate with the Dash Enterprise App Manager with the Graphql API.'
    },
]

DASH_ENTERPRISE_URLS = {
    'name': 'Production Capabilities',
    'description': (
        '''
        #### These capabilities are only available in Dash Enterprise

        > To deploy Dash apps in production environments, you'll need
        > [Dash Enterprise](https://plotly.com/dash).
        >
        > If you already have Dash Enterprise, **visit docs at
        > `https://<your-Dash-Enterprise-URL>/Docs/`**
        >
        > [Find out if your company has Dash Enterprise](https://go.plotly.com/company-lookup).
        '''
    ),
    'chapters': [
        {
            'url': '/deployment',
            'content': chapters.deployment.index.layout,
            'name': 'Deploy your Dash App',
            'description': (
                '''
                How to deploy & configure your application with
                Dash Enterprise App Manager.
                [Learn more](https://plotly.com/dash/app-manager/).
                '''
            ),
            'icon': 'fas fa-cloud-upload-alt',
        },

        {
            'url': '/authentication',
            'content': chapters.auth.index.layout,
            'name': 'Add Authentication to your Dash App',
            'description': (
                '''
                Protect your application behind a login screen &
                access user authentication data in your Dash apps.
                [Learn more](https://plotly.com/dash/authentication-middleware/).
                '''
            ),
            'icon': 'fas fa-users',
            'ad': 'dash-enterprise-app-manager.jpg',
            'adhref': 'https://plotly.com/get-demo/?utm_source=docs&utm_medium=ad&utm_campaign=april&utm_content=authentication',
        },

        {
            'url': '/integrating-dash',
            'content': chapters.integrating_dash.index.layout,
            'name': 'Embed your Dash App in other Websites',
            'description': (
                '''
                Embed your Dash applications in external websites securely
                without iframes.
                [Learn more](https://plotly.com/dash/embedding/).
                '''
            ),
            'icon': 'fas fa-code',
        },

        {
            'url': 'https://plotly.com/dash/design-kit/',
            'name': 'Design Kit',
            'description': (
                '''
                Dash Enterprise Design Kit is a set of Dash components
                designed to simplify application layout and theme your
                apps. No CSS required.
                [Learn more](https://plotly.com/dash/design-kit).
                '''
            ),
            'icon': 'fas fa-palette'
        },

        {
            'url': 'https://plotly.com/dash/snapshot-engine/',
            'name': 'Snapshot Engine',
            'description': (
                '''
                Snapshot Engine is a Dash Enterprise capability for saving
                views of Dash apps and generating PDF reports from Python.
                [Learn more](https://plotly.com/dash/snapshot-engine)
                '''
            ),
            'icon': 'fas fa-camera-retro'
        },

        {
            'url': 'https://plotly.com/dash/job-queue/',
            'name': 'Job Queue',
            'description': (
                '''
                Background jobs can dramatically improve the scalability of
                a Dash app by enabling it to offload slow or CPU-intensive
                tasks from its callback loops. Background jobs can also
                run periodically in the background to refresh your app's
                data on a daily or hourly basis. [Learn more](https://plotly.com/dash/job-queue/).
                '''
            ),
            'icon': 'fas fa-clock'
        },

        {
            'url': 'https://plotly.com/dash/kubernetes/',
            'name': 'Kubernetes Installation',
            'description': (
                '''
                Dash Apps on Dash Enterprise scale horizontally thanks to
                a stateless design and Kubernetes infrastructure.
                 [Learn more](https://plotly.com/dash/kubernetes/).
                '''
            ),
            'icon': 'fas fa-fighter-jet'
        },

        {
            'url': 'https://plotly.com/dash/snapshot-engine/',
            'name': 'Dash Notes',
            'description': (
                '''
                With Dash Notes, the entire Dash app becomes a drawing canvas.
                Dash app end users can make annotations on Dash apps that
                trigger email notifications to stakeholders. Try to do that
                in Tableau! [Learn more](https://plotly.com/dash/snapshot-engine/).
                '''
            ),
            'icon': 'fas fa-pencil-alt'
        },

        {
            'url': 'https://plotly.com/dash/workspaces/',
            'name': 'Data Science Workspaces',
            'description': (
                '''
                A built-in IDE to develop Dash apps or Jupyter notebooks on
                Dash Enterprise without leaving your browser. In Workspaces,
                the development environment closly matches production.
                [Learn more](https://plotly.com/dash/workspaces/).
                '''
            ),
            'icon': 'fas fa-copy'
        },

        {
            'url': 'https://plotly.com/dash/big-data-for-python/',
            'name': 'Dash Enterprise & Databricks',
            'description': (
                '''
                Connect your Dash apps to Databricks Spark clusters.
                [Learn more](https://plotly.com/dash/big-data-for-python/).
                '''
            ),
            'icon': 'fas fa-database'
        },

        {
            'url': 'https://plotly.com/dash/big-data-for-python/',
            'name': 'Dash Enterprise & Snowflake',
            'description': (
                '''
                Connect your Dash apps to Snowflake Data Warehouse.
                [Learn more](https://plotly.com/dash/big-data-for-python/).
                '''
            ),
            'icon': 'fas fa-snowflake'
        },

        {
            'url': 'https://plotly.com/dash/ai-and-ml-templates/',
            'name': 'Sample Apps & Templates',
            'description': (
                '''
                Get started with these curated sample apps or learn first
                principles from the templates in this section.
                Sample Apps include the [AI & ML App Catalogue](https://plotly.com/dash/ai-and-ml-templates/).
                '''
            ),
            'icon': 'fas fa-grip-horizontal'
        },

        {
            'url': '/dash-enterprise',
            'name': 'App Manager',
            'icon': 'fas fa-book',
            'description': (
                '''
                Documentation for the Dash Enterperise App Manager.
                Learn how to deploy apps, manage SSH keys, configure database
                mounts, manage buildpacks, configure databases and more.
                '''
            ),
            'chapters': APP_MANAGER_URLS
        }

    ]
}

URLS = [
    {
        'name': "What's Dash?",
        'chapters': [
            {
                'url': '/introduction',
                'name': 'Introduction',
                'description': '''
                    A quick paragraph about Dash and a link to the talk at
                    Plotcon that started it all.
                ''',
                'content': chapters.introduction.index.layout
            }
        ] + [
            {
                'url': 'https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503',
                'name': 'Announcement Essay (2017)',
                'description': (
                    '''
                    Our extended essay on Dash. An extended discussion of
                    Dash's architecture and our motivation behind the project.
                    '''
                )
            },
            {
                'url': 'https://dash-gallery.plotly.host/Portal/',
                'name': 'Dash App Gallery',
                'description': '''
                    A glimpse into what's possible with Dash.
                '''
            },
            {
                'url': 'https://go.plotly.com/dash-club',
                'name': 'Dash Club',
                'description': '''
                    An email newsletter by chriddyp, the creator of Dash.
                '''
            },
        ] +
        ([
            {
                'url': '/dash-enterprise',
                'name': 'Dash Enterprise',
                'description': '''
                    The commercial platform behind Dash Open Source for
                    developing, deploying, and managing better Dash Applications
                    at scale.
                ''',
                'className': 'red'
            }
        ] if not tools.is_in_dash_enterprise() else [])
    },

    {
        'name': 'Dash Tutorial',
        'chapters': [
            {
                'url': '/installation',
                'name': 'Part 1. Installation',
                'description': 'How to install and upgrade dash libraries with pip',
                'content': chapters.installation.index.layout
            },
            {
                'url': '/layout',
                'name': 'Part 2. Layout',
                'description': (
                    'The Dash `layout` describes what your app will '
                    'look like and is composed of a set of declarative '
                    'Dash components.'
                ),
                'content': chapters.getting_started.index.layout
            },
            {
                'url': '/basic-callbacks',
                'name': 'Part 3. Basic Callbacks',
                'description': (
                    "Dash apps are made interactive through Dash "
                    "Callbacks: Python functions that are "
                    "automatically called whenever an input "
                    "component's property changes. Callbacks "
                    "can be chained, allowing one update in the "
                    "UI to trigger several updates across the app."
                ),
                'content': chapters.basic_callbacks.index.layout
            },
            {
                'url': '/interactive-graphing',
                'name': 'Part 4. Interactive Graphing and Crossfiltering',
                'description': 'Bind interactivity to the Dash `Graph` ' \
                               'component whenever you hover, click, or ' \
                               'select points on your chart.',
                'content': chapters.graph_crossfiltering.index.layout
            },
            {
                'url': '/sharing-data-between-callbacks',
                'name': 'Part 5. Sharing Data Between Callbacks',
                'description': '`global` variables will break your Dash apps. ' \
                               'However, there are other ways to share data ' \
                               'between callbacks. This chapter is useful for ' \
                               'callbacks that run expensive data processing ' \
                               'tasks or process large data.',
                'content': chapters.sharing_data.index.layout
            },
            {
                'url': '/faqs',
                'name': 'Part 6. FAQs',
                'description': 'If you have read through the rest of the ' \
                'tutorial and still have questions or are encountering ' \
                'unexpected behaviour, this chapter may be useful.',
                'content': chapters.faq_gotchas.index.layout
            }
        ]
    },

    {
        'name': 'Dash Callbacks',
        'chapters': [
            {
                'url': '/basic-callbacks',
                'name': 'Basic Callbacks',
                'description': 'Go through this introductory chapter to '
                'learn the foundations of the Dash callback.',
                'content': chapters.basic_callbacks.index.layout
            },
            {
                'url': '/advanced-callbacks',
                'name': 'Advanced Callbacks',
                'description': 'Now that you\'ve gotten through the basics, '
                'take a look at other things you can do with callbacks - '
                'from performance improvements to callback contexts.',
                'content': chapters.advanced_callbacks.index.layout
            },
            {
                'url': '/clientside-callbacks',
                'name': 'Clientside Callbacks',
                'description': 'You might want to execute a callback in '
                'the frontend as opposed to the backend if you want to '
                'avoid the extra time that it takes to make a roundtrip '
                'to the server. Clientside callbacks allow you to write '
                'your callbacks in JavaScript that runs in the browser.',
                'content': chapters.clientside_callbacks.index.layout
            },
            {
                'url': '/pattern-matching-callbacks',
                'name': 'Pattern-Matching Callbacks',
                'description': (
                    'The pattern-matching callback selectors `MATCH`, `ALL`, '
                    '& `ALLSMALLER` allow you to write '
                    'callbacks that respond to or update an arbitrary or dynamic '
                    'number of components. '
                    'New in Dash 1.11.0!'
                ),
                'content': chapters.pattern_matching_callbacks.index.layout
            },
            {
                'url': '/callback-gotchas',
                'name': 'Callback Gotchas',
                'description': 'Dash callbacks have some idiosyncrasies that '
                'should be taken into consideration when building a Dash app. '
                'If you\'re running into unexpected callback behavior, '
                'and the rest of the documentation hasn\'t shed any light on '
                'the situation, try taking a look in this section.',
                'content': chapters.callback_gotchas.index.layout
            }
        ]
    },

    {
        'name': 'Open Source Component Libraries',
        'urls': [
            '/dash-core-components/',
            '/dash-html-components/',
            '/datatable/',
            '/dash-bio/'
            '/dash-daq/',
            '/canvas/',
            '/slicer/',
            '/annotations/',
            '/cytoscape/'
        ],
        'chapters': [
            {
                'name': 'Dash Core Components',
                'chapters': [{
                    'url': '/dash-core-components',
                    'name': 'Overview',
                    'breadcrumb': 'Dash Core Components',
                    'description': (
                        'The Dash Core Component library contains a set '
                        'of higher-level components like sliders, graphs, '
                        'dropdowns, tables, and more.'
                    ),
                    'content': chapters.dash_core_components.index.layout,
                    'ad': 'dash-enterprise-design-kit.jpg',
                    'adhref': 'https://plotly.com/dash/design-kit/?utm_source=docs&utm_medium=sidebar&utm_campaign=june&utm_content=htmlcore'
                }] + component_list(
                    dcc,
                    chapters.dash_core_components.content_module,
                    'dash-core-components',
                    'dcc',
                    'dash_core_components',
                    ad='dash-enterprise-design-kit.jpg',
                    adhref='https://plotly.com/dash/design-kit/?utm_source=docs&utm_medium=sidebar&utm_campaign=june&utm_content=htmlcore'
                )
            },

            {
                'name': 'Dash HTML Components',
                'chapters': [
                    {
                        'url': '/dash-html-components',
                        'name': 'Overview',
                        'breadcrumb': 'Dash HTML Components',
                        'description': 'Dash provides all of the available HTML tags ' \
                                       'as user-friendly Python classes. This chapter ' \
                                       'explains how this works and the few important ' \
                                       'key differences between Dash HTML components ' \
                                       'and standard html.',
                        'content': chapters.dash_html_components.index.layout,
                        'ad': 'dash-enterprise-design-kit.jpg',
                        'adhref': 'https://plotly.com/dash/design-kit/?utm_source=docs&utm_medium=sidebar&utm_campaign=june&utm_content=htmlcore'
                    }
                ] + component_list(
                    html,
                    chapters.dash_html_components.content_module,
                    'dash-html-components',
                    'html',
                    'dash_html_components',
                    escape_tags=True,
                    ad='dash-enterprise-design-kit.jpg',
                    adhref='https://plotly.com/dash/design-kit/?utm_source=docs&utm_medium=sidebar&utm_campaign=june&utm_content=htmlcore'
                )
            },

            {
                'name': 'Dash DataTable',

                'chapters': [
                    {
                        'url': '/datatable',
                        'name': 'Overview',
                        'breadcrumb': 'Dash DataTable',
                        'description': (
                            '`dash_table.DataTable` is an interactive table that ' \
                            'supports rich styling, ' \
                            'conditional formatting, editing, sorting, filtering, ' \
                            'and more.'
                        ),
                        'autogenerate_index': True,
                        'preamble': chapters.dash_datatable.index.preamble,
                    },

                    {
                        'url': '/datatable/reference',
                        'name': 'Reference',
                        'content': chapters.dash_datatable.reference.index.layout,
                        'description': '''
                            A comprehensive list of all of the
                            DataTable properties.
                        '''
                    },

                    {
                        'url': '/datatable/height',
                        'content': chapters.dash_datatable.height.index.layout,
                        'name': 'DataTable Height',
                        'description': '''
                            How to set the height of the DataTable.
                            Examples include how to set the height with
                            vertical scroll, pagination, virtualization, and
                            fixed headers.
                        '''
                    },

                    {
                        'url': '/datatable/width',
                        'content': chapters.dash_datatable.width.index.layout,
                        'name': 'DataTable Width & Column Width',
                        'description': '''
                            How to set the width of the table and the columns.
                            Examples include how to handle word wrapping,
                            cell clipping, horizontal scroll, fixed columns,
                            and more.
                        '''
                    },

                    {
                        'url': '/datatable/style',
                        'content': chapters.dash_datatable.styling.index.layout,
                        'name': 'Styling',
                        'description': '''
                            The style of the DataTable is highly customizable. This chapter
                            includes examples for:
                            - Displaying multiple rows of headers
                            - Text alignment
                            - Styling the table as a list view
                            - Changing the colors (including a dark theme!)
                        '''
                    },

                    {
                        'url': '/datatable/conditional-formatting',
                        'content': chapters.dash_datatable.conditional_formatting.index.layout,
                        'name': 'Conditional Formatting',
                        'description': '''
                            Several examples of how to highlight certain cells,
                            rows, or columns based on their value or state.
                        '''
                    },

                    {
                        'url': '/datatable/data-formatting',
                        'content': chapters.dash_datatable.data_formatting.index.layout,
                        'name': 'Number Formatting',
                        'description': '''
                            Several examples of how to format and localize numbers.
                        '''
                    },

                    {
                        'url': '/datatable/interactivity',
                        'content': chapters.dash_datatable.interactivity.index.layout,
                        'name': 'Sorting, Filtering, Selecting, and Paging Natively',
                        'description': '''
                            The DataTable is interactive. This chapter demonstrates the
                            interactive features of the table and how to wire up these
                            interations to Python callbacks. These actions include:
                            - Paging
                            - Selecting Rows
                            - Sorting Columns
                            - Filtering Data
                        '''
                    },

                    {
                        'url': '/datatable/tooltips',
                        'content': chapters.dash_datatable.tooltips.index.layout,
                        'name': 'DataTable Tooltips',
                        'description': '''
                            Display tooltips on data and header rows, conditional tooltips,
                            define tooltips for each cell, customize behavior.
                        '''
                    },

                    {
                        'url': '/datatable/callbacks',
                        'content': chapters.dash_datatable.callbacks.index.layout,
                        'name': 'Python-Driven Filtering, Paging, Sorting',
                        'description': '''
                            In Part 3, the paging, sorting, and filtering was done entirely
                            clientside (in the browser). This means that you need to
                            load all of the data into the table up-front. If your data is large,
                            then this can be prohibitively slow.

                            In this chapter, you'll learn how to write your own filtering,
                            sorting, and paging backends in Python with Dash.
                            We'll do the data processing with Pandas but you could write your
                            own routines with SQL or even generate the data on the fly!
                        '''
                    },

                    {
                        'url': '/datatable/editable',
                        'content': chapters.dash_datatable.editing.index.layout,
                        'name': 'Editable DataTable',
                        'description': '''
                            The DataTable is editable. Like a spreadsheet, it can be used
                            as an input for controlling models with a variable number
                            of inputs.

                            This chapter includes recipes for:

                            - Determining which cell has changed
                            - Filtering out null values
                            - Adding or removing columns
                            - Adding or removing rows
                            - Ensuring that a minimum set of rows are visible
                            - Running Python computations on certain columns or cells
                        '''
                    },

                    {
                        'url': '/datatable/typing',
                        'content': chapters.dash_datatable.typing.index.layout,
                        'name': 'Typing and User Input Processing',
                        'description': '''
                            In this chapter, you'll learn how to configure the table to
                            - assign the column type
                            - change the data presentation
                            - change the data formatting
                            - validate or coerce user data input
                            - apply default behavior for valid and invalid data
                        '''
                    },

                    {
                        'url': '/datatable/dropdowns',
                        'content': chapters.dash_datatable.dropdowns.index.layout,
                        'name': 'Dropdowns Inside DataTable',
                        'description': '''
                            Cells can be rendered as editable Dropdowns. This is our first
                            stake in bringing a full typing system to the table.
                            Rendering cells as dropdowns introduces some complexity in the
                            markup and so there are a few limitations that you should be aware
                            of.
                        '''
                    },

                    {
                        'url': '/datatable/virtualization',
                        'content': chapters.dash_datatable.virtualization.index.layout,
                        'name': 'Virtualization',
                        'description': '''
                            Examples using DataTable virtualization.
                        '''
                    },

                    {
                        'url': '/datatable/filtering',
                        'content': chapters.dash_datatable.filtering.index.layout,
                        'name': 'Filtering Syntax',
                        'description': '''
                            An explanation and examples of filtering syntax for both frontend
                            and backend filtering in the DataTable.
                        '''
                    },

                ]
            },

            {
                'name': 'Dash Bio',
                'chapters': [
                    dict({
                        'url': '/dash-bio',
                        'name': 'Overview',
                        'breadcrumb': 'Dash Bio',
                        'description': (
                            'Dash Bio is a component library '
                            'dedicated to visualizing bioinformatics data.'
                        ),
                        'autogenerate_index': (
                            True if
                            os.environ.get('IGNORE_DASH_BIO', False)
                            else False
                        )
                    },
                    **({} if os.environ.get('IGNORE_DASH_BIO', False)
                    else {'content': chapters.dash_bio.index.layout}))
                ] + component_list(
                    dash_bio,
                    None if os.environ.get('IGNORE_DASH_BIO', False) else
                    chapters.dash_bio.content_module,
                    'dash-bio',
                    'dash_bio',
                    'dash_bio'
                )
            },
            {
                'name': 'Dash DAQ',
                'chapters': [
                    {
                        'url': '/dash-daq',
                        'name': 'Overview',
                        'breadcrumb': 'Dash DAQ',
                        'content': chapters.dash_daq.index.layout,
                        'description': (
                            '''
                            Beautifully styled technical components for
                            data acquisition, monitoring, and engineering
                            applications.
                            '''
                        )
                    }
                ] + component_list(
                    dash_daq,
                    chapters.dash_daq.content_module,
                    'dash-daq',
                    'dash_daq',
                    'dash_daq'
                )
            },

            {
                'name': 'Dash Image annotations',
                'chapters': [
                    {
                        'url': '/annotations',
                        'name': 'Overview & Reference',
                        'content': chapters.dash_annotations.index.layout,
                        'description': (
                            'Image annotations for image processing applications.'
                        )
                    }
                ]
            },

            {
                'name': 'Dash Canvas',
                'chapters': [
                    {
                        'url': '/canvas',
                        'name': 'Overview & Reference',
                        'content': chapters.dash_canvas.index.layout,
                        'description': (
                            'Image rendering, drawing, annotations '
                            'for image processing applications '
                            '(legacy tool).'
                        )
                    }
                ]
            },

            {
                'name': 'Dash Slicer',
                'chapters': [
                    {
                        'url': '/slicer',
                        'name': 'Overview & Reference',
                        'content': chapters.dash_slicer.index.layout,
                        'description': (
                            'A volume slicer for Dash.'
                        )
                    }
                ]
            },

            {
                'name': 'Dash Cytoscape',
                'chapters': [
                    {
                        'url': '/cytoscape',
                        'name': 'Overview',
                        'breadcrumb': 'Dash Cytoscape',
                        'description': (
                            '''
                            Dash Cytoscape is our new network visualization
                            component. It offers a declarative and pythonic
                            interface to create beautiful, customizable,
                            interactive and reactive network graphs.
                            '''
                        ),
                        'autogenerate_index': True,
                        'preamble': chapters.dash_cytoscape.index.preamble
                    },

                    {
                        'url': '/cytoscape/elements',
                        'content': chapters.dash_cytoscape.elements.index.layout,
                        'name': 'Basic Usage & Elements',
                        'description': '''
                        Overview of element declaration and manipulation.
                        '''
                    },

                    {
                        'url': '/cytoscape/layout',
                        'content': chapters.dash_cytoscape.layout.index.layout,
                        'name': 'Layouts',
                        'description': '''
                        Description of built-in layouts, and how to modify their properties.
                        '''
                    },

                    {
                        'url': '/cytoscape/styling',
                        'content': chapters.dash_cytoscape.styling.index.layout,
                        'name': 'Styling',
                        'description': '''
                        Methods to style elements with a CSS-like syntax.
                        '''
                    },

                    {
                        'url': '/cytoscape/callbacks',
                        'content': chapters.dash_cytoscape.callbacks.index.layout,
                        'name': 'Callbacks',
                        'description': '''
                        Methods to combine Dash callbacks to update your Cytoscape object.
                        '''
                    },

                    {
                        'url': '/cytoscape/events',
                        'content': chapters.dash_cytoscape.events.index.layout,
                        'name': 'User Interactions',
                        'description': '''
                        Overview of user-interaction events that trigger callbacks in Dash,
                        and how to use them to update the Cytoscape component.
                        '''
                    },

                    {
                        'url': '/cytoscape/biopython',
                        'content': chapters.dash_cytoscape.applications.index.layout,
                        'name': 'Biopython Examples',
                        'description': '''
                        Examples of applications in bioinformatics using Biopython.
                        '''
                    },

                    {
                        'url': '/cytoscape/images',
                        'content': chapters.dash_cytoscape.image_export.index.layout,
                        'name': 'Exporting Images',
                        'description': '''
                        This example shows how to export your Cytoscape graphs as images (jpg, png, svg).
                        '''
                    },

                    {
                        'url': '/cytoscape/responsive',
                        'content': chapters.dash_cytoscape.responsive.index.layout,
                        'name': 'Making responsive graphs',
                        'description': '''
                        This example shows how to build a responsive Cytoscape graph.
                        '''
                    },

                    {
                        'url': '/cytoscape/reference',
                        'content': chapters.dash_cytoscape.reference.index.layout,
                        'name': 'Reference',
                        'description': '''
                        Comprehensive list of all of the Cytoscape properties.
                        '''
                    },

                ]
            },

            {
                'name': 'Dash Bootstrap Components',
                'chapters': [
                    {
                        'url': 'https://dash-bootstrap-components.opensource.faculty.ai/',
                        'name': 'faculty.ai',
                        'description': (
                            'A library of Bootstrap components '
                            'created by [faculty.ai](https://faculty.ai/). '
                            'Dash Bootstrap Components makes it easier to '
                            'build consistently styled '
                            'apps with complex, responsive layouts.'
                        ),
                    },
                ]
            },

            {
                'name': 'Dash Community Components',
                'chapters': [
                    {
                        'url': 'https://plotly.com/dash-community-components/',
                        'name': 'Components List',
                        'description': (
                            'A listicle of selected Dash components created by users '
                            'in [our community forum](https://community.plotly.com/). '
                            'These are Dash Components created by the '
                            'world\'s largest open-source community '
                            'for ML & data science web apps.'
                        ),
                    },
                ]
            }
        ]
    },

    {
        'name': 'Creating Your Own Components',
        'chapters': [
            {
                'name': 'React for Python Developers',
                'description': (
                    '''
                    A tutorial on how to program in React and JavaScript
                    for Python developers.
                    '''
                ),
                'url': '/react-for-python-developers',
                'content': chapters.react_for_python_developers.index.layout,
            },

            {
                'name': 'Build Your Own Components',
                'description': 'Dash components are built with ' \
                               '[React.js](https://reactjs.org/). Dash provides ' \
                               'a React &rarr; Dash toolchain that generates a Dash-' \
                               'compatible interface to these components in Python.',
                'url': '/plugins',
                'content': chapters.plugins.index.layout,
                'ad': 'dash-enterprise-design-kit.jpg',
                'adhref': 'https://plotly.com/get-demo/?utm_source=docs&utm_medium=ad&utm_campaign=april&utm_content=create'
            },

            {
                'name': 'Integrating D3.js into Dash Components',
                'description': (
                    '''
                    Tutorials and resources on encapsulating D3.js graphs in
                    Dash-friendly React components.
                    Includes two sample components: a D3.js network graph
                    and a D3.js sunburst chart.
                    '''
                ),
                'url': '/d3-react-components',
                'content': chapters.d3_react_components.index.layout,
            }
        ]
    },

    {
        'name': 'Beyond the Basics',
        'chapters': [
            {
                'url': '/performance',
                'content': chapters.performance.index.layout,
                'name': 'Performance',
                'description': 'There are three main ways to speed up Dash apps: '\
                               'caching, using WebGL chart types, and implementing '\
                               'clientside callbacks.'
            },

            {
                'url': '/live-updates',
                'content': chapters.live_updates.index.layout,
                'name': 'Live Updates',
                'description': '''
                    Update your apps on page load or
                    on a predefined interval (e.g. every 5 seconds)
                '''
            },

            {
                'url': '/external-resources',
                'content': chapters.external_resources.index.layout,
                'name': 'Adding CSS & JS and Overriding the Page-Load Template',
                'description': '''
                    New in dash v0.22.0! Learn how to add custom CSS and JS to your
                    application with the `assets` directory. Also, learn how to
                    customize the HTML template that Dash serves on page load in order
                    to add custom meta tags, customize the page's title, and more.
                '''
            },

            {
                'url': '/urls',
                'content': chapters.urls.index.layout,
                'name': 'URL Routing and Multiple Apps',
                'description': 'Dash provides two components (`dcc.Link` and ' \
                               '`dcc.Location`) that allow you to easily make ' \
                               'fast multipage apps using its own "Single Page ' \
                               'App (SPA)" design pattern.'
            },

            {
                'url': '/persistence',
                'content': chapters.persistence.index.layout,
                'name': 'Persisting User Preferences & Control Values',
                'description': '''
                    (Released September 2019 with Dash 1.3) Save user choices
                    across page reloads, or just when removing and re-adding a
                    component. Learn how to use persistence, and how to enable it
                    in components you write yourself.
                '''
            },

            {
                'url': '/devtools',
                'content': chapters.devtools.index.layout,
                'name': 'Dev tools',
                'description': 'Dash dev tools reference'
            },

            {
                'url': '/loading-states',
                'content': chapters.loading.index.layout,
                'name': 'Loading States',
                'description': 'Getting the loading state of a component and adding a loading component'
            },

            {
                'url': '/testing',
                'content': chapters.testing.index.layout,
                'name': 'Dash Testing',
                'description': 'An introduction to testing your dash app with selenium'
            },

            {
                'url': '/app-lifecycle',
                'content': chapters.app_lifecycle.index.layout,
                'name': 'Dash App Lifecycle',
                'description': 'An overview of the lifecycle of a Dash app'
            },

            {
                'url': '/dash-1-0-migration',
                'name': 'Dash 1.0.0 Migration',
                'description': (
                    "Dash v1.0 is out! If you're new to Dash, just head down to "
                    "the tutorial section below and get started. This section is "
                    "for users Dash v0.x upgrading to v1.0. We've learned a lot "
                    "from working with the amazing Dash community, and Dash v1.0 "
                    "makes a number of changes to make your apps even more "
                    "intuitive, powerful, and extensible as Dash continues to "
                    "evolve."
                ),
                'content': chapters.migration.index.layout
            },

        ],
    },

    {
        'name': 'Ecosystem Integration',
        'chapters': [
            {
                'url': '/holoviews',
                'content': chapters.holoviews.index.layout,
                'name': 'HoloViews',
                'description': 'HoloViews integration'
            },
        ]
    }
] + ([DASH_ENTERPRISE_URLS] if not tools.is_in_dash_enterprise() else []) + [{
        'name': 'Getting Help',
        'chapters': [
            {
                'url': 'https://community.plotly.com/c/dash',
                'description': '',
                'name': 'The Dash Community Forum'
            },
            {
                'url': '/support',
                'name': 'Support and Contact',
                'description': '',
                'content': chapters.support.index.layout,
            }
        ]
    },
]




def create_index_pages(url_set):
    for section in url_set:
        if section.get('autogenerate_index'):
            section['content'] = html.Div([
                html.Div(section.get('preamble', '')),
                # Convention is to let the first chapter
                # be the "overview" chapter/link,
                # so skip it when we're generating that page
                # as we're already on it.
                html.Div(TOCChapters(url_set[1:]))
            ])
        if 'chapters' in section:
            create_index_pages(section['chapters'])
create_index_pages(URLS)


def normalize_description_and_urls(url_set):
    for section in url_set:
        if 'description' in url_set:
            url_set['description'] = textwrap.dedent(url_set['description']).strip()
        if 'url' in url_set:
            url_set['url'] = url_set['url'].rstrip('/')
normalize_description_and_urls(URLS)


URL_TO_CONTENT_MAP = {}
URL_TO_BREADCRUMB_MAP = {}
def create_url_mapping(url_set):
    for section in url_set:
        if 'url' in section and section['url'].startswith('/'):
            stripped_url = section['url'].rstrip('/')
            URL_TO_CONTENT_MAP[stripped_url] = section.get(
                'content',
                'Content for {} not defined'.format(section['url'])
            )
            URL_TO_BREADCRUMB_MAP[stripped_url] = section.get(
                'breadcrumb',
                section['name']
            )
        if 'chapters' in section:
            create_url_mapping(section['chapters'])
create_url_mapping(URLS)

URL_TO_META_MAP = {}
def create_meta_map(url_set):
    for section in url_set:
        if 'url' in section:
            URL_TO_META_MAP[section['url'].rstrip('/')] = section
        if 'chapters' in section:
            create_meta_map(section['chapters'])
create_meta_map(URLS)

def find_section(url_set, name):
    for section in url_set:
        if section.get('name', '') == name:
            return section
        elif 'chapters' in section:
            return find_section(section['chapters'], name)


def _search_keywords(children):
    # Check if any of the component's proptypes are in the chapter so that
    # users can search for particular proptypes like selected_rows

    def _concat(unicode_or_str1, unicode_or_str2):
        if type(unicode_or_str1) == type(unicode_or_str2):
            return unicode_or_str1 + unicode_or_str2
        return unicode_or_str1 + unicode_or_str2.decode('utf8')

    stringified_children = u''
    if not hasattr(children, '_traverse'):
        children = html.Div(children)
    for item in children._traverse():
        if isinstance(item, six.string_types):
            # I don't really get this, but there seems to be a mix
            # of unicode and strings here
            stringified_children = _concat(stringified_children, item)
        elif (hasattr(item, 'children') and
              isinstance(item.children, six.string_types)):
            stringified_children = _concat(stringified_children, item.children)

    keywords = []
    common_keywords_to_ignore = [
        'id', 'className', 'loading_state', 'value'
    ]
    component_libraries = [
        html, dcc, dash_table, dash_daq, dash_cytoscape, dash_bio
    ]
    for component_library in component_libraries:
        component_names = [
            i for i in dir(component_library)
            if (
                not i.startswith('_') and
                i[0].upper() == i[0] and
                type(getattr(component_library, i)) == dash.development.base_component.ComponentMeta
            )
        ]
        for component_name in component_names:
            if component_name in ['DarkThemeProvider']:
                component = getattr(component_library, component_name)()
            elif component_name == 'Circos':
                component = getattr(component_library, component_name)(layout=None)
            elif component_name == 'Link':
                component = getattr(component_library, component_name)(href='')
            else:
                try:
                    component = getattr(component_library, component_name)(id='_')
                except Exception as e:
                    print(
                        ">> This doesn't look like a component!\n" +
                        'Add to the ignore list in _search_keywords:'
                    )
                    print([component_library, component_name])
                    raise e
            component_prop_types = component._prop_names
            for prop in component_prop_types:
                if (prop not in common_keywords_to_ignore and
                        prop not in keywords and
                        prop in stringified_children):
                    keywords.append(prop)

    return keywords


def index_pages(url_set):
    for section in url_set:
        if 'content' in section:
            section['meta_keywords'] = ', '.join(_search_keywords(section.get('content')))
        if 'chapters' in section:
            index_pages(section['chapters'])

def create_urls_without_content(url_set):
    for section in url_set:
        if 'content' in section:
            section.pop('content')
        if 'preamble' in section:
            section.pop('preamble')
        if 'ad' in section:
            section.pop('ad')
        if 'adhref' in section:
            section.pop('adhref')
        if ('description' in section and
                isinstance(section['description'],
                dash.development.base_component.Component)):
            section.pop('description')
        if 'chapters' in section:
            create_urls_without_content(section['chapters'])
