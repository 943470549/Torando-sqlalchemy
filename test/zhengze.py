import re
str=r'010-12345'
# print str
# print re.match(r'\d{3}\-\d{3,8}(5)$',str)

# print re.match(r'/[0-9a-zA-Z\_]+\.html','/index.html')
print re.match(r'/(.*)','index.html')