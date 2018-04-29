# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([

    dcc.Markdown('''
    # External CSS and JavaScript

    The component libraries that you use with dash, like `dash_core_components`
    and `dash_html_components`, include JavaScript and CSS bundles. Dash
    automatically checks which JavaScript and CSS bundles are necessary
    to render the application.

    Some of this functionality is customizable and extendable.

    ***

    ## Including custom CSS and JavaScript in your Dash app
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter('''from dash import Dash

app = Dash()

# Append an externally hosted CSS stylesheet
my_css_url = "https://unpkg.com/normalize.css@5.0.0"
app.css.append_css({
    "external_url": my_css_url
})

# Append an externally hosted JS bundle
my_js_url = 'https://unkpg.com/some-npm-package.js'
app.scripts.append_script({
    "external_url": my_js_url
})''', language='python', customStyle={'borderLeft': 'thin solid lightgrey'}),

    dcc.Markdown('''
    Dash currently only supports loading CSS and JavaScript bundles
    that are externally hosted.

    ***

    ### Default Styles

    Currently, Dash does not include styles by default.

    In future releases, Dash may include a default (removable) stylesheet.

    For now, you can use or fork this [CSS stylesheet](https://codepen.io/chriddyp/pen/bWLwgP?editors=1100) hosted
    on [Codepen](https://codepen.io).

    You can embed this stylesheet with this URL
    [https://codepen.io/chriddyp/pen/bWLwgP.css](https://codepen.io/chriddyp/pen/bWLwgP.css).

```
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
```

    Here is an embedded version of this stylesheet.
    '''.replace('    ', '')),

    html.Iframe(
        src="//codepen.io/chriddyp/embed/bWLwgP/?height=265&"
            "theme-id=light&default-tab=css,result&embed-version=2",
        style={'height': 400, 'width': '100%', 'border': 'none'}
    ),

    dcc.Markdown('''

    ***

    ## Rendering dash apps offline

    The JavaScript and CSS bundles that are included in
    Dash component libraries are hosted on the web
    (on the unpkg CDN) and in the Python packages that you install.

    By default, dash serves the JavaScript and CSS resources from the
    online CDNs. This is usually much faster than loading the resources
    from the file system.

    However, if you are working in an offline or firewalled environment or
    if the CDN is unavailable, then your dash app itself can serve these
    files. These files are stored as part of the component's site-packages
    folder.

    Here's how to enable this option:
    '''.replace('    ', '')),

    dcc.SyntaxHighlighter('''from dash import Dash

app = Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True''',
    language='python',
    customStyle={'borderLeft': 'thin lightgrey solid'})
])
