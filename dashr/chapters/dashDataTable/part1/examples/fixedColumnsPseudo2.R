dashDataTable(
  style_cell = list(
    minWidth = '180px', 
    width = '180px', 
    maxWidth = '180px',
    whiteSpace = 'no-wrap',
    overflow = 'hidden',
    textOverflow = 'ellipsis'
  ),
  css = list(
    list(
      selector = '.dash-cell div.dash-cell-value',
      rule = 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
    )
  ),
  fixed_columns= list(headers = TRUE, data = 1),
  columns = lapply(colnames(df_election), 
                   function(colName){
                     list(
                       id = colName,
                       name = colName
                     )
                   }),
  data = df_to_list(df_election)
)