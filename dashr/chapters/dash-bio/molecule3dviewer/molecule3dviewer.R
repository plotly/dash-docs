library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBio)
library(dashTable)

utils <- new.env()
source('assets/styles.R')
source('assets/utils.R')
source('assets/utils.R', local=utils)


examples <- list(
  default = utils$LoadExampleCode('molecule3dviewer/examples/default.R'),
  selectionType = utils$LoadExampleCode('molecule3dviewer/examples/selectionType.R'),
  # selectionTypePseudo = utils$LoadExampleCode('molecule3dviewer/examples/selectionTypePseudo.R'),
  table = utils$LoadExampleCode('molecule3dviewer/examples/table.R')
)

layout <- htmlDiv(
  list(
    dccMarkdown("
# Molecule3dViewer Examples and Reference

See Molecule 3D Viewer in action 
[here](https://dash-bio.plotly.host/dash-molecule3d/).

## Default Molecule 3D Viewer

An example of a default molecule 3d viewer component without any extra properties.
                "),
    
    examples$default$source,
    examples$default$layout,
    
    htmlHr(),
    
    dccMarkdown("
## Selection Type

Choose what gets highlighted with the same color upon selection.
                "),
    
    examples$selectionTypePseudo$source,
    examples$selectionType$layout,
    
    htmlHr(),
    
    dccMarkdown("
## Background Color/Opacity

Change the background color and opacity of the canvas on which Mol3D is rendered.
```r
dashbioMolecule3dViewer(
    id = 'my-dashbio-molecule3d',
                styles = styles_data,
                modelData = model_data,
                selectionType = 'Chain',
                backgroundColor='#FF0000',
                backgroundOpacity=0.2
    )
```
                "),
    
    htmlHr(),
    
    dccMarkdown("
## Molecule3dViewer Properties
                "),
    
    examples$table$layout,
    
    htmlHr(),
    dccMarkdown("
[Back to the Dash Documentation](/)
              ")
    
  )
)
