library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dash_docs/utils.R', local=utils)

examples <- list(
  local_css = utils$LoadExampleCode('dash_docs/chapters/external_resources/examples/local-css.R'),
  folderHost = utils$LoadExampleCode('dash_docs/chapters/external_resources/examples/folderHost.R'),
  embeddingImages = utils$LoadExampleCode('dash_docs/chapters/external_resources/examples/embeddingImages.R'),
  addingExternalCSS = utils$LoadExampleCode('dash_docs/chapters/external_resources/examples/addingExternalCSS.R'),
  custom_index_string = utils$LoadExampleCode('dash_docs/chapters/external_resources/examples/custom-index-string.R')
)

layout <- htmlDiv(list(
  htmlH1('Adding CSS & JS and Overriding the Page-Load Template'),
  dccMarkdown("
Dash applications are rendered in the web browser with CSS and JavaScript.
On page load, Dash serves a small HTML template that includes references to
the CSS and JavaScript that are required to render the application.
This chapter covers everything that you need to know about configuring
this HTML file and about including external CSS and JavaScript in Dash
applications.

**Table of Contents**
- Adding Your Own CSS and JavaScript to Dash Apps
- Embedding Images in Your Dash Apps
- Adding External CSS and JavaScript
- Customizing Dash's HTML Index Template
- Adding Meta Tags
- Serving Dash's Component Libraries Locally or from a CDN
- Sample Dash CSS Stylesheet
- Syntax Highlighting with Markdown
***
"),
  htmlH2('Adding Your Own CSS and JavaScript to Dash Apps'),
  dccMarkdown("
Including custom CSS or JavaScript in your Dash apps is simple.
Just create a folder named `assets` in the root of your app directory
and include your CSS and JavaScript
files in that folder. Dash will automatically serve all of the files that
are included in this folder. By default the url to request the assets will
be `/assets` but you can customize this with the `assets_url_path` argument
to `Dash`.

### Example: Including Local CSS and JavaScript

We'll create several files: `app.r`, a folder named `assets`, and
three files in that folder:
```
- app.r
- assets/
    |-- typography.css
    |-- header.css
    |-- custom-script.js
```

`app.r`
  "),
  examples$local_css$source_code,
    htmlDiv(
    dccMarkdown('`typography.css`'),
    style=list('paddingTop' = 20)
  ),
  
  htmlHr(),
  dccMarkdown("
body {
    font-family: sans-serif;
}
h1, h2, h3, h4, h5, h6 {
    color: hotpink
}
"),
 htmlHr(),

 htmlDiv(
  dccMarkdown('`header.css`'),
  style=list('paddingTop' = 20)
),

 dccMarkdown(
  "app-header {
    height: 60px;
    line-height: 60px;
    border-bottom: thin lightgrey solid;
}

.app-header .app-header--title {
    font-size: 22px;
    padding-left: 5px;
}
"
),

 htmlHr(),
 htmlDiv(
  dccMarkdown('`custom-script.js`'),
  style=list('paddingTop' = 20)
),
dccMarkdown("
alert('If you see this alert, then your custom JavaScript script has run!')
"
),
htmlHr(),

dccMarkdown("
When you run `app.r`, your app should look something like this:
(Note that there may be some slight differences in appearance as
the CSS from this Dash User Guide is applied to all of these embedded
examples.)
    "),
examples$local_css$layout,
htmlHr(),

dccMarkdown("
There are a few things to keep in mind when including assets automatically:

1 - The following file types will automatically be included:
            
  - CSS files suffixed with .css
            
  - JavaScript files suffixed with .js
            
  - A single file named favicon.ico (the page tab's icon)
            
2 - Dash will include the files in alphanumerical order by filename. 
So, we recommend prefixing your filenames with numbers if you need to ensure their order
(e.g. 10_typography.css, 20_header.css)
            
3 - You can ignore certain files in your assets folder with a regex filter using 
`app <- Dash$new(assets_ignore = '.*ignored.*').`
This will prevent Dash from loading files which contain the above pattern.
            
4 - If you want to include CSS from a remote URL, 
then see the next section.
            
5 - Your custom CSS will be included after the 
Dash component CSS
"),

 htmlH3("Hot Reloading"),
 dccMarkdown("
By default, Dash includes \"hot-reloading\". 
This means that Dash will automatically refresh your browser 
when you make a change in your Python code and your CSS code.

Give it a try: Change the color in typography.css from \"hotpink\" 
to \"orange\" and see your application update.
"),
 
 htmlH3("Load Assets from a Folder Hosted on a CDN"),
 dccMarkdown("
If you duplicate the file structure of your local assets folder 
to a folder hosted externally to your Dash app, 
you can use `assets_url_path = 'http://your-external-assets-folder-url'` in the Dash constructor to load the files from there instead of locally. 
Dash will index your local assets folder to find all of your assets, map their relative path onto assets_external_path and then request the resources from there. 
app.scripts.config.serve_locally = False must also be set in order for this to work.

**Example:**
"),

examples$folderHost$source_code,

dccMarkdown("
## Embedding Images in Your Dash Apps

In addition to CSS and javascript files, you can include images in the assets folder. 
An example of the folder structure:

```
- app.r
- assets/
    |-- image.png
```
In your app.r file you can use the relative path to that image:
            "),

examples$embeddingImages$source_code,

dccMarkdown("
## Adding external CSS/JavaScript

You can add resources hosted externally to your Dash app with the
`external_stylesheets/stylesheets` init keywords.

The resources can be either a string or 
a list containing the tag attributes (`src`, `integrity`, `crossorigin`, etc).
You can mix both.
            
External CSS/JavaScript files are loaded before the assets.
            "),

examples$addingExternalCSS$source_code,

dccMarkdown("
## Customizing Dash's HTML Index Template

Dash's UI is generated dynamically with Dash's React.js front-end. 
So, on page load, Dash serves a very small HTML template string that 
includes the CSS and JavaScript that is necessary to render the page 
and some simple HTML meta tags.
            
This simple HTML string is customizable. 
You might want to customize this string if you wanted to:

- Include a different <title> for your app 
(the <title> tag is the name that appears in your brower's tab. 
By default, it is \"dash\")

- Customize the way that your CSS or JavaScript is included in the page. 
For example, if you wanted to include remote scripts or if you wanted to 
include the CSS before the Dash component CSS

### Usage

Add an `index_string` to modify the default HTML Index Template:

```
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

external_stylesheets <- list(
  list('https://codepen.io/chriddyp/pen/bWLwgP.css')
)
app <- Dash$new(external_stylesheets = external_stylesheets)

string <- \"
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        <div>My Custom header</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>My Custom footer</div>
    </body>
</html>
\"
app$index_string <- string

app$layout(htmlDiv('Simple Dash App'))

app$run_server()
```

The `{%key%}`s are template variables that Dash will fill in automatically with default properties. The available keys are:

`{%favicon%}` (optional)
            
A favicon link tag if found in the `assets` folder.
            
`{%css%}` (optional)
            
`<link/>` tags to css resources. 
These resources include the Dash component library CSS resources 
as well as any CSS resources found in the `assets` folder.
            
`{%title%}` (optional)
            
The contents of the page `<title>` tag. Learn more about `<title/>`
            
`{%config%}` (required)
            
An auto-generated tag that includes configuration settings 
passed from Dash's backend to Dash's front-end (`dash-renderer`).
            
`{%app_entry%}` (required)
            
The container in which the Dash layout is rendered.
            
`{%scripts%}` (required)
            
The set of JavaScript scripts required to render the Dash app. 
This includes the Dash component JavaScript files as well as 
any JavaScript files found in the assets folder.
            
`{%renderer%}` (required)
          
The JavaScript script that instantiates dash-renderer 
by calling new `DashRenderer()`
            "),

dccMarkdown("
## Customizing Meta Tags

To add custom meta tags to your application, you can always override Dash's HTML Index Template. Alternatively, Dash provides a shortcut: you can specify meta tags directly in the Dash constructor:
```
library(dash)
library(dashHtmlComponents)

app <- Dash$new(meta_tags = list(
    # A description of the app, used by e.g.
    # search engines when displaying search results.
    list(
      name = 'description',
      content = 'my description'
    ),
    # A tag that tells Internet Explorer (IE)
    # to use the latest renderer version available
    # to that browser (e.g. Edge)
    list(
      `http-equiv` = 'X-UA-Compatible',
      content = 'IE=edge'
    ),
    # A tag that tells the browser not to scale
    # desktop widths to fit mobile screens.
    # Sets the width of the viewport (browser)
    # to the width of the device, and the zoom level
    # (initial scale) to 1.
    #
    # Necessary for 'true' mobile support.
    list(
      name = 'viewport',
      content = 'width=device-width, initial-scale=1.0'
    )
  )
)

app$layout(
  htmlDiv(
    'Simple Dash App'
  )
)

app$run_server(debug=TRUE)
```
              "),

dccMarkdown("
## Serving Dash's Component Libraries Locally or from a CDN

Dash's component libraries, like `dashCoreComponents` and `dashHtmlComponents`, are bundled with JavaScript and CSS files. Dash automatically checks with component libraries are being used in your application and will automatically serve these files in order to render the application.
By default, Dash serves the JavaScript and CSS resources from the local files on the server where Dash is running. This is the more flexible and robust option: in some cases, such as firewalled or airgapped environments, it is the only option. It also avoids some hard-to-debug problems like packages that have not been published to NPM or CDN downtime, and the unlikely but possible scenario of the CDN being hacked. And of course, component developers will want the local version while changing the code, so when dev bundles are requested (such as with `debug=TRUE`) we always serve locally.
However, for performance-critical apps served beyond an intranet, online CDNs can often deliver these files much faster than loading the resources from the file system, and will reduce the load on the Dash server.
```
library(dash)

app <- Dash$new(serve_locally=FALSE)
```
This will load the bundles from the [https://unpkg.com/](https://unpkg.com) CDN which is a community-maintained project that serves JavaScript bundles from NPM. We don't maintain it, so we cannot attest or guarantee to its uptime, performance, security, or long term availability.
              "),

dccMarkdown("
## Syntax Highlighting With Markdown

Both `dashTable` and `dashCoreComponents` support markdown formatting; this includes syntax highlighting for inline code.

Highlighting is taken care of by [highlight.js](https://highlightjs.org/). By default, only certain languages are recognized, and there is only one color scheme available. However, you can override this by downloading a custom `highlight.js` package. To do this, visit [https://highlightjs.org/download/](https://highlightjs.org/download/), and in the 'Custom package' section, check off all of the languages that you require, download your package, and place the resultant `highlight.pack.js` file into the `assets/` folder for your app. The package should also come with a `styles/` directory; to use a different color scheme, simply copy the corresponding stylesheet into your app's `assets/` folder.

              "),

dccMarkdown("
[Back to the Table of Contents](/)
              ")
))
