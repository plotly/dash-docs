# AUTO GENERATED FILE - DO NOT EDIT

Sidebar <- function(id=NULL, urls=NULL, depth=NULL) {

    props <- list(id=id, urls=urls, depth=depth)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Sidebar',
        namespace = 'dash_user_guide_components',
        propNames = c('id', 'urls', 'depth'),
        package = 'dashUserGuideComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
