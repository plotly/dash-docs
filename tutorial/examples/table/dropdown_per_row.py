import dash
import dash_html_components as html
import dash_table
import pandas as pd
from collections import OrderedDict


app = dash.Dash(__name__)

df_per_row_dropdown = pd.DataFrame(OrderedDict([
    ('City', ['NYC', 'Montreal', 'Los Angeles']),
    ('Neighborhood', ['Brooklyn', 'Mile End', 'Venice']),
    ('Temperature (F)', [70, 60, 90]),
]))


app.layout = html.Div([
    dash_table.DataTable(
        id='dropdown_per_row',
        data=df_per_row_dropdown.to_dict('records'),
        columns=[
            {'id': 'City', 'name': 'City'},
            {'id': 'Neighborhood', 'name': 'Neighborhood', 'presentation': 'dropdown'},
            {'id': 'Temperature (F)', 'name': 'Temperature (F)'}
        ],

        editable=True,
        column_conditional_dropdowns=[
            {
                # column id
                'id': 'Neighborhood',
                'dropdowns': [
                    {
                        # these are filter strings
                        'condition': '{City} eq "NYC"',
                        'dropdown': [
                            {'label': i, 'value': i}
                            for i in [
                                'Brooklyn',
                                'Queens',
                                'Staten Island'
                            ]
                        ]
                    },

                    {
                        'condition': '{City} eq "Montreal"',
                        'dropdown': [
                            {'label': i, 'value': i}
                            for i in [
                                'Mile End',
                                'Plateau',
                                'Hochelaga'
                            ]
                        ]
                    },

                    {
                        'condition': '{City} eq "Los Angeles"',
                        'dropdown': [
                            {'label': i, 'value': i}
                            for i in [
                                'Venice',
                                'Hollywood',
                                'Los Feliz'
                            ]
                        ]
                    }

                ]
            }
        ]
    ),
    html.Div(id='dropdown_per_row_container')
])


if __name__ == '__main__':
    app.run_server(debug=True)
