import sys
sys.path.append(r"C:\Users\marc_\Documents\Git\bfabric-web-apps")
from dash import html, dcc, Input, Output, State
from generic_bfabric import app
from bfabric_web_apps import (
    get_static_layout,
    get_logger,
    HOST, 
    PORT,
    DEV)


app_title = "My B-Fabric App (Basic)"

app_specific_layout = html.Div([
    html.H1("Welcome to My B-Fabric App"),
    html.P("This is a quickstart example using bfabric-web-apps."),
    html.Div(id='user-display')
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
    State('entity', 'data')
)
def update_user_display(token_data, entity_data):
    if token_data and entity_data:
        user_name = token_data.get("user_data", "Unknown User")  
        
        L = get_logger(token_data)
        L.log_operation("User Login", "User logged in successfully.")
        
        return f"User {user_name} is logged in successfully!"
    else:
        return "Please log in."

if __name__ == "__main__":
    app.run_server(debug=False, port=PORT, host=HOST)
