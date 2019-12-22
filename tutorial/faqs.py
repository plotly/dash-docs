# -*- coding: utf-8 -*-
import os
from textwrap import dedent as s

import dash_core_components as dcc
import dash_html_components as html

from tutorial.components import Example, Syntax
from tutorial import tools


def get_example_name(path):
    """Returns the name of an example given its path."""
    # name is the filename without the suffix
    return os.path.splitext(os.path.basename(path))[0]


examples = {get_example_name(path): tools.load_example(path) for path in
            ['tutorial/examples/faqs/last_clicked_button.py']}


layout = html.Div([
    dcc.Markdown(s('''
    # FAQs and Gotchas

    > This is the *7th* and final chapter of the essential [Dash Tutorial](/).
    > The [previous chapter](/sharing-data-between-callbacks) described how to
    > share data between callbacks. The [rest of the Dash documentation](/)
    > covers other topics like multi-page apps and component libraries.


    ## Frequently Asked Questions

    **Q:** *How can I customize the appearance of my Dash app?*

    **A:** Dash apps are rendered in the browser as modern standards compliant
      web apps. This means that you can use CSS to style your Dash app as you
      would standard HTML.

      All `dash-html-components` support inline CSS styling through a `style`
      attribute. An external CSS stylesheet can also be used to style
      `dash-html-components` and `dash-core-components` by targeting the ID or
      class names of your components. Both `dash-html-components` and
      `dash-core-components` accept the attribute `className`, which corresponds
      to the HTML element attribute `class`.

      The [Dash HTML Components](/dash-html-components) section in the Dash User
      Guide explains how to supply `dash-html-components` with both inline
      styles and CSS class names that you can target with CSS style sheets. The
      [Adding CSS & JS and Overriding the Page-Load
      Template](/external-resources) section in the Dash Guide explains how you
      can link your own style sheets to Dash apps.

    ------------------------

    **Q:** *How can I add JavaScript to my Dash app?*

    **A:** You can add your own scripts to your Dash app, just like you would
      add a JavaScript file to an HTML document. See the [Adding CSS & JS and
      Overriding the Page-Load Template](/external-resources) section in the
      Dash Guide.

    ------------------------

    **Q:** *Can I make a Dash app with multiple pages?*

    **A:** Yes! Dash has support for multi-page apps. See the [Multi-Page Apps
      and URL Support](/urls) section in the Dash User Guide.

    ------------------------

    **Q:** *How I can I organise my Dash app into multiple files?*

    **A:** A strategy for doing this can be found in the [Multi-Page Apps
      and URL Support](/urls) section in the Dash User Guide.

    ------------------------

    **Q:** *How do I determine which `Input` has changed?*

    **A:** *New in v0.38.0!* In addition to event properties like `n_clicks`
    that change whenever an event happens (in this case a click), there is a
    global variable `dash.callback_context`, available only inside a callback.
    It has properties:
    - `triggered`: list of changed properties. This will be empty on initial
      load, unless an `Input` prop got its value from another initial callback.
      After a user action it is a length-1 list, unless two properties of a
      single component update simultaneously, such as a value and a timestamp
      or event counter.
    - `inputs` and `states`: allow you to access the callback params
      by id and prop instead of through the function args. These have the form
      of dictionaries `{ 'component_id.prop_name': value }`

    Here's an example of how this can be done:''')),
    Syntax(examples['last_clicked_button'][0]),
    Example(examples['last_clicked_button'][1]),
    dcc.Markdown(s('''

    Prior to v0.38.0, you needed to compare timestamp properties like
    `n_clicks_timestamp` to find the most recent click. While existing uses of
    `*_timestamp` continue to work for now, this approach is deprecated, and
    may be removed in a future update. The one exception is
    `modified_timestamp` from `dcc.Store`, which is safe to use, it is NOT
    deprecated.

    ------------------------

    **Q:** *Can I use Jinja2 templates with Dash?*

    **A:** Jinja2 templates are rendered on the server (often in a Flask app)
      before being sent to the client as HTML pages. Dash apps, on the other
      hand, are rendered on the client using React. This makes these
      fundamentally different approaches to displaying HTML in a browser, which
      means the two approaches can't be combined directly. You can however
      integrate a Dash app with an existing Flask app such that the Flask app
      handles some URL endpoints, while your Dash app lives at a specific
      URL endpoint.

    ------------------------

    **Q:** *Can I use jQuery with Dash?*

    **A:** For the most part, you can't. Dash uses React to render your app on
      the client browser. React is fundamentally different to jQuery in that it
      makes use of a virtual DOM (Document Object Model) to manage page
      rendering. Since jQuery doesn't speak React's virtual DOM, you can't use
      any of jQuery's DOM manipulation facilities to change the page layout,
      which is frequently why one might want to use jQuery. You can however use
      parts of jQuery's functionality that do not touch the DOM, such as
      registering event listeners to cause a page redirect on a keystroke.

    In general, if you are looking to add custom clientside behavior in your
    application, we recommend encapsulating that behavior in a
    [custom Dash component](https://dash.plot.ly/plugins).

    ------------------------

    **Q:** *Where did those cool undo and redo buttons go?*

    **A:** OK, mostly we got the opposite question:
    [How do I get rid of the undo/redo buttons](https://community.plot.ly/t/is-it-possible-to-hide-the-floating-toolbar/4911/10).
    While this feature is neat from a technical standpoint most people don't
    find it valuable in practice. As of Dash 1.0 the buttons are removed by
    default, no hacky CSS tricks needed. If you want them back, use
    `show_undo_redo`:

    `app = Dash(show_undo_redo=True)`

    ------------------------

    **Q:** *I have more questions! Where can I go to ask them?*

    **A:** The [Dash Community forums](https://community.plot.ly/c/dash) is full
      of people discussing Dash topics, helping each other with questions, and
      sharing Dash creations. Jump on over and join the discussion.


    ## Gotchas

    There are some aspects of how Dash works that can be counter-intuitive. This
    can be especially true of how the callback system works. This section
    outlines some common Dash gotchas that you might encounter as you start
    building out more complex Dash apps. If you have read through the rest of
    the [Dash Tutorial](/) and are encountering unexpected behaviour, this is a
    good section to read through. If you still have residual questions, the
    [Dash Community forums](https://community.plot.ly/c/dash) is a great place
    to ask them.

    ### Callbacks require their `Inputs`, `States`, and `Output` to be present in the layout

    By default, Dash applies validation to your callbacks, which performs checks
    such as validating the types of callback arguments and checking to see
    whether the specified `Input` and `Output` components actually have the
    specified properties. For full validation, all components within your
    callback must therefore appear in the initial layout of your app, and you
    will see an error if they do not.

    However, in the case of more complex Dash apps that involve dynamic
    modification of the layout (such as multi-page apps), not every component
    appearing in your callbacks will be included in the initial layout. You can
    remove this restriction by disabling callback validation like this:

        app.config.supress_callback_exceptions = True


    ### Callbacks require *all* `Inputs`, `States`, and `Output` to be rendered on the page

    If you have disabled callback validation in order to support dynamic
    layouts, then you won't be automatically alerted to the situation where a
    component within a callback is not found within a layout. In this situation,
    where a component registered with a callback is missing from the layout, the
    callback will fail to fire. For example, if you define a callback with only
    a subset of the specified `Inputs` present in the current page layout, the
    callback will simply not fire at all.


    ### A component/property pair can only be the `Output` of one callback

    For a given component/property pair (eg `'my-graph'`, `'figure'`), it can
    only be registered as the `Output` of one callback. If you want to associate
    two logically separate sets of `Inputs` with the one output
    component/property pair, you’ll have to bundle them up into a larger
    callback and detect which of the relevant `Inputs` triggered the callback
    inside the function. For `html.Button` elements, detecting which one
    triggered the callback ca be done using the `n_clicks_timestamp`
    property. For an example of this, see the question in the FAQ, *How do I
    determine which `Input` has changed?*.


    ### All callbacks must be defined before the server starts

    All your callbacks must be defined before your Dash app's server starts
    running, which is to say, before you call `app.run_server(debug=True)`. This means
    that while you can assemble changed layout fragments dynamically during the
    handling of a callback, you can't define dynamic callbacks in response to
    user input during the handling of a callback. If you have a dynamic
    interface, where a callback changes the layout to include a different set of
    input controls, then you must have already defined the callbacks required to
    service these new controls in advance.

    For example, a common scenario is a `Dropdown` component that updates the
    current layout to replace a dashboard with another logically distinct
    dashboard that has a different set of controls (the number and type of which
    might which might depend on other user input) and different logic for
    generating the underlying data. A sensible organisation would be for each of
    these dashboards to have separate callbacks. In this scenario, each of these
    callbacks much then be defined before the app starts running.

    Generally speaking, if a feature of your Dash app is that the number of
    `Inputs` or `States` is determined by a user's input, then you must
    pre-define up front every permutation of callback that a user can
    potentially trigger. For an example of how this can be done programmatically
  using the `callback` decorator, see this [Dash Community forum
    post](https://community.plot.ly/t/callback-for-dynamically-created-graph/5511).

    ### All Dash Core Components in a layout should be registered with a callback.

    Note: This section is present for legacy purposes. Prior to v0.40.0, setProps was only defined if the component was connected to a
    callback. This required complex state management within the component like [this](https://github.com/plotly/dash-core-components/blob/63be1c258c15b419a82fb66366e1a31e66fbfaef/src/components/Input.react.js#L51-L59).
    Now, setProps is always defined which should simplify your component's state
    management. Learn more in this [community forum topic](TBD).

    If a Dash Core Component is present in the layout but not registered with a
    callback (either as an `Input`, `State`, or `Output`) then any changes to its
    value by the user will be reset to the original value when any callback
    updates the page.

    This is a known issue and you can track its status in this [GitHub
    Issue](https://github.com/plotly/dash-renderer/issues/40). '''))
])
