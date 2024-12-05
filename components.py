import dash_bootstrap_components as dbc
from dash import html, dcc

default_sidebar = [
    html.P(id="sidebar_text", children="Select a Value"),
    dcc.Slider(0, 20, 5, value=10, id='example-slider'),
    html.Br(),
    dcc.Dropdown(['Genomics', 'Proteomics', 'Metabolomics'], 'Genomics', id='example-dropdown'),
    html.Br(),
    dbc.Input(value='Enter Some Text', id='example-input'),
    html.Br(),
    dbc.Button('Submit', id='example-button'),
]

no_auth = [
    html.P("You are not currently logged into an active session. Please log into bfabric to continue:"),
    html.A('Login to Bfabric', href='https://fgcz-bfabric.uzh.ch/bfabric/')
]

auth = [html.Div(id="auth-div")]



def get_template_app_specific_layout():
    """
    Returns the app-specific layout components.
    """
    return dbc.Row(
        id="page-content-main",
        children=[
            dbc.Col(
                html.Div(
                    id="sidebar",
                    children=default_sidebar,
                    style={
                        "border-right": "2px solid #d4d7d9",
                        "height": "100%",
                        "padding": "20px",
                        "font-size": "20px"
                    }
                ),
                width=3,
            ),
            dbc.Col(
                html.Div(
                    id="page-content",
                    children=[
                        *no_auth,
                        html.Div(id="auth-div")  # Placeholder for `auth-div` to be updated dynamically
                    ],
                    style={
                        "margin-top": "20vh",
                        "margin-left": "2vw",
                        "font-size": "20px"
                    }
                ),
                width=9,
            ),
        ],
        style={"margin-top": "0px", "min-height": "40vh"}
    )