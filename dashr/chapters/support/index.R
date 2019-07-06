library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

utils <- new.env()
source('dashr/utils.R', local=utils)

layout = htmlDiv(list(dccMarkdown("
# Dash Support and Contact
Dash is an open-source product that is
developed and maintained by [Plotly](https://plot.ly).
### Dash Demos and Enterprise Trials
If you would like to trial or purchase a Dash Deployment Server,
[get in touch with us directly](https://plotly.typeform.com/to/rkO85m).
Our sales engineering team is happy to give you or your team
a demo of Dash and Dash Deployment Server too.

### Dash Workshops

We lead [two day Dash workshops](https://plotcon.plot.ly) every few months.
These frequently sell out, so [please register early](https://plotcon.plot.ly)
These workshops are lead by the authors of Dash and are tailored towards both beginners and experts.

### Sponsored Feature Requests and Customizations

If you or your company would like to sponsor a specific feature or enterprise
customization, get in touch with our
[advanced development team](https://plot.ly/dash/pricing/).
### Community Support
Our community forum at [community.plot.ly](https://community.plot.ly) has
a topic dedicated on [Dash](https://community.plot.ly/c/dash).
This forum is great for showing off projects, feature requests,
and general questions.
If you have found a bug, you can open an issue on GitHub at
[plotly/dash](https://github.com/plotly/dash).

### Direct Contact
If you would like to reach out to me directly,
you can email me at <chris@plot.ly> or on
Twitter at [@chriddyp](https://twitter.com/chriddyp).
Plotly is also on Twitter at [@plotlygraphs](https://twitter.com/plotlygraphs).
We are based in Montréal, Canada and our headquarters are in the Mile End.
If you're in the neighborhood, come say hi!"),
                      
htmlBr(),
htmlHr(),
dccMarkdown("[Back to the Table of Contents](/)")
)
)