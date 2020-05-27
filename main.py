from pymongo import MongoClient

url = 'mongodb://patrick:voxmflr1234@ds149593.mlab.com:49593/heroku_33krt5nm?retryWrites=false'
client = MongoClient(url)
db = client['heroku_33krt5nm']
collection = db['test']

# collection.insert_one({'name': 'bobby', 'age': 21})
# collection.insert_one({'name': 'kay', 'age': 27})
# collection.insert_one({'name': 'john', 'age': 30})
# collection.insert_one({'name': 'patrick', 'age': 72})

rows = collection.find({})

# collection.delete_many({'name':'bobby','age':21})

result = []

for row in rows:
  if 'age' in row: # 꼭 필요
    if row['age'] > 21 :
      result.append(row['age'])
# 이렇게 써야 공부가 됨 파이썬식

max_age = max(result)

rows = collection.find()

count_number = len(result)

for row in rows:
  if 'age' in row: 
    if row['age'] == max_age :
      print(count_number)

