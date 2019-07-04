<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

set.seed(0)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# df <- data.frame(replicate(1,sample(0:6,30,rep=TRUE))) 
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
df <- data.frame(matrix(ncol = 6, nrow = 30))
x <- c(1:6)
x <- paste("Column ", x)
colnames(df) <- x

for (i in 1:6){
  val <- (i-1)*10
  nameCol <- paste("Column ", i)
  for (j in 1:30){
    df[[i]] <- rnorm(1,val,0.1)
  }
}
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  # pd.DataFrame({
  # 'Column {}'.format(i): np.random.rand(30) + i*10
  # for i in range(6)})df
=======

>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======

>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======

>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5

app$layout_set(htmlDiv(list(
  htmlDiv(
    dccGraph(
      id='g1',
      config=list(displayModeBar = FALSE)
    ), className='four columns'
  ),
  htmlDiv(
    dccGraph(
      id='g2',
      config=list(displayModeBar = FALSE)
    ), className='four columns'),
  htmlDiv(
    dccGraph(
      id='g3',
      config=list(displayModeBar = FALSE)
    ), className='four columns')
  ), className='row')
)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
highlight <- function(x, y){
  callback <- function(selectedDatas){
    selectedpoints = colnames(df)
    for(selected_data in enumerate(selectedDatas)){
      if (!is.null(selected_data)){
        for (p in selected_data$points){
          selected_index = list(p$customdata)
        }
        if (length(selected_index) > 0){
          selectedpoints = np.intersect1d(
            selectedpoints, selected_index)
        }
      }
    }

    # set which points are selected with the `selectedpoints` property
    # and style those points with the `selected` and `unselected`
    # attribute. see
    # https://medium.com/@plotlygraphs/notes-from-the-latest-plotly-js-release-b035a5b43e21
    # for an explanation
    
    figure = list(
      data = list(
        list(
          x = df[x],
          y = df[y],
          text = df.index,
          textposition = 'top',
          selectedpoints = selectedpoints,
          customdata = df.index,
          type = 'scatter',
          mode = 'markers+text',
          marker = list(
            color = 'rgba(0, 116, 217, 0.7)',
            size = 12,
            line = list(
              color = 'rgb(0, 116, 217)',
              width = 0.5
            )
          ),
          textfont = list(
            color = 'rgba(30, 30, 30, 1)'
          ),
          unselected = list(
            marker =list(
              opacity = 0.3
            ),
            textfont = list(
              # make text transparent when not selected
              color = 'rgba(0, 0, 0, 0)'
            )
          )
        )
      ),
      layout = list(
        clickmode = 'event+select',
        margin = list('l' = 15, 'r' = 0, 'b' = 15, 't' = 5),
        dragmode = 'select',
        hovermode = 'closest',
        showlegend = FALSE
      )
    )
    
    # Display a rectangle to highlight the previously selected region
    shape = list(
      type = 'rect',
      line = list(
        width = 1,
        dash = 'dot',
        color = 'darkgrey'
      )
    )
    # if selectedDatas[0] and selectedDatas[0]['range']:
    #   figure['layout']['shapes'] = [dict({
    #     'x0' = selectedDatas[0]['range']['x'][0],
    #     'x1' = selectedDatas[0]['range']['x'][1],
    #     'y0' = selectedDatas[0]['range']['y'][0],
    #     'y1' = selectedDatas[0]['range']['y'][1]
    #   }, **shape)]
    # else:
    #   figure['layout']['shapes'] = [dict({
    #     'type' = 'rect',
    #     'x0' = np.min(df[x]),
    #     'x1' = np.max(df[x]),
    #     'y0' = np.min(df[y]),
    #     'y1' = np.max(df[y])
    #   }, **shape)]
    
    return(figure)
  }
  return(callback)
}

highlight('Column 2', 'Column 3')
# app.callback is a decorator which means that it takes a function
# as its argument.
# highlight is a function "generator": it's a function that returns function
app$callback(
  output = list(id='g1', property='figure'),
  params = list(input(id='g1', property='selectedData'),
                input(id='g2', property='selectedData'),
                input(id='g3', property='selectedData'))
)(highlight('Column 0', 'Column 1'))

app$callback(
  output = list(id='g2', property='figure'),
  params = list(input(id='g2', property='selectedData'),
                input(id='g1', property='selectedData'),
                input(id='g3', property='selectedData'))
)(highlight('Column 2', 'Column 3'))

app$callback(
  output = list(id='g3', property='figure'),
  params = list(input(id='g3', property='selectedData'),
                input(id='g1', property='selectedData'),
                input(id='g2', property='selectedData'))
)(highlight('Column 4', 'Column 5'))


# app$run_heroku()
=======
=======
>>>>>>> b59d07d... :construction_worker: example 3 chapt.5
# library(dashR)
# library(dashCoreComponents)
# library(dashHtmlComponents)
#
# app <- Dash$new()
#
# set.seed(0)
# df <- data.frame(matrix(ncol = 6, nrow = 30))
# x <- c(1:6)
# x <- paste("Column ", x)
# colnames(df) <- x
#
# for (i in 1:6){
#   val <- (i-1)*10
#   nameCol <- paste("Column ", i)
#   for (j in 1:30){
#     df[[i]] <- rnorm(1,val,0.1)
#   }
# }
#
#
<<<<<<< HEAD
# app$layout(htmlDiv(list(
=======
# app$layout_set(htmlDiv(list(
>>>>>>> b59d07d... :construction_worker: example 3 chapt.5
#   htmlDiv(
#     dccGraph(
#       id='g1',
#       config=list(displayModeBar = FALSE)
#     ), className='four columns'
#   ),
#   htmlDiv(
#     dccGraph(
#       id='g2',
#       config=list(displayModeBar = FALSE)
#     ), className='four columns'),
#   htmlDiv(
#     dccGraph(
#       id='g3',
#       config=list(displayModeBar = FALSE)
#     ), className='four columns')
#   ), className='row')
# )
#
<<<<<<< HEAD
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> b59d07d... :construction_worker: example 3 chapt.5
# highlight <- function(x, y){
#  callback <- function(selectedDatas){
#     selectedpoints = colnames(df)
#     for(selected_data in enumerate(selectedDatas)){
#       if (!is.null(selected_data)){
#         for (p in selected_data$points){
#           selected_index = list(p$customdata)
#         }
#         if (length(selected_index) > 0){
#           selectedpoints = intersect(
#             selectedpoints, selected_index)
#         }
#       }
#     }
#
#     # set which points are selected with the `selectedpoints` property
#     # and style those points with the `selected` and `unselected`
#     # attribute. see
#     # https://medium.com/@plotlygraphs/notes-from-the-latest-plotly-js-release-b035a5b43e21
#     # for an explanation
#
#     figure = list(
#       data = list(
#         list(
#           x = df$x,
#           y = df$y,
#           text = colnames(df),
#           textposition = 'top',
#           selectedpoints = selectedpoints,
#           customdata = colnames(df),
#           type = 'scatter',
#           mode = 'markers+text',
#           marker = list(
#             color = 'rgba(0, 116, 217, 0.7)',
#             size = 12,
#             line = list(
#               color = 'rgb(0, 116, 217)',
#               width = 0.5
#             )
#           ),
#           textfont = list(
#             color = 'rgba(30, 30, 30, 1)'
#           ),
#           unselected = list(
#             marker =list(
#               opacity = 0.3
#             ),
#             textfont = list(
#               # make text transparent when not selected
#               color = 'rgba(0, 0, 0, 0)'
#             )
#           )
#         )
#       ),
#       layout = list(
#         clickmode = 'event+select',
#         margin = list('l' = 15, 'r' = 0, 'b' = 15, 't' = 5),
#         dragmode = 'select',
#         hovermode = 'closest',
#         showlegend = FALSE
#       )
#     )
#
#     # Display a rectangle to highlight the previously selected region
#     shape = list(
#       type = 'rect',
#       line = list(
#         width = 1,
#         dash = 'dot',
#         color = 'darkgrey'
#       )
#     )
#
#
#     if (selectedDatas[[0]] && selectedDatas[[0]]$range){
#       figure$layout$shapes = list(list(list(
#         'x0' = selectedDatas[[0]]$range$x[[0]],
#         'x1' = selectedDatas[[0]]$range$x[[1]],
#         'y0' = selectedDatas[[0]]$range$y[[0]],
#         'y1' = selectedDatas[[0]]$range$y[[1]]
#       ), shape))
#     }else{
#       figure$layout$shapes = list(list(list(
#         'type' = 'rect',
#         'x0' = min(df$x),
#         'x1' = max(df$x),
#         'y0' = min(df$y),
#         'y1' = max(df$y)
#       ), shape))
#     }
#     return(figure)
#   }
#   return(callback)
# }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b59d07d... :construction_worker: example 3 chapt.5
#
#
# # app.callback is a decorator which means that it takes a function
# # as its argument.
# # highlight is a function "generator": it's a function that returns function
# app$callback(
#   output = list(id='g1', property='figure'),
#   params = list(input(id='g1', property='selectedData'),
#                 input(id='g2', property='selectedData'),
#                 input(id='g3', property='selectedData'))
# )(highlight('Column 0', 'Column 1'))
#
# app$callback(
#   output = list(id='g2', property='figure'),
#   params = list(input(id='g2', property='selectedData'),
#                 input(id='g1', property='selectedData'),
#                 input(id='g3', property='selectedData'))
# )(highlight('Column 2', 'Column 3'))
#
# app$callback(
#   output = list(id='g3', property='figure'),
#   params = list(input(id='g3', property='selectedData'),
#                 input(id='g1', property='selectedData'),
#                 input(id='g2', property='selectedData'))
# )(highlight('Column 4', 'Column 5'))
#
#
# # app$run_heroku()
<<<<<<< HEAD
>>>>>>> c3a3a477c201204fde289f3750a5e10dbc317464
=======
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5


# app.callback is a decorator which means that it takes a function
# as its argument.
# highlight is a function "generator": it's a function that returns function
app$callback(
  output = list(id='g1', property='figure'),
  params = list(input(id='g1', property='selectedData'),
                input(id='g2', property='selectedData'),
                input(id='g3', property='selectedData'))
)(highlight('Column 0', 'Column 1'))

app$callback(
  output = list(id='g2', property='figure'),
  params = list(input(id='g2', property='selectedData'),
                input(id='g1', property='selectedData'),
                input(id='g3', property='selectedData'))
)(highlight('Column 2', 'Column 3'))

app$callback(
  output = list(id='g3', property='figure'),
  params = list(input(id='g3', property='selectedData'),
                input(id='g1', property='selectedData'),
                input(id='g2', property='selectedData'))
)(highlight('Column 4', 'Column 5'))


# app$run_heroku()
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> parent of b59d07d... :construction_worker: example 3 chapt.5
=======
>>>>>>> b59d07d... :construction_worker: example 3 chapt.5
