import os
from .import tutorial

import dash_html_components as html
import dash_core_components as dcc
import dash_table
import dash_daq
import dash_cytoscape
import dash_bio

from dash_docs import reusable_components, tools
from .reusable_components import TOC, TOCChapters

## The chapters dict is used to generate the dash-docs search index
## If edited, update the search index by running `python dash_search_index.py`
## in the root of this repo.


def component_list(package, content_module, base_url, import_alias, escape_tags=False):
    return [
        {
            'url': tools.relpath('/{}/{}'.format(base_url, component.lower())),
            'name': '{}.{}'.format(import_alias, component),
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
                    reusable_components.Markdown(
                        getattr(package, component).__doc__,
                        escape_tags=escape_tags
                    ),
                ])
            )
        } for component in sorted(dir(package))
        if not component.startswith('_') and
        component[0].upper() == component[0]
    ]

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
                'content': tutorial.introduction.layout
            },
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
                'content': tutorial.migration.layout
            },
            {
                'url': 'https://go.plot.ly/dash-club',
                'name': 'Dash Club',
                'description': '''
                    An email newsletter by chriddyp, the creator of Dash.
                '''
            }
        ]
    },

    {
        'name': 'Dash Tutorial',
        'chapters': [
            {
                'url': '/installation',
                'name': 'Part 1. Installation',
                'description': 'How to install and upgrade dash libraries with pip',
                'content': tutorial.installation.layout
            },
            {
                'url': '/getting-started',
                'name': 'Part 2. Layout',
                'description': (
                    'The Dash `layout` describes what your app will '
                    'look like and is composed of a set of declarative '
                    'Dash components.'
                ),
                'content': tutorial.getting_started_part_1.layout
            },
            {
                'url': '/getting-started-part-2',
                'name': 'Part 3. Basic Callbacks',
                'description': (
                    "Dash apps are made interactive through Dash "
                    "Callbacks: Python functions that are "
                    "automatically called whenever an input "
                    "component's property changes. Callbacks "
                    "can be chained, allowing one update in the "
                    "UI to trigger several updates across the app."
                ),
                'content': tutorial.getting_started_part_2.layout
            },
            {
                'url': '/state',
                'name': 'Part 4. More About Callbacks',
                'description': (
                    "Basic callbacks are fired whenever the values "
                    "change. Use Dash `State` with Dash `Inputs` to "
                    "pass in extra values whenever the `Inputs` "
                    "change. `State` is useful for UIs that contain "
                    "forms or buttons. Use the `PreventUpdate` exception "
                    "to leave the callback output unchanged"
                ),
                'content': tutorial.state.layout
            },
            {
                'url': '/interactive-graphing',
                'name': 'Part 5. Interactive Graphing and Crossfiltering',
                'description': 'Bind interactivity to the Dash `Graph` ' \
                               'component whenever you hover, click, or ' \
                               'select points on your chart.',
                'content': tutorial.graphing.layout
            },
            {
                'url': '/sharing-data-between-callbacks',
                'name': 'Part 6. Sharing Data Between Callbacks',
                'description': '`global` variables will break your Dash apps. ' \
                               'However, there are other ways to share data ' \
                               'between callbacks. This chapter is useful for ' \
                               'callbacks that run expensive data processing ' \
                               'tasks or process large data.',
                'content': tutorial.sharing_state.layout
            },
            {
                'url': '/faqs',
                'name': 'Part 7. FAQs & Gotchas',
                'description': 'If you have read through the rest of the ' \
                'tutorial and still have questions or are encountering ' \
                'unexpected behaviour, this chapter may be useful.',
                'content': tutorial.faqs.layout
            }
        ]
    },

    {
        'name': 'Open Source Component Libraries',
        'chapters': [
            {
                'name': 'Dash Core Components',
                'chapters': [{
                    'url': '/dash-core-components/',
                    'name': 'Overview',
                    'description': (
                        'The Dash Core Component library contains a set '
                        'of higher-level components like sliders, graphs, '
                        'dropdowns, tables, and more.'
                    ),
                    'content': tutorial.core_components.layout
                }] + component_list(
                    dcc,
                    tutorial.examples,
                    'dash-core-components',
                    'dcc'
                )
            },

            {
                'name': 'Dash HTML Components',
                'chapters': [
                    {
                        'url': '/dash-html-components/',
                        'name': 'Overview',
                        'description': 'Dash provides all of the available HTML tags ' \
                                       'as user-friendly Python classes. This chapter ' \
                                       'explains how this works and the few important ' \
                                       'key differences between Dash HTML components ' \
                                       'and standard html.',
                        'content': tutorial.html_components.layout
                    }
                ] + component_list(
                    html,
                    None,
                    'dash-html-components',
                    'html',
                    escape_tags=True
                )
            },

            {
                'name': 'Dash DataTable',

                'chapters': [
                    {
                        'url': '/datatable',
                        'name': 'Overview',
                        'description': (
                            '`dash_table.DataTable` is an interactive table that ' \
                            'supports rich styling, ' \
                            'conditional formatting, editing, sorting, filtering, ' \
                            'and more.'
                        ),
                        'autogenerate_index': True,
                        'preamble': tutorial.dash_table_index.preamble,
                    },

                    {
                        'url': '/datatable/reference',
                        'name': 'Reference',
                        'content': tutorial.table.reference_chapter.layout,
                        'description': '''
                            A comprehensive list of all of the
                            DataTable properties.
                        '''
                    },

                    {
                        'url': '/datatable/sizing',
                        'content': tutorial.table.sizing_chapter.layout,
                        'name': 'Sizing',
                        'description': """
                            All about sizing the DataTable. Examples include:
                            - Setting the width and the height of the table
                            - Responsive table design
                            - Setting the widths of individual columns
                            - Handling long text
                            - Fixing rows and columns
                        """
                    },

                    {
                        'url': '/datatable/style',
                        'content': tutorial.table.styling_chapter.layout,
                        'name': 'Styling',
                        'description': """
                            The style of the DataTable is highly customizable. This chapter
                            includes examples for:
                            - Conditional formatting
                            - Displaying multiple rows of headers
                            - Highlighting rows, columns, and cells
                            - Styling the table as a list view
                            - Changing the colors (including a dark theme!)

                            The sizing API for the table has been particularly tricky for
                            us to nail down, so be sure to read this chapter to understand the nuances,
                            limitations, and the APIs that we're exploring.
                        """
                    },

                    {
                        'url': '/datatable/interactivity',
                        'content': tutorial.table.interactivity_chapter.layout,
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
                        'url': '/datatable/callbacks',
                        'content': tutorial.table.table_callbacks_chapter.layout,
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
                        'content': tutorial.table.editing_recipes_chapter.layout,
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
                        'content': tutorial.table.table_typing_chapter.layout,
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
                        'content': tutorial.table.dropdowns_chapter.layout,
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
                        'content': tutorial.table.virtualization_chapter.layout,
                        'name': 'Virtualization',
                        'description': '''
                            Examples using DataTable virtualization.
                        '''
                    },

                    {
                        'url': '/datatable/filtering',
                        'content': tutorial.table.filtering_chapter.layout,
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
                    else {'content': tutorial.dashbio.layout}))
                ] + component_list(
                    dash_bio,
                    None if os.environ.get('IGNORE_DASH_BIO', False) else
                    tutorial.dashbio_examples,
                    'dash-bio',
                    'dash_bio'
                )
            },

            {
                'name': 'Dash DAQ',
                'chapters': [
                    {
                        'url': '/dash-daq',
                        'name': 'Overview',
                        'content': tutorial.daq.layout,
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
                    tutorial.daq_examples,
                    'dash-daq',
                    'dash_daq'
                )
            },

            {
                'name': 'Dash Canvas',
                'chapters': [
                    {
                        'url': '/canvas',
                        'name': 'Overview & Reference',
                        'content': tutorial.canvas.layout,
                        'description': (
                            'Image rendering, drawing, annotations '
                            'for image processing applications.'
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
                        'description': (
                            '''
                            Dash Cytoscape is our new network visualization
                            component. It offers a declarative and pythonic
                            interface to create beautiful, customizable,
                            interactive and reactive graphs.
                            '''
                        ),
                        'autogenerate_index': True,
                        'preamble': tutorial.dash_cytoscape_index.preamble
                    },

                    {
                        'url': '/cytoscape/elements',
                        'content': tutorial.cytoscape.elements_chapter.layout,
                        'name': 'Basic Usage & Elements',
                        'description': '''
                        Overview of element declaration and manipulation.
                        '''
                    },

                    {
                        'url': '/cytoscape/layout',
                        'content': tutorial.cytoscape.layout_chapter.layout,
                        'name': 'Layouts',
                        'description': '''
                        Description of built-in layouts, and how to modify their properties.
                        '''
                    },

                    {
                        'url': '/cytoscape/styling',
                        'content': tutorial.cytoscape.styling_chapter.layout,
                        'name': 'Styling',
                        'description': '''
                        Methods to style elements with a CSS-like syntax.
                        '''
                    },

                    {
                        'url': '/cytoscape/callbacks',
                        'content': tutorial.cytoscape.callbacks_chapter.layout,
                        'name': 'Callbacks',
                        'description': '''
                        Methods to combine Dash callbacks to update your Cytoscape object.
                        '''
                    },

                    {
                        'url': '/cytoscape/events',
                        'content': tutorial.cytoscape.events_chapter.layout,
                        'name': 'User Interactions',
                        'description': '''
                        Overview of user-interaction events that trigger callbacks in Dash,
                        and how to use them to update the Cytoscape component.
                        '''
                    },

                    {
                        'url': '/cytoscape/biopython',
                        'content': tutorial.cytoscape.applications_chapter.layout,
                        'name': 'Biopython Examples',
                        'description': '''
                        Examples of applications in bioinformatics using Biopython.
                        '''
                    },

                    {
                        'url': '/cytoscape/reference',
                        'content': tutorial.cytoscape.reference_chapter.layout,
                        'name': 'Reference',
                        'description': '''
                        Comprehensive list of all of the Cytoscape properties.
                        '''
                    },

                ]
            },

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
                'content': tutorial.react_for_python_developers.layout,
            },

            {
                'name': 'Build Your Own Components',
                'description': 'Dash components are built with ' \
                               '[React.js](https://reactjs.org/). Dash provides ' \
                               'a React &rarr; Dash toolchain that generates a Dash-' \
                               'compatible interface to these components in Python.',
                'url': '/plugins',
                'content': tutorial.plugins.layout,
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
                'content': tutorial.d3.layout,
            }
        ]
    },

    {
        'name': 'Beyond the Basics',
        'chapters': [
            {
                'url': '/performance',
                'content': tutorial.performance.layout,
                'name': 'Performance',
                'description': 'There are three main ways to speed up Dash apps: '\
                               'caching, using WebGL chart types, and implementing '\
                               'clientside callbacks.'
            },

            {
                'url': '/live-updates',
                'content': tutorial.live_updates.layout,
                'name': 'Live Updates',
                'description': '''
                    Update your apps on page load or
                    on a predefined interval (e.g. every 5 seconds)
                '''
            },

            {
                'url': '/external-resources',
                'content': tutorial.external_css_and_js.layout,
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
                'content': tutorial.urls.layout,
                'name': 'URL Routing and Multiple Apps',
                'description': 'Dash provides two components (`dcc.Link` and ' \
                               '`dcc.Location`) that allow you to easily make ' \
                               'fast multipage apps using its own "Single Page ' \
                               'App (SPA)" design pattern.'
            },

            {
                'url': '/persistence',
                'content': tutorial.persistence.layout,
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
                'content': tutorial.devtools.layout,
                'name': 'Dev tools',
                'description': 'Dash dev tools reference'
            },

            {
                'url': '/loading-states',
                'content': tutorial.loading_states.layout,
                'name': 'Loading States',
                'description': 'Getting the loading state of a component and adding a loading component'
            },

            {
                'url': '/testing',
                'content': tutorial.testing.layout,
                'name': 'Dash Testing',
                'description': 'An introduction to testing your dash app with selenium'
            }
        ],
    },

    {
        'name': 'Production',
        'chapters': [
            {
                'url': '/authentication',
                'content': tutorial.auth.layout,
                'name': 'Authentication',
                'description': ''
            },

            {
                'url': '/deployment',
                'content': tutorial.deployment.layout,
                'name': 'Deployment',
                'description': 'To share a Dash app, you need to "deploy" your Dash ' \
                               'app to a server'
            },

            {
                'url': '/integrating-dash',
                'content': tutorial.integrating_dash.layout,
                'name': 'Integrating Dash with Existing Web Apps',
                'description': 'Strategies for integrating Dash apps with existing web ' \
                               'apps.'
            }
        ]
    },

    {
        'name': 'Getting Help',
        'chapters': [
            {
                'url': 'https://community.plot.ly/c/dash',
                'description': '',
                'name': 'The Dash Community Forum'
            },
            {
                'url': '/support',
                'name': 'Support and Contact',
                'description': '',
                'content': tutorial.support.layout,
            }
        ]
    },

    {
        'name': 'Dash Enterprise',
        'description': (
            """
            Dash Enterprise is Plotly's commercial offering for managing
            and improving your Dash apps in your organization.
            """
        ),
        'chapters': [
            {
                'name': 'About Dash Enterprise',
                'url': 'https://plot.ly/dash/'
            },
            {
                'name': 'Dash Enterprise Documentation',
                'chapters': [
                    {
                        'name': 'Overview',
                        'url': '/dash-enterprise',
                        'content': tutorial.dash_deployment_server.layout
                    },
                    {
                        'url': '/dash-enterprise/initialize',
                        'content': tutorial.dds_examples.Initialize,
                        'name': 'Part 1. Initialize Dash Apps on Dash Enterprise',
                        'description': 'Initialize Dash Apps on Plotly Enterprise'
                    },
                    {
                        'url': '/dash-enterprise/deployment',
                        'content': tutorial.dds_examples.Deploy,
                        'name': 'Part 2. Deploy Dash Apps on Dash Enterprise',
                        'description': 'Deploy Dash Apps on Dash Enterprise'
                    },
                    {
                        'url': '/dash-enterprise/application-structure',
                        'content': tutorial.dds_examples.Requirements,
                        'name': 'Application Structure',
                        'description': 'Ensure that your app meets all the requirements for deployment.'
                    },
                    {
                        'url': '/dash-enterprise/static-assets',
                        'content': tutorial.dds_examples.staticAssets,
                        'name': 'Adding Static Assets',
                        'description': 'Learn how to include custom CSS, JS, and images with the `assets` directory.'
                    },
                    {
                        'url': '/dash-enterprise/configure-system-dependencies',
                        'content': tutorial.dds_examples.ConfigSys,
                        'name': 'Configuring System Dependencie',
                        'description': 'Install and configure system dependencies such '
                        'as database drivers or the Java JRE environment.'
                    },
                    {
                        'url': '/dash-enterprise/portal',
                        'content': tutorial.dds_examples.Portal,
                        'name': 'Dash App Portal',
                        'description': 'Learn about the Dash App Portal '
                    },
                    {
                        'url': '/dash-enterprise/admin-panel',
                        'content': tutorial.dds_examples.AdminPanel,
                        'name': 'Admin Panel',
                        'description': 'Manage users in the Admin Panel '
                    },
                    {
                        'url': '/dash-enterprise/privacy',
                        'content': tutorial.dds_examples.AppPrivacy,
                        'name': 'Dash App Privacy',
                        'description': 'Dash App Privacy and Managing Collaborators'
                    },
                    {
                        'url': '/dash-enterprise/redis-database',
                        'content': tutorial.dds_examples.Redis,
                        'name': 'Linking a Redis Database',
                        'description': 'Create and link an in-memory database to your Dash Apps.'
                    },
                    {
                        'url': '/dash-enterprise/environment-variables',
                        'content': tutorial.dds_examples.EnvVars,
                        'name': 'Setting Enviornment Variables',
                        'description': 'Environment variables are commonly used to store '
                        'secret variables like database passwords.'
                    },
                    {
                        'url': '/dash-enterprise/map-local-directories',
                        'content': tutorial.dds_examples.LocalDir,
                        'name': 'Mapping Local Directories',
                        'description': 'Directory mappings allow you to make directories '
                        'on the Dash Enterprise available to your app.'
                    },
                    {
                        'url': '/dash-enterprise/ssh',
                        'content': tutorial.dds_examples.Ssh,
                        'name': 'Authenticating to Dash Enterprise with SSH',
                        'description': "There are two methods to deploy Dash Apps: HTTPS and SSH "
                        "and we recommend getting started with the HTTPS method."
                    },
                    {
                        'url': '/dash-enterprise/cli',
                        'content': tutorial.dds_examples.Cli,
                        'name': 'Managing Dash Apps via the Command Line',
                        'description': "A list of commands to manage Dash apps available  "
                        "to app owners from the command line via ssh."
                    },
                    {
                        'url': '/dash-enterprise/app-authentication',
                        'content': tutorial.dds_examples.Authentication,
                        'name': 'Dash Enterprise Auth Features',
                        'description': 'Accessing User Authentication Data in your Dash App'
                    },
                    {
                        'url': '/dash-enterprise/checks',
                        'content': tutorial.dds_examples.Checks,
                        'name': 'Dash Enterprise App Health Checks',
                        'description': 'Create custom checks to ensure that a newly deployed app can serve traffic.'
                    },
                    {
                        'url': '/dash-enterprise/private-packages',
                        'content': tutorial.dds_examples.PrivatePackages,
                        'name': 'Adding Private Python Packages',
                        'description': 'Intsall private python packages in your Dash Apps.'
                    },
                    {
                        'url': '/dash-enterprise/celery-process',
                        'content': tutorial.dds_examples.Celery,
                        'name': 'Linking a Celery Process',
                        'description': 'Add a task queue to your Dash Apps.'
                    },
                    {
                        'url': '/dash-enterprise/staging-app',
                        'content': tutorial.dds_examples.StagingApp,
                        'name': 'Create a Staging Dash App ',
                        'description': 'Use a staged Dash App to test changes before updating '
                        'your prodcution Dash App.'
                    },
                    {
                        'url': '/dash-enterprise/pdf-service',
                        'content': tutorial.dds_examples.pdfService,
                        'name': 'Dash Enterprise PDF Service',
                        'description': 'Utilize the Dash Enterprise API endpoint for '
                        'creating PDF exports of your Dash applications'
                    },
                    {
                        'url': '/dash-enterprise/analytics',
                        'content': tutorial.dds_examples.Analytics,
                        'name': 'App Analytics',
                        'description': 'View app analytics such as last updated, '
                        'CPU usage, Memory Usage, and more.'
                    },
                    {
                        'url': '/dash-enterprise/logs',
                        'content': tutorial.dds_examples.Logs,
                        'name': 'App Logs',
                        'description': """Check your Dash App's logs via the Dash
                        Enterprise UI or via the command line."""
                    },
                    {
                        'url': '/dash-enterprise/troubleshooting',
                        'content': tutorial.dds_examples.Troubleshooting,
                        'name': 'Common Errors',
                        'description': 'Common errors when deploying Dash Apps.'
                    },
                    {
                        'url': '/dash-enterprise/support',
                        'content': tutorial.dds_examples.Support,
                        'name': 'Support',
                        'description': 'Having trouble deploying your app? Our dedicated '
                        'support team is available to help you out.'
                    },
                    {
                        'url': '/dash-enterprise/git',
                        'content': tutorial.dds_examples.Git,
                        'name': 'Advanced Git',
                        'description': 'A reference for git commands and how they are used '
                        'with Dash Enterprise.'
                    },
                ]
            }
        ]
    }

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


URL_TO_CONTENT_MAP = {}
def create_url_mapping(url_set):
    for section in url_set:
        if 'url' in section:
            URL_TO_CONTENT_MAP[section['url'].rstrip('/')] = section.get(
                'content',
                'Content for {} not defined'.format(section['url'])
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
