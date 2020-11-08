# coding=UTF-8
# https://www.cnblogs.com/superhin/p/10338915.html
# https://www.cnblogs.com/superhin/p/10338993.html
# 组装请求——>发送请求，获取相应——>解释相应

'''
从post 或 get请求的返回数据中，需将返回的字符串转成json 或 dict格式
data=json.loads(data)  //将字符串转成json格式，或
data=eval(data)  //将字符串转成dict格式。
'''


from Common import func
import json

testCommon = func()
url = "http://httpbin.org/post"
data = {"name": "hanzhichao", "age": 18}
testCommon.testRequest('post', url, data)
