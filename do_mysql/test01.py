import datetime

from do_mysql.Do_mysql import Do_mysql

dm=Do_mysql('localhost','root','root123456','test',charset='utf8')

age=dm.create_column.int('age3')
name=dm.create_column.string('name3',20)
time=dm.create_column.datetime('time',default='')
new_age=dm.create_column.int('age1')
new_name=dm.create_column.string('name1',50)

dm.query_by_equal_condition_or('hahu3',[age,name],[1,'小明'])

# res=dm.query_all_data_by_columns('hahu3',[age])
# print(res)

# dm.add_data('hahu3',(18,'lisi','zhangsan'))

# res=dm.query_all_data('hahu3')
# print(res)
# for one in res:
#     print(one)

# res=dm.add_adta_by_columns('hahu3',(age,name),(2,'牛逼不牛逼?'))
# print(res)

# result=dm.add_data('hahu3',(190,'小明','大名'))
# print(result)

#测试循环插入数据
# for i in range(0,100):
#     result = dm.add_data('hahu3', (190, '小明', '大名'))
#     print(str(result)+str(i))

# dm.desc_table('hahu')

# res=dm.create_table('hahu5',(age,name,new_name,time))
# print(res)

# result=dm.add_table_column('hahu2',(age,name,new_name))
# print(result)

# resu=dm.delete_table_column('hahu2',(age,name))
# print(resu)

# resu=dm.change_table_column_type('hahu2', (age, name))
# print(resu)

# dm.change_table_column_name('hahu2',[age,name],[new_age,new_name])

# res=dm.change_table_name('hahu2','new_hahu')
# print(res)

# res=dm.delete_table('hahu2')
# print(len(res))