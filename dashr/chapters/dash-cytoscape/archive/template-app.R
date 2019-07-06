library(dash)
library(dashHtmlComponents)
library(dashCoreComponents)
library(dashTable)
library(dashCytoscape)

app <- Dash$new()

app$layout(
  htmlDiv(
    list(
      
    )
  )
)

app$run_server()
