'''
The Bfabric web app template serves as a foundation for building new applications using the Bfabric web apps module.
The Bfabric web apps module facilitates the rapid and professional development of visually appealing applications.
To effectively use the template, a basic knowledge of Dash is required. It is recommended to review the documentation
for Dash Fundamentals, Parts 1 to 4.

- https://dash.plotly.com/layout

It is also recommended to take a look at the Bfabric web apps documentation:

- https://pypi.org/project/bfabric-web-apps/

To preview the template, execute this file and access the application on your localhost in the browser.
'''

import sys
from dash import Input, Output, State, html
sys.path.append(r"C:\Users\marc_\Documents\Git\bfabric-web-apps")

from bfabric_web_apps import create_app, load_config, get_static_layout, display_page_generic, submit_bug_report
from components import get_template_app_specific_layout
import components
import dash_bootstrap_components as dbc

# Load configuration for the Dash app.
# The configuration file (PARAMS.py) contains host, port, DEV, and the config file path to the .bfabricpy.yml file.
# The .bfabricpy.yml contains the login, password, and base URL. This is needed to log in as a power user.
# load_config: Reads the PARAMS.py file and parses the configuration settings for the app.
config = load_config("./PARAMS.py")

# Initialize the Dash application.
# create_app: Sets up the Dash app instance with necessary configurations and middleware for Bfabric integration.
app = create_app()

# App title that will appear in the browser tab.
app_title = "Bfabric App Template"

# Define the content for the main section of the app.
# This layout is specific to the current application and is defined in the components.py file.
main_content = get_template_app_specific_layout()

'''
Define the app.layout using the get_static_layout method from bfabric_web_apps.
The parameters passed are:

- app_title: A specific title for the app.
- main_content: The main content for the app, defined in the components.py file.
- documentation_content: Documentation content specific to the app, designed in the components.py file.

get_static_layout: Combines the app title, main content, and documentation into a structured layout.
'''
app.layout = get_static_layout(app_title, main_content, components.documentation_content)

@app.callback(
    [
        Output('token', 'data'),
        Output('token_data', 'data'),
        Output('entity', 'data'),
        Output('page-title', 'children'),
        Output('session-details', 'children'),
    ],
    [Input('url', 'search')]
)
def display_page(url_params):
    """
    Callback for processing URL parameters and managing authentication.

    Args:
        url_params (str): URL parameters passed to the app.

    Returns:
        Tuple containing:
            - token: Authentication token.
            - token_data: Data associated with the authentication token.
            - entity_data: Details of the authenticated entity.
            - page_title: Title to display on the page.
            - session_details: Information about the current session.

    display_page_generic: A function from bfabric_web_apps that handles generic URL parsing
    and returns the necessary data for authentication and page content setup.
    """
    token, tdata, entity_data, _, page_title, session_details = display_page_generic(url_params)
    return token, tdata, entity_data, page_title, session_details

'''
Define a callback to handle bug report submissions.

The parameters passed are:
- n_clicks: The number of times the "submit-bug-report" button was clicked.
- bug_description: A string describing the bug to be submitted.
- token: The authentication token for the session.
- entity_data: Information about the authenticated entity.

Returns:
    - is_open: A boolean indicating whether the success alert should be displayed.
    - is_fail: A boolean indicating whether the failure alert should be displayed.

submit_bug_report: A bfabric_web_apps function that submits the bug report using the
provided description, token, and entity data. It returns success and failure states.
'''
@app.callback(
    [
        Output("alert-fade-bug-success", "is_open"),
        Output("alert-fade-bug-fail", "is_open")
    ],
    [Input("submit-bug-report", "n_clicks")],
    [State("bug-description", "value"), State("token", "data"), State("entity", "data")],
    prevent_initial_call=True
)
def handle_bug_report(n_clicks, bug_description, token, entity_data):
    """
    Delegates to the submit_bug_report function from bfabric_web_apps.
    """
    is_open, is_fail = submit_bug_report(n_clicks, bug_description, token, entity_data)
    return is_open, is_fail

'''
Define a callback to dynamically update UI components based on user input.
This is an app-specific callback function. It updates content on the main page dynamically
based on user interactions and authentication status.

The parameters are:

Inputs:
    - slider_val: The current value of the slider.
    - dropdown_val: The selected value from the dropdown.
    - input_val: The current value of the input field.
    - n_clicks: The number of clicks on the example button.
    - token_data: Data associated with the authentication token.

States:
    - entity_data: Information about the authenticated entity.

Returns:
    - sidebar_state: Tuple indicating whether the sidebar and inputs should be disabled.
    - auth_div_content: Content to be displayed in the authorization section.
'''
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
    Updates the main UI elements dynamically based on user interactions.
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
        auth_div_content = html.Div(children=components.no_auth)
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

    return (*sidebar_state, auth_div_content)

# Entry point for running the app.
# If the script is run directly, the server starts with the specified configurations.
if __name__ == "__main__":
    app.run_server(debug=True, port=config["PORT"], host=config["HOST"])