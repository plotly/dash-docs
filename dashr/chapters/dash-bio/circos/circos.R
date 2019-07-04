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


# app <- Dash$new()


examples <- list(
  defaultCircos=utils$LoadExampleCode('circos/examples/defaultCircos.R')
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
  dccMarkdown('# Circos Examples and Reference'),
  
  
  dccMarkdown('
  See Circos in action [here](https://dash-bio.plotly.host/dash-circos/)
  ')
))


# Individual Components and Examples


defaultCircos <- htmlDiv(list(
  dccMarkdown('## Default Circos Chart'),
  htmlP('An example of a default alignment chart component without any extra properties.'),
  htmlDiv(list(
    examples$defaultCircos$source_code,
    examples$defaultCircos$layout))
))



inner_outer_radii <- htmlDiv(list(
  dccMarkdown('## Inner and Outer Radii'),
  htmlP('Change the inner and outer radii of your Circos graph.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)
library(readr)
library(jsonlite)
    
data <- "assets/sample_data/circos_graph_data.json"

circos_graph_data = read_json(data)
     
dashbioCircos(
  id = "circos_radii_example",
  layout = circos_graph_data[["GRCh37"]],
  tracks = list(list(
    "type" = "CHORDS",
    "data" = circos_graph_data[["chords"]]
  )),

  config = list(
    "innerRadius" = 40,
    "outerRadius" = 200
  )

)
    '
  )
))




library(dashTable)


circos_props <- propsToList("dashbioCircos")

circosPropsDF <- rbindlist(circos_props, fill = TRUE)


circos_props_table <- generate_props_table(circosPropsDF)



# Main docs layout

layout <- htmlDiv(list(
      dashbio_intro,
      htmlHr(),
      defaultCircos,
      inner_outer_radii,
      dccMarkdown('## Circos Properties'),
      circos_props_table,
      htmlA("Back to the Table of Contents", href = "/")
))



# app$run_server(showcase = TRUE)

