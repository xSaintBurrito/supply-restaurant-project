import json

from dash_table import DataTable
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

    return pantry


def check_orders():
    orders = pd.read_csv("Data\\Orders.csv", sep=",")
    orders.columns = ["Order Nr.", "Item", "Quantity"]

    return orders


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
    brand="Simple Restaurant",
    color="info",
    dark=True
)

pantry = dbc.Card(
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H1("Current Orders", style={'textAlign': 'center', 'margin-top': '10px'}),
                    html.Br(),
                    dbc.Row(
                        [
                            DataTable(
                                data=check_orders().to_dict('records'),
                                columns=[{'id': c, 'name': c} for c in check_orders().columns],
                                style_table={'width': '90%', 'margin-top': '35px'},
                                style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
                                style_cell={'textAlign': 'center'}
                            )
                        ], justify="center", align="center", className="h-50"
                    )
                ], width=5),
            dbc.Col(
                [
                    html.H1("Pantry Analysis", style={'textAlign': 'center', 'margin-top': '10px'}),
                    dcc.Graph(id='example-graph', figure=render_graph())
                ], width=7),
        ],
        justify="between",
    )
)

orders = dbc.Card(
    [
        dbc.Row(html.H1("Make an order", style={'textAlign': 'center', 'margin-top': '10px', 'margin-bottom': '25px'}),
                justify="center", align="center", className="h-50"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon(["Tomatoes", dbc.Checkbox()], addon_type="prepend"),
                                        dbc.Input(placeholder="Amount", type="number"),
                                    ],
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon(["Potatoes", dbc.Checkbox()], addon_type="prepend"),
                                        dbc.Input(placeholder="Amount", type="number"),
                                    ]
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon(["Carrots", dbc.Checkbox()], addon_type="prepend"),
                                        dbc.Input(placeholder="Amount", type="number"),
                                    ],
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon(["Lettuces", dbc.Checkbox()], addon_type="prepend"),
                                        dbc.Input(placeholder="Amount", type="number"),
                                    ]
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon(["Milks", dbc.Checkbox()], addon_type="prepend"),
                                        dbc.Input(placeholder="Amount", type="number"),
                                    ],
                                )
                            ]
                        )
                    ], width=4),
                dbc.Col(
                    [
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon(["Flours", dbc.Checkbox()], addon_type="prepend"),
                                dbc.Input(placeholder="Amount", type="number"),
                            ]
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon(["Eggs", dbc.Checkbox()], addon_type="prepend"),
                                dbc.Input(placeholder="Amount", type="number"),
                            ],
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon(["Beef", dbc.Checkbox()], addon_type="prepend"),
                                dbc.Input(placeholder="Amount", type="number"),
                            ]
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon(["Chicken", dbc.Checkbox()], addon_type="prepend"),
                                dbc.Input(placeholder="Amount", type="number"),
                            ],
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon(["Fish", dbc.Checkbox()], addon_type="prepend"),
                                dbc.Input(placeholder="Amount", type="number"),
                            ]
                        )
                    ], width=4),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H4("Your product isn't listed?", className="card-title"),
                                        html.P(
                                            "No Problem! We can deliver anything after "
                                            "filling the order form listed below.",
                                            className="card-text",
                                        ),
                                        html.Div(
                                            [
                                                dbc.Button("Open Form", id="open_form"),
                                                dbc.Modal(
                                                    [
                                                        dbc.ModalHeader("Order Form"),
                                                        dbc.ModalBody("This is the content of the modal"),
                                                        dbc.ModalFooter(
                                                            dbc.Button("Order!", id="order", className="ml-auto",
                                                                       block=True)
                                                        ),
                                                    ],
                                                    id="modal",
                                                ),
                                            ]
                                        )
                                    ]
                                ),
                            ],
                        )
                    ], width=4)
            ],
            justify="between", style={'margin-right': '25px', 'margin-left': '25px'}
        ),
        dbc.Row(
            [
                dbc.Button("Place Order", id="place_order", color="info", block=True),
                dbc.Alert("Order placed. The supplier will be informed about the needed roducts", id="order_alert",
                          is_open=False, dismissable=True, style={'margin-top': '15px', 'margin-bottom': '15px'})
            ], style={'width': '100%', 'margin-top': '25px', 'margin-bottom': '50px', 'margin-right': '40px', 'margin-left': '40px'}),
    ]
)


@app.callback(
    Output("modal", "is_open"),
    [Input("open_form", "n_clicks"), Input("order", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open


@app.callback(
    Output("order_alert", "is_open"),
    Input("place_order", "n_clicks"),
    State("order_alert", "is_open")
)
def send_orders(clicked, is_open):
    if clicked:
        return not is_open
    return is_open


app.layout = html.Div([
    navbar,
    dbc.Container(
        [
            html.Div(pantry, id='pantry_div'),
            html.Div(orders, id='orders_div'),
        ]
    )
])

if __name__ == "__main__":
    app.run_server()
