from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px


# Data
df = px.data.iris()

# ZBT Icon
def drawIcon():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.Img(src='assets/zbt.PNG')
                ], style={'textAlign': 'center'})
            ])
        ),
    ])

# Text field Title
def drawTextTitle():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("IGF MAXCoat - PEMFC-AST Testing"),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])




# Testrig Figure
def drawFigureTestrig():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.line(
                        df, color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                    }
                )
            ])
        ),
    ])

# Figure
def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                )
            ])
        ),
    ])

# Figure AST
def drawFigureAST():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.line(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
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
                    figure=px.line(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                )
            ])
        ),
    ])


# Figure EIS
def drawFigureEIS():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.scatter(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                )
            ])
        ),
    ])

# Figure CV
def drawFigureCV():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.line(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
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
        ]), color = 'dark'
    )
])

# Run app and display result inline in the notebook
app.run_server()