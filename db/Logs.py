from tinydb import TinyDB, Query
from pprint import pprint
import time

class Logs():
    def __init__(self):
        pass
        # print 'Database ready'

    def getTrimValues(self):
        rp_db = TinyDB('db/data/robotProperties.json')
        left_trim = rp_db.search(Query().property=='left_trim')[0]['value']
        right_trim = rp_db.search(Query().property=='right_trim')[0]['value']
        return {'L':left_trim,'R':right_trim}


    def updateTrimValues(self,ltrim,rtrim):
        rp_db = TinyDB('db/data/robotProperties.json')
        rp_db.update({'value': ltrim}, Query().property=='left_trim')
        rp_db.update({'value': rtrim}, Query().property=='right_trim')

    # def log(table,data):
    #     if table=='socket':
    #         socket_db = TinyDB('db/data/robotProperties.json')
    #         res = socket_db.insert()
    #     elif table=='sensor':
    #         res = self.db.sensorLogs.insert_one(data)
    #     else:
    #         print "table not recognized"
    #     pprint(res.inserted_id)
