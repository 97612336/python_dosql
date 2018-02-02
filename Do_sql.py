from do_mysql.Do_mysql import Do_mysql


class Do_sql(object):
    def __init__(self, ip, name, password, db_name, charset='utf8'):
        self.dm=Do_mysql(ip,name,password,db_name,charset)




