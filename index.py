import sys
from dash import Input, Output, State, html
sys.path.append(r"C:\Users\marc_\Documents\Git\bfabric-web-apps")

from bfabric_web_apps import create_app, load_config, get_static_layout, display_page_generic, submit_bug_report
from components import get_template_app_specific_layout
import components
import dash_bootstrap_components as dbc

# Load configuration for the Dash app.
config = load_config("./PARAMS.py")

# Initialize the app
app = create_app()

# App title
app_title = "Bfabric App Template"

# Specific content for the Main tab
main_content = get_template_app_specific_layout()

# Define app layout
app.layout = get_static_layout(app_title, main_content)

@app.callback(
    [
        Output('token', 'data'),
        Output('token_data', 'data'),
        Output('entity', 'data'),
        Output('page-title', 'children'),
    ],
    [Input('url', 'search')]
)
def display_page(url_params):
    """
    Callback for processing URL parameters and managing authentication.
    """
    token, tdata, entity_data, _, page_title = display_page_generic(url_params, app_title)
    return token, tdata, entity_data, page_title

@app.callback(
    [
        Output("alert-fade-bug", "is_open"),
        Output("alert-fade-bug-fail", "is_open")
    ],
    [Input("submit-bug-report", "n_clicks")],
    [State("bug-description", "value"), State("token", "data"), State("entity", "data")],
    prevent_initial_call=True
)
def handle_bug_report(n_clicks, bug_description, token, entity_data):
    """
    Delegates to the submit_bug_report function.
    """
    is_open, is_fail = submit_bug_report(n_clicks, bug_description, token, entity_data)
    return is_open, is_fail


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
    # Handle sidebar and input disabling based on token_data
    if token_data is None:
        sidebar_state = (True, True, True, True, True)
    elif not config["DEV"]:
        sidebar_state = (False, False, False, False, False)
    else:
        sidebar_state = (True, True, True, True, True)

    # Handle auth-div content
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
            html.P(f"Modified: {entity_data['modified']}"),
        ]
        auth_div_content = dbc.Row([dbc.Col(component_data), dbc.Col(entity_details)])

    return (*sidebar_state, auth_div_content)


if __name__ == "__main__":
    app.run_server(debug=True, port=config["PORT"], host=config["HOST"])
