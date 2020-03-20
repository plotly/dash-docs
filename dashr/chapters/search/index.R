library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

layout = htmlDiv(style=list('padding'= 20),
                  children=list(htmlH1('DashR Doc Search'),
                            dccInput(id='search-inputR',
                                      placeholder='Search the Dash docs...',
                                      type='text',
                                      value=''),
                            htmlDiv(id='hitsR',
                                     children=list(htmlDiv(id='hit-templateR',
                                                        style=list('display'= 'none'),
                                                        children=list(htmlH3(htmlA('{{{_highlightResult.name.value}}}',
                                                                                 href='{{permalink}}',
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
