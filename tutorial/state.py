from textwrap import dedent as s
import dash_core_components as dcc
import dash_html_components as html

from components import Example, Syntax
import tools

examples = {
    'basic-input': tools.load_example('tutorial/examples/basic-input.py'),
    'basic-state': tools.load_example('tutorial/examples/basic-state.py')
}

layout = html.Div([
    html.H1('Dash State'),

    dcc.Markdown(s('''
        > This is the *4th* chapter of the [Dash Tutorial](/).
        > The [previous chapter](/getting-started-part-2) covered Dash Callbacks
        > and the [next chapter](/interactive-graphing) covers interactive
        > Just getting started? Make sure to
        > [install the necessary dependencies](/installation).
    ''')),

    dcc.Markdown(s('''
        In the previous chapter on
        [basic dash callbacks](/getting-started-part-2),
        our callbacks looked something like:
    ''')),
    Syntax(examples['basic-input'][0]),
    Example(examples['basic-input'][1]),

    dcc.Markdown(s('''
        In this example, the callback function is fired whenever any of the
        attributes described by the `dash.dependencies.Input` change.
        Try it for yourself by entering data in the inputs above.

        `dash.dependencies.State` allows you to pass along extra values without
        firing the callbacks. Here's the same example as above but with the
        `dcc.Input` as `dash.dependencies.State` and a button as
        `dash.dependencies.Input`.
    ''')),
    Syntax(examples['basic-state'][0]),
    Example(examples['basic-state'][1]),

    dcc.Markdown(s('''
        In this example, changing text in the `dcc.Input` boxes won't fire
        the callback but clicking on the button will. The current values of
        the `dcc.Input` values are still passed into the callback even though
        they don't trigger the callback function itself.

        Note that we're triggering the callback by listening to the
        `n_clicks` property of the `html.Button` component. `n_clicks` is a
        property that gets incremented every time the component has been
        clicked on. It is available in every component in the
        `dash_html_components` library.

    ''')),

    dcc.Markdown('''
    ***

    The next chapter of the user guide explains how to use callbacks
    principles with the `dash_core_components.Graph` component
    to make applications that
    respond to interactions with graphs on the page.
    '''.replace('    ', '')),

    dcc.Link(
        'Dash Tutorial Part 5. Interactive Graphing',
        href='/interactive-graphing'),

])
