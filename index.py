'''
Bfabric Web App Template
========================

This file serves as a user-editable template for building applications using the Bfabric web apps module. 
Users can customize the layout, callbacks, and components in this file to suit their application's needs.

Before starting, ensure a basic understanding of Dash and refer to the following resources:
  - Dash Fundamentals (https://dash.plotly.com/layout)
  - Bfabric Web Apps Documentation (https://pypi.org/project/bfabric-web-apps/)

To preview the template:
1. Execute this file.
2. Access the application on your localhost in the browser.
'''

# Required Imports
# ----------------
import sys
# Ensure the bfabric-web-apps module is accessible.
sys.path.append(r"C:\Users\marc_\Documents\Git\bfabric-web-apps")
from dash import Input, Output, State, html, dcc
import dash_bootstrap_components as dbc
from bfabric_web_apps import load_config, get_static_layout, get_logger, get_power_user_wrapper
import generic_bfabric
from generic_bfabric import app

# Sidebar Components
# -------------------
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

# App Layout
# -----------
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

# Documentation Content
# ----------------------
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

# Load Configuration
# -------------------
# Here we read the PARAMS.py file and parse the configuration settings for the app from PARAMS.py per https://github.com/GWCustom/bfabric-web-app-template
config = load_config("./PARAMS.py")

# Set Title
# -------------------
# App title that will appear in the browser tab.
app_title = "Bfabric App Template"

# Set App Layout
# ---------------
# Define the content to be displayed in the User Interface:
app.layout = get_static_layout(         # The function from bfabric_web_apps that sets up the app layout.
    app_title,                          # The app title we defined previously
    app_specific_layout,     # The main content for the app defined in components.py
    documentation_content    # Documentation content for the app defined in components.py
)

# Callback for Updating UI
# -------------------------
@app.callback(
    [
        Output('sidebar_text', 'hidden'),
        Output('example-slider', 'disabled'),
        Output('example-dropdown', 'disabled'),
        Output('example-input', 'disabled'),
        Output('example-button', 'disabled'),
        Output('auth-div', 'children'),
    ],
    [
        Input('example-slider', 'value'),
        Input('example-dropdown', 'value'),
        Input('example-input', 'value'),
        Input('example-button', 'n_clicks'),
        Input('token_data', 'data'),
    ],
    [State('entity', 'data')]
)
def update_ui(slider_val, dropdown_val, input_val, n_clicks, token_data, entity_data):
    
    """
    EDIT HERE! 

    This is an example of a specific callback function for the app. You may edit this function to 
    handle various user interactions and update the UI accordingly.
    
    Define a callback to dynamically update UI components based on user input.
    This is an app-specific callback function. It updates content on the main page dynamically
    based on user interactions and authentication status.

    Specific details about app.callback functions can be found int he dash documentation:
    https://dash.plotly.com/basic-callbacks
    """

    # Determine sidebar and input states based on token_data and development mode.
    if token_data is None:
        sidebar_state = (True, True, True, True, True)
    elif not config["DEV"]:
        sidebar_state = (False, False, False, False, False)
    else:
        sidebar_state = (True, True, True, True, True)

    # Generate content for the auth-div based on authentication and entity data.
    if not entity_data or not token_data:
        auth_div_content = html.Div(children=generic_bfabric.no_auth)
    else:
        component_data = [
            html.H1("Component Data:"),
            html.P(f"Slider Value: {slider_val}"),
            html.P(f"Dropdown Value: {dropdown_val}"),
            html.P(f"Input Value: {input_val}"),
            html.P(f"Button Clicks: {n_clicks}")
        ]
        entity_details = [
            html.H1("Entity Data:"),
            html.P(f"Entity Class: {token_data['entityClass_data']}"),
            html.P(f"Entity ID: {token_data['entity_id_data']}"),
            html.P(f"Created By: {entity_data['createdby']}"),
            html.P(f"Created: {entity_data['created']}"),
            html.P(f"Modified: {entity_data['modified']}")
        ]
        auth_div_content = dbc.Row([dbc.Col(component_data), dbc.Col(entity_details)])


        # Get the Power User Wrapper
        # -------------------------
        # Use the `get_power_user_wrapper` function to initialize and retrieve the Power User Wrapper instance.  
         
        power_user_wrapper = get_power_user_wrapper(token_data) # The `token_data` parameter must be provided. 

        # For detailed examples and advanced usage, consult the official documentation:  
        # !!!ADD LINK TO SPECIFIC PART IN DOCUMENTATION!!!

        # Create Loggs
        # -------------------------

        # Step 1: Initialize the Logger instance
        # Use the `get_logger` function to get a Logger instance.   

        L = get_logger(token_data) # The `token_data` parameter needs to be provided.

        # Step 2: Log a message  
        # Use the `log_operation` method of the Logger instance to log messages.
        # This example demonstrates logging an operation with a descriptive message:

        L.log_operation(
            "Example Log",                       # Operation name
            "This is an example of how to use the log_operation method.",  # Descriptive message
            params=None,                         # (Optional) Additional parameters to log
            flush_logs=True                      # (Optional) Flush logs immediately (default: True)
        )

        # Notes on usage:  
        # The `Logger` class provides two primary ways to log operations:  
        # 1. Using the `log_operation` method for general logging.  
        # 2. Using the `logthis` method to wrap and log API calls.  

        # For more details and examples on both methods, please refer to the official documentation:  
        # !!!ADD LINK TO SPECIFIC PART IN DOCUMENTATION!!!

    return (*sidebar_state, auth_div_content)

# Run the Application
# --------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=config["PORT"], host=config["HOST"])