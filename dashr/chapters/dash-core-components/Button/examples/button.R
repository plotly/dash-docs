library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout(
  htmlDiv(
    list(
      htmlDiv(dccInput(id="input-box", type="text")),
      htmlButton("Submit", id="button"),
      htmlDiv(id="output-container-button",
              children="Enter a value and press submit")
    )
  )
)

app$callback(
  output = list(id = "output-container-button", property = 'children'),
  params=list(input(id = "button", property = "n_clicks"),
              input(id = "input-box", property = "value")),
  function(n_clicks, value) {
    sprintf("The input value was \'%s\' and the button has been clicked \'%s\' times", value, n_clicks)
  })

app$run_server()
