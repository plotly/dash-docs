
source('app.R')
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(jsonlite)

components <- new.env()
source('dashr/components.R', local=components)

chapters.installation <- new.env()
source('dashr/chapters/installation/index.R', local=chapters.installation)
chapters.getting_started <- new.env()
source('dashr/chapters/getting-started/index.R', local=chapters.getting_started)
chapters.callbacks <- new.env()
source('dashr/chapters/callbacks/index.R', local=chapters.callbacks)
chapters.state <- new.env()
source('dashr/chapters/state/index.R', local=chapters.state)
chapters.graph_crossfiltering <- new.env()
source('dashr/chapters/graph-crossfiltering/index.R', local=chapters.graph_crossfiltering)
chapters.data_callbacks <- new.env()
source('dashr/chapters/data-callbacks/index.R', local=chapters.data_callbacks)
chapters.faq_gotchas <- new.env()
source('dashr/chapters/faq-gotchas/index.R', local=chapters.faq_gotchas)
chapters.dashCoreComponents <- new.env()
source('dashr/chapters/dash-core-components/index.R', local=chapters.dashCoreComponents)
chapters.dccDropdown <- new.env()
source('dashr/chapters/dash-core-components/Dropdown/index.R', local=chapters.dccDropdown)
chapters.dccSlider <- new.env()
source('dashr/chapters/dash-core-components/Slider/index.R', local=chapters.dccSlider)
chapters.RangeSlider <- new.env()
source('dashr/chapters/dash-core-components/RangeSlider/index.R', local=chapters.RangeSlider)
chapters.Input <- new.env()
source('dashr/chapters/dash-core-components/Input/index.R', local=chapters.Input)
chapters.TextArea <- new.env()
source('dashr/chapters/dash-core-components/Textarea/index.R', local=chapters.TextArea)
chapters.Checklist <- new.env()
source('dashr/chapters/dash-core-components/Checklist/index.R', local=chapters.Checklist)
chapters.RadioItems <- new.env()
source('dashr/chapters/dash-core-components/RadioItems/index.R', local=chapters.RadioItems)
chapters.Button <- new.env()
source('dashr/chapters/dash-core-components/Button/index.R', local=chapters.Button)
chapters.DatePickerSingle  <- new.env()
source('dashr/chapters/dash-core-components/DatePickerSingle/index.R', local=chapters.DatePickerSingle)
chapters.DatePickerRange  <- new.env()
source('dashr/chapters/dash-core-components/DatePickerRange/index.R', local=chapters.DatePickerRange)
chapters.Markdown  <- new.env()
source('dashr/chapters/dash-core-components/Markdown/index.R', local=chapters.Markdown)
chapters.UploadComponent  <- new.env()
source('dashr/chapters/dash-core-components/UploadComponent/index.R', local=chapters.UploadComponent)
chapters.ConfirmDialog  <- new.env()
source('dashr/chapters/dash-core-components/ConfirmDialog/index.R', local=chapters.ConfirmDialog)
chapters.ConfirmDialogProvider  <- new.env()
source('dashr/chapters/dash-core-components/ConfirmDialogProvider/index.R', local=chapters.ConfirmDialogProvider)
chapters.Store  <- new.env()
source('dashr/chapters/dash-core-components/Store/index.R', local=chapters.Store)
chapters.Location  <- new.env()
source('dashr/chapters/dash-core-components/Location/index.R', local=chapters.Location)
chapters.LoadingComponent  <- new.env()
source('dashr/chapters/dash-core-components/LoadingComponent/index.R', local=chapters.LoadingComponent)
chapters.Graph  <- new.env()
source('dashr/chapters/dash-core-components/Graph/index.R', local=chapters.Graph)
chapters.Tabs  <- new.env()
source('dashr/chapters/dash-core-components/Tabs/index.R', local=chapters.Tabs)
chapters.UploadComponent  <- new.env()
source('dashr/chapters/dash-core-components/UploadComponent/index.R', local=chapters.UploadComponent )
chapters.dashHtmlComponents <- new.env()
source('dashr/chapters/dash-html-components/index.R', local=chapters.dashHtmlComponents)
chapters.external_resources <- new.env()
source('dashr/chapters/external-resources/index.R', local=chapters.external_resources)
chapters.dashDataTable <- new.env()
source('dashr/chapters/dashDataTable/index.R', local=chapters.dashDataTable)
chapters.dashDataTablePart1 <- new.env()
source('dashr/chapters/dashDataTable/part1/index.R', local=chapters.dashDataTablePart1)
chapters.dashDataTablePart2 <- new.env()
source('dashr/chapters/dashDataTable/part2/index.R', local=chapters.dashDataTablePart2)
chapters.dashDataTablePart3 <- new.env()
source('dashr/chapters/dashDataTable/part3/index.R', local=chapters.dashDataTablePart3)
chapters.dashDataTablePart4 <- new.env()
source('dashr/chapters/dashDataTable/part4/index.R', local=chapters.dashDataTablePart4)
chapters.dashDataTablePart5 <- new.env()
source('dashr/chapters/dashDataTable/part5/index.R', local=chapters.dashDataTablePart5)
chapters.dashDataTablePart6 <- new.env()
source('dashr/chapters/dashDataTable/part6/index.R', local=chapters.dashDataTablePart6)
chapters.dashDataTablePart7 <- new.env()
source('dashr/chapters/dashDataTable/part7/index.R', local=chapters.dashDataTablePart7)
chapters.dashDataTablePart8 <- new.env()
source('dashr/chapters/dashDataTable/part8/index.R', local=chapters.dashDataTablePart8)
chapters.dashDataTablePart9 <- new.env()
source('dashr/chapters/dashDataTable/part9/index.R', local=chapters.dashDataTablePart9)
chapters.Whats_dash <- new.env()
source('dashr/chapters/Whats_dash/introduction.R', local=chapters.Whats_dash)
chapters.plugins <- new.env()
source('dashr/chapters/plugins/index.R', local=chapters.plugins)
chapters.d3 <- new.env()
source('dashr/chapters/d3-react-components/index.R', local=chapters.d3)
chapters.support <- new.env()
source('dashr/chapters/support/index.R', local=chapters.support)
chapters.search <- new.env()
source('dashr/chapters/search/index.R', local=chapters.search)

header <- htmlDiv(
  className = 'header',
  list(
    htmlDiv(
      style = list(height = '95%'),
      className = 'container-width',
      children = list(
        htmlA(htmlImg(
          style = list(height = '100%'),
          src = 'assets/images/logo.png'
        ), href = 'https://plot.ly/products/dash', className='logo-link'),
        htmlDiv(className='links', children = list(
          htmlA('pricing', className='link', href = 'https://plot.ly/dash/pricing'),
          htmlA('user guide', className='link', href = '/'),
          htmlA('plotly', className='link', href = 'https://plot.ly/'),
          htmlA(children=list(htmlI(className="fa fa-search")), className='link', href='https://dash.plot.ly/search')
        ))
      ))
  ))

header <- htmlDiv(
  className = 'header',
  list(
    htmlDiv(
      style = list(height = '95%'),
      className = 'container-width',
      children = list(
        htmlA(htmlImg(
          style = list(height = '100%'),
          src = 'assets/images/logo.png'
        ), href = 'https://plot.ly/products/dash', className='logo-link'),
        htmlDiv(className='links', children = list(
          htmlA('pricing', className='link', href = 'https://plot.ly/dash/pricing'),
          htmlA('user guide', className='link', href = '/'),
          htmlA('plotly', className='link', href = 'https://plot.ly/'),
          htmlA('🔎', className='link', href='/search')
        ))
      ))
  ))

app$layout(
  header,
  htmlDiv(
    list(
      htmlDiv(
        style = list(display = "none"),
        children = list(dashDataTable())
      ),
      dccLocation(id='url'),
      htmlDiv(
        className='background',
        children=list(
          htmlDiv(id='wait-for-layout'),
          htmlDiv(
            className='container-width',
            children=htmlDiv(
              htmlDiv(id='chapter', className='content'),
              className='content-container'
            )
          )
        )
      )
    )
  )
)

app$callback(
  output=list(id='chapter', property='children'),
  params=list(input('url', 'pathname')),
  function(pathname) {
    switch(
      pathname,
      "/Whats_dash" = return(chapters.Whats_dash$layout),
      "/installation" = return(chapters.installation$layout),
      "/getting-started" = return(chapters.getting_started$layout),
      "/getting-started-part-2" = return(chapters.callbacks$layout),
      "/state" = return(chapters.state$layout),
      "/graph-crossfiltering" = return(chapters.graph_crossfiltering$layout),
      "/data-callbacks" = return(chapters.data_callbacks$layout),
      "/faq-gotchas" = return(chapters.faq_gotchas$layout),
      '/dash-core-components' = return(chapters.dashCoreComponents$layout),
      '/dash-core-components/Dropdown' = return(chapters.dccDropdown$layout),
      '/dash-core-components/Slider' = return(chapters.dccSlider$layout),
      '/dash-core-components/RangeSlider' = return(chapters.RangeSlider$layout),
      '/dash-core-components/Input' = return(chapters.Input$layout),
      '/dash-core-components/Textarea' = return(chapters.TextArea$layout),
      '/dash-core-components/Checklist' = return(chapters.Checklist$layout),
      '/dash-core-components/RadioItems' = return(chapters.RadioItems$layout),
      '/dash-core-components/Button' = return(chapters.Button$layout),
      '/dash-core-components/DatePickerSingle' = return(chapters.DatePickerSingle$layout),
      '/dash-core-components/DatePickerRange' = return(chapters.DatePickerRange$layout),
      '/dash-core-components/Markdown' = return(chapters.Markdown$layout),
      '/dash-core-components/UploadComponent' = return(chapters.UploadComponent$layout),
      '/dash-core-components/ConfirmDialog' = return(chapters.ConfirmDialog$layout),
      '/dash-core-components/ConfirmDialogProvider' = return(chapters.ConfirmDialogProvider$layout),
      '/dash-core-components/Store' = return(chapters.Store$layout),
      '/dash-core-components/Location' = return(chapters.Location$layout),
      '/dash-core-components/LoadingComponent' = return(chapters.LoadingComponent$layout),
      '/dash-core-components/Graph' = return(chapters.Graph$layout),
      '/dash-core-components/Tabs' = return(chapters.Tabs$layout),
      '/dash-core-components/UploadComponent' = return(chapters.UploadComponent$layout),
      '/dash-html-components' = return(chapters.dashHtmlComponents$layout),
      '/dashDataTable' = return(chapters.dashDataTable$layout),
      '/dashDataTable/Part1' = return(chapters.dashDataTablePart1$layout),
      '/dashDataTable/Part2' = return(chapters.dashDataTablePart2$layout),
      '/dashDataTable/Part3' = return(chapters.dashDataTablePart3$layout),
      '/dashDataTable/Part4' = return(chapters.dashDataTablePart4$layout),
      '/dashDataTable/Part5' = return(chapters.dashDataTablePart5$layout),
      '/dashDataTable/Part6' = return(chapters.dashDataTablePart6$layout),
      '/dashDataTable/Part7' = return(chapters.dashDataTablePart7$layout),
      '/dashDataTable/Part8' = return(chapters.dashDataTablePart8$layout),
      '/dashDataTable/Part9' = return(chapters.dashDataTablePart9$layout),
      '/external-resources' = return(chapters.external_resources$layout),
      '/plugins' = return(chapters.plugins$layout),
      '/d3-react-components' = return(chapters.d3$layout),
      '/support' = return(chapters.support$layout),
      '/search' = return(chapters.search$layout),
      {
        htmlDiv(
          list(
            htmlH1('Dash for R User Guide'),
            
            
            components$Section(
              'What\'s Dash?',
              list(
                components$Chapter(
                  'Introduction',
                  href='https://dash.plot.ly/introduction',
                  caption="A quick paragraph about Dash and a link to the talk at Plotcon that started it all."
                ),
                components$Chapter(
                  'Announcement Essay',
                  href='https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503',
                  caption="Our extended essay on Dash. An extended discussion of Dash's architecture and our motivation behind the project."
                ),
                components$Chapter(
                  'Dash App Gallery',
                  href='https://dash.plot.ly/gallery',
                  caption="A glimpse into what's possible with Dash."
                ),
                components$Chapter(
                  'Dash Club',
                  href='https://plot.us12.list-manage.com/subscribe?u=28d7f8f0685d044fb51f0d4ee&id=0c1cb734d7',
                  caption="A fortnightly email newsletter by chriddyp, the creator of Dash."
                )
              )
            ),
            
            
            components$Section(
              'Dash Tutorial',
              list(
                components$Chapter(
                  'Part 1. Installation',
                  href='/installation'
                ),
                components$Chapter(
                  'Part 2. The Dash Layout',
                  href='/getting-started',
                  caption="The Dash `layout` describes what your app will look like and is composed of a set of declarative Dash components."
                ),
                components$Chapter(
                  'Part 3. Basic Callbacks',
                  href='/getting-started-part-2',
                  caption="Dash apps are made interactive through Dash Callbacks:
                  R functions that are automatically called whenever an input component's property changes. Callbacks can be chained,
                  allowing one update in the UI to trigger several updates across the app."
                ),
                components$Chapter(
                  'Part 4. Callbacks With State',
                  href='/state',
                  caption="Basic callbacks are fired whenever the values change.
                  Use Dash `state` with Dash `inputs` to pass in extra values whenever the `inputs` change.
                  `state` is useful for UIs that contain forms or buttons."
                ),
                components$Chapter(
                  'Part 5. Interactive Graphing and Crossfiltering',
                  href='/graph-crossfiltering',
                  caption="Bind interactivity to the Dash `Graph` component whenever you hover, click, or
                  select points on your chart."
                ),
                components$Chapter(
                  'Part 6. Sharing Data Between Callbacks',
                  href='/data-callbacks',
                  caption="`global` variables will break your Dash apps.
                  However, there are other ways to share data between callbacks.
                  This chapter is useful for callbacks that run expensive data processing tasks or process large data."
                ),
                components$Chapter(
                  'Part 7. FAQs and Gotchas',
                  href='/faq-gotchas',
                  caption="If you have read through the rest of the tutorial and still have questions
                  or are encountering unexpected behaviour,this chapter may be useful."
                )
              )
            ),
            
            
            components$Section(
              'Component Libraries',
              list(
                components$Chapter(
                  'Dash Core Components',
                  href='/dash-core-components',
                  caption="The Dash Core Component library contains a set of higher-level components like sliders, graphs, dropdowns, tables, and more."
                ),
                components$Chapter(
                  'Dash HTML Components',
                  href='/dash-html-components',
                  caption="Dash provides all of the available HTML tags as user-friendly Python classes.
                  This chapter explains how this works and the few important key differences between Dash HTML components and standard html."
                ),
                components$Chapter(
                  'Dash DataTable',
                  href='/dashDataTable',
                  caption="(New! Released Nov 2, 2018) The Dash DataTable is our latest and most advanced component.
                  It is an interactive table that supports rich styling, conditional formatting, editing, sorting, filtering, and more."
                )
              )
            ),
            
            
            components$Section(
              'Creating Your Own Components',
              list(
                components$Chapter(
                  'Build Your Own Components',
                  href='/plugins',
                  caption="Dash components are built with React.js. Dash provides 
                  a React → Dash toolchain that generates a Dash-compatible interface to 
                  these components in Python."
                ),
                components$Chapter(
                  'Integrating D3.js into Dash Components',
                  href='/d3-react-components',
                  caption="Tutorials and resources on encapsulating D3.js graphs in Dash-friendly
                  React components. Includes two sample components: a D3.js network graph and a D3.js 
                  sunburst chart."
                )
              )
            ),
            
            
            components$Section(
              'Beyond the Basics',
              list(
                components$Chapter(
                  'Adding CSS & JS and Overriding the Page-Load Template',
                  href='/external-resources',
                  caption="Learn how to add custom CSS and JS to your application with the `assets` directory.
                  Also, learn how to customize the HTML template that Dash serves on page load in order to add custom meta tags, customize the page's title, and more."
                )
              )
            ),
            
            
            components$Section(
              'Production',
              list(
                components$Chapter(
                  'See Our Products Page',
                  href='https://plot.ly/products/dash/'
                )
              )
            ),
            
            
            components$Section(
              'Getting Help',
              list(
                components$Chapter(
                  'The Dash Community Forum',
                  href='https://community.plot.ly/c/dash?_ga=2.35982368.1800098105.1562085881-85134653.1547603472'
                ),
                components$Chapter(
                  'Support and Contact',
                  href='/support'
                )
              )
            ),
            
            
            components$Section(
              'Dash Deployment Server',
              list(
                components$Chapter(
                  'About Dash Deployment Server',
                  href='/faq-gotchas'
                ),
                components$Chapter(
                  'Dash Deployment Server Documentation',
                  href='/faq-gotchas'
                )
              ),
              description="Dash Deployment Server is Plotly's commercial offering for hosting and sharing
              Dash apps on-premises or in the cloud.",
              headerStyle=list('color'='#0D76BF')
            )
          )
        )
      }
    )
  }
)


app$run_server(host = "0.0.0.0", port = Sys.getenv('PORT', 8050))