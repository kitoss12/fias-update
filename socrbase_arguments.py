import argparse

parser = argparse.ArgumentParser(description='Read XML file and update fias database (socrbase table)')

parser.add_argument('source', help='source of file')
parser.add_argument('-n', help='the database name')
parser.add_argument('-a', help='database host address')
parser.add_argument('-u', help='user name used to authe nticate in db connection')
parser.add_argument('-s', help='password used to authenticate in db connection')
parser.add_argument('-p', help=' connection port number (defaults to 5432 if not provided)')
 
args = parser.parse_args()