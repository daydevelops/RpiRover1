# this script will be used to initialize assets for the robot

# set up the db collections
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/robotdb')
db = client.robotLogs
print ('mongodb collection robotLogs initialized')

# robotProperties table
db.robotProperties.insert_many([
    {
        'property':'left_trim',
        'value':0
    },{
        'property':'right_trim',
        'value':0
    }
])
print ('robot properties collection initialized')
