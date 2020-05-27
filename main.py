from pymongo import MongoClient

url = 'mongodb://patrick:voxmflr1234@ds149593.mlab.com:49593/heroku_33krt5nm?retryWrites=false'
client = MongoClient(url)
db = client['heroku_33krt5nm']
collection = db['test']

collection.insert_one({'a':'b'})

rows = collection.find({})
for row in rows:
  print(row)