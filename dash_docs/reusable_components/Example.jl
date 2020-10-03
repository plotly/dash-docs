using DashHtmlComponents

function Example(example::Component)
    return html_div(
        example,
        className = "example-container"
    )
end
