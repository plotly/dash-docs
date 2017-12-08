import dash_html_components as html
import dash_core_components as dcc


layout = html.Div(className='gallery', children=[

    dcc.Markdown('''

    # Dash Gallery

    ***

    ## Getting Started Example

    The [Dash Getting Started Guide](/dash/getting-started) contains
    many applications that range in complexity.

    The first interactive app that you'll create combines a `Slider`
    with a `Graph` and filters data using a Pandas `DataFrame`.
    The `animate` property in the `Graph` component was set to `True`
    so that the points transition smoothly.
    Some interactivity is built-in to the `Graph` component including
    hovering over values, clicking on legend items to toggle traces, and
    zooming into regions.

    '''.replace('    ', '')),

    html.A(
        className='image-link',
        href='https://plot.ly/dash/getting-started',
        children=html.Img(
            src='https://github.com/plotly/dash-docs/raw/master/images/gapminder-animation.gif',
            alt='Screenshot of simple Dash app'
        )
    ),

    dcc.Markdown('''
    [View the getting started guide](https://plot.ly/dash/getting-started)

    ***

    ## Oil and Gas Explorer

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

    html.A(
        className='image-link',
        href='https://plot.ly/dash/gallery/new-york-oil-and-gas',
        children=html.Img(
            src='https://github.com/plotly/dash-docs/raw/master/images/oil-and-gas.gif',
            alt='Screenshot of an oil and gas Dash app'
        )
    ),

    dcc.Markdown('''

    [View the app](/dash/gallery/new-york-oil-and-gas) | [View the source code](https://github.com/plotly/dash-oil-and-gas-demo)

    ***

    ## Goldman Sachs Remake: Portfolio Report

    This app recreates the look and feel of a Goldman Sachs report.
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

    html.A(
        className='image-link',
        href='https://plot.ly/dash/gallery/goldman-sachs-report',
        children=html.Img(
            src='https://github.com/plotly/dash-docs/raw/master/images/goldman-sachs.png',
            alt='Screenshot of Goldman Sachs report'
        )
    ),

    dcc.Markdown('''

    [View the app](/dash/gallery/goldman-sachs-report) | [View the source code](https://github.com/plotly/dash-goldman-sachs-report-demo)

    ***

    ## Uber Rides

    This app displays all of the Uber rides in New York City in 2014.
    The original datafile is almost 500MB large and all of the filtering is
    done in memory with Pandas. Buttons on the chart itself highlight
    different regions in the city.
    '''.replace('    ', '')),

    html.A(
        className='image-link',
        href='https://plot.ly/dash/gallery/uber-rides',
        children=html.Img(
            src='https://github.com/plotly/dash-docs/raw/master/images/uber-rides.gif',
            alt='Screenshot of an Uber rides Dash app'
        )
    ),

    dcc.Markdown('''

    [View the app](https://plot.ly/dash/gallery/uber-rides) | [View the source code](https://github.com/plotly/dash-uber-rides-demo)

    ***

    ## Dash DataTable

    Dash is currently incubating an interactive table component that provides
    built-in filtering, row-selection, editing, and sorting.
    Prototypes of this component are being developed in the
    [`dash-table-experiments`](https://github.com/plotly/dash-table-experiments)
    repository. Join the discussion in the
    [Dash Community Forum](https://community.plot.ly/t/display-tables-in-dash/4707/38).

    This example was written in ~100 lines of code.

    '''.replace('    ', '')),

    html.A(
        className='image-link',
        href='https://github.com/plotly/dash-table-experiments',
        children=html.Img(
            src='https://github.com/plotly/dash-table-experiments/raw/master/images/DataTable.gif',
            alt='Example of a Dash Interactive Table'
        )
    ),

    dcc.Markdown('''

    [View the Dash Table Experiments Project](https://github.com/plotly/dash-table-experiments) | [Join the discussion](https://community.plot.ly/t/display-tables-in-dash/4707/38)

    ***

    ## Simple Stock Tickers App

    This app queries data from Google Finance and displays the results as candlestick
    charts. Dash comes with several financial chart types including candlestick
    charts, OHLC graphs, time series, and range sliders.

    This app was written in just around 100 lines of code.

    '''.replace('    ', '')),

    html.A(
        className='image-link',
        href='https://plot.ly/dash/gallery/stock-tickers',
        children=html.Img(
            src='https://github.com/plotly/dash-docs/raw/master/images/stock-tickers.png',
            alt='Screenshot of a stock tickers Dash app'
        )
    ),

    dcc.Markdown('''

    [View the app](https://plot.ly/dash/gallery/stock-tickers) | [View the source code](https://github.com/plotly/dash-stock-tickers-demo-app)


    ***

    ## Volatility Surface Explorer

    This demo fetches CBOE options chain data from Yahoo Finance with Pandas Datareader
    and calculates the implied volatility of each option using the [`py_vollib`](https://github.com/vollib/py_vollib)
    library.

    All parameters of the IV calculation are adjustable and the
    resulting volatility curve is rendered using a [Mesh 3D chart](https://plot.ly/python/3d-mesh/)
    with several subplots showing subsections of the 3D plot.

    Initially fetching the options data and calculating the IV might take a
    few seconds due to the scale of the calculations required.

    '''.replace('    ', '')),

    html.A(
        className='image-link',
        href='https://plot.ly/dash/gallery/volatility-surface',
        children=html.Img(
            src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-volatility-surface.gif',
            alt='Screenshot of volatility surface'
        )
    ),

    dcc.Markdown('''
    [View the app](https://plot.ly/dash/gallery/volatility-surface) | [View the source code](https://github.com/plotly/dash-volatility-surface)

    ***

    ## Drug Discovery App

    This app displays a description of the drug as you hover over points in the
    graph.

    Selecting drugs in the dropdown highlights their position in the chart and
    appends their symbol in the table below.

    Built in a few hundred lines of Python code.

    '''.replace('    ', '')),

    html.A(
        className='image-link',
        href='https://plot.ly/dash/gallery/drug-explorer',
        children=html.Img(
            src='https://github.com/plotly/dash-docs/raw/master/images/drug-discovery-app.gif',
            alt='Screenshot of a drug discovery Dash app'
        )
    ),

    dcc.Markdown('''
    [View the app](https://plot.ly/dash/gallery/drug-explorer) | [View the source code](https://github.com/plotly/dash-drug-discovery-demo/)

    ***

    ## Live Wind Streaming

    This app continually queries a SQL database and displays live charts of
    wind speed and wind direction. In Dash, the [dcc.Interval](https://plot.ly/dash/live-upates)
    component can be used to update any element on a recurring interval.

    '''.replace('    ', '')),

    html.A(
        className='image-link',
        href='https://plot.ly/dash/gallery/live-wind-data',
        children=html.Img(
            src='https://cdn.rawgit.com/plotly/dash-wind-streaming/d84b15eebf2c502372740416d445e8e3f23d0619/Gif/dash-wind-streaming.gif',
            alt='gif of a wind streaming Dash app'
        )
    ),

    dcc.Markdown('''
    [View the app](https://plot.ly/dash/gallery/live-wind-data) | [View the source code](https://github.com/plotly/dash-wind-streaming)


    ***

    ## NYTimes Remake: Recession in 255 Charts

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

    html.A(
        className='image-link',
        href='https://plot.ly/dash/gallery/recession-report',
        children=html.Img(
            src='https://github.com/plotly/dash-docs/raw/master/images/nytimes.png',
            alt='Screenshot of a recession reports'
        )
    ),

    dcc.Markdown('''

    [View the app](https://plot.ly/dash/gallery/recession-report) | [View the source code](https://github.com/plotly/dash-recession-report-demo)


    ***

    ## NYTimes Remake: Yield Curve

    This Dash app adapts the excellent NY Times
    report [A 3-D View of a Chart That Predicts The Economic Future: The Yield Curve](https://www.nytimes.com/interactive/2015/03/19/upshot/3d-yield-curve-economic-growth.html).


    Dash comes with a wide range of interactive 3D chart types,
    such as 3D scatter plots, surface plots, network graphs and ribbon plots.
    [View more 3D chart examples](https://plot.ly/python/3d-charts/).


    '''.replace('    ', '')),

    html.A(
        className='image-link',
        href='https://plot.ly/dash/gallery/yield-curve',
        children=html.Img(
            src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-yield-curve-app.png',
            alt='Screenshot of a dash home page'
        )
    ),
    dcc.Markdown('''

    [View the app](https://plot.ly/dash/gallery/yield-curve) | [View the source code](https://github.com/plotly/dash-yield-curve)


    ***

    ## Dash Documentation

    These Dash docs that you're looking at? They are itself a Dash app!

    '''.replace('    ', '')),

    html.A(
        className='image-link',
        href='https://plot.ly/dash/',
        children=html.Img(
            src='https://github.com/plotly/dash-docs/raw/master/images/dash-home-page.png',
            alt='Screenshot of a dash home page'
        )
    ),
    dcc.Markdown('''


    [View Dash User Guide source code](https://github.com/plotly/dash-docs)

    '''.replace('    ', '')),

])
