library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(jsonlite)
library(readr)
library(heatmaply)
library(data.table)
library(dashTable)


utils <- new.env()
source('dashr/styles.R')
source('dashr/utils.R')
source('dashr/utils.R', local=utils)


examples <- list(
  defaultManhattan=utils$LoadExampleCode('dashr/chapters/dash-bio/manhattan/examples/defaultManhattan.R')
)


dashbio_intro <- htmlDiv(list(
  dccMarkdown('# ManhattanPlot Examples and Reference'),
  
  
  dccMarkdown('
  See ManhattanPlot in action [here](https://dash-bio.plotly.host/dash-manhattan-plot/)
  ')
))


# Individual Components and Examples


defaultManhattan <- htmlDiv(list(
  dccMarkdown('## Default ManhattanPlot'),
  htmlP('An example of a default ManhattanPlot component without any extra properties.'),
  htmlDiv(list(
    examples$defaultManhattan$source_code,
    examples$defaultManhattan$layout))
))


lineColors <- htmlDiv(list(
  dccMarkdown('## Line Colors'),
  htmlP('Change the colors of the suggestive line and the genome-wide line.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

data = read.table("assets/sample_data/manhattan_data.csv",
                  header = TRUE, sep = ",")

dccGraph(
  figure = dashbioManhattan(
    dataframe = data,
    suggestiveline_color = "#AA00AA",
    genomewideline_color = "#AA5500"
  )
)
    '
  )
))



highlightedPoints <- htmlDiv(list(
  dccMarkdown('## Highlighted Points Color'),
  htmlP('Change the color of the points that are considered significant.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

data = read.table("assets/sample_data/manhattan_data.csv",
                  header = TRUE, sep = ",")

dccGraph(
  figure = dashbioManhattan(
    dataframe = data,
    highlight_color = "#00FFAA"
  )
)
    '
  )
))



manhattanProps <- props_to_list("dashbioManhattan")

manhattanPropsDF <- rbindlist(manhattanProps, fill = TRUE)

manhattanPropsTable <- generate_props_table(manhattanPropsDF)



# Main docs layout

layout <- htmlDiv(list(
  
  dashbio_intro,
  htmlHr(),
  defaultManhattan,
  htmlHr(),
  lineColors,
  htmlHr(),
  highlightedPoints,
  htmlHr(),
  dccMarkdown('## ManhattanPlot Properties'),
  manhattanPropsTable,
  htmlA("Back to the Table of Contents", href = "/dash-bio/")
))



