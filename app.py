from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from app_data import tb_data, iv_data, ast_data, eis_data, cv1_data, deg_data, df_param_ast, df_param_pol
import plotly.graph_objects as go


# Data
df = px.data.iris()

# Design Specific
colors = {'zbt':'#005EB8'}

# Iamge - Icon
def drawIcon():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.Img(src='assets/ZBT_Logo_RGB_B_S_cropped.png',
                             style={'height':'45px', 'width':'auto', 'max-width': '100%'}
                    )
                ],
                )
            ], style={'height': '80px'}
            )
        ),
    ],
    )

# Text - Title
def drawTextTitle():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("IGF MAXCoat - PEMFC-AST Testing"),
                ], style={'textAlign': 'center', 'color': 'white'}
                )
            ], style={'height': '80px'}
            )
        ),
    ])


def drawFigureTestrig():
    return html.Div([
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
                        legend={"x": 1.1, 'y':1.4}
                    ),
                    config={
                    }
                )
            ], style={})
        ),
    ])


# Table - Testing Parameters
def drawTableParameterAST():
    return html.Div([
        html.Div([
            html.H6("Testing Parameters - AST"),
        ], style={'textAlign': 'center', 'color': 'white'}
        ),
        html.Br(),

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
        )
        ]
    )

# Table - AST Parameters
def drawTableParameterPOL():
    return html.Div([
        html.Div([
            html.H6("Testing Parameters - AST"),
        ], style={'textAlign': 'center', 'color': 'white'}
        ),
        html.Br(),
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
        )
    ]
    )

# Figure AST
def drawFigureAST():
    return  html.Div([
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
            ])
        ),
    ])

# Figure AST
def drawFigureDEG():
    return  html.Div([
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
            ], style={'textAlign': 'center'}
            )
        ),
    ])

# Figure IV
def drawFigureIV():
    return  html.Div([
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
    ])


# Figure EIS
def drawFigureEIS():
    return html.Div([
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
            ])
        ),
    ])

# Figure CV
def drawFigureCV():
    return html.Div([
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
            ])
        ),
    ])


# Build App
app = Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([                   # 1
                dbc.Col([
                    drawIcon()
                ], width=2, style={'background': 'red', 'padding': '1px'}
                ),
                dbc.Col([
                    drawTextTitle()
                ], width=10, style={'background': 'yellow','padding': '1px', 'mr': '1px'}
                ),
            ], align='center', justify=False
                , style={'background': 'white', 'height': '80px', 'mb':'10px', 'mt':'2px', 'padding' : '0px'}
            ),
            dbc.Row([                   # 2
                dbc.Col([
                    drawFigureTestrig()
                ], width=9, style={}
                ),
                dbc.Col([
                    dbc.Row([
                            dbc.Card(
                                dbc.CardBody([
                                    drawTableParameterAST()
                                ])
                            )
                    ], align='center'
                    ),
                    html.Br(),
                    dbc.Row([
                        dbc.Card(
                            dbc.CardBody([
                                dbc.CardBody([
                                    drawTableParameterPOL()
                                ])
                            ])
                        )
                    ], align='center'
                    )
                ], width=3, style={}
                ),
                ], align='center', style={'background': 'white', 'height': '80px', 'mb':'10px', 'mt':'2px', 'padding' : '0px'}
            ),
            # html.Br(),
            # dbc.Row([                   # 3
            #     dbc.Col([
            #         drawFigureAST()
            #     ], width=6),
            #     dbc.Col([
            #         drawFigureDEG()
            #     ], width=6),
            # ], align='center'),
            # html.Br(),
            # dbc.Row([                   # 4
            #     dbc.Col([
            #         drawFigureEIS()
            #     ], width=6),
            #     dbc.Col([
            #         drawFigureCV()
            #     ], width=6),
            # ], align='center'),
            # html.Br(),
            # dbc.Row([                   # 5
            #     dbc.Col([
            #         drawFigureIV()
            #     ], width=6),
            #     dbc.Col([
            #     ], width=6),
            # ], align='center', style={'height': '400px'}),
        ], style={'background': colors['zbt'], 'mt': '0px', 'mb': '0px', 'padding': '1px'}),
    )
], style={'background': 'pink'}
)

# Run app and display result inline in the notebook
app.run_server(debug=True)