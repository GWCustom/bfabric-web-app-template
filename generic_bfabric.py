"""
Reusable UI Components and Core Functions for Bfabric App
=========================================================

IMPORTANT: DO NOT MODIFY THIS FILE
----------------------------------
This module contains essential components and core functionalities for the Bfabric web app.
It is a foundational part of the system, and any changes to this file may disrupt functionality
or compatibility with other modules.

This module includes:
  - Initialization of the Dash app instance.
  - Callbacks for authentication and URL parameter processing.
  - Callback for bug report handling.
  - Content to display for authenticated and unauthenticated users.
"""

# Required Imports
# ----------------
import sys
# Ensure the bfabric-web-apps module is accessible.
sys.path.append(r"C:\Users\marc_\Documents\Git\bfabric-web-apps")
from dash import Input, Output, State
from bfabric_web_apps import create_app, process_url_and_token, submit_bug_report
from dash import html

# Application Initialization
# ---------------------------
# Create the Dash app instance.
app = create_app()

# Callbacks
# ---------

## URL and Token Processing
# --------------------------
@app.callback(
    [
        Output('token', 'data'),                # Store authentication token.
        Output('token_data', 'data'),           # Store token metadata.
        Output('entity', 'data'),               # Store entity data.
        Output('page-title', 'children'),       # Update page title.
        Output('session-details', 'children'),  # Update session details.
    ],
    [Input('url', 'search')]                    # Extract token from URL parameters.
)
def generic_process_url_and_token(url_params):
    """
    Handles URL parameter processing and manages authentication.

    Parameters:
        url_params (str): URL parameters containing the token.

    Returns:
        tuple: Data for token, token metadata, entity, page title, and session details.
    """
    return process_url_and_token(url_params)

## Bug Report Handling
# ---------------------
@app.callback(
    [
        Output("alert-fade-bug-success", "is_open"),  # Show success alert.
        Output("alert-fade-bug-fail", "is_open")       # Show failure alert.
    ],
    [Input("submit-bug-report", "n_clicks")],          # Detect button clicks.
    [
        State("bug-description", "value"),            # Bug description input.
        State("token", "data"),                       # Authentication token.
        State("entity", "data")                       # Entity metadata.
    ],
    prevent_initial_call=True                            # Prevent callback on initial load.
)
def generic_handle_bug_report(n_clicks, bug_description, token, entity_data):
    """
    Handles the submission of bug reports by delegating to the `submit_bug_report` function.

    Parameters:
        n_clicks (int): Number of times the submit button was clicked.
        bug_description (str): Description of the bug provided by the user.
        token (dict): Authentication token data.
        entity_data (dict): Metadata about the authenticated entity.

    Returns:
        tuple: Success and failure alert states.
    """
    return submit_bug_report(n_clicks, bug_description, token, entity_data)

# UI Components
# --------------

## Unauthenticated User Content
# ------------------------------
# Message displayed to users who are not authenticated.
no_auth = [
    html.P("You are not currently logged into an active session. Please log into bfabric to continue:"),
    html.A('Login to Bfabric', href='https://fgcz-bfabric.uzh.ch/bfabric/')  # Link to the Bfabric login page.
]

## Placeholder for Authenticated User Content
# --------------------------------------------
# Dynamic content displayed to authenticated users.
auth = [html.Div(id="auth-div")]
