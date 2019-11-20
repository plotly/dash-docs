import dash
import dash_core_components as dcc
import dash_html_components as html


layout = html.Div(style={'padding': 20},
                  children=[html.H1('Dash Doc Search'),
                            dcc.Input(id='search-input',
                                      placeholder='Search the Dash docs...',
                                      type='text',
                                      value=''),
                            html.Div(id='hits',
                                     children=[html.Div(id='hit-template',
                                                        style={'display': 'none'},
                                                        children=[html.H3(html.A('{{{_highlightResult.name.value}}}',
                                                                                 href='{{permalink}}',
                                                                                 style={'background-color': '#ffffff',
                                                                                        'padding-left': '0px'}),
                                                                          style={'margin-bottom': '1rem'}),
                                                                  html.P('{{{_highlightResult.description.value}}}')
                                                        ])

                            ])

])
