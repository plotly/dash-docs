library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashCytoscape)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  #example = utils$LoadExampleCode('dashr/chapters/dash-cytoscape/part7/examples/example.R')
)

layout <- htmlDiv(list(
  htmlH1("Main Title"),

  htmlH2("Subtitle"),
  dccMarkdown("
  Text
  "),
  # Block 0.0
  utils$LoadAndDisplayComponent("htmlH2('BLOCK 0.0 (LoadAndDisplayComponent)')"),
  htmlDetails(
    open = FALSE,
    children = list(
      htmlSummary('View hidden snippet'),
      dccMarkdown("
      Snippet
      ")
    )
  ),

  htmlHr(),
  dccMarkdown("[Back to Cytoscape Documentation](/dash-cytoscape)"),
  dccMarkdown("[Back to Dash Documentation](/)")
))
