import arguments
import psycopg2
args = arguments.args
conn = psycopg2.connect(dbname = args.n, host = args.a, user = args.u, password = args.s, port = args.p)

cur = conn.cursor()
