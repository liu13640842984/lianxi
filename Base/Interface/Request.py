# coding=UTF-8
import requests
import json

#公共的Request类
class Request(object):
    def __init__(self):
        # data = {step_infos: {'请求方式': get, '请求参数': {'A': 11}}}
        pass


    def requestFun(self, method, url, params):
        '''
        :param method:请求方式
        :param url: 访问地址
        :param data: 传入参数，一般为字典类型
        :return:
        '''
        if method == 'get':
            # headers = {'Content-Type': 'application/json', 'session': XXXXX}  # 消息头，根据实际需要添加
            return requests.get(url, params=params)

        elif method == 'options':
            res = requests.options(url)

        elif method == 'head':
            res = requests.head(url)

        elif method == 'post':
            data = str(params).replace("'", '"').replace('\\', '\\\\')
            if self.is_json(data):
                res = requests.post(url=url, json=params)
            res = requests.post(url, params)

        elif method == 'put':
            res = requests.put(url,params)

        elif method == 'patch':
            res = requests.patch(url, params)

        elif method == 'delete':
            res = requests.delete(url)


    def is_json(self, params):

        '''
        是否为json字符串
        :return:
        '''
        try:
            jsonData = json.loads(params)
        except ValueError as e:
            return False
        return True