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
import components
import dash_bootstrap_components as dbc


# Here we read the PARAMS.py file and parse the configuration settings for the app from PARAMS.py per https://github.com/GWCustom/bfabric-web-app-template
config = load_config("./PARAMS.py")

# Initialize the Dash application.
# create_app: Sets up the Dash app instance with necessary configurations and middleware for Bfabric integration.
app = create_app()

# App title that will appear in the browser tab.
app_title = "Bfabric App Template"

# Define the content to be displayed in the User Interface:
app.layout = get_static_layout(         # The function from bfabric_web_apps that sets up the app layout.
    app_title,                          # The app title we defined previously
    components.app_specific_layout,     # The main content for the app defined in components.py
    components.documentation_content    # Documentation content for the app defined in components.py
)

# This function updates various data stores in the User Interface which can be referenced later by your 
# custom callback functions. This function is necessary for handling authentication and URL parameters.
@app.callback(
    [
        Output('token', 'data'),                # Output the authentication token to the 'token' data store.
        Output('token_data', 'data'),           # Output the token data to the 'token_data' data store.
        Output('entity', 'data'),               # Output the entity data to the 'entity' data store.
        Output('page-title', 'children'),       # Output the page title to the 'page-title' children.
        Output('session-details', 'children'),  # Output the session details to the 'session-details' children.
    ],
    [Input('url', 'search')]                    # The token which is extracted from the URL parameters.   
)
def display_page(url_params):
    """
    DO NOT EDIT THIS FUNCTION.
    Callback for processing URL parameters and managing authentication.
    """

    # Here we generate the necessary data for the app to function from the token recieved in the URL parameters.
    return display_page_generic(url_params)


# This is the callback which handles bug report submissions. 
@app.callback(
    [
        Output("alert-fade-bug-success", "is_open"), # A bool indicating whether the success alert should be displayed.
        Output("alert-fade-bug-fail", "is_open")     # A bool indicating whether the failure alert should be displayed.
    ],
    [Input("submit-bug-report", "n_clicks")],        # The number of times the "submit-bug-report" button was clicked.
    [State("bug-description", "value"), State("token", "data"), State("entity", "data")], # State parameters for the bug report.
    prevent_initial_call=True
)
def handle_bug_report(n_clicks, bug_description, token, entity_data):
    """
    DO NOT EDIT THIS FUNCTION.
    Delegates to the submit_bug_report function from bfabric_web_apps.
    """
    # A bfabric_web_apps function that submits the bug report using the provided description, token, and entity data.  
    return submit_bug_report(n_clicks, bug_description, token, entity_data)


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
if __name__ == "__main__":
    app.run_server(debug=True, port=config["PORT"], host=config["HOST"])