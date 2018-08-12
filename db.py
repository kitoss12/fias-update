import psycopg2

def get_connect(dbname, host, user, password, port):
    return psycopg2.connect(dbname = dbname, host = host, user = user, password = password, port = port)