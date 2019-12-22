
library(dash)
library(dashBio)
library(dashHtmlComponents)
library(dashCoreComponents)


app <- Dash$new()

df <- read.csv(
  file = 'https://raw.githubusercontent.com/plotly/dash-docs/master/assets/sample_data/volcano_data1.csv',
  stringsAsFactors = FALSE
)

app$layout(
  dccGraph(
    id = 'my-dashbio-volcanoplot-color',
    figure = dashbioVolcano(
      dataframe = df,
      point_size=10,
      effect_size_line_width=4,
      genomewideline_width=2
    )
  )
)

app$run_server()
