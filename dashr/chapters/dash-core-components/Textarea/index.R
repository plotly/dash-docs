library(dashCoreComponents)
library(dashHtmlComponents)
library(dash)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  textarea = utils$LoadExampleCode('dashr/chapters/dash-core-components/Textarea/examples/textareaproptable.R')
)

layout = htmlDiv(list(
  htmlH3('Textarea Properties'),
  examples$textarea$layout,
  
  htmlHr(),
  dccMarkdown("
[Back to the Table of Contents](/)
              ")
))
