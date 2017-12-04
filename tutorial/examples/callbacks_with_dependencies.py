# -*- coding: utf-8 -*-
import time
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

all_options = {
    'NYC': {
        'Places': [
            'Statue of Liberty', 'Wall Street'
        ],
        'Boroughs': [
            'Brooklyn', 'The Bronx', 'Manhattan', 'Queens', 'Staten Island'
        ]
    },
    u'Montréal': {
        u'Monuments Célèbres': [
            'Olympic Stadium', 'Parc la Fontaine'
        ],
        'Les Voisinages': [
            'Le Plateau', 'Hochelaga', 'Outremont'
        ]
    }
}
app.layout = html.Div([
    # Initial dropdown with initial state
    dcc.Dropdown(
        id='cities-dropdown',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='NYC'
    ),

    # Note how options and values aren't supplied for the
    # remaining two dropdowns.
    # When the dash app starts, it will traverse the callback dependency tree
    # and call all of the appropriate callbacks to fill out the app's state
    dcc.Dropdown(id='category-dropdown'),
    dcc.Dropdown(id='sub-category-dropdown'),

    # We'll display the values of the dropdowns in this component
    html.Div(id='display')
])


# Update the category dropdown's 'options'
# when the input dropdown's 'value' changes
@app.callback(Output('category-dropdown', 'options'),
              [Input('cities-dropdown', 'value')])
def update_category_options(selected_city):
    time.sleep(2)
    filtered_options = all_options[selected_city].keys()
    return [{'label': k, 'value': k} for k in filtered_options]


# Update the category dropdown's 'value'
# when its 'options' get changed
@app.callback(Output('category-dropdown', 'value'),
              [Input('category-dropdown', 'options')])
def update_category_value(new_options):
    return new_options[0]['value']


# Update the sub-category dropdown's 'options'
# when the cities-dropdown dropdown's 'value' changes or
# when the categories dropdown's value changes
@app.callback(Output('sub-category-dropdown', 'options'), [
    Input('cities-dropdown', 'value'),
    Input('category-dropdown', 'value')])
def update_sub_category_options(selected_city, selected_category):
    time.sleep(2)
    filtered_options = all_options[selected_city][selected_category]
    return [{'label': k, 'value': k} for k in filtered_options]


# Update the sub-category dropdown's 'value'
# when its options change
@app.callback(
    Output('sub-category-dropdown', 'value'),
    [Input('sub-category-dropdown', 'options')])
def update_sub_category_value(new_options):
    return new_options[0]['value']


# Display the selected value when all of the
# dropdown's values have finished updating.
@app.callback(
    Output('display', 'children'),
    [Input(id, 'value') for id in
     ['cities-dropdown', 'category-dropdown', 'sub-category-dropdown']])
def update_display(selected_city, selected_category, selected_sub_category):
    time.sleep(2)
    return u"You've selected {}, {}, and {}".format(
        selected_city,
        selected_category,
        selected_sub_category
    )


if __name__ == '__main__':
    app.run_server(debug=True)
