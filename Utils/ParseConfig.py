#coding:utf-8
from Base.Paths import Path
from configparser import ConfigParser
from Utils.Logger import Logger
import os

#获取配置文件信息
class ParseConfig:
    log = Logger(logger='ParseConfig获取配置文件信息').getlog()


    def __init__(self, fileType):
        self.log.info('获取配置文件信息')
        #获取配置文件信息
        self.conf = ConfigParser()
        # self.conf.read('F:/SeleniumProject/config/config.ini', encoding='utf-8')
        self.conf.read(Path.getPath(fileType), encoding='utf-8')


    def log_config(self):
        dictData = {}
        sections = self.conf.sections()
        itemList = []
        [itemList.append(dict(self.conf.items(item))) for item in sections]
        for index1, value1 in enumerate(sections):
            for index2, value2 in enumerate(itemList):
                if index1 == index2:
                    dictData.update({value1: value2})
        try:
            return dictData
        except Exception as e:
            self.log.exception('[ConfigFileException]:', exc_info=True)