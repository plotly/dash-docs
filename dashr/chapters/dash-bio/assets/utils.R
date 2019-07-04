library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

LoadExampleCode <- function(filename, wd = NULL) {
  # Take a self-contained DashR example filename,
  # eval it, and return that example's `layout`
  # and the source code.
  example.file.as.string <- readChar(filename, file.info(filename)$size);
  
  # modify the example code so that it can run within
  # the context of an already running app
  example.ready.for.eval <- example.file.as.string
  replacements = list(
    # set the layout to a variable so that we can access it
    # and return it
    list('app\\$layout\\(', 'layout <- htmlDiv\\('),
    
    # Since app is in the namespace from the `app.R` import,
    # it will implicity be picked up by the
    # `eval` call below
    list('app <- Dash\\$new\\(\\)', ''),
    list('app\\$run_server\\(\\)', '')
  )
  for(replacement in replacements) {
    example.ready.for.eval <- gsub(
      replacement[1],
      replacement[2],
      example.ready.for.eval
    )
  }
  
  example.ready.for.eval <- paste(unlist(strsplit(example.ready.for.eval, "\r")), collapse = " ")
  
  if(!is.null(wd)) {
    
    currentWd <- getwd()
    newWd <- paste(c(currentWd, wd),collapse =  "/")
    
    example.ready.for.eval <- paste(c("setwd(newWd)", 
                                      example.ready.for.eval, 
                                      "setwd(currentWd)"), 
                                    collapse = "\n")
  }
  
  # run the example and implicitly assign the `layout` variable
  eval(parse(text=example.ready.for.eval))
  
  list(
    layout=htmlDiv(className='example-container', children=layout),
    source_code=htmlDiv(
      children=dccMarkdown(sprintf("```r
%s
                                   ```",example.file.as.string)),
      className='code-container'
    )
  )
}

LoadAndDisplayComponent <- function(example_string) {
  return(
    htmlDiv(
      list(
        htmlDiv(
          children=dccMarkdown(sprintf('```r
                                       %s
                                       ```',example_string)),
          className='code-container'
        ),
        htmlDiv(
          className='example-container',
          children=eval(parse(text=example_string))
        )
      )
    )
  )
}


propsToList <- function(componentName) {
  Rd <- utils:::.getHelpFile(do.call(`?`, 
                                     list(componentName)))
  
  containsArgs <- vapply(Rd, function(x) {
    attr(x, "Rd_tag")=="\\arguments"
  }, 
  logical(1))
  
  # Subset the help data to function arguments only
  args  <- Rd[containsArgs]
  
  # Assemble a list of function arguments, stripping linefeeds  
  list_of_args <- lapply(unlist(args, 
                                recursive=FALSE), 
                         function(x) x[x != "\n"])
  
  # Extract the prop metadata for tabulation  
  props_as_list <- invisible(sapply(list_of_args, function(x) {
    if (any(sapply(x, is.list))) {
      all_types <- paste("List of numerics",
                         "Numeric",
                         "Character",
                         "Logical",
                         "Named list",
                         "Unnamed list",
                         "List of named lists",
                         "List of unnamed lists",
                         "List of character \\| numerics",
                         "Logical \\| numeric \\| character \\| named list \\| unnamed list",
                         "List",
                         sep="|")
      
      attribute <- x[[1]]
      
      descstring <- paste(gsub("\n", "", x[[2]]), collapse=" ")
      
      description <- gsub("Logical\\. |Numeric\\. |Named list\\. |Unnamed list\\. | Character\\.", 
                          "", 
                          descstring)
      type <- regmatches(descstring, regexpr(all_types, descstring))
      default <- NULL
      return(c(attribute=attribute, 
               description=description, 
               type=type,
               default=default))
    }
  }))
  
  # strip NULL values
  props_as_list[lengths(props_as_list) != 0]
}


generate_props_table <- function(df) {
  return(
    dashDataTable(
      
      id = 'table',
      
      columns = lapply(colnames(df), function(x) {
        
        list(name = x, id = x)
        
      }),
      
      data = setNames(lapply(split(df, seq(nrow(df))), FUN = function (x) {as.list(x)}), NULL),

      style_as_list_view = TRUE,
      
      style_data = list('whiteSpace' = 'normal'),
       
      style_cell = list(
        'whiteSpace'= 'no-wrap',
        'overflow'='inherit',
        'textOverflow'= 'inherit',
        'textAlign' = 'left'
      ),


      style_header=(list("fontWeight"="bold", 
                         "text-transform"="capitalize"))

      
    )
  )
}
