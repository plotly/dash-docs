library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dash_docs/utils.R', local=utils)

layout <- htmlDiv(list(
  htmlH1('Server Routes and Redirects'),
  dccMarkdown("
As covered in the [`Deployment Chapter`](deployment), 
Dash for R uses the Fiery web framework under the hood.
Fiery leverages the `routr` package to handle routing.
While it's possible to access this directly via
`app$server$attach` and `server$plugins$request_routr`, 
we've added some convenience methods that are more
user-friendly for redirects and other user-defined routes.

The `server_route` method takes three arguments: a `path`
which references the URL for which routing should be performed,
a `handler` function that instructs Dash how to handle requests
for that path, and (optionally) the `methods` supported for
the request. If you don't specify `methods`, Dash will assume
that the desired method is `get`.

The URL path is composed of strings, parameters (strings
prefixed with `:`), and wildcards (`*`) which are separated
by `/`. The wildcards allow you to match any path element,
while parameters allow you to reuse a segment of the path
as a variable within your handler function.

Let's see this in action using a simple example. Here we
set up a temporary redirect (HTTP status code `307`) for
requests to `/getting-started` to the path `/layout`
instead:


```r
    library(dash)
    library(dashCoreComponents)
    library(dashHtmlComponents)

    app <- Dash$new()

    app$server_route('/getting-started', function(request, response, keys, ...) {
      response$status <- 307L
      response$set_header('Location', '/layout')
      TRUE
    })
```

The handler must return `TRUE` (indicating that the next route handler in the stack
should be called), or `FALSE` (if no further route handlers should be called). An
in-depth discussion of [`routr`](https://cran.r-project.org/package=routr) and its interface
is available [here](https://www.data-imaginist.com/2017/introducing-routr/).

We could also incorporate a wildcard to handle subpaths -
in this case redirecting `/getting-started/` with anything
after it to just `/layout`:


```r
    app$server_route('/getting-started/*', function(request, response, keys, ...) {
      response$status <- 307L
      response$set_header('Location', '/layout')
      TRUE
    })
```


If we had wanted to use a parameter as well, here's an
example of that syntax. In this case, we capture the
subpath within `/accounts`, and reuse it as `user_id`
within the handler. We need to prepend the parameter
with `keys`, since internally this is how `routr` will
expect the handler to be formatted:


```r
    app$server_route('/accounts/:user_id/*', function(request, response, keys, ...) {
      response$status <- 307L
      response$set_header('Location', paste0('/users/', keys$user_id))
      TRUE
    })
```

---

## Adding redirects to your Dash application

While the `server_route` method is powerful and easy to
use, if you're just looking to add permanent redirects from
one path to another, Dash also supports a simple `redirect`
method.

Like `server_route`, the `redirect` method takes three
arguments. The `old_path` argument specifies the path to
redirect, while `new_path` accepts either the path to
which requests should be rerouted or a function that is
used to construct it, and `methods` works exactly as
above (with `get` as its default option).

For a simple path-to-path redirect, this syntax is as
concise as it gets. Here we redirect all traffic from
`/getting-started` to `/layout`, while returning a
`301` HTTP status code.


```r
app$redirect('/getting-started', '/layout')
```


If we want to add a wildcard, the above statement changes
slightly:


```r
app$redirect('/getting-started/*', '/layout/*')
```


If we had decided to use a parameterized redirect, while 
creating the new path dynamically from the parameter,
we would pass a function instead of a character string
for `new_path`:


```r
app$redirect('/accounts/:user_id/*', function(keys) paste0('/users/', keys$user_id))
```
  "),
htmlHr(),
dccMarkdown("
[Back to the Table of Contents](/)
              ")
))
