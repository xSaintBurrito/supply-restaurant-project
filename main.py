import json
from varname import nameof
from dash_table import DataTable
import flask
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px

from app import app, server

ORDER_NUMBER = 4


def render_graph():
    pantry = check_pantry()
    fig = px.bar(pantry, x="Groceries", y="Quantity")

    return fig


def update_pantry(pantry, items):
    updated_pantry = pantry.append(items)

    return updated_pantry


def check_pantry():
    # CHECK DATABASE
    pantry = pd.read_csv("Data\\Pantry.csv", sep=",")
    pantry.columns = ["Groceries", "Quantity"]

    return pantry


def check_orders():
    # CHECK DATABASE
    orders = pd.read_csv("Data\\Orders.csv", sep=",")
    orders.columns = ["Order Nr.", "Item", "Quantity"]

    return orders


def json_orders():
    # CHECK DATABASE
    orders = pd.read_csv("Data\\Orders.csv", sep=",")
    orders.columns = ["Order Nr.", "Item", "Quantity"]

    result = orders.to_json(orient="records")
    parsed_orders = json.loads(result)

    return parsed_orders


def add_to_order(new_name, new_amount, tomato, potato, carrot, lettuce, milk, flour, eggs, beef, chicken, fish,
                 t_c=False, p_c=False, c_c=False, l_c=False, m_c=False, f_c=False, e_c=False, b_c=False, chick_c=False,
                 fish_c=False):
    global ORDER_NUMBER
    orders = check_orders()
    new_order = pd.DataFrame(columns=['Order Nr.', 'Item', 'Quantity'])
    checkboxes = [t_c, p_c, c_c, l_c, m_c, f_c, e_c, b_c, chick_c, fish_c]
    amounts = [tomato, potato, carrot, lettuce, milk, flour, eggs, beef, chicken, fish]

    for checked, value in zip(checkboxes, amounts):
        if checked != False:
            name = nameof(checked)
            temp = pd.DataFrame({"Order Nr.": ORDER_NUMBER, "Item": [name.capitalize()], "Quantity": [value]})
            new_order.append(temp)

    if new_name != "" and new_amount is not None:
        temp = pd.DataFrame({"Order Nr.": ORDER_NUMBER, "Item": [new_name], "Quantity": [new_amount]})
        new_order.append(temp)

    updated_orders = orders.append(new_order)

    ORDER_NUMBER += 1
    return updated_orders


@server.route('/orders', methods=['GET'])
def send_orders():
    data = json_orders()

    return json.dumps(data, indent=4)


@server.route("/delivery", methods=["POST"])
def get_groceries():
    json_delivery = flask.request.json
    delivery = pd.read_json(json_delivery)
    pantry = check_pantry()
    updated_pantry = update_pantry(pantry, delivery)

    return updated_pantry


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
                                        dbc.InputGroupAddon(["Tomatoes", dbc.Checkbox(id="tomato_c")],
                                                            addon_type="prepend"),
                                        dbc.Input(placeholder="Amount", type="number", id="tomato"),
                                    ],
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon(["Potatoes", dbc.Checkbox(id="potato_c")],
                                                            addon_type="prepend"),
                                        dbc.Input(placeholder="Amount", type="number", id="potato"),
                                    ]
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon(["Carrots", dbc.Checkbox(id="carrot_c")],
                                                            addon_type="prepend"),
                                        dbc.Input(placeholder="Amount", type="number", id="carrot"),
                                    ],
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon(["Lettuces", dbc.Checkbox(id="lettuce_c")],
                                                            addon_type="prepend"),
                                        dbc.Input(placeholder="Amount", type="number", id="lettuce"),
                                    ]
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon(["Milks", dbc.Checkbox(id="milk_c")], addon_type="prepend"),
                                        dbc.Input(placeholder="Amount", type="number", id="milk"),
                                    ],
                                )
                            ]
                        )
                    ], width=4),
                dbc.Col(
                    [
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon(["Flours", dbc.Checkbox(id="flour_c")], addon_type="prepend"),
                                dbc.Input(placeholder="Amount", type="number", id="flour"),
                            ]
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon(["Eggs", dbc.Checkbox(id="egg_c")], addon_type="prepend"),
                                dbc.Input(placeholder="Amount", type="number", id="egg"),
                            ],
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon(["Beef", dbc.Checkbox(id="beef_c")], addon_type="prepend"),
                                dbc.Input(placeholder="Amount", type="number", id="beef"),
                            ]
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon(["Chicken", dbc.Checkbox(id="chicken_c")], addon_type="prepend"),
                                dbc.Input(placeholder="Amount", type="number", id="chicken"),
                            ],
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon(["Fish", dbc.Checkbox(id="fish_c")], addon_type="prepend"),
                                dbc.Input(placeholder="Amount", type="number", id="fish"),
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
                                                        dbc.ModalBody(
                                                            dbc.InputGroup(
                                                                [
                                                                    dbc.Input(placeholder="New product...",
                                                                              id="new_product_name", type="text",
                                                                              className="mb-3"),
                                                                    dbc.Input(placeholder="Amount",
                                                                              id="new_product_amount", type="number"),
                                                                ],
                                                            ),
                                                        ),
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
                dbc.Alert("Order placed. The supplier will be informed about the needed products", id="order_alert",
                          is_open=False, dismissable=True, style={'margin-top': '15px', 'margin-bottom': '15px'})
            ], style={'width': '100%', 'margin-top': '25px', 'margin-bottom': '50px', 'margin-right': '40px',
                      'margin-left': '40px'}),
    ]
)


@app.callback(
    Output("modal", "is_open"),
    [Input("open_form", "n_clicks"),
     Input("order", "n_clicks"),
     Input("new_product_name", "value"),
     Input("new_product_amount", "value")]
)
def toggle_modal(open_form, add_new, name, amount):
    if open_form:
        return True

    if add_new:
        orders = check_orders()
        updated_orders = orders.append({"Order Nr.": ORDER_NUMBER, "Item": [name.capitalize()], "Quantity": [amount]})
        updated_orders.set_index("Order Nr.")
        updated_orders.to_csv('Data\\Orders.csv', mode='w', header="Order Nr.,Item,Quantity")


@app.callback(
    Output("order_alert", "is_open"),
    [Input("place_order", "n_clicks"),
     Input("new_product_name", "value"),
     Input("new_product_amount", "value"),
     Input("tomato", "value"),
     Input("potato", "value"),
     Input("carrot", "value"),
     Input("lettuce", "value"),
     Input("milk", "value"),
     Input("flour", "value"),
     Input("egg", "value"),
     Input("beef", "value"),
     Input("chicken", "value"),
     Input("fish", "value")],
    [State("order_alert", "is_open"),
     State("tomato_c", "checked"),
     State("potato_c", "checked"),
     State("carrot_c", "checked"),
     State("lettuce_c", "checked"),
     State("milk_c", "checked"),
     State("flour_c", "checked"),
     State("egg_c", "checked"),
     State("beef_c", "checked"),
     State("chicken_c", "checked"),
     State("fish_c", "checked")]
)
def send_orders(clicked, new_name, new_amount, tomato, potato, carrot, lettuce, milk, flour, eggs, beef,
                chicken, fish, is_open, t_c, p_c, c_c, l_c, m_c, f_c, e_c, b_c, chick_c, fish_c):
    if clicked:
        updated_orders = add_to_order(new_name, new_amount, tomato, potato, carrot, lettuce, milk, flour, eggs, beef,
                                      chicken, fish, t_c, p_c, c_c, l_c, m_c, f_c, e_c, b_c, chick_c, fish_c)
        updated_orders = updated_orders.set_index("Order Nr.")
        updated_orders.to_csv('Data\\Orders.csv', mode='w', header="Order Nr.,Item,Quantity")
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
    app.run_server(debug=True, port=8051)
