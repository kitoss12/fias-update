import sys
import xml.etree.ElementTree as ET
import addrobj_arguments as arguments
import fias
import db

source = arguments.args.source
args = arguments.args

connect = db.get_connect(
    dbname = args.n, host = args.a, user = args.u, password = args.s, port = args.p
)

cursor = connect.cursor()

count = 0

for event, elem in ET.iterparse(source):
    if elem.tag == "Object":
        count = count + 1
        fias_item = elem.attrib
        fias.delete_addrobj_item_by_aoid(cursor, fias_item.get('AOID'))
        sys.stdout.write("\r" + "Deleted: {c}".format(c=count))
        sys.stdout.flush()
        elem.clear()

connect.commit()
cursor.close()
connect.close()        