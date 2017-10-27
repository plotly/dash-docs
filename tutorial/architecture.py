import dash_core_components as dcc

layout = dcc.Markdown('''

# Architecture Drafts

## Events, State, and Dependencies

In the frontend, dash components are controlled by the `dash renderer`.
The dash renderer contains the state of all of the components
and passes the state in as props.

This is typical of the circular React data flow:
- Components don't store their own state, a central store does.
- Components fire actions to update the central store.
- Updates to the central store trigger a re-rendering of components,
- passing the data from the store throughout the components.

In Dash, these actions are fired through a prop called `setProps`.

Component authors are required to call `setProps` with an object
containing the new props for that component.

For example, a simple input component would look something like this:

```
function Input(props) {
    const {setProps} = props;
    return (
        <input
            onChange={e => setProps({value: e.target.value})}
            {...props}
        />
    );
}
```

Here's what happens when a user types a value into the input:
- React calls the input's `onChange` function
- This input calls `setProps` with e.g. `{value: 'new value'}`
- `dash renderer` merges that object into its store
- `dash renderer` re-renders the input component with the new props,
  passing in `new value` as the Input's `value` property.

***

In `dash`, updating the values in a component can update other components
("observers") through API calls to a dash server. Here's the flow:
1. User types a value into the input
2. `setProps` is called.
3. The new properties are merged into the store and the input gets re-rendered.
4. `dash renderer` checks if any components "depend" on this "input updating event".
   If they do, then `dash renderer` makes an API call to the `dash server`
   with the necessary state.
5. The `dash server` returns with new properties of the observer
which get merged into `dash renderer`'s store.
6. `dash renderer` re-renders the observed component with the new values.

The tricky thing is providing dash users with a declarative interface to the relationship between components. For example,
- Should an Input fire an API call whenever it's props change or just on blur?
- What if the input is itself an observer? When it's value gets updated,
  should it fire an API call?
- What properties should the input pass to the API call?
  Some components, like graphs or tables, may have huge props that the user
  might not want to send over the wire.

One solution is to introduce a separation of events and state into this
declarative description of dependencies between components.

Consider the following example:
- A Dropdown updates a slider's `min`, `max`, and `value` props
  and should update whenever the dropdown changes value.
- A graph depends on the value of the dropdown's value and the slider's value.
- The graph should update whenever the slider's value changes.

Component's values can change through the server and through user intefaces.

Declaring event IDs for user interfaces is simple and intuitive:
"`onClick`", "`onSelect`", "`onBlur`".

But what about server-driven changes to props handled by `dash-renderer`?

Here are some different scenarios:

- When subscribing to graph updates, like `onHover` events, you don't
always want to subscribe to prop changes. And `hover` events don't even
change the props of a graph.
- When subscribing to text inputs, if your callbacks are fast you might
want to update on every keypress. But if they're slow, you'll want to
update on enter (`onBlur`) or through a click event on a button.

  If you're controlling updates through a button press, then you don't
  want to trigger updates through server changes.
  But if you're apps are more "reactive", updating whenever an input changes,
  you will want to trigger API calls.

There are three types of events:
- User-driven events: hovering over a graph, entering data into an input, selecting an item from a dropdown.
- Server events: An observer dropdown's value gets updated through a server call when its controller input's value changes.
- Display events: when a controller first appears, it may need to update it's observers.

Observer components may observe all types of events or none of them.

Dash users will need to declaratively describe these dependency relationships
and the event triggers.

Here are a few different ways this could be done.

### Events *are* state

In the typical "reactive" UIs, observers are only listening to changes in the
state that they have subscribed to.

This works great for many cases.
You just describe which slices of the state you need and whenever
that state changes, the API call gets fired.

In this paradigm, it doesn't matter *how* a property changed, it just matters
that it changed.

Consider an example with two input components (`input-1` and `input-2`) and
one output component (`output-1`). `output-1` depends on `input-1`s
 values and `input-2`s values. `input-2`s values depend on on `input-1`s
 values.

This relationship could be encoded as:

```
{
    "input-2": {
        "input-1": ["value"]
    }
    "output-1": {
        "input-1": ["value"],
        "input-2": ["value"]
    }
}
```

Easy.

Now, what happens if `output-1` depends on `input-1` and `input-2`'s values
but should only updated when `button-1` is clicked.
`input-2` still depends on `input-1` and should
still get updated whenever `input-1`'s value changes.

This examples becomes cumbersome because we just want to subscribe to
`button-1`'s click event, we don't
actually need any of its state or props.

With this paradigm, we would need to transform transform
button clicks into some state, like a
counter of the number of times that it has been clicked, and then
subscribe to that.

We need to introduce two new concepts:
- transforming events like "click" into some type of state like a click counter
- separating "triggering" state which determines *when* a callback should be
  fired from "argument" state which determines which values should be
  passed into the API callbacks.

```
{
    "output-1": {
        // Whenever the "trigger-state" changes, the callback gets fired.
        "trigger-state": {
            "button-1": ["click-counter"]
        },
        // The callback gets fired with these values
        "argument-state": {
            "input-1": ["value"],
            "input-2": ["value"]
        }
    },
    "input-2": {
        "trigger-state": {
            "input-1": ["value"]
        },
        "argument-state": {
            "input-1": ["value"]
        }
    }
}
```

It feels cumbersome to have to transform these events as state and
it's a little bit confusing to wrap your head around.

`input-2` observing changes to `input-1` is intuitive but listenining
to the "`button`"'s `click-counter` prop feels contrived.

### Subscribe to state or events

Allow full granular control over subscribing to any of the events
whether they are user driven, server driven, or display driven.

Server driven events are given the name "`server-update`"
(alternatively "`computed-update`", "`derived-update`")

Display driven events are given the name `initial-render`.

The reactive example above would be serialized like this:

```
{
    "output-1": {
        "events": {
            "input-1": [
                "onChange",
                "server-update",

                // Not fired in practice because input-1
                // is controlled by input-2,
                // and input-2's would respond to the
                // initial-render and then fire it's own
                // server-update.
                "initial-render"
            ],
            "input-2": [
                // Not fired in practice because output-1
                // wouldn't get updated until input-1's
                // has finished updating. input-1 responds to
                // this component's onChange first
                "onChange",

                // Not fired in practice because it doesn't
                // have a controller
                "server-update",

                "initial-render"
            ]
        },
        "state": {
            "input-1": ["value"],
            "input-2": ["value"]
        }
    },
    "input-1": {
        "events": {
            "input-2": [
                "onChange",
                // Not fired in practice because input-2
                // isn't controlled.
                "server-update",

                "initial-render"
            ]
        },
        "state": {
            "input-2": ["value"]
        }
    }
}
```

While the example with the button click would be rendered like this:

```
{
    "output-1": {
        "events": {
            "button-1": ["click"]
        },
        "state": {
            "input-1": ["value"],
            "input-2": ["value"]
        }
    },
    "input-2": {
        "events": {
            "input-1": [
                // user driven change
                "onChange",

                // Never fired in since
                // input-1 doesn't observe any other controller.
                // But if an "input-3" was added that
                // "input-2" listened to, then it could get fired.
                "server-update",

                // Fired when the input is first rendered.
                // Users might not subscribe to this change
                // if they don't want an output element
                // being populated when it gets rendered.
                //
                // For example, "output-1" doesn't listen to
                // "input-2"'s "initial-render" event but it
                // could, prefilling the UI with an example
                // output.
                "initial-render"
            ]
        },
        "state": {
            "input-1": ["value"]
        }
    }
}
```

There is still some ambiguity in declaration.
- Should `server-update` fire when the `value` changes or any prop changes?
  Similarly with `initial-render`.
- Does "`initial-render`" fire for props or just for renders?
  For example, does the button fire an `initial-render` event?
- Would users *ever* want to subscribe to "`server-update`" and
  "`initial-render`" but not that controller's user interface props?
- Similarly with the inverse. Would users *ever* want to subscribe to
  the user interface events that update a value but not the
  server update events that update the same value? Two scenarios:
  - If the observer doesn't need the controller's props (like a button),
    then it would only subscribe to the user interface events.
  - If the observer's controller isn't controlled, then "server-update"
    will never fire.
- Some of the "initial-render" and "server-update" events will never get
  fired depending on whether the component has dependencies or not
  (respectively). While subscribing to unused events won't break anything,
  it's challenging to wrap your head around and it requires a lot of
  implicit knowledge about the internals of `dash-renderer`.

In light of these ambiguities, perhaps we introduce a new concept
that ties together events and state a little bit better: "observables"

### Observables

Observables are props that are necessary as input arguments
and should fire events when they change.

The simple reactive case looks like this:

```
{
    "output-1": {
        "observables": {
            "input-1": ["value"],
            "input-2": ["value"]
        }
    },
    "input-2": {
        "observables": {
            "input-1": ["value"]
        }
    }
}
```

Whenever "value" changes, whether from user interaction, "server-update",
or "initial-render", actions get fired.
It implicitly wraps up these events.

The button example would look like this:
```
{
    "output-1": {
        "state": {
            "input-1": ["value"],
            "input-2": ["value"]
        },
        "events": {
            "button-1": ["click"]
        }
    },
    "input-1": {
        "observables": {
            "input-2": ["value"]
        }
    }
}
```

This looks good. Almost too good. Surely I'm missing something.

Let's roll through some more examples.

Displaying hover and click info.
```
{
    "output-1": {
        "observables": {
            "graph-1": ["hoverData", "clickData"]
        }
    }
}
```

- When do we have observerables and state or events? are they mutally exclusive?
- Are there any practical examples besides clicking on elements? Graph hover, click, and select can effectively be serialized as state.
- `dash-renderer` events like `initial-render` and `server-update` are no
  longer exposed. They are wrapped up in the "observerable" concept.
  It's not possible to subscribe to them separately.
  Does this exclude any behaviours?

***

### Python interface to events

The simplest interface just treats
python components as observables,
and passes in all of the properties
(or just the properties that have changed)

```
@app.callback('output-1', ['input-1', 'input-2'])
def update_output(input1, input2):
    value1 = input1['value']
    value2 = input2['value']
```

Yet frequently, you just want the value.
You don't care about any of the other
properties like `style` or `placeholder`.

- By observing single properties, does our dependency chain need to know which properties get returned as part of the output of the callback functions? It might, right? For deferred requests?
- For example, if a callback just update's a dropdown's placeholder, and another output element depends on that dropdown's value, then the output element doesn't need to wait for the callback to finish because it won't affect the input:

```
@app.callback('dropdown-1', ['input-1'])
def update_dropdown(input):
    return {'placeholder': input['value']}

@app.callback('output-1', ['input-1', 'dropdown-1'])
def update_output(input1, dropdown1):
    return {'content': '{}: {}'.format(
        input1['value'], dropdown1['value']
    )}
```

This example implies that we need to specify which
properties we should update both in the input and the output.

What should this look like?

**Dot-separated strings**
```
@app.callback('output-1.content', [
    'input-1.value',
    'input-2.value'
])
def update_output(input1_value, input2_value):
    return '{} - {}'.format(
        input1_value, input2_value
    )
```

**Components**
```
@app.callback(
    Div(id='output-1').props.content,
    [
        Input('input-1').props.value,
        Input('input-2').props.value
    ]
)
def update_output(input1_value, input2_value):
    return '{} - {}'.format(
        input1_value, input2_value
    )
```

**Output, Observable, Event, State Classes**
```
@app.callback(
    Output('output-1', 'content'),
    [
        Observable('input-1', 'value'),
        Observable('input-2', 'value')
    ]
)
def update_output(input1_value, input2_value):
    return '{} - {}'.format(
        input1_value, input2_value
    )
```

"Observable" is a confusing term.

Perhaps it could just be "Input":
```
@app.callback(
    Output('output-1', 'content'),
    [Input('input-1', 'value'),
     Input('input-2', 'value')]
)
def update_output(input1_value, input2_value):
    return '{} - {}'.format(
        input1_value, input2_value
    )
```

You could return multiple values of the element by
passing an array in.
```
@app.callback(
    Output(
        'dropdown-1',
        ['value', 'options']
    ),
    [Input('input-1', 'value'),
     Input('input-2', 'value')]
)
def update_output(input1_value, input2_value):
    options = ...
    return {
        'options': options,
        'value': options[0]['value']
    }
```

Yet that same functionality could be written
in a slightly more composable way
with two different callbacks.

```
@app.callback(Output('dropdown-1', 'options'), [Input('input-1'), Input('input-2')])
def compute_options(input1, input2):
    return {'options': [...]}

@app.callback(
    Output('dropdown-1', 'value'),
    [Input('dropdown-1', 'options')]
)
def compute_value(options):
    return options[0]['value']
```

In fact, we could even allow users to
return multiple outputs from a single
callback.

Consider a double dropdown and a graph.

There would be three ways to write this:

**One function per property**
```
@app.callback(
    Output('dropdown-2', 'options'),
    Input('dropdown-1', 'value')
)
def update_options(value):
    return compute_options(value)

@app.callback(
    Output('dropdown-2', 'value')
    Input('dropdown-2', 'options')
)
def update_value(options):
    return options[0]['value']

@app.callback(
    Output('graph', 'figure'),
    Input('dropdown-1', 'value'),
    Input('dropdown-2', 'value')
)
def update_graph(value1, value2):
    return compute_figure(value1, value2)
```

**One function per component**
```
@app.callback(
    Output('dropdown-2', ['value', 'options']),
    [Input('dropdown-1', 'value')]
)
def update_dropdown2(value):
    options = compute_options(value)
    return {
        'options': options,
        'value': options[0]['value']
    }

@app.callback(
    Output('graph-1', 'figure'),
    [Input('dropdown-2', 'value'),
     Input('dropdown-1', 'value')]
)
def update_graph(value1, value2):
    return {'data': [...], 'layout': {...}}
```

**One function for the entire app**
```
@app.callback(
    Output('graph', 'figure'),
    Output('dropdown-2', 'value'),
    Output('dropdown-2', 'options'),
    Input('dropdown-2', 'value'),
    Input('dropdown-1', 'value')
)
def update_app(val1, val2):
    # very subtle logic here.
    # If `dropdown-2` changed, then
    # it's options are consistent.
    # But if `dropdown-1` changed,
    # then `dropdown-2`'s value is
    # inconsistent, and we need to
    # overwrite it. we also need to
    # compute new options for
    # dropdown-2.
    # If computing options is expensive,
    # then this is unecessarily slow.
    d2_options = compute_options(val1, val2)

    if val2 not in d2_options:
        val2 = d2_options[0]['value']

    figure = compute_graph(val1, val2)

    return {
        # will always change
        'graph': figure,

        # these values will only change
        # if `dropdown-1` changed
        'dropdown-2': {
            'value': val2,
            'options': d2_options
        }
    }
```

What do use? Some considerations:
- Separating the functions out by component is the most intuitive and efficient. It saves a network trip.
- Is there ever a case when you would want to
  update different properties of the same component
  in different callbacks?
- I think only when they have the same inputs.
- That's it: Any functions that have the same input arguments should be placed in the same function. In fact, dash-renderer could optimize this for you!

```
@app.callback(
    Output('div-1', 'content'),
    Input('dropdown-1', 'value')
)
def display_selected_option(value):
    return value

@app.callback(
    Output('graph', 'figure'),
    Input('dropdown-1', 'value')
)
def update_graph(value):
    return compute_figure(value)
```

Users can write these functions under separate
decorators to keep their code modular.
But dash-renderer could make just a single API call
instead of two API calls in parallel.

Will one API call always be better than two?

Actually, no! It's really nice to be able to
update components separately.
Suppose that updating the graph takes a really
long time. That update shouldn't block the
rest of the requests and updates in the
user interface.

The code is so much cleaner when it's modularized
by output component.

***

Let's consider the original examples

```
@app.callback(
    Output('input-1', 'value'),
    Input('input-2', 'value')
)
def update_input1(input2_value):
    return input2_value * 10

@app.callback(
    Output('output-1', 'content'),
    Input('input-1', 'value'),
    Input('input-2', 'value')
)
def update_output(value1, value2):
    return '{} - {}'.format(value1, value2)
```

Protected by a button
```
@app.callback(
    Output('input-1', 'value'),
    Input('input-2', 'value')
)
def update_input1(input2_value):
    return input2_value * 10

@app.callback(
    Output('output-1', 'content'),
    State('input-1', 'value'),
    State('input-2', 'value'),
    Event('button-1', 'click')
)
def update_output(input1_value, input2_value):
    return '{} - {}'.format(value1, value2)
```

- Would `State` ever be used without `Event`?
- Would `Event` ever be used with an `Input`?

Alternative signatures:

```
@app.callback(
    output=[Variable('output-1', 'content')],
    input=[Variable('input-1', 'value')],
    state=[Variable('input-1', 'value')]
)
```

```
@app.callback(
    Output('output-1', 'content'),
    input=[
        Input('input-1', 'value'),
        Input('input-2', 'value')
    ]
)
```

```
@app.callback(
    output=app.prop('output-1', 'content')
    inputs=[app.prop('input-1', 'value'),
            app.prop('input-2', 'value')])
def update_output()
```

A progression of call signatures

Originally:
```
@app.callback('output-1', ['input-1'])
def update_output(input1):
    [...]
```
- Con: Too inflexible: need to specify which properties in the components should update.
- Con: Implicit - argument order matters
- Pro: Terse

***

```
@app.callback('output-1.content', ['input-1.value'])
def update_output(input1):
    [...]
```
- Con: Restrictive - can't have ids or properties with periods in them
- Con: Implicit
- Pro: Terse

***

```
@app.callback(Output('output-1', 'content'), [Input('input-1', 'value')])
def update_output(input1):
    [...]
```
- Pro: Output and Input is expressive
- Pro: Can call `help` on `Output` and `Input`
- Con: `Input` is shared with `dash_html_components` and `dash_core_components`
- Con: Where to put `Event`? Where to put `State`?

```
@app.callback(Output('output-1', 'content'), [
    State('input-1', 'value'), Event('button-1', 'click')
])
def update_output(input1):
    [...]
```
- Con: `Event` doesn't belong in the same list as `State` and `Input` since it
  doesn't get added as an input argument.

***

```
@app.callback(
    Output('output-1', 'content'),
    [State('input-1', 'value'), State('input-2', 'value')],
    [Event('button-1', 'click')]
)
def update_output(input1, input2):
    [...]
```

```
@app.callback(
    Output('output-1', 'content'),
    [State('input-1', 'value'),
     State('input-1', 'style'),
     State('input-2', 'value')],
    [Event('button-1', 'click')]
)
def update_output(input1, input2):
    [...]
```

Imports

```
from dash import Input, Event, State, Output, Dash
import dash_core_components as dcc
import dash_html_components as html

app = Dash()

app.layout = html.Div([
    dcc.Input(id='my-input'),
    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'), [Input('my-input', 'value')])
def update_figure(value):
    return {
        'data': [...],
        'layout': {...}
    }
```

### Validation Checks

**Raise if ids don't exist**
We can check `layout` for the IDs and throw an exception if they don't exist.
If the user is generating the IDs through dynamic components, then we can
provide a method for them to supress the exceptions.

If they suppress the exceptions then we can still show them an error
modal in the front-end if the ID doesn't exist.

**Raise if `State` exists without `Input` or `Events`**
```
@app.callback(Output('my-graph', 'figure'), [State('my-input', 'value')])
def update_figure(value):
    return figure
```

`update_figure` will never get called because only `Input` or `Event`s
fire changes.

### Typeahead
`Input`, `Output`, and `State` are generic across components and so they
don't offer good solutions for typeahead.

They do offer opportunities for validation though, and the error messages
that get raised can include a list of the valid arguments.

And users can call `help` on a component to see the available events and
properties.

```
>>> help(dcc.Input)
An input element.
Available properties: ['value', 'style', 'className', 'type']
Available events: ['input', 'blur']

More on properties:
- value: The displayed value
- style: A dictionary
```
''')
