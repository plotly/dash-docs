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
                                    html.Div(id='hit-template', children=[
                                        html.Div(className='hit', children=[
                                            html.Div(className='hit-content', children=[
                                                html.H2('{{_highlightResult.name.value}}', className='hit-name'),
                                                html.A(href='{{permalink}}', children='{{permalink}}')
                                            ])
                                        ])
                                    ])
                                ])])
