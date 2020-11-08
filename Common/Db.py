# coding=UTF-8
# https://blog.csdn.net/weixin_42213622/article/details/86523400
# https://www.cnblogs.com/superhin/p/10338985.html,公共数据库操作类


import pymysql
from Common.dbConfig import DBConfig

class DB:
    def __init__(self):
        db = DBConfig()
        cfInfo = db.getDbInfo()
        host = cfInfo["host"]["host"]
        port = cfInfo["port"]["port"]
        user = cfInfo["user"]["user"]
        passwd = cfInfo["passwd"]["passwd"]
        db = cfInfo["db"]["db"]
        self.conn =  pymysql.connect(host=host,
                        port=port,
                        user=user,
                        passwd=passwd,
                        db=db)
        self.cur = self.conn.cursor()


    def __del__(self):
        self.cur.close()
        self.conn.close()


    def queryDb(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()


    def execDb(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print('Db Error',format(e))


    #检查用户是否存在
    def check_user(self, name):
        result = self.query("select * from user where name='{}'".format(name))
        return True if result else False


    def del_user(self, name):
        self.execDb("delete from user where name='{}'".format(name))