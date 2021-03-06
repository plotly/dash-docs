# Deploying to Heroku

There are at least two ways to deploy a **dashR** app to [Heroku](https://www.heroku.com/): via a build-pack or a [docker](https://www.docker.com/) container. The docker approach is more flexible in that you can completely control the computing environment of your app, but as a result it's a bit more cumbersome. If you have interest in using docker, you may want to build off our minimal [base images](../docker).

## Deploying via a build-pack

Since **dashR** builds upon a [**fiery** web server](https://cran.r-project.org/package=fiery), in order to deploy **dashR** app(s) to Heroku, we can use an approach similar to the one outlined [here](https://www.data-imaginist.com/2017/setting-fire-to-deployment/). If you are brand new to Heroku, I suggest reading that post first then coming back here for a **dashR** example.

There are three critical files required to run any **dashR** app via the [Heroku buildpack for R](https://github.com/virtualstaticvoid/heroku-buildpack-r/tree/heroku-16): an `Aptfile` for installing system libraries, a `init.R` script for installing R packages, and a `run.R` script for running the **dashR** application. For simple applications, you probably won't have to modify the `Aptfile`, but if you need R packages that require external system libraries (e.g., **sf**, **leaflet**, **rmarkdown**, etc), you have to add relevant apt packages to this file. There is a nice collection of apt requirements for popular R packages [here](https://github.com/rstudio/shinyapps-package-dependencies/tree/master/packages). 

We suggest that you start from our Heroku app template, which you can summon via the `heroku_app_template()` function. This copies the template to your current working directory:

```r
library(dashR)
heroku_app_template()
```

After you've modified those files to run your own **dashR** app, login to Heroku via the command-line tool:

```shell
heroku login
```

If you know your way around git, you can follow these instructions for [deploying to Heroku via git](https://devcenter.heroku.com/articles/git), which the `dashR::heroku_app_deploy()` function attempts to automate for you:

dashR::heroku_app_deploy("my-test-app")

On Windows systems `waitress` can be a replacement for `gunicorn`

`pip install waitress`
`waitress-serve --listen=*:8000 run:server`
open http://127.0.0.1:8000 in your browser

```r
dashR::heroku_app_deploy("my-test-app")
```

### Protocol
```r
heroku git:clone -a dashr-docs
heroku plugins:install heroku-repo
heroku buildpacks:set https://github.com/virtualstaticvoid/heroku-buildpack-r.git#heroku-16
heroku stack:set heroku-16
git push heroku master
```

