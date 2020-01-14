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

## Dash Enterprise 

[Dash Enterprise](https://plot.ly/dash/pricing/?_ga=2.249471751.1080104966.1578062860-1986131108.1567098614) is Plotly's commercial product for deploying Dash
Apps on your company's servers or on AWS, Google Cloud, or Azure. It
offers an enterprise-wide Dash App Portal, easy git-based deployment,
automatic URL namespacing, built-in SSL support, LDAP authentication, and
more. [Learn more about Dash Enterprise](https://plot.ly/dash/pricing?_ga=2.249471751.1080104966.1578062860-1986131108.1567098614) or [get in touch to start a
trial](https://go.plot.ly/dash-doc?_ga=2.48144423.1080104966.1578062860-1986131108.1567098614).

For existing customers, see the [Dash Enterprise Documentation](https://dash.plot.ly/dash-enterprise).

## Dash and Fiery

Dash apps are web applications. Dash uses Fiery as the web framework.
The underlying Fiery app is available at `app`, that is:

```r
    library(dash)

    app <- Dash$new()
```

## Heroku Example

Heroku is one of the easiest platforms for deploying and managing public web applications.

Here is a simple example. This example requires a Heroku account and `git`. We currently recommend using a Dockerfile-based
approach when deploying Dash for R applications to Heroku. You may use our base image (as below), or supply your own.

For more information about this deployment method, [please consult the Heroku documentation](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml).

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

Step 3. Initialize the folder with a sample app (`app.R`), a `.gitignore` file, `Dockerfile`, `heroku.yml` for deployment

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

**`Dockerfile`**

```
FROM plotly/heroku-docker-r:3.6.2_heroku18

# on build, copy application files
COPY . /app/
              
# for installing additional dependencies etc.
RUN if [ -f '/app/onbuild' ]; then bash /app/onbuild; fi; 
              
# look for /app/apt-packages and if it exists, install the packages contained
RUN if [ -f '/app/apt-packages' ]; then apt-get update -q && cat apt-packages | xargs apt-get -qy install && rm -rf /var/lib/apt/lists/*; fi;              

# look for /app/init.R and if it exists, execute it
RUN if [ -f '/app/init.R' ]; then /usr/bin/R --no-init-file --no-save --quiet --slave -f /app/init.R; fi; 
              
CMD cd /app && /usr/bin/R --no-save -f /app/run.R
```

---

**`heroku.yml`**
```
build:
  docker:
    web: Dockerfile
```

---

**`init.R`**

`init.R` describes your R dependencies. Here is an example script. It's fairly trivial to
install packages from both CRAN mirrors and GitHub repositories:

```r
# R script to run author supplied code, typically used to install additional R packages
# contains placeholders which are inserted by the compile script
              # NOTE: this script is executed in the chroot context; check paths!
              
              r <- getOption('repos')
              r['CRAN'] <- 'http://cloud.r-project.org'
              options(repos=r)
              
              # ======================================================================
              
              # packages go here
              install.packages('remotes')
              
              remotes::install_github('plotly/dashR', upgrade=TRUE)
              install.packages('manhattanly')
```

---

**`apt-packages`**

`apt-packages` describes system-level dependencies. A suggested
initial configuration is below; add Debian/Ubuntu package names as
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
    $ heroku stack:set container # use container as the stack type
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

This workflow for deploying apps on Heroku is analogous to how deployment works with Plotly's Enterprise offering. 
[Learn more](https://plot.ly/dash/pricing/?_ga=2.176345125.1075922756.1562168385-916141078.1562168385) or [get in touch](https://plotly.typeform.com/to/rkO85m?_ga=2.176345125.1075922756.1562168385-916141078.1562168385).

  "),
htmlHr(),
dccMarkdown("
[Back to the Table of Contents](/)
              ")
))
