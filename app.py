from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from app_data import tb_data, iv_data, ast_data, eis_data, cv1_data, deg_data
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
                ], style={'textAlign': 'center'})
            ])
        ),
    ])

# Text - Title
def drawTextTitle():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("IGF MAXCoat - PEMFC-AST Testing"),
                ], style={'textAlign': 'center', 'color':colors['zbt']})
            ])
        ),
    ])

# Figure - Testbench
def drawFigureTestrig():
    return html.Div([
        dbc.Row([
            dbc.Col([
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
                    ])
                ),
                ], width=10
            ),
            dbc.Col([
                dbc.Row([
                    dbc.Card(
                        dbc.CardBody([
                            html.Div([
                                html.H2("Time of Operation: 8days"),
                            ], style={'textAlign': 'center'}
                            )
                        ])
                    )
                    ], align='center'
                ),
                dbc.Row([
                    dbc.Card(
                        dbc.CardBody([
                            dbc.CardBody([
                                html.Div([
                                    html.H2("Time of AST: 6days"),
                                ], style={'textAlign': 'center'}
                                )
                            ])
                        ])
                    )
                    ], align='center'
                )
                ], width=2
            )
            ], align='center'
        )
    ])

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
            ])
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
app = Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([                   # 1
                dbc.Col([
                    drawIcon()
                ], width=2),
                dbc.Col([
                    drawTextTitle()
                ], width=10),
            ], align='center'),
            html.Br(),
            dbc.Row([                   # 2
                dbc.Col([
                    drawFigureTestrig()
                ], width=12),
            ], align='center'),
            html.Br(),
            dbc.Row([                   # 3
                dbc.Col([
                    drawFigureAST()
                ], width=6),
                dbc.Col([
                    drawFigureIV()
                ], width=6),
            ], align='center'),
            html.Br(),
            dbc.Row([                   # 4
                dbc.Col([
                    drawFigureEIS()
                ], width=6),
                dbc.Col([
                    drawFigureCV()
                ], width=6),
            ], align='center'),
            html.Br(),
            dbc.Row([                   # 5
                dbc.Col([
                    drawFigureDEG()
                ], width=6),
                dbc.Col([
                ], width=6),
            ], align='center'),
        ]), color = 'dark'
    )
])

# Run app and display result inline in the notebook
app.run_server(debug=True)