library(dashCoreComponents)
library(dashHtmlComponents)
library(dash)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  storeclick = utils$LoadExampleCode('dashr/chapters/dash-core-components/Store/examples/storeclick.R'),
  sharecallback = utils$LoadExampleCode('dashr/chapters/dash-core-components/Store/examples/sharecallbacks.R'),
  storeproptable = utils$LoadExampleCode('dashr/chapters/dash-core-components/Store/examples/storeproptable.R')
  
)

layout <- htmlDiv(list(
htmlH1('Store component'),
dccMarkdown("
Store json data in the browser.
## limitations.
- The store will not work properly if there is no callback associated.
- `modified_timestamp` is read only.
### local/session specifics
- The store will not work properly if it's not included in the initial layout.
- The total data of all stores should not exceed 10MB.
### Retrieving the initial store data
If you use the `data` prop as an output, you cannot get the
initial data on load with the `data` prop. To counter this,
you can use the `modified_timestamp` as `Input` and the `data` as `State`.
This limitation is due to the initial None callbacks blocking the true
data callback in the request queue.
See https://github.com/plotly/dash-renderer/pull/81 for further discussion.
                 ))
"),

htmlH2('Store clicks example'),

examples$storeclick$source,
examples$storeclick$layout,

htmlH2('Share data between callbacks'),
examples$sharecallback$source,
examples$sharecallback$layout,

examples$storeproptable$layout
  
  
))
