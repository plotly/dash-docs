library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashTable)
library(data.table)

utils <- new.env()
source('dashr/utils.R', local=utils)

layout <- htmlDiv(list(
  htmlH1("DashTable Reference"),

  htmlH2("DashTable Properties"),
  utils$generate_table(rbindlist(utils$props_to_list('dashDataTable'), fill = TRUE)),

  htmlHr(),
  dccMarkdown("[Back to DataTable Documentation](/datatable)"),
  dccMarkdown("[Back to Dash Documentation](/)")
))
