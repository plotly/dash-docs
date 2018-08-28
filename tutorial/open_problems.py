import dash_html_components as html
import dash_core_components as dcc


layout = dcc.Markdown('''
# Open Problems

### Links

Navigation can be done through state and events.

For example, consider navigation done through radio items:

```
app.layout = Div([
    RadioItems(options=[
        {'label': i, 'value': i} for i in ['Chapter 1', 'Chapter 2']
    ], value='Chapter 1',
    id='toc'),
    Div(id='body')
])

@app.callback(Output('body', 'content'), [Input('toc', 'value')])
def display_content(chapter):
    if chapter == 'Chapter 1':
        return Div('Welcome to Chapter 1')
    elif chapter == 'Chapter 2':
        return Div('Welcome to Chapter 2')
```

With this, one way that we could provide links would be to sync state
with the URL.

For example, when the app's store's `toc` item would have the value
`Chapter 1`, the URL would get populated with some user-configured
path. To the dash developer, this might look like:


```
app.urls = [
    {
        'id': 'toc',
        'state': [
            {'id': 'toc', 'property': 'value', 'value': 'Chapter 1'}
        ],
        'path': 'chapter-1'
    },
    {
        'id': 'toc',
        'state': [
            {'id': 'toc', 'property': 'value', 'value': 'Chapter 2'}
        ],
        'path': 'chapter-2'
    }
]
```

When the app loads, it will check the path and load the associated state with
that path. For example, if the path is `/chapter-2`, then the app will load
preload the input `toc` with the `Chapter 2` under its `value` property.

Nested paths could be extended by matching several state properties:

```
app.urls = [
    {
        'state': [
            {'id': 'toc', 'property': 'value', 'value': 'Chapter 1'},
            {'id': 'sub-toc', 'property': 'value', 'value': 'Section 1'},
        ],
        'path': 'chapter-1/section-1'
    }
    ...
]
```

This structure lends itself well to stateful link navigation components like
`RadioItems`. But `RadioItems` itself is kind of a hack. A true `<a>` link
is the semantic link element.

While users could use `<a/>` links, the browser will refresh the page when
the user clicks on it, breaking the single-page-app experience
(unless we use `#` URLs but that's not semantic for multi-page apps).

Perhaps we could create a component for setting the URL path.
It's "value" would be the path of the URL. When the URL path changes
within the app, it would get called. Link elements could update its
value when they get clicked.

```
dash.layout = Div([
    A('Chapter 1', href='#chapter-1'),
    A('Chapter 2', href='#chapter-2'),
    Div(id='body'),

    # This "component" doesn't render anything to the dom
    dcc.URLPath(id='url', path='/')
])

@app.callback(Output('body', 'content'), [Input('url', 'path')])
def view(path):
    if '#chapter-1' in path:
        return Div('Welcome to Chapter 1')
    elif '#chapter-2' in path:
        return Div('Welcome to Chapter 2')
```

Stateful content driven by `RadioItems` or `Tabs` would update the URL path
instead of updating the `content` of an item directly. The URL path would then
update the `content` of an item.

```
dash.layout = Div([
    RadioItems(
        id='toc',
        options=[{'label': i, 'value': i} for i in ['Chapter 1', 'Chapter 2']],
        value='Chapter 1'
    ),
    Div(id='body'),

    # This "component" doesn't render anything to the dom
    dcc.URLPath(id='url', path='/')
])

@app.callback(Output('url', 'path'), [Input('toc', 'value')]):
def update_url(value):
    if value == 'Chapter 1':
        return '/chapter-1'
    elif value == 'Chapter 2':
        return '/chapter-2'

@app.callback(Output('body', 'content'), [Input('url', 'path')])
def view(path):
    if path == '/chapter-1'
        return Div('Welcome to Chapter 1')
    elif path == '/chapter-2'
        return Div('Welcome to Chapter 2')
```

This doesn't quite work though. In this case, updating the radio items
will update the URL and changes to the URL will update the content.

However, the initial URL will always be the initial value of the `RadioItems`.
The `RadioItems` component updates the `URLPath` component, not the other way
around.

This is a limitation of `dash`. Two components can't be "synced" up with each
other. Components must depend on each other.

However, `<a/>` links that have non-hashed URLs would still refresh the page.

One way a developer could get around this would be to bind to the `<a/>`s
click event using IDs. Setting multiple links to the same place would be a
little bit annoying.

```
app.layout = Div([
    A('Return to Chapter 1', id='chapter-1-link-1'),
    A('Go back to Chapter 1', id='chapter-1-link-2'),
    A('Back to start', id='chapter-1-link-3'),
    A('Chapter 1', id='chapter-1-link-4'),
    A('Chapter 2', id='chapter-2'),
    Div(id='body'),
    dcc.URLPath(id='url', path='/')
])

@app.callback(Output('body', 'content'), [Input('url', 'path')])
def view(path):
    if path == '/chapter-1'
        return Div('Welcome to Chapter 1')
    elif path == '/chapter-2'
        return Div('Welcome to Chapter 2')

def generate_update_url(url):
    def update_url():
        if url == 'Chapter 1':
            return '/chapter-1'
        elif url == 'Chapter 2':
            return '/chapter-2'
    return update_url

for id in app.layout.keys():
    if 'chapter-1' in id:
        navigation_callback = generate_update_url('Chapter 1')
    elif 'chapter-2' in id:
        navigation_callback = generate_update_url('Chapter 2')

    app.callback(Output('url', 'path'), events=[Event(id, 'click')])(
        navigation_callback
    )
```

That's pretty complex. Setting the IDs in each of the `<a/>` URLs is pretty
cumbersome too.

We could introduce a new single page link element that would modify the
the path of the URL without updating the page. It would be an unsemantic
dash component because it wouldn't require a callback.

```
app.layout = Div([
    dcc.Link('Chapter 1', path='/chapter-1'),
    dcc.Link('Another Link to Chapter 1', path='/chapter-1'),
    Div(id='body'),
    dcc.URLPath(id='url', path='/')
])

@app.callback(Output('body', 'content'), [Input('url', 'path')])
def view(path):
    if path == '/chapter-1'
        return Div('Welcome to Chapter 1')
    elif path == '/chapter-2'
        return Div('Welcome to Chapter 2')
```

That's pretty nice. However, what do we do about other `<a/>` elements
like those that appear in `dcc.Markdown`?
- We can't just override the `<a>`'s `onClick` behaviour because the
  dash developer might be loading content from a different web server.
- The user could set `#` links but we don't want to hijack on-page scroll
  behaviour.
- We could render a custom `<a/>` element inside `dcc.Markdown`.
  How would we know if the URL should reload the page or not?
  By default, we could treat non `https` links as relative links
  and any relative links as SPA links.


### Saving and Loading Views

- If URLs are state, can this tie into multi-page apps?

### Front-end store

- Allow users to modify data through events

### Hotloading

- Use flask-sockets
- Re-run the initialization steps in the front-end
- Tie into general websockets framework?

### Layouts

- Report layout
- App layout
- Container layout

### Authentication and saving

- Oauth
- Keep as much logic in front end so that other languages can just use
  dash-renderer

### ID-Groups

- Register callbacks on groups of elements
- Allows arbitrary number of elements to be created, e.g. TODO MVP

### Caching requests in front end

- Caching on by default, turn it off with a decorator

```
@dash.caching('off')
@dash.callback(...)
def realtime_data(...):
    ...
```

### Finalize variable names

**`Input`, `Output`**
```
from dash.dependencies import Input, Output

from dash.decorators import Input, Output
```

### New Components

**Typeahead Input**
```
@app.callback(
    Input('my-input', 'typeaheadOptions'),
    [Input('my-input', 'value')]
)
def update_typeahead_options(value):
    return get_list_of_options(startsWith=value)[0:5]
```

**Interactive Table**

- Specify types for numbers, decimal places, dates, categories
- Editable
- Sortable

**Date, Time, Week Inputs**

- [http://react-component.github.io/calendar/](http://react-component.github.io/calendar/)

**Upload**


**Tabs**


''')
