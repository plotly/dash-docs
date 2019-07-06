library(dashCoreComponents)
library(dashHtmlComponents)
library(dash)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  radioitemsproptable = utils$LoadExampleCode('dashr/chapters/dash-core-components/RadioItems/examples/radioitemsproptable.R')
)

layout = htmlDiv(list(
  htmlH3('Radio Items Properties'),
  examples$radioitemsproptable$layout,
  
  htmlHr(),
  dccMarkdown("
              [Back to the Table of Contents](/)
              ")
))
