from tinydb import TinyDB, Query
from pprint import pprint
import time

class Logs():
    def __init__(self):
        self.cc_logs = "" # buffer for db
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

    def log(self,table,data):
        if table=='controllerCommands':
            if self.cc_logs!="":
                self.cc_logs += ','+data
            else:
                self.cc_logs += data

            if len(self.cc_logs)>200:
                print "dumping"
                cc_db = TinyDB('db/data/controllerCommands.json')
                cc_db.insert(self.cc_logs)
                self.cc_logs = ""
