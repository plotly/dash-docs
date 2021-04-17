
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

code = """   
```
    html.Div(
    [
        dcc.Markdown(
            code,
            id="code",
            style={"width": 500, "height": 200, "overflow": "auto"},
        ),
        dcc.Clipboard(
            target_id="code",
            style={
                "position": "absolute",
                "top": 0,
                "right": 20,
                "fontSize": 20,
            },
        ),
    ],
    style={
        "width": 500,
        "height": 200,
        "position": "relative",
    },
)

```"""

app.layout = html.Div(
    [
        dcc.Markdown(
            code,
            id="code",
            style={"width": 500, "height": 200, "overflow": "auto"},
        ),
        dcc.Clipboard(
            target_id="code",
            style={
                "position": "absolute",
                "top": 0,
                "right": 20,
                "fontSize": 20,
            },
        ),
    ],
    style={
        "width": 500,
        "height": 200,
        "position": "relative",
    },
)


if __name__ == "__main__":
    app.run_server(debug=True)

