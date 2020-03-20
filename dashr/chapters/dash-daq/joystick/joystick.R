library(dash)
library(dashDaq)
library(data.table)
library(dashTable)

utils <- new.env()
source('dashr/styles.R')
source('dashr/utils.R', local=utils)

examples <- list(
  defaultJoystick = utils$LoadExampleCode(
    "dashr/chapters/dash-daq/joystick/examples/defaultJoystick.R")
)

dashdaq_intro <- htmlDiv(list(
  dccMarkdown('# Joystick Examples and Reference')
  )
)

# Individual Components and Examples

defaultJoystick <- htmlDiv(list(
  htmlH3("Default Joystick"),
  htmlP("An example of a default Joystick without any extra properties."),
  htmlDiv(
    list(
      examples$defaultJoystick$source_code,
      examples$defaultJoystick$layout
    ),
    className = 'code-container'
  )
))

joystickLabel <-  htmlDiv(list(
  htmlH3("Label"),
  dccMarkdown(
    "Change the label and label orientation with `label` and `labelPosition`."
  ),
  utils$LoadAndDisplayComponent(
    '
library(dashDaq)

daqJoystick(
    label = "Label",
    labelPosition = "bottom",
)
  '
  )))

joystickSize <-  htmlDiv(list(
  htmlH3("Size"),
  dccMarkdown("Change the size of the joystick with `size`."),
  utils$LoadAndDisplayComponent('
library(dashDaq)

daqJoystick(
    size = 250)
  '
  )))

joystickProps <- props_to_list("daqJoystick")

joystickPropsDF <- rbindlist(joystickProps, fill = TRUE)

joystickTable <- generate_table(joystickPropsDF)

layout <- htmlDiv(list(
  dashdaq_intro,
  htmlHr(),
  defaultJoystick,
  htmlHr(),
  joystickLabel,
  htmlHr(),
  joystickSize,
  htmlHr(),
  htmlHr(),
  htmlH3("Joystick Properties"),
  joystickTable,
  htmlHr(),
  dccMarkdown("[Back to Dash DAQ Documentation](/dash-daq)"),
  dccMarkdown("[Back to the Table of Contents](/)")
))
