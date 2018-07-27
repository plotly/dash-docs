import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs", value='tab-2', children=[
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
        ]),
    html.Div(id='tabs-content')
])

@app.callback(dash.dependencies.Output('tabs-content', 'children'),
            [dash.dependencies.Input('tabs', 'value')])
def render_content(tab):
    if(tab == 'tab-1'):
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif(tab == 'tab-2'):
        return html.Div([
            html.H3('Tab content 2')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)