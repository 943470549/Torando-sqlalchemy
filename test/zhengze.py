import re
str=r'010-12345'
print str
print re.match(r'\d{3}\-\d{3,8}(5)$',str)

if __name__=='__main__':
    print(' ')