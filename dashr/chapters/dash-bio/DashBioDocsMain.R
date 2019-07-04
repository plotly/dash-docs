library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(dashDaq)
library(rjson)
library(jsonlite)
library(readr)
library(heatmaply)



utils <- new.env()
source('styles.R')
source('utils.R', local=utils)


# Necessary Functions:

titleLink <- function(componentName) {
  return(htmlH2(
    dccLink(
      componentName,
      href=paste('/', componentName, sep='')
    )
  ))
}

referenceLink <- function(componentName) {
  return(dccLink(
    'More examples & reference',
    href=paste('/', componentName, sep='')
  ))
}



# app <- Dash$new()


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
  dccMarkdown('# Dash Bio'),
  
  
  dccMarkdown('
  Dash is a web application framework that provides pure R and Python abstraction
  around HTML, CSS, and JavaScript.
  
  Dash Bio is a suite of bioinformatics components that make it simpler to
  analyze and visualize bioinformatics data and interact with them in a Dash
  application.
  
  The source can be found on GitHub at [plotly/dash-bio](https://github.com/plotly/dash-bio).
  These docs are using Dash Bio version 1.0.0.
  
  To install, run the following commands below in your R console:
  '),
  
  dccMarkdown('
```r
>remotes::install_github("plotly/dash-bio")
>library(dashBio)
```              
              ')
))


# Individual Components and Examples

alignmentChart <- htmlDiv(list(
  htmlDiv(titleLink('AlignmentChart')),
  htmlP('An alignment chart that intuitively graphs complex, genome-scale, sequence alignments.'),
  
  htmlDiv(id = 'alignment-container', children = list()),
  daqToggleSwitch(
    id= 'alignment-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('AlignmentChart'))
))


circos <- htmlDiv(list(
  htmlDiv(titleLink('Circos')),
  htmlP('A circular ideogram with arcs representing links between genes.'),
  htmlDiv(id = 'circos-container', children = list()),
  daqToggleSwitch(
    id= 'circos-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('Circos'))
))




clustergram <- htmlDiv(list(
  htmlDiv(titleLink('Clustergram')),
  htmlP('A heatmap with dendrograms to display clustering of data such as gene expression data.'),
  htmlDiv(id = 'clustergram-container', children = list()),
  daqToggleSwitch(
    id= 'clustergram-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('Clustergram'))
))


ideogram <- htmlDiv(list(
  htmlDiv(titleLink('Ideogram')),
  htmlP('A visual representation and analysis tool for chromosome bands.'),
  htmlDiv(id = 'ideogram-container', children = list()),
  daqToggleSwitch(
    id= 'ideogram-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('Ideogram'))
))


manhattanPlot <- htmlDiv(list(
  htmlDiv(titleLink('ManhattanPlot')),
  htmlP('A plot that can be used to display the results of genomic studies sorted out by chromosome. 
        Perfect for Genome Wide Association Studies (GWAS)'),
  htmlDiv(id = 'manhattan-container', children = list()),
  daqToggleSwitch(
    id= 'manhattan-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('ManhattanPlot'))
))


molecule2dviewer <- htmlDiv(list(
  htmlDiv(titleLink('Molecule2dViewer')),
  htmlP('A 2D rendering of molecular structures.'),
  htmlDiv(id = 'molecule2d-container', children = list()),
  daqToggleSwitch(
    id= 'molecule2d-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('Molecule2dViewer'))
))




molecule3dviewer <- htmlDiv(list(
  htmlDiv(titleLink('Molecule3dViewer')),
  htmlP('A 3D visualization of biomolecular structures.'),
  htmlDiv(id = 'molecule3d-container', children = list()),
  daqToggleSwitch(
    id= 'molecule3d-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('Molecule3dViewer'))
))



needleplot <- htmlDiv(list(
  htmlDiv(titleLink('NeedlePlot')),
  htmlP('A combination of a bar chart and a scatter plot, for data that are both categorical and continuous.'),
  htmlDiv(id = 'needle-container', children = list()),
  daqToggleSwitch(
    id= 'needle-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('NeedlePlot'))
))


oncoprint <- htmlDiv(list(
  htmlDiv(titleLink('OncoPrint')),
  htmlP('A chart that can be used to visualize multiple genomic alternations with an interactive heatmap.'),
  htmlDiv(id = 'oncoprint-container', children = list()),
  daqToggleSwitch(
    id= 'oncoprint-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('OncoPrint'))
))


sequenceviewer <- htmlDiv(list(
  htmlDiv(titleLink('SequenceViewer')),
  htmlP('A sequence viewer that can highlight and display strings of amino acids sequences.'),
  htmlDiv(id = 'sequence-container', children = list()),
  daqToggleSwitch(
    id= 'sequence-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('SequenceViewer'))
))



speck <- htmlDiv(list(
  htmlDiv(titleLink('Speck')),
  htmlP('A 3D WebGL molecule viewer.'),
  htmlDiv(id = 'speck-container', children = list()),
  daqToggleSwitch(
    id= 'speck-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('Speck'))
))



volcanoplot <- htmlDiv(list(
  htmlDiv(titleLink('VolcanoPlot')),
  htmlP("A graph that can be used to identify clinically meaningful markers in genomic experiments."),
  htmlDiv(id = 'volcano-container', children = list()),
  daqToggleSwitch(
    id= 'volcano-switch',
    value = FALSE,
    color = "#AB63FA",
    label = list('Image', 'Live')
  ),
  htmlDiv(referenceLink('VolcanoPlot'))
))



# Main docs layout

mainLayout <- htmlDiv(list(
  dashbio_intro,
  htmlHr(),
  alignmentChart,
  htmlHr(),
  circos,
  htmlHr(),
  clustergram,
  htmlHr(),
  ideogram,
  htmlHr(),
  manhattanPlot,
  htmlHr(),
  molecule2dviewer,
  htmlHr(),
  molecule3dviewer,
  htmlHr(),
  needleplot,
  htmlHr(),
  oncoprint,
  htmlHr(),
  sequenceviewer,
  htmlHr(),
  speck,
  htmlHr(),
  volcanoplot
))



# app$run_server(showcase = TRUE)

