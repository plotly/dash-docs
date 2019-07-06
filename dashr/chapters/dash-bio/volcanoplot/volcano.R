library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(dashTable)

# app <- Dash$new()

utils <- new.env()
source('dashr/styles.R')
source('dashr/utils.R')
source('dashr/utils.R', local=utils)


examples <- list(
  default = utils$LoadExampleCode('dashr/chapters/dash-bio/volcanoplot/examples/default.R'),
  colors = utils$LoadExampleCode('dashr/chapters/dash-bio/volcanoplot/examples/colors.R'),
  # colorsPseudo = utils$LoadExampleCode('volcanoplot/examples/colorsPseudo.R'),
  pointSizesLineWidths = utils$LoadExampleCode('dashr/chapters/dash-bio/volcanoplot/examples/pointSizesLineWidths.R'),
  # pointSizesLineWidthsPseudo = utils$LoadExampleCode('volcanoplot/examples/pointSizesLineWidthsPseudo.R'),
  table = utils$LoadExampleCode('dashr/chapters/dash-bio/volcanoplot/examples/table.R')
)

layout <- htmlDiv(
  list(
    dccMarkdown("
# VolcanoPlot Examples and Reference
                
See Volcano Plot in action 
[here](https://dash-bio.plotly.host/dash-volcano-plot/).
                "),
    
    htmlHr(),
    
    dccMarkdown("
## Default Volcano Plot

An example of a default volcano plot component without any extra properties.                
                "),
    
    examples$default$source,
    examples$default$layout,
    
    htmlHr(),
    
    dccMarkdown("
## Colors

Choose the colors of the scatter plot points, the highlighted points, 
the genome-wide line, and the effect size lines.                  
                "),
    
    examples$colorsPseudo$source,
    examples$colors$layout,
    
    htmlHr(),
    
    dccMarkdown("
## Point Sizes And Line Widths
Change the size of the points on the scatter plot 
and the widths of the effect lines and genome-wide line. 
                "),
    
    examples$pointSizesLineWidthsPseudo$source,
    examples$pointSizesLineWidths$layout,
    
    htmlHr(),
    
    dccMarkdown("
## VolcanoPlot Properties
                "),
    
    examples$table$layout,
    
    htmlHr(),
    dccMarkdown("
[Back to the Dash Documentation](/dash-bio/)
                ")
    
  )
)

# app$layout(htmlDiv(list(
#   layout
# )))
# 
# 
#  app$run_server(showcase = TRUE)