if environ("DASH_APP_LOCATION") != "ABSOLUTE"
    import .server.app
else
    import server.app
end

@doc """
This is a helper function which returns an empty string if
an environment variable corresponding to `var` cannot be found,
or the value of this variable when it exists.
"""
function environ(var)
  if var in keys(ENV)
    return ENV[var]
  else
    return ""
  end
end

@doc """
This function simplifies prepending relative paths
with (optional) paths derived from the `DASH_DOCS_URL_PREFIX`
environment variable. In Dash Enterprise, the help content is
typically hosted within `/Docs`, so `relpath("/somepath")`
would return "/Docs/somepath".
"""ex
function dash_relpath(path)
    if startswith(path, "/") && "DASH_DOCS_URL_PREFIX" in keys(ENV) && !startswith(path, string("/", strip(environ("DASH_DOCS_URL_PREFIX"), ['/'])))
        # In enterprise docs, all assets are under `/Docs` 
        return string(rstrip(environ("DASH_DOCS_URL_PREFIX"), ['/']), path)
    end
    return path
end

@doc """
This is a helper function which catches errors, and prints a
useful console message describing the path of the file containing
the code which threw the error. The original error is then
rethrown. Julia offers macros, which are more powerful than
Python's decorators, but here we can just wrap a function by
prepending `exception_handler`, and appending the arguments, e.g.
`exception_handler(load_example)("/somepath", true)`
"""
function exception_handler(func)
    function wrapper(path, kwargs...)
        try
            return(func(path, kwargs...))
        catch e
            println(string("\nError running ", path, "\n", '='^76))
            rethrow()
        end
    end
    return wrapper
end

@doc """
`load_examples` is a helper function for assembling an
array of examples which are referenced in the page
rendered from `index_filename`. It works in concert with
`load_example` below.
"""
function load_examples(index_filename, omit = [])
    dir = dirname(relpath(index_filename))
    example_dir = joinpath(dir, "examples")
    try
        example_filenames = readdir(example_dir)
    catch
        return []
    end

    examples = []
    for filename in example_filenames
        full_filename = joinpath(example_dir, filename)
        if !(filename in omit) && isfile(full_filename) && endswith(filename, ".py")
            push!(examples, load_example(full_filename))
        end
    end
    return examples
end

function load_example(path, relative_path=false)
    if relative_path
        thispath = @__DIR__
        # in Julia, if path is absolute, it will omit
        # thispath in the statement below, so should
        # probably use lstrip to avoid this behaviour
        path = joinpath(thispath, lstrip(path, ['/']))
    end
    open(path) do file
        _source = read(file, string)
        _example = _source

        if !occursin("app = dash()", _example) && !occursin("app = CustomDash()", _example)
            throw("Didn't declare app")
        end

        _example = replace(_example, r"app = dash()" => "# app = dash()")

        commented_configs = [
            "app.scripts.config.serve_locally"
            "app.css.config.serve_locally"
        ]

        for config in commented_configs
            _example = replace(_example, Regex("# " * config))
        end

        if !occursin("using Dash\n", _example)
            throw("Didn't import dash")
        end
        
        if !occursin("app.layout = ", _example)
            throw("app.layout not assigned")
        end

        _example = replace(_example, r"app.layout =" => "layout =")

        if !occursin(r"run_server\(.*?\)", _example)
            throw("run_server(app) missing")
        end
        
        if occursin(r"$tools", _example)
            _example = replace(_example, r"$tools" => dirname(@__FILE__))
        end

        # replace remote datasets with local ones
        # so that the app can run in internet-less environments
        find_and_replace = Dict(
            "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"=>
            "datasets/gapminderDataFiveYear.csv",

            "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"=>
            "datasets/gapminder2007.csv",

            "https://raw.githubusercontent.com/plotly/datasets/master/solar.csv"=>
            "datasets/solar.csv",

            "https://raw.githubusercontent.com/plotly/datasets/master/Emissions%20Data.csv"=>
            "datasets/Emissions%20Data.csv",

            "https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv"=>
            "datasets/1962_2006_walmart_store_openings.csv",

            "https://upload.wikimedia.org/wikipedia/commons/e/e4/Mitochondria%2C_mammalian_lung_-_TEM_%282%29.jpg"=>
            "datasets/mitochondria.jpg",

            "https://gist.githubusercontent.com/chriddyp/cb5392c35661370d95f300086accea51/raw/8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/indicators.csv"=>
            "datasets/indicators.csv",

            "https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv"=>
            "datasets/usa-agricultural-exports-2011.csv",

            "https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv"=>
            "datasets/gdp-life-exp-2007.csv",

            "https://plotly.github.io/datasets/country_indicators.csv"=>
            "datasets/country_indicators.csv",

            "https://github.com/plotly/datasets/raw/master/26k-consumer-complaints.csv"=>
            "datasets/26k-consumer-complaints.csv",

            "https://js.cytoscape.org/demos/colajs-graph/data.json"=>
            "datasets/colajs-graph-data.json",

            "https://js.cytoscape.org/demos/colajs-graph/cy-style.json"=>
            "datasets/colajs-graph-cy-style.json",

            "https://www.publicdomainpictures.net/pictures/60000/nahled/flower-outline-coloring-page.jpg"=>
            dash_relpath("/assets/images/gallery/flower-outline-coloring-page.jpg"),

            "https://raw.githubusercontent.com/plotly/datasets/master/mitochondria.jpg"=>
            dash_relpath("/assets/images/gallery/mitochondria.jpg")
        )
        
        for key in find_and_replace
            if occursin(key, _example)
                _example = replace(_example, Regex("# " * config) => find_and_replace[key])
            end
        end

        try
            include_string(app, _example)
        catch e
            print(_example)
            rethrow()
        end

        return(
            string("```python \n", _source, "```")
        )
    end
end
