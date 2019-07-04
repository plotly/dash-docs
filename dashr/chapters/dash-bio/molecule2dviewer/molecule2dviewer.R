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
  defaultMolecule2dViewer=utils$LoadExampleCode('molecule2dviewer/examples/defaultMolecule2dviewer.R')
)


dashbio_intro <- htmlDiv(list(
  dccMarkdown('# Molecule2dViewer Examples and Reference'),
  
  
  dccMarkdown('
  See Molecule2dViewer in action [here](http://dash-bio.plotly.host/dash-molecule-2d-viewer)
  ')
))


# Individual Components and Examples


defaultMolecule2dViewer <- htmlDiv(list(
  dccMarkdown('## Default Molecule2dViewer'),
  htmlP('An example of a default Molecule2DViewer component without any extra properties.'),
  htmlDiv(list(
    examples$defaultMolecule2dViewer$source_code,
    examples$defaultMolecule2dViewer$layout))
))


selectedAtom <- htmlDiv(list(
  dccMarkdown('## Selected Atom IDs'),
  htmlP('Highlight specific atoms in the molecule.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

model_data <- read_json("assets/sample_data/mol2d_buckminsterfullerene.json")

dashbioMolecule2dViewer(
        modelData = model_data,
        selectedAtomIds = list(seq(1:10))
      )
    '
  )
))



modelData <- htmlDiv(list(
  dccMarkdown('## Model Data'),
  htmlP('Change the bonds and atoms in the molecule.'),
  utils$LoadAndDisplayComponent(
    '
library(dashBio)

model_data <- read_json("assets/sample_data/mol2d_buckminsterfullerene.json")

for (node in model_data$nodes) {
    node$atom <- "N"
}

for (link in model_data$links) {
    link$distance <- 50.0
    link$strength <- 0.5
}

dashbioMolecule2dViewer(
        modelData = model_data,
        selectedAtomIds = list(seq(1:10))
      )
    '
  )
))





library(dashTable)


molecule2dviewerProps <- propsToList("dashbioMolecule2dViewer")

molecule2dviewerPropsDF <- rbindlist(molecule2dviewerProps, fill = TRUE)

molecule2dviewerPropsTable <- generate_props_table(molecule2dviewerPropsDF)



# Main docs layout

layout <- htmlDiv(list(
  
  dashbio_intro,
  htmlHr(),
  defaultMolecule2dViewer,
  htmlHr(),
  selectedAtom,
  htmlHr(),
  modelData,
  htmlHr(),
  dccMarkdown('## Molecule2dViewer Properties'),
  molecule2dviewerPropsTable,
  htmlA("Back to the Table of Contents", href = "/")
))


