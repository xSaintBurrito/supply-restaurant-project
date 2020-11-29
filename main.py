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
                    html.H1("Current Orders", style={'textAlign': 'center'}),
                    DataTable(
                        data=check_orders().to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in check_orders().columns],
                        style_table={'width': '70%', 'overflowX': 'scroll'},
                        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
                        style_cell={'textAlign': 'center'},
                        style_cell_conditional=
                        [
                            {'if': {'column_id': 'Order Nr.'}, 'width': '20%'},
                            {'if': {'column_id': 'Quantity'}, 'width': '20%'}
                        ]
                    )
                ], width=4),
            dbc.Col(
                [
                    html.H1("Pantry Analysis", style={'textAlign': 'center'}),
                    dcc.Graph(id='example-graph', figure=render_graph())
                ], width=8),
        ],
        justify="between",
    )
)

orders = dbc.Card(
    html.H1("Orders", style={'textAlign': 'center'}),
)

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
