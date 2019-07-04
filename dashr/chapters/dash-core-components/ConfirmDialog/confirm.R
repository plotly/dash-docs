app = Dash$new()


app$layout(htmlDiv(list(
  dccConfirmDialog(
    id='confirm',
    message='Danger danger! Are you sure you want to continue?',
  ),
  
  dccDropdown(
    options=lapply(list('Safe', 'Danger!!'), 
                   function(x){list('label'= x, 'value'= x)}),
    id='dropdown'
  ),
  htmlDiv(id='output-confirm')
  )))

app$callback(output = list(id = 'confirm', property = 'displayed'),
             params = list(
               input(id = 'dropdown', property = 'value')),
             function(value){
               if(value == 'Danger!!'){
                 return(TRUE)
               }else{
                 return(FALSE)
               }
             }
             
      )


app$callback(output = list(id = 'output-confirm', property = 'displayed'),
             params = list(
               input(id = 'confirm', property = 'submit_n_clicks')),
             function(submit_n_clicks){
               if(length(submit_n_clicks) == FALSE){
                 sprintf('It wasnt easy but we did it %s', str(submit_n_clicks))
               }
             }
             
)

app$run_server()
