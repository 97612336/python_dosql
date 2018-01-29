from do_mysql.Do_mysql import Do_mysql

dm=Do_mysql('localhost','root','root123456','test',charset='utf8')

age=dm.create_column.int('age',null=False)
name=dm.create_column.string('name',20,default='hahah',unique=True)

dm.create_table('ceshi',(age,name))
