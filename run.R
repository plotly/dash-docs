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
source('dash_docs/components.R', local=components)
source('allcallbacks.R')

chapters.whats_dash <- new.env()
source('dash_docs/chapters/whats_dash/introduction.R', local=chapters.whats_dash)
# Dash Tutorial
chapters.installation <- new.env()
source('dash_docs/chapters/installation/index.R', local=chapters.installation)
chapters.getting_started <- new.env()
source('dash_docs/chapters/getting_started/index.R', local=chapters.getting_started)
chapters.callbacks <- new.env()
source('dash_docs/chapters/basic_callbacks/index.R', local=chapters.callbacks)
chapters.graph_crossfiltering <- new.env()
source('dash_docs/chapters/graph_crossfiltering/index.R', local=chapters.graph_crossfiltering)
chapters.sharing_data <- new.env()
source('dash_docs/chapters/sharing_data/index.R', local=chapters.sharing_data)
chapters.faq_gotchas <- new.env()
source('dash_docs/chapters/faq_gotchas/index.R', local=chapters.faq_gotchas)
# Dash Callbacks
chapters.advanced_callbacks <- new.env()
source('dash_docs/chapters/advanced_callbacks/index.R', local=chapters.advanced_callbacks)
chapters.clientside_callbacks <- new.env()
source('dash_docs/chapters/clientside_callbacks/index.R', local=chapters.clientside_callbacks)
chapters.callback_gotchas <- new.env()
source('dash_docs/chapters/callback_gotchas/index.R', local=chapters.callback_gotchas)
# Component Libraries (Dash Core Components)
chapters.dashCoreComponents <- new.env()
source('dash_docs/chapters/dash_core_components/index.R', local=chapters.dashCoreComponents)
chapters.dccDropdown <- new.env()
source('dash_docs/chapters/dash_core_components/Dropdown/index.R', local=chapters.dccDropdown)
chapters.dccSlider <- new.env()
source('dash_docs/chapters/dash_core_components/Slider/index.R', local=chapters.dccSlider)
chapters.RangeSlider <- new.env()
source('dash_docs/chapters/dash_core_components/RangeSlider/index.R', local=chapters.RangeSlider)
chapters.Input <- new.env()
source('dash_docs/chapters/dash_core_components/Input/index.R', local=chapters.Input)
chapters.TextArea <- new.env()
source('dash_docs/chapters/dash_core_components/Textarea/index.R', local=chapters.TextArea)
chapters.Checklist <- new.env()
source('dash_docs/chapters/dash_core_components/Checklist/index.R', local=chapters.Checklist)
chapters.RadioItems  <- new.env()
source('dash_docs/chapters/dash_core_components/RadioItems/index.R', local=chapters.RadioItems)
chapters.Button  <- new.env()
source('dash_docs/chapters/dash_core_components/Button/index.R', local=chapters.Button)
chapters.DatePickerSingle  <- new.env()
source('dash_docs/chapters/dash_core_components/DatePickerSingle/index.R', local=chapters.DatePickerSingle)
chapters.DatePickerRange  <- new.env()
source('dash_docs/chapters/dash_core_components/DatePickerRange/index.R', local=chapters.DatePickerRange)
chapters.Markdown  <- new.env()
source('dash_docs/chapters/dash_core_components/Markdown/index.R', local=chapters.Markdown)
chapters.UploadComponent  <- new.env()
source('dash_docs/chapters/dash_core_components/Upload/index.R', local=chapters.UploadComponent)
chapters.ConfirmDialog  <- new.env()
source('dash_docs/chapters/dash_core_components/ConfirmDialog/index.R', local=chapters.ConfirmDialog)
chapters.ConfirmDialogProvider  <- new.env()
source('dash_docs/chapters/dash_core_components/ConfirmDialogProvider/index.R', local=chapters.ConfirmDialogProvider)
chapters.Store  <- new.env()
source('dash_docs/chapters/dash_core_components/Store/index.R', local=chapters.Store)
chapters.Location  <- new.env()
source('dash_docs/chapters/dash_core_components/Location/index.R', local=chapters.Location)
chapters.LoadingComponent  <- new.env()
source('dash_docs/chapters/dash_core_components/Loading/index.R', local=chapters.LoadingComponent)
chapters.Graph  <- new.env()
source('dash_docs/chapters/dash_core_components/Graph/index.R', local=chapters.Graph)
chapters.Tabs  <- new.env()
source('dash_docs/chapters/dash_core_components/Tabs/index.R', local=chapters.Tabs)
chapters.UploadComponent  <- new.env()
source('dash_docs/chapters/dash_core_components/Upload/index.R', local=chapters.UploadComponent)
# Component Libraries (Dash HTML Components)
chapters.dashHtmlComponents <- new.env()
source('dash_docs/chapters/dash_html_components/index.R', local=chapters.dashHtmlComponents)
# Component Libraries (Dash DataTable)
chapters.dashDataTable <- new.env()
source('dash_docs/chapters/dash_datatable/index.R', local=chapters.dashDataTable)
chapters.dashDataTableSizing <- new.env()
source('dash_docs/chapters/dash_datatable/width/index.R', local=chapters.dashDataTableSizing)
chapters.dashDataTable2 <- new.env()
source('dash_docs/chapters/dash_datatable/part2/index.R', local=chapters.dashDataTable2)
chapters.dashDataTable3 <- new.env()
source('dash_docs/chapters/dash_datatable/part3/index.R', local=chapters.dashDataTable3)
chapters.dashDataTable4 <- new.env()
source('dash_docs/chapters/dash_datatable/part4/index.R', local=chapters.dashDataTable4)
chapters.dashDataTable5 <- new.env()
source('dash_docs/chapters/dash_datatable/part5/index.R', local=chapters.dashDataTable5)
chapters.dashDataTable6 <- new.env()
source('dash_docs/chapters/dash_datatable/part6/index.R', local=chapters.dashDataTable6)
chapters.dashDataTable7 <- new.env()
source('dash_docs/chapters/dash_datatable/part7/index.R', local=chapters.dashDataTable7)
chapters.dashDataTable8 <- new.env()
source('dash_docs/chapters/dash_datatable/part8/index.R', local=chapters.dashDataTable8)
chapters.dashDataTable9 <- new.env()
source('dash_docs/chapters/dash_datatable/part9/index.R', local=chapters.dashDataTable9)
chapters.dashDataTable10 <- new.env()
source('dash_docs/chapters/dash_datatable/part10/index.R', local=chapters.dashDataTable10)
# Component Libraries (Dash DAQ Components)
chapters.dashDaq <- new.env()
source('dash_docs/chapters/dash_daq/index.R', local=chapters.dashDaq)
chapters.booleanswitch <- new.env()
source('dash_docs/chapters/dash_daq/boolean-switch/booleanswitch.R', local = chapters.booleanswitch)
chapters.colorpicker <- new.env()
source('dash_docs/chapters/dash_daq/color-picker/colorpicker.R', local = chapters.colorpicker)
chapters.gauge <- new.env()
source('dash_docs/chapters/dash_daq/gauge/gauge.R', local = chapters.gauge)
chapters.graduatedbar <- new.env()
source('dash_docs/chapters/dash_daq/graduated-bar/graduatedbar.R', local = chapters.graduatedbar)
chapters.indicator <- new.env()
source('dash_docs/chapters/dash_daq/indicator/indicator.R', local = chapters.indicator)
chapters.joystick <- new.env()
source('dash_docs/chapters/dash_daq/joystick/joystick.R', local = chapters.joystick)
chapters.knob <- new.env()
source('dash_docs/chapters/dash_daq/knob/knob.R', local = chapters.knob)
chapters.leddisplay <- new.env()
source('dash_docs/chapters/dash_daq/led-display/leddisplay.R', local = chapters.leddisplay)
chapters.numericinput <- new.env()
source('dash_docs/chapters/dash_daq/numeric-input/numericinput.R', local = chapters.numericinput)
chapters.powerbutton <- new.env()
source('dash_docs/chapters/dash_daq/power-button/powerbutton.R', local = chapters.powerbutton)
chapters.precisioninput <- new.env()
source('dash_docs/chapters/dash_daq/precision-input/precisioninput.R', local = chapters.precisioninput)
chapters.slider <- new.env()
source('dash_docs/chapters/dash_daq/slider/slider.R', local = chapters.slider)
chapters.stopbutton <- new.env()
source('dash_docs/chapters/dash_daq/stop-button/stopbutton.R', local = chapters.stopbutton)
chapters.tank <- new.env()
source('dash_docs/chapters/dash_daq/tank/tank.R', local = chapters.tank)
chapters.thermometer <- new.env()
source('dash_docs/chapters/dash_daq/thermometer/thermometer.R', local = chapters.thermometer)
chapters.toggleswitch <- new.env()
source('dash_docs/chapters/dash_daq/toggle-switch/toggleswitch.R', local = chapters.toggleswitch)
chapters.darkthemeprovider <- new.env()
source('dash_docs/chapters/dash_daq/dark-theme-provider/darkthemeprovider.R', local = chapters.darkthemeprovider)
# Component Libraries (Dash Canvas)
chapters.dashCanvas <- new.env()
source('dash_docs/chapters/dash_canvas/index.R', local=chapters.dashCanvas)
# Component Libraries (Dash Cytoscape)
chapters.dashCytoscape <- new.env()
source('dash_docs/chapters/dash_cytoscape/index.R', local=chapters.dashCytoscape)
chapters.dashCytoscape1 <- new.env()
source('dash_docs/chapters/dash_cytoscape/elements/index.R', local=chapters.dashCytoscape1)
chapters.dashCytoscape2 <- new.env()
source('dash_docs/chapters/dash_cytoscape/layout/index.R', local=chapters.dashCytoscape2)
chapters.dashCytoscape3 <- new.env()
source('dash_docs/chapters/dash_cytoscape/styling/index.R', local=chapters.dashCytoscape3)
chapters.dashCytoscape4 <- new.env()
source('dash_docs/chapters/dash_cytoscape/callbacks/index.R', local=chapters.dashCytoscape4)
chapters.dashCytoscape5 <- new.env()
source('dash_docs/chapters/dash_cytoscape/events/index.R', local=chapters.dashCytoscape5)
chapters.dashCytoscape6 <- new.env()
source('dash_docs/chapters/dash_cytoscape/phylogeny/index.R', local=chapters.dashCytoscape6)
chapters.dashCytoscape7 <- new.env()
source('dash_docs/chapters/dash_cytoscape/reference/index.R', local=chapters.dashCytoscape7)
# Component Libraries (Dash Bio)
chapters.dashBio <- new.env()
source('dash_docs/chapters/dash_bio/index.R', local=chapters.dashBio)
chapters.alignment <- new.env()
source('dash_docs/chapters/dash_bio/alignment-chart/alignment-chart.R', local=chapters.alignment)
chapters.circos <- new.env()
source('dash_docs/chapters/dash_bio/circos/circos.R', local=chapters.circos)
chapters.clustergram <- new.env()
source('dash_docs/chapters/dash_bio/clustergram/clustergram.R', local=chapters.clustergram)
chapters.ideogram <- new.env()
source('dash_docs/chapters/dash_bio/ideogram/ideogram.R', local=chapters.ideogram)
chapters.volcanoplot <- new.env()
source('dash_docs/chapters/dash_bio/volcanoplot/volcano.R', local=chapters.volcanoplot)
chapters.manhattan <- new.env()
source('dash_docs/chapters/dash_bio/manhattan/manhattan.R', local = chapters.manhattan)
chapters.molecule3dviewer <- new.env()
source('dash_docs/chapters/dash_bio/molecule3dviewer/molecule3dviewer.R', local=chapters.molecule3dviewer)
chapters.molecule2dviewer <- new.env()
source('dash_docs/chapters/dash_bio/molecule2dviewer/molecule2dviewer.R', local=chapters.molecule2dviewer)
chapters.needleplot <- new.env()
source('dash_docs/chapters/dash_bio/needleplot/needleplot.R', local=chapters.needleplot)
chapters.oncoprint <- new.env()
source('dash_docs/chapters/dash_bio/oncoprint/oncoprint.R', local=chapters.oncoprint)
chapters.sequenceviewer <- new.env()
source('dash_docs/chapters/dash_bio/sequenceviewer/sequenceviewer.R', local=chapters.sequenceviewer)
chapters.speck <- new.env()
source("dash_docs/chapters/dash_bio/speck/speck.R", local=chapters.speck)
# Beyond the Basics
chapters.external_resources <- new.env()
source('dash_docs/chapters/external_resources/index.R', local=chapters.external_resources)
chapters.plugins <- new.env()
source('dash_docs/chapters/plugins/index.R', local=chapters.plugins)
chapters.d3 <- new.env()
source('dash_docs/chapters/d3_react_components/index.R', local=chapters.d3)
chapters.support <- new.env()
source('dash_docs/chapters/support/index.R', local=chapters.support)
chapters.deployment <- new.env()
source('dash_docs/chapters/deployment/index.R', local=chapters.deployment)
chapters.urls <- new.env()
source('dash_docs/chapters/urls/index.R', local=chapters.urls)
chapters.devtools <- new.env()
source('dash_docs/chapters/devtools/index.R', local=chapters.devtools)

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
          htmlA('pricing', className='link', href = 'https://plotly.com/dash'),
          htmlA('user guide', className='link', href = '/'),
          htmlA('plotly', className='link', href = 'https://plotly.com/')
        ))
    ))
))

app$layout(htmlDiv(
  list(
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

        PageMenu(id = 'pagemenu')

      )
    )
  )
))

app$callback(
  output=list(output(id='chapter', property='children'),
              output(id='pagemenu', property='dummy2')),
  params=list(input('url', 'pathname')),
  function(pathname) {
    return(list(
      switch(
      pathname,
      '/introduction' = chapters.whats_dash$layout,
      # Dash Tutorial
      '/installation' = chapters.installation$layout,
      '/layout' = chapters.getting_started$layout,
      '/basic-callbacks' = chapters.callbacks$layout,
      '/interactive-graphing' = chapters.graph_crossfiltering$layout,
      '/sharing-data-between-callbacks' = chapters.sharing_data$layout,
      '/faqs' = chapters.faq_gotchas$layout,
      # Dash Callbacks
      '/advanced-callbacks' = chapters.advanced_callbacks$layout,
      '/clientside-callbacks' = chapters.clientside_callbacks$layout,
      '/callback-gotchas' = chapters.callback_gotchas$layout,
      # Component Libraries (Dash Core Components)
      '/dash-core-components' = chapters.dashCoreComponents$layout,
      '/dash-core-components/dropdown' = chapters.dccDropdown$layout,
      '/dash-core-components/slider' = chapters.dccSlider$layout,
      '/dash-core-components/rangeslider' = chapters.RangeSlider$layout,
      '/dash-core-components/input' = chapters.Input$layout,
      '/dash-core-components/textarea' = chapters.TextArea$layout,
      '/dash-core-components/checklist' = chapters.Checklist$layout,
      '/dash-core-components/radioitems' = chapters.RadioItems$layout,
      '/dash-core-components/button' = chapters.Button$layout,
      '/dash-core-components/datepickersingle' = chapters.DatePickerSingle$layout,
      '/dash-core-components/datepickerrange' = chapters.DatePickerRange$layout,
      '/dash-core-components/markdown' = chapters.Markdown$layout,
      '/dash-core-components/uploadcomponent' = chapters.UploadComponent$layout,
      '/dash-core-components/confirmdialog' = chapters.ConfirmDialog$layout,
      '/dash-core-components/confirmdialogprovider' = chapters.ConfirmDialogProvider$layout,
      '/dash-core-components/store' = chapters.Store$layout,
      '/dash-core-components/location' = chapters.Location$layout,
      '/dash-core-components/loadingcomponent' = chapters.LoadingComponent$layout,
      '/dash-core-components/graph' = chapters.Graph$layout,
      '/dash-core-components/tabs' = chapters.Tabs$layout,
      '/dash-core-components/uploadcomponent' = chapters.UploadComponent$layout,
      # Component Libraries (Dash HTML Components)
      '/dash-html-components' = chapters.dashHtmlComponents$layout,
      # Component Libraries (Dash DataTable)
      '/datatable' = chapters.dashDataTable$layout,
      '/datatable/width' = chapters.dashDataTableSizing$layout,
      '/datatable/style' = chapters.dashDataTable2$layout,
      '/datatable/interactivity' = chapters.dashDataTable3$layout,
      '/datatable/callbacks' = chapters.dashDataTable4$layout,
      '/datatable/typing' = chapters.dashDataTable5$layout,
      '/datatable/editable' = chapters.dashDataTable6$layout,
      '/datatable/dropdowns' = chapters.dashDataTable7$layout,
      '/datatable/virtualization' = chapters.dashDataTable8$layout,
      '/datatable/filtering' = chapters.dashDataTable9$layout,
      '/datatable/reference' = chapters.dashDataTable10$layout,
      # Component Libraries (Dash DAQ Components)
      '/dash-daq' = chapters.dashDaq$layout,
      '/dash-daq/booleanswitch' = chapters.booleanswitch$layout,
      '/dash-daq/colorpicker' = chapters.colorpicker$layout,
      '/dash-daq/gauge' = chapters.gauge$layout,
      '/dash-daq/graduatedbar' = chapters.graduatedbar$layout,
      '/dash-daq/indicator' = chapters.indicator$layout,
      '/dash-daq/joystick' = chapters.joystick$layout,
      '/dash-daq/knob' = chapters.knob$layout,
      '/dash-daq/leddisplay' = chapters.leddisplay$layout,
      '/dash-daq/numericinput' = chapters.numericinput$layout,
      '/dash-daq/powerbutton' = chapters.powerbutton$layout,
      '/dash-daq/precisioninput' = chapters.precisioninput$layout,
      '/dash-daq/slider' = chapters.slider$layout,
      '/dash-daq/stopbutton' = chapters.stopbutton$layout,
      '/dash-daq/tank' = chapters.tank$layout,
      '/dash-daq/thermometer' = chapters.thermometer$layout,
      '/dash-daq/toggleswitch' = chapters.toggleswitch$layout,
      '/dash-daq/darkthemeprovider' = chapters.darkthemeprovider$layout,
      # Component Libraries (Dash Canvas)
      '/dash-canvas' = chapters.dashCanvas$layout,
      # Component Libraries (Dash Cytoscape)
      '/cytoscape' = chapters.dashCytoscape$layout,
      '/cytoscape/elements' = chapters.dashCytoscape1$layout,
      '/cytoscape/layout' = chapters.dashCytoscape2$layout,
      '/cytoscape/styling' = chapters.dashCytoscape3$layout,
      '/cytoscape/callbacks' = chapters.dashCytoscape4$layout,
      '/cytoscape/events' = chapters.dashCytoscape5$layout,
      '/cytoscape/phylogeny' = chapters.dashCytoscape6$layout,
      '/cytoscape/reference' = chapters.dashCytoscape7$layout,
      # Component Libraries (Dash Bio)
      "/dash-bio" = chapters.dashBio$layout,
      "/dash-bio/alignmentchart" = chapters.alignment$layout,
      "/dash-bio/circos" = chapters.circos$layout,
      "/dash-bio/clustergram" = chapters.clustergram$layout,
      "/dash-bio/ideogram" = chapters.ideogram$layout,
      "/dash-bio/manhattanplot" = chapters.manhattan$layout,
      "/dash-bio/molecule2dviewer" = chapters.molecule2dviewer$layout,
      "/dash-bio/molecule3dviewer" = chapters.molecule3dviewer$layout,
      "/dash-bio/volcanoplot" = chapters.volcanoplot$layout,
      "/dash-bio/needleplot" = chapters.needleplot$layout,
      "/dash-bio/oncoprint" = chapters.oncoprint$layout,
      "/dash-bio/sequenceviewer" = chapters.sequenceviewer$layout,
      "/dash-bio/speck" = chapters.speck$layout,
      # Production
      "/deployment" = chapters.deployment$layout,
      # Beyond the Basics
      '/external-resources' = chapters.external_resources$layout,
      '/urls' = chapters.urls$layout,
      '/devtools' = chapters.devtools$layout,
      '/support' = chapters.support$layout,
      '/plugins' = chapters.plugins$layout,
      '/d3-react-components' = chapters.d3$layout,
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
                href='/basic-callbacks',
                caption="Dash apps are made interactive through Dash Callbacks:
                R functions that are automatically called whenever an input component's property changes. Callbacks can be chained,
                allowing one update in the UI to trigger several updates across the app."
                ),
                components$Chapter(
                'Part 4. Interactive Graphing and Crossfiltering',
                href='/interactive-graphing',
                caption="Bind interactivity to the Dash `Graph` component whenever you hover, click, or
                select points on your chart."
                ),
                components$Chapter(
                'Part 5. Sharing Data Between Callbacks',
                href='/sharing-data-between-callbacks',
                caption="`global` variables will break your Dash apps.
                However, there are other ways to share data between callbacks.
                This chapter is useful for callbacks that run expensive data processing tasks or process large data."
                ),
                components$Chapter(
                'Part 6. FAQs and Gotchas',
                href='/faqs',
                caption="If you have read through the rest of the tutorial and still have questions
                or are encountering unexpected behaviour, this chapter may be useful."
                )
              )
            ),


            components$Section(
              'Dash Callbacks',
              list(
                components$Chapter(
                  'Basic Callbacks',
                  href='/basic-callbacks',
                  caption="Go through this introductory chapter to learn the foundations of the Dash callback."
                ),
                components$Chapter(
                  'Advanced Callbacks',
                  href='/advanced-callbacks',
                  caption="Now that you've gotten through the basics, take a look at other things you can do with
                  callbacks - from performance improvements to callback contexts."
                ),
                components$Chapter(
                  'Clientside Callbacks',
                  href='/clientside-callbacks',
                  caption="You might want to execute a callback in the frontend as opposed to the backend if you
                  want to avoid the extra time that it takes to make a roundtrip to the server. Clientside
                  callbacks allow you to write your callbacks in JavaScript that runs in the browser."
                ),
                components$Chapter(
                  'Callback Gotchas',
                  href='/callback-gotchas',
                  caption="Dash callbacks have some idiosyncracies that should be taken into consideration when
                  building a Dash app. If you're running into unexpected callback behavior, and the rest of the
                  documentation hasn't shed any light on the situation, try taking a look in this section."
                )
              )
            ),


            components$Section(
              'Open Source Component Libraries',
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
                caption="`dash_table.DataTable` is an interactive table that supports rich styling, conditional formatting, editing, sorting, filtering, and more."
                ),
                components$Chapter(
                  'Dash Bio Components',
                  href='/dash-bio',
                  caption="Dash Bio is a component library dedicated to visualizing bioinformatics data."
                ),
                components$Chapter(
                'Dash DAQ Components',
                href='/dash-daq',
                caption="Beautifully styled technical components for data acquisition, monitoring, and engineering applications."
                ),
                components$Chapter(
                'Dash Canvas',
                href='/dash-canvas',
                caption="Image rendering, drawing, annotations for image processing applications."
                ),
                components$Chapter(
                'Dash Cytoscape',
                href='/cytoscape',
                caption="Dash Cytoscape is our new network visualization component. It offers a declarative and
                user-friendly R interface to create beautiful, customizable, interactive and reactive graphs."
                ),
                components$Chapter(
                  'Dash Booststrap Components',
                  href='https://dash-bootstrap-components.opensource.faculty.ai/',
                  caption="A library of Bootstrap components created by [faculty.ai](https://faculty.ai/). Dash Boostrap Components makes it easier
                  to build consistently styled apps with complex, responsive layouts."
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
                href='https://plotly.com/dash/?_ga=2.180458663.1075922756.1562168385-916141078.1562168385'
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
    ),
    ''
    ))
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

plugin <- list(
  on_attach = function(server) {
    router <- server$plugins$request_routr
    route <- routr::Route$new()
    redirect_getting_started <- function(request, response, keys, ...) {
      response$status <- 301L
      response$set_header('Location', '/layout')
      TRUE
    }
    redirect_getting_started_2 <- function(request, response, keys, ...) {
      response$status <- 301L
      response$set_header('Location', '/basic-callbacks')
      TRUE
    }
    redirect_state <- function(request, response, keys, ...) {
      response$status <- 301L
      response$set_header('Location', '/basic-callbacks')
      TRUE
    }
    redirect_sizing <- function(request, response, keys, ...) {
      response$status <- 301L
      response$set_header('Location', '/datatable/width')
      TRUE
    }
    route$add_handler('get', '/getting-started', redirect_getting_started)
    route$add_handler('get', '/getting-started-part-2', redirect_getting_started_2)
    route$add_handler('get', '/state', redirect_state)
    route$add_handler('get', '/datatable/sizing', redirect_sizing)
    router$add_route(route, "redirects")
  },
  name = 'redirect_urls',
  require = 'request_routr'
)

app$server$attach(plugin)

app$run_server(host = "0.0.0.0")
