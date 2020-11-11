# TO DO Sample App

library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()


app$layout(htmlDiv(list(
  htmlDiv('Dash To-Do List'),
  dccInput(id = 'new-item'),
  htmlButton("Add", id = "add"),
  htmlButton("Clear Done", id = "clear-done"),
  htmlDiv(id = "list-container"),
  htmlDiv(id = "totals")
)))


style_todo <- list("display" = "inline", "margin" = "10px")
style_done <- list("display" = "inline", "margin" = "10px", "textDecoration" = "line-through", "color" = "#888")


app$callback(
  output = list(
    output("list-container", "children"),
    output("new-item", "value")
  ),
  params = list(
    input("add", "n_clicks"),
    input("new-item", "n_submit"),
    input("clear-done", "n_clicks"),
    state("new-item", "value"),
    state(list("index" = ALL, "type" = "check"), "children"),
    state(list("index" = ALL, "type" = "done"), "value")
  ),
  edit_list <- function(add, add2, clear, new_item, items, items_done) {
    ctx <- app$callback_context()
    triggered <- ifelse(is.null(ctx$triggered$prop_id), " ", ctx$triggered$prop_id)
    adding <- grepl(triggered, "add.n_clicks|new-item.n_submit")
    clearing = grepl(triggered, "clear-done.n_clicks")
    
    # Create a list which we will hydrate with "items" and "items_done"
    new_spec <- list()
    for (i in seq_along(items)) {
      if (!is.null(items[[i]])) {
        new_spec[[length(new_spec) + 1]] <- list(items[[i]], list())
      }
    }
    
    for (i in seq_along(items_done)) {
      if (!is.null(items_done[[i]])) {
        new_spec[[i]][[2]] <- items_done[[i]]
      }
    }
    
    # If clearing, we remove elements from the list which have been marked "done"
    if (clearing) {
      remove_vector <- c()
      for (i in seq_along(new_spec)) {
        if (length(new_spec[[i]][[2]]) > 0) {
          remove_vector <- c(remove_vector, i)
        }
      }
      new_spec <- new_spec[-remove_vector]
    }
    
    # Add a new item to the list
    if (adding) {
      new_spec[[length(new_spec) + 1]] <- list(new_item, list())
    }
    
    # Generate dynamic components with pattern matching IDs
    new_list <- list()
    if (!is.null(unlist(new_spec))) {
      for (i in seq_along(new_spec)) {
        add_list <- list(htmlDiv(list(
          dccChecklist(
            id = list("index" = i, "type" = "done"),
            options = list(
              list("label" = "", "value" = "done")
            ),
            value = new_spec[[i]][[2]],
            style = list("display" = "inline"),
            labelStyle = list("display" = "inline")
          ),
          htmlDiv(new_spec[[i]][[1]], id = list("index" = i, "type" = "check"), style = if (length(new_spec[[i]][[2]]) == 0) style_todo else style_done)
        ), style = list("clear" = "both")))
        new_list <- c(new_list, add_list)
      }
      return(list(new_list, ""))
    } else {
      return(list(list(), ""))
    }
  }
)

app$callback(
  output(id = list("index" = MATCH, "type" = "check"), property = "style"),
  params = list(
    input(id = list("index" = MATCH, "type" = "done"), property = "value")
  ),
  mark_done <- function(done){
    if (length(done[[1]] > 0)) return(style_done) else return(style_todo)
  }
)


app$callback(
  output(id = "totals", property = "children"),
  params = list(
    input(list("index" = ALL, "type" = "done"), property = "value"),
    state(list("index" = ALL, "type" = "check"), property = "children")
  ),
  show_totals <- function(done, total) {
    count_all = length(total)
    count_done = length(done)
    
    result = sprintf("%s of %s items completed", count_done, count_all)
    
    if (count_all > 0) {
      result = paste(result, sprintf(" - %s%%", as.integer(100 * count_done/count_all)))
    }
    
    if (is.null(total[[1]])) {
      return("Add an item to the list to get started.")
    } else {
      return(result)
    }
  }
)


app$run_server()
