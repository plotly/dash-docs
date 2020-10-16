library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dash_docs/utils.R', local=utils)

examples <- list(
  simple_all=utils$LoadExampleCode('dash_docs/chapters/pattern_matching_callbacks/examples/simple_all.R'),
  simple_match=utils$LoadExampleCode('dash_docs/chapters/pattern_matching_callbacks/examples/simple_match.R'),
  simple_allsmaller=utils$LoadExampleCode('dash_docs/chapters/pattern_matching_callbacks/examples/simple_allsmaller.R'),
  todo=utils$LoadExampleCode('dash_docs/chapters/pattern_matching_callbacks/examples/todo.R')
)

layout <- htmlDiv(list(
    dccMarkdown("
# Pattern Matching Callbacks
The pattern-matching callback selectors `MATCH`, `ALL`, & `ALLSMALLER`
allow you to write callbacks that respond to or update an
arbitrary or dynamic number of components.

## Simple Example with `ALL`

This example renders an arbitrary number of `dccDropdown` elements
and the callback is fired whenever any of the `dccDropdown` elements
change. Try adding a few dropdowns and selecting their values to see how
the app updates.
  "),
    examples$simple_all$source_code,
    examples$simple_all$layout,

    dccMarkdown("
Some notes about this example:
- Notice how the `id` in `dccDropdown` is a _named list_ rather than a _string_.
This is a new feature that we enabled for pattern-matching callbacks
(previously, IDs had to be strings).
- In our second callback, we have ` input(id=list('index' = ALL, 'type' = 'filter-dropdown'), property= 'value')`.
This means 'match any input that has an ID list where `'type'` is `'filter-dropdown'`
and `'index'` is _anything_. Whenever the `value` property of any of the
dropdowns change, send _all_ of their values to the callback.'
- The names & values of the ID list (`type`, `index`, `filter-dropdown`)
are arbitrary. This could've be named `list('foo' = 'bar', 'baz' = n_clicks)`.
- However, for readability, we recommend using names like `type`, `index`, or `id`.
`type` can be used to refer to the class or set dynamic components and
`index` or `id` could be used to refer _which_ component you are matching
within that set. In this example, we just have a single set of dynamic
components but you may have multiple sets of dynamic components in more
complex apps or if you are using `MATCH` (see below).
- In fact, in this example, we didn't actually _need_ `'type' = 'filter-dropdown'`.
The same callback would have worked with `Input(list('index'= ALL), 'value')`.
We included `'type' = 'filter-dropdown'` as an extra specifier in case you
create multiple sets of dynamic components.
- The component properties themselves (e.g. `value`) cannot be matched by
a pattern, only the IDs are dynamic.
- This example uses a common pattern with `State` - the currently displayed
set of dropdowns within the `dropdown-container` component are passed into
the callback when the button is clicked. Within the callback, the new
dropdown is appended to the list and then returned.
- You can also use `app$callback_context` to access the inputs and state
and to know which input changed.
Here is what that data might look like with two dropdowns rendered on the page.

- `app$callback_context$triggered`. Note that the `prop_id` is a stringified named list with no whitespace.
```
{
'prop_id': '{\'index\':0,\'type\':\'filter-dropdown\'}.value',
  'value': [
    NYC
  ]
}
```
- `dash.callback_context.inputs`. Note that the name is a stringified named list with no whitespace.
```
{
  '{\'index\':0,\'type\':\'filter-dropdown\'}.value : NYC',
  '{\'index\':1,\'type\':\'filter-dropdown\'}.value : LA'
}
```
  "),

    dccMarkdown("
## Simple Example with `MATCH`

Like `ALL`, `MATCH` will fire the callback when any of the
component's properties change. However, instead of passing _all_ of the
values into the callback, `MATCH` will pass just a single value into the
callback. Instead of updating a single output, it will update the dynamic
output that is 'matched' with.
  "),
    examples$simple_match$source_code,
    examples$simple_match$layout,

    
    dccMarkdown("
Notes about this example:
- The `display_dropdown` callback returns two elements with the _same_
`index`: a dropdown and a div.
- The second callback uses the `MATCH` selector. With this selector,
we're asking Dash to:

  1. Fire the callback whenever the `value` property of any component
  with the id `'type' = 'dynamic-dropdown'` changes:
  `input(id=list('index' = MATCH, 'type' = 'dynamic-dropdown'), property= 'value')`
  2. Update the component with the id `'type' = 'dynamic-output'`
  and the `index` that _matches_ the same `index` of the input:
  `Output(id=list('index' = MATCH, 'type' = 'dynamic-output'), property= 'children')`
  3. Pass along the `id` of the dropdown into the callback:
  `state(id=list('index' = MATCH, 'type' = 'dynamic-dropdown'), property= 'id')`
- With the `MATCH` selector, only a _single_ value is passed into the callback
for each `Input` or `State`. This is unlike the previous example with the
`ALL` selector where Dash passed _all_ of the values into the callback.
- Notice how it's important to design ID named lists that 'line up' the
inputs with outputs. The `MATCH` contract is that Dash will update
whichever output has the same dynamic ID as the id. In this case, the
'dynamic ID' is the value of the `index` and we've designed our layout to
return dropdowns & divs with identical values of `index`.
- In some cases, it may be important to know _which_ dynamic component changed.
As above, you can access this by setting `id` as `State` in the callback.
- You can also use `app$callback_context` to access the inputs and state
and to know which input changed. 
Here is what that data might look like with two dropdowns rendered on the page after
we change the first dropdown.
  - `app$callback_context$triggered`. Note that the `prop_id` is a stringified named list with no whitespace.
  ```
{
'prop_id': '{\'index\':0,\'type\':\'dynamic-dropdown\'}.value',
  'value': [
    NYC
  ]
}
  ```
  - `app$callback_context$inputs`. Note that the key is a stringified named list with no whitespace.
  ```
{
  '{\'index\':0,\'type\':\'filter-dropdown\'}.value : NYC'
}
  ```
  "),
    
    dccMarkdown("
## Simple Example with `ALLSMALLER`

In the example below, `ALLSMALLER` is used to pass in the values of
all of the dropdowns on the page that have an index smaller than the
index corresponding to the div.

The user interface in the example below displays filter results that are
increasingly specific in each as we apply each additional dropdown.

`ALLSMALLER` can only be used in `Input` and `State` items, and
must be used on a key that has `MATCH` in the `Output` item(s).

`ALLSMALLER` it isn't always necessary (you can usually use `ALL` and
filter out the indices in your callback) but it will make your logic simpler.
  "),
    examples$simple_allsmaller$source_code,
    examples$simple_allsmaller$layout,
    
    dccMarkdown("
- In the example above, try adding a few filters and then change the first
dropdown. Notice how changing this dropdown will update the text
of each `htmlDiv` that has an index that depends on that dropdown.
- That is, each `htmlDiv` will get updated whenever any of the
dropdowns with an `index` smaller than it has changed.
- So, if there are 10 filters added and the first dropdown has changed, Dash
will fire your callback 10 times, once to update each `htmlDiv` that depends
on the `dccDropdown` that changed.
- As above, you can also use `app$callback_context` to access the inputs and state
and to know which input changed.
Here is what that data might look like when updating the second div
with two dropdowns rendered on the page after we change the first dropdown.
  - `app$callback_context$triggered`. Note that the `prop_id` is a stringified named list with no whitespace.
  ```
{
'prop_id': '{\'index\':0,\'type\':\'filter-dropdown-ex3\'}.value',
  'value': Canada
  ]
}
  ```
  - `app$callback_context$inputs`. Note that the key is a stringified named list with no whitespace.
  ```
{
  '{\'index\':1,\'type\':\'filter-dropdown-ex3\'}.value : Albania',
  '{\'index\':0,\'type\':\'filter-dropdown-ex3\'}.value : Canada'
}
  ```
'''
  "),
    dccMarkdown("
## ToDo App

Creating a ToDo App is a classic UI exercise in that demonstrates many
features in common 'create, read, update and delete' (CRUD) applications.
  "),
    examples$todo$source_code,
    examples$todo$layout,

    htmlHr(),
    dccMarkdown("
[Back to the Table of Contents](/)
   ")
  )
)
