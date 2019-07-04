library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  two_inputs=utils$LoadExampleCode('dashr/chapters/state/examples/two_inputs.R'),
  one_input_two_states=utils$LoadExampleCode('dashr/chapters/state/examples/one_input_two_states.R')
)



layout <- htmlDiv(list(
  htmlH1('Dash State'),
  dccMarkdown("
> This is the 4th chapter of the
> Dash Tutorial.
> The [previous chapter](/getting-started-part-2) covered Dash
> Callbacks and the [next chapter](/state)
> covers interactive graphing and
> crossfiltering.
> Just getting started?
> Make sure to
> [install the necessary dependencies](/installation).

In the previous chapter on [basic Dash callbacks](/getting-started-part-2),
our callbacks looked something like:
"),
  #example of two inputs
  examples$two_inputs$source,
  examples$two_inputs$layout,

  dccMarkdown("
In this example, the callback function is fired whenever any of the
attributes described by the `input` change.
Try it for yourself by entering data in the inputs above.

`state` allows you to pass along extra values without
firing the callbacks. Here's the same example as above but with the
`dccInput` as `state` and a button as
`input`.    
  "),
  
  #example of one input and two states
  examples$one_input_two_states$source,
  examples$one_input_two_states$layout,
  
  dccMarkdown("
In this example, changing text in the `dccInput` boxes won't fire
the callback but clicking on the button will. The current values of
the `dccInput` values are still passed into the callback even though
they don't trigger the callback function itself.

Note that we're triggering the callback by listening to the
`n_clicks` property of the `htmlButton` component. `n_clicks` is a
property that gets incremented every time the component has been
clicked on. It is available in every component in the
`dashHtmlComponents` package.  
  "),
  
  dccMarkdown("
***

The next chapter of the user guide explains how to use callback
principles with the `dccGraph` component
to make applications that
respond to interactions with graphs on the page.
  "),
  
  dccLink(
    'Dash Tutorial Part 5. Interactive Graphing',
    href='/graph-crossfiltering'
  ),
  
  htmlHr(),
  dccMarkdown("
[Back to the Table of Contents](/)
              ")
  )
)
