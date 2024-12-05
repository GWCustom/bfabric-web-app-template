import sys
from dash import html
from dash import Input, Output, State, html
import dash_bootstrap_components as dbc
import components

sys.path.append(r"C:\Users\marc_\Documents\Git\bfabric-web-apps")
from bfabric_web_apps import create_app, load_config, get_layout_with_side_panel, display_page_generic

#Load configuration for the Dash app.
config = load_config("./PARAMS.py")

# Initialize the app
app = create_app()

# Sidebar content and main content for customization
sidebar_content = [html.P("Sidebar Content")]
main_content = [html.P("Main Content")]

app_title = "Bfabric App Template"

# Select a layout
app.layout = html.Div(
children=[
    get_layout_with_side_panel(app_title),
    components.get_template_app_specific_layout()
])

@app.callback(
    [
        Output('token', 'data'),
        Output('token_data', 'data'),
        Output('entity', 'data'),
        Output('page-content', 'children'),
        Output('page-title', 'children'),
    ],
    [Input('url', 'search')]
)
def display_page(url_params):
    """
    Integrates the generic function into the app callback.
    """
    token, tdata, entity_data, page_content, page_title = display_page_generic(url_params, app_title)
    return token, tdata, entity_data, page_content, page_title

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
    Combined callback for managing UI elements and the auth-div content.
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
        auth_div_content = None
    else:
        entity_details = [
            html.H1("Entity Data:"),
            html.P(f"Entity Class: {token_data['entityClass_data']}"),
            html.P(f"Entity ID: {token_data['entity_id_data']}"),
            html.P(f"Created By: {entity_data['createdby']}"),
            html.P(f"Created: {entity_data['created']}"),
            html.P(f"Modified: {entity_data['modified']}"),
        ]
        auth_div_content = dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Component Data:"),
                        html.P(f"Slider Value: {slider_val}"),
                        html.P(f"Dropdown Value: {dropdown_val}"),
                        html.P(f"Input Value: {input_val}"),
                        html.P(f"Button Clicks: {n_clicks}")
                    ]
                ),
                dbc.Col(entity_details),
            ]
        )

    return (*sidebar_state, auth_div_content)
 
if __name__ == "__main__":
    app.run_server(debug=True, port=config["PORT"], host=config["HOST"])