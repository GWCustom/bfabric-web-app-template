from dash import Input, Output, State, html, dcc
import dash_bootstrap_components as dbc
import dash
import sys

sys.path.append("../bfabric-web-apps") 
from bfabric_web_apps.layouts.layouts import get_layout_with_sidebar 

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

# app.layout = get_layout_with_sidebar() # TODO, this function actually needs to return an html.Div object or some dash components to work corectly. 