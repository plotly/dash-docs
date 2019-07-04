
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(rjson)
library(readr)
library(heatmaply)
library(data.table)
library(dashTable)


utils <- new.env()
source('assets/styles.R')
source('assets/utils.R')
source('assets/utils.R', local=utils)



examples <- list(
  defaultIdeogram=utils$LoadExampleCode('ideogram/examples/defaultIdeogram.R')
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
  dccMarkdown('# Ideogram Examples and Reference'),
  
  
  dccMarkdown('
  See Ideogram in action [here](https://dash-bio.plotly.host/dash-ideogram/)
  ')
))


# Individual Components and Examples


defaultIdeogram <- htmlDiv(list(
  dccMarkdown('## Default Ideogram'),
  htmlP('An example of a default ideogram component without any extra properties.'),
  htmlDiv(list(
    examples$defaultIdeogram$source_code,
    examples$defaultIdeogram$layout))
))


heightWidthIdeogram <- htmlDiv(list(
  dccMarkdown('## Height/Width'),
  htmlP('Change the size of the chromosomes in your ideogram.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

dashbioIdeogram(
    id = "ideogram-size",
    chrHeight = 800,
    chrWidth = 200
)
    '
  )
))



annotationsIdeogram <- htmlDiv(list(
  dccMarkdown('## Annotations'),
  htmlP('Display annotations that are loaded from a JSON file.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

dashbioIdeogram(
    id = "ideogram-annotations",
    chromosomes = list("X", "Y"),
    annotationsPath = "assets/SRR562646.json"
)
    '
  )
))


rotationIdeogram <- htmlDiv(list(
  dccMarkdown('## Rotatability'),
  htmlP('Enable or disable rotation of the chromosome upon clicking on it.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

dashbioIdeogram(
    id = "ideogram-rotation",
    rotatable = FALSE
)
    '
  )
))



orientationIdeogram <- htmlDiv(list(
  dccMarkdown('## Orientation'),
  htmlP('Display chromosomes horizontally or vertically.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

dashbioIdeogram(
    id = "ideogram-orientation",
    rotatable = "horizontal"
)
    '
  )
))


brushIdeogram <- htmlDiv(list(
  dccMarkdown('## Brush Highlights'),
  htmlP('Highlight a region of the chromosome by adding a brush.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

dashbioIdeogram(
    id = "ideogram-brush",
    orientation = "horizontal",
    chromosomes = list("X"),
    brush = "chrX:1-10000000"
)
    '
  )
))



library(dashTable)


ideogramprops <- propsToList("dashbioIdeogram")

ideogramPropsDF <- rbindlist(ideogramprops, fill = TRUE)

ideogramPropsTable <- generate_props_table(ideogramPropsDF)



# Main docs layout

layout <- htmlDiv(list(
  
  dashbio_intro,
  htmlHr(),
  defaultIdeogram,
  htmlHr(),
  heightWidthIdeogram,
  htmlHr(),
  annotationsIdeogram,
  htmlHr(),
  rotationIdeogram,
  htmlHr(),
  orientationIdeogram,
  htmlHr(),
  brushIdeogram,
  htmlHr(),
  dccMarkdown('## Ideogram Properties'),
  ideogramPropsTable,
  htmlA("Back to the Table of Contents", href = "/")
))






