library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  simple_example=utils$LoadExampleCode('dashr/chapters/dash-core-components/dropdown/examples/simple-example.R')
)


layout <- htmlDiv(list(
htmlH1('dccDropdown - Examples & Reference'),
htmlHr(),

dccMarkdown('
# Default Dropdown

An example of a default dropdown without any extra properties.
'),
examples$simple_example$source_code,
examples$simple_example$layout,

dccMarkdown('
***

## Multi-Value Dropdown

A dropdown component with the `multi` property set to `TRUE`
will allow the user to select more than one value at a time.
'),
utils$LoadAndDisplayComponent(
'
dccDropdown(
  options=list(
    list(label="New York City", value="NYC"),
    list(label="Montréal", value="MTL"),
    list(label="San Francisco", value="SF")
  ),
  value=list("MTL", "NYC"),
  multi=TRUE
)
'
)

))
