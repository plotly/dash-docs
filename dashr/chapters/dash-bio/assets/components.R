source('assets/styles.R')

Syntax = function(children, language='R', style=styles$code_container, summary=''){
  if (!(summary == '')){
    return(htmlDetails(list(
      htmlSummary(summary),
      htmlDiv(children)
    )
    , 
    open=TRUE))}
  else{
    return(dccSyntaxHighlighter(
      children,
      'language'=language,
      'customStyle'=style
    ))
  }}

Example = function(example){
  return(htmlDiv(example, className='example-container'))}
