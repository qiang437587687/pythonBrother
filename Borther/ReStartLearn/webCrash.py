#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

在 python3 中 urllib 和 urllib2 合并到一起了 这个和 2.7 是不一样的

'''

# import urllib
# from urllib import request
# import os
# import threading

# body = urllib.request.urlopen('http://www.baidu.com')
# urllib.request.urlopen('http://www.baidu.com')
# print(body)


# target = 'www.handabao.com'
#
# directory = '/Users/zhangxianqiang/Desktop/webCrash'
#
# filters = ['.jpg', '.gif', 'png', '.css']

# os.chdir(directory)


print('韩大宝')

from scapy.all import *

def packet_callback(packet):
    print(packet.show())

sniff(prn=packet_callback, count=1)


# def mailpacket_callback(packet):
#     if packet['TCP'].payload:
#         mail_packet = str(packet['TCP'].payload)
#         if 'user' in mail_packet.lower() or 'pass' in mail_packet.lower():
#             print('[*] Server: %s' % packet['IP'].dst)
#             print('[*] %s' % packet['TCP'].payload)
#
# sniff(filter='tcp port 110 or tcp port 24 or tcp port 143', prn=mailpacket_callback, store=0)



