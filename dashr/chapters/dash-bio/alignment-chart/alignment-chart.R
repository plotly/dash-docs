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
source('assets/styles.R')
source('assets/utils.R')
source('assets/utils.R', local=utils)


examples <- list(
  defaultAlignmentChart=utils$LoadExampleCode('alignment-chart/examples/defaultAlignmentChart.R'),
  colorScaleAlignmentChart=utils$LoadExampleCode('alignment-chart/examples/colorscaleAlignmentChart.R'),
  hideBarPlots=utils$LoadExampleCode('alignment-chart/examples/hideBarPlots.R'),
  tileAlignmentChart=utils$LoadExampleCode('alignment-chart/examples/tileAlignmentChart.R'),
  consensusAlignmentChart=utils$LoadExampleCode('alignment-chart/examples/consensusAlignmentChart.R')
)

# Header and Introduction

header <- htmlDiv(list(
  htmlDiv(list(
    htmlDiv(list(
      htmlA(className = "logo-link", href = "https://plot.ly/products/dash",
            children= htmlImg(src="assets/logo.png",
                              style = list("height" = "60px", "width" = "230px"))),
      htmlDiv(className = "links", children = list(
        htmlA(className = "link", children = "pricing", href = "https://plot.ly/dash/pricing?_ga=2.241429382.584183071.1559580389-2135338473.1556993734"),
        htmlA(className = 'link', children = 'user guide', href = "/"),
        htmlA(className = 'link', children = 'plotly', href = "https://plot.ly/"),
        htmlA(className = 'link', href="https://dash.plot.ly/search", children = 
                htmlI(className = 'fa fa-search'))
        
      ))
    ))
  ), className = 'container-width')
), className = "header")


dashbio_intro <- htmlDiv(list(
  dccMarkdown('# AlignmentChart Examples and Reference'),
  
  
  dccMarkdown('
  See AlignmentChart in action [here](https://dash-bio.plotly.host/dash-alignment-viewer/)
  ')
))


# Individual Components and Examples


defaultAlignment <- htmlDiv(list(
  dccMarkdown('## Default Alignment Chart'),
  htmlP('An example of a default alignment chart component without any extra properties.'),
  htmlDiv(list(
    examples$defaultAlignmentChart$source_code,
    examples$defaultAlignmentChart$layout))
))


colorscaleAlignment <-  htmlDiv(list(
  dccMarkdown('## Color Scales'),
  htmlP('The colors used for the heatmap can be changed by adjusting the colorscale property.'),
  htmlDiv(list(
    examples$colorScaleAlignmentChart$source_code,
    examples$colorScaleAlignmentChart$layout))
))


hideAlignment <-  htmlDiv(list(
  dccMarkdown('## Show/Hide Barplots'),
  htmlP('Enable or disable the secondary bar plots for gaps and conservation.'),
  htmlDiv(list(
    examples$hideBarPlots$source_code,
    examples$hideBarPlots$layout))
))


tileAlignment <-  htmlDiv(list(
  dccMarkdown('## Tile Size'),
  htmlP('Change the height and/or width of the tiles.'),
  htmlDiv(list(
    examples$tileAlignmentChart$source_code,
    examples$tileAlignmentChart$layout))
))


consensusAlignment <-  htmlDiv(list(
  dccMarkdown('## Consensus Sequence'),
  htmlP('Toggle the display of the consensus sequence at the bottom of the heatmap.'),
  htmlDiv(list(
    examples$consensusAlignmentChart$source_code,
    examples$consensusAlignmentChart$layout))
))



library(dashTable)


alignmentprops <- propsToList("dashbioAlignmentChart")

alignmentPropsDF <- rbindlist(alignmentprops, fill = TRUE)

alignmentPropsTable <- generate_props_table(alignmentPropsDF)


# Main docs layout

layout <- htmlDiv(list(

      dashbio_intro,
      htmlHr(),
      defaultAlignment,
      colorscaleAlignment,
      hideAlignment,
      tileAlignment,
      consensusAlignment,
      dccMarkdown('## AlignmentChart Properties'),
      alignmentPropsTable,
      htmlA("Back to the Table of Contents", href = "/")
))






