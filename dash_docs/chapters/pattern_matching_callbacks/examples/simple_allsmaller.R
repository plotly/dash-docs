# Example with ALLSMALLER 

library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)


df <- read.csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv', stringsAsFactors = FALSE)


app <- Dash$new()

app$layout(htmlDiv(list(
  htmlButton("Add Filter", id = "add-filter-ex3", n_clicks = 0),
  htmlDiv(id = "container-ex3", children = list())
)))


app$callback(
  output('container-ex3', 'children'),
  params = list(
    input('add-filter-ex3', 'n_clicks'),
    state('container-ex3', 'children')
  ),
  display_dropdowns <- function(n_clicks, existing_children){
    new_children <- htmlDiv(list(
      dccDropdown(
        id = list("index" = n_clicks, "type" = "filter-dropdown-ex3"),
        options = lapply(unique(df$country), function(x){
          list("label" = x, "value" = x)
        }),
        value = unique(df$country)[n_clicks + 1]
      ),
      htmlDiv(id = list("index" = n_clicks, "type" = "output-ex3"), children = list(unique(df$country)[n_clicks + 1]))
    ))
    
    existing_children <- c(existing_children, list(new_children))
  }
)


app$callback(
  output(id = list("type" = "output-ex3", "index" = MATCH), property = "children"),
  params = list(
    input(id = list("type" = "filter-dropdown-ex3", "index" = MATCH), property = "value"),
    input(id = list("type" = "filter-dropdown-ex3", "index" = ALLSMALLER), property = "value")
  ),
  display_output <- function(matching_value, previous_values){
    previous_values_in_reversed_order = rev(previous_values)
    all_values = c(matching_value, previous_values_in_reversed_order)
    all_values = unlist(all_values)
    
    dff = df[df$country %in% all_values,]
    avgLifeExp = round(mean(dff$lifeExp), digits = 2)
    
    if (length(all_values) == 1) {
      return(
        htmlDiv(sprintf("%s is the life expectancy of %s.", avgLifeExp, matching_value))
      )
    } else if (length(all_values) == 2) {
      return(
        htmlDiv(sprintf("%s is the life expectancy of %s.", avgLifeExp, paste(all_values, collapse = " and ")))
      )
    } else {
      return(
        htmlDiv(sprintf("%s is the life expectancy of %s, and %s.", avgLifeExp, paste(all_values[-length(all_values)], collapse = " , "), paste(all_values[length(all_values)])))
      )
    }
  }
)

app$run_server()
