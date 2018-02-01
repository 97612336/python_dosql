import datetime

import pymysql


class Do_mysql(object):
    # 在初始化的时候链接数据库,并获取游标对象
    def __init__(self, ip, name, password, db_name, charset='utf8'):
        # 确定数据库的主机地址,用户名,密码,数据库名,默认的字符集编码
        self.db = pymysql.connect(ip, name, password, db_name, charset=charset)
        self.cursor = self.db.cursor()
        # 这个是规定的字段类型
        self.column_type = ['int', 'float', 'string', 'text', 'boolean', 'file', 'datetime']

    # 创建字段类,其中的方法用于创建特定的字段
    class create_column(object):
        # int类型的字段
        @classmethod
        def int(cls, column_name, null=True, unique=False, default=None):
            return {'type': 'BIGINT', 'column_name': column_name, 'null': null,
                    'unique': unique, 'default': default}

        # float类型的字段
        @classmethod
        def float(cls, column_name, null=True, unique=False, default=None):
            return {'type': 'DOUBLE', 'column_name': column_name, 'null': null,
                    'unique': unique, 'default': default}

        # string类型的字段
        @classmethod
        def string(cls, column_name, length, null=True, unique=False, default=None):
            return {'type': 'VARCHAR', 'column_name': column_name, 'length': length,
                    'null': null, 'unique': unique, 'default': default}

        # 大文本类型
        @classmethod
        def text(cls, column_name, null=True, unique=False, default=None):
            return {'type': 'TEXT', 'column_name': column_name,
                    'null': null, 'unique': unique, 'default': default}

        # 布尔值类型的字段
        @classmethod
        def boolean(cls, column_name, null=True, unique=False, default=None):
            return {'type': 'BOOLEAN', 'column_name': column_name,
                    'null': null, 'unique': unique, 'default': default}

        # 文件类型的字段
        @classmethod
        def file(cls, column_name, null=True, unique=False, default=None):
            return {'type': 'BOOLEAN', 'column_name': column_name,
                    'null': null, 'unique': unique, 'default': default}

        # 时间类型的字段
        @classmethod
        def datetime(cls, column_name, null=True, unique=False, default=None):
            return {'type': 'DATETIME', 'column_name': column_name,
                    'null': null, 'unique': unique, 'default': default}

    ##############################################################
    ##                                                          ##
    ##                  内置方法开始..                             ##
    ##                                                          ##
    ##############################################################

    # 得到字段的所有信息:
    def get_columns(self, column_list):
        a=column_list
        if not isinstance(column_list,list):
            raise Exception('传入的字段必须是列表')
        columns_list = []
        # 遍历每一个元素,创建每一个元素
        for one_column in column_list:
            # 获得这个元素
            name = one_column['column_name']
            ctype = one_column['type']
            # 判断字段是否是null值
            null = one_column['null']
            if null:
                null = ''
            else:
                null = 'not null'
            # 判断字段是否唯一
            unique = one_column['unique']
            if unique:
                unique = 'unique'
            else:
                unique = ''
            # 判断字段是否有默认值
            default = one_column['default']
            if default:
                default = 'default "' + str(default) + '"'
            else:
                default = ''
            # 得到字段的长度,如果字段没有长度属性,则把长度属性设为none
            try:
                length = one_column['length']
            except:
                length = None
            # 创建一个字段语句
            if ctype == 'VARCHAR':
                one_column_string = str(name) + ' ' + str(ctype) + '(' + str(
                    length) + ') ' + ' ' + default + null + ' ' + unique
            else:
                one_column_string = str(name) + ' ' + str(ctype) + ' ' \
                                    + default + null + ' ' + unique
            # 把这个字段添加到列表中
            columns_list.append(one_column_string)
        return columns_list

    #得到字段的所有字段名称:
    def get_columns_name(self,column_list):
        # 得到所有字段
        column_list2 = self.get_columns(column_list)
        # 得到每个字段名称
        column_names_list = []
        for one_column in column_list2:
            column_name = one_column.split(' ')[0]
            column_names_list.append(column_name)
        return column_names_list

    #执行sql语句的方法
    def run_sql(self,sql):
        # 执行sql语句
        try:
            #执行sql语句
            self.cursor.execute(sql)
            #返回查询结果
            result=self.cursor.fetchall()
            # 提交请求
            self.db.commit()
            #如果结果的长度为0,则返回运行成功
            if len(result)==0:
                result='运行成功'
            return result
        except Exception as e:
            self.db.rollback()
            raise e

    # 清洗数据,得到正确的传入的值
    def get_data(self, data_list):
        # 清洗数据,都转变为字符串类型
        new_list = []
        for one_data in data_list:
            if isinstance(one_data, str):
                one_data = '"' + one_data + '"'
            elif isinstance(one_data,datetime.datetime):
                one_data=one_data.strftime("%Y-%m-%d %H:%M:%S")
                one_data = '"' + one_data + '"'
            else:
                one_data = str(one_data)
            new_list.append(one_data)
        return new_list

    #清洗单个数据

    #得到字段名字和判断条件的一一对应关系
    def get_column_and_condition(self,column_list,condition_list):
        # 得到所有的字段名字
        column_names = self.get_columns_name(column_list)
        if len(column_list)!=len(condition_list):
            raise Exception('字段列表长度要和判断列表长度相同')
        # #把字段列表和条件列表建立一一对应的关系
        condition_dict={}
        for i in range(0,len(condition_list)):
            condition_dict[column_names[i]]=condition_list[i]
        return condition_dict



    ##############################################################
    ##                                                          ##
    ##                  表格语句开始..                             ##
    ##                                                          ##
    ##############################################################

    # 创建数据表的方法:
    def create_table(self, table_name, columns):
        #得到字段组成的列表
        columns_list=self.get_columns(columns)
        #把列表中的每个元素重新组合成新的字符串
        columns_string=','.join(columns_list)
        #去除总的字段语句中最后一个逗号
        # columns_string=columns_string[:-1]
        #写sql语句
        sql='create table '+str(table_name)+'('+'id BIGINT primary key auto_increment,' \
            +columns_string+');'
        result=self.run_sql(sql)
        return result

    #查看表格的信息
    def desc_table(self,table_name):
        sql='desc '+str(table_name)+';'
        res=self.run_sql(sql)
        print(res)

    #增加表的字段
    def add_table_column(self,table_name,column_list):
        #得到所有字段
        column_list=self.get_columns(column_list)
        columns=',add '.join(column_list)
        columns_string='add '+columns
        sql='alter table '+str(table_name)+' '+columns_string+';'
        return self.run_sql(sql)

    #删除表的字段
    def delete_table_column(self,table_name,column_list):
        #得到每个字段名称
        column_names_list=self.get_columns_name(column_list)
        #组成新的字符串字段
        columns_string=',drop '.join(column_names_list)
        sql='alter table '+str(table_name)+' drop '+columns_string+';'
        return self.run_sql(sql)

    #更改表格的字段类型
    def change_table_column_type(self, table_name, column_list):
        # 得到所有字段
        column_list = self.get_columns(column_list)
        columns=[]
        #重组为新的string
        for one_column in column_list:
            one_column='modify '+one_column
            columns.append(one_column)
        columns_string=','.join(columns)
        sql='alter table '+str(table_name)+' '+columns_string+';'
        #执行sql
        return self.run_sql(sql)

    #更改表格字段名称
    def change_table_column_name(self,table_name,column_list,new_column_list):
        # 得到所有字段名称
        column_list = self.get_columns_name(column_list)
        #得到所有新的字段
        new_column_list=self.get_columns(new_column_list)
        #判断长度是否相等
        if len(column_list)!=len(new_column_list):
            raise Exception('传入的两个列表长度不一样')
        #遍历第一个列表和第二个列表,得到其中的值,并组合成一个新的字典
        columns_string=[]
        for i in range(0,len(column_list)):
            new_string=str(column_list[i])+' '+str(new_column_list[i])
            columns_string.append(new_string)
        #组合成一个新的字符串
        new_columns_string=',change '.join(columns_string)
        sql='alter table '+str(table_name)+' change '+new_columns_string+';'
        return self.run_sql(sql)

    #更改表格名字
    def change_table_name(self,old_name,new_name):
        sql='alter table '+str(old_name)+' rename to '+str(new_name)
        return self.run_sql(sql)

    #删除指定表格
    def delete_table(self,table_name):
        sql='drop table '+str(table_name)
        return self.run_sql(sql)


    ##############################################################
    ##                                                          ##
    ##                  数据语句开始..                             ##
    ##                                                          ##
    ##############################################################

    #指定表名,插入所有数据
    def add_data(self,table_name,data_list):
        #得到数据
        data_list=self.get_data(data_list)
        column_string=','.join(data_list)
        sql='insert into '+str(table_name)+' values(0,'+column_string+');'
        #执行sql语句:
        return self.run_sql(sql)

    #根据表明和特定字段名,插入指定数据
    def add_adta_by_columns(self,table_name,column_list,data_list):
        #得到字段的所有字段名
        column_names=self.get_columns_name(column_list)
        #得到数据
        data=self.get_data(data_list)
        # insert
        # into
        # 表格名称(字段名称，字段名称)  values(数据，数据);
        columns=','.join(column_names)
        datas=','.join(data)
        sql='insert into '+str(table_name)+' ('+columns+') values ('+datas+');'
        #执行sql语句
        return self.run_sql(sql)

    #查询表格的所有数据
    def query_all_data(self,table_name):
        # select *
        # from    表格名称;
        sql='select * from '+str(table_name)
        return self.run_sql(sql)

    #查询表格执行字段的所有数据
    def query_all_data_by_columns(self,table_name,column_list):
        #得到所有字段的名字
        columns=self.get_columns_name(column_list)
        # select
        # 字段名称, 字段名称
        # from   表格名称;

        #组合成新的字段
        columns_string=','.join(columns)
        sql='select '+columns_string+' from '+str(table_name)
        #执行sql语句
        return self.run_sql(sql)

    #根据指定条件查询
    def query_by_equal_condition_or(self,table_name,column_list,condition_list):
        #得到字段名字
        column_name_list=self.get_columns_name(column_list)
        #得到条件配对
        condition_dict=self.get_column_and_condition(column_list,condition_list)
        # select *
        # from  表格名称  where
        # 字段名称 = 数据 and / or 字段名称 = 数据;

        #遍历字典,然后组成新的查询条件:
        for key,value in condition_dict.items():
            #判断类型,然后省心字符串:
            # if isinstance()
            new_string=key+'='+value

