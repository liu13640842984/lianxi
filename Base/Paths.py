#coding:utf-8
import os
from Utils.Logger import Logger


# 获取配置文件路径的类
class Path(object):
    log = Logger(logger='Paths获取配置文件路径').getlog()
    # log.info('获取配置文件路径')
    dirName = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


    def __init__(self):
        pass

    @classmethod
    def getPath(self,fileType):
        self.log.info('获取配置文件路径')
        if fileType == 'File':
            config = 'config\config.ini'
        elif fileType == 'browser':
            config = 'config\browser.ini'
        else:
            config = 'config\database.ini'

        # config = "config\config.ini" if fileType =="File" else "config\database.ini"
        filePath = os.path.join(self.dirName, config)
        try:
            return filePath
        except Exception as e:
            self.log.exception('[FilePathException]:', exc_info=True)