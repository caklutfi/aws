import pymongo

client = pymongo.MongoClient("mongodb+srv://caklutfi:toshibaC840.@cluster0.rmbyfax.mongodb.net/?retryWrites=true&w=majority")
db = client.caklutfi
collection = db.clients

data = {"username":"caklutfi",
        "address":"gresik",
        "col12":"kosong",
        "col14":"kosong",
        "date":"2023 10 10",
        "email":"lutfytalker@gmail.com",
        "file":"jpeg",
        "name":"lutfi",
        "password":"password",
        "phone":"089514220808",
        "service":"package",
        "time":"13.30"}

# collection.insert_one(data)
# for i in collection.find({}):
#     print(i)

result= collection.find_one({"username": "caklutfi"})
print(result)