library(dash)

metas <- list(
  list(name = 'description', 
       content = 'Dash User Guide and Documentation. Dash is a framework for building analytical web apps in Python and R.')
)

app <- Dash$new(name = "Dash User Guide and Documentation - Dash by Plotly",
                meta_tags = metas)
