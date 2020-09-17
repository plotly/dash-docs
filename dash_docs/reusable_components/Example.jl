using DashHtmlComponents

function Example(example::String)
    return html_div(
        example,
        className = "example-container"
    )
end
