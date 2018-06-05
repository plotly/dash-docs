# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_core_components as dcc

layout = html.Div(className='gallery', children=[

    # Getting Started Section
    dcc.Markdown('''

    # Dash Gallery

    ***

    ## Getting Started
    '''.replace('    ', '')),

    html.Div(className="row", children=[
        html.Div(className="columns", children=[
            html.A(
                className='image-link',
                href='https://dash.plot.ly/getting-started',
                children=html.Img(
                    src='https://github.com/plotly/dash-docs/raw/master/images/gapminder-animation.gif',
                    alt='Screenshot of simple Dash app'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [View the getting started guide](https://dash.plot.ly/getting-started)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
            
            The [Dash Getting Started Guide](/getting-started) contains
            many applications that range in complexity.
        
            The first interactive app that you'll create combines a `Slider`
            with a `Graph` and filters data using a Pandas `DataFrame`.
            The `animate` property in the `Graph` component was set to `True`
            so that the points transition smoothly.
            Some interactivity is built-in to the `Graph` component including
            hovering over values, clicking on legend items to toggle traces, and
            zooming into regions.
        
            '''.replace('    ', '')),
        ]),
    ]),
    ####################################################################################################################
    # FINANCE SECTION
    dcc.Markdown('''    
    ***

    ## Finance
    '''.replace('    ', '')),

    html.Div(className="row", children=[
        html.Div(className="six columns", children=[
            # Stock Tickers
            html.A(
                className='image-link',
                href='https://dash-stock-tickers.plot.ly',
                children=html.Img(
                    src='https://github.com/plotly/dash-docs/raw/master/images/stock-tickers.png',
                    alt='Screenshot of a stock tickers Dash app'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [Stock Tickers](https://dash-stock-tickers.plot.ly) | [Source code](https://github.com/plotly/dash-stock-tickers-demo-app)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
        
            This app queries data from Google Finance and displays the results as candlestick
            charts. Dash comes with several financial chart types including candlestick
            charts, OHLC graphs, time series, and range sliders.
        
            This app was written in just around 100 lines of code.
        
            '''.replace('    ', ''))
        ]),

        html.Div(className="six columns", children=[
            # Vanguard Report
            html.A(
                className='image-link',
                href='https://vanguard-report.herokuapp.com/',
                children=html.Img(
                    src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/vanguard.gif',
                    alt='Screenshot of vanguard report'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [Financial Report](https://vanguard-report.herokuapp.com/) | [Source code](https://github.com/plotly/dash-vanguard-report)
                
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
            This app recreates the look and feel of a Vanguard report.
            It includes a Print to PDF button and the styles were optimized
            to look good on the web and in PDF form.
        
            The charts in the report on the web version are interactive.
            You can hover over points to see their values and zoom into
            regions. Since this report was built on top of Dash, you could
            adapt this report to include even more interactive elements, like
            a dropdown or a search box.
        
            With PDF styles, you can hide and show elements depending on whether
            the app is being viewed in the web browser or in print, using the
            same framework for the rich interactive applications as the static
            PDF reports.
        
            '''.replace('    ', '')),
        ]),
    ]),

    html.Div(className="row", children=[
        html.Div(className="six columns", children=[
            # Yield Curve
            html.A(
                className='image-link',
                href='https://dash-yield-curve.plot.ly',
                children=html.Img(
                    src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-yield-curve-app.png',
                    alt='Screenshot of a dash home page'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [3D Yield Curve](https://dash-yield-curve.plot.ly) | [Source code](https://github.com/plotly/dash-yield-curve)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
        
            This Dash app adapts the excellent NY Times
            report [A 3-D View of a Chart That Predicts The Economic Future: The Yield Curve](https://www.nytimes.com/interactive/2015/03/19/upshot/3d-yield-curve-economic-growth.html).

            Dash comes with a wide range of interactive 3D chart types,
            such as 3D scatter plots, surface plots, network graphs and ribbon plots.
            [View more 3D chart examples](https://plot.ly/python/3d-charts/).
        
        
            '''.replace('    ', ''))
        ]),

        html.Div(className="six columns", children=[
            # Recession Report
            html.A(
                className='image-link',
                href='https://dash-recession-report.plot.ly',
                children=html.Img(
                    src='https://github.com/plotly/dash-docs/raw/master/images/nytimes.png',
                    alt='Screenshot of a recession reports'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [Recession in 255 Charts](https://dash-recession-report.plot.ly) | [View the source code](https://github.com/plotly/dash-recession-report-demo)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
        
            485 lines of Python code, including text copy.
        
            This Dash app was adapted from NYTimes's excellent
            [How the Recession Reshaped the Economy in 255 Charts](https://www.nytimes.com/interactive/2014/06/05/upshot/how-the-recession-reshaped-the-economy-in-255-charts.html).
        
            This Dash app displays its content linearly, like an
            interactive report. The report highlights several notable
            views of the data and then invites the user to highlight
            their own regions at the end. This method of highlighting
            views is a great strategy for walking your readers through
            your complex analysis.
        
            The height of the charts was specified in viewport units (`vh`),
            scaling the size of the chart to the height of the screen. It
            looks great on monitors big and small.
        
            The text in the application is centered and its width is restricted
            to improve the reading experience. The graphs are full bleed:
            the extend past the narrow column of text the edges of page.
        
            '''.replace('    ', '')),
        ]),
    ]),
    ####################################################################################################################
    # ENERGY AND TRANSPORT SECTION
    html.Div([
        dcc.Markdown('''
        
        ***
        
        ## Energy and Transportation
        
        '''.replace('    ', '')),
    ]),

    html.Div(className="row", children=[
        html.Div(className="six columns", children=[
            html.A(
                className='image-link',
                href='https://dash-oil-and-gas.plot.ly',
                children=html.Img(
                    src='https://github.com/plotly/dash-docs/raw/master/images/oil-and-gas.gif',
                    alt='Screenshot of an oil and gas Dash app'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [Natural gas well production](https://dash-oil-and-gas.plot.ly) | [Source code](https://github.com/plotly/dash-oil-and-gas-demo)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
            
            This Dash app displays well data from New York State. As you hover over
            values in the map, a time series is displayed showing production values
            over time. As you change the years in the range slider, the aggregate
            time series is updated with the sum of all production over time.
            The histogram chart is also selectable, serving as an alternative
            control for selecting a range of time.
            
            This application is also mobile-friendly. Dash apps are built and
            published in the Web, so the full power of CSS is available.
            The Dash core team maintains a [core style guide here](https://codepen.io/chriddyp/pen/bWLwgP)
            that  includes a responsive 12 column grid.
            
            '''.replace('    ', '')),
        ]),

        html.Div(className="six columns", children=[
            html.A(
                className='image-link',
                href='https://dash-uber-rides.plot.ly',
                children=html.Img(
                    src='https://github.com/plotly/dash-docs/raw/master/images/uber-rides.gif',
                    alt='Screenshot of an Uber rides Dash app'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [NYC Uber rides](https://dash-uber-rides.plot.ly) | [Source code](https://github.com/plotly/dash-uber-rides-demo)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
            
            This app displays all of the Uber rides in New York City in 2014.
            The original datafile is almost 500MB large and all of the filtering is
            done in memory with Pandas. Buttons on the chart itself highlight
            different regions in the city.
            '''.replace('    ', '')),
        ]),
    ]),
    ####################################################################################################################
    # LIFE SCIENCES SECTION
    dcc.Markdown('''
    
    ***

    ## Life sciences
    
    '''.replace('    ', '')),

    html.Div(className="row", children=[
        html.Div(className="six columns", children=[
            html.A(
                className='image-link',
                href='https://dash-drug-explorer.plot.ly',
                children=html.Img(
                    src='https://github.com/plotly/dash-docs/raw/master/images/drug-discovery-app.gif',
                    alt='Screenshot of a drug discovery Dash app'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [Drug precursors](https://dash-drug-explorer.plot.ly) | [Source code](https://github.com/plotly/dash-drug-discovery-demo/)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
        
            This app displays a description of the drug as you hover over points in the
            graph.
        
            Selecting drugs in the dropdown highlights their position in the chart and
            appends their symbol in the table below.
        
            Built in a few hundred lines of Python code.
        
            '''.replace('    ', '')),
        ]),

        html.Div(className="six columns", children=[
            html.A(
                className='image-link',
                href='http://brain-surface-viewer.herokuapp.com/',
                children=html.Img(
                    src='https://raw.githubusercontent.com/plotly/dash-brain-surface-viewer/master/ZOMBIE_BRAIN.png',
                    alt='Screenshot of brain surface viewer'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [MRI reconstruction](http://brain-surface-viewer.herokuapp.com/) | [Source code](https://github.com/plotly/dash-brain-surface-viewer)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
            
            🐭 Explore human and mice brains in 3d.
            
            Add interactive labels to points on the brain surface and change the surface colorscale.
            
            '''.replace('    ', '')),
        ]),
    ]),
    ####################################################################################################################
    # GOVERNMENT AND PUBLIC HEALTH

    dcc.Markdown('''
        
    ***
    
    ## Government & Public Health
    
    '''.replace('    ', '')),

    html.Div(className="row", children=[
        html.Div(className="columns", children=[
            html.A(
                className='image-link',
                href='https://opioid-epidemic.herokuapp.com/',
                children=html.Img(
                    src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/opioid-epidemic.png',
                    alt='Screenshot of opioid epidemic'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [US Opioid Epidemic](https://opioid-epidemic.herokuapp.com/) | [Source code](https://github.com/plotly/dash-opioid-epidemic-demo)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
            
            Interactively explore the effect of the opioid epidemic in North America.
            
            '''.replace('    ', '')),
        ]),
    ]),
    ####################################################################################################################
    # MACHINE LEARNING AND COMPUTER VISION
    dcc.Markdown('''
    
    ***
    
    ## Machine Learning & Computer Vision
    
    '''.replace('    ', '')),

    html.Div(className="row", children=[
        html.Div(className="six columns", children=[
            html.A(
                className='image-link',
                href='https://github.com/plotly/dash-object-detection',
                children=html.Img(
                    src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-object-detection-app.png',
                    alt='Link to Object Detection App'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
            [Object Detection App](https://dash-object-detection.plot.ly/)| [Source Code](https://github.com/plotly/dash-object-detection)
            '''.replace('    ', '')
            ),

            dcc.Markdown('''
            
            For every Deep Learning models, keeping track of accuracy and loss is an essential part of the training 
            process, since they indicate how good your models are. This app is a real-time visualization app that 
            monitors core metrics of your Tensorflow graphs during the training, so that you can quickly detect 
            anomalies within your model.
    
            '''.replace('    ', '')),
        ]),

        html.Div(className="six columns", children=[
            html.A(
                className='image-link',
                href='https://github.com/plotly/dash-live-model-training',
                children=html.Img(
                    src="https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-live-model-training-viewer.png",
                    alt='Link to Live Model Training Viewer'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
            [Live Model Training Viewer](https://dash-live-model-training.plot.ly/)| [Source Code](https://github.com/plotly/dash-live-model-training)
            '''.replace('    ', '')
            ),

            dcc.Markdown('''
            
            This app provides useful visualizations about what’s happening inside a complex video (e.g. object presence 
            heatmaps, object count pie charts), rendering the data generated by the video more insightful. The data in
            the demo is generated using MobileNet v1, trained on the COCO dataset.

            '''.replace('    ', ''))
        ]),
    ]),

    ####################################################################################################################
    # LIVE UPDATES SECTION
    dcc.Markdown('''    
    
    ***
    
    ## Live Updates
    
    '''.replace('    ', '')),

    html.Div(className="row", children=[
        html.Div(className="columns", children=[
            html.A(
                className='image-link',
                href='https://dash-live-wind-data.plot.ly',
                children=html.Img(
                    src='https://cdn.rawgit.com/plotly/dash-wind-streaming/d84b15eebf2c502372740416d445e8e3f23d0619/Gif/dash-wind-streaming.gif',
                    alt='gif of a wind streaming Dash app'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [Window speed measurement](https://dash-live-wind-data.plot.ly) | [Source code](https://github.com/plotly/dash-wind-streaming)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
            
            This app continually queries a SQL database and displays live charts of
            wind speed and wind direction. In Dash, the [dcc.Interval](https://dash.plot.ly/live-upates)
            component can be used to update any element on a recurring interval.
        
            '''.replace('    ', '')),
        ]),
    ]),

    ####################################################################################################################
    # COMPONENT LIBRARIES SECTION

    dcc.Markdown('''

    ***
    
    ## Component Libraries
    
    '''.replace('    ', '')),

    html.Div(className="row", children=[
        html.Div(className="six columns", children=[
            html.A(
                className='image-link',
                href='https://github.com/plotly/dash-table-experiments',
                children=html.Img(
                    src='https://github.com/plotly/dash-table-experiments/raw/master/images/DataTable.gif',
                    alt='Example of a Dash Interactive Table'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [Join the discussion](https://community.plot.ly/t/display-tables-in-dash/4707/38)| [Source Code](https://github.com/plotly/dash-table-experiments)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
        
            Dash is currently incubating an interactive table component that provides
            built-in filtering, row-selection, editing, and sorting.
            Prototypes of this component are being developed in the
            [`dash-table-experiments`](https://github.com/plotly/dash-table-experiments)
            repository. Join the discussion in the
            [Dash Community Forum](https://community.plot.ly/t/display-tables-in-dash/4707/38).
        
            This example was written in ~100 lines of code. 
        
            '''.replace('    ', '')),
        ]),

        html.Div(className="six columns", children=[
            html.A(
                className='image-link',
                href='https://dash.plot.ly/dash-core-components',
                children=html.Img(
                    src="https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-core-components.png",
                    alt='Link to Dash Core Components'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [Dash Core Components](https://dash.plot.ly/dash-core-components)| [Source Code](https://github.com/plotly/dash-core-components)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
            Dash comes with a set of rich components like sliders, dropdowns, graphs, and more. 
            [View the official Dash documentation to learn more](https://dash.plot.ly/dash-core-components).
            '''.replace('    ', ''))
        ]),
    ]),

    html.Div(className="row", children=[
        html.Div(className="six columns", children=[
            html.A(
                className='image-link',
                href='https://community.plot.ly/t/show-and-tell-community-thread/7554',
                children=html.Img(
                    src="https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-community-components.png",
                    alt='Link to Dash Core Components'
                )
            ),

            dcc.Markdown(
                className="markdown-links",
                children='''
                [Dash Community Components](https://community.plot.ly/t/show-and-tell-community-thread/7554)
                '''.replace('    ', '')
            ),

            dcc.Markdown('''
            Dash has a [plugin system](https://dash.plot.ly/plugins) for integrating your own React.js components. 
            The Dash community has built many of their component libraries, like 
            [Video Components](https://community.plot.ly/t/modifying-a-dom-property-in-html-video/7649/11) 
            and [Large File Upload](https://community.plot.ly/t/show-and-tell-dash-resumable-upload/9519). 
            View more community maintained components and other projects in the Dash Community Forum’s 
            [Show and Tell Thread](https://community.plot.ly/t/show-and-tell-community-thread/7554)
            '''.replace('    ', ''))
        ]),
    ]),

    ####################################################################################################################
    # DASH DOC SECTION
    html.Div(className="row", children=[
        dcc.Markdown('''
        
        ***
    
        ## Dash Documentation
    
        These Dash docs that you're looking at? They are itself a Dash app!
    
        '''.replace('    ', '')),

        html.A(
            className='image-link',
            href='https://dash.plot.ly/',
            children=html.Img(
                src='https://github.com/plotly/dash-docs/raw/master/images/dash-home-page.png',
                alt='Screenshot of a dash home page'
            )
        ),

        dcc.Markdown(
            className="markdown-links",
            children='''
            [View Dash User Guide source code](https://github.com/plotly/dash-docs)
            '''.replace('    ', '')
        ),
    ]),
])
