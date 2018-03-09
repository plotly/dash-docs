import dash_core_components as dcc
import dash_html_components as html

import styles

layout = [dcc.Markdown('''
# Writing your own components

One of the really cool things about dash is that
it is built on top of [React.js](https://facebook.github.io/react/),
a JavaScript library for building web components.

The React community is huge. Thousands of components have been built and
released with open source licenses. For example, here are just some of the
[slider components](https://react.rocks/?q=slider) and
[table components](https://react.rocks/?q=tables) that have been published
by the community.

## From React.js to Python

Dash provides a framework that converts React components
(written in JavaScript) into Python classes that are
compatible with the Dash ecosystem.

On a high level, this is how that works:
- Components in dash are serialized as [JSON](www.json.org).
  To write a dash-compatible component, all of the properties
  of the component must be serializable as JSON. For example,
  JavaScript functions are not valid input arguments.
- By annotating components with React docstrings, Dash extracts
  the information about the component's name, properties, and a description
  of the components through [React Docgen](https://github.com/reactjs/react-docgen).
  This is exported as a JSON file.
- Dash reads this JSON file and dynamically creates Python classes that subclass
  a core Dash component. These classes include argument validation,
  Python docstrings, types, and a basic set of methods. _These classes are
  generated entirely automatically._ A JavaScript developer does not need to
  write _any_ Python in order to generate a component that can be used in the
  Dash ecosystem.
- The Python component package includes the JSON file and the JavaScript bundle
  as extra files through the `MANIFEST.in` file.
- The Dash app will crawl through the app's `layout` property and check which
  component packages are included in the layout and it will extract that
  component's necessary JavaScript or CSS bundles. Dash will serve these bundles
  to Dash's front-end. These JavaScript bundles are used to render the components.
- Dash's `layout` is serialized as JSON and served to Dash's front-end. This
  `layout` is recursively rendered with these JavaScript bundles and React.


## Step-by-step guide

The Dash ecosystem includes a command-line tool for
generating component package templates with all of the necessary
boiler plate.

We use the package [builder](https://github.com/FormidableLabs/builder) built by
the excellent team at [Formidable Labs](https://formidable.com/) to manage
these templates.

The code behind the template is available in the
[plotly/dash-components-archetype](https://github.com/plotly/dash-components-archetype)
repository on GitHub.

### Step 1 - Prerequisites

You'll need Node, NPM, and Python installed.
Components are built with [React.js](https://facebook.github.io/react/).

> If you're just getting started, we've written a great
[React.js tutorial](https://academy.plot.ly/) as part of our open source academy.

### Step 2 - Install Builder
'''),
dcc.SyntaxHighlighter('''$ npm install -g builder-init''',
    language='bash', customStyle=styles.code_container),

dcc.Markdown('''### Step 3 - Initialize a Project'''),
dcc.SyntaxHighlighter('''$ builder-init dash-components-archetype''',
    language='bash', customStyle=styles.code_container),

dcc.Markdown('''
Builder will initialize a folder containing the boilerplate
of a dash component package.

This will walk you through a series of prompts about your package like
the name and description of the project. The name of the project will be
the name of the Python package, with hyphens replaced by underscores.
For example, if the name is `acme-components` then the Python package will
end up being `acme_components`, importable like `import acme_components`.

> One cool thing about this Builder archetype is that it will
> template in the name of your package in the files and folders that it
> generates. This requires way less work than say cloning a boilerplate Git Repo.

This will end up looking _something_ like:
'''),

dcc.SyntaxHighlighter('''$ builder-init dash-components-archetype
dash-components-archetype-0.2.4.tgz
[builder-init] Preparing templates for: dash-components-archetype
? Please name your component suite. acme-components
? Enter a description Components used by the Acme Corp
? GitHub organization or user name acme-corp
? License organization (e.g., you or your company) acme-corp
? Destination directory to write acme-components

[builder-init] Wrote files:
 - acme-components/.babelrc
 - acme-components/.builderrc
 - acme-components/CHANGELOG.md
 - acme-components/LICENSE.txt
 - acme-components/MANIFEST.in
 - acme-components/README.md
 - acme-components/package.json
 - acme-components/requirements.txt
 - acme-components/setup.py
 - acme-components/.eslintrc
 - acme-components/.gitignore
 - acme-components/demo/Demo.react.js
 - acme-components/demo/index.html
 - acme-components/demo/index.js
 - acme-components/src/index.js
 - acme-components/test/main.js
 - acme-components/acme_components/__init__.py
 - acme-components/src/components/ExampleComponent.react.js
 - acme-components/src/components/__tests__/.eslintrc
 - acme-components/src/components/__tests__/ExampleComponent.test.js

[builder-init] New dash-components-archetype project is ready at: acme-components
''', language='bash', customStyle=styles.code_container),

dcc.Markdown('''
### Step 4 - Test the Generated Boilerplate

At this point, Builder has created a folder that contains the necessary
JavaScript and Python code to build a valid component.

The component is in the `components/ExampleComponent.react.js` file.

The source code in this folder can't be used directly as a Python package.
The JavaScript source will need to get transpiled into a single bundle and
react-docgen will need to generate a valid JSON file. This is the "build step"
and this step needs to be run every time you make a modification to the source.

To create a build, run `npm install`:
'''),

dcc.SyntaxHighlighter('''$ cd my-component-library # replace with the name of your component library
$ npm install''',
    language='bash', customStyle=styles.code_container),

dcc.Markdown('''

This will perform several tasks:
- Install the necessary packages
- Run tests
- Create a build

The JavaScript bundle and the react-docgen JSON file will be in a folder named
after your package alongside an `__init__.py` file.

### Step 5 - Test Components in a Dash App

The package is now ready to test. You can test this component by running the
`usage.py` file that is included in the repository:
'''),

dcc.SyntaxHighlighter('''$ python usage.py''', language='bash', customStyle=styles.code_container),

dcc.Markdown('''
You are free to edit this file as you develop your component. Note that
this file is importing the package locally (as it is in the root folder of
the package). If you want to test the installation of your package and run a
Dash app in a separate folder, you can install the package with `python setup.py install`.

#### Step 6 - Customize Your Component

By now, we've just exported the component that was included by default by the
archetype. The source of this component is available in the
`src/components/ExampleComponent.react.js` file.

Edit this source to modify the component. You can rename this file to change
the name of the component and the Python class. If you rename the file or
add a new file, be sure to make those changes to to the `src/index.js` file
as well.

Notice how the docstrings and keyword arguments of the Python class will
match the comments in the React component.

For example, the default component `ExampleComponent.react.js` looks something
like this:

'''),

dcc.SyntaxHighlighter('''import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class ExampleComponent extends Component {
    render() {
        const {id, label, setProps, value} = this.props;

        return (
            <div id={id}>
                ExampleComponent: {label}
                <input
                    value={value}
                    onChange={e => {
                        /*
                         * Send the new value to the parent component.
                         * In a Dash app, this will send the data back to the
                         * Python Dash app server.
                         */
                         if (setProps) {
                             setProps({
                                value: e.target.value
                            });
                         }
                    }}
                />
            </div>
        );
    }
}

ExampleComponent.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * A label that will be printed when this component is rendered.
     */
    label: PropTypes.string.isRequired,

    /**
     * The value displayed in the input
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func
};
''', language='JavaScript', customStyle=styles.code_container),

dcc.Markdown('''
Dash converts this component into a Python class automatically. If you import
this class into your Python context, you'll be able to interact with it like
this:
'''),

dcc.SyntaxHighlighter('''>>> import acme_components
>>> help(acme_components.ExampleComponent)
Help on class ExampleComponent in module __builtin__:

class ExampleComponent(dash.development.base_component.Component)
 |  A ExampleComponent component.
 |  ExampleComponent is an example component.
 |  It takes a property, `label`, and
 |  displays it.
 |  It renders an input with the property `value`
 |  which is editable by the user.
 |
 |  Keyword arguments:
 |  - id (string; optional): The ID used to identify this component in Dash callbacks
 |  - label (string; required): A label that will be printed when this component is rendered.
 |  - value (string; optional): The value displayed in the input

>>> acme_components.ExampleComponent(label='My label')
ExampleComponent('My label')

>>> acme_components.ExampleComponent(label='My label')
ExampleComponent('My label')

>>> acme_components.ExampleComponent(foo='bar') # foo is not a property of this component
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 25, in __init__
  File "/Users/chriddyp/Repos/venvpy27/lib/Python2.7/site-packages/dash/development/base_component.py", line 23, in __init__
    ', '.join(self._prop_names)
Exception: Unexpected keyword argument `foo`
Allowed arguments: label
''', customStyle=styles.code_container),

dcc.Markdown('''
Notice how the comments in the `ExampleComponent.react` match the docstring
of the `ExampleComponent` Python class. Also notice how the docstring includes
the types of the arguments (extracted from `propTypes`) and how the classes
perform keyword validation. All of this logic and translation is provided
to you automatically through dash through React-docgen and your comments
that you include around your `propTypes` and component definition.

So, if you add new components, you'll need annotate the components properties
with these docstrings, otherwise Dash won't be able to generate Python dash
classes.

Dash components are described declaratively through that set of component
properties. Some of these properties are editable by the user. For example,
in the `ExampleComponent`, the `value` property is editable by the user.
To propagate changes that are made to properties through the user interface to
Dash, your component code must call `props.setProps({name_of_the_property: new_value_of_the_property})`.
This will update the property of that component, will rerender the component with that property,
and will send that new value to the appropriate Python Dash app callback.

Once you've made some changes or created a new component, you can recreate
your bundle and re-install your package locally by running:
'''),

dcc.SyntaxHighlighter('''$ npm run prepublish
$ python setup.py install
''', customStyle=styles.code_container),

dcc.Markdown('''
You can also interact with your component in pure JavaScript by running
'''),

dcc.SyntaxHighlighter('''$ builder run demo
''', customStyle=styles.code_container),

dcc.Markdown('''
and then opening your web browser to `http://localhost:9000`. This command
sets up hot-reloading, so changes that you make the code will be visible
in your web browser immediately.
'''),

dcc.Markdown('''

#### Step 7 - Publish Your Component

Finally, you can publish your component to both NPM and PyPI (Python's package registry).
You'll need an account on both registries:
- NPM: [https://www.npmjs.com](https://www.npmjs.com)
- PyPI: [https://pypi.org/](https://pypi.org/)

We publish to NPM so that Dash can use a global CDN called [unpkg](https://unpkg.com/).
Unpkg automatically serves content from NPM packages.

After you have created accounts, you'll need to save your login credentials on your local machine
so that they can be used when you publish to the registries. For PyPI, create a file named `~/.pypirc`:
```
[distutils]
index-servers =
  pypi

[pypi]
repository=https://pypi.python.org/pypi
username=your_username
password=your_password
```

For NPM, your credentials will be saved in `~/.npmrc`. NPM will save these credentials for you if you run:
```
$ npm login
```

> PyPI is moving to new infrastructure for publishing packages. 
> If you have published packages before using PyPI, you may recieve an authentication 
> warning if your account's email address is not verified. You can verify your address
> on their new site ([https://pypi.org/](https://pypi.org/)). You can find your PyPI 
> credentials in a `~/.pypirc` file.


To publish the components (to NPM _and_ PyPI), run:

'''),

dcc.SyntaxHighlighter('''npm run publish-all
''', customStyle=styles.code_container),

dcc.Markdown('''
The version of the package is set in both `package.json` and a `version.py` file.

For more information on publishing to PyPI, 
see this [community blogpost](http://peterdowns.com/posts/first-time-with-pypi.html).

By convention, dash components should adhere to [semver](http://semver.org/).
Finally, if you'd like, share your component suite with other Dash users in the
[Dash community forum](https://community.plot.ly/c/dash)!

To be notified of **breaking changes** in the component API, please subscribe to one of these issues:
- https://github.com/plotly/dash-components-archetype/issues/40
- https://community.plot.ly/t/mega-react-component-authors-subscribe-to-be-notified-of-breaking-changes/8640
''')
]
