#this was made to have the callbacks to certain examples fire in the global 
#environment. Due to R's scoping rules, callbacks were not ran in the parent
#env and thus not fired.

#UPLOAD COMPONENT CALLBACKS---------------------------------

app$callback(
  output = list(id='output-data-upload', property = 'children'),
  params = list(input(id = 'upload-data', property = 'contents'),
                state(id = 'upload-data', property = 'filename'),
                state(id = 'upload-data', property = 'last_modified')),
  function(list_of_contents, list_of_names, list_of_dates){
    if(is.null(list_of_contents) == FALSE){
      children = lapply(1:length(list_of_contents), function(x){
        parse_content(list_of_contents[[x]], list_of_names[[x]], list_of_dates[[x]])
      })
      
    }
    return(children)
  })


parse_content = function(contents, filename, date){
  return(htmlDiv(list(
    htmlH5(filename),
    htmlH6(anytime(date)),
    htmlImg(src=contents),
    htmlHr(),
    htmlDiv('Raw Content'),
    htmlPre(paste(substr(toJSON(contents), 1, 100), "..."), style=list(
      'whiteSpace'= 'pre-wrap',
      'wordBreak'= 'break-all'
    ))
  )))
}

app$callback(
  output = list(id='output-image-upload', property = 'children'),
  params = list(input(id = 'upload-image', property = 'contents'),
                state(id = 'upload-image', property = 'filename'),
                state(id = 'upload-image', property = 'last_modified')),
  function(list_of_contents, list_of_names, list_of_dates){
    if(is.null(list_of_contents) == FALSE){
      children = lapply(1:length(list_of_contents), function(x){
        parse_content(list_of_contents[[x]], list_of_names[[x]], list_of_dates[[x]])
      })
    } else{
      
    }
    return(children)
  }
)

#CONFIRM DIALOGUE ---------------------------------

app$callback(
  output = list(id = 'confirm', property = 'displayed'),
  params=list(input(id = 'dropdown', property = 'value')),
  function(value){
    if(value == 'Danger!!'){
      return(TRUE)}
    else{
      return(FALSE)}
  })


app$callback(
  output = list(id = 'output-confirm1', property = 'children'),
  params=list(input(id = 'confirm', property = 'submit_n_clicks')),
  function(n_clicks, value) {
    if(length(submit_n_clicks) == FALSE){
      sprintf('It wasnt easy but we did it %s', str(submit_n_clicks))
    }
  })

#STORE ---------------------------------

for (store in c('memory', 'local', 'session')) {
  
  app$callback(
    output = list(id=store, property = 'data'),
    params = list(input(id = sprintf('%s-button', store), property = 'n_clicks'),
                  state(store, 'data')),
    function(n_clicks, data){
      #browser()
      if(is.null(n_clicks)){
        return()
      }
      
      if(is.null(data[[1]])){
        data = list('clicks' = 0)
      } else{
        data = data
      }  
      data['clicks'] = data$clicks + 1
      return(data)
    }
  )
  
  app$callback(
    output = list(id=sprintf('%s-clicks', store), property = 'children'),
    params = list(input(id = store, property = 'modified_timestamp'),
                  state(store, 'data')),
    function(ts, data){
      #browser()
      if(is.null(ts)){
        return()
      }
      if(is.null(data[[1]])){
        data = list()
      } else{
        data = data
      }  
      return(data$clicks[[1]])
    })
  
}

app$callback(
  output = list(id="memory-output", property = 'data'),
  params = list(input(id = "memory-countries", property = 'value')),
  function(countries_selected){
    if(length(countries_selected) < 1){
      return(df_to_list(df))
    }
    filtered = df[which(df$country %in% countries_selected), ]
    return(df_to_list(filtered))
  })

app$callback(
  output = list(id="memory-table", property = 'data'),
  params = list(input(id = "memory-output", property = 'data')),
  function(data){
    if(is.null(data) == TRUE){
      return()
    }
    return(data)
  })

app$callback(
  output = list(id="memory-graph", property = 'figure'),
  params = list(input(id = "memory-output", property = 'data'),
                input(id = "memory-field", property = 'value')),
  function(data, field){
    data = data.frame(matrix(unlist(data), nrow=length(data), byrow=T))
    colnames(data)[1:ncol(data)] = c('country', 'year','pop','continent','lifeExp', 'gdpPercap')
    if(is.null(data) == TRUE){
      return()
    }
    aggregation = list()
    data <- split(data, f = data$country)
    for (row in 1:length(data)) {
      aggregation[[row]] <- list(
        x = unlist(data[[row]][[field]]),
        y = unlist(data[[row]]['year']),
        text = data[[row]]['country'],
        mode = 'lines+markers',
        name = as.character(unique(data[[row]]['country'])$country)
      )
    }
    
    return(list(
      'data' = aggregation))
  })

#LOADING COMPONENT ---------------------------------

app$callback(
  output = list(id='loading-output-1', property = 'children'),
  params = list(input(id = 'input-1', property = 'value')),
  function(value){
    Sys.sleep(1)
    return(value)
  }
)


app$callback(
  output = list(id='loading-output-2', property = 'children'),
  params = list(input(id = 'input-2', property = 'value')),
  function(value){
    Sys.sleep(1)
    return(value)
  }
)
#TABS ---------------------------------

app$callback(
  output = list(id='tabs-content-example', property = 'children'),
  params = list(input(id = 'tabs-example', property = 'value')),
  function(tab){
    if(tab == 'tab-1-example'){
      return(htmlDiv(list(
        htmlH3('Tab content 1'),
        dccGraph(
          id='graph-1-tabs',
          figure=list(
            'data' = list(list(
              'x' = c(1, 2, 3),
              'y' = c(3, 1, 2),
              'type' = 'bar'
            ))
          )
        )
      )))
    }
    
    else if(tab == 'tab-2-example'){
      return(htmlDiv(list(
        htmlH3('Tab content 2'),
        dccGraph(
          id='graph-2-tabs',
          figure=list(
            'data' = list(list(
              'x' = c(1, 2, 3),
              'y' = c(5, 10, 6),
              'type' = 'bar'
            ))
          )
        )
      )))
    }
  }
  
  
  
)

app$callback(
  output = list(id='tabs-content-classes', property = 'children'),
  params = list(input(id = 'tabs-with-classes', property = 'value')),
  function(tab){
    if(tab == 'tab-1'){
      return(htmlDiv(
        list(htmlH3('Tab content 1'))
      ))
    } else if(tab == 'tab-2'){
      return(htmlDiv(
        list(htmlH3('Tab content 2'))
      ))
    } else if(tab == 'tab-3'){
      return(htmlDiv(
        list(htmlH3('Tab content 3'))
      ))
    } else if(tab == 'tab-4'){
      return(htmlDiv(
        list(htmlH3('Tab content 4'))
      ))
    }
  }
)

app$callback(
  output = list(id='tabs-content-inline', property = 'children'),
  params = list(input(id = 'tabs-styled-with-inline', property = 'value')),
  function(tab){
    if(tab == 'tab-1'){
      return(htmlDiv(
        list(htmlH3('Tab content 1'))
      ))
    } else if(tab == 'tab-2'){
      return(htmlDiv(
        list(htmlH3('Tab content 2'))
      ))
    } else if(tab == 'tab-3'){
      return(htmlDiv(
        list(htmlH3('Tab content 3'))
      ))
    } else if(tab == 'tab-4'){
      return(htmlDiv(
        list(htmlH3('Tab content 4'))
      ))
    }
  }
)

app$callback(
  output = list(id='tabs-content-props', property = 'children'),
  params = list(input(id = 'tabs-styled-with-props', property = 'value')),
  function(tab){
    if(tab == 'tab-1'){
      return(htmlDiv(
        list(htmlH3('Tab content 1'))
      ))
    } else if(tab == 'tab-2'){
      return(htmlDiv(
        list(htmlH3('Tab content 2'))
      ))
    }
  })

app$callback(output('tabs-content', 'children'),
             params = list(input('tabs', 'value')),
             function(tab){
               if(tab == 'tab-1'){
                 return(htmlDiv(list(
                   htmlH3('Tab content 1')
                 )))}
               else if(tab == 'tab-2'){
                 return(htmlDiv(list(
                   htmlH3('Tab content 2')
                 )))}
             }
)




