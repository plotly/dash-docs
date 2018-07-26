# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent as s

import styles
from tools import load_example, read_file


examples = {
    'local-css': load_example(
        'tutorial/examples/external_css_and_js/local-css.py'
    ),
    'custom-index-string': read_file(
        'tutorial/examples/external_css_and_js/custom-index-string.py'
    ),
    'custom-interpolate-string': read_file(
        'tutorial/examples/external_css_and_js/custom-interpolate-string.py'
    ),
    'dash-meta-tags': read_file(
        'tutorial/examples/external_css_and_js/dash-meta-tags.py'
    ),

}


layout = html.Div([
    html.H1('Adding Local CSS & JS and Overriding the Page-Load Template'),

    dcc.Markdown(s('''
    Dash applications are rendered in the web browser with CSS and JavaScript.
    On page load, Dash serves a small HTML template that includes references to
    the CSS and JavaScript that are required to render the application.
    This chapter covers everything that you need to know about configuring
    this HTML file and about including external CSS and JavaScript in Dash
    applications.

    **Table of Contents**
    - Adding Your Own CSS and JavaScript to Dash Apps
    - Customizing Dash's HTML Index Template
    - Adding Meta Tags
    - Serving Dash's Component Libraries Locally or from a CDN
    - Sample Dash CSS Stylesheet
    ***

    ## Adding Your Own CSS and JavaScript to Dash Apps

    **New in dash 0.22.0**

    Including custom CSS or JavaScript in your Dash apps is simple.
    Just create a folder named `assets` in the root of your app directory
    and include your CSS and JavaScript
    files in that folder. Dash will automatically serve all of the files that
    are included in this folder.

    ### Example: Including Local CSS and JavaScript

    We'll create several files: `app.py`, a folder named `assets`, and
    three files in that folder:
    ```
    - app.py
    - assets/
        |-- typography.css
        |-- header.css
        |-- custom-script.js


    ```

    `app.py`

    ''')),

    dcc.SyntaxHighlighter(
        examples['local-css'][0],
        language='python',
        customStyle=styles.code_container
    ),

    html.Hr(),

    html.Div(
        dcc.Markdown('`typography.css`'),
        style={'paddingTop': 20}
    ),

    dcc.SyntaxHighlighter(
        s('''body {
    font-family: sans-serif;
}
h1, h2, h3, h4, h5, h6 {
    color: hotpink
}
        '''),
        language='css',
        customStyle=styles.code_container
    ),

    html.Hr(),

    html.Div(
        dcc.Markdown('`header.css`'),
        style={'paddingTop': 20}
    ),

    dcc.SyntaxHighlighter(
        s('''.app-header {
    height: 60px;
    line-height: 60px;
    border-bottom: thin lightgrey solid;
}

.app-header .app-header--title {
    font-size: 22px;
    padding-left: 5px;
}
        '''),
        language='css',
        customStyle=styles.code_container
    ),

    html.Hr(),

    html.Div(
        dcc.Markdown('`custom-script.js`'),
        style={'paddingTop': 20}
    ),

    dcc.SyntaxHighlighter(
        s('''
        alert('If you see this alert, then your custom JavaScript script has run!')
        '''),
        language='javascript',
        customStyle=styles.code_container
    ),

    html.Hr(),

    dcc.Markdown(s('''
        When you run `app.py`, your app should look something like this:
        (Note that there may be some slight differences in appearance as
        the CSS from this Dash User Guide is applied to all of these embedded
        examples.)
    ''')),

    html.Div(
        examples['local-css'][1],
        className='css-example',
        style={
            'border': 'thin lightgrey solid',
            'marginTop': 40,
            'marginBottom': 40,
        }
    ),

    dcc.Markdown(s('''

    There are a few things to keep in mind when including assets automatically:
    1 - Currently, the files are automatically cached by the browser. So, if
    you make changes to the file you may need to disable your browser's cache.
    [Learn how to disable your browser cache](https://stackoverflow.com/questions/5690269/).
    Note that we plan on fixing this issue, [track our progress in dash#303](https://github.com/plotly/dash/issues/303).

    2 - The following file types will automatically be included:
        - CSS files suffixed with `.css`
        - JavaScript files suffixed with `.js`
        - A single file named `favicon.io` (the page tab's icon)

    3 - Dash will include the files in alphanumerical order by filename.
    So, we recommend prefixing your filenames with numbers if you need to ensure
    their order (e.g. `10_typography.css`, `20_header.css`)

    4 - If you want to include CSS from a remote URL, then we recommend
    overriding the app's HTML template, as described in the next section.
    We are working on an easier method for including remote CSS urls in
    [dash#302](https://github.com/plotly/dash/issues/302)

    5 - Your custom CSS will be included _after_ the Dash component CSS

    ***

    ## Customizing Dash's HTML Index Template

    **New in dash 0.22.0**

    Dash's UI is generated dynamically with Dash's React.js front-end. So,
    on page load, Dash serves a very small HTML template string that includes
    the CSS and JavaScript that is necessary to render the page and some simple
    HTML meta tags.

    This simple HTML string is customizable. You might want to customize this
    string if you wanted to:
    - Include a different `<title>` for your app (the `<title>` tag is the name
    that appears in your brower's tab. By default, it is "Dash")
    - Customize the way that your CSS or JavaScript is included in the page.
    For example, if you wanted to include remote scripts or if you wanted to
    include the CSS _before_ the Dash component CSS
    - Include custom meta tags in your app. Note that meta tags can also be
    added with the `meta_tags` argument (example below).

    #### Usage

    **Option 1 - `index_string`**

    Add an `index_string` to modify the default HTML Index Template:

    ''')),

    dcc.SyntaxHighlighter(
        examples['custom-index-string'],
        language='python',
        customStyle=styles.code_container
    ),

    dcc.Markdown(s('''

    The `{%key%}`s are template variables that Dash will fill in automatically
    with default properties. The available keys are:

    `{%metas%}` (optional)

    The registered meta tags included by the `meta_tags` argument in `dash.Dash`

    `{%favicon%}` (optional)

    A favicon link tag if found in the `assets` folder.

    `{%css%}` (optional)

    `<link/>` tags to css resources. These resources include the Dash component
    library CSS resources as well as any CSS resources found in the `assets` folder.

    `{%title%}` (optional)

    The contents of the page `<title>` tag.
    [Learn more about `<title/>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)

    `{%config%}` (required)

    An auto-generated tag that includes configuration settings passed from
    Dash's backend to Dash's front-end (`dash-renderer`).

    `{%app_entry%}` (required)

    The container in which the Dash layout is rendered.

    `{%scripts%}` (required)

    The set of JavaScript scripts required to render the Dash app.
    This includes the Dash component JavaScript files as well as any
    JavaScript files found in the `assets` folder.

    **Option 2 - `interpolate_index`**

    If your HTML content isn't static or if you would like to introspect or modify
    the templated variables, then you can override the `Dash.interpolate_index`
    method.
    ''')),

    dcc.SyntaxHighlighter(
        examples['custom-interpolate-string'],
        language='python',
        customStyle=styles.code_container
    ),

    dcc.Markdown(s('''
    Unlike the `index_string` method, where we worked with template string
    variables, the keyword variables that are passed into `interpolate_index`
    are already evaluated.
    ''')),

    dcc.Markdown(s('''

    In the example above, when we print the input arguments of
    `interpolate_index` we should see an output like this:
    ''')),

    html.Div(dcc.Markdown("""
```
{
    'title': 'Dash',
    'app_entry': '\\n<div id="react-entry-point">\\n    <div class="_dash-loading">\\n        Loading...\\n    </div>\\n</div>\\n',
    'favicon': '',
    'metas': '<meta charset="UTF-8"/>',
    'scripts': '<script src="https://unpkg.com/react@15.4.2/dist/react.min.js"></script>\\n<script src="https://unpkg.com/react-dom@15.4.2/dist/react-dom.min.js"></script>\\n<script src="https://unpkg.com/dash-html-components@0.11.0/dash_html_components/bundle.js"></script>\\n<script src="https://unpkg.com/dash-renderer@0.13.0/dash_renderer/bundle.js"></script>',
    'config': '<script id="_dash-config" type="application/json">{"requests_pathname_prefix": "/", "url_base_pathname": "/"}</script>',
    'css': ''
}
```"""), style={'overflowX': 'scroll'}),
    dcc.Markdown(s('''
    The values of the `scripts` and `css` keys may be different depending on
    which component libraries you have included or which files
    might be in your assets folder.

    ***

    ## Customizing Meta Tags

    > Not sure what meta tags are?
    > [Check out this tutorial on meta tags and why you might want to use them](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML).

    To add custom meta tags to your application, you can always override Dash's
    HTML Index Template. Alternatively, Dash provides a shortcut:
    you can specify meta tags directly in the Dash constructor:
    ''')),

    dcc.SyntaxHighlighter(
        examples['dash-meta-tags'],
        language='python',
        customStyle=styles.code_container
    ),

    dcc.Markdown(s('''

    If you inspect the source of your app, you should see the meta tags appear:
    ![Dash App with Custom Meta Tags](https://user-images.githubusercontent.com/1280389/43233036-cd050eae-9028-11e8-910e-f0d140c37e4c.png)

    ***

    ## Serving Dash's Component Libraries Locally or from a CDN

    Dash's component libraries, like `dash_core_components` and `dash_html_components`,
    are bundled with JavaScript and CSS files. Dash automatically checks with
    component libraries are being used in your application and will automatically
    serve these files in order to render the application.

    By default, dash serves the JavaScript and CSS resources from the
    online CDNs. This is usually much faster than loading the resources
    from the file system.

    However, if you are working in an offline or firewalled environment or
    if the CDN is unavailable, then your dash app itself can serve these
    files. These files are stored as part of the component's site-packages
    folder.

    Here's how to enable this option:

    ''')),

    dcc.SyntaxHighlighter('''from dash import Dash

app = Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True''',
        language='python',
        customStyle={'borderLeft': 'thin lightgrey solid'}
    ),

    dcc.Markdown(s('''

    Note that in the future, we will likely make "offline" the default option.
    [Follow dash#284](https://github.com/plotly/dash/issues/284) for more information.

    ***

    ## Sample Dash CSS Stylesheet

    Currently, Dash does not include styles by default.

    To get started with Dash styles, we recommend starting with this [CSS stylesheet](https://codepen.io/chriddyp/pen/bWLwgP?editors=1100) hosted
    on [Codepen](https://codepen.io).

    To include this stylesheet in your application, copy and paste it into a file
    in your `assets` folder. You can view the raw CSS source here:
    [https://codepen.io/chriddyp/pen/bWLwgP.css](https://codepen.io/chriddyp/pen/bWLwgP.css).

    Here is an embedded version of this stylesheet.
    ''')),

    html.Iframe(
        src="//codepen.io/chriddyp/embed/bWLwgP/?height=265&"
            "theme-id=light&default-tab=css,result&embed-version=2",
        style={'height': 400, 'width': '100%', 'border': 'none'}
    )
])
