import xml.etree.ElementTree as ET
import arguments
import fias
import db

source = arguments.args.source

count = 0

for event, elem in ET.iterparse(source):
    if elem.tag == "Object":
        count = count + 1
        fias_item = elem.attrib
        fias.update_addobj(fias_item)
        print(count)
        elem.clear()

db.conn.commit()
db.cur.close()
db.conn.close()
