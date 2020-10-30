library(dash)
library(dashHtmlComponents)

external_scripts <- list(
  'https://www.google-analytics.com/analytics.js',
  'https://cdn.polyfill.io/v2/polyfill.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js'
)

# external CSS stylesheets
external_stylesheets <- list(
  'https://codepen.io/chriddyp/pen/bWLwgP.css',
  'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css'
)

app <- Dash$new(
  external_scripts = external_scripts,
  external_stylesheets = external_stylesheets
)

app$layout(htmlDiv())

app$run_server()
