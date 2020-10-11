include("app.jl")

using Dash, DashCoreComponents, DashHtmlComponents, Match

# Load Chapter, Example, Header, Section, Syntax components
map(include, filter(x->occursin(r".jl$", x), readdir("dash_docs/reusable_components/", join=true)))

include("dash_docs/chapters/whats_dash/introduction.jl")
include("dash_docs/chapters/installation/index.jl")
include("dash_docs/chapters/getting_started/index.jl")
include("dash_docs/chapters/basic_callbacks/index.jl")
include("dash_docs/chapters/graph_crossfiltering/index.jl")

header = html_div() do 
    className = "header",
    html_div(
        style = Dict("height" => "95%"),
        className = "container-width",
        children = (
            html_a(
                html_img(
                    style = Dict("height" => "100%"),
                    src = "https://plotly.com/products/dash"
                ),
                href = "https://plotly.com/products/dash",
                className = "logo-link"
            ),
            html_div(
                className = "links",
                children = (
                    html_a("pricing", className = "link", href = "https://plotly.com/dash"),
                    html_a("user guide", className = "link", href = "/"),
                    html_a("plotly", className = "link", href = "https://plotly.com")
                )
            )
        )
    )
end;

app.layout = html_div() do 
    html_div(id = "wait-for-layout")
    dcc_location(id = "url", refresh=false)
    header
    html_div(
        className = "content-wrapper",
        children = (
            html_div(
                (
                    html_div(id = "backlinks-top", className = "backlinks"),
                    html_div(
                        html_div(id = "chapter", className = "content"),
                        className = "content-container"
                    ),
                    html_div(id = "backlinks-bottom", className = "backlinks")
                ),
                className = "rhs-content container-width"
            )
        # dugcPageMenu will go here
        )
    )
end

callback!(app,
    Output("chapter", "children"),
    #Output("pagemenu", "dummy2")
    Input("url", "pathname")) do pathname
        return @match pathname begin
            "/introduction" => chapters_whats_dash.app.layout
            "/installation" => chapters_installation.app.layout
            "/layout" => chapters_getting_started.app.layout
            "/basic-callbacks" => chapters_callbacks.app.layout
            "/interactive-graphing" => chapters_interactive_graphing.app.layout
            "/sharing-data-between-callbacks" => chapters_sharing_data.app.layout
            _ => html_div() do 
                html_h1("Dash for Julia User Guide")
                Section(
                    "What's Dash?",
                    (
                        Chapter(
                            "Introduction",
                            "/introduction",
                            "A quick paragraph about Dash and a link to the talk at Plotcon that started it all."
                        ),
                        Chapter(
                            "Announcement Essay",
                            "https://medium.com/plotly/dash-is-react-for-python-r-and-julia-c75822d1cc24",
                            "Our extended essay on Dash. An extended discussion of Dash's architecture and our motivation behind the project."
                        ),
                        Chapter(
                            "Dash App Gallery",
                            "https://dash.plotly.com/gallery",
                            "A glimpse into what's possible with Dash."
                        ),
                        Chapter(
                            "Dash Club",
                            "https://plot.us12.list-manage.com/subscribe?u=28d7f8f0685d044fb51f0d4ee&id=0c1cb734d7",
                            "A fortnightly email newsletter by chriddyp, the creator of Dash."
                        )
                    )
                )
                Section(
                "Dash Tutorial",
                (
                    Chapter(
                        "Part 1. Installation",
                        "/installation",
                        "A quick paragraph about Dash and a link to the talk at Plotcon that started it all."
                    ),
                    Chapter(
                        "Part 2. The Dash Layout",
                        "/getting-started",
                        "The Dash `layout` describes what your app will look like and is composed of a set of declarative Dash components."
                    ),
                    Chapter(
                        "Part 3. Basic Callbacks",
                        "/basic-callbacks",
                        "Dash apps are made interactive through Dash Callbacks:
                        R functions that are automatically called whenever an input component's property changes. Callbacks can be chained,
                        allowing one update in the UI to trigger several updates across the app."
                    ),
                    Chapter(
                        "Part 4. Interactive Graphing and Crossfiltering",
                        "/interactive-graphing",
                        "Bind interactivity to the Dash `Graph` component whenever you hover, click, or
                        select points on your chart."
                    ),
                    Chapter(
                        "Part 6. FAQs and Gotchas",
                        "/faqs",
                        "If you have read through the rest of the tutorial and still have questions
                        or are encountering unexpected behaviour, this chapter may be useful."
                        )
                    )
                )
            end
        end
end

run_server(app)
