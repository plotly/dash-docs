# R script to run author supplied code, typically used to install additional R packages
# contains placeholders which are inserted by the compile script
# NOTE: this script is executed in the chroot context; check paths!

r <- getOption("repos")
r["CRAN"] <- "http://cloud.r-project.org"
options(repos=r)

# ======================================================================
# packages go here
install.packages("remotes")

# installs Rcpp, rlang, BH
install.packages("later")

install.packages("jsonlite")
install.packages("rjson")
install.packages("listenv")
install.packages("anytime")
install.packages("readr")
install.packages("heatmaply")
install.packages("bezier")
install.packages("magick")
install.packages("png")
install.packages("foreach")
install.packages("glue")
install.packages("stringr")

remotes::install_github("plotly/dashR", upgrade=TRUE)
install.packages("manhattanly")
remotes::install_github("plotly/dash-canvas", ref="93224c3")
remotes::install_github("plotly/dash-cytoscape", ref="25b0301")
remotes::install_github("plotly/dash-bio", ref="44f8f3a")
remotes::install_github("plotly/dash-daq", ref="7ad539")
remotes::install_github("plotly/reqres", ref="verbose-debugging", upgrade=FALSE)

install.packages("dash-user-guide-components", repos=NULL, type="source")
