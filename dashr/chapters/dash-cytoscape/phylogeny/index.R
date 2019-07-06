library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashCytoscape)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  #example = utils$LoadExampleCode('dashr/chapters/dash-cytoscape/phylogeny/examples/example.R')
)

layout <- htmlDiv(list(
  htmlH1("Main Title"),

  htmlH2("Subtitle"),
  dccMarkdown("
  Sample Text
  "),
  # Block 6.1
  utils$LoadAndDisplayComponent("htmlH2('BLOCK 6.1 (LoadAndDisplayComponent)')"),

  htmlHr(),
  dccMarkdown("[Back to Cytoscape Documentation](/cytoscape)"),
  dccMarkdown("[Back to Dash Documentation](/)")
))
