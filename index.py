import sys
# Ensure the bfabric-web-apps module is accessible.
# sys.path.append(r"C:\Users\marc_\Documents\Git\bfabric-web-apps")
sys.path.append("../bfabric-web-apps")
from dash import Input, Output, State, html, dcc
import dash_bootstrap_components as dbc
from bfabric_web_apps import ( 
    get_static_layout, 
    get_logger, 
    get_power_user_wrapper,
    HOST, 
    PORT,
    DEV
)

import generic_bfabric
from generic_bfabric import app

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

documentation_content = [
    html.H2("Welcome to Bfabric App Template"),
    html.P(
        [
            "This app serves as the user-interface for Bfabric App Template, "
            "a versatile tool designed to help build and customize new applications."
        ]
    ),
    html.Br(),
    html.P(
        [
            "Please check out the official documentation of ",
            html.A("Bfabric Web Apps", href="https://pypi.org/project/bfabric-web-apps/", target="_blank"),
            "."
        ]
    )
]

app_title = "Bfabric App Template"

app.layout = get_static_layout(         # The function from bfabric_web_apps that sets up the app layout.
    app_title,                          # The app title we defined previously
    app_specific_layout,     # The main content for the app defined in components.py
    documentation_content    # Documentation content for the app defined in components.py
)

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
    
    # Determine sidebar and input states based on token_data and development mode.
    if token_data is None:
        sidebar_state = (True, True, True, True, True)
    elif not DEV:
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
         
        power_user_wrapper = get_power_user_wrapper(token_data) # The `token_data` parameter must be provided. 

        L = get_logger(token_data) # The `token_data` parameter needs to be provided.

        L.log_operation(
            "Example Log",                       # Operation name
            "This is an example of how to use the log_operation method.",  # Descriptive message
            params=None,                         # (Optional) Additional parameters to log
            flush_logs=True                      # (Optional) Flush logs immediately (default: True)
        )

    return (*sidebar_state, auth_div_content)

if __name__ == "__main__":
    app.run_server(debug=False, port=PORT, host=HOST)