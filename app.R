library(dash)

metas <- list(
  list(name = 'description', 
       content = 'Dash for R User Guide and Documentation. Dash is a framework for building analytical web apps in R and Python.')
)

app <- Dash$new(assets_folder="dash_docs/assets", meta_tags = metas)

index_string <-
  "<!DOCTYPE html>
        <html>
          <head>
            {%meta_tags%}
            <title>{%private$name%}</title>
            {%favicon%}
            {%css_tags%}
            <script>
              (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
              new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
              j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
              'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
              })(window,document,'script','dataLayer','GTM-N6T2RXG');
            </script>
          </head>
          <body>
            <!-- Google Tag Manager (noscript) -->
              <noscript><iframe src='https://www.googletagmanager.com/ns.html?id=GTM-N6T2RXG'
              height='0' width='0' style='display:none;visibility:hidden'></iframe></noscript>
          <!-- End Google Tag Manager (noscript) -->
            {%app_entry%}
            <footer>
              {%config%}
              {%scripts%}
            </footer>
          </body>
        </html>"

app$index_string(index_string)

app$title("Dash for R User Guide and Documentation | R & RStats | Plotly")
