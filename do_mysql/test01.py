import datetime

# 得到所有字段信息,并组合成一个新的字符串
#         new_string=',change '.join(new_column_list)
#         sql='alter table '+str(table_name)+' change '+new_string
#         return self.run_sql(sql)

from do_mysql import Column
from do_mysql.Do_mysql import Do_mysql

dm=Do_mysql('localhost','root','root123456','test',charset='utf8')

age=dm.create_column.int('age123')
name=dm.create_column.string('name123',20)
time=dm.create_column.datetime('time',default='')
new_age=dm.create_column.int('age123')
new_name=dm.create_column.string('name1',50)

# age.change_column_type([age])

# res=dm.change_table_column_name('hahu3',[age],[new_age])
# print(res)

# age.change_column_name('age')
# name.change_column_name('name')

# res=dm.change_table_column_name('hahu3', [age.change_column('age12'), name.change_column('name123')])
# print(res)

# res=dm.add_data('hahu3',[age.add_new(123),name.add_new('还是牛逼')])
# print(res)

# res=dm.change_table_column_name('hahu3',[age],['age'])
# print(res)

# res=dm.change_by_condition('hahu3',[age.equal(2)],[name.change_to('真牛逼'),new_name.change_to('123')])
# print(res)

# age.change_data(123)

# res=dm.delete_by_condition('hahu3',[age.equal(190)])
# print(res)

res=dm.query_by_condition('hahu3',[age.big_than(1),age.small_than(190)])
print(res)

res=dm.query_by_id('hahu3',1)
print(res)

# res=age.contain_with('123')
# print(res)

# res=dm.query_by_equal_condition_or('hahu3',[age,name,name],[1,'小明','ceshi'])
# print(res)

# res=dm.query_all_data_by_columns('hahu3',[age,name])
# print(res)

# dm.add_data('hahu3',(18,'lisi','zhangsan'))

# res=dm.query_all_data('hahu3')
# print(res)
# for one in res:
#     print(one)

# res=dm.add_data_by_columns('hahu3', [age, name], [2, '牛逼不牛逼?123'])
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