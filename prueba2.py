import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlite3
from sqlite3 import Error

def sql_connection(): 
    try:

        con = sqlite3.connect('/Users/UX490/Desktop/FlaskFrontend/orders.db')

        print("Connection is established: Database is created in memory")

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE Orders_deliv(id integer PRIMARY KEY, product text, prize real, rider text)")

    con.commit()

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('Select id from Orders_rest')

    rows = cursorObj.fetchall()

    for row in rows: 
        print(row)
    return rows
    print("End of the database")

def sql_insert_order(con):

    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO orders_rest VALUES(null, 'ice cream', 4)")

    con.commit()

con = sql_connection()

app = dash.Dash()

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  


app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Delivery',
                        className='nine columns'),
                html.Img(
                   src="http://test.fulcrumanalytics.com/wp-content/uploads/2015/10/Fulcrum-logo_840X144.png",
                    className='three columns',
                    style={
                        'height': '9%',
                        'width': '9%',
                        'float': 'right',
                        'position': 'relative',
                        'margin-top': 10,
                    },
                ),
                html.Div(children='''
                        Delivery page for Sam's restaurant.
                        ''',
                        className='nine columns'
                )
            ], className="row"
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose your order:'),
                        dcc.Checklist(
                                id = 'Orders',
                                options=[
                                    {'label': 'burger', 'value': 'burger'},
                                    {'label': 'fries', 'value': 'fries'}, 
                                    {'label': 'salad', 'value': 'salad'}, 
                                    {'label': 'ice cream', 'value': 'ice cream'}
                                ],
                                value=['burger', 'fries', 'salad', 'ice cream'],
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
            ], className="row"
        ),

        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='orders'
                )
                ], className= 'six columns'
                ),

                html.Div([
                dcc.Graph(
                    id='nº of orders by product each week',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'burger'},
                            {'x': [2, 3, 4], 'y': [2, 2, 4], 'type': 'line', 'name': u'fries'},
                            {'x': [4, 5, 6], 'y': [2, 9, 8], 'type': 'line', 'name': u'salad'},
                            {'x': [5, 6, 7], 'y': [1, 3, 8], 'type': 'line', 'name': u'ice cream'},
                        ],
                        'layout': {
                            'title': 'nº of orders by prod each week'
                        }
                    }
                )
                ], className= 'six columns'
                )
            ], className="row"
        )
    ], className='ten columns offset-by-one')
)

@app.callback(
    dash.dependencies.Output('orders', 'figure'),
    [dash.dependencies.Input('Orders', 'value')])
def update_image_src(selector):
    data = []
    print("Me meto en la funcion update")
    rows = sql_fetch(con)
    for row in rows:
        print("Me meto en el for")
        print(row)
        if row == 1:
            data.append({'x': [row], 'y': [4], 'type': 'bar', 'name': 'burger'})
        if row == 2:
            data.append({'x': [row], 'y': [1], 'type': 'bar', 'name': u'fries'})
        if row == 3:
            data.append({'x': [row], 'y': [2], 'type': 'bar', 'name': 'salad'})
        if row == 4:
            data.append({'x': [row], 'y': [5], 'type': 'bar', 'name': 'ice cream'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Orders',
            'xaxis' : dict(
                title='product id',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='total number of orders',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(dash.dependencies.Output('nº of orders by product each week', 'figure'), [dash.dependencies.Input('Orders', 'id')])
def update_image_src2(selector):
    data = []
     
    if 'burger' in selector:
        data.append({'x': [1], 'y': [4], 'type': 'line', 'name': 'burger'})
    if 'fries' in selector:
        data.append({'x': [2], 'y': [2], 'type': 'line', 'name': u'fries'})
    if 'salad' in selector:
        data.append({'x': [3], 'y': [1], 'type': 'line', 'name': u'salad'})
    if 'ice cream' in selector:
        data.append({'x': [4], 'y': [5], 'type': 'line', 'name': u'salad'})
    figure = {
        'data': data,
        'layout': {
            'title': 'number of orders',
            'xaxis' : dict(
                title='products',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='nº of orders by product each week',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

#sql_table(con)
sql_fetch(con)
#sql_insert_order(con)

if __name__ == '__main__':
    app.run_server(debug=True)