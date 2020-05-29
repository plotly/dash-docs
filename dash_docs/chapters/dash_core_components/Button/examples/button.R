library(dash)
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
    if (is.list(n_clicks)) {
      sprintf("'n_clicks' is a list of length %d", length(n_clicks))
    } else {
      sprintf("'n_clicks' is a vector and you have clicked the button %d time(s)", n_clicks)
    }
  }
)

app$run_server()
