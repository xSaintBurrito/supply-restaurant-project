import json
import flask
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px


from app import app, server


def render_graph():
    pantry = check_pantry()
    fig = px.bar(pantry, x="Groceries", y="Quantity")
    # color="In progress" Could be added as already have and order in progress

    return fig


def check_pantry():
    pantry = pd.read_csv("Data\\Pantry.csv", sep=",")
    pantry.columns = ["Groceries", "Quantity"]

    #result = pantry.to_json(orient="records")
    #parsed_pantry = json.loads(result)

    return pantry


def json_orders():
    orders = pd.read_csv("Data\\Orders.csv", sep=",")
    orders.columns = ["Order Nr.", "Item", "Quantity"]

    result = orders.to_json(orient="records")
    parsed_orders = json.loads(result)

    return parsed_orders


@server.route('/orders', methods=['GET'])
def send_orders():
    data = json_orders()
    return json.dumps(data, indent=4)


@server.route("/delivery", methods=["POST"])
def get_groceries():
    json_delivery = flask.request.json
    delivery = pd.read_json(json_delivery)
    pantry = check_pantry()
    return "JSON value sent: " + json_delivery


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(html.Img(src=app.get_asset_url("logo.png"), height="50px", width="auto", className="ml-2")),
    ],
    brand="Internet Applications Programming",
    color="info",
    dark=True
)

header = dbc.Card(
    dbc.Row(
        [
            html.H1("Simple Restaurant", className="display-3")
        ],
        justify="center",
    )
)


pantry = dbc.Card(
    dbc.Row(
        [
            html.H1("Dynamically rendered tab content"),
            dcc.Graph(id='example-graph', figure=render_graph())
        ],
        justify="center",
    )
)

orders = dbc.Card(
    dbc.Row(
        [
            html.H1("Orders"),
        ],
        justify="center",
    )
)

app.layout = html.Div([
    navbar,
    dbc.Container([
        html.Div(header, id='header_div'),
        html.Div(pantry, id='pantry_div'),
        html.Div(orders, id='orders_div'),
            ]
        )
    ])


if __name__ == "__main__":
    app.run_server()
