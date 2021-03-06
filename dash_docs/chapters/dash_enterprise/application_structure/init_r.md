## init.R

`init.R` is an R script that is used to install R packages.

```
instal.packages('remotes')
install.packages('dashR')
```

The install.packages commands will install the packages from a CRAN mirror. Dash for R is published on Github and on CRAN. The version on Github will often have updates that haven't yet been published to CRAN. To use the latest version of Dash for R, install from Github with:

```
install.packages('remotes')
remotes::install_github('plotly/dashR', upgrade=TRUE)
```

When installing from Github, be mindful of Github's rate limits for anonymous downloads.
To get around Github's rate limit, supply a Github personal access token (PAT) in environment variable named GITHUB_PAT in the App Manager.

---
