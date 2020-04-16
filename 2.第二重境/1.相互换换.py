# 1. json字符串，dict，对象，之间的相互转换

'''
loads()：将json-- ->dict数据
dumps()：将dict-- ->json数据
load()：读取json文件数据，转成dict数据
dump()：将dict数据转化成json数据后写入json文件
eval():将字典格式的字符串-- ->dict,语法：eval(expression[, globals[, locals]])
vars():蒋object-- ->dict
object无法直接与json转化，只能先将object转化成dict，再转化成json；对json，也只能先转换成dict，再转化成object
object.__dict__:   dict -- ->object,python对象默认都有一个私有的属性dict,取值就是object的字典形式， 赋值就就可以给对象属性对应赋值

'''

import json
#dict_to_json
dict ={}
dict["name"] ="mary"
dict["age"] = 10
dict["sex"] = "male"
print("dict:%s"%dict)
j = json.dumps(dict)
print("dict_to_json:%s"%j)

#json_to_dict
j ='{"name":"many","age":10,"sex":"male"}'
dict = json.loads(j)
print("json:%s"%j)
print("json_to_dict:%s"%dict)

# 字符串转dict
str_1 = "{'name':'mary2','age':'11','sex':'male'}"
dict_1 = eval(str_1)
print(type(dict_1))
print(dict_1)

# json和object之间的转换

class MyClass:
    def __init__(self):
       self.a = 2
       self.b = "bb"

myclass = MyClass()
myclass.c = 123
myclass.a = 1
myclass_Dict = myclass.__dict__
print("myclass_Dict的数据类型是：%s"%type(myclass_Dict))
print("myclass_Dict：%s"%myclass_Dict)
myclass_json= json.dumps(myclass_Dict)
print("myclass_json的数据类型是：%s"%type(myclass_json))
print("myclass_json：%s"%myclass_json)

myclass_dict2 = json.loads(myclass_json)
print("myclass_dict2的数据类型是：%s"%type(myclass_dict2))
print("myclass_dict2：%s"%myclass_dict2)
myclass2=MyClass()
myclass2.__dict__ = myclass_dict2
print(myclass2.a)
