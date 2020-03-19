# Contributing

This documentation is a Python and R Dash app.

Here is an incomplete set of patterns that we use:
1. Remote URL examples need to be on a single line, a copy of their data needs to provided in `datasets/`, and the lookup between remote URL and local URL needs to be updated in `tools.load_example`. These remote URLs are replaced on-the-fly when running the docs so that this project can run in airgapped environments.

2. All paths (`href` & `src`) need to use `tools.relpath`

3. The markdown content needs to use `reusable_components.Markdown` instead of `dcc.Markdown`. `reusable_components.Markdown` will replace relative links with `tools.relpath`

4. Two custom components are used. The source is in `dash-user-guide-components`. They are built into a tarball with a command like:
```
cd dash-user-guide-components
npm run build
python setup.py sdist
cp dist/dash_user_guide_components-0.0.1.tar.gz ..
```
If you make changes here, you will need to bump the version number so that the product server installs the new version when deployed.
