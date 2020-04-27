import pymysql

## 创建 数据库__________________________
# db = pymysql.connect(host = '127.0.0.1',user = 'root',password = '1234',port = 3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('database version:',data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

## 创建 表__________________________

# db = pymysql.connect(host = '127.0.0.1',user = 'root',password = '1234',port = 3306,db = 'spiders')
# cursor =  db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) not null, name varchar(255) not null ,age int not null,primary key (id))'
# cursor.execute(sql)
# db.close()

## 插入数据__________________________


# id  = '20000001'
# user = 'Bob'
# age = 20

# db = pymysql.connect(host = '127.0.0.1',user = 'root',password = '1234',port = 3306,db = 'spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students (id,name,age) values (%s,%s,%s)'
# try:
#     cursor.execute(sql,(id,user,age))
#     db.commit()

# except:
#     db.rollback()
# db.close()

# db = pymysql.connect(host = '127.0.0.1',user = 'root',password = '1234',port = 3306,db = 'spiders')
# cursor = db.cursor()
# data = {
#     'id':'20120005',
#     'name':'阿第三方',
#     'age':24
# }
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s']*len(data))
# sql = 'insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close

## 更新数据__________________________

db = pymysql.connect(host = '127.0.0.1',user = 'root',password = '1234',port = 3306,db = 'spiders')
cursor = db.cursor()
# data = {
#     'id' :'20120002',
#     'name' :'hi',
#     'age' : 21
# }

# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))

# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
# update = ','.join([" {key} = %s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values())*2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

## 删除 __________________________

# table = 'students'
# condition = 'age>20'
# sql = 'delete from {table} where {condition}'.format(table=table,condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()

##查询__________________________

# sql = 'select * from students where age >= 20 '

# try:
#     cursor.execute(sql)
#     print('count:',cursor.rowcount)
#     one = cursor.fetchone()
#     print('one:',one)
#     results = cursor.fetchall()
#     print('results:',results)
#     print('results type:',type(results))
#     for row in results:
#         print(row)
# except:
#     print('Error')

## 查询所有数据

sql = 'select * from students where age >= 20'
try:
    cursor.execute(sql)
    print('count:',cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('row:',row)
        row=cursor.fetchone()
except:
    print('Error')