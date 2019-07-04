library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout(
  htmlDiv(
    list(
      dccRadioItems(
        id = 'dropdown-a',
        options = list(list(label = 'Canada', value = 'Canada'),
                       list(label = 'USA', value = 'USA'),
                       list(label = 'Mexico', value = 'Mexico')),
        value = 'Canada'
      ),
      htmlDiv(id='output-a'),
      dccRadioItems(
        id = 'dropdown-b',
        options = list(list(label = 'MTL', value = 'MTL'),
                       list(label = 'NYC', value = 'NYC'),
                       list(label = 'SF', value = 'SF')),
        value = 'MTL'
      ),
      htmlDiv(id='output-b')
    )
  )
)

app$callback(
  output=list(id='output-a', property='children'),
  params=list(input(id='dropdown-a', property='value')),
  function(dropdown_value) {
    sprintf("You've entered \"%s\"", dropdown_value)
})

app$callback(
  output=list(id='output-b', property='children'),
  params=list(input(id='dropdown-b', property='value')),
  function(dropdown_value) {
    sprintf("You've entered \"%s\"", dropdown_value)
})

#app$run_server()
