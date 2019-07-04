#Source assets
source("assets/utils.R")
source("DashBioDocsMain.R")
source("app.R")

# Load Necessary Packages
library('dash')
library('dashCoreComponents')
library('dashHtmlComponents')
library('dashBio')
library('dashTable')
library('readr')
library('heatmaply')
library('data.table')
library('jsonlite')
library('rjson')

chapters.alignment <- new.env()
source('alignment-chart/alignment-chart.R', local=chapters.alignment)
chapters.circos <- new.env()
source('circos/circos.R', local=chapters.circos)
chapters.clustergram <- new.env()
source('clustergram/clustergram.R', local=chapters.clustergram)
chapters.ideogram <- new.env()
source('ideogram/ideogram.R', local=chapters.ideogram)
chapters.volcanoplot <- new.env()
source('volcanoplot/volcano.R', local=chapters.volcanoplot)
chapters.manhattan <- new.env()
source('manhattan/manhattan.R', local = chapters.manhattan)
chapters.molecule3dviewer <- new.env()
source('molecule3dviewer/molecule3dviewer.R', local=chapters.molecule3dviewer)
chapters.molecule2dviewer <- new.env()
source('molecule2dviewer/molecule2dviewer.R', local=chapters.molecule2dviewer)
chapters.needleplot <- new.env()
source('needleplot/needleplot.R', local=chapters.needleplot)
chapters.oncoprint <- new.env()
source('oncoprint/oncoprint.R', local=chapters.oncoprint)
chapters.sequenceviewer <- new.env()
source('sequenceviewer/sequenceviewer.R', local=chapters.sequenceviewer)
chapters.speck <- new.env()
source("speck/speck.R", local=chapters.speck)

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

layout <-
  htmlDiv(
    list(
      header,      
      dccLocation(id='url'),
      htmlDiv(
        className='background',
        children=list(
          htmlDiv(id='wait-for-layout'),
          htmlDiv(
            className='container-width',
            children=htmlDiv(
              htmlDiv(id='chapter', className='content'),
              className='content-container'
            )
          )
        )
      )
    )
  )
)

app$callback(output=list(id='chapter', property='children'),
             params=list(input('url', 'pathname')),
             function(pathname) {
               switch(
                 pathname,
                 "/AlignmentChart" = return(chapters.alignment$layout),
                 "/Circos" = return(chapters.circos$layout),
                 "/Clustergram" = return(chapters.clustergram$layout),
                 "/Ideogram" = return(chapters.ideogram$layout),
                 "/ManhattanPlot" = return(chapters.manhattan$layout),
                 "/Molecule2dViewer" = return(chapters.molecule2dviewer$layout),
                 "/Molecule3dViewer" = return(chapters.molecule3dviewer$layout),
                 "/VolcanoPlot" = return(chapters.volcanoplot$layout),
                 "/NeedlePlot" = return(chapters.needleplot$layout),
                 "/OncoPrint" = return(chapters.oncoprint$layout),
                 "/SequenceViewer" = return(chapters.sequenceviewer$layout),
                 "/Speck" = return(chapters.speck$layout),
                 {mainLayout
                 }
               )
             })

app$callback(
  output(id = 'alignment-container', property = 'children'),
  params = list(
    input(id = 'alignment-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
library(readr)

data = read_file("assets/sample_data/alignment_viewer_p53.fasta")

dashbioAlignmentChart(
id = "my-dashbio-alignmentchart",
data = data
)
    '
        )
      )
      )
    }
    
    
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/alignment.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
    
    
  }
)

app$callback(
  output(id = 'circos-container', property = 'children'),
  params = list(
    input(id = 'circos-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
library(readr)
library(jsonlite)
    
data <- "assets/sample_data/circos_graph_data.json"

circos_graph_data = read_json(data)
     
dashbioCircos(
id = "my-dashbio-circos",
layout = circos_graph_data[["GRCh37"]],
tracks = list(list(
  "type" = "CHORDS",
  "data" = circos_graph_data[["chords"]],
  "opacity" = 0.7,
  "color" = list("name" = "color"),
  "config" = list(
      "tooltipContent" = list(
        "source" = "source",
        "sourceID" = "id",
        "target" = "target",
        "targetID" = "id",
        "targetEnd" = "end"
      )
    )
))

)
    '
        )
      )
      )
    }
    
    
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/circos.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
    
    
  }
)

app$callback(
  output(id = 'clustergram-container', property = 'children'),
  params = list(
    input(id = 'clustergram-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
library(dashCoreComponents)
    
df = read.table("assets/sample_data/clustergram_mtcars.tsv",
                  skip = 4, sep ="\t",  row.names = 1, header = TRUE)
                  
dccGraph(figure = heatmaply(df, 
        row_labels = list(row.names(data)),
        hide_labels = list("row"),
        column_labels = as.list(colnames(data)),
        color_threshold = list(
            "row" = 150,
            "col" = 700
          )
       )
    )
    '
        )
      )
      )
    }
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/clustergram.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
  }
)

app$callback(
  output(id = 'ideogram-container', property = 'children'),
  params = list(
    input(id = 'ideogram-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
    
dashbioIdeogram(
id = "my-dashbio-ideogram",
chrHeight = 300
)
    '
        )
      )
      )
    }
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/ideogram.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
  }
)

app$callback(
  output(id = 'manhattan-container', property = 'children'),
  params = list(
    input(id = 'manhattan-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
    
data = read.table("assets/sample_data/manhattan_data.csv",
                     header = TRUE, sep = ",")

dccGraph(figure = dashbioManhattan(
    dataframe=data
))
    '
        )
      )
      )
    }
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/manhattan.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
  }
)

app$callback(
  output(id = 'molecule2d-container', property = 'children'),
  params = list(
    input(id = 'molecule2d-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
library(jsonlite)

model_data = read_json("https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol2d_buckminsterfullerene.json")

dashbioMolecule2dViewer(
id = "my-dashbio-molecule2dviewer",
modelData = model_data
)
    '
        )
      )
      )
    }
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/molecule2d.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
  }
)

app$callback(
  output(id = 'molecule3d-container', property = 'children'),
  params = list(
    input(id = 'molecule3d-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
library(jsonlite)

model_data <- read_json("https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/model_data.js")
styles_data <- read_json("https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/styles_data.js")

dashbioMolecule3dViewer(
    id = "my-dashbio-molecule3dviewer",
    styles = styles_data,
    modelData = model_data,
    selectionType = "Chain"
  )
    '
        )
      )
      )
    }
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/molecule3d.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
  }
)

app$callback(
  output(id = 'needle-container', property = 'children'),
  params = list(
    input(id = 'needle-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
library(jsonlite)
    
mdata = read_json("assets/sample_data/needle_PIK3CA.json")

dashbioNeedlePlot(
id = "my-dashbio-needleplot",
mutationData = mdata
)
    '
        )
      )
      )
    }
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/needle.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
  }
)

app$callback(
  output(id = 'oncoprint-container', property = 'children'),
  params = list(
    input(id = 'oncoprint-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
library(jsonlite)
    
data = read_json("assets/sample_data/oncoprint_dataset3.json")

dashbioOncoPrint(
id = "my-dashbio-oncoprint",
data = data
)
    '
        )
      )
      )
    }
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/oncoprint.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
  }
)

app$callback(
  output(id = 'sequence-container', property = 'children'),
  params = list(
    input(id = 'sequence-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
    
sequence ="MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFY
TPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"


dashbioSequenceViewer(
id = "my-dashbio-sequenceviewer",
sequence = sequence
)
    '
        )
      )
      )
    }
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/sequence.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
  }
)

app$callback(
  output(id = 'speck-container', property = 'children'),
  params = list(
    input(id = 'speck-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
library(dash)
    
importSpeck <- function(filepath,
                        
                        header = FALSE,
                        
                        skip = 2) {
  
  textdata <- read.table(
    
    text = paste0(
      
      readLines(filepath), collapse="\n"
      
    ),
    
    header = header,
    
    skip = skip,
    
    col.names = c("symbol", "x", "y", "z"),
    
    stringsAsFactors = FALSE)
  
  return(dashTable::df_to_list(textdata))
  
}


data <- importSpeck("assets/sample_data/speck_methane.xyz")

dashbioSpeck(
  id = "my-speck",
  view = list("resolution" = 600),
  data = data
)
    '
        )
      )
      )
    }
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/speck.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
  }
)

app$callback(
  output(id = 'volcano-container', property = 'children'),
  params = list(
    input(id = 'volcano-switch', property = 'value')
  ),
  
  change_img <- function(value) {
    if (value == TRUE) {
      return(list(
        utils$LoadAndDisplayComponent(
          '
library(dashBio)
library(dashCoreComponents)
    
data = read.table("assets/sample_data/volcano_data1.csv",
                     header = TRUE, sep = ",")

dccGraph(figure = dashbioVolcano(
    id = "my-dashbio-volcanoplot",
    dataframe = data
  )
)
    '
        )
      )
      )
    }
    else if(value == FALSE) {
      return(list(htmlImg(src = "assets/images/volcano.PNG", style = list("height" = "100%", "width" = "100%"))))
    }
  }
)

#Run App

if (appName != "") {
  app$run_server(host = "0.0.0.0", port = Sys.getenv('PORT', 8050))

} else {
  app$run_server()
}
