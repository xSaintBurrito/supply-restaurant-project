import pyodbc
import pandas as pd


def get_data_from_database(server, database, username, password):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server +
                          ';DATABASE=' + database +
                          ';UID=' + username +
                          ';PWD=' + password)
    sql = 'SELECT * FROM database_name.table'
    cursor = conn.cursor()
    cursor.execute(sql)
    data = pd.read_sql(sql, conn)

    return data
