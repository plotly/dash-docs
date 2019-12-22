library(dashBio)
library(readr)

app <- Dash$new()


data = read_file("https://raw.githubusercontent.com/plotly/dash-docs/master/assets/sample_data/alignment_viewer_p53.fasta")

app$layout(htmlDiv(list(
  dashbioAlignmentChart(
    data = data,
    showconsensus = FALSE
  )
)))

app$run_server()
