import db

cur = db.cur

def get_params_by_fias_item(fias_item):
    return {
        'aoid': fias_item.get('AOID'),
        'aoguid': fias_item.get('AOGUID'),
        'parentguid': fias_item.get('PARENTGUID'),
        'nextid': fias_item.get('NEXTID'),
        'formalname': fias_item.get('FORMALNAME'),
        'offname': fias_item.get('OFFNAME'),
        'shortname': fias_item.get('SHORTNAME'),
        'aolevel': fias_item.get('AOLEVEL'),
        'regioncode': fias_item.get('REGIONCODE'),
        'areacode': fias_item.get('AREACODE'),
        'autocode': fias_item.get('AUTOCODE'),
        'citycode': fias_item.get('CITYCODE'),
        'ctarcode': fias_item.get('CTARCODE'),
        'placecode': fias_item.get('PLACECODE'),
        'plancode': fias_item.get('PLANCODE'),
        'streetcode': fias_item.get('STREETCODE'),
        'extrcode': fias_item.get('EXTRCODE'),
        'sextcode': fias_item.get('SEXTCODE'),
        'plaincode': fias_item.get('PLAINCODE'),
        'code': fias_item.get('CODE'),
        'currstatus': fias_item.get('CURRSTATUS'),
        'actstatus': fias_item.get('ACTSTATUS'),
        'livestatus': fias_item.get('LIVESTATUS'),
        'centstatus': fias_item.get('CENTSTATUS'),
        'operstatus': fias_item.get('OPERSTATUS'),
        'ifnsfl': fias_item.get('IFNSFL'),
        'ifnsul': fias_item.get('IFNSUL'),
        'terrifnsfl': fias_item.get('TERRIFNSFL'),
        'terrifnsul': fias_item.get('TERRIFNSUL'),
        'okato': fias_item.get('OKATO'),
        'oktmo': fias_item.get('OKTMO'),
        'postalcode': fias_item.get('POSTALCODE'),
        'startdate': fias_item.get('STARTDATE'),
        'enddate': fias_item.get('ENDDATE'),
        'updatedate': fias_item.get('UPDATEDATE'),
        'divtype': fias_item.get('DIVTYPE')
    }

def update_addobj(fias_item):
    formatted_item = get_params_by_fias_item(fias_item)
    aoid = formatted_item['aoid']
    cur.execute("SELECT * FROM addrobj WHERE aoid = %s", (aoid,))
    res = cur.fetchone()
    if res == None:
        cur.execute(""" 
        INSERT INTO addrobj(""" + ",".join(formatted_item.keys()) + """)
        VALUES (""" + ",".join(map(lambda x: '%(' + x + ')s' ,formatted_item.keys())) + """)""", formatted_item)
    else:
        cur.execute(""" 
        UPDATE addrobj SET (""" + ",".join(formatted_item.keys()) + """) 
        = (""" + ",".join(map(lambda x: '%(' + x + ')s' ,formatted_item.keys())) + """)
        WHERE aoid = %(aoid)s""", formatted_item)
