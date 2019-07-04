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
  defaultSpeck=utils$LoadExampleCode('speck/examples/defaultSpeck.R')
)


dashbio_intro <- htmlDiv(list(
  dccMarkdown('# Speck Examples and Reference'),
  
  
  dccMarkdown('
  See Speck in action [here](https://dash-bio.plotly.host/dash-speck/)
  ')
))


# Individual Components and Examples


defaultSpeck <- htmlDiv(list(
  dccMarkdown('## Default Speck'),
  htmlP('An example of a default speck component without any extra properties.'),
  htmlDiv(list(
    examples$defaultSpeck$source_code,
    examples$defaultSpeck$layout))
))


speckRender <- htmlDiv(list(
  dccMarkdown('## Molecule Rendering Styles'),
  htmlP('Change the level of atom outlines, ambient occlusion, and more with the "view" parameter.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

data <- importSpeck("assets/sample_data/speck_methane.xyz")

dashbioSpeck(
  data = data,
  view = list(
    "resolution" = 400,
    "ao" = 0.1,
    "outline" = 1,
    "atomScale" = 0.25,
    "relativeAtomScale" = 0.33,
    "bonds" = TRUE
  )
)
    '
  )
))



scrollZoom <- htmlDiv(list(
  dccMarkdown('## Scroll to Zoom'),
  htmlP('Allow for the scroll wheel to control zoom for the molecule.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

data <- importSpeck("assets/sample_data/speck_methane.xyz")

dashbioSpeck(
  data = data,
  scrollZoom  = TRUE
)
    '
  )
))



library(dashTable)


speckProps <- propsToList("dashbioSpeck")

speckPropsDF <- rbindlist(speckProps, fill = TRUE)

speckPropsTable <- generate_props_table(speckPropsDF)



# Main docs layout

layout <- htmlDiv(list(
  
  dashbio_intro,
  htmlHr(),
  defaultSpeck,
  htmlHr(),
  speckRender,
  htmlHr(),
  scrollZoom,
  htmlHr(),
  dccMarkdown('## Speck Properties'),
  speckPropsTable,
  htmlA("Back to the Table of Contents", href = "/")
))
# 
# app$layout(htmlDiv(list(
#   layout
# )))
# app$run_server(showcase = TRUE)
