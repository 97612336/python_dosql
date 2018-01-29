import pymysql

db=pymysql.connect('localhost','root','root123456','test',charset='utf8')
cursor=db.cursor()

sql='create table haha (haha VARCHAR (20));'

resul=cursor.execute(sql)

print(resul)

db.commit()

cursor.close()
db.close()