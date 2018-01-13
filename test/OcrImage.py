#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aip import AipImageClassify
import json
""" 你的 APPID AK SK """
APP_ID = '10661527'
API_KEY = 'pxG2F0LuVx5i0iKM3laZUETG'
SECRET_KEY = '8iYhDOgswCD8q6bcXbFGHE4DhGZ9sSwh '

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(r'C:\Users\user98\Desktop\meishi.jpg')

# """ 调用菜品识别 """
# json1=client.dishDetect(image)[u'result']
# for str in json1:
#     print str['name']
""" 如果有可选参数 """
options = {}
options["top_num"] = 1

""" 带参数调用菜品识别 """
json = client.dishDetect(image, options)[u'result']
for str in json:
    print str['name']

image2 = get_file_content(r'C:\Users\user98\Desktop\car.jpg')
optionscar = {}
optionscar["top_num"] = 1
json2 = client.carDetect(image2, optionscar)[u'result']
for str in json2:
    print str['name']