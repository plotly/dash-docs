source('dash_docs/styles.R')

# Added Reusable Components

Header <- function(title) {
  return (
    htmlDiv(
      htmlH2(
        title,
        style = list('borderBottom' = 'thin lightgrey solid', 'marginRight' = 20)
      )
    )
  )
}

Chapter <- function(name, href = NA, caption = NA) {
  divTitle <- htmlA(
    name,
    href = href,
    id = href,
    className = 'toc--chapter-link'
  )
  divCaption <- htmlSmall(
    className = 'toc--chapter-content',
    children = dccMarkdown(caption),
    style = list('display' = 'block', 'marginTop' = '3px')
  )
  if (!is.na(caption)) {
    return (
      htmlDiv(
        className = 'toc--chapter',
        style = list('marginTop' = '10px'),
        children = list(divTitle, divCaption)
      )
    )
  } else {
    return (
      htmlDiv(
        className = 'toc--chapter',
        style = list('marginTop' = '10px'),
        children = list(divTitle)
      )
    )
  }
}

Section <- function(title, links, description = NA, headerStyle = list()) {
  #ifelse(is.na(description), )
  return(
    htmlDiv(
      className = 'toc--section',
      children = list(
        htmlH2(
          title,
          style = c(list('borderBottom' = 'thin lightgrey solid', 'marginTop' = 50), headerStyle)
        ),
        htmlDiv(description),
        htmlUl(
          links,
          className = 'toc--chapters'
        )
      )
    )
  )
}

# Existing Components (may need to edit)

Syntax <- function(children, language = 'R', style = styles$code_container, summary = ''){
  if (!(summary == '')) {
    return(
      htmlDetails(
        list(
          htmlSummary(summary),
          htmlDiv(children)
        ),
        open=TRUE
      )
    )
  } else {
    return(
      dccSyntaxHighlighter(
        children,
        'language' = language,
        'customStyle' = style
      )
    )
  }
}

Example <- function(example){
  return(
    htmlDiv(
      example,
      className = 'example-container'
    )
  )
}
