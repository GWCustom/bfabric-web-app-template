import dash_bootstrap_components as dbc
from dash import html, dcc

"""
Defines reusable UI components for the Bfabric app.
Each section provides specific elements like sidebars or authentication messages.
"""

# Sidebar layout components for user interaction.
sidebar = [
    html.P(id="sidebar_text", children="Select a Value"),  # Sidebar header text.
    dcc.Slider(0, 20, 5, value=10, id='example-slider'),  # Slider for selecting a numeric value.
    html.Br(),
    dcc.Dropdown(
        ['Genomics', 'Proteomics', 'Metabolomics'],  # Dropdown options.
        'Genomics',  # Default value.
        id='example-dropdown'  # Dropdown ID for callback integration.
    ),
    html.Br(),
    dbc.Input(value='Enter Some Text', id='example-input'),  # Text input field.
    html.Br(),
    dbc.Button('Submit', id='example-button'),  # Button for user submission.
]

# Here is the content to be displayed when the user is NOT authenticated.
no_auth = [
    html.P("You are not currently logged into an active session. Please log into bfabric to continue:"),
    html.A('Login to Bfabric', href='https://fgcz-bfabric.uzh.ch/bfabric/')  # Link to the Bfabric login page.
]

# Placeholder for authenticated user content.
auth = [html.Div(id="auth-div")]


# Documentation content for the app. This get's displayed under the "Documentation" tab.
# This content must always be a list of dash components.
documentation_content = [
    html.H2("Welcome to Bfabric App Template"),
    html.P(
        [
            "This app serves as the user-interface for ",
            html.A("Bfabric App Template,", href="#", target="_blank"),
            " a versatile tool designed to help build and customize new applications.",
        ]
    ),
    html.Br(),
    html.H4("Developer Info"),
    html.P(
        [
            """This app was written by Griffin White, for the FGCZ. 
            If you wish to report a bug, please use the \"bug reports\" tab. 
            If you wish to contact the developer for other reasons, please use the email:""",
            html.A(" griffin@gwcustom.com", href="mailto:griffin@gwcustom.com"),
        ]
    ),
    html.Br(),
    html.H4("Main Features"),
    html.P(
        [
            html.B("Feature 1 -- "),
            "Brief description of Feature 1.",
            html.Br(),
            html.Br(),
            html.B("Feature 2 -- "),
            "Brief description of Feature 2.",
            html.Br(),
            html.Br(),
            html.B("Feature 3 -- "),
            "Brief description of Feature 3.",
            html.Br(),
            html.Br(),
            html.B("Custom Flags -- "),
            "Details about using custom flags for advanced configurations. Provide examples or references if applicable.",
            html.Br(),
            html.Br(),
        ],
        style={"margin-left": "2vw"},
    ),
    html.H4("Other Tabs"),
    html.P(
        [
            "Descriptions of other tabs or features, such as:",
            html.Br(),
            html.B("Tab 1 -- "),
            "Brief description of Tab 1 functionality.",
            html.Br(),
            html.B("Tab 2 -- "),
            "Brief description of Tab 2 functionality.",
            html.Br(),
            html.B("Tab 3 -- "),
            "Brief description of Tab 3 functionality.",
        ],
        style={"margin-left": "2vw"},
    ),
    html.Br(),
    html.H4("Future Enhancements"),
    html.P(
        "This section can outline planned features or enhancements for the application.",
        style={"margin-left": "2vw"},
    ),
    html.Br(),
]

# Below is the primary layout for the app. This layout includes a sidebar and a main content area.
# This object MUST be a "dbc.Row" element to render properly.
app_specific_layout = dbc.Row(
        id="page-content-main",
        children=[
            dbc.Col(
                html.Div(
                    id="sidebar",
                    children=sidebar,  # Sidebar content defined earlier.
                    style={
                        "border-right": "2px solid #d4d7d9",
                        "height": "100%",
                        "padding": "20px",
                        "font-size": "20px"
                    }
                ),
                width=3,  # Width of the sidebar column.
            ),
            dbc.Col(
                html.Div(
                    id="page-content",
                    children=[
                        html.Div(id="auth-div")  # Placeholder for `auth-div` to be updated dynamically.
                    ],
                    style={
                        "margin-top": "20vh",
                        "margin-left": "2vw",
                        "font-size": "20px"
                    }
                ),
                width=9,  # Width of the main content column.
            ),
        ],
        style={"margin-top": "0px", "min-height": "40vh"}  # Overall styling for the row layout.
    )
