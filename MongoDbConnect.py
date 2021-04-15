import pymongo

mongocon =pymongo.MongoClient("mongodb://localhost:27017")

mydb=mongocon["mydatabase"]

mycol =mydb["customers"]

mydoc ={"name":"maanavan.com","course":"MongoDB Python"}

#insertmy =mycol.insert_one(mydoc)
x=mycol.find_one()
print(x)