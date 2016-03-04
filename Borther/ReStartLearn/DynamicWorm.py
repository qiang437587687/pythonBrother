#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import re

print('想要抓取动态的数据 (js加载的数据)')




def getComment(realurl):
    # 上面这个是获取数据后解析的过程
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64)' \
                          ' AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/43.0.2357.130 Safari/537.36'}
    # strurl = 'http://coral.qq.com/article/1165021596/comment?commentid=0&reqnum=50'
    jscontent = requests.get(realurl, headers=head).content.decode()  # content 后面加上这个decode()才行要不显示的是 byte 解析不出来
    jsdict = json.loads(jscontent)
    jsdata = jsdict['data']
    comments = jsdata['commentid']
    for each in comments:
        print(each['content'])


# 解析对应的数据 返回一个json 字符串
'''
json1 = re.split('[re]', jsonStr)
# str(字符串).split(x) 后面的x 中是分割的符号 貌似不能多个一起用
# [] 中的每一个字符都当做是分割用的字符 这估计还需要在看一下 re 里面的东西
'''


def ParseJson(jsonstr):    # 解析出对应的json串
    json1 = re.split('[=;]', jsonstr)  # str.split(x) 后面的x 中是分割的符号 貌似不能多个一起用
    print(json1)
    return json1[1]


# 获取对应的commentid

def GetCommentID(commenturl):
    jsonconent = requests.get(commenturl).content.decode()  # .content 是获取其中二进制内容 .decode() 转换为了 json 字符串.
    jsonstr = ParseJson(jsonconent)
    commentid = json.loads(jsonstr)['comment_id']
    return commentid



def getVid(sourceurl):
    # vid 其实上面的网址里面就包含了这个了为了练习,去源代码中获取对应的一个 vid
    html = requests.get(sourceurl)
    # print(html.text)
    # 正则去匹配一下  chinese = re.findall(tr, html.text, re.S) vid:"n0016ibg4eb",
    tr = r'vid:"(.*?)"'
    vidList = re.findall(tr, html.text, re.S)
    # print(vidList[0])
    vid = vidList[0]
    return vid

def realCommentUrl(commentId):
    return 'http://coral.qq.com/article/%s/comment?commentid=0&reqnum=50' % commentId




# 待获取目标
sourceUrl = 'http://v.qq.com/cover/e/e4uer5m850721h8.html?vid=j0164r2thel'

vid = getVid(sourceUrl)

# http://ncgi.video.qq.com/fcgi-bin/video_comment_id?otype=json&op=3&vid=   获取comment_id 的url

getCommentUrl = 'http://ncgi.video.qq.com/fcgi-bin/video_comment_id?otype=json&op=3&vid=%s' % vid
# print(getCommentUrl)

commentID = GetCommentID(getCommentUrl)

commentrealUrl = realCommentUrl(commentID)

getComment(commentrealUrl)






