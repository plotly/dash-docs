library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

layout = htmlDiv(style=list('padding'= 20),
                  children=list(htmlH1('Dash Doc Search'),
                            dccInput(id='search-input',
                                      placeholder='Search the Dash docs...',
                                      type='text',
                                      value=''),
                            htmlDiv(id='hits',
                                     children=list(htmlDiv(id='hit-template',
                                                        style=list('display'= 'none'),
                                                        children=list(htmlH3(htmlA('{{{_highlightResult.name.value}}}',
                                                                                 href='list(list(permalink))',
                                                                                 style=list('background-color'= '#ffffff',
                                                                                   'padding-left'= '0px')),
                                                                          style=list('margin-bottom'= '1rem')),
                                                                  htmlP('{{{_highlightResult.description.value}}}')
                                                                  ))
                                               
                                               )),
                            htmlBr(),
                            htmlHr(),
                            dccMarkdown("
[Back to the Table of Contents](/)")
                            
                            ))