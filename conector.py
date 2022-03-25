import mysql.connector as myql

con = myql.connect (host='localhost', database='Nome do banco', user='boot', password='')

if (con.is_connectes()):
    db_info = con,get_server_info()
    print
