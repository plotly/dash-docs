# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

from textwrap import dedent as s

from tutorial import styles
from tutorial.tools import load_example

examples = [
    load_example(example) for example in [
        'tutorial/examples/getting_started_interactive_simple.py',
        'tutorial/examples/getting_started_graph.py',
        'tutorial/examples/getting_started_multiple_viz.py',
        'tutorial/examples/getting_started_multiple_outputs_1.py',
        'tutorial/examples/getting_started_callback_chain.py',
    ]
]


layout = html.Div([

    dcc.Markdown(s('''
    # Basic Dash Callbacks

    > This is the *3rd* chapter of the [Dash Tutorial](/).
    > The [previous chapter](/getting-started) covered the Dash app `layout`
    > and the [next chapter](/state) covers an additional concept of callbacks
    > known as `state`. Just getting started? Make sure to
    > [install the necessary dependencies](/installation).

    ''')),

    dcc.Markdown(s('''

        In the [previous chapter on the `app.layout`](/getting-started) we
        learned that the `app.layout` describes what the app looks like and is
        a hierarchical tree of components.
        The `dash_html_components` library provides classes for all of the HTML
        tags, and the keyword arguments describe the HTML attributes like
        `style`, `className`, and `id`. The `dash_core_components` library
        generates higher-level components like controls and graphs.

        This chapter describes how to make your
        Dash apps interactive.

        Let's get started with a simple example.

    ''')),

    html.H4('''
    Dash App Layout
    ''', id='dash-app-layout'),

    dcc.Markdown(
        examples[0][0],
        style=styles.code_container
    ),

    html.Div(examples[0][1], className="example-container"),

    dcc.Markdown(s('''
    Try typing in the text box. The children of the output component updates
    right away. Let's break down what's happening here:

    1. The "inputs" and "outputs" of our application interface are described
       declaratively through the `app.callback` decorator.
    2. In Dash, the inputs and outputs of our application are simply the
       properties of a particular component. In this example,
       our input is the "`value`" property of the component that has the ID
       "`my-id`". Our output is the "`children`" property of the
       component with the ID "`my-div`".
    3. Whenever an input property changes, the function that the
       callback decorator wraps will get called automatically.
       Dash provides the function with the new value of the input property as
       an input argument and Dash updates the property of the output component
       with whatever was returned by the function.
    4. The `component_id` and `component_property` keywords are optional
       (there are only two arguments for each of those objects).
       I have included them here for clarity but I will omit them from here on
       out for brevity and readability.
    5. Don't confuse the `dash.dependencies.Input` object from the
       `dash_core_components.Input` object. The former is just used in these
       callbacks and the latter is an actual component.
    6. Notice how we don't set a value for the `children` property of the
       `my-div` component in the `layout`. When the Dash app starts, it
       automatically calls all of the callbacks with the initial values of the
       input components in order to populate the initial state of the output
       components. In this example, if you specified something like
       `html.Div(id='my-div', children='Hello world')`, it would get
       overwritten when the app starts.

    It's sort of like programming with Microsoft Excel:
    whenever an input cell changes, all of the cells that depend on that cell
    will get updated automatically. This is called "Reactive Programming".

    Remember how every component was described entirely through its set of
    keyword arguments? Those properties are important now.
    With Dash interactivity, we can dynamically update any of those properties
    through a callback function. Frequently we'll update the `children` of a
    component to display new text or the `figure` of a `dcc.Graph` component
    to display new data, but we could also update the `style` of a component or
    even the available `options` of a `dcc.Dropdown` component!

    ***

    Let's take a look at another example where a `dcc.Slider` updates a
    `dcc.Graph`.
    ''')),

    dcc.Markdown(
        examples[1][0],
        style=styles.code_container
    ),

    html.Div(examples[1][1], className="example-container", style={
        'paddingLeft': '20px',
        'paddingRight': '35px',
        'paddingBottom': '30px'
    }),

    dcc.Markdown(s('''
    In this example, the `"value"` property of the `Slider` is the input of the
    app and the output of the app is the `"figure"` property of the `Graph`.
    Whenever the `value` of the `Slider` changes, Dash calls the callback
    function `update_figure` with the new value. The function filters the
    dataframe with this new value, constructs a `figure` object,
    and returns it to the Dash application.

    There are a few nice patterns in this example:

    1. We're using the [Pandas](http://pandas.pydata.org/) library for
       importing and filtering datasets in memory.
    2. We load our dataframe at the start of the app:
       `df = pd.read_csv('...')`.
       This dataframe `df` is in the global state of the app and can be
       read inside the callback functions.
    3. Loading data into memory can be expensive. By loading querying data at
       the start of the app instead of inside the callback functions, we ensure
       that this operation is only done when the app server starts. When a user
       visits the app or interacts with the app, that data (the `df`)
       is already in memory.
       If possible, expensive initialization (like downloading or querying
       data) should be done in the global scope of the app instead of within
       the callback functions.
    4. The callback does not modify the original data, it just creates copies
       of the dataframe by filtered through pandas filters.
       This is important: *your callbacks should never mutate variables
       outside of their scope*. If your callbacks modify global state, then one
       user's session might affect the next user's session and when the app is
       deployed on multiple processes or threads, those modifications will not
       be shared across sessions.

    #### Multiple inputs

    In Dash, any "`Output`" can have multiple "`Input`" components.
    Here's a simple example that binds five Inputs
    (the `value` property of 2 `Dropdown` components,
    2 `RadioItems` components, and 1 `Slider` component)
    to 1 Output component (the `figure` property of the `Graph` component).
    Notice how the `app.callback` lists all five `dash.dependencies.Input`
    inside a list in the second argument.

    ''')),

    dcc.Markdown(
        examples[2][0],
        style=styles.code_container
    ),

    html.Div(examples[2][1], className="example-container", style={
        'padding-right': '35px',
        'padding-bottom': '30px'
    }),

    dcc.Markdown(s('''

    In this example, the `update_graph` function gets called whenever the
    `value` property of the `Dropdown`, `Slider`, or `RadioItems` components
    change.

    The input arguments of the `update_graph` function are the new or current
    value of each of the `Input` properties, in the order that they were
    specified.

    Even though only a single `Input` changes at a time (a user can only change
    the value of a single Dropdown in a given moment), Dash collects the
    current state of all of the specified `Input` properties and passes them
    into your function for you. Your callback functions are always guaranteed
    to be passed the representative state of the app.

    Let's extend our example to include multiple outputs.

    #### Multiple Outputs

    *New in dash 0.39.0*

    So far all the callbacks we've written only update a
    single `Output` property. We can also update several at once: put all the
    properties you want to update as a list in the decorator, and return that
    many items from the callback. This is particularly nice if two outputs
    depend on the same computationally intense intermediate result, such as a
    slow database query.
    ''')),

    dcc.Markdown(
        examples[3][0],
        style=styles.code_container
    ),

    html.Div(examples[3][1], className="example-container"),

    dcc.Markdown(s('''
    A word of caution: it's not always a good idea to combine Outputs, even if
    you can:

    - If the Outputs depend on some but not all of the same Inputs, keeping
      them separate can avoid unnecessary updates.
    - If they have the same Inputs but do independent computations with these
      inputs, keeping the callbacks separate can allow them to run in parallel.

    #### Chained Callbacks

    You can also chain outputs and inputs together: the output of one callback
    function could be the input of another callback function.

    This pattern can be used to create dynamic UIs where one input component
    updates the available options of the next input component.
    Here's a simple example.
    ''')),

    dcc.Markdown(
        examples[4][0],
        style=styles.code_container
    ),

    html.Div(examples[4][1], className="example-container"),

    dcc.Markdown(s(u'''
    The first callback updates the available options in the second `RadioItems`
    component based off of the selected value in the first `RadioItems`
    component.

    The second callback sets an initial value when the `options` property
    changes: it sets it to the first value in that `options` array.

    The final callback displays the selected `value` of each component.
    If you change the `value` of the countries `RadioItems` component, Dash
    will wait until the `value` of the cities component is updated
    before calling the final callback. This prevents your callbacks from being
    called with inconsistent state like with `"America"` and `"Montréal"`.

    ''')),

    dcc.Markdown(s('''

    ### Summary

    We've covered the fundamentals of callbacks in Dash.
    Dash apps are built off of a set
    of simple but powerful principles: declarative UIs that are customizable
    through reactive and functional Python callbacks.
    Every element attribute of the declarative components can be updated
    through a callback and a subset of the attributes, like the `value`
    properties of the `dcc.Dropdown`, are editable by the user in the
    interface.

    ***

    ''')),


    dcc.Markdown(s('''
        The next part of the Dash tutorial covers an additional concept of
        Dash callbacks: `State`
    ''')),

    dcc.Link(
        'Dash Tutorial Part 4: State',
        href="/state"
    )


])
