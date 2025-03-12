# Ensure version compatibility between bfabric_web_apps and bfabric_web_app_template.
# Both must be the same version to avoid compatibility issues.
# Example: If bfabric_web_apps is version 0.1.3, bfabric_web_app_template must also be 0.1.3.
# Verify and update versions accordingly before running the application.



from dash import html, dcc, Input, Output, State
from generic.callbacks import app
from bfabric_web_apps import get_static_layout, get_logger, HOST, PORT
import dash_bootstrap_components as dbc

app_title = "My B-Fabric App (Basic)"

app_specific_layout = dbc.Row([
    dbc.Col(
        html.Div(style={"border-right": "2px solid #d4d7d9","height": "70vh","padding": "20px"}),
        width=3,  # Width of the sidebar column.
    ),
    dbc.Col([
        html.H1("Welcome to The Sample B-Fabric App", style={"margin": "2vh 0 2vh 0"}),
        html.Div(id='user-display', style={"margin": "2vh 0 2vh 0"}),
    ], width=9)
])

documentation_content = [html.H2("Documentation"),html.P("Describe your app's features here.")]

app.layout = get_static_layout(app_title, app_specific_layout, documentation_content, layout_config={"bug":True})

@app.callback(
    [Output('user-display', 'children'),Output('submit-bug-report', 'disabled')],
    [Input('token_data', 'data')],
    [State('app_data', 'data')]
)
def update_user_display(token_data, app_data):
    if token_data and app_data:
        try:
            user_name = token_data.get("user_data", "Unknown User")
            app_name = app_data.get("name", "Unknown App")
            app_description = app_data.get("description", "Unknown App")
            
            L = get_logger(token_data)
            L.log_operation("User Login", "User logged in successfully.")

            return html.Div([
                html.P(f"User {user_name} has successfully logged in!"), html.Br(),
                html.P(f"Application Name: {app_name}"),
                html.P(f"Application Description: {app_description}")
            ]), False
        except Exception as e:
            return html.P(f"Error Logging into B-Fabric: {str(e)}"), True

    else:
        return "Please log in.", True

if __name__ == "__main__":
    app.run_server(debug=False, port=PORT, host=HOST)
