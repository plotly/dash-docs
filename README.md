# Dash Userguide

The [Dash Userguide](https://plot.ly/dash): everything that you need to know to be productive with Dash.

The Dash Userguide is hosted online at: [https://plot.ly/dash](https://plot.ly/dash). A [PDF version](/pdf-docs/Dash_User_Guide_and_Documentation.pdf) is also available. 

### Running an app locally

To run an app locally:

1. (optional) create and activate new virtualenv or conda env:

```r
library(dash)
heroku_app_template()
```

or, with conda:
```
conda create --yes -n dash_docs
source activate dash_docs
```

2. `pip install -r requirements.txt`
3. `gunicorn run:server`
4. open http://127.0.0.1:8000 in your browser


on Windows systems `waitress` can be a replacement for `gunicorn`

3. `pip install waitress`
4. `waitress-serve --listen=*:8000 run:server`
5. open http://127.0.0.1:8000 in your browser


### Contributing

PRs accepted! The Dash user guide is itself a Dash app. Each file in `tutorial` represents a "chapter" of the docs.

Changes to master will get deployed automatically.
