import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.renderer = '''
var renderer = new DashRenderer({
    request_pre: (payload) => {
        // print out payload parameter
        console.log(payload);
    },
    request_post: (payload, response) => {
        // print out payload and response parameter
        console.log(payload);
        console.log(response);
    },
    csrf_config: {
        headerName: 'X-XSRF-TOKEN',
        cookieName: 'XSRF-TOKEN'
    }
})
'''

app.layout = html.Div('Simple Dash App')

if __name__ == '__main__':
    app.run_server(debug=True)
