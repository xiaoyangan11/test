import requests
def cs():
    '''离返校'''
    url='https://open.uyiban.com/scanSignIn/signv1/confirm'
    parameter={
        'sign':'5d4aaa2a4fe80424dbbd80eed4b2df35',  # md5 转换  albert加上当前日期 例如 albert20221808
        'Key':'25be75d6219d7ff596a1a9cc1baa6bc2',   # 取 返校码 - 设备码 f12 里 guid 的参数
        'appId': 'albert'
        }
    request=requests.post(url,parameter)
    print(request.json())
cs()