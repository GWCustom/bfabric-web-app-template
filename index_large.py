# Ensure version compatibility between bfabric_web_apps and bfabric_web_app_template.
# Both must be the same version to avoid compatibility issues.
# Example: If bfabric_web_apps is version 0.1.3, bfabric_web_app_template must also be 0.1.3.
# Verify and update versions accordingly before running the application.



from dash import Input, Output, State, html, dcc
import dash_bootstrap_components as dbc
import bfabric_web_apps
from generic.callbacks import app
from generic.components import no_auth
from pathlib import Path

bfabric_web_apps.CONFIG_FILE_PATH = "~/.bfabricpy.yml"
bfabric_web_apps.DEVELOPER_EMAIL_ADDRESS = "griffin@gwcustom.com"
bfabric_web_apps.BUG_REPORT_EMAIL_ADDRESS = "gwtools@fgcz.system"

dropdown_options = ['Genomics (project 2220)', 'Proteomics (project 3000)', 'Metabolomics (project 31230)']
dropdown_values = ['2220', '3000', '31230']

# Here we define the sidebar of the UI, including the clickable components like dropdown and slider. 
sidebar = [
    html.P(id="sidebar_text", children="How Many Resources to Create?"),  # Sidebar header text.
    dcc.Slider(0, 10, 1, value=4, id='example-slider'),  # Slider for selecting a numeric value.
    html.Br(),
    html.P(id="sidebar_text_2", children="For Which Internal Unit?"),
    dcc.Dropdown(
        options=[{'label': option, 'value': value} for option, value in zip(dropdown_options, dropdown_values)],
        value=dropdown_options[0],
        id='example-dropdown'  # Dropdown ID for callback integration.
    ),
    html.Br(),
    dbc.Input(value='Content of Resources', id='example-input'),  # Text input field.
    html.Br(),
    dbc.Button('Submit', id='example-button'),  # Button for user submission.
]

# here we define the modal that will pop up when the user clicks the submit button.
modal = html.Div([
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Ready to Prepare Create Workunits?")),
        dbc.ModalBody("Are you sure you're ready to create workunits?"),
        dbc.ModalFooter(dbc.Button("Yes!", id="Submit", className="ms-auto", n_clicks=0)),],
    id="modal-confirmation",
    is_open=False,),
])

# Here are the alerts which will pop up when the user creates workunits 
alerts = html.Div(
    [
        dbc.Alert("Success: Workunit created!", color="success", id="alert-fade-success", dismissable=True, is_open=False),
        dbc.Alert("Error: Workunit creation failed!", color="danger", id="alert-fade-fail", dismissable=True, is_open=False),
    ], style={"margin": "20px"}
)

# Here we define a Dash layout, which includes the sidebar, and the main content of the app. 
app_specific_layout = dbc.Row(
        id="page-content-main",
        children=[
            dcc.Loading(alerts), 
            modal,  # Modal defined earlier.
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

# Here we define the documentation content for the app.
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
            "It is a simple application which allows you to bulk-create resources, "
            "workunits, and demonstrates how to use the bfabric-web-apps library."
        ]
    ),
    html.Br(),
    html.P(
        [
            "Please check out the official documentation of ",
            html.A("Bfabric Web Apps", href="https://bfabric-docs.gwc-solutions.ch/index.html"),
            "."
        ]
    )
]

app_title = "Bfabric App Template"

# here we use the get_static_layout function from bfabric_web_apps to set up the app layout.
app.layout = bfabric_web_apps.get_static_layout(         # The function from bfabric_web_apps that sets up the app layout.
    app_title,                          # The app title we defined previously
    app_specific_layout,     # The main content for the app defined in components.py
    documentation_content,    # Documentation content for the app defined in components.py
    layout_config={"workunits": True, "queue": False, "bug": True}  # Configuration for the layout
)

# This callback is necessary for the modal to pop up when the user clicks the submit button.
@app.callback(
    Output("modal-confirmation", "is_open"),
    [Input("example-button", "n_clicks"), Input("Submit", "n_clicks")],
    [State("modal-confirmation", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# This callback updates the UI based on the user's authentication status and the entity data.
@app.callback(
    [
        Output('sidebar_text', 'hidden'),
        Output('example-slider', 'disabled'),
        Output('example-dropdown', 'disabled'),
        Output('example-input', 'disabled'),
        Output('example-button', 'disabled'),
        Output('submit-bug-report', 'disabled'),
        Output('Submit', 'disabled'),
        Output('auth-div', 'children'),
    ],
    [
        Input('example-slider', 'value'),
        Input('example-dropdown', 'value'),
        Input('example-input', 'value'),
        Input('token_data', 'data'),
    ],
    [State('entity', 'data')]
)
def update_ui(slider_val, dropdown_val, input_val, token_data, entity_data):

    # Determine sidebar and input states based on token_data and development mode.
    if token_data is None:
        sidebar_state = (True, True, True, True, True, True, True)
    elif not bfabric_web_apps.DEV:
        sidebar_state = (False, False, False, False, False, False, False)
    else:
        sidebar_state = (True, True, True, True, True, True, True)

    # Generate content for the auth-div based on authentication and entity data.
    if not entity_data or not token_data:
        auth_div_content = html.Div(children=no_auth)
    else:
        try:
            component_data = [
                html.H1("Component Data:"),
                html.P(f"Number of Resources to Create: {slider_val}"),
                html.P(f"Create workunit inside project: {dropdown_val}"),
                html.P(f"Resource Content: {input_val}")
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

        except Exception as e:
            return (*sidebar_state, html.P(f"Error Logging into B-Fabric: {str}"))

    return (*sidebar_state, auth_div_content)


# This callback creates workunits and resources based on the user's input, and displays the corresponding alert, based on success or failure.
@app.callback(
    [
        Output("alert-fade-success", "is_open"), 
        Output("alert-fade-fail", "is_open"), 
        Output("alert-fade-fail", "children"),
        Output("refresh-workunits", "children")
    ],
    [Input("Submit", "n_clicks")],
    [
        State("example-slider", "value"),
        State("example-dropdown", "value"),
        State("example-input", "value"),
        State("token_data", "data"),
    ],
    prevent_initial_call=True
)
def create_resources(n_clicks, slider_val, dropdown_val, input_val, token_data):

    app_id = token_data.get("application_data", None) 
    container_id = int(dropdown_val)

    if n_clicks:
        try: 
            workunit_id = bfabric_web_apps.create_workunit(
                token_data, "Bfabric App Template", "Bfabric App Template Workunit", app_id, container_id
            )
            for i in range(slider_val):
                file_path = Path(f"resource_example_{i}.txt")
                file_path.write_text(input_val)
                try:
                    bfabric_web_apps.create_resource(token_data, workunit_id, file_path)
                finally: 
                    file_path.unlink(missing_ok=True)
            return True, False, None, html.Div()
        except Exception as e:
            return False, True, f"Error: Workunit creation failed: {str(e)}", html.Div()


# Here we run the app on the specified host and port.
if __name__ == "__main__":
    app.run_server(debug=False, port=bfabric_web_apps.PORT, host=bfabric_web_apps.HOST)

