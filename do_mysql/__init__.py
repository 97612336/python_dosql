import datetime


class Column(object):
    #实例化时获取传入的参数
    def __init__(self, column_name,ctype, null=True, unique=False, default=None):
        self.column_name=column_name
        self.ctype=ctype
        self.null=null
        self.unique=unique
        self.default=default
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