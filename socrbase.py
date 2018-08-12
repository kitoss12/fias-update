import sys
import socrbase_arguments as arguments
import db
import fias
import xml.etree.ElementTree as ET

source = arguments.args.source
args = arguments.args

connect = db.get_connect(
    dbname = args.n,
    host = args.a,
    user = args.u,
    password = args.s,
    port = args.p
)

cursor = connect.cursor()

count_of_deleted_items = fias.delete_socrbase_items(cursor)

count_of_added_items = 0

for event, elem in ET.iterparse(source):
    if elem.tag == "AddressObjectType":
        count_of_added_items = count_of_added_items + 1
        socrbase_item = elem.attrib
        fias.add_socrbase_item(cursor, socrbase_item)
        sys.stdout.write("\r" + "Deleted: {c}, Inserted: {i}".format(c=count_of_deleted_items, i=count_of_added_items))
        sys.stdout.flush()
        elem.clear()

connect.commit()
cursor.close()
connect.close()