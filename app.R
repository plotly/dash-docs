library(dash)

metas <- list(
  list(name = 'description', 
       content = 'Dash for R User Guide and Documentation. Dash is a framework for building analytical web apps in R and Python.')
)

app <- Dash$new(assets_folder="dash_docs/assets", meta_tags = metas)

app$title("Dash for R User Guide and Documentation | R & RStats | Plotly")
