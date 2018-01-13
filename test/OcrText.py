#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aip import AipOcr

APP_ID='10661443'
API_KEY = 'oNYb8EkoSaT4N9epl8kNZcs2'
SECRET_KEY = 'kvQslIZu8kpkAHA42gPc6FmVPEWGER7u '

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
'''读取图片'''
def get_file_content(filepath):
    with open(filepath) as fp:
        return fp.read()
image = get_file_content(r'C:\Users\user98\Desktop\a.png')
'''文字识别'''
text = client.basicGeneral(image, options)
print text
