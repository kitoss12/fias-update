import sys
import xml.etree.ElementTree as ET
import arguments
import fias
import db

source = arguments.args.source

count = 0
update_count = 0
insert_count = 0

for event, elem in ET.iterparse(source):
    if elem.tag == "Object":
        count = count + 1
        fias_item = elem.attrib
        update_type = fias.update_addobj(fias_item)
        if update_type == fias.UPDATE_TYPE['INSERT']:
            insert_count = insert_count + 1
        elif update_type == fias.UPDATE_TYPE['UPDATE']:
            update_count = update_count + 1
        sys.stdout.write("\r" + "Total: {c}, Updated: {u}, Inserted: {i}".format(c=count, u=update_count, i=insert_count))
        sys.stdout.flush()
        elem.clear()

db.conn.commit()
db.cur.close()
db.conn.close()
