library(dashCoreComponents)
library(dashHtmlComponents)
library(dash)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  loading = utils$LoadExampleCode('dashr/chapters/dash-core-components/LoadingComponent/examples/loading.R'),
  loadingproptable = utils$LoadExampleCode('dashr/chapters/dash-core-components/LoadingComponent/examples/loadingcomponentproptable.R')
  
)

layout <- htmlDiv(list(
htmlH1('Loading Component'),
  
dccMarkdown("
Here’s a simple example that wraps the outputs for a couple of `Input` components in the `Loading` component. As you can see, you can define the type of spinner you would like to show (refer to the reference table below for all possible types of spinners).
You can modify other attributes as well, such as `fullscreen=True` if you would like the spinner to be displayed fullscreen. Notice that, the Loading component traverses all
of it's children to find a loading state, as demonstrated in the second callback, so that even nested children will get picked up.
                 "),

examples$loading$source,
examples$loading$layout,

examples$loadingproptable$layout
  
  
))
