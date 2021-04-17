import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Textarea(
            id="textarea_id",
            value="Copy and paste here",
            style={ "height": 100},
        ),
        dcc.Clipboard(
            target_id="textarea_id",
            title="copy",
            style={
                "display": "inline-block",
                "fontSize": 20,
                "verticalAlign": "top",
            },
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)


