from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from app_data import tb_data, iv_data, ast_data, eis_data, cv1_data, deg_data, df_param_ast, df_param_pol, summary, \
    sum_data_tr
import plotly.graph_objects as go


# Data
df = px.data.iris()

# Design Specific
colors = {'zbt':'#005EB8'}

# Iamge - Icon
def drawIcon():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.Img(src='assets/ZBT_Logo_RGB_B_S_cropped.png',
                             style={'height': '45px', 'width': 'auto', 'max-width': '100%'}
                    )
                ],
                )
            ], style={'textAlign': 'center', 'height': '80px'}
            )
        ),
    ], fluid=True, style={'padding': '0px'}
    )

# Text - Title
def drawTextTitle():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("IGF MAXCoat - PEMFC-AST Testing"),
                ], style={'textAlign': 'center', 'color': 'white'}
                )
            ], style={'height': '80px'}
            )
        ),
    ], fluid=True, style={'padding': '0px'}
    )


def drawFigureTestrig():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(data=tb_data).update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        title='Testbench-Parameter Monitoring',
                        xaxis=dict(title='duration [h]'),
                        yaxis=dict(title='current density [A/cm2]'),
                        yaxis2=dict(title='parameter selection', overlaying='y', side='right'),
                        legend={"x": 1.1, 'y': 1.4}
                    ),
                    config={
                    }
                )
            ], style={
                'height': '450px'
            }
            )
        ),
    ], fluid=True, style={'padding': '0px'}
    )


# Table - Testing Parameters
def drawTableParameterAST():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H6("Testing Parameters - AST"),
                ], style={'textAlign': 'center', 'color': 'white'}
                ),
                html.Div([
                    dash_table.DataTable(data=df_param_ast.to_dict('records'),
                                         style_data={'width': 'auto', 'height': 'auto',
                                                     'backgroundColor': 'rgba(0, 0, 0, 0)', 'color': 'white'
                                                     },
                                         style_cell={'font_size': '12px'
                                                     },
                                         style_header={'backgroundColor': colors['zbt'], 'color': 'white'
                                                       },
                                         style_cell_conditional=[
                                             {'if': {'column_id': 'Parameters'}, 'textAlign': 'left'
                                              },
                                             {'if': {'column_id': 'SetPoints'}, 'textAlign': 'right'
                                              }
                                             ],
                                         columns=[{"name": i, "id": i} for i in df_param_ast.columns
                                                  ],
                                         ),
                    ],
                    style={'padding': '5px'}
                )
                ], style={
                'height': '222px'
            }
            )
        )
    ], fluid=True, style={'padding': '0px'}
    )

# Table - AST Parameters
def drawTableParameterPOL():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H6("Testing Parameters - AST"),
                ], style={'textAlign': 'center', 'color': 'white'}
                ),
                html.Div([
                dash_table.DataTable(data=df_param_pol.to_dict('records'),
                                     style_data={'width': 'auto', 'height': 'auto',
                                                 'backgroundColor': 'rgba(0, 0, 0, 0)', 'color': 'white'
                                                 },
                                     style_cell={'font_size': '12px'
                                                 },
                                     style_header={'backgroundColor': colors['zbt'], 'color': 'white'
                                                   },
                                     style_cell_conditional=[
                                         {'if': {'column_id': 'Parameters'}, 'textAlign': 'left'
                                          },
                                         {'if': {'column_id': 'SetPoints'}, 'textAlign': 'right'
                                          }
                                         ],
                                     columns=[{"name": i, "id": i} for i in df_param_ast.columns
                                              ],
                                     ),
                    ],
                    style={'padding': '5px'}
                )
                ], style={
                'height': '222px'
            }
            )
        )
    ], fluid=True, style={'padding': '0px'}
    )

# Figure AST
def drawFigureAST():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(data=ast_data
                                     ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        title='AST-Load-Cycles',
                        xaxis=dict(title='duration [h]'),
                        yaxis=dict(title='current density [A/cm2]'),
                        legend={"x": 1.1, 'y': 1.4}
                    ),
                    config={
                    }
                )
            ], style={}
            )
        ),
    ], fluid=True, style={'padding': '0px'}
    )

# Figure AST
def drawFigureDEG():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(data=deg_data,
                                     ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        title='AST-Load-Cycles',
                        xaxis=dict(title='duration [h]'),
                        yaxis=dict(title='current density [A/cm2]'),
                        yaxis2=dict(title='ASR [mOhm*cm2]', overlaying='y', side='right'),
                        legend={"x": 1.1, 'y': 1.4}
                    ),
                    config={
                    }
                )
            ], style={}
            )
        ),
    ], fluid=True, style={'padding': '0px'}
    )

# Figure IV
def drawFigureIV():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(data=iv_data
                                     ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        title='IV-Curves in between AST-Cycling',
                        xaxis=dict(title='potential [V]'),
                        yaxis=dict(title='current density [A/cm2]'),
                        legend={"x": 1.1, 'y': 1.4}
                    ),
                    config={
                    }
                )
            ])
        ),
    ], fluid=True, style={'padding': '0px'}
    )


# Figure EIS
def drawFigureEIS():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(data=eis_data
                                     ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        title='EIS in between AST-Cycling',
                        xaxis=dict(title='impedance real [Ohm*cm2]'),
                        yaxis=dict(title='impedance imag [Ohm*cm2]'),
                        legend={"x": 1.1, 'y': 1.4}
                    ),
                    config={
                    }
                )
            ],
            )
        ),
    ], fluid=True, style={'padding': '0px'}
    )

# Figure CV
def drawFigureCV():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(data=cv1_data
                                     ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        title='CV in between AST-Cycling',
                        xaxis=dict(title='potential vs. H2-Anode [V]'),
                        yaxis=dict(title='current [A]'),
                        legend={"x": 1.1, 'y': 1.4}
                    ),
                    config={
                    }
                )
            ],
            )
        ),
    ], fluid=True, style={'padding': '0px'}
    )

def drawPlaceholder():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H6('Test')
                ], style={
                    'textAlign': 'center', 'color': 'white'
                }
                )
            ], style={
            }
            )
        )
    ], fluid=True, style={'padding': '0px'}
    )

def drawTestrigSummary():
    return dbc.Container([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2('Time of Operation'),
                ], style={
                    'textAlign': 'center', 'color': 'white'
                }
                ),
                html.Div([
                    html.H1(str(summary['time of operation [h]']) + ' h'),
                    dcc.Graph(figure=go.Figure(data=sum_data_tr
                              ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        # title='CV in between AST-Cycling',
                        # xaxis=dict(title='potential vs. H2-Anode [V]'),
                        # yaxis=dict(title='current [A]'),
                        legend={"x": 1.1, 'y': 1.4}
                    ),
                    config={
                    }
                    )
                ], style={
                }
                )
            ], style={
            }
            )
        )
    ], fluid=True, style={'padding': '0px'}
    )

# Build App
app = Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([                   # 1
                dbc.Col([
                    drawIcon()
                ], width=2, style={'background': colors['zbt'], 'padding': '2px'}
                ),
                dbc.Col([
                    drawTextTitle()
                ], width=10, style={'background':  colors['zbt'], 'padding': '2px'}
                ),
            ], align='center',
            ),
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        drawTableParameterAST()
                    ], style={'background': colors['zbt'], 'padding': '2px'}
                    ),
                    dbc.Row([
                        drawTableParameterPOL()
                    ], style={'background': colors['zbt'], 'padding': '2px'}
                    )
                ], width=3, style={}
                ),
                dbc.Col([
                    drawFigureTestrig()
                ], width=7, style={'background':  colors['zbt'],  'padding': '2px'}
                ),
                dbc.Col([
                    drawTestrigSummary()
                ], width=2, style={'background': colors['zbt'], 'padding': '2px'}
                ),
            ], align='center',
            ),
            dbc.Row([                   # 3
                dbc.Col([
                    drawFigureAST()
                ], width=4,
                    style={'background': colors['zbt'], 'padding': '2px'
                    }
                ),
                dbc.Col([
                    drawPlaceholder()
                ], width=2, style={'background': colors['zbt'], 'padding': '2px'}
                ),
                dbc.Col([
                    drawFigureDEG()
                ], width=4,
                    style={'background': colors['zbt'], 'padding': '2px'
                           }
                ),
                dbc.Col([
                    drawPlaceholder()
                ], width=2, style={'background': colors['zbt'], 'padding': '2px'}
                ),
            ], align='center'),
            dbc.Row([                   # 4
                dbc.Col([
                    drawFigureEIS()
                ], width=6,
                    style={'background': colors['zbt'], 'padding': '2px'
                           }
                ),
                dbc.Col([
                    drawFigureCV()
                ], width=6,
                    style={'background': colors['zbt'], 'padding': '2px'
                           }
                ),
            ], align='center'),
            dbc.Row([                   # 5
                dbc.Col([
                    drawFigureIV()
                ], width=6,
                    style={'background': colors['zbt'], 'padding': '2px'
                           }
                ),
                dbc.Col([
                ], width=6,
                    style={'background': colors['zbt'], 'padding': '2px'
                           }
                ),
            ], align='center', style={'height': '400px'}),
        ], style={'background': colors['zbt'], 'padding': '0px'
                  }),
    )
], fluid=True
)

# Run app and display result inline in the notebook
app.run_server(debug=True)