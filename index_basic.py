from dash import html, dcc, Input, Output, State
from generic_bfabric import app
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

documentation_content = [
    html.H2("Documentation"),
    html.P("Describe your app's features here.")
]

app.layout = get_static_layout(
    app_title,  
    app_specific_layout,  
    documentation_content  
)

@app.callback(
    Output('user-display', 'children'),
    Input('token_data', 'data'),
    State('app_data', 'data')
)
def update_user_display(token_data, app_data):
    if token_data and app_data:
        user_name = token_data.get("user_data", "Unknown User")
        app_name = app_data.get("name", "Unknown App")
        app_description = app_data.get("description", "Unknown App")
        
        L = get_logger(token_data)
        L.log_operation("User Login", "User logged in successfully.")

        return html.Div([
            html.P(f"User {user_name} has successfully logged in!"),
            html.Br(),
            html.P(f"Application Name: {app_name}"),
            html.P(f"Application Description: {app_description}")
        ])

    else:
        return "Please log in."

if __name__ == "__main__":
    app.run_server(debug=False, port=PORT, host=HOST)
