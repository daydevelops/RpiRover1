from pymongo import MongoClient
from pprint import pprint
import time

class MDB():
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/robotdb')
        self.db = self.client.robotLogs

    def readLog(self,table):
        if table=='socket':
            res = self.db.socketLogs.find()
        elif table=='sensor':
            res = self.db.sensorLogs.find()
        else:
            print "table not recognized"
        return (res)

    def log(self,table,data):
        if table=='socket':
            res = self.db.socketLogs.insert_one(data)
        elif table=='sensor':
            res = self.db.sensorLogs.insert_one(data)
        else:
            print "table not recognized"
        # pprint(res.inserted_id)

    def getTrimValues(self):
        left_trim = self.db.robotProperties.find_one({'property':'left_trim'},{'value':1,'_id':0})['value']
        right_trim = self.db.robotProperties.find_one({'property':'right_trim'},{'value':1,'_id':0})['value']
        return {'L':left_trim,'R':right_trim}

    def updateTrimValues(self):
        pass
