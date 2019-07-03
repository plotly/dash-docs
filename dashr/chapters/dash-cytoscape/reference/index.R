library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashCytoscape)
library(data.table)

utils <- new.env()
source('dashr/utils.R', local=utils)

layout <- htmlDiv(list(
  htmlH1("Cytoscape Reference"),

  htmlH2("Cytoscape"),
  htmlH3("Properties"),
  utils$generate_table(rbindlist(utils$props_to_list('cytoCytoscape'), fill = TRUE)),

  htmlHr(),
  dccMarkdown("[Back to Cytoscape Documentation](/dash-cytoscape)"),
  dccMarkdown("[Back to Dash Documentation](/)")
))
