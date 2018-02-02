import datetime


class Column(object):
    #实例化时获取传入的参数
    def __init__(self, column_name,ctype, null, unique, default,length=None):
        self.column_name=column_name
        self.ctype=ctype
        self.null=null
        self.unique=unique
        self.default=default
        self.length=length
        self.id=''

    #返回的返回值
    def go_back(self):
        return {'type': self.ctype, 'column_name': self.column_name, 'null': self.null,
                'unique': self.unique, 'default': self.default}

    # 清洗数据,得到正确的传入的值
    def get_data(self, data):
        # 清洗数据,都转变为字符串类型
        if isinstance(data, str):
            one_data = '"' + data + '"'
        elif isinstance(data,datetime.datetime):
            one_data=data.strftime("%Y-%m-%d %H:%M:%S")
            one_data = '"' + one_data + '"'
        else:
            one_data = str(data)
        return one_data

    #大于
    def big_than(self,data):
        #得到数据值
        data=self.get_data(data)
        #获得字段名字
        column_name=self.column_name
        #组合成新的字符串
        column_string=str(column_name)+' > '+str(data)
        return column_string

    #大于等于
    def big_and_equal(self,data):
        #字段名>=数据值
        data=self.get_data(data)
        column_name=self.column_name
        column_string=str(column_name)+' >= '+str(data)
        return column_string

    #小于
    def small_than(self,data):
        #字段名<数据值
        data = self.get_data(data)
        column_name = self.column_name
        column_string = str(column_name) + ' < ' + str(data)
        return column_string

    #小于等于
    def small_and_equal(self,data):
        #字段值<=数据值
        data = self.get_data(data)
        column_name = self.column_name
        column_string = str(column_name) + ' <= ' + str(data)
        return column_string

    #等于
    def equal(self,data):
        #字段值=数据值
        data = self.get_data(data)
        column_name = self.column_name
        column_string = str(column_name) + ' = ' + str(data)
        return column_string

    #不等
    def unequal(self,data):
        #字段值<>数据值
        data = self.get_data(data)
        column_name = self.column_name
        column_string = str(column_name) + ' <> ' + str(data)
        return column_string

    #以特定字符串开始
    def start_with(self,data):
        #字段值 like data%
        data = self.get_data(data)
        column_name = self.column_name
        column_string = str(column_name) + ' like ' + str(data)+'%'
        return column_string

    #以特定字符串结尾
    def end_with(self,data):
        #字段值 like %data
        data = self.get_data(data)
        column_name = self.column_name
        column_string = str(column_name) + ' like %' + str(data)
        return column_string

    #包含特定字符串
    def contain_with(self,data):
        #字段值 like %data%
        data = self.get_data(data)
        column_name = self.column_name
        column_string = str(column_name) + ' like %' + str(data)+'%'
        return column_string

    #修改字段的值
    def change_to(self,data):
        data=self.get_data(data)
        column_name = self.column_name
        column_string = str(column_name) + ' = ' + str(data)
        return column_string

    #添加字段的新值
    def add_new(self,data):
        new_data=self.get_data(data)
        column_name = self.column_name
        new_data_list=[]
        new_data_list.append(column_name)
        new_data_list.append(new_data)
        return new_data_list

    #更改字段名称:
    # def change_column(self, data):
    #     new_column_name=data
    #     column_name=self.column_name
    #     ctype=self.ctype
    #     null=self.null
    #     unique=self.unique
    #     default=self.default
    #     length=self.length
    #     if null:
    #         null = ''
    #     else:
    #         null = 'not null'
    #     # 判断字段是否唯一
    #     if unique:
    #         unique = 'unique'
    #     else:
    #         unique = ''
    #     # 判断字段是否有默认值
    #     if default:
    #         default = 'default "' + str(default) + '"'
    #     else:
    #         default = ''
    #     # 得到字段的长度,如果字段没有长度属性,则把长度属性设为none
    #     if length:
    #         length=str(length)
    #     else:
    #         length=''
    #     # 创建一个字段语句
    #     if ctype == 'VARCHAR':
    #         one_column_string = str(column_name) + ' ' +str(new_column_name)+' '+str(ctype) \
    #                             + '(' + str(length) + ') ' + ' ' + default + null + ' ' + unique
    #     else:
    #         one_column_string = str(column_name) + ' '+str(new_column_name)+' ' + str(ctype) \
    #                             + ' '+ default + null + ' ' + unique
    #     return one_column_string

    #更改表格的字段类型
    # def change_column_type(self,ctype,length=None, null=True, unique=False, default=None):
    #     column_name=self.column_name
    #     if null:
    #         null = ''
    #     else:
    #         null = 'not null'
    #     # 判断字段是否唯一
    #     if unique:
    #         unique = 'unique'
    #     else:
    #         unique = ''
    #     # 判断字段是否有默认值
    #     if default:
    #         default = 'default "' + str(default) + '"'
    #     else:
    #         default = ''
    #     # 得到字段的长度,如果字段没有长度属性,则把长度属性设为none
    #     if length:
    #         length=str(length)
    #     else:
    #         length=''
    #     # 创建一个字段语句
    #     if ctype == 'VARCHAR':
    #         one_column_string = str(column_name) +' '+str(ctype) \
    #                             + '(' + str(length) + ') ' + ' ' + \
    #                             default + null + ' ' + unique
    #     else:
    #         one_column_string = str(column_name)+' ' + str(ctype) \
    #                             + ' '+ default + null + ' ' + unique
    #     print(one_column_string)
    #     return one_column_string