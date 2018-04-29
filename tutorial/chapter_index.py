import auth
import core_component_examples as examples
import core_components
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
        'name': 'External CSS and JS',
        'description': 'By default, Dash loads CSS and JS assets from a ' \
                       'fast, global CDN - but you can optionally these ' \
                       'resources locally, making your apps completely self ' \
                       'contained (no internet access required!). Also, ' \
                       'learn how to append your own CSS styleseets or JS ' \
                       'scripts to your apps.'
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

    'deployment-onpremise': {
        'url': '/deployment/on-premise',
        'content': on_premise_deployment.layout,
        'name': 'Deploying Dash Apps on Plotly On-Premises',
        'description': "Plotly On-Premises is Plotly's commercial " \
                       "offering for hosting and sharing Dash apps."
    },

    'support': {
        'url': '/support',
        'content': support.layout,
        'name': 'Support and Contact',
        'description': 'More information for Dash demos, On-Premise trials, ' \
                       'Dash workshops, sponsored feature requests and ' \
                       'customizations.'
    },
### End of home.py ###

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

    'search': {
        'url': '/search',
        'content': search.layout,
        'name': '',
        'description': 'Search the Dash Docs'
    },
}
