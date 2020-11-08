# coding=UTF-8
import logging
import os.path
import time

#获取程序运行的错误，记得加上当前运行的文件名
class Log:
    def __init__(self):
        pass

    @staticmethod
    def getLogger(self, logType, logInfo):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))[:-4]
        log_path = os.path.dirname(os.getcwd()) + '/logs/'
        log_name = log_path + rq + '.log'
        logfile = log_name
        fh = logging.FileHandler(logfile, mode='a')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        if logType == "debug":
            logger.debug(logInfo)
        elif logType == "info":
            logger.info(logInfo)
        elif logType == "warning":
            logger.info(logInfo)
        elif logType == "error":
            logger.info(logInfo)
        elif logType == "critical":
            logger.info(logInfo)

