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


# app <- Dash$new()


examples <- list(
  defaultClustergram=utils$LoadExampleCode('clustergram/examples/defaultClustergram.R')
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
  dccMarkdown('# Clustergram Examples and Reference'),
  
  
  dccMarkdown('
  See Clustergram in action [here](https://dash-bio.plotly.host/dash-clustergram/)
  ')
))


# Individual Components and Examples


defaultClustergram <- htmlDiv(list(
  dccMarkdown('## Default Clustergram'),
  htmlP('An example of a default clustergram component without any extra properties.'),
  htmlDiv(list(
    examples$defaultClustergram$source_code,
    examples$defaultClustergram$layout))
))


heatmapColorScale <- htmlDiv(list(
  dccMarkdown('## Heatmap Color Scale'),
  htmlP('Change the color scale by specifying values and colors.'),
  utils$LoadAndDisplayComponent(
    '
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(heatmaply)
library(data.table)
    
df = read.table("assets/sample_data/clustergram_mtcars.tsv",
                        skip = 4, sep ="\t",  row.names = 1, header = TRUE)
                        
                        
dccGraph(figure = heatmaply(df, 
                            row_labels = list(row.names(data)),
                            hide_labels = list("row"),
                            column_labels = as.list(colnames(data)),
                            color_threshold = list(
                            "row" = 150,
                            "col" = 700
                            ),
                            colors = BrBG,
                            limits = c(0, 500),
                            midpoint = 200
          )
        )
    '
  )
))


dendrogramColorWidth <- htmlDiv(list(
  dccMarkdown('## Dendrogram Cluster Colors/Line Widths'),
  htmlP('Change the colors of the dendrogram traces that are used to represent clusters, and configure their line widths.'),
  utils$LoadAndDisplayComponent(
    '
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(heatmaply)
library(data.table)
    
df = read.table("assets/sample_data/clustergram_mtcars.tsv",
                        skip = 4, sep ="\t",  row.names = 1, header = TRUE)
                        

# The following is a color palette.

rc <- colorspace::rainbow_hcl(nrow(df))
                        
dccGraph(figure = heatmaply(df, 
                            row_labels = list(row.names(data)),
                            hide_labels = list("row"),
                            column_labels = as.list(colnames(data)),
                            color_threshold = list(
                            "row" = 250,
                            "col" = 700
                            ),
                            seriate = "mean",
                            RowSideColors = rc,
                            k_col = 2,
                            k_row = 2
          )
        )
    '
  )
))



dendrogramRelativeSize <- htmlDiv(list(
  dccMarkdown('## Relative Dendrogram Size'),
  htmlP('Change the relative width and height of, respectively, the row and column dendrograms compared to the width and height of the heatmap.'),
  utils$LoadAndDisplayComponent(
    '
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(heatmaply)
library(data.table)
    
df = read.table("assets/sample_data/clustergram_mtcars.tsv",
                        skip = 4, sep ="\t",  row.names = 1, header = TRUE)
                        
                        
dccGraph(figure = heatmaply(df, 
                            row_labels = list(row.names(data)),
                            hide_labels = list("row"),
                            column_labels = as.list(colnames(data)),
                            color_threshold = list(
                            "row" = 250,
                            "col" = 700
                            ),
                            height = 800,
                            width = 700,
                            display_ratio=list(0.1, 0.7)

          )
        )
    '
  )
))


hiddenLabels <- htmlDiv(list(
  dccMarkdown('## Hidden Labels'),
  htmlP('Hide the labels along one or both dimensions.'),
  utils$LoadAndDisplayComponent(
    '
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(heatmaply)
library(data.table)
    
df = read.table("assets/sample_data/clustergram_mtcars.tsv",
                        skip = 4, sep ="\t",  row.names = 1, header = TRUE)
                        
                        
dccGraph(figure = heatmaply(df, 
                            row_labels = list(row.names(data)),
                            hide_labels = list("row"),
                            column_labels = as.list(colnames(data)),
                            color_threshold = list(
                            "row" = 250,
                            "col" = 700
                            ),
                            showticklabels = c(T,F)

          )
        )
    '
  )
))



heatmapAnnotations <- htmlDiv(list(
  dccMarkdown('## Annotations'),
  htmlP('Annotate the clustergram by highlighting specific clusters.'),
  utils$LoadAndDisplayComponent(
    '
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(heatmaply)
library(data.table)
    
df = read.table("assets/sample_data/clustergram_mtcars.tsv",
                        skip = 4, sep ="\t",  row.names = 1, header = TRUE)
                        
                        
dccGraph(figure = heatmaply(df[, -c(8,9)], 
                            row_labels = list(row.names(data)),
                            hide_labels = list("row"),
                            column_labels = as.list(colnames(data)),
                            color_threshold = list(
                            "row" = 250,
                            "col" = 700
                            ),
                            seriate = "mean",
                            col_side_colors = c(rep(0,5), rep(1,4)),
                            row_side_colors = df[,8:9],
                            

          )
        )
    '
  )
))

heatmaply_props <- propsToList("heatmaply")

heatmaplyPropsDF <- rbindlist(heatmaply_props, fill = TRUE)


heatmaply_props_table <- generate_props_table(heatmaplyPropsDF)
  


# Main docs layout

layout <- htmlDiv(list(
      dashbio_intro,
      htmlHr(),
      defaultClustergram,
      htmlHr(),
      heatmapColorScale,
      htmlHr(),
      dendrogramColorWidth,
      htmlHr(),
      dendrogramRelativeSize,
      htmlHr(),
      hiddenLabels,
      htmlHr(),
      heatmapAnnotations,
      htmlHr(),
      dccMarkdown('## Clustergram Properties'),
      heatmaply_props_table,
      htmlA("Back to the Table of Contents", href = "/")
))


# app$run_server(showcase = TRUE)

