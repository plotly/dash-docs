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

## Creating a Component

To create a Dash component, fork our sample component repository and
follow the instructions in the README.md:
[https://github.com/plotly/dash-component-boilerplate](https://github.com/plotly/dash-component-boilerplate)

If you are just getting started with React.js, check out a draft of our essay
["React for Python Devs"](https://github.com/plotly/dash-docs/pull/116).


### How Are Components Converted From React.js to Python?

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


''')
]
