from do_mysql.Do_mysql import Do_mysql

dm=Do_mysql('localhost','root','root123456','test',charset='utf8')

age=dm.create_column.int('age3')
name=dm.create_column.string('name3',20)

new_age=dm.create_column.int('age1')
new_name=dm.create_column.string('name1',50)

# dm.create_table('hahu2',(age,name))

# result=dm.add_table_column('hahu2',(age,name))
# print(result)

# resu=dm.delete_table_column('hahu2',(age,name))
# print(resu)

# resu=dm.change_table_column_type('hahu2', (age, name))
# print(resu)

# dm.change_table_column_name('hahu2',[age,name],[new_age,new_name])

res=dm.change_table_name('hahu2','new_hahu')
print(res)