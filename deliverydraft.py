import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlite3
from sqlite3 import Error
import dash_table
import pandas as pd
import urllib
from dash.dependencies import Input, Output, State
from flask import Flask
import dash_bootstrap_components as dbc

header = dbc.Card(
    dbc.Row(
        [
            html.H1("Simple Restaurant", className="display-3")
        ],
        justify="center",
    )
)


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


df = pd.read_sql("select * from Orders_rest", con)

df = df[['id', 'product', 'quantity']]

df.head(1)

app.layout = html.Div([
    dash_table.DataTable(
    id='table-sorting-filtering',
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto'
    },
    style_table={
        'maxHeight': '800px'
        ,'overflowY': 'scroll'
    },
    columns=[
        {'name': i, 'id': i} for i in df.columns
    ],
    page_current= 0,
    page_size= 200,
    page_action='custom',
filter_action='custom',
    filter_query='',
sort_action='custom',
    sort_mode='multi',
    sort_by=[]
)
])# end div

operators = [['ge ', '>='],
['le ', '<='],
['lt ', '<'],
['gt ', '>'],
['ne ', '!='],
['eq ', '='],
['contains '],
['datestartswith ']]

def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]
                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part
# word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value
    return [None] * 3

@app.callback(
    Output('table-sorting-filtering', 'data'),
    [Input('table-sorting-filtering', "page_current"),
     Input('table-sorting-filtering', "page_size"),
     Input('table-sorting-filtering', 'sort_by'),
     Input('table-sorting-filtering', 'filter_query')])
def update_table(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = df
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)
        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
         # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]
    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )
    page = page_current
    size = page_size
    return dff.iloc[page * size: (page + 1) * size].to_dict('records')

#html button 

#app.layout = html.Div([
#    html.Div(dcc.Input(id='input-on-submit', type='text')),
#    html.Button('Submit', id='submit-val', n_clicks=0),
#    html.Div(id='container-button-basic',
#            children='Enter a value and press submit')
#])


#@app.callback(
#    dash.dependencies.Output('container-button-basic', 'children'),
#    [dash.dependencies.Input('submit-val', 'n_clicks')],
#    [dash.dependencies.State('input-on-submit', 'value')])
#def update_output(n_clicks, value):
#    return 'The input value was "{}" and the button has been clicked {} times'.format(
#        value,
#        n_clicks
#    )



#sql_table(con)
#rows = sql_fetch(con)
#sql_insert_order(con)


if __name__ == '__main__':
    app.run_server(debug=True)