## app.R

`app.R` is a required R file that contains your Dash app's code and is invoked by the command that you specify in the `Procfile`. It must be placed in your project's root directory.
This file must also contain a line that includes `app$run_server()`, or that
loads an R script that does.

Dash Enterprise app deployment will fail if `app.R` is not included in the project folder, or if `app.R` does not contain `app$run_server()`.

```
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout(
    
    [...]
)

app$run_server()

```

---
