source('app.R')

library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashUserGuideComponents)
library(jsonlite)
library(stringr)

getVersion <- function(package_name) {
  cat(package_name, ": ", as.character(utils::packageVersion(package_name)), "\n", sep = "")
}

dashDeps <- c("dash", "dashHtmlComponents", "dashCoreComponents",
"dashTable", "R6", "fiery", "routr",
"plotly", "reqres", "jsonlite", "htmltools", "assertthat", "digest",
"base64enc", "mime", "crayon")

cat("########## Environment variables ##########\n")
Sys.getenv()

cat("########## Package versions      ##########\n")
invisible(lapply(dashDeps, getVersion))

cat("########## Working directory     ##########\n")
getwd()

cat("########## App object            ##########\n")
app

components <- new.env()
source('dashr/components.R', local=components)
source('allcallbacks.R')

chapters.whats_dash <- new.env()
source('dashr/chapters/whats-dash/introduction.R', local=chapters.whats_dash)
# Dash Tutorial
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
# Component Libraries (Dash Core Components)
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
chapters.RadioItems  <- new.env()
source('dashr/chapters/dash-core-components/RadioItems/index.R', local=chapters.RadioItems)
chapters.Button  <- new.env()
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
source('dashr/chapters/dash-core-components/UploadComponent/index.R', local=chapters.UploadComponent)
# Component Libraries (Dash HTML Components)
chapters.dashHtmlComponents <- new.env()
source('dashr/chapters/dash-html-components/index.R', local=chapters.dashHtmlComponents)
# Component Libraries (Dash DataTable)
chapters.dashDataTable <- new.env()
source('dashr/chapters/dash-datatable/index.R', local=chapters.dashDataTable)
chapters.dashDataTable1 <- new.env()
source('dashr/chapters/dash-datatable/part1/index.R', local=chapters.dashDataTable1)
chapters.dashDataTable2 <- new.env()
source('dashr/chapters/dash-datatable/part2/index.R', local=chapters.dashDataTable2)
chapters.dashDataTable3 <- new.env()
source('dashr/chapters/dash-datatable/part3/index.R', local=chapters.dashDataTable3)
chapters.dashDataTable4 <- new.env()
source('dashr/chapters/dash-datatable/part4/index.R', local=chapters.dashDataTable4)
chapters.dashDataTable5 <- new.env()
source('dashr/chapters/dash-datatable/part5/index.R', local=chapters.dashDataTable5)
chapters.dashDataTable6 <- new.env()
source('dashr/chapters/dash-datatable/part6/index.R', local=chapters.dashDataTable6)
chapters.dashDataTable7 <- new.env()
source('dashr/chapters/dash-datatable/part7/index.R', local=chapters.dashDataTable7)
chapters.dashDataTable8 <- new.env()
source('dashr/chapters/dash-datatable/part8/index.R', local=chapters.dashDataTable8)
chapters.dashDataTable9 <- new.env()
source('dashr/chapters/dash-datatable/part9/index.R', local=chapters.dashDataTable9)
chapters.dashDataTable10 <- new.env()
source('dashr/chapters/dash-datatable/part10/index.R', local=chapters.dashDataTable10)
# Component Libraries (Dash DAQ Components)
chapters.dashDaq <- new.env()
source('dashr/chapters/dash-daq/index.R', local=chapters.dashDaq)
chapters.booleanswitch <- new.env()
source('dashr/chapters/dash-daq/boolean-switch/booleanswitch.R', local = chapters.booleanswitch)
chapters.colorpicker <- new.env()
source('dashr/chapters/dash-daq/color-picker/colorpicker.R', local = chapters.colorpicker)
chapters.gauge <- new.env()
source('dashr/chapters/dash-daq/gauge/gauge.R', local = chapters.gauge)
chapters.graduatedbar <- new.env()
source('dashr/chapters/dash-daq/graduated-bar/graduatedbar.R', local = chapters.graduatedbar)
chapters.indicator <- new.env()
source('dashr/chapters/dash-daq/indicator/indicator.R', local = chapters.indicator)
chapters.joystick <- new.env()
source('dashr/chapters/dash-daq/joystick/joystick.R', local = chapters.joystick)
chapters.knob <- new.env()
source('dashr/chapters/dash-daq/knob/knob.R', local = chapters.knob)
chapters.leddisplay <- new.env()
source('dashr/chapters/dash-daq/led-display/leddisplay.R', local = chapters.leddisplay)
chapters.numericinput <- new.env()
source('dashr/chapters/dash-daq/numeric-input/numericinput.R', local = chapters.numericinput)
chapters.powerbutton <- new.env()
source('dashr/chapters/dash-daq/power-button/powerbutton.R', local = chapters.powerbutton)
chapters.precisioninput <- new.env()
source('dashr/chapters/dash-daq/precision-input/precisioninput.R', local = chapters.precisioninput)
chapters.slider <- new.env()
source('dashr/chapters/dash-daq/slider/slider.R', local = chapters.slider)
chapters.stopbutton <- new.env()
source('dashr/chapters/dash-daq/stop-button/stopbutton.R', local = chapters.stopbutton)
chapters.tank <- new.env()
source('dashr/chapters/dash-daq/tank/tank.R', local = chapters.tank)
chapters.thermometer <- new.env()
source('dashr/chapters/dash-daq/thermometer/thermometer.R', local = chapters.thermometer)
chapters.toggleswitch <- new.env()
source('dashr/chapters/dash-daq/toggle-switch/toggleswitch.R', local = chapters.toggleswitch)
chapters.darkthemeprovider <- new.env()
source('dashr/chapters/dash-daq/dark-theme-provider/darkthemeprovider.R', local = chapters.darkthemeprovider)
# Component Libraries (Dash Canvas)
chapters.dashCanvas <- new.env()
source('dashr/chapters/dash-canvas/index.R', local=chapters.dashCanvas)
# Component Libraries (Dash Cytoscape)
chapters.dashCytoscape <- new.env()
source('dashr/chapters/dash-cytoscape/index.R', local=chapters.dashCytoscape)
chapters.dashCytoscape1 <- new.env()
source('dashr/chapters/dash-cytoscape/elements/index.R', local=chapters.dashCytoscape1)
chapters.dashCytoscape2 <- new.env()
source('dashr/chapters/dash-cytoscape/layout/index.R', local=chapters.dashCytoscape2)
chapters.dashCytoscape3 <- new.env()
source('dashr/chapters/dash-cytoscape/styling/index.R', local=chapters.dashCytoscape3)
chapters.dashCytoscape4 <- new.env()
source('dashr/chapters/dash-cytoscape/callbacks/index.R', local=chapters.dashCytoscape4)
chapters.dashCytoscape5 <- new.env()
source('dashr/chapters/dash-cytoscape/events/index.R', local=chapters.dashCytoscape5)
chapters.dashCytoscape6 <- new.env()
source('dashr/chapters/dash-cytoscape/phylogeny/index.R', local=chapters.dashCytoscape6)
chapters.dashCytoscape7 <- new.env()
source('dashr/chapters/dash-cytoscape/reference/index.R', local=chapters.dashCytoscape7)
# Component Libraries (Dash Bio)
chapters.dashBio <- new.env()
source('dashr/chapters/dash-bio/index.R', local=chapters.dashBio)
chapters.alignment <- new.env()
source('dashr/chapters/dash-bio/alignment-chart/alignment-chart.R', local=chapters.alignment)
chapters.circos <- new.env()
source('dashr/chapters/dash-bio/circos/circos.R', local=chapters.circos)
chapters.clustergram <- new.env()
source('dashr/chapters/dash-bio/clustergram/clustergram.R', local=chapters.clustergram)
chapters.ideogram <- new.env()
source('dashr/chapters/dash-bio/ideogram/ideogram.R', local=chapters.ideogram)
chapters.volcanoplot <- new.env()
source('dashr/chapters/dash-bio/volcanoplot/volcano.R', local=chapters.volcanoplot)
chapters.manhattan <- new.env()
source('dashr/chapters/dash-bio/manhattan/manhattan.R', local = chapters.manhattan)
chapters.molecule3dviewer <- new.env()
source('dashr/chapters/dash-bio/molecule3dviewer/molecule3dviewer.R', local=chapters.molecule3dviewer)
chapters.molecule2dviewer <- new.env()
source('dashr/chapters/dash-bio/molecule2dviewer/molecule2dviewer.R', local=chapters.molecule2dviewer)
chapters.needleplot <- new.env()
source('dashr/chapters/dash-bio/needleplot/needleplot.R', local=chapters.needleplot)
chapters.oncoprint <- new.env()
source('dashr/chapters/dash-bio/oncoprint/oncoprint.R', local=chapters.oncoprint)
chapters.sequenceviewer <- new.env()
source('dashr/chapters/dash-bio/sequenceviewer/sequenceviewer.R', local=chapters.sequenceviewer)
chapters.speck <- new.env()
source("dashr/chapters/dash-bio/speck/speck.R", local=chapters.speck)
# Beyond the Basics
chapters.external_resources <- new.env()
source('dashr/chapters/external-resources/index.R', local=chapters.external_resources)
chapters.plugins <- new.env()
source('dashr/chapters/plugins/index.R', local=chapters.plugins)
chapters.d3 <- new.env()
source('dashr/chapters/d3-react-components/index.R', local=chapters.d3)
chapters.support <- new.env()
source('dashr/chapters/support/index.R', local=chapters.support)
chapters.search <- new.env()
source('dashr/chapters/search/index.R', local=chapters.search)
chapters.deployment <- new.env()
source('dashr/chapters/deployment/index.R', local=chapters.deployment)
chapters.urls <- new.env()
source('dashr/chapters/urls/index.R', local=chapters.urls)
chapters.devtools <- new.env()
source('dashr/chapters/devtools/index.R', local=chapters.devtools)

header <- htmlDiv(
  className = 'header',
  list(
    htmlDiv(
      style = list(height = '95%'),
      className = 'container-width',
      children = list(
        htmlA(htmlImg(
          style = list(height = '100%'),
          src = 'https://dash.plotly.com/assets/images/logo-plotly.png'
        ), href = 'https://plotly.com/products/dash', className='logo-link'),
        htmlDiv(className='links', children = list(
          htmlA('pricing', className='link', href = 'https://plotly.com/dash/pricing'),
          htmlA('user guide', className='link', href = '/'),
          htmlA('plotly', className='link', href = 'https://plotly.com/'),
          htmlA('\U{1F50E}', className='link', href='/search')
        ))
    ))
))

app$layout(htmlDiv(
  list(
    # Stores used by examples.
    dccStore(id = 'memory'),
    dccStore(id = 'memory-output'),
    dccStore(id = 'local', storage_type = 'local'),
    dccStore(id = 'session', storage_type = 'session'),
    
    # div used in tests
    htmlDiv(id = 'wait-for-layout'),
    
    dccLocation(id = 'url', refresh = FALSE),
    
    header,
    
    htmlDiv(
      className = 'content-wrapper',
      children = list(
        htmlDiv(list(
          htmlDiv(id = 'backlinks-top', className = 'backlinks'),
          htmlDiv(htmlDiv(id = 'chapter', className = 'content'),
                  className = 'content-container'),
          htmlDiv(id = 'backlinks-bottom', className = 'backlinks')
        ),
        className = 'rhs-content container-width'),
        
        pageMenu(id = 'pagemenu')
        
      )
    )
  )
))

app$callback(
  output=list(id='chapter', property='children'),
  params=list(input('url', 'pathname')),
  function(pathname) {
    switch(
      pathname,
      '/introduction' = return(chapters.whats_dash$layout),
      # Dash Tutorial
      '/installation' = return(chapters.installation$layout),
      '/getting-started' = return(chapters.getting_started$layout),
      '/getting-started-part-2' = return(chapters.callbacks$layout),
      '/state' = return(chapters.state$layout),
      '/interactive-graphing' = return(chapters.graph_crossfiltering$layout),
      '/sharing-data-between-callbacks' = return(chapters.data_callbacks$layout),
      '/faqs' = return(chapters.faq_gotchas$layout),
      # Component Libraries (Dash Core Components)
      '/dash-core-components' = return(chapters.dashCoreComponents$layout),
      '/dash-core-components/dropdown' = return(chapters.dccDropdown$layout),
      '/dash-core-components/slider' = return(chapters.dccSlider$layout),
      '/dash-core-components/rangeslider' = return(chapters.RangeSlider$layout),
      '/dash-core-components/input' = return(chapters.Input$layout),
      '/dash-core-components/textarea' = return(chapters.TextArea$layout),
      '/dash-core-components/checklist' = return(chapters.Checklist$layout),
      '/dash-core-components/radioitems' = return(chapters.RadioItems$layout),
      '/dash-core-components/button' = return(chapters.Button$layout),
      '/dash-core-components/datepickersingle' = return(chapters.DatePickerSingle$layout),
      '/dash-core-components/datepickerrange' = return(chapters.DatePickerRange$layout),
      '/dash-core-components/markdown' = return(chapters.Markdown$layout),
      '/dash-core-components/uploadcomponent' = return(chapters.UploadComponent$layout),
      '/dash-core-components/confirmdialog' = return(chapters.ConfirmDialog$layout),
      '/dash-core-components/confirmdialogprovider' = return(chapters.ConfirmDialogProvider$layout),
      '/dash-core-components/store' = return(chapters.Store$layout),
      '/dash-core-components/location' = return(chapters.Location$layout),
      '/dash-core-components/loadingcomponent' = return(chapters.LoadingComponent$layout),
      '/dash-core-components/graph' = return(chapters.Graph$layout),
      '/dash-core-components/tabs' = return(chapters.Tabs$layout),
      '/dash-core-components/uploadcomponent' = return(chapters.UploadComponent$layout),
      # Component Libraries (Dash HTML Components)
      '/dash-html-components' = return(chapters.dashHtmlComponents$layout),
      # Component Libraries (Dash DataTable)
      '/datatable' = return(chapters.dashDataTable$layout),
      '/datatable/sizing' = return(chapters.dashDataTable1$layout),
      '/datatable/style' = return(chapters.dashDataTable2$layout),
      '/datatable/interactivity' = return(chapters.dashDataTable3$layout),
      '/datatable/callbacks' = return(chapters.dashDataTable4$layout),
      '/datatable/typing' = return(chapters.dashDataTable5$layout),
      '/datatable/editable' = return(chapters.dashDataTable6$layout),
      '/datatable/dropdowns' = return(chapters.dashDataTable7$layout),
      '/datatable/virtualization' = return(chapters.dashDataTable8$layout),
      '/datatable/filtering' = return(chapters.dashDataTable9$layout),
      '/datatable/reference' = return(chapters.dashDataTable10$layout),
      # Component Libraries (Dash DAQ Components)
      '/dash-daq' = return(chapters.dashDaq$layout),
      '/dash-daq/booleanswitch' = return(chapters.booleanswitch$layout),
      '/dash-daq/colorpicker' = return(chapters.colorpicker$layout),
      '/dash-daq/gauge' = return(chapters.gauge$layout),
      '/dash-daq/graduatedbar' = return(chapters.graduatedbar$layout),
      '/dash-daq/indicator' = return(chapters.indicator$layout),
      '/dash-daq/joystick' = return(chapters.joystick$layout),
      '/dash-daq/knob' = return(chapters.knob$layout),
      '/dash-daq/leddisplay' = return(chapters.leddisplay$layout),
      '/dash-daq/numericinput' = return(chapters.numericinput$layout),
      '/dash-daq/powerbutton' = return(chapters.powerbutton$layout),
      '/dash-daq/precisioninput' = return(chapters.precisioninput$layout),
      '/dash-daq/slider' = return(chapters.slider$layout),
      '/dash-daq/stopbutton' = return(chapters.stopbutton$layout),
      '/dash-daq/tank' = return(chapters.tank$layout),
      '/dash-daq/thermometer' = return(chapters.thermometer$layout),
      '/dash-daq/toggleswitch' = return(chapters.toggleswitch$layout),
      '/dash-daq/darkthemeprovider' = return(chapters.darkthemeprovider$layout),
      # Component Libraries (Dash Canvas)
      '/dash-canvas' = return(chapters.dashCanvas$layout),
      # Component Libraries (Dash Cytoscape)
      '/cytoscape' = return(chapters.dashCytoscape$layout),
      '/cytoscape/elements' = return(chapters.dashCytoscape1$layout),
      '/cytoscape/layout' = return(chapters.dashCytoscape2$layout),
      '/cytoscape/styling' = return(chapters.dashCytoscape3$layout),
      '/cytoscape/callbacks' = return(chapters.dashCytoscape4$layout),
      '/cytoscape/events' = return(chapters.dashCytoscape5$layout),
      '/cytoscape/phylogeny' = return(chapters.dashCytoscape6$layout),
      '/cytoscape/reference' = return(chapters.dashCytoscape7$layout),
      # Component Libraries (Dash Bio)
      "/dash-bio" = return(chapters.dashBio$layout),
      "/dash-bio/alignmentchart" = return(chapters.alignment$layout),
      "/dash-bio/circos" = return(chapters.circos$layout),
      "/dash-bio/clustergram" = return(chapters.clustergram$layout),
      "/dash-bio/ideogram" = return(chapters.ideogram$layout),
      "/dash-bio/manhattanplot" = return(chapters.manhattan$layout),
      "/dash-bio/molecule2dviewer" = return(chapters.molecule2dviewer$layout),
      "/dash-bio/molecule3dviewer" = return(chapters.molecule3dviewer$layout),
      "/dash-bio/volcanoplot" = return(chapters.volcanoplot$layout),
      "/dash-bio/needleplot" = return(chapters.needleplot$layout),
      "/dash-bio/oncoprint" = return(chapters.oncoprint$layout),
      "/dash-bio/sequenceviewer" = return(chapters.sequenceviewer$layout),
      "/dash-bio/speck" = return(chapters.speck$layout),
      # Production
      "/deployment" = return(chapters.deployment$layout),
      # Beyond the Basics
      '/external-resources' = return(chapters.external_resources$layout),
      '/urls' = return(chapters.urls$layout),
      '/devtools' = return(chapters.devtools$layout),      
      '/support' = return(chapters.support$layout),
      '/plugins' = return(chapters.plugins$layout),
      '/d3-react-components' = return(chapters.d3$layout),
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
                href='/introduction',
                caption="A quick paragraph about Dash and a link to the talk at Plotcon that started it all."
                ),
                components$Chapter(
                'Announcement Essay',
                href='https://medium.com/plotly/announcing-dash-for-r-82dce99bae13',
                caption="Our extended essay on Dash. An extended discussion of Dash's architecture and our motivation behind the project."
                ),
                components$Chapter(
                'Dash App Gallery',
                href='https://dash.plotly.com/gallery',
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
                'Part 4. More About Callbacks',
                href='/state',
                caption="Basic callbacks are fired whenever the values change.
                Use Dash `state` with Dash `inputs` to pass in extra values whenever the `inputs` change.
                `state` is useful for UIs that contain forms or buttons."
                ),
                components$Chapter(
                'Part 5. Interactive Graphing and Crossfiltering',
                href='/interactive-graphing',
                caption="Bind interactivity to the Dash `Graph` component whenever you hover, click, or
                select points on your chart."
                ),
                components$Chapter(
                'Part 6. Sharing Data Between Callbacks',
                href='/sharing-data-between-callbacks',
                caption="`global` variables will break your Dash apps.
                However, there are other ways to share data between callbacks.
                This chapter is useful for callbacks that run expensive data processing tasks or process large data."
                ),
                components$Chapter(
                'Part 7. FAQs and Gotchas',
                href='/faqs',
                caption="If you have read through the rest of the tutorial and still have questions
                or are encountering unexpected behaviour, this chapter may be useful."
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
                caption="Dash provides all of the available HTML tags as user-friendly R functions.
                This chapter explains how this works and the few important key differences between Dash HTML components and standard html."
                ),
                components$Chapter(
                'Dash DataTable',
                href='/datatable',
                caption="(New! Released Nov 2, 2018) The Dash DataTable is our latest and most advanced component.
                It is an interactive table that supports rich styling, conditional formatting, editing, sorting, filtering, and more."
                ),
                components$Chapter(
                'Dash DAQ Components',
                href='/dash-daq',
                caption="Beautifully styled technical components for data acquisition and engineering applications."
                ),
                components$Chapter(
                'Dash Canvas',
                href='/dash-canvas',
                caption="(New! Released March 2019) Drawing and annotations for image processing."
                ),
                components$Chapter(
                'Dash Cytoscape',
                href='/cytoscape',
                caption="Dash Cytoscape is our new network visualization component. It offers a declarative and
                user-friendly R interface to create beautiful, customizable, interactive and reactive graphs."
                ),
                components$Chapter(
                'Dash Bio Components',
                href='/dash-bio',
                caption="(New! Released April 2019) Components dedicated to visualizing bioinformatics data."
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
                these components in R."
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
                ),
                components$Chapter(
                'URL Routing & Multiple Apps',
                href='/urls',
                caption="Dash provides two components (`dccLink` and `dccLocation`) that allow you to easily make fast multipage apps using its own \"Single Page App (SPA)\" design pattern."
                ),
                components$Chapter(
                'Dev tools',
                href='/devtools',
                caption="Dash dev tools reference"
                )
              )
            ),


            components$Section(
              'Production',
              list(
                components$Chapter(
                'See Our Products Page',
                href='https://plotly.com/products/dash/'
                ),
                components$Chapter(
                  'Deployment',
                  href='/deployment'
                )
              )
            ),


            components$Section(
            'Getting Help',
              list(
                components$Chapter(
                'The Dash Community Forum',
                href='https://community.plotly.com/c/dash?_ga=2.35982368.1800098105.1562085881-85134653.1547603472'
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
                href='https://plotly.com/dash/pricing/?_ga=2.180458663.1075922756.1562168385-916141078.1562168385'
                ),
                components$Chapter(
                'Dash Deployment Server Documentation',
                href='https://dash.plotly.com/dash-deployment-server'
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

app$callback(
  output=list(output('chapter', 'children'),
              output('pagemenu', 'dummy2')
              ),
  params=list(input('url', 'pathname')),
  function(pathname) {
    return(list(''))
  }
)

app$callback(
  output('pagemenu', 'dummy'),
  params=list(input('chapter', 'children')),
  clientsideFunction(
    namespace = 'clientside',
    function_name = 'pagemenu'
  )
)

app$run_server(host = "0.0.0.0")
