# coding=UTF-8
from Common.func import Common
class DBConfig:
    #数据库配置类
    def __init__(self):
        pass
    def getDbInfo(self):
        cfInfo = Common.get_conf_info("config\db_config.ini")
        return cfInfo

# db = DBConfig()
# cfInfo = db.getDbInfo()
# print(cfInfo["host"]["host"])


