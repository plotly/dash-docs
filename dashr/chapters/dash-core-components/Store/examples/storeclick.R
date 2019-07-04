library(dashCoreComponents)
library(dashHtmlComponents)
library(dash)

app = Dash$new()

app$layout(htmlDiv(list(
  # The memory store reverts to the default on every page refresh
  dccStore(id='memory'),
  # The local store will take the initial data
  # only the first time the page is loaded
  # and keep it until it is cleared.
  dccStore(id='local', storage_type='local'),
  # Same as the local store but will lose the data
  # when the browser/tab closes.
  dccStore(id='session', storage_type='session'),
  htmlTable(list(
    htmlThead(list(
      htmlTr(htmlTh('Click to store in:', colSpan="3")),
      htmlTr(list(
        htmlTh(htmlButton('memory', id='memory-button')),
        htmlTh(htmlButton('localStorage', id='local-button')),
        htmlTh(htmlButton('sessionStorage', id='session-button'))
      )),
      htmlTr(list(
        htmlTh('Memory clicks'),
        htmlTh('Local clicks'),
        htmlTh('Session clicks')
      ))
    )),
    htmlTbody(list(
      htmlTr(list(
        htmlTd(0, id='memory-clicks'),
        htmlTd(0, id='local-clicks'),
        htmlTd(0, id='session-clicks')
      ))
    ))
  ))
)))

for (store in c('memory', 'local', 'session')) {
  
  app$callback(
    output = list(id=store, property = 'data'),
    params = list(input(id = sprintf('%s-button', store), property = 'n_clicks'),
                  state(store, 'data')),
    function(n_clicks, data){
      if(is.null(n_clicks) == TRUE){
        return()
      }
      
      if(is.null(data) == TRUE){
        data = list('clicks' = 0)
      } else{
        data = data
      }  
      data['clicks'] = data['clicks'] + 1
      return(data)
    }
  )
  
  app$callback(
    output = list(id=sprintf('%s-clicks', store), property = 'children'),
    params = list(input(id = store, property = 'modified_timestamp'),
                  state(store, 'data')),
    function(ts, data){
      if(is.null(ts) == TRUE){
        return()
      }
      if(is.null(data) == TRUE){
        data = list()
      } else{
        data = data
      }  
      return(data['clicks' == 0])
    })

}

app$run_server()


