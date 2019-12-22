import tutorial
from tutorial import auth
from tutorial import core_component_examples as examples
from tutorial import core_components
from tutorial import cytoscape
from tutorial import d3
from tutorial import dash_cytoscape_index
from tutorial import dash_deployment_server
from tutorial import dash_deployment_server_examples as dds_examples
from tutorial import dash_table_index
from tutorial import daq
from tutorial import daq_component_examples as daq_examples
from tutorial import dashbio
from tutorial import dashbio_component_examples as dashbio_examples
from tutorial import deployment
from tutorial import external_css_and_js
from tutorial import gallery
from tutorial import canvas
from tutorial import getting_started_part_1
from tutorial import getting_started_part_2
from tutorial import faqs
from tutorial import graphing
from tutorial import html_components
from tutorial import installation
from tutorial import introduction
from tutorial import live_updates
from tutorial import migration
from tutorial import performance
from tutorial import plugins
from tutorial import search
from tutorial import sharing_state
from tutorial import state
from tutorial import support
from tutorial import urls
from tutorial import react_for_python_developers
from tutorial import table
from tutorial import devtools
from tutorial import loading_states
from tutorial import testing
from tutorial import integrating_dash


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

    'dash-1-0-migration': {
        'url': '/dash-1-0-migration',
        'content': migration.layout,
        'name': 'Dash v1.0 Migration',
        'description': 'How to upgrade from Dash v0.x to v1.0.'
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

    'faqs': {
        'url': '/faqs',
        'content': faqs.layout,
        'name': 'Part 7. FAQs and Gotchas',
        'description': 'If you have read through the rest of the ' \
        'tutorial and still have questions or are encountering ' \
        'unexpected behaviour, this chapter may be useful.'
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
        ],
        'name': 'Dash HTML Components',
        'description': 'Dash provides all of the available HTML tags ' \
                       'as user-friendly Python classes. This chapter ' \
                       'explains how this works and the few important ' \
                       'key differences between Dash HTML components ' \
                       'and standard html.'
    },

    'datatable': {
        'url': '/datatable',
        'content': dash_table_index.layout,
        'name': 'Dash DataTable',
        'description': '(New! Released Nov 2, 2018) The Dash DataTable is our latest and ' \
                       'most advanced component. It is an interactive table that ' \
                       'supports rich styling, ' \
                       'conditional formatting, editing, sorting, filtering, ' \
                       'and more.'
    },

    'cytoscape': {
        'url': '/cytoscape',
        'content': dash_cytoscape_index.layout,
        'name': 'Dash Cytoscape',
        'description': '(New! Released Feb 5, 2019) Dash Cytoscape is our new network ' \
                       'visualization component. It offers a declarative and ' \
                       'pythonic interface to create beautiful, customizable, ' \
                       'interactive and reactive graphs.'

    },

    'dashdaq': {
        'url': '/dash-daq',
        'content': daq.layout,
        'name': 'Dash DAQ Components',
        'description': 'Beautifully styled technical components for \
        data acquisition and engineering applications.'
    },

    'dashbio': {
        'url': '/dash-bio',
        'content': dashbio.layout,
        'name': 'Dash Bio Components',
        'description': '(New! Released April 2019) Components dedicated to visualizing \
        bioinformatics data.'
    },

  'canvas': {
        'url': '/canvas',
        'content': canvas.layout,
        'name': 'Dash Canvas',
        'description': '(New! Released March 2019) Drawing and annotations for image processing.'
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

    'd3-plugins': {
        'url': '/d3-react-components',
        'content': d3.layout,
        'name': 'Integrating D3.js into Dash Components',
        'description': 'Tutorials and resources on encapsulating ' \
                       'D3.js graphs in Dash-friendly React components. '\
                       'Includes two sample components: a D3.js network graph '\
                       'and a D3.js sunburst chart.'
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

    'integrating-dash': {
        'url': '/integrating-dash',
        'content': integrating_dash.layout,
        'name': 'Integrating Dash with Existing Web Apps',
        'description': 'Strategies for integrating Dash apps with existing web ' \
                       'apps.'
    },

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
    'react-for-python-developers': {
        'url': '/react-for-python-developers',
        'content': react_for_python_developers.layout,
        'name': 'React for Python Developers',
        'description': 'A tutorial on how to program in React and JavaScript for Python developers.'
    },
    'loading-states': {
        'url': '/loading-states',
        'content': loading_states.layout,
        'name': 'Loading States',
        'description': 'Getting the loading state of a component and adding a loading component'
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

    'button-examples': {
        'url': '/dash-core-components/button',
        'content': examples.Button,
        'name': 'Button Component',
        'description': 'Button examples, properties, and reference.'
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

    'graphs-example': {
        'url': '/dash-core-components/graph',
        'content': examples.Graphs,
        'name': 'Graphs',
        'description': 'Graph examples, properties, and reference.'
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

    'location-examples': {
        'url': '/dash-core-components/location',
        'content': examples.Location,
        'name': 'Location Component',
        'description': 'Location examples, properties, and reference.'
    },

### Dash DAQ Components ###
    'booleanswitch-examples': {
        'url': '/dash-daq/booleanswitch',
        'content': daq_examples.BooleanSwitch,
        'name': 'Boolean Switch Component',
        'description': 'Boolean switch examples, properties, and reference.'
    },

    'colorpicker-examples': {
        'url': '/dash-daq/colorpicker',
        'content': daq_examples.ColorPicker,
        'name': 'Color Picker Switch Component',
        'description': 'Color picker examples, properties, and reference.'
    },

    'gauge-examples': {
        'url': '/dash-daq/gauge',
        'content': daq_examples.Gauge,
        'name': 'Gauge Component',
        'description': 'Gauge examples, properties, and reference.'
    },

    'graduatedbar-examples': {
        'url': '/dash-daq/graduatedbar',
        'content': daq_examples.GraduatedBar,
        'name': 'Graduated bar Component',
        'description': 'Graduated bar examples, properties, and reference.'
    },

    'indicator-examples': {
        'url': '/dash-daq/indicator',
        'content': daq_examples.Indicator,
        'name': 'Indicator Component',
        'description': 'Indicator examples, properties, and reference.'
    },

    'joystick-examples': {
        'url': '/dash-daq/joystick',
        'content': daq_examples.Joystick,
        'name': 'Joystick Component',
        'description': 'Joystick examples, properties, and reference.'
    },

    'knob-examples': {
        'url': '/dash-daq/knob',
        'content': daq_examples.Knob,
        'name': 'Knob Component',
        'description': 'Knob examples, properties, and reference.'
    },

    'leddisplay-examples': {
        'url': '/dash-daq/leddisplay',
        'content': daq_examples.LEDDisplay,
        'name': 'LED display Component',
        'description': 'LED display examples, properties, and reference.'
    },

    'numericinput-examples': {
        'url': '/dash-daq/numericinput',
        'content': daq_examples.NumericInput,
        'name': 'Numeric input Component',
        'description': 'Numeric input examples, properties, and reference.'
    },

    'powerbutton-examples': {
        'url': '/dash-daq/powerbutton',
        'content': daq_examples.PowerButton,
        'name': 'Power button Component',
        'description': 'Power button examples, properties, and reference.'
    },

    'precisioninput-examples': {
        'url': '/dash-daq/precisioninput',
        'content': daq_examples.PrecisionInput,
        'name': 'Precision input Component',
        'description': 'Precision input examples, properties, and reference.'
    },

    'stopbutton-examples': {
        'url': '/dash-daq/stopbutton',
        'content': daq_examples.StopButton,
        'name': 'Stop button Component',
        'description': 'StopButton examples, properties, and reference.'
    },

    'daq-slider-examples': {
        'url': '/dash-daq/slider',
        'content': daq_examples.Slider,
        'name': 'Slider Component',
        'description': 'Slider examples, properties, and reference.'
    },

    'tank-examples': {
        'url': '/dash-daq/tank',
        'content': daq_examples.Tank,
        'name': 'Tank Component',
        'description': 'Tank examples, properties, and reference.'
    },

    'thermometer-examples': {
        'url': '/dash-daq/thermometer',
        'content': daq_examples.Thermometer,
        'name': 'Thermometer Component',
        'description': 'Thermometer examples, properties, and reference.'
    },

    'toggleswitch-examples': {
        'url': '/dash-daq/toggleswitch',
        'content': daq_examples.ToggleSwitch,
        'name': 'Toggle switch Component',
        'description': 'Toggle switch examples, properties, and reference.'
    },

    'darkthemeprovider-examples': {
        'url': '/dash-daq/darkthemeprovider',
        'content': daq_examples.DarkThemeProvider,
        'name': 'Dark theme provider Component',
        'description': 'Dark theme provider examples, properties, and reference.'
    },

    # Dash Bio examples

    'sequenceviewer-examples': {
        'url': '/dash-bio/sequenceviewer',
        'content': dashbio_examples.SequenceViewer,
        'name': 'Sequence Viewer Component',
        'description': 'Sequence viewer examples, properties, and reference.'
    },

    'alignmentchart-examples': {
        'url': '/dash-bio/alignmentchart',
        'content': dashbio_examples.AlignmentChart,
        'name': 'Alignment Chart Component',
        'description': 'Alignment Chart examples, properties, and reference.'
    },

    'clustergram-examples': {
        'url': '/dash-bio/clustergram',
        'content': dashbio_examples.Clustergram,
        'name': 'Clustergram Component',
        'description': 'Clustergram examples, properties, and reference.'
    },

    'speck-examples': {
        'url': '/dash-bio/speck',
        'content': dashbio_examples.Speck,
        'name': 'Speck Component',
        'description': 'Speck examples, properties, and reference.'
    },

    'circos-examples': {
        'url': '/dash-bio/circos',
        'content': dashbio_examples.Circos,
        'name': 'Circos Component',
        'description': 'Circos examples, properties, and reference.'
    },

    'ideogram-exmaples': {
        'url': '/dash-bio/ideogram',
        'content': dashbio_examples.Ideogram,
        'name': 'Ideogram Component',
        'description': 'Ideogram examples, properties, and reference.'
    },

    'molecule-2d-examples': {
        'url': '/dash-bio/molecule2dviewer',
        'content': dashbio_examples.Molecule2dViewer,
        'name': 'Molecule 2D Component',
        'description': 'Molecule2D examples, properties, and reference.'
    },

    'molecule-3d-examples': {
        'url': '/dash-bio/molecule3dviewer',
        'content': dashbio_examples.Molecule3dViewer,
        'name': 'Molecule 3D Component',
        'description': 'Molecule3D examples, properties, and reference.'
    },

    'needle-plot-examples': {
        'url': '/dash-bio/needleplot',
        'content': dashbio_examples.NeedlePlot,
        'name': 'Needle Plot Component',
        'description': 'NeedlePlot examples, properties, and reference.'
    },

    'manhattan-plot-examples': {
        'url': '/dash-bio/manhattanplot',
        'content': dashbio_examples.ManhattanPlot,
        'name': 'Manhattan Plot Component',
        'description': 'ManhattanPlot examples, properties, and reference.'
    },

    'volcano-plot-examples': {
        'url': '/dash-bio/volcanoplot',
        'content': dashbio_examples.VolcanoPlot,
        'name': 'Volcano Plot Component',
        'description': 'VolcanoPlot examples, properties, and reference.'
    },

    'onco-print-examples': {
        'url': '/dash-bio/oncoprint',
        'content': dashbio_examples.OncoPrint,
        'name': 'OncoPrint Component',
        'description': 'Oncoprint examples, properties, and reference.'
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

    'static-assets-examples': {
        'url': '/dash-deployment-server/static-assets',
        'content': dds_examples.staticAssets,
        'name': 'Adding Static Assets',
        'description': 'Learn how to include custom CSS, JS, and images with the `assets` directory.'
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
        'name': 'Dash Enterprise Auth Features',
        'description': 'Accessing User Authentication Data in your Dash App'
    },

    'app-privacy': {
        'url': '/dash-deployment-server/privacy',
        'content': dds_examples.AppPrivacy,
        'name': 'Dash App Privacy',
        'description': 'Dash App Privacy and Managing Collaborators'
    },

    'deployment-checks': {
        'url': '/dash-deployment-server/checks',
        'content': dds_examples.Checks,
        'name': 'Dash Deployment Health Checks',
        'description': 'Create custom checks to ensure that a newly deployed app can serve traffic.'
    },

    'private-packages-examples': {
        'url': '/dash-deployment-server/private-packages',
        'content': dds_examples.PrivatePackages,
        'name': 'Adding Private Python Packages',
        'description': 'Intsall private python packages in your Dash Apps.'
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
        'url': '/dash-deployment-server/environment-variables',
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

    'pdf-service-examples': {
        'url': '/dash-deployment-server/pdf-service',
        'content': dds_examples.pdfService,
        'name': 'Dash Deployment Server PDF Service',
        'description': 'Utilize the Dash Deployment Server API endpoint for '
        'creating PDF exports of your Dash applications'
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

    'git-examples': {
        'url': '/dash-deployment-server/git',
        'content': dds_examples.Git,
        'name': 'Advanced Git',
        'description': 'A reference for git commands and how they are used '
        'with Dash Deployment Server.'
    },

    'dds-portal': {
        'url': '/dash-deployment-server/portal',
        'content': dds_examples.Portal,
        'name': 'Dash App Portal',
        'description': 'Learn about the Dash App Portal '
    },
### End Dash Deployment Server ###

### Start DataTable Docs

    'datatable-sizing': {
        'url': '/datatable/sizing',
        'content': tutorial.table.sizing_chapter.layout,
        'name': 'Sizing - DataTable',
        'description': """
            All about sizing the DataTable.
            Examples on how to change the width and height of the table,
            the widths of the individual columns columns, handling
            text overflow, and more.
        """
    },

    'datatable-styling': {
        'url': '/datatable/style',
        'content': tutorial.table.styling_chapter.layout,
        'name': 'Style - DataTable',
        'description': """
            All about styling the DataTable.
            Examples on how to change the colors, conditional formatting,
            styling the table as a list view, and more.
        """
    },

    'interactivity': {
        'url': '/datatable/interactivity',
        'content': tutorial.table.interactivity_chapter.layout,
        'name': 'Interactive DataTable',
        'description': '''
        A showcase of the interactive features of the DataTable.
        '''
    },

    'recipes': {
        'url': '/datatable/editable',
        'content': tutorial.table.editing_recipes_chapter.layout,
        'name': 'Editable DataTable',
        'description': '''
        DataTable as a Spreadsheet: examples for determining which
        cell has changed, filtering null values, adding or removing
        columns, and more.
        '''
    },

    'callbacks': {
        'url': '/datatable/callbacks',
        'content': tutorial.table.table_callbacks_chapter.layout,
        'name': 'Python-Driven Filtering, Paging, Sorting - DataTable',
        'description': '''
        Examples on filtering, sorting, and paging data with Python.
        '''
    },

    'typing': {
        'url': '/datatable/typing',
        'content': tutorial.table.table_typing_chapter.layout,
        'name': 'Typing and User Input Processing',
        'description': '''
        Column typing and user input validation, coercing, defaulting.
        '''
    },

    'dropdowns': {
        'url': '/datatable/dropdowns',
        'content': tutorial.table.dropdowns_chapter.layout,
        'name': 'Dropdowns Inside DataTable',
        'description': '''
        Learn how to embed dropdowns inside the DataTable.
        '''
    },

    'virtualization': {
        'url': '/datatable/virtualization',
        'content': tutorial.table.virtualization_chapter.layout,
        'name': 'Virtualization',
        'description': '''
        Examples using DataTable virtualization.
        '''
    },

    'filtering': {
        'url': '/datatable/filtering',
        'content': tutorial.table.filtering_chapter.layout,
        'name': 'Filtering Syntax',
        'description': '''
        Reference for frontend and backend filtering syntax for the DataTable.
        '''
    },

    'roadmap': {
        'url': '/datatable/reference',
        'content': tutorial.table.reference_chapter.layout,
        'name': 'DataTable Reference',
        'description': '''
        A comprehensive list of all of the DataTable properties.
        '''
    },

### End DataTable Docs

### Start Cytoscape Docs

    'cytoscape-elements': {
        'url': '/cytoscape/elements',
        'content': tutorial.cytoscape.elements_chapter.layout,
        'name': 'Cytoscape Elements',
        'description': '''
        Overview of element declaration and manipulation.
        '''
    },

    'cytoscape-layout': {
        'url': '/cytoscape/layout',
        'content': tutorial.cytoscape.layout_chapter.layout,
        'name': 'Cytoscape Layouts',
        'description': '''
        Description of built-in layouts, and how to modify their properties.
        '''
    },

    'cytoscape-styling': {
        'url': '/cytoscape/styling',
        'content': tutorial.cytoscape.styling_chapter.layout,
        'name': 'Cytoscape Styling',
        'description': '''
        Methods to style elements with a CSS-like syntax.
        '''
    },

    'cytoscape-callbacks': {
        'url': '/cytoscape/callbacks',
        'content': tutorial.cytoscape.callbacks_chapter.layout,
        'name': 'Cytoscape Callbacks',
        'description': '''
        Methods to combine Dash callbacks to update your Cytoscape object.
        '''
    },

    'cytoscape-events': {
        'url': '/cytoscape/events',
        'content': tutorial.cytoscape.events_chapter.layout,
        'name': 'Cytoscape events',
        'description': '''
        Overview of user-interaction events that trigger callbacks in Dash,
        and how to use them to update the Cytoscape component.
        '''
    },

    'cytoscape-biopython': {
        'url': '/cytoscape/biopython',
        'content': tutorial.cytoscape.applications_chapter.layout,
        'name': 'Cytoscape with Biopython',
        'description': '''
        Examples of applications in bioinformatics using Biopython.
        '''
    },

    'cytoscape-reference': {
        'url': '/cytoscape/reference',
        'content': tutorial.cytoscape.reference_chapter.layout,
        'name': 'Cytoscape Reference',
        'description': '''
        Comprehensive list of all of the Cytoscape properties.
        '''
    },

### End Cytoscape Docs

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
    },

    'store-examples': {
        'url': '/dash-core-components/store',
        'content': examples.Store,
        'name': 'Store component',
        'description': 'Store examples, properties and reference'
    },

    'devtools': {
        'url': '/devtools',
        'content': devtools.layout,
        'name': 'Dev tools',
        'description': 'Dash dev tools reference'
    },

    'testing': {
        'url': '/testing',
        'content': testing.layout,
        'name': 'Dash Testing',
        'description': '(New in Dash 1.0!) An introduction to testing your dash app with selenium'
    },

    'logout-button': {
        'url': '/dash-core-components/logout_button',
        'content': examples.LogoutButton,
        'name': 'Logout button',
        'description': 'LogoutButton examples, properties and reference'
    },

    'loading-component': {
        'url': '/dash-core-components/loading_component',
        'content': examples.LoadingComponent,
        'name': 'Loading component',
        'description': 'Loading component examples, properties and reference'
    }

}
