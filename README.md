# Dash Userguide

The [Dash Userguide](https://plot.ly/dash): everything that you need to know to be productive with Dash.

The Dash Userguide is hosted online at: [https://plot.ly/dash](https://plot.ly/dash).

### Running an app locally

To run an app locally:

1. (optional) create and activate new virtualenv or conda env (Python 2.7):

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

or, with conda:
```
conda create --yes -n dash_docs python=2.7
source activate dash_docs
```

2. `pip install -r requirements.txt`
3. `gunicorn tutorial.run:server`
4. open http://127.0.0.1:8000 in your browser


### Contributing

PRs accepted! The Dash user guide is itself a Dash app. Each file in `tutorial` represents a "chapter" of the docs.

Changes to master will get deployed automatically.
