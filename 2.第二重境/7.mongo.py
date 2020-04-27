import pymongo

myclinet = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclinet["rnnoodbd"]

# dblist = myclinet.list_database_names()
# if "rnnoodbd" in dblist :
#     print("数据库已存在！")
mycol = mydb["sites"]

# mydict = {"name":"runoob","alexa":"10000","rul":"http:hahah.com"}
# x = mycol.insert_one(mydict)
# print(x.inserted_id)

# mylist = [
#     {"name":"runoob","alexa":"10000","rul":"http:hahah.com"},
#     {"name":"TAobo","alexa":"10001","rul":"http:taobao.com"},
#     { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
#     { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
#     { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
#     { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
# ]
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)

# mylist = [
#   { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
#   { "_id": 2, "name": "Google", "address": "Google 搜索"},
#   { "_id": 3, "name": "Facebook", "address": "脸书"},
#   { "_id": 4, "name": "Taobao", "address": "淘宝"},
#   { "_id": 5, "name": "Zhihu", "address": "知乎"}
# ]

# x = mycol.insert_many(mylist)
# print(x.inserted_ids)

# x = mycol.find_one()
# print(x)

# for x in mycol.find():
#     print(x)

# for x in mycol.find({},{ "alexa": 1 }):
#   print(x)

# myquery = {"alexa":"10000"}
# newvalues ={"$set":{"alexa":"12345"}}

# mycol.update_many(myquery,newvalues)
# for x in mycol.find():
#     print(x)

# mydoc = mycol.find().sort("alexa",-1)
# for x in mydoc:
#   print(x)


myquery ={"name":{"$regex":"^T"}}
x=mycol.delete_many(myquery)
print(x.deleted_count,"个文档已删除")
for x in mycol.find():
    print(x)
