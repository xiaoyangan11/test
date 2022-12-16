# 获取请求中数据
# response = requests.get('http://www.example.com') data = response.json()
#
# 准备再次请求参数
# params = {'param1': data['key1'], 'param2': data['key2']}
#
# 再次请求
# response = requests.get('http://www.example.com', params=params)
#
#
# -*- coding:utf-8 -*-
import requests

url = 'https://api.uyiban.com'  # 登录


Name = '循环测试009'   # 设置 循环规则名称 和 循环项目名称 同名


ProjectId = Id ='141bb2bb9cf443702c8588cd572fa886' # 获取最新一条id后  输入上去

def login():
    '''登录'''
    entrance = '/base/admin/login/passLogin'
    parameter = {'mobile': '18059039677',
                 'password': 'c3b5a5687344c4311227428987e9f390'}
    request = requests.post(url + entrance, parameter)
    if request.json()['code'] == 0:
        print("登录成功")
    else:
        print("登录失败%s" % (request.json()))
    cookies = request.cookies
    return cookies


def chaojiliucheng(Name):
    entrance = '/superProcess/admin/project/add'
    parameter = {
        'IsCycleRule':'1',
        'Name':Name,   # 循环规则名称
        'TaskNameRule[0][type]':'date',
        'TaskNameRule[1][type]':'fixed',
        'TaskNameRule[1][value]':Name,  # 循环项目名称 和 循环规则名称相同
        'IsNotice':'1',
        'NoticeMode':'1',
        'ReadingTime':'0',
        'Notice':'<p>项目须知</p>',
        'LoopWeek':'{"Mon":1,"Tue":1,"Wed":1,"Thu":1,"Fri":1,"Sat":1,"Sun":1}',
        'StartDate':'2022-12-16',
        'EndDate':'2022-12-30'
        }
    request1 = requests.post(url + entrance, parameter, cookies=login())

    if request1.json()['code'] == 0:
        print(parameter['Name'], '创建成功',  request1.json())
    else:

        print(parameter['Name'], '创建失败,%s' % (request1.json()['msg']))

def get_formid():
    entrance = '/superProcess/admin/project/list?IsCycleRule=1&CSRF=fa476a3e6df7c37433e4e8d70d17d9ea'
    parameter = {}  # 默认第一页,数据只有10条  需要加入 page: 1  pageSize: 10  参数 来修改
    request1 = requests.get(url + entrance, parameter, cookies=login())

    data_list = request1.json()['data']['list'][0:1]   # 获取最新 x 条记录  最大设置为10,[0:10]. 默认为第一页 [0:1]为最新一条数据

    for item in data_list:
        print(item)

def publish_subprojects(ProjectId):            # 只写负责人扫码  其他同理
    entrance = '/superProcess/admin/subProject/add'
    parameter = {
        'Type': '1',
        'Name': '子项目测试固定名称',
        'applyRule[Person][IdSet][0]': 'a8db125497f67cc53ebcc9d8407443c3',
        'applyRule[Label]': '人员【王文(1589)】',
        'Remark': '<p>备注</p>',
        'StartTime': '2022-12-16 9:02:45',
        'EndTime': '2022-12-19 17:32:46',
        'ReceiveRule': '{"Person":{"IdSet":["a8db125497f67cc53ebcc9d8407443c3"]},"Label":"人员【王文(1589)】"}',
        'ProjectId': ProjectId  # 设置 形参为ProjectId 和 id 相同

    }
    request2 = requests.post(url + entrance, parameter, cookies=login())
    if request2.json()['code'] == 0:
        print(parameter['Name'], '创建成功', request2.json())
    else:

        print(parameter['Name'], '创建失败,%s' % (request2.json()['msg']))

def fbjsr(Id):
    entrance = '/superProcess/admin/project/publish'
    parameter = {

        'Id':Id, # 设置 形参为ProjectId 和 id 相同


        'ReceiveRule':'{"Organization":{"StudentAttr":{"Gender":[],"Grade":[],"Campus":[],"EducationLevel":[],"State":["1"]},"PersonType":"all","IdSet":["8e68fb0220be618d98c3f3606ed95174"]},"Label":"全校政工和在读学生"}'
        

    }
    request3 = requests.post(url + entrance, parameter, cookies=login())
    if request3.json()['code'] == 0:
        print( '发布人设置成功', request3.json())
    else:

        print('发布人设置失败,%s' % (request3.json()['msg']))



login()

chaojiliucheng(Name) # 创建循环规则

get_formid()  # 获取创建的最新表单

publish_subprojects(ProjectId)   # 创建子项目

fbjsr(Id)  # 创建发布人
