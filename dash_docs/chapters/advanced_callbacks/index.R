library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dash_docs/utils.R', local=utils)

examples <- list(
  prevent_update_button=utils$LoadExampleCode('dash_docs/chapters/advanced_callbacks/examples/prevent_update_button.R'),
  prevent_update=utils$LoadExampleCode('dash_docs/chapters/advanced_callbacks/examples/prevent_update.R'),
  last_clicked_button=utils$LoadExampleCode('dash_docs/chapters/advanced_callbacks/examples/last_clicked_button.R')
)

layout <- htmlDiv(
  list(
    # htmlH1('Advanced Callbacks'),
    dccMarkdown("
## Catching errors with `dashNoUpdate()`
In certain situations, you don't want to update the callback output. You can
achieve this by returning a `dashNoUpdate()` in the callback function.
  "),
    
    examples$prevent_update_button$source_code,
    examples$prevent_update_button$layout,
    
    dccMarkdown("
## Displaying errors with `dashNoUpdate()`
This example illustrates how you can show an error while keeping the previous
input, using `dashNoUpdate()` to update the output partially.
  "),
    
    examples$prevent_update$source_code,
    examples$prevent_update$layout,
    
    dccMarkdown("
## Determining which `Input` has fired with `callback_context()`
In addition to event properties like `n_clicks` that change whenever 
an event happens (in this case a click), there is a global variable 
`app$callback_context()`, available only inside a callback. It has properties:

  - `triggered`:  list of changed properties. 
This will be empty on initial load, unless an `input` prop got its value from 
another initial callback. 
After a user action it is a length-1 list, 
unless two properties of a single component update simultaneously, 
such as a value and a timestamp or event counter.

   - `inputs` and `states`: allow you to access the callback params by id and prop instead of through the function args. 
These have the form of dictionarie `app$callback_context()$triggered$value`

Here's an example of how this can be done:
  "),
    
    examples$last_clicked_button$source,
    examples$last_clicked_button$layout,
    
    dccMarkdown("
### Legacy behavior: Using timestamps
Prior to the addition of `callback_context`, you needed to compare timestamp properties 
like `n_clicks_timestamp` to find the most recent click. 
While existing uses of `*_timestamp` continue to work for now, this approach is deprecated, 
and may be removed in a future update. The one exception is `modified_timestamp` from `dccStore`, 
which is safe to use, it is NOT deprecated.
  "),
    
    dccMarkdown("
## Improving performance with memoization
Memoization allows you to bypass long computations by storing the results of function calls.

To better understand how memoization works, let's start with a simple example.
  "),
    
    dccMarkdown("
```r
library(memoise)

# We can start by memoising the function sys.sleep
memoised_sleep <- memoise::memoise(Sys.sleep)
  
# The first time it is called will take the full 10 seconds
memoised_sleep(10)
    
# The second time it will instantly execute.
memoised_sleep(10)
```
    "),
    
    dccMarkdown("
Calling `memoised_sleep(10)` the first time will take 10 seconds.
Calling it a second time with the same argument will take almost no time
since the previously computed result was saved in memory and reused.

The [Performance](/performance) section of the Dash docs delves a
little deeper into leveraging multiple processes and threads in
conjunction with memoization to further improve performance.
"),
    
    htmlHr(),
    dccMarkdown("
[Back to the Table of Contents](/)
                ")
  )
)