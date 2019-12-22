library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

layout <- htmlDiv(list(
  htmlH1('Deploying Dash Apps'),
  dccMarkdown("
By default, Dash apps run on `localhost` - you can only access them on your
own machine. To share a Dash app, you need to 'deploy' your Dash app to a
server and open up the server's firewall to the public or to a restricted
set of IP addresses.

## Dash Deployment Server

[Dash Deployment Server](https://plot.ly/dash/pricing/?_ga=2.218363033.1075922756.1562168385-916141078.1562168385) is Plotly's commercial product for deploying Dash
Apps on your company's servers or on AWS, Google Cloud, or Azure. It
offers an enterprise-wide Dash App Portal, easy git-based deployment,
automatic URL namespacing, built-in SSL support, LDAP authentication, and
more. [Learn more about Dash Deployment Server](https://plot.ly/dash/pricing?_ga=2.218363033.1075922756.1562168385-916141078.1562168385) or [get in touch to start a
trial](https://plotly.typeform.com/to/rkO85m?_ga=2.17487673.1075922756.1562168385-916141078.1562168385).

For existing customers, see the [Dash Deployment Server Documentation](https://dash.plot.ly/dash-deployment-server).

## Dash and Fiery

Dash apps are web applications. Dash uses Fiery as the web framework.
The underlying Fiery app is available at `app`, that is:

```r
    library(dash)

    app <- Dash$new()
```

## Heroku Example

Heroku is one of the easiest platforms for deploying and managing public web applications.

Here is a simple example. This example requires a Heroku account and `git`.

---

Step 1. Create a new folder for your project:

```
    $ mkdir dash_app_example
    $ cd dash_app_example
```

---

Step 2. Initialize the folder with `git`

```
    $ git init        # initializes an empty git repo
```

---

Step 3. Initialize the folder with a sample app (app.R), a .gitignore file, requirements.txt, and a Procfile for deployment

Create the following files in your project folder:

**`app.R`**

```r

    app <- Dash$new(external_stylesheets = list('https://codepen.io/chriddyp/pen/bWLwgP.css'))

    app$layout(htmlDiv(list(htmlH2('Hello World'),
              dccDropdown(id = 'dropdown',
              options = list(
                 list('label' = 'LA', 'value' = 'LA'),
                 list('label' = 'NYC', 'value' = 'NYC'),
                 list('label' = 'MTL', 'value' = 'MTL')
              ),
              value = 'LA'),
              htmlDiv(id = 'display-value'))
       )
    )

    app$callback(output=list(id='display-value', property='children'),
                 params=list(
      input(id='dropdown', property='value')),
      function(value)
      {
        sprintf('You have selected %s', value)
      }
    )

    app$run_server(debug = TRUE)
```

---

**`.gitignore`**

```
    venv
    *.pyc
    .DS_Store
    .env
```

---

**`Procfile`**

```
    web: R -f /app/app.R
```

---

**`init.R`**

`init.R` describes your R dependencies. A suggested initial
configuration is below; this avoids compilation issues with
`httpuv` on `heroku-16` by pinning package versions.

```r
    # R script to run author supplied code, typically used to install additional R packages
    # contains placeholders which are inserted by the compile script
    # NOTE: this script is executed in the chroot context; check paths!
    r <- getOption('repos')
    r['CRAN'] <- 'http://cloud.r-project.org'
    options(repos=r)

    # packages go here
    install.packages('remotes')

    # installs Rcpp, rlang, BH
    install.packages('later')

    install.packages('jsonlite')
    install.packages('listenv')

    # installs magrittr, promises, R6
    remotes::install_version('httpuv', version = '1.4.5.1', repos = 'http://cloud.r-project.org', upgrade='never')

    # installs crayon, digest, htmltools, mime, sourcetools, xtable
    remotes::install_version('shiny', version = '1.2.0', repos = 'http://cloud.r-project.org', upgrade='never')

    # installs askpass, assertthat, base64enc, cli, colorspace, crosstalk, curl, data.table, dplyr, fansi, ggplot2, glue, gtable, hexbin, htmlwidgets, httr, labeling, lattice, lazyeval, mgcv, munsell, nlme, openssl, pillar, pkgconfig, plogr, plyr, purrr, RColorBrewer, reshape2, scales, stringi, stringr, sys, tibble, tidyr, tidyselect, utf8, viridisLite, withr, yaml
    remotes::install_version('plotly', version = '4.9.0', repos = 'http://cloud.r-project.org', upgrade='never')

    install.packages('https://cloud.r-project.org/src/contrib/assertthat_0.2.1.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/xml2_1.2.0.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/triebeard_0.3.0.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/Archive/urltools/urltools_1.7.2.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/jsonlite_1.6.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/webutils_0.6.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/brotli_1.2.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/reqres_0.2.2.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/uuid_0.1-2.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/base64enc_0.1-3.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/codetools_0.2-16.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/globals_0.12.4.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/Archive/future/future_1.11.1.1.tar.gz', type='source', repos=NULL)

    # fiery and friends
    install.packages('https://cloud.r-project.org/src/contrib/routr_0.3.0.tar.gz', type='source', repos=NULL)
    install.packages('https://cloud.r-project.org/src/contrib/fiery_1.1.1.tar.gz', type='source', repos=NULL)

    remotes::install_github('plotly/dashR', dependencies=FALSE)
```

---

**`Aptfile`**

`Aptfile` describes system-level dependencies. A suggested
initial configuration is below; add Ubuntu package names as
needed for your applications.

```
    libcurl4-openssl-dev
    libxml2-dev
    libv8-3.14-dev
```
---

4. Initialize Heroku, add files to Git, and deploy

```
    $ heroku create my-dash-app # change my-dash-app to a unique name
    $ git add . # add all files to git
    $ git commit -m 'Initial app boilerplate'
    $ git push heroku master # deploy code to heroku
    $ heroku ps:scale web=1  # run the app with a 1 heroku 'dyno'
```

You should be able to view your app at https://my-dash-app.herokuapp.com (changing my-dash-app to the name of your app).

---

5. Update the code and redeploy

When you modify app.R with your own code, you will need to add the changes to git and push those changes to heroku.

```
    $ git status # view the changes
    $ git add .  # add all the changes
    $ git commit -m 'a description of the changes'
    $ git push heroku master
```

This workflow for deploying apps on heroku is very similar to how deployment works with the Plotly Enterprise's
Dash Deployment Server. [Learn more](https://plot.ly/dash/pricing/?_ga=2.176345125.1075922756.1562168385-916141078.1562168385) or [get in touch](https://plotly.typeform.com/to/rkO85m?_ga=2.176345125.1075922756.1562168385-916141078.1562168385).

  "),
htmlHr(),
dccMarkdown("
[Back to the Table of Contents](/)
              ")
))
