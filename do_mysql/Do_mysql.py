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

    # 创建数据表的方法:
    def create_table(self, table_name, columns):
        # 总的字段语句
        columns_string = ''
        # 遍历每一个元素,创建每一个元素
        for one_column in columns:
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
                default = 'default "' + str(default)+'"'
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
            #在字段语句的结尾处添加一个逗号
            one_column_string=one_column_string+','
            #把这个字段语句添加到总的语句中
            columns_string=columns_string+one_column_string
        #去除总的字段语句中最后一个逗号
        columns_string=columns_string[:-1]
        #写sql语句
        sql='create table '+str(table_name)+'('+'id BIGINT primary key auto_increment,'+columns_string+');'
        print(sql)
        #执行sql语句
        try:
            self.cursor.execute(sql)
            #提交请求
            self.db.commit()
            return '创建成功'
        except Exception as e:
            self.db.rollback()
            print(e)

    #创建表的方法
