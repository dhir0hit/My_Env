import pymongo

#client = pymongo.MongoClient("mongodb+srv://admin:admin123@cluster0.tgneiwg.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["myenv"]
# managerCollection = db["manager"]
notesCollection = db["notes"]

# i = managerCollection.find()
# for x in i:
#     print(x)
# a = managerCollection.find({"_id": "ObjectId('6382a4f6d03fc4d6c08cf528')"})
# print(a)

j = notesCollection.find()
for x in j:
    print(j)