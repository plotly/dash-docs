# Simple Example with MATCH

library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)


app <- Dash$new()

app$layout(htmlDiv(list(
  htmlButton("Add Filter", id="dynamic-add-filter", n_clicks=0),
  htmlDiv(id="dynamic-dropdown-container", children = list())
)))


app$callback(
  output(id="dynamic-dropdown-container", "children"),
  params = list(
    input("dynamic-add-filter", "n_clicks"),
    state("dynamic-dropdown-container", "children")
  ),
  display_dropdown <- function(n_clicks, children){
    new_element = htmlDiv(list(
      dccDropdown(
        id = list("index" = n_clicks, "type" = "dynamic-dropdown"),
        options = lapply(c("NYC", "MTL", "LA", "TOKYO"), function(x){
          list("label" = x, "value" = x)
        })
      ),
      htmlDiv(
        id = list("index" = n_clicks, "type" = "dynamic-output"),
        children = list()
      )
    ))
    
    children <- c(children, list(new_element))
    return(children)
  }
)


app$callback(
  output(id = list("index" = MATCH, "type" = "dynamic-output"), property= "children"),
  params = list(
    input(id=list("index" = MATCH, "type" = "dynamic-dropdown"), property= "value"),
    state(id=list("index" = MATCH, "type" = "dynamic-dropdown"), property= "id")
  ),
  display_output <- function(value, id){
    return(htmlDiv(sprintf("Dropdown %s = %s", id$index, value)))
  }
)

app$run_server()