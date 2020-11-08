# Simple Example with ALL

library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout(htmlDiv(list(
  htmlButton("Add Filter", id="add-filter", n_clicks=0),
  htmlDiv(id="dropdown-container", children=list()),
  htmlDiv(id="dropdown-container-output")
)))


app$callback(
  output(id="dropdown-container", property = "children"),
  params = list(
    input(id = "add-filter", property = "n_clicks"),
    state(id = "dropdown-container", property = "children")
  ),
  display_dropdowns <- function(n_clicks, children){
    new_dropdown = dccDropdown(
      id=list(
        "index" = n_clicks,
        "type" = "filter-dropdown"
      ),
      options = lapply(c("NYC", "MTL", "LA", "TOKYO"), function(x){
        list("label" = x, "value" = x)
      })
    )
    children[[n_clicks + 1]] <- new_dropdown
    return(children)
  }
)


app$callback(
  output(id="dropdown-container-output", property="children"),
  params = list(
    input(id=list("index" = ALL, "type" = "filter-dropdown"), property= "value")
  ),
  display_output <- function(test){
    ctx <- app$callback_context()
    return(htmlDiv(
      lapply(seq_along(test), function(x){
        return(htmlDiv(sprintf("Dropdown %s = %s", x, test[[x]])))
      })
    ))
  }
)


app$run_server()
