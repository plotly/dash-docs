import dash
import dash_core_components as dcc
import dash_html_components as html


layout = html.Div(style={'padding': 20},
                  children=[html.H1('Dash Doc Search'),
                            dcc.Input(id='search-input',
                                      placeholder='Search the Dash docs...',
                                      type='text',
                                      value=''),
                            html.Div(id='search-results', children=[
                                    html.Div(id='hits'),
                                    html.Div(id='hit-template',
                                             style={'display': 'none'},
                                             children=[html.Div(
                                                    children=[html.A(href='{{permalink}}',
                                                                     children=[html.H3('{{{_highlightResult.name.value}}}')]),
                                                              html.P('{{{_highlightResult.description.value}}}')])

                                            ])
                                ])
])
