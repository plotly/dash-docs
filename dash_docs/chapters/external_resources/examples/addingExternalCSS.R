library(dash)
library(dashHtmlComponents)

# external JavaScript files
external_scripts <- list(
  'https://www.google-analytics.com/analytics.js',
  'https://cdn.polyfill.io/v2/polyfill.min.js',
  list(
    src = 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
    integrity = 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
    crossorigin = 'anonymous'
    )
)

# external CSS stylesheets
external_stylesheets <- list(
  href='https://codepen.io/chriddyp/pen/bWLwgP.css',
  list(
    href = 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
    integrity = 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
    crossorigin = 'anonymous'
    )
)

app <- Dash$new(
  external_scripts = external_scripts,
  external_stylesheets = external_stylesheets
)

app$layout(htmlDiv())

app$run_server()
