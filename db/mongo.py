from pymongo import MongoClient
from pprint import pprint
import time

class MDB():
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/testdb')
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
