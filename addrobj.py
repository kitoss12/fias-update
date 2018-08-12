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
update_count = 0
insert_count = 0
delete_count = 0
skip_count = 0

for event, elem in ET.iterparse(source):
    if elem.tag == "Object":
        count = count + 1
        fias_item = elem.attrib
        update_type = fias.update_addobj(cursor, fias_item)
        if update_type == fias.UPDATE_TYPE['INSERT']:
            insert_count = insert_count + 1
        elif update_type == fias.UPDATE_TYPE['UPDATE']:
            update_count = update_count + 1
        elif update_type == fias.UPDATE_TYPE['SKIP']:
            skip_count = skip_count + 1
        sys.stdout.write("\r" + "Total: {c}, Skip: {s}, Updated: {u}, Inserted: {i}".format(c=count, s=skip_count, u=update_count, i=insert_count))
        sys.stdout.flush()
        elem.clear()

delete_count = fias.delete_historical_addobj_items(cursor)

sys.stdout.write("\r"
 + "Total: {c}, Skip: {s}, Updated: {u}, Inserted: {i}, Deleted: {d}"
 .format(c=count, s=skip_count, u=update_count, i=insert_count, d=delete_count))
sys.stdout.flush()

connect.commit()
cursor.close()
connect.close()
