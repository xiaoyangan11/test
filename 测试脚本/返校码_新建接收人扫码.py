# -*- coding:utf-8 -*-
import requests

url = 'https://api.uyiban.com'  # 登录


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


login()


def jieshouresaoma():
    entrance = '/scanSignIn/admin/notice/add'
    parameter = {
        'ScanPersonType': '2',
        'Title': '接收人扫码-1',
        'PubOrgId': 'de6c68ce91a745dce6d22b600eecf199',
        'ApplyRule': '{"label":"全校政工和在读学生","Organization":{"StudentAttr":{"Gender":[],"Grade":[],"Campus":[],"EducationLevel":[],"State":["1"]},"PersonType":"all","IdSet":["8e68fb0220be618d98c3f3606ed95174"]}}',
        'ManageRule': '{"label":"角色【辅导员】","Role":{"IdSet":["9a4fe048146fd925f75b62a30126fcb1"]}}',
        'Content': '<p>嘿嘿嘿</p>',
        'StartTime': '2022-11-21 09:20:07',
        'EndTime': '2022-11-30 09:20:09'
    }
    request1 = requests.post(url + entrance, parameter, cookies=login())
    if request1.json()['code'] == 0:
        print(parameter['Title'], '创建成功')
    else:
        print(parameter['Title'], '创建失败,%s' % (request1.json()['msg']))


jieshouresaoma()

